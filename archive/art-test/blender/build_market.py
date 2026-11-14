"""Art test: Ladderfoot, storey 6 market. Run headless:
  blender -b -P build_market.py -- <out.glb>
Everything is built by code with bmesh; colour lives in a linear float vertex-colour layer "Col".
Blender axes: X right, Y back, Z up. Deck top is z = 0. Units are metres.
"""
import bpy, bmesh, math, random, sys
from mathutils import Vector, Matrix

random.seed(66)
OUT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "market.glb"


def lin(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]
    return tuple(((v / 12.92) if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4) for v in c)


PAL = {k: lin(v) for k, v in {
    "concrete": "#8f8a7c", "concrete_dk": "#6f6b62", "concrete_lt": "#a39d8c", "soot": "#3a3833",
    "steel": "#4a3f38", "rust": "#8a4a2c", "rust_lt": "#a8623a",
    "lime": "#e6e1d1", "lime_dk": "#c9c3b0",
    "wood": "#8a6a47", "wood_dk": "#5e4630", "wood_new": "#c9a877", "rope": "#b79c6b",
    "cap_ochre": "#b58a45", "cap_rust": "#9c5334", "cap_teal": "#5f8580", "cap_cream": "#bfb394",
    "glass": "#22303a", "dark": "#1c1b1a",
    "orange": "#e8762a", "flame": "#ffc070",
    "cloth_red": "#a8473a", "cloth_blue": "#4f6f8f", "cloth_ochre": "#c79a42", "cloth_white": "#d9d2bf",
    "cloth_green": "#6f8052", "cloth_plum": "#7a4f63",
    "clay": "#a9643f", "sack": "#b3a17a", "basket": "#a37f4a", "green": "#6c8a45", "red": "#b5482f",
    "skin1": "#c69a7a", "skin2": "#8d5f43", "skin3": "#e0b89a", "skin4": "#6b4631",
    "oilskin": "#6b6a3f", "oilskin_dk": "#3f4a3c", "keeping": "#3f7a5c", "soil": "#4a3a2a", "leaf": "#6f9148", "leaf_dk": "#4f7040",
    "brick": "#7c4a38",
    "mud": "#3f4636", "willow": "#44563a", "willow_lt": "#5c7046", "tin": "#8d9291",
}.items()}


class B:
    """One mesh under construction."""

    def __init__(self, name):
        self.name = name
        self.bm = bmesh.new()
        self.col = self.bm.loops.layers.float_color.new("Col")
        self.done = self.bm.faces.layers.int.new("done")   # 0 = not yet painted

    def _mark(self):
        pass

    def _new(self):
        # bmesh operators clear tags and reuse freed slots, so new geometry is found by a face flag
        return [f for f in self.bm.faces if f[self.done] == 0]

    def paint(self, faces, color, grime=0.22, jitter=0.05, hi=()):
        if not faces:
            return
        base = PAL[color] if isinstance(color, str) else color
        zs = [v.co.z for f in faces for v in f.verts]
        z0, z1 = min(zs), max(zs)
        span = max(z1 - z0, 1e-4)
        hi = set(hi)
        for f in faces:
            j = 1.0 + random.uniform(-jitter, jitter)
            nz = f.normal.z
            k = 1.10 if nz > 0.7 else (0.72 if nz < -0.5 else 1.0)
            if f in hi:
                k *= 1.18
            f[self.done] = 1
            for lp in f.loops:
                t = (lp.vert.co.z - z0) / span
                g = 1.0 - grime * (1.0 - t) ** 2
                lp[self.col] = (base[0] * j * k * g, base[1] * j * k * g, base[2] * j * k * g, 1.0)

    def box(self, size, loc, color, rz=0.0, bevel=0.03, rot=None, **kw):
        self._mark()
        m = Matrix.Translation(Vector(loc)) @ (rot if rot else Matrix.Rotation(rz, 4, "Z")) @ Matrix.Diagonal((*size, 1.0))
        bmesh.ops.create_cube(self.bm, size=1.0, matrix=m)
        hi = []
        if bevel > 0:
            edges = list({e for f in self._new() for e in f.edges})
            r = bmesh.ops.bevel(self.bm, geom=edges, offset=bevel, segments=1, profile=0.5, affect="EDGES")
            hi = [f for f in r["faces"] if f.is_valid]
        faces = self._new()
        self.bm.normal_update()
        self.paint(faces, color, hi=hi, **kw)
        return faces

    def cyl(self, r, h, loc, color, segs=12, r2=None, rot=None, caps=True, **kw):
        self._mark()
        m = Matrix.Translation(Vector(loc)) @ (rot if rot else Matrix.Identity(4))
        bmesh.ops.create_cone(self.bm, cap_ends=caps, cap_tris=False, segments=segs, radius1=r,
                              radius2=r if r2 is None else r2, depth=h, matrix=m)
        faces = self._new()
        self.bm.normal_update()
        self.paint(faces, color, **kw)
        return faces

    def tube(self, a, b, r, color, segs=6, **kw):
        a, b = Vector(a), Vector(b)
        d = b - a
        rot = Vector((0, 0, 1)).rotation_difference(d.normalized()).to_matrix().to_4x4()
        return self.cyl(r, d.length, (a + b) / 2, color, segs=segs, rot=rot, **kw)

    def ball(self, r, loc, color, scale=(1, 1, 1), sub=2, **kw):
        self._mark()
        m = Matrix.Translation(Vector(loc)) @ Matrix.Diagonal((*scale, 1.0))
        bmesh.ops.create_icosphere(self.bm, subdivisions=sub, radius=r, matrix=m)
        faces = self._new()
        self.bm.normal_update()
        self.paint(faces, color, **kw)
        return faces

    def cloth(self, p00, p10, p01, p11, colors, nx=8, ny=5, sag=0.15, flutter=0.03):
        """Quad patch between four corners, sagging in the middle. colors: list cycled across nx (stripes)."""
        self._mark()
        p00, p10, p01, p11 = map(Vector, (p00, p10, p01, p11))
        grid = []
        for iy in range(ny + 1):
            v = iy / ny
            row = []
            for ix in range(nx + 1):
                u = ix / nx
                p = (p00 * (1 - u) + p10 * u) * (1 - v) + (p01 * (1 - u) + p11 * u) * v
                p.z -= sag * math.sin(math.pi * u) * math.sin(math.pi * v) + random.uniform(-flutter, flutter)
                row.append(self.bm.verts.new(p))
            grid.append(row)
        for iy in range(ny):
            for ix in range(nx):
                f = self.bm.faces.new((grid[iy][ix], grid[iy][ix + 1], grid[iy + 1][ix + 1], grid[iy + 1][ix]))
                f.smooth = True
        self.bm.normal_update()
        faces = self._new()
        for f in faces:
            cx = sum(v.co.dot((p10 - p00).normalized()) for v in f.verts) / 4 - p00.dot((p10 - p00).normalized())
            idx = int(cx / max((p10 - p00).length, 1e-4) * nx)
            self.paint([f], colors[idx % len(colors)], grime=0.0, jitter=0.06)
        # thin cloth: give it a back face so it reads from below too
        r = bmesh.ops.duplicate(self.bm, geom=faces)
        back = [g for g in r["geom"] if isinstance(g, bmesh.types.BMFace)]
        for f in back:
            f[self.done] = 1
        bmesh.ops.reverse_faces(self.bm, faces=back)
        for f in back:
            for lp in f.loops:
                c = lp[self.col]
                lp[self.col] = (c[0] * 0.6, c[1] * 0.6, c[2] * 0.6, 1.0)
        return faces

    def finish(self, smooth_angle=None):
        me = bpy.data.meshes.new(self.name)
        self.bm.faces.layers.int.remove(self.done)
        self.bm.normal_update()
        self.bm.to_mesh(me)
        self.bm.free()
        ob = bpy.data.objects.new(self.name, me)
        bpy.context.scene.collection.objects.link(ob)
        me.color_attributes.active_color = me.color_attributes["Col"]
        me.color_attributes.render_color_index = 0
        me.materials.append(MAT)
        ca = me.color_attributes["Col"]
        n = len(ca.data)
        import numpy as np
        arr = np.zeros(n * 4, dtype=np.float32)
        ca.data.foreach_get("color", arr)
        arr = arr.reshape(-1, 4)
        white = float((arr[:, :3].min(axis=1) > 0.99).mean())
        print(f"  {self.name}: {len(me.polygons)} faces, mean colour {arr[:, :3].mean(axis=0).round(3)}, unpainted {white:.0%}")
        return ob


