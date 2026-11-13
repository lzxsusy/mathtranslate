import io, re
t = io.open(r"<本地路径>", encoding="utf-8").read()
parts = re.split(r"===== PDF PAGE (\d+) =====", t)
pages = {}
for k in range(1, len(parts), 2):
    pages[int(parts[k])] = parts[k+1]

def clean(s):
    return "".join(ch if (ch == "\n" or 32 <= ord(ch) < 127 or 0x4E00 <= ord(ch) <= 0x9FFF or 0x3000 <= ord(ch) <= 0x30FF) else " " for ch in s)

buf = []
for p in (46, 47, 48, 49, 50, 51):
    txt = pages[p].strip()
    buf.append("===== PAGE %d =====" % p)
    buf.append("HEAD: " + clean(txt[:330]))
    buf.append("TAIL: " + clean(txt[-260:]))
# 找 A.x 出现
for p in sorted(pages):
    for m in re.finditer(r"A\.\d+", pages[p]):
        buf.append("A-num p%d: %s | %s" % (p, m.group(0), clean(pages[p][max(0, m.start()-30):m.start()+60]).replace("\n", " ")))
        break
io.open(r"<本地路径>", "w", encoding="utf-8").write("\n\n".join(buf))
