import pathlib, sys

root = pathlib.Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-32_迹公式与函子性_一个纲领的开端\源码")
bs = chr(92)
changed = []
for p in sorted(root.rglob("*.tex")):
    s = p.read_text(encoding="utf-8")
    n = s.count(bs + bs)
    if n:
        s2 = s.replace(bs + bs, bs)
        p.write_text(s2, encoding="utf-8")
        changed.append((p.name, n))
for name, n in changed:
    print(name, n)
print("done", len(changed))
