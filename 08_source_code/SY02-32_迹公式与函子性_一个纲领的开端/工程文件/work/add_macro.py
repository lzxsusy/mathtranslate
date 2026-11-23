import pathlib
bs = chr(92)
p = pathlib.Path(r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-32_迹公式与函子性_一个纲领的开端\源码\preamble.tex")
s = p.read_text(encoding="utf-8")
line = bs + "newcommand{" + bs + "Hecke}{" + bs + "mathrm{Hecke}}" + chr(10)
if "\\Hecke}" not in s and line not in s:
    s = s.replace(bs + "newcommand{" + bs + "Hck}{" + bs + "mathrm{Hecke}}", bs + "newcommand{" + bs + "Hck}{" + bs + "mathrm{Hecke}}" + chr(10) + line)
p.write_text(s, encoding="utf-8")
print("ok")
