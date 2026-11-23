import pathlib
bs = chr(92)
root = pathlib.Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-32_迹公式与函子性_一个纲领的开端\源码")

m = root / "main.tex"
s = m.read_text(encoding="utf-8")
s = s.replace(bs + "[0.3em]", bs + bs + "[0.3em]")
s = s.replace(bs + "[0.6em]", bs + bs + "[0.6em]")
m.write_text(s, encoding="utf-8")

p = root / "sections" / "s03-sec2.tex"
t = p.read_text(encoding="utf-8")
t = t.replace("&0" + bs + "0&", "&0" + bs + bs + "0&")
p.write_text(t, encoding="utf-8")
print("ok")
