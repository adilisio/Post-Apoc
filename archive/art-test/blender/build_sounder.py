"""Art test 2: the Sounder, rigged and walking. Run headless:
  blender -b -P build_sounder.py -- <out.glb>
Faces -Y. Left is +X. The staff is its own bone; the right hand follows it by IK, the feet follow IK targets.
"""
import bpy, sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mathutils import Vector, Matrix
import rig
from rig import R

OUT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "sounder.glb"
rig.reset_scene()
bpy.context.scene.render.fps = 30

PAL = rig.palette({
    "oilskin": "#77703f", "oilskin_dk": "#4b4a30", "oilskin_lt": "#8f8850", "trouser": "#3b3a36",
    "boot": "#3a2c22", "leather": "#5a3e2a", "leather_lt": "#7d5a3a", "skin": "#a8765a", "skin_dk": "#7e5440",
    "dark": "#191715", "hair": "#2a221d", "band": "#a8473a", "hose": "#b39a6a", "hose_dk": "#8a7650",
    "bladder": "#a58c62", "wood": "#7b5d3e", "wood_dk": "#4f3a28", "rope": "#b79c6b", "tin": "#8d9291",
    "tin_dk": "#5f6566", "flame": "#ffc070", "chalk": "#d9d2bf",
})

SPEC = [
    ("hips", (0, 0, 0.96), (0, 0, 1.10), None, True),
    ("spine", (0, 0, 1.10), (0, 0.01, 1.26), "hips", True),
    ("chest", (0, 0.01, 1.26), (0, 0, 1.46), "spine", True),
    ("neck", (0, 0, 1.46), (0, -0.01, 1.56), "chest", True),
    ("head", (0, -0.01, 1.56), (0, -0.01, 1.78), "neck", True),
]
for s, sx in ((".L", 1), (".R", -1)):
    SPEC += [
        ("thigh" + s, (0.095 * sx, 0, 0.93), (0.095 * sx, -0.03, 0.50), "hips", True),
        ("shin" + s, (0.095 * sx, -0.03, 0.50), (0.095 * sx, 0.01, 0.09), "thigh" + s, True),
        ("foot" + s, (0.095 * sx, 0.01, 0.09), (0.095 * sx, -0.17, 0.03), "shin" + s, True),
        ("ik_foot" + s, (0.095 * sx, 0.01, 0.09), (0.095 * sx, -0.17, 0.03), None, False),
    ]
SPEC += [
    ("upper_arm.L", (0.2, 0, 1.42), (0.245, 0.02, 1.14), "chest", True),
    ("forearm.L", (0.245, 0.02, 1.14), (0.265, -0.03, 0.90), "upper_arm.L", True),
    ("hand.L", (0.265, -0.03, 0.90), (0.27, -0.05, 0.79), "forearm.L", True),
    ("upper_arm.R", (-0.2, 0, 1.42), (-0.26, 0.03, 1.15), "chest", True),
    ("forearm.R", (-0.26, 0.03, 1.15), (-0.27, -0.22, 1.20), "upper_arm.R", True),
    ("hand.R", (-0.27, -0.22, 1.20), (-0.27, -0.31, 1.22), "forearm.R", True),
    ("staff", (-0.27, -0.30, 0.0), (-0.27, -0.30, 2.3), None, True),
    ("ik_hand.R", (-0.27, -0.22, 1.20), (-0.27, -0.31, 1.22), "staff", False),
]
arm = rig.armature("Sounder", SPEC)
BONES = [s[0] for s in SPEC if s[4]]
for s in (".L", ".R"):
    rig.ik(arm, "shin" + s, "ik_foot" + s, 2)
    rig.copy_rot(arm, "foot" + s, "ik_foot" + s)
rig.ik(arm, "forearm.R", "ik_hand.R", 2)
rig.copy_rot(arm, "hand.R", "ik_hand.R")