def empty(name, loc):
    ob = bpy.data.objects.new(name, None)
    ob.location = loc
    bpy.context.scene.collection.objects.link(ob)
    return ob


# ---------------------------------------------------------------- scene reset
bpy.ops.wm.read_factory_settings(use_empty=True)
MAT = bpy.data.materials.new("VCol")
MAT.use_nodes = True
nt = MAT.node_tree
bsdf = nt.nodes.get("Principled BSDF")
attr = nt.nodes.new("ShaderNodeVertexColor")
attr.layer_name = "Col"
nt.links.new(attr.outputs["Color"], bsdf.inputs["Base Color"])
bsdf.inputs["Roughness"].default_value = 0.95

CORE = Vector((-10.0, 10.0, 0.0))
CORE_R = 5.0
TILE = 4.0


def tile_exists(ix, iy):
    cx, cy = ix * TILE + 2, iy * TILE + 2
    if (Vector((cx, cy, 0)) - CORE).length < CORE_R - 0.5:
        return False
    if (ix, iy) in {(2, -2), (1, -1)}:          # missing bays (bridged with timber)
        return False
    if ix >= 2 and iy <= -2:                      # broken corner
        return False
    return -4 <= ix <= 2 and -2 <= iy <= 3


# ---------------------------------------------------------------- deck
deck = B("Deck")
for ix in range(-4, 3):
    for iy in range(-2, 4):
        if not tile_exists(ix, iy):
            continue
        c = random.choice(["concrete", "concrete", "concrete_lt", "concrete_dk"])
        deck.box((TILE - 0.06, TILE - 0.06, 0.4), (ix * TILE + 2, iy * TILE + 2, -0.2), c, bevel=0.05, grime=0.35)
        # worn patches and seams
        for _ in range(2):
            px, py = ix * TILE + random.uniform(0.6, 3.4), iy * TILE + random.uniform(0.6, 3.4)
            deck.box((random.uniform(0.5, 1.4), random.uniform(0.4, 1.1), 0.02), (px, py, 0.008),
                     random.choice(["concrete_dk", "concrete_dk", "soot"]) if random.random() < 0.7 else c, rz=random.uniform(0, 3), bevel=0, grime=0, jitter=0.02)
for k in range(34):                                   # dashed safety stripe along the front edge
    if random.random() < 0.8:
        deck.box((0.5, 0.16, 0.02), (-15.6 + k * 0.7, -7.55, 0.01), "orange", bevel=0, grime=0, jitter=0.12)
for k in range(20):                                   # and the left edge
    if random.random() < 0.8:
        deck.box((0.16, 0.5, 0.02), (-15.55, -7.3 + k * 0.7, 0.01), "orange", bevel=0, grime=0, jitter=0.12)
deck.finish()

# ---------------------------------------------------------------- space frame under the deck and columns above
frame = B("Frame")
for ix in range(-4, 4):
    for iy in range(-2, 5):
        x, y = ix * TILE, iy * TILE
        near = [tile_exists(ix + a, iy + b) for a in (-1, 0) for b in (-1, 0)]
        if not any(near):
            continue
        frame.cyl(0.16, 0.3, (x, y, -0.55), "steel", segs=8)
        for (dx, dy) in ((1, 0), (0, 1)):
            if tile_exists(ix, iy) or tile_exists(ix - (1 - dx), iy - (1 - dy)) or tile_exists(ix + dx - 1, iy + dy - 1):
                frame.tube((x, y, -0.55), (x + dx * TILE, y + dy * TILE, -0.55), 0.07, random.choice(["steel", "rust"]))
        if tile_exists(ix, iy):
            cx, cy = x + 2, y + 2
            for (ax, ay) in ((0, 0), (TILE, 0), (0, TILE), (TILE, TILE)):
                frame.tube((x + ax, y + ay, -0.55), (cx, cy, -2.9), 0.055, random.choice(["steel", "steel", "rust"]))
            frame.cyl(0.14, 0.24, (cx, cy, -2.9), "rust", segs=8)
for ix in range(-4, 3):
    for iy in range(-2, 4):
        if tile_exists(ix, iy) and tile_exists(ix + 1, iy):
            frame.tube((ix * TILE + 2, iy * TILE + 2, -2.9), (ix * TILE + 6, iy * TILE + 2, -2.9), 0.05, "steel")
        if tile_exists(ix, iy) and tile_exists(ix, iy + 1):
            frame.tube((ix * TILE + 2, iy * TILE + 2, -2.9), (ix * TILE + 2, iy * TILE + 6, -2.9), 0.05, "steel")

