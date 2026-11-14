"""Shared helpers for agent-built characters: lofted skinned meshes, armatures, keyed animation, GLB export.
Blender axes: X right, Y back, Z up. Characters face -Y. Units are metres.
Colour is a linear float vertex-colour layer "Col"; UVMap holds the rest position so the paint noise does not swim.
"""
import bpy, bmesh, math, random
from mathutils import Vector, Matrix, noise


def lin(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]
    return tuple(((v / 12.92) if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4) for v in c)


def palette(d):
    return {k: lin(v) for k, v in d.items()}


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def R(c, rx, ry=None, dn=None, w=None, col=None, k=1.0):
    """One loft ring: centre, half-width, front radius, back radius, weights, colour, brightness."""
    ry = rx if ry is None else ry
    return dict(c=Vector(c), rx=rx, ry=ry, dn=ry if dn is None else dn, w=w, col=col, k=k)


class Skin:
    """One skinned mesh under construction."""

    def __init__(self, name, bones, pal):
        self.name, self.pal = name, pal
        self.bones = list(bones)
        self.gi = {b: i for i, b in enumerate(self.bones)}
        self.bm = bmesh.new()
        self.col = self.bm.loops.layers.float_color.new("Col")
        self.uv = self.bm.loops.layers.uv.new("UVMap")
        self.dl = self.bm.verts.layers.deform.verify()
        self.vcl = self.bm.verts.layers.float_color.new("vc")   # a layer, not a dict: bmesh ops reallocate verts

    def rgb(self, color, k=1.0):
        c = self.pal[color] if isinstance(color, str) else color
        return (c[0] * k, c[1] * k, c[2] * k)

    def vert(self, p, w, rgb):
        v = self.bm.verts.new(p)
        if isinstance(w, str):
            w = {w: 1.0}
        tot = sum(w.values()) or 1.0
        for b, x in w.items():
            if x > 0.001:
                v[self.dl][self.gi[b]] = x / tot
        v[self.vcl] = (*rgb, 1.0)
        return v

    def loft(self, rings, color, segs=10, front=(0, -1, 0), axis=None, w=None, caps=True, smooth=True, twist=0.0):
        """Skin a tube through rings. `front` is the direction ring.ry points; ring.dn is the opposite side.
        color / w may be callables: color(p, a, i) -> rgb, w(p) -> {bone: weight}."""
        front = Vector(front)
        n = len(rings)
        vr = []
        for i, r in enumerate(rings):
            if axis is not None:
                t = Vector(axis).normalized()
            else:
                t = (rings[min(i + 1, n - 1)]["c"] - rings[max(i - 1, 0)]["c"]).normalized()
            o = front - t * front.dot(t)
            o = o.normalized() if o.length > 1e-5 else Vector((1, 0, 0))
            s = t.cross(o)
            row = []
            for k in range(segs):
                a = 2 * math.pi * k / segs + twist
                cs, sn = math.cos(a), math.sin(a)
                p = r["c"] + s * (r["rx"] * cs) + o * ((r["ry"] if sn >= 0 else r["dn"]) * sn)
                ww = r["w"] if r["w"] is not None else w
                if callable(ww):
                    ww = ww(p)
                if callable(color) and r["col"] is None:
                    c = color(p, a, i)
                    c = (c[0] * r["k"], c[1] * r["k"], c[2] * r["k"])
                else:
                    c = self.rgb(r["col"] or color, r["k"])
                row.append(self.vert(p, ww, c))
            vr.append(row)
        faces = []
        for i in range(n - 1):
            for k in range(segs):
                k2 = (k + 1) % segs
                faces.append(self.bm.faces.new((vr[i][k], vr[i][k2], vr[i + 1][k2], vr[i + 1][k])))
        if caps in (True, "start"):
            faces.append(self.bm.faces.new(vr[0]))
        if caps in (True, "end"):
            faces.append(self.bm.faces.new(vr[-1]))
        for f in faces:
            f.smooth = smooth
        bmesh.ops.recalc_face_normals(self.bm, faces=faces)
        return vr

    def tube(self, pts, r, color, w, segs=6, front=(0, -1, 0), **kw):
        return self.loft([R(p, r) for p in pts], color, segs=segs, w=w, front=front, **kw)

    def box(self, size, loc, color, w, rot=None, bevel=0.0, k=1.0):
        m = Matrix.Translation(Vector(loc)) @ (rot.to_4x4() if rot else Matrix.Identity(4)) @ Matrix.Diagonal((*size, 1.0))
        r = bmesh.ops.create_cube(self.bm, size=1.0, matrix=m)
        vs = r["verts"]
        if bevel > 0:
            edges = list({e for v in vs for e in v.link_edges})
            rb = bmesh.ops.bevel(self.bm, geom=edges, offset=bevel, segments=1, profile=0.5, affect="EDGES")
            vs = rb["verts"]
        self._own(vs, w, self.rgb(color, k))

    def ball(self, r, loc, color, w, scale=(1, 1, 1), sub=2, k=1.0, smooth=True):
        m = Matrix.Translation(Vector(loc)) @ Matrix.Diagonal((*scale, 1.0))
        res = bmesh.ops.create_icosphere(self.bm, subdivisions=sub, radius=r, matrix=m)
        self._own(res["verts"], w, self.rgb(color, k))
        for v in res["verts"]:
            for f in v.link_faces:
                f.smooth = smooth

    def _own(self, verts, w, rgb):
        if isinstance(w, str):
            w = {w: 1.0}
        for v in verts:
            if not v.is_valid:
                continue
            for b, x in w.items():
                v[self.dl][self.gi[b]] = x
            v[self.vcl] = (*rgb, 1.0)

    def finish(self, arm=None, amp=0.10, freq=7.0):
        self.bm.normal_update()
        for f in self.bm.faces:
            for lp in f.loops:
                v = lp.vert
                c = v[self.vcl]
                if c[3] < 0.5:
                    c = (1, 0, 1, 1)
                p = v.co
                nz = 1.0 + amp * (noise.noise(p * freq) * 0.7 + noise.noise(p * freq * 3.1) * 0.3)
                sh = 1.0 + 0.10 * v.normal.z                      # tops lighter, undersides darker
                lp[self.col] = (c[0] * nz * sh, c[1] * nz * sh, c[2] * nz * sh, 1.0)
                lp[self.uv].uv = (p.x + p.y * 0.61, p.z + p.y * 0.23)
        self.bm.verts.layers.float_color.remove(self.bm.verts.layers.float_color["vc"])
        me = bpy.data.meshes.new(self.name)
        self.bm.to_mesh(me)
        self.bm.free()
        ob = bpy.data.objects.new(self.name, me)
        bpy.context.scene.collection.objects.link(ob)
        for b in self.bones:
            ob.vertex_groups.new(name=b)
        if arm:
            ob.parent = arm
            ob.modifiers.new("Armature", "ARMATURE").object = arm
        print(f"{self.name}: {len(me.polygons)} faces")
        return ob