body = rig.Skin("Body", BONES, PAL)
gear = rig.Skin("Gear", BONES, PAL)
flames = rig.Skin("Flames", BONES, PAL)

# ---------------------------------------------------------------- legs and boots
for s, sx in ((".L", 1), (".R", -1)):
    x = 0.095 * sx
    T, S, F = "thigh" + s, "shin" + s, "foot" + s
    body.loft([
        R((x, 0, 0.92), 0.095, 0.10, w={"hips": .5, T: .5}), R((x, -0.01, 0.72), 0.085, 0.09, w=T),
        R((x, -0.03, 0.52), 0.07, 0.078, 0.07, w={T: .5, S: .5}), R((x, -0.025, 0.44), 0.064, 0.066, 0.07, w=S),
        R((x, -0.005, 0.33), 0.06, 0.058, 0.076, w=S), R((x, 0.005, 0.25), 0.055, 0.055, 0.065, w=S, k=0.85),
    ], "trouser", segs=10)
    body.loft([                                                                   # boot shaft, wrapped gaiter
        R((x, 0.0, 0.30), 0.072, 0.07, 0.082, w=S, col="leather"), R((x, 0.0, 0.285), 0.066, 0.064, 0.076, w=S, col="leather"),
        R((x, 0.004, 0.20), 0.062, 0.062, 0.07, w=S), R((x, 0.008, 0.12), 0.058, 0.06, 0.064, w={S: .6, F: .4}),
        R((x, 0.01, 0.05), 0.056, 0.06, 0.062, w=F, k=0.8),
    ], "boot", segs=10)
    body.loft([                                                                   # foot
        R((x, 0.075, 0.042), 0.04, 0.036, 0.04, w=F), R((x, 0.03, 0.058), 0.054, 0.06, 0.056, w=F),
        R((x, -0.06, 0.05), 0.058, 0.05, 0.048, w=F), R((x, -0.13, 0.04), 0.056, 0.036, 0.038, w=F),
        R((x, -0.185, 0.034), 0.042, 0.026, 0.032, w=F), R((x, -0.20, 0.03), 0.02, 0.014, 0.024, w=F, k=0.8),
    ], "boot", segs=10, front=(0, 0, 1))
    for i, z in enumerate((0.23, 0.185, 0.14)):                                    # gaiter bindings
        gear.loft([R((x, 0.004, z + 0.012), 0.066, 0.066, 0.074), R((x, 0.004, z - 0.012), 0.066, 0.066, 0.074)],
                  "rope", segs=10, w=S, caps=False, axis=(0, 0, -1))


# ---------------------------------------------------------------- coat
def skirt(a):
    def w(p):
        s = max(-1.0, min(1.0, p.x / 0.12))
        return {"hips": 1 - a, "thigh.L": a * (0.5 + 0.5 * s), "thigh.R": a * (0.5 - 0.5 * s)}
    return w


def coat_col(p, a, i):
    d = abs(a - math.pi / 2)
    base = PAL["oilskin"]
    k = 0.62 if d < 0.2 else 1.0                                                   # the front placket
    if abs(a - math.pi * 1.5) < 0.2:
        k = 0.86                                                                   # back seam
    return (base[0] * k, base[1] * k, base[2] * k)