# upper frame carrying the capsules (bays behind the market)
COLS = [(-4, 8), (0, 8), (4, 8), (8, 8), (-4, 12), (0, 12), (4, 12), (8, 12)]
for (x, y) in COLS:
    frame.box((0.34, 0.34, 9.6), (x, y, 4.8), "steel", bevel=0.04, grime=0.3)
    frame.box((0.7, 0.7, 0.12), (x, y, 0.06), "rust", bevel=0.02)
for z in (3.2, 6.6):
    for y in (8, 12):
        frame.box((12.4, 0.26, 0.3), (2, y, z - 0.15), "steel", bevel=0.03)
    for x in (-4, 0, 4, 8):
        frame.box((0.26, 4.2, 0.3), (x, 10, z - 0.15), "rust", bevel=0.03)
for (a, b) in (((-4, 8, 0.2), (0, 8, 3.0)), ((8, 8, 0.2), (4, 8, 3.0)), ((0, 8, 3.3), (4, 8, 6.3)), ((-4, 8, 3.3), (-4, 12, 6.3))):
    frame.tube(a, b, 0.05, "rust")
frame.finish()

# ---------------------------------------------------------------- the core
core = B("Core")
for i in range(-6, 9):
    z = i * 1.5
    r = CORE_R + (0.0 if i % 2 else 0.05)
    c = "concrete_dk" if i < 0 else random.choice(["concrete", "concrete", "concrete_lt"])
    core.cyl(r, 1.46, (CORE.x, CORE.y, z + 0.75), c, segs=36, grime=0.3, jitter=0.07)
    core.cyl(CORE_R - 0.03, 0.06, (CORE.x, CORE.y, z), "soot", segs=36, grime=0, caps=False)
# rust bleeds: darker vertical streaks
for a in (0.2, 1.1, 1.9, 5.6, 6.0):
    px, py = CORE.x + math.cos(a) * (CORE_R + 0.03), CORE.y + math.sin(a) * (CORE_R + 0.03)
    core.box((0.22, 0.05, random.uniform(2.5, 5.5)), (px, py, random.uniform(3, 7)), "rust", rz=a + math.pi / 2, bevel=0, grime=0.5)
# whitewashed band at living height, then the record air-mark line in signal orange
core.cyl(CORE_R + 0.07, 1.25, (CORE.x, CORE.y, 0.63), "lime", segs=36, caps=False, grime=0.45, jitter=0.08)
core.cyl(CORE_R + 0.09, 0.09, (CORE.x, CORE.y, 1.70), "orange", segs=36, caps=False, grime=0, jitter=0.02)
# doorway facing the market (direction -45 degrees) with a timber lintel
ang = -math.pi / 4
dx, dy = math.cos(ang), math.sin(ang)
door_c = Vector((CORE.x + dx * (CORE_R - 0.15), CORE.y + dy * (CORE_R - 0.15), 1.1))
core.box((0.9, 1.3, 2.2), door_c, "dark", rz=ang, bevel=0, grime=0, jitter=0)
core.box((0.5, 1.7, 0.22), door_c + Vector((dx * 0.3, dy * 0.3, 1.2)), "wood_dk", rz=ang)
for s in (-1, 1):
    core.box((0.4, 0.2, 2.3), door_c + Vector((dx * 0.3 - dy * 0.75 * s, dy * 0.3 + dx * 0.75 * s, 0.05)), "wood", rz=ang)
# upper balcony ring
core.cyl(CORE_R + 0.9, 0.14, (CORE.x, CORE.y, 4.5), "concrete_dk", segs=36)
for k in range(36):
    a = k * math.tau / 36
    core.box((0.05, 0.05, 1.0), (CORE.x + math.cos(a) * (CORE_R + 0.8), CORE.y + math.sin(a) * (CORE_R + 0.8), 5.05), "steel", bevel=0)
core.cyl(CORE_R + 0.82, 0.06, (CORE.x, CORE.y, 5.55), "rust", segs=36, caps=False)
for k in range(12):
    a = k * math.tau / 12 + 0.13
    if abs(((a - ang + math.pi) % math.tau) - math.pi) < 0.3:
        continue
    px, py = CORE.x + math.cos(a) * (CORE_R + 0.1), CORE.y + math.sin(a) * (CORE_R + 0.1)
    core.box((0.3, 0.55, 22.0), (px, py, 2.0), "concrete_dk", rz=a, bevel=0.04, grime=0.35, jitter=0.06)
for k, a in enumerate((-1.25, -0.2, 0.55)):
    px, py = CORE.x + math.cos(a) * (CORE_R + 0.35), CORE.y + math.sin(a) * (CORE_R + 0.35)
    core.cyl(0.11 if k else 0.16, 20.0, (px, py, 2.0), "rust" if k else "tin", segs=8, grime=0.3)
    for z in (-3, 0.4, 3.6, 7.2):
        core.box((0.5, 0.12, 0.08), (px - math.cos(a) * 0.15, py - math.sin(a) * 0.15, z), "steel", rz=a, bevel=0)
for a in (-1.6, -1.0, 0.2, 0.85):
    for z in (2.9, 7.4):
        px, py = CORE.x + math.cos(a) * (CORE_R + 0.02), CORE.y + math.sin(a) * (CORE_R + 0.02)
        core.box((0.12, 0.7, 1.1), (px, py, z), "dark", rz=a, bevel=0, grime=0, jitter=0)
        core.box((0.2, 0.9, 0.1), (px, py, z - 0.6), "concrete_lt", rz=a, bevel=0.01)
# green enamel pictogram plate beside the door: a figure sealing a cap
pa = ang + 0.42
pc = Vector((CORE.x + math.cos(pa) * (CORE_R + 0.12), CORE.y + math.sin(pa) * (CORE_R + 0.12), 2.45))
prot = Matrix.Rotation(pa, 4, "Z") @ Matrix.Rotation(math.pi / 2, 4, "Y")
core.cyl(0.52, 0.04, pc, "lime", segs=20, rot=prot, grime=0)
core.cyl(0.46, 0.06, pc, "keeping", segs=20, rot=prot, grime=0, jitter=0.02)
po = Vector((math.cos(pa), math.sin(pa), 0)) * 0.04
core.ball(0.07, pc + po + Vector((0, 0, 0.2)), "lime", sub=1, grime=0, jitter=0)
core.box((0.05, 0.14, 0.26), pc + po, "lime", rz=pa, bevel=0, grime=0, jitter=0)
core.box((0.05, 0.4, 0.07), pc + po + Vector((0, 0, -0.2)), "lime", rz=pa, bevel=0, grime=0, jitter=0)
core.finish()