def armature(name, spec):
    """spec: (bone, head, tail, parent, deform). Returns the armature object."""
    if bpy.context.scene is None:
        bpy.context.window.scene = bpy.data.scenes.new("Scene")
    arm = bpy.data.armatures.new(name)
    ob = bpy.data.objects.new(name, arm)
    bpy.context.scene.collection.objects.link(ob)
    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.mode_set(mode="EDIT")
    for (n, head, tail, parent, deform) in spec:
        eb = arm.edit_bones.new(n)
        eb.head, eb.tail = Vector(head), Vector(tail)
        eb.roll = 0.0
        eb.use_deform = deform
        if parent:
            eb.parent = arm.edit_bones[parent]
    bpy.ops.object.mode_set(mode="OBJECT")
    for pb in ob.pose.bones:
        pb.rotation_mode = "QUATERNION"
    return ob


def ik(ob, bone, target, chain):
    c = ob.pose.bones[bone].constraints.new("IK")
    c.target, c.subtarget, c.chain_count = ob, target, chain
    c.iterations = 200


def copy_rot(ob, bone, target):
    c = ob.pose.bones[bone].constraints.new("COPY_ROTATION")
    c.target, c.subtarget = ob, target
    c.target_space = c.owner_space = "WORLD"


class Anim:
    """Keys bones using armature-space axes and offsets, so gait maths stays readable."""

    def __init__(self, ob):
        self.ob = ob
        self.rest = {b.name: b.matrix_local.to_3x3() for b in ob.data.bones}
        ob.animation_data_create()
        self.actions = []

    def begin(self, name):
        for pb in self.ob.pose.bones:
            pb.location = (0, 0, 0)
            pb.rotation_quaternion = (1, 0, 0, 0)
        act = bpy.data.actions.new(name)
        self.ob.animation_data.action = act
        self.actions.append(act)

    def rot(self, bone, frame, *pairs):
        """pairs: (axis 'X'|'Y'|'Z' or Vector, angle) applied in order, in rest armature space."""
        rw = Matrix.Identity(3)
        for ax, ang in pairs:
            rw = Matrix.Rotation(ang, 3, ax) @ rw
        m = self.rest[bone]
        pb = self.ob.pose.bones[bone]
        pb.rotation_quaternion = (m.inverted() @ rw @ m).to_quaternion()
        pb.keyframe_insert("rotation_quaternion", frame=frame)

    def loc(self, bone, frame, d):
        pb = self.ob.pose.bones[bone]
        pb.location = self.rest[bone].inverted() @ Vector(d)
        pb.keyframe_insert("location", frame=frame)

    def stash(self):
        ad = self.ob.animation_data
        ad.action = None
        for act in self.actions:
            tr = ad.nla_tracks.new()
            tr.name = act.name
            st = tr.strips.new(act.name, 0, act)
            try:
                if st.action_slot is None and act.slots:
                    st.action_slot = act.slots[0]
            except AttributeError:
                pass
        for pb in self.ob.pose.bones:
            pb.location = (0, 0, 0)
            pb.rotation_quaternion = (1, 0, 0, 0)


def export(path):
    for o in bpy.data.objects:
        o.select_set(True)
    kw = dict(filepath=path, export_format="GLB", export_apply=False, export_yup=True, export_normals=True,
              export_materials="EXPORT", export_extras=False, export_skins=True, export_animations=True,
              export_animation_mode="NLA_TRACKS", export_force_sampling=True, export_frame_step=1,
              export_def_bones=False, export_optimize_animation_size=False, export_texcoords=True)
    try:
        bpy.ops.export_scene.gltf(**kw, export_vertex_color="ACTIVE", export_all_vertex_colors=True)
    except TypeError as e:
        print("fallback export:", e)
        bpy.ops.export_scene.gltf(**kw)
    print("WROTE", path)
