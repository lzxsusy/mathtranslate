import io, re
t = io.open(r"<本地路径>", encoding="utf-8").read()
envs = {}
for m in re.finditer(r"<本地路径>]+)\}", t):
    envs[m.group(1)] = envs.get(m.group(1), 0) + 1
out = "\n".join("%s %d" % (k, v) for k, v in sorted(envs.items(), key=lambda kv: -kv[1]))
io.open(r"<本地路径>", "w", encoding="utf-8").write(out)
