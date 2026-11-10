"""Art test 2: a Longshank (tall feral dog, head always high), rigged and walking. Run headless:
  blender -b -P build_longshank.py -- <out.glb>
Faces -Y. Left is +X. All four paws follow IK targets, so they stay planted through a four-beat walk.
"""
import bpy, sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mathutils import Vector, noise
import rig
from rig import R

OUT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "longshank.glb"
random.seed(7)
rig.reset_scene()
bpy.context.scene.render.fps = 30

PAL = rig.palette({
    "fur": "#6f6456", "fur_dk": "#2c2622", "fur_lt": "#b9aa8e", "muzzle": "#3a312b", "nose": "#141211",
    "eye": "#d9a441", "paw": "#3d342d", "ear_in": "#8a6458", "scar": "#9a8f85",
})

FX, HX = 0.105, 0.11
SPEC = [
    ("pelvis", (0, 0.46, 0.96), (0, 0.22, 0.99), None, True),
    ("spine", (0, 0.22, 0.99), (0, -0.06, 0.985), "pelvis", True),
    ("chest", (0, -0.06, 0.985), (0, -0.34, 0.97), "spine", True),
    ("neck1", (0, -0.34, 1.0), (0, -0.46, 1.14), "chest", True),
    ("neck2", (0, -0.46, 1.14), (0, -0.57, 1.27), "neck1", True),
    ("head", (0, -0.57, 1.27), (0, -0.90, 1.20), "neck2", True),
    ("tail1", (0, 0.50, 0.94), (0, 0.64, 0.74), "pelvis", True),
    ("tail2", (0, 0.64, 0.74), (0, 0.74, 0.52), "tail1", True),
    ("tail3", (0, 0.74, 0.52), (0, 0.86, 0.40), "tail2", True),
]
for s, sx in ((".L", 1), (".R", -1)):
    fx, hx = FX * sx, HX * sx
    SPEC += [
        ("ear" + s, (0.06 * sx, -0.55, 1.355), (0.10 * sx, -0.47, 1.38), "head", True),
        ("humerus" + s, (fx, -0.33, 0.84), (fx, -0.22, 0.60), "chest", True),
        ("radius" + s, (fx, -0.22, 0.60), (fx, -0.25, 0.27), "humerus" + s, True),
        ("pastern" + s, (fx, -0.25, 0.27), (fx, -0.275, 0.07), "radius" + s, True),
        ("fpaw" + s, (fx, -0.275, 0.07), (fx, -0.37, 0.03), "pastern" + s, True),
        ("ik_fpaw" + s, (fx, -0.275, 0.07), (fx, -0.37, 0.03), None, False),
        ("thigh" + s, (hx, 0.42, 0.88), (hx, 0.30, 0.58), "pelvis", True),
        ("shin" + s, (hx, 0.30, 0.58), (hx, 0.53, 0.31), "thigh" + s, True),
        ("hock" + s, (hx, 0.53, 0.31), (hx, 0.49, 0.07), "shin" + s, True),
        ("hpaw" + s, (hx, 0.49, 0.07), (hx, 0.39, 0.03), "hock" + s, True),
        ("ik_hpaw" + s, (hx, 0.49, 0.07), (hx, 0.39, 0.03), None, False),
    ]
arm = rig.armature("Longshank", SPEC)
BONES = [s[0] for s in SPEC if s[4]]
for s in (".L", ".R"):
    rig.ik(arm, "pastern" + s, "ik_fpaw" + s, 3)
    rig.copy_rot(arm, "fpaw" + s, "ik_fpaw" + s)
    rig.ik(arm, "hock" + s, "ik_hpaw" + s, 3)
    rig.copy_rot(arm, "hpaw" + s, "ik_hpaw" + s)

dog = rig.Skin("Dog", BONES, PAL)


def mix(a, b, t):
    t = max(0.0, min(1.0, t))
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def coat(p, a, i):
    """Brindle: dark saddle on top, pale belly, broken dark bands along the body."""
    up = math.sin(a)
    c = mix(PAL["fur"], PAL["fur_lt"], (-up - 0.25) * 1.6)
    c = mix(c, PAL["fur_dk"], (up - 0.35) * 1.3)
    band = math.sin(p.y * 46.0 + p.z * 14.0 + 5.0 * noise.noise(Vector((p.x * 3.0, p.y * 4.0, p.z * 5.0))))
    if band > 0.35 and up > -0.7:
        c = mix(c, PAL["fur_dk"], 0.75)
    return c


def leg(p, a, i):
    c = mix(PAL["fur"], PAL["paw"], (0.42 - p.z) * 2.2)           # dark stockings
    if noise.noise(Vector((p.x * 3.0, p.y * 4.0, p.z * 11.0))) > 0.22 and p.z > 0.4:
        c = mix(c, PAL["fur_dk"], 0.5)
    return c