body.loft([
    R((0, 0, 1.475), 0.105, 0.09, w="chest", k=0.8),
    R((0, 0, 1.44), 0.20, 0.11, 0.12, w="chest"), R((0, 0, 1.34), 0.208, 0.126, 0.132, w="chest"),
    R((0, 0.005, 1.21), 0.186, 0.12, 0.126, w={"chest": .5, "spine": .5}),
    R((0, 0.005, 1.09), 0.172, 0.116, 0.122, w={"spine": .5, "hips": .5}),
    R((0, 0, 0.97), 0.192, 0.132, 0.142, w="hips"),
    R((0, 0, 0.82), 0.216, 0.152, 0.162, w=skirt(0.45)), R((0, 0, 0.66), 0.236, 0.168, 0.178, w=skirt(0.65), k=0.92),
    R((0, 0, 0.54), 0.252, 0.182, 0.192, w=skirt(0.78), k=0.78),
    R((0, 0, 0.515), 0.256, 0.186, 0.196, w=skirt(0.8), k=0.6),
], coat_col, segs=16, axis=(0, 0, -1), caps="start")
body.loft([                                                                       # high collar, open at the top
    R((0, 0.0, 1.455), 0.118, 0.102, 0.108, w="chest"), R((0, -0.002, 1.54), 0.108, 0.104, 0.11, w={"chest": .6, "neck": .4}),
    R((0, -0.004, 1.615), 0.118, 0.116, 0.124, w={"chest": .4, "neck": .6}),
    R((0, -0.004, 1.632), 0.124, 0.122, 0.13, w={"chest": .4, "neck": .6}, k=0.8),
], "oilskin_lt", segs=14, axis=(0, 0, 1), caps=False)
body.loft([                                                                       # shoulder yoke
    R((0, 0, 1.485), 0.12, 0.10, 0.105, w="chest"), R((0, 0, 1.455), 0.225, 0.13, 0.14, w="chest"),
    R((0, 0, 1.39), 0.25, 0.15, 0.158, w="chest"), R((0, 0, 1.365), 0.252, 0.152, 0.16, w="chest", k=0.7),
], "oilskin_dk", segs=16, axis=(0, 0, -1), caps=False)
gear.loft([R((0, 0.004, 1.115), 0.18, 0.124, 0.13), R((0, 0.004, 1.06), 0.182, 0.126, 0.132)], "leather", segs=16,
          w={"spine": .5, "hips": .5}, axis=(0, 0, -1), caps=False)                # belt
gear.box((0.05, 0.02, 0.06), (0.0, -0.128, 1.088), "tin", {"spine": .5, "hips": .5}, bevel=0.006)
for z in (1.38, 1.28, 1.18, 0.98, 0.88):                                           # toggles down the front
    wz = "chest" if z > 1.25 else ("spine" if z > 1.1 else "hips")
    gear.box((0.022, 0.016, 0.04), (0.012, -0.132 - (0.02 if z < 1.0 else 0) - (0.008 if z > 1.3 else 0), z), "wood_dk", wz, bevel=0.005)
gear.box((0.15, 0.07, 0.17), (-0.13, 0.15, 0.94), "leather_lt", "hips", rot=Matrix.Rotation(0.5, 3, "Z"), bevel=0.02)   # satchel
gear.box((0.16, 0.076, 0.06), (-0.13, 0.15, 1.01), "leather", "hips", rot=Matrix.Rotation(0.5, 3, "Z"), bevel=0.015)
gear.box((0.035, 0.03, 0.2), (0.2, -0.03, 0.96), "leather", "hips", rot=Matrix.Rotation(0.15, 3, "X"), bevel=0.008)      # knife
gear.box((0.03, 0.026, 0.07), (0.2, -0.045, 1.085), "wood", "hips", rot=Matrix.Rotation(0.15, 3, "X"), bevel=0.008)
for i in range(3):                                                                 # chalk sticks in a belt loop
    gear.box((0.016, 0.016, 0.07), (0.09 + i * 0.022, -0.135, 1.05), "chalk", {"spine": .5, "hips": .5}, bevel=0.003)