# ---------------------------------------------------------------- stencil numerals (seven-segment, hand-cut look)
SEG = {"0": "abcdef", "1": "bc", "2": "abged", "3": "abgcd", "4": "fgbc", "5": "afgcd", "6": "afgedc",
       "7": "abc", "8": "abcdefg", "9": "abfgcd"}


def stencil(b, text, origin, right, up, h=0.42, color="orange"):
    right, up = Vector(right).normalized(), Vector(up).normalized()
    nrm = right.cross(up)
    rot = Matrix((right, up, nrm)).transposed().to_4x4()
    w, t = h * 0.5, h * 0.11
    x = 0.0
    for ch in text:
        if ch == ".":
            b.box((t, t, 0.02), Vector(origin) + right * (x + t), color, rot=rot, bevel=0, grime=0, jitter=0.03)
            x += t * 3
            continue
        segs = {"a": (w / 2, h, w, t), "g": (w / 2, h / 2, w, t), "d": (w / 2, 0, w, t),
                "f": (0, h * 0.75, t, h / 2), "b": (w, h * 0.75, t, h / 2),
                "e": (0, h * 0.25, t, h / 2), "c": (w, h * 0.25, t, h / 2)}
        for s in SEG[ch]:
            sx, sy, sw, sh = segs[s]
            b.box((sw * 0.82, sh * 0.82, 0.02), Vector(origin) + right * (x + sx) + up * sy, color, rot=rot, bevel=0, grime=0, jitter=0.03)
        x += w + t * 2.2


# ---------------------------------------------------------------- capsules hung in the upper frame
caps = B("Capsules")
timber = B("Timber")


def capsule(cx, cy, z, color, flip=False):
    L, W, H = 3.7, 3.4, 2.5
    caps.box((L, W, H), (cx, cy, z + H / 2), color, bevel=0.28, grime=0.3, jitter=0.06)
    fy = cy - W / 2
    # hooded window: frame, glass, timber shutter
    wx = cx + (-0.8 if flip else 0.8)
    rotx = Matrix.Rotation(math.pi / 2, 4, "X")
    caps.cyl(0.62, 0.16, (wx, fy - 0.04, z + 1.45), "soot", segs=16, rot=rotx, grime=0)
    caps.cyl(0.50, 0.20, (wx, fy - 0.05, z + 1.45), "glass", segs=16, rot=rotx, grime=0, jitter=0.02)
    caps.box((1.5, 0.5, 0.08), (wx, fy - 0.28, z + 2.15), "rust", rot=Matrix.Rotation(0.35, 4, "X"), bevel=0.01)
    # door with new timber
    dxp = cx + (0.9 if flip else -0.9)
    timber.box((0.85, 0.1, 1.75), (dxp, fy - 0.03, z + 0.95), "wood_new", bevel=0.02)
    timber.box((1.05, 0.14, 0.12), (dxp, fy - 0.04, z + 1.9), "wood_dk", bevel=0.02)
    # patch panels and ribs
    for k in range(3):
        caps.box((0.06, W + 0.05, H - 0.5), (cx - L / 2 + 0.6 + k * 1.25, cy, z + H / 2), "soot", bevel=0, grime=0.1)
    timber.box((1.3, 0.05, 0.9), (cx + random.uniform(-0.6, 0.6), fy - 0.02, z + 0.6), "wood", bevel=0.01)
    # roof clutter: cistern, stovepipe, tarp
    caps.cyl(0.55, 0.9, (cx - 1.0, cy + 0.3, z + H + 0.45), "tin", segs=12, grime=0.3)
    caps.cyl(0.09, 1.3, (cx + 1.2, cy + 0.9, z + H + 0.6), "soot", segs=8)
    caps.cyl(0.16, 0.08, (cx + 1.2, cy + 0.9, z + H + 1.28), "soot", segs=8)


capsule(-2, 10, 3.2, "cap_ochre")
capsule(2, 10, 3.2, "cap_teal", flip=True)
capsule(6, 10, 3.2, "cap_rust")
capsule(0, 10, 6.6, "cap_cream", flip=True)
capsule(6, 10, 6.6, "cap_ochre")
caps.finish()

# timber gallery in front of the lower capsules, with rail, and a ladder down to the deck
for k in range(44):
    x = -4.2 + k * 0.29
    timber.box((0.26, 1.5, 0.06), (x, 7.45, 3.2 + random.uniform(-0.01, 0.01)), random.choice(["wood", "wood", "wood_dk", "wood_new"]),
               rz=random.uniform(-0.03, 0.03), bevel=0.01, grime=0.1)
for x in (-4.2, -1.4, 1.4, 4.2, 7.0, 8.4):
    timber.box((0.09, 0.09, 1.05), (x, 6.78, 3.75), "wood_dk", bevel=0.01)
    timber.tube((x, 6.78, 3.2), (x, 7.9, 2.9), 0.04, "wood_dk")
timber.box((12.7, 0.07, 0.07), (2.1, 6.78, 4.25), "wood", bevel=0.01)
timber.box((12.7, 0.05, 0.05), (2.1, 6.78, 3.8), "wood_dk", bevel=0.01)
# upper gallery (short)
for k in range(30):
    timber.box((0.26, 1.3, 0.06), (-1.9 + k * 0.29, 7.6, 6.6), random.choice(["wood", "wood_dk", "wood_new"]), bevel=0.01, grime=0.1)
timber.box((8.6, 0.06, 0.06), (2.3, 7.0, 7.6), "wood", bevel=0.01)
for x in (-1.9, 1.0, 3.9, 6.6):
    timber.box((0.08, 0.08, 1.0), (x, 7.0, 7.1), "wood_dk", bevel=0.01)


def ladder(b, base, top, width=0.5):
    base, top = Vector(base), Vector(top)
    d = (top - base)
    side = Vector((d.y, -d.x, 0)).normalized() if abs(d.x) + abs(d.y) > 1e-3 else Vector((1, 0, 0))
    side = Vector((1, 0, 0)) if side.length < 0.5 else side
    for s in (-1, 1):
        b.tube(base + side * s * width / 2, top + side * s * width / 2, 0.035, "wood_dk")
    n = int(d.length / 0.32)
    for i in range(1, n):
        p = base + d * (i / n)
        b.tube(p - side * width / 2, p + side * width / 2, 0.025, "wood")


ladder(timber, (8.0, 5.6, 0.0), (8.0, 6.8, 3.25))
ladder(timber, (-1.2, 6.9, 3.25), (-1.2, 7.2, 6.65))