# ---------------------------------------------------------------- torso: deep chest, tucked loin
dog.loft([
    R((0, 0.57, 0.925), 0.045, 0.045, 0.06, w="pelvis"), R((0, 0.49, 0.94), 0.105, 0.10, 0.14, w="pelvis"),
    R((0, 0.37, 0.95), 0.122, 0.112, 0.17, w="pelvis"), R((0, 0.21, 0.955), 0.10, 0.10, 0.125, w={"pelvis": .5, "spine": .5}),
    R((0, 0.06, 0.95), 0.10, 0.105, 0.145, w="spine"), R((0, -0.09, 0.94), 0.118, 0.12, 0.215, w={"spine": .5, "chest": .5}),
    R((0, -0.23, 0.93), 0.13, 0.145, 0.275, w="chest"), R((0, -0.35, 0.94), 0.118, 0.145, 0.245, w="chest"),
    R((0, -0.43, 0.96), 0.075, 0.105, 0.15, w="chest"),
], coat, segs=14, front=(0, 0, 1))
dog.loft([                                                                        # neck, carried high
    R((0, -0.29, 0.97), 0.105, 0.12, 0.14, w="chest"), R((0, -0.40, 1.07), 0.088, 0.10, 0.115, w={"chest": .4, "neck1": .6}),
    R((0, -0.49, 1.18), 0.074, 0.085, 0.095, w={"neck1": .5, "neck2": .5}), R((0, -0.56, 1.26), 0.068, 0.075, 0.085, w={"neck2": .6, "head": .4}),
    R((0, -0.59, 1.29), 0.06, 0.06, 0.07, w="head"),
], lambda p, a, i: mix(mix(PAL["fur"], PAL["fur_lt"], (math.sin(a) - 0.3) * 1.5), PAL["fur_dk"], (-math.sin(a) - 0.5) * 1.5), segs=10, front=(0, -1, 0))


def face(p, a, i):
    c = mix(PAL["fur"], PAL["muzzle"], (-0.70 - p.y) * 6.0)                       # dark mask toward the nose
    return mix(c, PAL["fur_dk"], (math.sin(a) - 0.5) * 1.2)


dog.loft([                                                                        # skull and long muzzle
    R((0, -0.50, 1.295), 0.05, 0.05, 0.06, w="head"), R((0, -0.57, 1.30), 0.086, 0.078, 0.088, w="head"),
    R((0, -0.66, 1.285), 0.08, 0.068, 0.082, w="head"), R((0, -0.73, 1.255), 0.056, 0.045, 0.066, w="head"),
    R((0, -0.84, 1.232), 0.046, 0.036, 0.054, w="head"), R((0, -0.93, 1.212), 0.038, 0.03, 0.042, w="head"),
    R((0, -0.957, 1.207), 0.022, 0.02, 0.026, w="head", col="nose"),
], face, segs=10, front=(0, 0, 1))
dog.ball(0.027, (0, -0.95, 1.22), "nose", "head", scale=(1.1, 0.9, 0.8), sub=1)
for sx in (1, -1):
    dog.ball(0.017, (0.062 * sx, -0.688, 1.312), "eye", "head", scale=(0.7, 1.1, 0.9), sub=1)
    dog.ball(0.008, (0.07 * sx, -0.696, 1.313), "nose", "head", sub=1)
    dog.box((0.006, 0.17, 0.01), (0.043 * sx, -0.85, 1.195), "nose", "head")        # lip line
    E = "ear.L" if sx > 0 else "ear.R"
    dog.loft([R((0.06 * sx, -0.555, 1.355), 0.036, 0.014, w={"head": .6, E: .4}), R((0.088 * sx, -0.51, 1.392), 0.03, 0.012, w=E),
              R((0.105 * sx, -0.455, 1.365), 0.006, 0.004, w=E)], "fur_dk", segs=6, front=(0, -1, 0))   # rose ear, folded back

dog.loft([                                                                        # tail, low and hooked
    R((0, 0.53, 0.925), 0.045, w={"pelvis": .6, "tail1": .4}), R((0, 0.64, 0.74), 0.04, 0.04, 0.05, w={"tail1": .5, "tail2": .5}),
    R((0, 0.74, 0.52), 0.04, 0.04, 0.055, w={"tail2": .5, "tail3": .5}, k=0.8), R((0, 0.82, 0.43), 0.03, w="tail3", k=0.6),
    R((0, 0.875, 0.405), 0.006, w="tail3", col="fur_dk"),
], "fur", segs=7, front=(0, 1, 0))

