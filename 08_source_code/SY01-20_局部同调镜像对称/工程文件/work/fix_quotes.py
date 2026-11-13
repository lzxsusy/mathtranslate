import io
import re
import glob

def fix_quotes(path):
    s = io.open(path, encoding="utf-8").read()
    n0 = s.count('"')
    s2 = re.sub(r'"([^"\n]*)"', lambda m: "\u300c" + m.group(1) + "\u300d", s)
    if s2 != s:
        io.open(path, "w", encoding="utf-8").write(s2)
    return n0, s2.count('"')

files = [r"<本地路径>"]
for f in files:
    n0, n1 = fix_quotes(f)
    print(f, n0, "->", n1)

p = r"<本地路径>"
s = io.open(p, encoding="utf-8").read()
if "\\pagestyle{plain}" not in s:
    s = s.replace("\\allowdisplaybreaks[3]", "\\allowdisplaybreaks[3]\n\\pagestyle{plain}")
    io.open(p, "w", encoding="utf-8").write(s)
    print("pagestyle plain added")
