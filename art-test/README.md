# Art test 1: Ladderfoot, storey 6 market

Question: can our own agents make a scene that is not basic shapes, with no bought or generated assets?

Everything here is made by code. `blender/build_market.py` builds the whole scene in headless Blender (geometry
and vertex colour, no textures) and exports one `.glb`. `godot/` loads it, applies one painted-look shader, lights
it for dusk and saves three screenshots to `out/`. `run.sh` does both steps.

Requires Blender 5.2 and Godot 4.7.2 (paths are set in `run.sh`).

| Shot | File |
|---|---|
| Game-camera view | `out/wide.png` |
| Market close-up | `out/market.png` |
| Capsule dwellings | `out/capsules.png` |

About 50,000 faces. Four build-and-look rounds.

# Art test 2: the Sounder and a Longshank, rigged and walking

Question: can agents make a hero character and an animal that hold up in the same scene, and make them move?

Again everything is code. `blender/rig.py` is a small shared library: meshes are skinned tubes lofted through
rings, each ring carrying its own bone weights and colour; skeletons, IK and keyframes are written by script.
`blender/build_sounder.py` and `blender/build_longshank.py` build one character each and export a `.glb` with
`walk` and `idle` animations. `godot/chars.tscn` poses them and saves the shots. `chars.sh` does all of it;
`chars.sh gif` also renders `out/walk.gif`.

| Shot | File |
|---|---|
| Sounder in the market, game camera | `out/market_game.png` |
| Sounder close-up | `out/sounder_close.png` |
| Sounder walk cycle, six phases | `out/sounder_walk.png` |
| Longshank close-up | `out/longshank_close.png` |
| Longshank walk cycle, five phases | `out/longshank_walk.png` |
| Both at game-camera distance | `out/pair_game.png` |
| Both walking | `out/walk.gif` |

Sounder: 2,300 faces, 18 bones. Feet follow IK targets; the staff plants with the left foot and the right hand
follows it by IK. Longshank: 900 faces, 31 bones, four IK legs, a four-beat walk.

Result: the Sounder passes at game-camera distance and is clearly better than the test 1 crowd figures. The
Longshank moves correctly but looks rougher: smooth tube limbs, no real fur, a stiff face. Not yet tested: faces
that can talk, hands with fingers, cloth that swings, attack and death animations, turning and stopping.