# ---------------------------------------------------------------- legs
for s, sx in ((".L", 1), (".R", -1)):
    x = FX * sx
    H, Rd, P, Pw = "humerus" + s, "radius" + s, "pastern" + s, "fpaw" + s
    dog.loft([
        R((x * 0.95, -0.335, 0.93), 0.064, 0.109, 0.122, w={"chest": .7, H: .3}), R((x, -0.305, 0.77), 0.064, 0.090, 0.096, w={"chest": .2, H: .8}),
        R((x, -0.225, 0.60), 0.049, 0.059, 0.074, w={H: .5, Rd: .5}), R((x, -0.235, 0.45), 0.040, 0.042, 0.051, w=Rd),
        R((x, -0.25, 0.27), 0.038, 0.042, 0.045, w={Rd: .5, P: .5}), R((x, -0.262, 0.17), 0.032, 0.033, 0.036, w=P),
        R((x, -0.275, 0.065), 0.036, 0.038, 0.038, w={P: .5, Pw: .5}),
    ], leg, segs=8)
    dog.loft([R((x, -0.235, 0.042), 0.030, 0.032, 0.037, w=Pw), R((x, -0.30, 0.04), 0.042, 0.032, 0.039, w=Pw),
              R((x, -0.36, 0.032), 0.042, 0.024, 0.032, w=Pw), R((x, -0.39, 0.026), 0.024, 0.013, 0.024, w=Pw)],
             "paw", segs=8, front=(0, 0, 1))
    x = HX * sx
    T, Sh, Hk, Pw = "thigh" + s, "shin" + s, "hock" + s, "hpaw" + s
    dog.loft([
        R((x * 0.9, 0.43, 0.93), 0.077, 0.128, 0.141, w={"pelvis": .7, T: .3}), R((x, 0.375, 0.75), 0.074, 0.122, 0.128, w={"pelvis": .2, T: .8}),
        R((x, 0.30, 0.58), 0.051, 0.064, 0.079, w={T: .5, Sh: .5}), R((x, 0.40, 0.45), 0.040, 0.044, 0.059, w=Sh),
        R((x, 0.53, 0.31), 0.035, 0.038, 0.046, w={Sh: .5, Hk: .5}), R((x, 0.51, 0.19), 0.031, 0.031, 0.033, w=Hk),
        R((x, 0.49, 0.065), 0.035, 0.036, 0.038, w={Hk: .5, Pw: .5}),
    ], leg, segs=8)
    dog.loft([R((x, 0.53, 0.042), 0.030, 0.032, 0.037, w=Pw), R((x, 0.46, 0.04), 0.042, 0.032, 0.039, w=Pw),
              R((x, 0.40, 0.032), 0.042, 0.024, 0.032, w=Pw), R((x, 0.37, 0.026), 0.024, 0.013, 0.024, w=Pw)],
             "paw", segs=8, front=(0, 0, 1))


# ---------------------------------------------------------------- shag: rough tufts break the smooth tubes
def tuft(base, d, length, r, w, color="fur_dk"):
    """A flat lock of hair lying along direction d."""
    base, d = Vector(base), Vector(d).normalized()
    up = Vector((0, 0, 1)) - d * d.z
    up = up.normalized() if up.length > 0.1 else Vector((0, 1, 0))
    dog.loft([R(base - d * 0.03, r * 0.8, r * 0.3, w=w), R(base + d * length * 0.45, r, r * 0.34, w=w), R(base + d * length, r * 0.25, 0.004, w=w)],
             color, segs=6, front=up, caps=False)


for i in range(6):                                                                 # mane down the nape and over the withers
    u = i / 5
    b = Vector((random.uniform(-0.012, 0.012), -0.42 + 0.22 * u, 1.275 - 0.165 * u))
    w = {"neck2": 1.0} if u < 0.3 else ({"neck1": 1.0} if u < 0.65 else {"chest": 1.0})
    tuft(b, (random.uniform(-0.15, 0.15), 0.9, 0.05 if u < 0.7 else -0.2), random.uniform(0.06, 0.085), 0.04, w)
for i in range(4):                                                                 # hackles along the back
    u = i / 3
    tuft((random.uniform(-0.01, 0.01), -0.16 + 0.42 * u, 1.065 - 0.012 * u), (0, 1, -0.05), 0.08, 0.035, "chest" if u < 0.3 else ("spine" if u < 0.8 else "pelvis"))
dog.box((0.006, 0.09, 0.012), (0.074, -0.63, 1.335), "scar", "head")                 # an old scar over the left brow
dog.finish(arm, amp=0.13, freq=9.0)

# ---------------------------------------------------------------- animation
an = rig.Anim(arm)
TAU = 2 * math.pi
N_WALK, DUTY, REACH = 24, 0.65, 0.22
SPEED = 2 * REACH / DUTY / (N_WALK / 30.0)
print("WALK_SPEED", round(SPEED, 3))
LEGS = (("hpaw.L", 0.0, ("thigh.L", "shin.L", "hock.L")), ("fpaw.L", 0.25, ("humerus.L", "radius.L", "pastern.L")),
        ("hpaw.R", 0.5, ("thigh.R", "shin.R", "hock.R")), ("fpaw.R", 0.75, ("humerus.R", "radius.R", "pastern.R")))