# ---------------------------------------------------------------- arms
body.loft([
    R((0.195, 0, 1.425), 0.066, w={"chest": .6, "upper_arm.L": .4}), R((0.215, 0.006, 1.33), 0.06, w="upper_arm.L"),
    R((0.245, 0.02, 1.14), 0.052, w={"upper_arm.L": .5, "forearm.L": .5}), R((0.255, 0.0, 1.03), 0.048, w="forearm.L"),
    R((0.264, -0.026, 0.925), 0.05, w="forearm.L"), R((0.265, -0.03, 0.905), 0.052, w="forearm.L", k=0.7),
], "oilskin", segs=10)
body.loft([
    R((0.265, -0.03, 0.915), 0.03, 0.024, w="hand.L"), R((0.268, -0.04, 0.86), 0.04, 0.024, w="hand.L"),
    R((0.27, -0.052, 0.805), 0.036, 0.022, w="hand.L"), R((0.27, -0.056, 0.78), 0.02, 0.014, w="hand.L", k=0.85),
], "skin", segs=8, front=(1, 0, 0))
body.tube([(0.262, -0.06, 0.87), (0.258, -0.085, 0.835)], 0.012, "skin", "hand.L", segs=5)
body.loft([
    R((-0.195, 0, 1.425), 0.066, w={"chest": .6, "upper_arm.R": .4}), R((-0.225, 0.012, 1.31), 0.06, w="upper_arm.R"),
    R((-0.26, 0.03, 1.15), 0.054, w={"upper_arm.R": .5, "forearm.R": .5}), R((-0.265, -0.09, 1.172), 0.049, w="forearm.R"),
    R((-0.27, -0.195, 1.196), 0.05, w="forearm.R"), R((-0.27, -0.21, 1.2), 0.052, w="forearm.R", k=0.7),
], "oilskin", segs=10, front=(0, 0, 1))
body.loft([R((-0.27, -0.20, 1.2), 0.028, 0.03, w="hand.R"), R((-0.27, -0.255, 1.212), 0.036, 0.04, w="hand.R"),
           R((-0.27, -0.30, 1.22), 0.04, 0.045, w="hand.R"), R((-0.27, -0.335, 1.225), 0.03, 0.04, w="hand.R"),
           R((-0.27, -0.345, 1.226), 0.012, 0.02, w="hand.R", k=0.85)], "skin", segs=8, front=(0, 0, 1))

# ---------------------------------------------------------------- head and hat
body.loft([
    R((0, -0.008, 1.50), 0.05, 0.055, w="neck", k=0.8), R((0, -0.012, 1.56), 0.052, 0.062, 0.06, w="neck", k=0.85),
    R((0, -0.016, 1.59), 0.064, 0.078, 0.072, w="head"), R((0, -0.016, 1.635), 0.075, 0.09, 0.086, w="head"),
    R((0, -0.012, 1.685), 0.078, 0.09, 0.096, w="head", k=0.9), R((0, -0.006, 1.735), 0.074, 0.084, 0.092, w="head"),
    R((0, 0, 1.775), 0.05, 0.06, 0.065, w="head"),
], "skin", segs=12, axis=(0, 0, 1))
body.loft([R((0, -0.098, 1.672), 0.012, 0.008, 0.01, w="head"), R((0, -0.116, 1.642), 0.017, 0.012, 0.016, w="head"),
           R((0, -0.106, 1.622), 0.014, 0.006, 0.012, w="head", k=0.85)], "skin", segs=6, front=(0, -1, 0))             # nose
for sx in (1, -1):
    body.ball(0.0125, (0.031 * sx, -0.094, 1.672), "dark", "head", scale=(1.3, 0.6, 0.8), sub=1)                         # eyes
    body.box((0.04, 0.012, 0.01), (0.032 * sx, -0.096, 1.69), "hair", "head")                                            # brow
    body.ball(0.02, (0.078 * sx, -0.01, 1.655), "skin_dk", "head", scale=(0.5, 1, 1.4), sub=1)                           # ear
body.box((0.05, 0.01, 0.008), (0, -0.1, 1.6), "skin_dk", "head")                                                         # mouth
body.loft([R((0, 0.03, 1.60), 0.07, 0.05, 0.07, w="head"), R((0, 0.02, 1.68), 0.082, 0.07, 0.10, w="head"),
           R((0, 0.01, 1.74), 0.08, 0.08, 0.098, w="head")], "hair", segs=10, axis=(0, 0, 1))
