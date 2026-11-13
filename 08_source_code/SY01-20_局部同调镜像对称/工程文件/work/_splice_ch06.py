import io, re

SRC = r"<本地路径>"
dst_path = r"<本地路径>"

def lines(path):
    return io.open(path, encoding="utf-8").read().split("\n")

ch05 = lines(SRC + r"\ch05_src.tex")
ch06 = lines(SRC + r"\ch06_src.tex")

MARK = re.compile(r"^\s*%\s*----\s*原文行\s*\d+\s*----\s*$")

def slice_clean(ls, a, b):
    """1-based inclusive slice, dropping splitter comment lines."""
    out = [l for l in ls[a-1:b] if not MARK.match(l)]
    return "\n".join(out)

fig4 = slice_clean(ch05, 148, 261) + "\n" + slice_clean(ch06, 3, 8)
fig5 = slice_clean(ch06, 24, 70)
cd1 = slice_clean(ch06, 10, 13)
cd2 = slice_clean(ch06, 160, 163)

s = io.open(dst_path, encoding="utf-8").read()
for key, val in [("<<FIG4>>", fig4), ("<<FIG5>>", fig5), ("<<CD1>>", cd1), ("<<CD2>>", cd2)]:
    assert key in s, key
    s = s.replace(key, val)
assert "<<" not in s
io.open(dst_path, "w", encoding="utf-8", newline="\n").write(s)
print("spliced ok; total lines:", s.count("\n") + 1)