# bridged bays: planks over the missing tiles
for k in range(13):
    timber.box((0.28, 4.5, 0.07), (8.15 + k * 0.31, -6 + random.uniform(-0.1, 0.1), 0.02),
               random.choice(["wood", "wood_dk", "wood_new", "wood"]), rz=random.uniform(-0.04, 0.04), bevel=0.01, grime=0.1)
for k in range(13):
    timber.box((4.5, 0.28, 0.07), (6 + random.uniform(-0.1, 0.1), -3.85 + k * 0.31, 0.02),
               random.choice(["wood", "wood_dk", "wood_new", "wood"]), rz=random.uniform(-0.04, 0.04), bevel=0.01, grime=0.1)

# rope rails round the open edges
ropes = B("Ropes")


def rail(pts):
    for i, p in enumerate(pts):
        timber.box((0.1, 0.1, 1.1), (p[0], p[1], 0.55), "wood_dk", bevel=0.015)
        if i:
            q = pts[i - 1]
            for z in (1.0, 0.55):
                mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2, z - 0.09)
                ropes.tube((q[0], q[1], z), mid, 0.022, "rope", segs=5)
                ropes.tube(mid, (p[0], p[1], z), 0.022, "rope", segs=5)


rail([(-15.8, y, 0) for y in (-7.8, -5.2, -2.6, 0, 2.6, 5.2)])
rail([(x, -7.85, 0) for x in (-15.8, -13, -10.4, -7.8, -5.2, -2.6, 0, 2.6, 5.2, 7.9)])
rail([(7.9, -7.85, 0), (7.9, -4.15, 0)])
rail([(11.85, -3.9, 0), (11.85, -1.4, 0), (11.85, 1.2, 0), (11.85, 3.8, 0), (11.85, 6.4, 0)])

# ---------------------------------------------------------------- market
market = B("Market")
cloth = B("Cloth")
flames = B("Flames")
lamp_i = 0


def lamp(x, y, h=2.5):
    global lamp_i
    market.box((0.09, 0.09, h), (x, y, h / 2), "wood_dk", bevel=0.015)
    market.box((0.5, 0.06, 0.06), (x + 0.22, y, h - 0.1), "wood_dk", bevel=0.01)
    market.cyl(0.11, 0.1, (x + 0.42, y, h - 0.2), "tin", segs=8, r2=0.14)
    flames.cyl(0.07, 0.2, (x + 0.42, y, h - 0.05), "flame", segs=6, r2=0.0, grime=0, jitter=0)
    empty(f"Lamp_{lamp_i}", (x + 0.42, y, h + 0.05))
    lamp_i += 1


def goods(x, y, z, rz, kind):
    r = Matrix.Rotation(rz, 4, "Z")

    def at(lx, ly, lz=0.0):
        v = r @ Vector((lx, ly, 0))
        return (x + v.x, y + v.y, z + lz)
    if kind == "pots":
        for i in range(5):
            s = random.uniform(0.09, 0.15)
            market.cyl(s, s * 1.6, at(-0.8 + i * 0.38, random.uniform(-0.15, 0.15), s * 0.8), random.choice(["clay", "clay", "lime_dk"]), segs=8, r2=s * 0.6)
    elif kind == "baskets":
        for i in range(3):
            market.cyl(0.2, 0.2, at(-0.65 + i * 0.6, 0, 0.1), "basket", segs=10, r2=0.26)
            for _ in range(6):
                market.ball(0.07, at(-0.65 + i * 0.6 + random.uniform(-0.12, 0.12), random.uniform(-0.12, 0.12), 0.22),
                            random.choice(["green", "red", "cloth_ochre"]), sub=1, grime=0)
    elif kind == "sacks":
        for i in range(3):
            market.ball(0.24, at(-0.6 + i * 0.55, random.uniform(-0.1, 0.1), 0.17), "sack", scale=(1.0, 0.8, 0.75), sub=2, grime=0.3)
    elif kind == "salvage":
        market.cyl(0.06, 1.3, at(-0.2, 0.1, 0.07), "rust", segs=8, rot=r @ Matrix.Rotation(math.pi / 2, 4, "Y"))
        market.cyl(0.22, 0.07, at(0.6, 0, 0.04), "tin", segs=12)
        market.box((0.4, 0.3, 0.22), at(-0.75, -0.05, 0.11), "cap_teal", rz=rz + 0.3)
        market.cyl(0.09, 0.24, at(0.15, -0.2, 0.12), "glass", segs=8)
    elif kind == "lime":
        for i in range(4):
            market.box((0.3, 0.2, 0.14), at(-0.6 + i * 0.36, 0.05, 0.07 + (0.14 if i % 2 else 0)), "lime", rz=rz + random.uniform(-0.2, 0.2), bevel=0.02)
        market.cyl(0.2, 0.28, at(0.85, 0, 0.14), "wood", segs=10)


def stall(x, y, rz, cols, kind, w=2.6, d=1.5):
    r = Matrix.Rotation(rz, 4, "Z")

    def at(lx, ly, lz):
        v = r @ Vector((lx, ly, 0))
        return (x + v.x, y + v.y, lz)
    hf, hb = 2.05, 2.55
    for (lx, ly, h) in ((-w / 2, -d / 2, hf), (w / 2, -d / 2, hf), (-w / 2, d / 2, hb), (w / 2, d / 2, hb)):
        market.box((0.08, 0.08, h), at(lx, ly, h / 2), "wood_dk", rz=rz, bevel=0.012)
    market.box((w, d * 0.62, 0.06), at(0, -0.1, 0.9), "wood", rz=rz, bevel=0.015)
    market.box((w, 0.05, 0.3), at(0, -0.1 - d * 0.31, 0.72), "wood_dk", rz=rz, bevel=0.01)
    for lx in (-w / 2 + 0.1, w / 2 - 0.1):
        market.box((0.07, d * 0.55, 0.88), at(lx, -0.1, 0.44), "wood_dk", rz=rz, bevel=0.01)
    cloth.cloth(at(-w / 2 - 0.25, -d / 2 - 0.45, hf - 0.12), at(w / 2 + 0.25, -d / 2 - 0.45, hf - 0.12),
                at(-w / 2 - 0.25, d / 2 + 0.1, hb + 0.02), at(w / 2 + 0.25, d / 2 + 0.1, hb + 0.02), cols, nx=10, ny=5, sag=0.16)
    goods(x + (r @ Vector((0, -0.1, 0))).x, y + (r @ Vector((0, -0.1, 0))).y, 0.93, rz, kind)
    # floor clutter beside the stall
    c = at(w / 2 + 0.5, 0.2, 0)
    market.box((0.55, 0.45, 0.4), (c[0], c[1], 0.2), "wood", rz=rz + 0.4, bevel=0.02)
    if random.random() < 0.6:
        market.box((0.45, 0.4, 0.35), (c[0] + 0.05, c[1], 0.58), "wood_new", rz=rz - 0.3, bevel=0.02)


