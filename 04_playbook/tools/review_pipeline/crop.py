# -*- coding: utf-8 -*-
"""crop.py <pdf> <page> <word> <out.png> [margin]"""
import subprocess, re, os, sys
from PIL import Image

pdftoppm = r"<本地路径>"
pdftotext = r"<本地路径>"

pdf, page, word, out = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 300

xml = subprocess.run([pdftotext, "-f", str(page), "-l", str(page), "-bbox", pdf, "-"], capture_output=True).stdout.decode("utf-8", "replace")
m = re.search(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">' + re.escape(word) + r'[^<]*</word>', xml)
if not m:
    print("word not found"); sys.exit(1)
x0, y0, x1, y1 = [float(v) for v in m.groups()]
tmp = os.path.splitext(out)[0] + "_page"
subprocess.run([pdftoppm, "-f", str(page), "-l", str(page), "-r", str(dpi), "-png", pdf, tmp], check=True)
f = [x for x in os.listdir(os.path.dirname(out) or ".") if x.startswith(os.path.basename(tmp))]
im = Image.open(os.path.join(os.path.dirname(out) or ".", f[0]))
W, H = im.size
scale = dpi / 72.0
top = max(0, int(y0*scale) - 30); bot = min(H, int(y1*scale) + 30)
left = max(0, int(x0*scale) - 400); right = min(W, W - 20)
c = im.crop((left, top, right, bot))
c.save(out)
print("saved", out, c.size, "img", W, H)
