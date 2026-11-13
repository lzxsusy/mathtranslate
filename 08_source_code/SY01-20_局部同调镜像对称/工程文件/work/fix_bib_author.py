import io

p = r"<本地路径>"
s = io.open(p, encoding="utf-8").read()
old = "Yusuf Bar<本地路径> s"
new = "Yusuf Bar{\\i}\\c{s}"
print("found", old in s)
s = s.replace(old, new)
io.open(p, "w", encoding="utf-8").write(s)
print([l for l in s.splitlines() if "Bar" in l])