stall(-6.5, -3.0, 0.15, ["cloth_red", "cloth_white"], "pots")
stall(-2.6, -4.2, -0.1, ["cloth_ochre"], "baskets")
stall(1.6, -3.4, 0.2, ["cloth_blue", "cloth_white"], "salvage")
stall(-5.0, 2.0, math.pi / 2 + 0.1, ["cloth_green", "cloth_ochre"], "sacks")
stall(3.4, 2.6, -0.25, ["cloth_white"], "lime")
stall(-11.5, -4.5, 0.6, ["cloth_plum", "cloth_ochre"], "baskets")

# lime tanks: whitewashed vats with timber lids and splash rings on the deck
for (x, y) in ((-1.0, 4.8), (1.4, 5.4)):
    market.cyl(1.05, 1.5, (x, y, 0.75), "lime", segs=16, grime=0.4, jitter=0.07)
    for z in (0.3, 1.2):
        market.cyl(1.08, 0.08, (x, y, z), "rust", segs=16, caps=False)
    market.cyl(1.1, 0.08, (x, y, 1.54), "wood", segs=16)
    market.cyl(1.7, 0.012, (x, y, 0.012), "lime_dk", segs=14, grime=0, jitter=0.1)
market.tube((0.2, 5.1, 1.2), (0.2, 6.9, 3.0), 0.06, "tin")
market.box((0.9, 0.7, 0.5), (3.2, 5.6, 0.25), "wood", rz=0.3)
market.box((0.9, 0.7, 0.5), (3.3, 5.5, 0.75), "wood_dk", rz=0.1)

# lamps at measured heights
for (x, y) in ((-8.5, -6.4), (-0.4, -6.6), (5.6, -0.6), (-3.2, 0.0), (-9.6, 2.4), (6.5, 5.4), (10.6, 2.0)):
    lamp(x, y)
# gallery lamps
for x in (-3.0, 3.2, 7.6):
    flames.cyl(0.06, 0.18, (x, 6.85, 4.55), "flame", segs=6, r2=0.0, grime=0, jitter=0)
    market.cyl(0.1, 0.08, (x, 6.85, 4.42), "tin", segs=8)
    empty(f"Lamp_{lamp_i}", (x, 6.85, 4.65)); lamp_i += 1

# barrels, crates, benches
for (x, y) in ((-13.5, 1.5), (-13.0, 2.3), (9.6, 6.2), (-7.6, 5.2)):
    market.cyl(0.38, 0.95, (x, y, 0.475), "wood", segs=12, grime=0.3)
    for z in (0.2, 0.75):
        market.cyl(0.395, 0.06, (x, y, z), "rust", segs=12, caps=False)
for (x, y, rz) in ((-9.0, -1.0, 0.2), (5.5, -5.9, 1.5)):
    market.box((1.8, 0.4, 0.07), (x, y, 0.48), "wood", rz=rz, bevel=0.015)
    for s in (-0.7, 0.7):
        v = Matrix.Rotation(rz, 4, "Z") @ Vector((s, 0, 0))
        market.box((0.08, 0.36, 0.46), (x + v.x, y + v.y, 0.23), "wood_dk", rz=rz, bevel=0.01)

# bucket-lift gantry at the open corner
for s in (-0.8, 0.8):
    timber.box((0.16, 0.16, 3.4), (10.9, -3.0 + s, 1.7), "wood_dk", bevel=0.02)
timber.box((2.9, 0.18, 0.18), (11.9, -3.0, 3.3), "wood", bevel=0.02)
timber.box((0.2, 2.0, 0.16), (10.9, -3.0, 3.45), "wood_dk", bevel=0.02)
timber.tube((10.9, -3.8, 0.1), (12.4, -3.0, 3.2), 0.05, "wood_dk")
market.cyl(0.22, 0.12, (13.0, -3.0, 3.1), "wood_dk", segs=10, rot=Matrix.Rotation(math.pi / 2, 4, "X"))
ropes.tube((13.0, -3.0, 3.0), (13.0, -3.0, -3.2), 0.025, "rope", segs=5)
market.cyl(0.3, 0.45, (13.0, -3.0, -3.4), "wood", segs=10, r2=0.36)

# the record board by the core door: date-less stencil "9.2" and tonight's "7.4" lower down
board_o = door_c + Vector((dx * 0.42 - dy * 1.9, dy * 0.42 + dx * 1.9, 0.0))
market.box((0.06, 1.3, 1.5), board_o + Vector((0, 0, 0.35)), "lime", rz=ang, bevel=0.01, grime=0.2)
right = Vector((-dy, dx, 0))
stencil(market, "9.2", board_o + right * -0.5 + Vector((dx * 0.04, dy * 0.04, 0.55)), right, (0, 0, 1))
stencil(market, "7.4", board_o + right * -0.5 + Vector((dx * 0.04, dy * 0.04, -0.25)), right, (0, 0, 1), h=0.3, color="soot")

# laundry lines between the frame columns
for (a, b, z) in (((-4, 8, 2.7), (0, 8, 2.7), 0), ((4, 8, 6.2), (8, 8, 6.2), 0), ((0.0, 8, 6.0), (4, 8, 6.0), 0)):
    a, b = Vector(a), Vector(b)
    ropes.tube(a, b, 0.015, "rope", segs=5)
    t = 0.12
    while t < 0.85:
        wdt = random.uniform(0.35, 0.7)
        hgt = random.uniform(0.5, 0.95)
        p = a + (b - a) * t
        q = p + (b - a).normalized() * wdt
        cloth.cloth(p + Vector((0, -0.02, -hgt)), q + Vector((0, -0.02, -hgt)), p, q,
                    [random.choice(["cloth_white", "cloth_red", "cloth_blue", "cloth_ochre", "cloth_plum", "cloth_green"])],
                    nx=3, ny=4, sag=0.0, flutter=0.04)
        t += (wdt + random.uniform(0.15, 0.4)) / (b - a).length