gear.loft([R((0, 0.02, 1.722), 0.215, 0.20, 0.265, w="head", k=0.8), R((0, 0.012, 1.738), 0.15, 0.15, 0.19, w="head"),
           R((0, 0.004, 1.748), 0.086, 0.098, 0.104, w="head")], "oilskin_dk", segs=16, axis=(0, 0, 1), caps=False)      # brim
gear.loft([R((0, 0.004, 1.742), 0.087, 0.099, 0.105, w="head", col="band"), R((0, 0.004, 1.772), 0.086, 0.097, 0.103, w="head", col="band"),
           R((0, 0.004, 1.775), 0.085, 0.096, 0.102, w="head"), R((0, 0.006, 1.83), 0.076, 0.086, 0.092, w="head"),
           R((0, 0.008, 1.858), 0.05, 0.058, 0.062, w="head"), R((0, 0.008, 1.866), 0.012, w="head")],
          "oilskin_dk", segs=16, axis=(0, 0, 1), caps="end")                                                             # crown

# ---------------------------------------------------------------- air bladder and coiled hose
C, A, Bv = Vector((-0.01, 0, 1.225)), Vector((0.185, 0, 0.245)), Vector((0, 1, 0))
N = A.cross(Bv).normalized()


def torso_r(z, front):
    """Coat radius toward front/back at height z, read off the coat rings."""
    pts = [(1.44, 0.11, 0.12), (1.34, 0.126, 0.132), (1.21, 0.12, 0.126), (1.09, 0.116, 0.122), (0.97, 0.132, 0.142)]
    for (z0, f0, b0), (z1, f1, b1) in zip(pts, pts[1:]):
        if z1 <= z <= z0:
            t = (z0 - z) / (z0 - z1)
            return (f0 + (f1 - f0) * t) if front else (b0 + (b1 - b0) * t)
    return 0.13


def hose_w(p):
    if p.z > 1.3:
        return {"chest": 1}
    if p.z > 1.12:
        return {"chest": .5, "spine": .5}
    return {"spine": .4, "hips": .6}


for loop, off in enumerate((-0.03, 0.0, 0.03)):
    pts = []
    for i in range(25):
        th = 2 * math.pi * i / 24
        p = C + A * math.cos(th) + N * (off * (1.0 + 0.4 * math.cos(th)))
        sn = math.sin(th)
        depth = torso_r(p.z, sn < 0) + 0.03 + 0.012 * loop
        p.y = (-1 if sn < 0 else 1) * depth * abs(sn) ** 0.6
        if math.cos(th) > 0.8:
            p.z += 0.02
        pts.append(p)
    gear.tube(pts, 0.02, "hose" if loop != 1 else "hose_dk", hose_w, segs=6, caps=False)
gear.ball(0.12, (0.07, 0.185, 1.20), "bladder", {"chest": .5, "spine": .5}, scale=(1.0, 0.62, 1.35), sub=2)
for z in (1.28, 1.12):
    gear.loft([R((0.07, 0.185, z + 0.012), 0.118, 0.076), R((0.07, 0.185, z - 0.012), 0.118, 0.076)], "leather", segs=10,
              w={"chest": .5, "spine": .5}, axis=(0, 0, -1), caps=False)
gear.tube([(0.07, 0.2, 1.36), (0.1, 0.17, 1.44), (0.15, 0.1, 1.47)], 0.018, "hose_dk", "chest", segs=6)

# ---------------------------------------------------------------- the staff: three flames at knee, hip and shoulder
SX, SY = -0.27, -0.30
gear.loft([R((SX, SY, 0.0), 0.016), R((SX, SY, 0.02), 0.024), R((SX, SY, 0.10), 0.024), R((SX, SY, 0.105), 0.02, col="wood"),
           R((SX, SY, 1.0), 0.021, col="wood"), R((SX, SY, 1.9), 0.019, col="wood"), R((SX, SY, 2.28), 0.016, col="wood_dk")],
          "tin_dk", segs=7, w="staff", axis=(0, 0, 1))
