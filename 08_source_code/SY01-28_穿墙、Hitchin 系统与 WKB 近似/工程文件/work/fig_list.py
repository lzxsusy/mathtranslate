import re, os, glob
d = r"C:\Users\admin\Desktop\GMN系列\01_翻译\GMN2_0907.3987\源码\chunks"
order = ["ch01","ch02","ch03","ch04","ch05","ch06","ch07","ch08","ch09","ch10","ch11","ch12","ch13","ch14","ch15","ch16","ch17","appA","appB","appC","appD","appE"]
n = 0
out = []
for name in order:
    p = os.path.join(d, name + ".tex")
    if not os.path.exists(p):
        continue
    src = open(p, encoding="utf-8").read()
    # find figure environments and the includegraphics / insfig filenames in order
    items = []
    for m in re.finditer(r"\\insfig\{[^}]*\}\{([a-zA-Z0-9_-]+)\}", src):
        items.append((m.start(), m.group(1)))
    for m in re.finditer(r"\\includegraphics\[[^\]]*\]\{figures/([a-zA-Z0-9_-]+)-crop\.pdf\}", src):
        items.append((m.start(), m.group(1)))
    items.sort()
    # dedupe: includegraphics inside insefig macro definition won't appear; keep order
    for _, fn in items:
        n += 1
        out.append("%s\t%d\t%s" % (name, n, fn))
open(r"C:\Users\admin\Desktop\GMN系列\01_翻译\GMN2_0907.3987\工程文件\work\fig_list.tsv", "w", encoding="utf-8").write("\n".join(out))
print(len(out))
print("\n".join(out))