# ---------------------------------------------------------------- second pass: life and clutter
def handcart(x, y, rz):
    r = Matrix.Rotation(rz, 4, "Z")

    def at(lx, ly, lz):
        v = r @ Vector((lx, ly, 0))
        return (x + v.x, y + v.y, lz)
    market.box((1.5, 0.85, 0.08), at(0, 0, 0.55), "wood", rz=rz, bevel=0.015)
    rx = r @ Matrix.Rotation(math.pi / 2, 4, "X")
    for ly in (-0.42, 0.42):
        market.box((1.5, 0.05, 0.28), at(0, ly, 0.72), "wood_dk", rz=rz, bevel=0.01)
        market.cyl(0.36, 0.07, at(-0.1, ly * 1.22, 0.36), "wood_dk", segs=12, rot=rx)
        market.cyl(0.08, 0.1, at(-0.1, ly * 1.22, 0.36), "rust", segs=8, rot=rx)
        market.tube(at(0.7, ly * 0.8, 0.6), at(1.6, ly * 0.8, 0.85), 0.03, "wood")
    market.box((0.05, 0.85, 0.28), at(-0.74, 0, 0.72), "wood_dk", rz=rz, bevel=0.01)
    for _ in range(4):
        market.ball(0.2, at(random.uniform(-0.5, 0.4), random.uniform(-0.25, 0.25), 0.74), "sack", scale=(1, 0.85, 0.7), sub=2, grime=0.3)


def planter(x, y, rz, n=1.8):
    r = Matrix.Rotation(rz, 4, "Z")
    market.box((n, 0.5, 0.42), (x, y, 0.21), random.choice(["wood", "wood_dk"]), rz=rz, bevel=0.02)
    market.box((n - 0.12, 0.38, 0.04), (x, y, 0.42), "soil", rz=rz, bevel=0, grime=0)
    k = -n / 2 + 0.25
    while k < n / 2 - 0.1:
        v = r @ Vector((k, random.uniform(-0.08, 0.08), 0))
        h = random.uniform(0.16, 0.34)
        market.ball(h, (x + v.x, y + v.y, 0.44 + h * 0.75), random.choice(["leaf", "leaf", "leaf_dk", "green"]), scale=(1, 1, 0.9), sub=1, grime=0.3, jitter=0.12)
        k += random.uniform(0.25, 0.42)


def rug(x, y, rz, cols, w=1.9, d=1.0):
    r = Matrix.Rotation(rz, 4, "Z")
    n = 7
    for i in range(n):
        v = r @ Vector((-w / 2 + (i + 0.5) * w / n, 0, 0))
        market.box((w / n, d, 0.025), (x + v.x, y + v.y, 0.013), cols[i % len(cols)], rz=rz, bevel=0, grime=0, jitter=0.08)


people = B("People")


def person(x, y, rz, cloak, skin, head="hat", carry=None, z=0.0, sounder=False):
    global lamp_i
    r = Matrix.Rotation(rz, 4, "Z")

    def at(lx, ly, lz):
        v = r @ Vector((lx, ly, 0))
        return (x + v.x, y + v.y, z + lz)
    for ly in (-0.09, 0.09):
        people.box((0.13, 0.12, 0.5), at(0, ly, 0.25), "soot", rz=rz, bevel=0.02)
    fs = people.cyl(0.27, 0.9, at(0, 0, 0.88), cloak, segs=9, r2=0.17, grime=0.35, jitter=0.08)
    fs += people.ball(0.2, at(0, 0, 1.33), cloak, scale=(0.9, 1.15, 0.6), sub=2, grime=0.1)
    fs += people.ball(0.125, at(0.01, 0, 1.56), skin, scale=(1, 0.95, 1.08), sub=2, grime=0.15, jitter=0.03)
    if head == "hat":
        people.cyl(0.25, 0.03, at(0, 0, 1.66), "basket", segs=12)
        people.cyl(0.12, 0.1, at(0, 0, 1.72), "basket", segs=10, r2=0.09)
    elif head == "hood":
        fs += people.ball(0.17, at(-0.035, 0, 1.58), cloak, scale=(1, 1, 1.05), sub=2, grime=0.1)
    elif head == "scarf":
        people.cyl(0.15, 0.1, at(0, 0, 1.66), random.choice(["cloth_red", "cloth_blue", "cloth_ochre"]), segs=10, r2=0.11)
    for f in fs:
        f.smooth = True
    if sounder:        # high collar, coiled air bladder, the three-flame staff
        people.cyl(0.19, 0.16, at(0, 0, 1.45), cloak, segs=9, r2=0.21, caps=False)
        people.ball(0.17, at(-0.12, 0.2, 1.2), "basket", scale=(1, 0.6, 1.2), sub=2, grime=0.2)
        sx, sy = 0.36, -0.26
        people.tube(at(sx, sy, 0.0), at(sx, sy, 2.25), 0.028, "wood")
        people.tube(at(0.05, -0.2, 1.3), at(sx, sy, 1.25), 0.05, cloak)
        for hz in (0.5, 1.0, 1.5):
            people.box((0.2, 0.03, 0.03), at(sx + 0.08, sy, hz), "wood_dk", rz=rz, bevel=0)
            people.cyl(0.05, 0.07, at(sx + 0.17, sy, hz + 0.02), "tin", segs=8, r2=0.065)
            flames.cyl(0.035, 0.11, at(sx + 0.17, sy, hz + 0.11), "flame", segs=6, r2=0.0, grime=0, jitter=0)
        empty(f"Lamp_{lamp_i}", at(sx + 0.17, sy, 1.2))
        lamp_i += 1
    else:
        for ly in (-0.2, 0.2):
            people.tube(at(0, ly, 1.3), at(0.1 if carry else 0.03, ly * 1.15, 0.85), 0.05, cloak)
        if carry == "basket":
            people.cyl(0.18, 0.2, at(0.26, 0, 0.95), "basket", segs=10, r2=0.23)
            people.ball(0.1, at(0.26, 0, 1.07), "green", sub=1, grime=0)
        elif carry == "sack":
            people.ball(0.24, at(-0.1, 0, 1.5), "sack", scale=(1, 0.9, 0.75), sub=2, grime=0.3)
        elif carry == "pole":
            people.tube(at(0.2, 0.3, 0.0), at(0.2, 0.3, 2.6), 0.025, "wood_dk")
            people.box((0.3, 0.04, 0.04), at(0.3, 0.3, 2.55), "rust", rz=rz, bevel=0)