gear.loft([R((SX, SY, 1.08), 0.026), R((SX, SY, 1.36), 0.026)], "rope", segs=7, w="staff", axis=(0, 0, 1), caps=False)
hook = [Vector((SX, SY, 2.26)) + Vector((0, -0.07 * math.sin(t), 0.07 - 0.07 * math.cos(t))) for t in [i * 0.45 for i in range(9)]]
gear.tube(hook, 0.011, "tin_dk", "staff", segs=5)                                   # hook for hanging on a rope
gear.box((0.012, 0.012, 0.16), (SX, SY - 0.07, 2.2), "chalk", "staff")              # the rag that shows the wind
for hz in (0.50, 1.0, 1.52):
    gear.box((0.024, 0.15, 0.022), (SX, SY - 0.075, hz), "wood_dk", "staff", bevel=0.004)
    gear.tube([(SX, SY - 0.02, hz - 0.1), (SX, SY - 0.12, hz - 0.012)], 0.007, "tin_dk", "staff", segs=4)
    gear.loft([R((SX, SY - 0.15, hz - 0.012), 0.022, col="tin_dk"), R((SX, SY - 0.15, hz + 0.0), 0.04), R((SX, SY - 0.15, hz + 0.055), 0.044),
               R((SX, SY - 0.15, hz + 0.056), 0.036, col="dark"), R((SX, SY - 0.15, hz + 0.03), 0.03, col="dark")],
              "tin", segs=8, w="staff", axis=(0, 0, 1), caps="start")
    flames.loft([R((SX, SY - 0.15, hz + 0.035), 0.014), R((SX, SY - 0.15, hz + 0.08), 0.034), R((SX, SY - 0.15, hz + 0.14), 0.022),
                 R((SX, SY - 0.15, hz + 0.21), 0.003)], "flame", segs=6, w="staff", axis=(0, 0, 1))

body.finish(arm)
gear.finish(arm, amp=0.07)
flames.finish(arm, amp=0.0)

# ---------------------------------------------------------------- animation
an = rig.Anim(arm)
TAU = 2 * math.pi
N_WALK, DUTY, REACH = 30, 0.6, 0.27          # frames per cycle, stance share, half a stance length
SPEED = 2 * REACH / DUTY                     # metres per cycle = metres per second at 30 fps
print("WALK_SPEED", round(SPEED, 3))


def foot_path(ph):
    """(y, z, toe-down pitch) of the ankle relative to rest, for one foot at phase ph."""
    ph %= 1.0
    if ph < DUTY:
        s = ph / DUTY
        y = -REACH + 2 * REACH * s
        if s < 0.15:
            pitch = -0.30 * (1 - s / 0.15)
        elif s > 0.68:
            pitch = 0.65 * ((s - 0.68) / 0.32) ** 1.4
        else:
            pitch = 0.0
        z = 0.115 * math.sin(max(pitch, 0.0))
    else:
        s = (ph - DUTY) / (1 - DUTY)
        e = 0.5 - 0.5 * math.cos(math.pi * s)
        y = REACH - 2 * REACH * e
        pitch = 0.65 + (-0.30 - 0.65) * (s ** 0.8)
        z = 0.07 * (1 - s) ** 2 + 0.075 * math.sin(math.pi * s)
    return y, z, pitch


