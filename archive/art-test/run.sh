#!/usr/bin/env bash
# Rebuild the model in Blender, re-import in Godot, and capture screenshots into out/.
set -e
cd "$(dirname "$0")"
ROOT="$(pwd -W 2>/dev/null || pwd)"
BLENDER="/c/Program Files/Blender Foundation/Blender 5.2/blender.exe"
GODOT=$(ls ~/AppData/Local/Microsoft/WinGet/Packages/GodotEngine*/Godot_v4.7.2-stable_win64_console.exe)
"$BLENDER" -b -P blender/build_market.py -- "$ROOT/godot/assets/market.glb" 2>&1 | grep -E "faces|TOTAL|Error|Traceback|line "
"$GODOT" --headless --path godot --import >/dev/null 2>&1
"$GODOT" --path godot -- --out="$ROOT/out" 2>&1 | grep -E "saved|ERROR|error" 
