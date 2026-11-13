import io
import re

src = io.open(r"<本地路径>", encoding="utf-8").read().splitlines()
bounds = {"ch00": 171, "ch01": 215, "ch02": 365, "ch03": 516, "ch04": 811, "ch05": 1055,
           "ch06": 1301, "ch07": 1805, "ch08": 2170, "ch09": 2671, "ch10": 3291,
           "ch11": 3821, "ch12": 4216, "ch13": 4656, "ch14": 5101, "end": 5546}

stack = []
report = {b: None for b in bounds}
maxline = max(bounds.values())
for i in range(1, maxline + 1):
    for b, L in bounds.items():
        if i == L:
            report[b] = list(stack)
    line = src[i - 1] if i - 1 < len(src) else ""
    # strip comments (unescaped %)
    line = re.sub(r"(?<!\\)%.*", "", line)
    for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", line):
        kind, env = m.group(1), m.group(2)
        if kind == "begin":
            stack.append((env, i))
        else:
            # pop matching
            for j in range(len(stack) - 1, -1, -1):
                if stack[j][0] == env:
                    del stack[j:]
                    break

out = []
for b in ["ch00", "ch01", "ch02", "ch03", "ch04", "ch05", "ch06", "ch07", "ch08",
          "ch09", "ch10", "ch11", "ch12", "ch13", "ch14"]:
    st = report[b]
    out.append("%s boundary line %d -> open envs: %s" % (b, bounds[b], st))
io.open(r"<本地路径>", "w", encoding="utf-8").write("\n".join(out))
for line in out:
    print(line)