def paw_path(ph, lift):
    ph %= 1.0
    if ph < DUTY:
        s = ph / DUTY
        y = -REACH + 2 * REACH * s
        pitch = 0.5 * ((s - 0.8) / 0.2) ** 1.5 if s > 0.8 else 0.0
        z = 0.06 * math.sin(pitch)
    else:
        s = (ph - DUTY) / (1 - DUTY)
        e = 0.5 - 0.5 * math.cos(math.pi * s)
        y = REACH - 2 * REACH * e
        pitch = 0.5 * (1 - s) + 0.9 * math.sin(math.pi * s) * (1 - s * 0.6) - 0.15 * s
        z = 0.03 * (1 - s) ** 2 + lift * math.sin(math.pi * s)
    return y, z, pitch


an.begin("walk-loop")
for f in range(N_WALK + 1):
    t = f / N_WALK
    s1, c1 = math.sin(TAU * t), math.cos(TAU * t)
    s2 = math.sin(2 * TAU * t)
    an.loc("pelvis", f, (0.012 * s1, 0, -0.035 + 0.01 * s2))
    an.rot("pelvis", f, ("Z", 0.05 * c1), ("Y", 0.03 * s1), ("X", 0.015 * s2))
    an.rot("spine", f, ("Z", -0.05 * c1))
    an.rot("chest", f, ("Z", -0.05 * c1), ("Y", -0.05 * math.sin(TAU * (t - 0.25))), ("X", -0.02 * s2))
    an.rot("neck1", f, ("X", 0.05 * math.sin(2 * TAU * (t - 0.1))), ("Z", 0.03 * c1))
    an.rot("neck2", f, ("X", 0.03 * math.sin(2 * TAU * (t - 0.15))), ("Z", 0.02 * c1))
    an.rot("head", f, ("X", -0.07 * math.sin(2 * TAU * (t - 0.12))))
    an.rot("tail1", f, ("Z", 0.12 * math.sin(TAU * (t - 0.1))))
    an.rot("tail2", f, ("Z", 0.16 * math.sin(TAU * (t - 0.22))), ("X", 0.04 * s2))
    an.rot("tail3", f, ("Z", 0.2 * math.sin(TAU * (t - 0.34))))
    an.rot("ear.L", f, ("X", 0.05 * s2))
    an.rot("ear.R", f, ("X", 0.05 * s2))
    for paw, off, chain in LEGS:
        y, z, pitch = paw_path(t - off, 0.10 if paw[0] == "f" else 0.08)
        an.loc("ik_" + paw, f, (0, y + (0.03 if paw[0] == "f" else -0.04), z))
        an.rot("ik_" + paw, f, ("X", pitch))
        an.rot(paw, f)
        for b in chain:
            an.rot(b, f)

N_IDLE = 90
an.begin("idle-loop")
for f in range(0, N_IDLE + 1, 3):
    t = f / N_IDLE
    br = math.sin(TAU * t * 3)
    look = math.sin(TAU * t)
    an.loc("pelvis", f, (0, 0, -0.02 + 0.002 * br))
    an.rot("pelvis", f)
    an.rot("spine", f, ("X", 0.006 * br))
    an.rot("chest", f, ("X", -0.01 * br))
    an.rot("neck1", f, ("Z", 0.22 * look), ("X", -0.04))
    an.rot("neck2", f, ("Z", 0.25 * look), ("X", -0.05))
    an.rot("head", f, ("Z", 0.2 * look), ("X", 0.08 + 0.04 * math.cos(TAU * t * 2)))
    an.rot("tail1", f, ("Z", 0.06 * math.sin(TAU * t * 2)), ("X", 0.1))
    an.rot("tail2", f, ("Z", 0.09 * math.sin(TAU * (t * 2 - 0.15))))
    an.rot("tail3", f, ("Z", 0.12 * math.sin(TAU * (t * 2 - 0.3))))
    an.rot("ear.L", f, ("Z", 0.25 * max(0.0, math.sin(TAU * t * 3))))
    an.rot("ear.R", f, ("Z", -0.2 * max(0.0, math.sin(TAU * (t * 3 + 0.4)))))
    for paw, off, chain in LEGS:
        an.loc("ik_" + paw, f, (0, 0, 0))
        an.rot("ik_" + paw, f)
        an.rot(paw, f)
        for b in chain:
            an.rot(b, f)
an.stash()
bpy.context.scene.frame_start, bpy.context.scene.frame_end = 0, N_IDLE
rig.export(OUT)
