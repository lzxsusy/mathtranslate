import glob
import re

total = 0
for f in sorted(glob.glob("sections/*.tex")):
    t = open(f, encoding="utf-8").read()
    t2, n = re.subn(r"\\paragraph\{([^}]*?)[。.]\}", r"\\paragraph{\1}", t)
    if n:
        open(f, "w", encoding="utf-8").write(t2)
        print(f, n)
        total += n
print("total", total)
