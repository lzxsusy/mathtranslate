import io, sys
sys.stdout.reconfigure(encoding="utf-8")
LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl",
       "\ufb05": "st", "\ufb06": "st"}
for p in (r"<本地路径>",
          r"<本地路径>"):
    s = io.open(p, encoding="utf-8").read()
    n = 0
    for k, v in LIG.items():
        n += s.count(k)
        s = s.replace(k, v)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
    print(p, "replaced", n)
