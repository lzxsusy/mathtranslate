import io
p = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论\源码\chunks\ch18.tex"
s = io.open(p, encoding="utf-8").read()
bs = chr(92)
old = "\\QCoh(\\on{pt}/\\cG)) " + bs + "\n&\\qquad"
# generic fix: any line ending with a single backslash inside the split we generated
bad = "\\QCoh(\\on{pt}/\\cG)) " + bs + "\r\n"
good = "\\QCoh(\\on{pt}/\\cG)) " + bs + bs + "\r\n"
if bad in s:
    s = s.replace(bad, good)
else:
    bad = "\\QCoh(\\on{pt}/\\cG)) " + bs + "\n"
    good = "\\QCoh(\\on{pt}/\\cG)) " + bs + bs + "\n"
    assert bad in s, "pattern missing"
    s = s.replace(bad, good)
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("fixed")
