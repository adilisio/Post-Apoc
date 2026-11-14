"""Assemble out/gif/*.png (written by chars.gd --gif) into out/walk.gif."""
import glob
from PIL import Image

frames = sorted(glob.glob("out/gif/*.png"))[:84]
ims = [Image.open(f).convert("RGB").resize((720, 405), Image.LANCZOS) for f in frames]
pal = [i.quantize(colors=128, method=Image.MEDIANCUT, dither=Image.NONE) for i in ims]
pal[0].save("out/walk.gif", save_all=True, append_images=pal[1:], duration=67, loop=0, optimize=True)
print("saved out/walk.gif", len(pal), "frames")
