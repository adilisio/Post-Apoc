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
