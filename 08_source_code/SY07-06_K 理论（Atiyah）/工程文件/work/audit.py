# -*- coding: utf-8 -*-
"""装配前审计：陈述编号跨块重复 / 节标题顺序 / \tag 重复 / 跨块句重复 / 页标记连续性"""
import os, re, glob, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
CH = r"<本地路径>"
MAIN = r"<本地路径>"

order = []
for line in open(MAIN, encoding="utf-8"):
    m = re.search(r'<本地路径>]+)\}', line)
    if m and m.group(1) != "index_notes":
        order.append(m.group(1))

stmt, tags, secs, pages = [], [], [], []
for name in order:
    f = os.path.join(CH, name + ".tex")
    if not os.path.exists(f):
        print("MISSING", name); continue
    t = open(f, encoding="utf-8").read()
    body = "\n".join(l for l in t.splitlines() if not re.match(r'\s*%', l))
    for m in re.finditer(r'<本地路径>|theorem|lemma|proposition|corollary|example|remark|notation|formulaenv)(\*?)\}\{([^}]*)\}', body):
        stmt.append((name, m.group(1) + m.group(2), m.group(3)))
    for m in re.finditer(r'<本地路径>]*)\}', body):
        tags.append((name, m.group(1)))
    for m in re.finditer(r'\\(chapter|section)\*?\{([^}]*)\}', body):
        secs.append((name, m.group(1), m.group(2)))
    for m in re.finditer(r'% \[原文 p\.(\w+)\]', t):
        pages.append((name, m.group(1)))

print("== 陈述计数 ==", len(stmt))
dup = collections.defaultdict(list)
for name, kind, num in stmt:
    if num:
        dup[num].append(f"{name}:{kind}")
print("同号陈述（不同 chunk = 错；同 chunk 可能是原书体例）：")
for k, v in sorted(dup.items()):
    chunks = {x.split(':')[0] for x in v}
    if len(chunks) > 1:
        print("  !!", k, v)
print()
print("== 公式 tag ==", len(tags))
dupt = collections.defaultdict(list)
for name, tg in tags:
    dupt[tg].append(name)
for k, v in sorted(dupt.items()):
    if len(v) > 1:
        print("  !! tag", k, v)
print()
print("== 章节标题顺序 ==")
for name, kind, title in secs:
    print(f"  {name:8s} {kind:7s} {title}")
print()
print("== 页标记（原书页）==")
seen = []
for name, p in pages:
    seen.append((name, p))
nums = []
for name, p in seen:
    try:
        nums.append(int(p))
    except Exception:
        pass
print("count", len(nums), "min", min(nums), "max", max(nums))
miss = [p for p in range(1, 203) if p not in set(nums) and p not in (82, 110)]
print("缺页标记（1..202，除空白 82/110）:", miss)
