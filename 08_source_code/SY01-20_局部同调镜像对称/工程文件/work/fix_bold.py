import io
import re

p = r"<本地路径>"
s = io.open(p, encoding="utf-8").read()
s2 = re.sub(r"\*\*((?:(?!\n\n).)+?)\*\*", lambda m: "\\textbf{" + m.group(1) + "}", s, flags=re.S)
io.open(p, "w", encoding="utf-8").write(s2)
print("before", s.count("**"), "after", s2.count("**"))