an.begin("walk-loop")
for f in range(N_WALK + 1):
    t = f / N_WALK
    c1, s1 = math.cos(TAU * t), math.sin(TAU * t)
    bob = -0.05 - 0.018 * math.cos(2 * TAU * t)
    sway = 0.02 * math.sin(TAU * (t - 0.05))
    an.loc("hips", f, (sway, 0, bob))
    an.rot("hips", f, ("X", 0.05), ("Z", -0.10 * c1), ("Y", 0.03 * math.sin(TAU * (t - 0.05))))
    an.rot("spine", f, ("Z", 0.07 * c1), ("X", 0.02))
    an.rot("chest", f, ("Z", 0.08 * c1), ("Y", -0.03 * math.sin(TAU * (t - 0.05))))
    an.rot("neck", f, ("Z", -0.03 * c1))
    an.rot("head", f, ("Z", -0.03 * c1), ("X", -0.05 + 0.015 * math.cos(2 * TAU * t)))
    for s, ph in ((".L", t), (".R", t + 0.5)):
        y, z, pitch = foot_path(ph)
        an.loc("ik_foot" + s, f, (0, y, z))
        an.rot("ik_foot" + s, f, ("X", pitch))
        for b in ("thigh" + s, "shin" + s, "foot" + s):
            an.rot(b, f)
    an.rot("upper_arm.L", f, ("X", 0.05 + 0.32 * c1), ("Y", -0.05))
    an.rot("forearm.L", f, ("X", -0.28 + 0.16 * c1))
    an.rot("hand.L", f, ("X", -0.1))
    # the staff plants with the left foot, rides back with the ground, then swings forward
    if t < 0.56:
        ty, tz = -0.26 + SPEED * t, 0.0
    else:
        s = (t - 0.56) / 0.44
        e = 0.5 - 0.5 * math.cos(math.pi * s)
        ty, tz = (-0.26 + SPEED * 0.56) * (1 - e) + (-0.26) * e, 0.13 * math.sin(math.pi * s)
    grip_y = 0.0 + 0.01 * c1                              # where the hand wants to be, relative to rest
    lean = -math.asin(max(-0.6, min(0.6, (grip_y - ty) / 1.21)))
    an.loc("staff", f, (sway * 0.6, ty, tz + (bob + 0.05) * 0.5))
    an.rot("staff", f, ("X", lean), ("Y", 0.04 * s1))
    an.rot("ik_hand.R", f)
    for b in ("upper_arm.R", "forearm.R", "hand.R"):
        an.rot(b, f)

N_IDLE = 90
an.begin("idle-loop")
for f in range(0, N_IDLE + 1, 3):
    t = f / N_IDLE
    br = math.sin(TAU * t * 2)                             # two breaths
    look = math.sin(TAU * t)
    an.loc("hips", f, (0.012 * look, 0, -0.012 + 0.003 * br))
    an.rot("hips", f, ("Y", 0.02 * look))
    an.rot("spine", f, ("X", 0.01 + 0.008 * br))
    an.rot("chest", f, ("X", -0.012 * br), ("Z", 0.05 * look))
    an.rot("neck", f, ("Z", 0.12 * look))
    an.rot("head", f, ("Z", 0.22 * look), ("X", 0.04 + 0.03 * math.cos(TAU * t)))
    for s in (".L", ".R"):
        an.loc("ik_foot" + s, f, (0, 0, 0))
        an.rot("ik_foot" + s, f)
        for b in ("thigh" + s, "shin" + s, "foot" + s):
            an.rot(b, f)
    an.rot("upper_arm.L", f, ("X", 0.03 + 0.01 * br), ("Y", -0.04))
    an.rot("forearm.L", f, ("X", -0.12))
    an.rot("hand.L", f)
    an.loc("staff", f, (0, 0, 0))
    an.rot("staff", f, ("X", 0.02 + 0.006 * br), ("Y", 0.015 * look))
    an.rot("ik_hand.R", f)
    for b in ("upper_arm.R", "forearm.R", "hand.R"):
        an.rot(b, f)
an.stash()
bpy.context.scene.frame_start, bpy.context.scene.frame_end = 0, N_IDLE
rig.export(OUT)
