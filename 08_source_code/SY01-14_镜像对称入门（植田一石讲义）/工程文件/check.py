# -*- coding: utf-8 -*-
"""check.py —— JP02 交付前自检。

检查项：
1. 每个 chunk 的 \\tag 数 = BRIEF 预期；按节分组后编号连续（1..N，无跳号/重号）。
2. 环境配对（全书合并判断，允许跨 chunk 的 begin/end）、占位符残留、BOM/CRLF、markdown 残留。
3. 章节标题出现次数。
"""
import io, os, re, sys
from collections import Counter, defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, "src", "chunks")

EXPECT = {"c00": 1, "c01": 23, "c02": 13, "c03": 13, "c04": 14,
          "c05": 38, "c06": 41, "c07": 38, "c08": 34, "c09": 9, "c10": 0}

chunks = sorted(f[:-4] for f in os.listdir(CH) if re.fullmatch(r"c\d\d\.tex", f))
problems = []
global_b = Counter()
global_e = Counter()
total = 0
sec_tags = defaultdict(list)
env_count = Counter()
nsec = 0

for name in chunks:
    p = os.path.join(CH, name + ".tex")
    raw = open(p, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append(f"{name}: 含 BOM")
    if b"\r\n" in raw:
        problems.append(f"{name}: CRLF 换行")
    t = raw.decode("utf-8")
    if "placeholder" in t:
        problems.append(f"{name}: 仍是占位文件")
        continue
    if "**" in t:
        problems.append(f"{name}: 残留 markdown 粗体")
    tags = re.findall(r"<本地路径>]*)\}", t)
    total += len(tags)
    exp = EXPECT.get(name)
    if exp is not None and len(tags) != exp:
        problems.append(f"{name}: tag 数 {len(tags)} != 预期 {exp}")
    for tg in tags:
        m = re.match(r"(\d+)\.(\d+)$", tg.strip())
        if not m:
            problems.append(f"{name}: tag 格式异常 {tg!r}")
            continue
        sec_tags[int(m.group(1))].append((int(m.group(2)), name))
    begins = Counter(re.findall(r"<本地路径>)\}", t))
    ends = Counter(re.findall(r"<本地路径>)\}", t))
    global_b.update(begins)
    global_e.update(ends)
    env_count.update({k: v for k, v in begins.items()
                      if k in ("definition", "theorem", "example", "remark", "problem", "exercise")})
    nsec += len(re.findall(r"<本地路径>", t))
    print(f"{name}: tag={len(tags):>3}  \\section={len(re.findall(r'\\section', t)):>2}  定理类={sum(v for k, v in begins.items() if k in ('definition','theorem','example','remark','problem','exercise'))}")

diff = global_b - global_e
diff2 = global_e - global_b
if diff or diff2:
    problems.append(f"全书环境不配对 begin多={dict(diff)} end多={dict(diff2)}")

print(f"\n合计编号公式：{total}（预期 224）")
print("\n按节检查编号连续性：")
for sec in sorted(sec_tags):
    nums = sorted(n for n, _ in sec_tags[sec])
    dup = [n for n, c in Counter(nums).items() if c > 1]
    gaps = [n for n in range(1, max(nums) + 1) if n not in nums]
    status = "OK" if not dup and not gaps else f"重号{dup} 缺号{gaps}"
    if dup or gaps:
        problems.append(f"第 {sec} 节 {status}")
    print(f"  第 {sec:>2} 节: {len(nums):>2} 条, 最大 {max(nums):>2}  {status}")

print("\n定理类环境计数：", dict(env_count))
print(f"\\section 总数：{nsec}（预期 14）")
if nsec != 14:
    problems.append(f"\\section 总数 {nsec} != 14")
if problems:
    print("\n[问题]")
    for x in problems:
        print("  -", x)
else:
    print("\n[OK] 全部通过")
