#!/usr/bin/env bash
# Art test 2: rebuild the characters in Blender, re-import in Godot, capture screenshots into out/.
# Usage: ./chars.sh [sounder|longshank|pair|market]   (optional: only shots starting with that word)
#        ./chars.sh gif    (also renders 84 frames and assembles out/walk.gif; needs Python with Pillow)
set -e
cd "$(dirname "$0")"
ROOT="$(pwd -W 2>/dev/null || pwd)"
BLENDER="/c/Program Files/Blender Foundation/Blender 5.2/blender.exe"
GODOT=$(ls ~/AppData/Local/Microsoft/WinGet/Packages/GodotEngine*/Godot_v4.7.2-stable_win64_console.exe)
for c in sounder longshank; do
  [ -f "blender/build_$c.py" ] || continue
  "$BLENDER" -b -P "blender/build_$c.py" -- "$ROOT/godot/assets/$c.glb" 2>&1 | grep -E "faces|SPEED|Error|Traceback|line |WROTE" || true
done
"$GODOT" --headless --path godot --import >/dev/null 2>&1 || true
if [ "$1" = "gif" ]; then
  mkdir -p out/gif
  "$GODOT" --path godot --resolution 960x540 res://chars.tscn -- --out="$ROOT/out" --gif 2>&1 | grep -E "ERROR|error" || true
  python make_gif.py
else
  "$GODOT" --path godot res://chars.tscn -- --out="$ROOT/out" ${1:+--only=$1} 2>&1 | grep -E "saved|ERROR|error" || true
fi
