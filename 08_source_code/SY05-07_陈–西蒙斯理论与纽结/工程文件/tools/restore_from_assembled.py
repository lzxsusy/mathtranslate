import re

t = open("CS and Knots.tex", encoding="utf-8").read().splitlines()
marks = [(i, l) for i, l in enumerate(t) if l.startswith("% >>>>>>>>>>>>>>>>")]
print(len(marks))
for k in range(0, len(marks), 2):
    m1 = re.search(r"sections/(\S+)\.tex", marks[k][1])
    m2 = re.search(r"end sections/(\S+)\.tex", marks[k + 1][1])
    assert m1.group(1) == m2.group(1), (m1.group(1), m2.group(1))
    body = "\n".join(t[marks[k][0] + 1:marks[k + 1][0]]) + "\n"
    open("sections/" + m1.group(1) + ".tex", "w", encoding="utf-8").write(body)
    print(m1.group(1), len(body.splitlines()), "lines")
