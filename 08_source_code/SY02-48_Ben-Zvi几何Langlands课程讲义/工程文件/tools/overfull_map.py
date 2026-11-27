# -*- coding: utf-8 -*-
"""把 main.log 里的 Overfull/Underfull 按当前输入文件归位。"""
import io, re, sys

log = io.open(sys.argv[1], encoding="utf-8", errors="replace").read()
cur = "?"
out = []
for line in log.splitlines():
    m = re.search(r"\((\./sections/[^\s\)]+\.tex)", line)
    if m:
        cur = m.group(1)
    m2 = re.match(r"(Overfull|Underfull) \\[hv]box \(([\d.]+)pt too (wide|high)\) .*lines? (\d+)--(\d+)", line)
    if m2:
        out.append((float(m2.group(2)), m2.group(1), cur, m2.group(4), m2.group(5), line[:60]))
for o in sorted(out, reverse=True)[:25]:
    print("%6.2fpt %s %s:%s-%s" % (o[0], o[1], o[2], o[3], o[4]))
print("total", len(out))