CLOAKS = ["oilskin", "oilskin_dk", "cloth_blue", "cloth_plum", "sack", "cap_teal", "cloth_red", "wood_dk", "cloth_ochre", "cloth_green"]
SKINS = ["skin1", "skin2", "skin3", "skin4"]
person(-4.3, 5.6, -0.9, "oilskin", "skin2", head="hood", sounder=True)                # the Sounder by the core door
for (x, y, rz, head, carry) in (
        (-6.4, -2.2, 1.6, "hat", None), (-6.9, -4.6, 1.3, "scarf", "basket"), (-2.7, -3.3, 1.6, "hood", None),
        (-2.2, -5.6, 1.7, "hat", "sack"), (1.5, -2.6, 1.5, "scarf", None), (2.3, -5.0, 1.9, "hat", None),
        (-4.0, 2.2, 3.1, "hat", None), (-6.6, 1.6, 0.2, "scarf", "basket"), (3.6, 3.4, 1.4, "hood", None),
        (4.6, 1.2, 2.0, "hat", "pole"), (-9.4, -1.9, -0.5, "hat", None), (-11.0, -3.0, 0.9, "scarf", None),
        (6.6, -2.4, 2.6, "hood", "sack"), (9.2, -5.4, 2.4, "hat", "pole"), (-12.6, 3.6, -0.7, "hood", "basket"),
        (0.2, 0.4, 0.5, "hat", None), (-0.6, -0.4, -2.4, "scarf", None), (8.4, 2.6, -2.2, "hat", "basket")):
    person(x, y, rz, random.choice(CLOAKS), random.choice(SKINS), head=head, carry=carry)
for (x, rz) in ((-2.4, -1.4), (4.9, -1.7)):                                             # two on the gallery
    person(x, 7.3, rz, random.choice(CLOAKS), random.choice(SKINS), head="scarf", z=3.24)
people.finish()

handcart(-9.8, 4.6, 0.5)
handcart(7.4, -1.6, 2.2)
for (x, y, rz) in ((-15.2, -1.0, math.pi / 2), (-15.2, 1.2, math.pi / 2), (-15.2, 3.4, math.pi / 2), (10.9, 0.2, math.pi / 2),
                   (10.9, 2.6, math.pi / 2), (-12.4, 7.2, 0.3), (5.6, 6.9, 0.0)):
    planter(x, y, rz)
for x in (-3.4, 0.6, 4.6, 7.0):                                                           # window boxes on the gallery rail
    timber.box((1.1, 0.26, 0.2), (x, 6.6, 3.36), "wood_dk", bevel=0.015)
    for k in range(4):
        market.ball(0.13, (x - 0.38 + k * 0.26, 6.6, 3.52), random.choice(["leaf", "green", "red", "cloth_ochre"]), sub=1, grime=0.2, jitter=0.1)
rug(-6.6, -4.5, 0.15, ["cloth_red", "cloth_ochre", "cloth_white"])
rug(1.7, -5.0, 0.2, ["cloth_blue", "cloth_white", "cloth_plum"])
rug(3.2, 1.0, -0.25, ["cloth_green", "cloth_ochre"])
rug(-2.7, -5.8, -0.1, ["cloth_plum", "cloth_ochre", "cloth_red"])
# stacked goods, jars, coils and a drying rack
for (x, y) in ((-13.6, -6.6), (-8.2, 1.2), (6.2, 3.4), (9.8, -1.2), (-1.4, 2.4), (-14.4, 5.8)):
    for k in range(random.randint(2, 4)):
        sz = random.uniform(0.4, 0.62)
        market.box((sz, sz * random.uniform(0.8, 1.1), sz * 0.8),
                   (x + random.uniform(-0.5, 0.5), y + random.uniform(-0.5, 0.5), sz * 0.4 + (sz * 0.8 if k == 3 else 0)),
                   random.choice(["wood", "wood_dk", "wood_new"]), rz=random.uniform(0, 1.5), bevel=0.025)
    for k in range(random.randint(1, 3)):
        s2 = random.uniform(0.16, 0.24)
        market.cyl(s2, s2 * 2.0, (x + random.uniform(-0.8, 0.8), y + random.uniform(-0.8, 0.8), s2),
                   random.choice(["clay", "clay", "lime_dk"]), segs=9, r2=s2 * 0.55)
for (x, y) in ((8.6, 4.4), (-11.8, 0.4)):
    for k in range(3):
        market.cyl(0.42 - k * 0.03, 0.14, (x, y, 0.07 + k * 0.14), "rope", segs=12, grime=0.2)
for sd in (-1.1, 1.1):
    timber.box((0.07, 0.07, 1.9), (-9.6 + sd, -6.2, 0.95), "wood_dk", bevel=0.01)
ropes.tube((-10.7, -6.2, 1.8), (-8.5, -6.2, 1.8), 0.015, "rope", segs=5)
for k in range(7):
    market.box((0.09, 0.03, 0.34), (-10.5 + k * 0.3, -6.2, 1.62), random.choice(["tin", "tin", "lime_dk"]), bevel=0.01, grime=0.2)

market.finish()
cloth.finish()
ropes.finish()
timber.finish()
flames.finish()

# ---------------------------------------------------------------- the dead ground far below, with willow scrub
ground = B("Ground")
ground.box((120, 120, 0.2), (0, 0, -7.6), "mud", bevel=0, grime=0, jitter=0)
for _ in range(70):
    x, y = random.uniform(-45, 45), random.uniform(-45, 45)
    s = random.uniform(1.5, 3.6)
    ground.cyl(0.18, 2.2, (x, y, -6.4), "wood_dk", segs=5)
    for k in range(random.randint(3, 5)):
        ox, oy = random.uniform(-s, s) * 0.6, random.uniform(-s, s) * 0.6
        r = s * random.uniform(0.45, 0.8)
        fs = ground.ball(r, (x + ox, y + oy, -5.6 + r * 0.5 + random.uniform(0, 0.8)), random.choice(["willow", "willow", "willow_lt"]),
                         scale=(1, 1, 0.7), sub=2, grime=0.55, jitter=0.1)
        for f in fs:
            f.smooth = True
for _ in range(16):                                   # chimney stacks: all that is left of the lowland houses
    x, y = random.uniform(-40, 40), random.uniform(-40, 40)
    ground.box((0.9, 0.9, random.uniform(2.5, 5.0)), (x, y, -5.5), "brick", rz=random.uniform(0, 1), bevel=0.05, grime=0.5)
    ground.box((random.uniform(4, 7), 0.4, 0.6), (x + 2, y, -7.2), "concrete_dk", rz=random.uniform(0, 3), bevel=0)
ground.finish()

# ---------------------------------------------------------------- export
total = sum(len(o.data.polygons) for o in bpy.data.objects if o.type == "MESH")
print("TOTAL FACES", total)
kw = dict(filepath=OUT, export_format="GLB", export_apply=True, export_yup=True, export_normals=True,
          export_materials="EXPORT", export_extras=False)
try:
    bpy.ops.export_scene.gltf(**kw, export_vertex_color="ACTIVE", export_all_vertex_colors=True)
except TypeError as e:
    print("fallback export:", e)
    bpy.ops.export_scene.gltf(**kw)
print("WROTE", OUT)
