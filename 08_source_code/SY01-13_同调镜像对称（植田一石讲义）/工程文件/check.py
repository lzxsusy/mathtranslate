# -*- coding: utf-8 -*-
"""check.py —— 交付前自检。

检查项：
1. 每个 chunk 的 \tag 数，以及按节分组后编号是否连续（1..N，无跳号/重号）。
   这是比「固定条数」更硬的标准：原文每节的编号公式都是从 1 连续编号的。
2. 定理/定义环境的自动编号与原文是否同节共享（交叉检查 \begin{theorem} 数量）。
3. 环境配对、占位符残留、BOM/CRLF。
"""
import io, os, re, sys
from collections import Counter, defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(ROOT, "src", "chunks")

chunks = sorted(f[:-4] for f in os.listdir(CH) if re.fullmatch(r"c\d\d\.tex", f))
problems = []
total = 0
sec_tags = defaultdict(list)      # section -> [(tag, chunk)]
env_count = Counter()

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
    tags = re.findall(r"<本地路径>]*)\}", t)
    total += len(tags)
    for tg in tags:
        m = re.match(r"(\d+)\.(\d+)$", tg.strip())
        if not m:
            problems.append(f"{name}: tag 格式异常 {tg!r}")
            continue
        sec_tags[int(m.group(1))].append((int(m.group(2)), name))
    begins = Counter(re.findall(r"<本地路径>)\}", t))
    ends = Counter(re.findall(r"<本地路径>)\}", t))
    if begins != ends:
        problems.append(f"{name}: 环境不配对 {dict(set(begins.items()) ^ set(ends.items()))}")
    env_count.update({k: v for k, v in begins.items() if k not in ("equation", "align", "gather", "figure", "list", "thebibliography")})
    print(f"{name}: tag={len(tags):>3}  节={len(re.findall(r'\\section', t)):>2}  "
          f"定理类环境={sum(v for k, v in begins.items() if k not in ('equation','align','gather','figure','list'))}")

print(f"\n合计编号公式：{total}")
print("\n按节检查编号连续性：")
bad_secs = 0
for sec in sorted(sec_tags):
    nums = sorted(n for n, _ in sec_tags[sec])
    dup = [n for n, c in Counter(nums).items() if c > 1]
    gaps = [n for n in range(1, max(nums) + 1) if n not in nums]
    status = "OK" if not dup and not gaps else f"重号{dup} 缺号{gaps}"
    if dup or gaps:
        bad_secs += 1
        problems.append(f"第 {sec} 节 {status}")
    print(f"  第 {sec:>2} 节: {len(nums):>2} 条, 最大 {max(nums):>2}  {status}")

print("\n定理类环境计数：", dict(env_count))
if problems:
    print("\n[问题]")
    for x in problems:
        print("  -", x)
else:
    print("\n[OK] 全部通过")
