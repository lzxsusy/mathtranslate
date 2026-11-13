# -*- coding: utf-8 -*-
r"""Gate 1 静态检查（每次改动后跑）：python check.py

检查项：
 1. 编号定理类完整性：定义 1–8、命题 1–3、引理 1、定理 1–9 必须各出现一次（本稿无编号公式）
 2. 每页页码标记 % [原文 p.N]（p.1–p.10）是否齐全
 3. 花括号平衡（去注释后粗略计数）
 4. \begin/\end 环境配对
 5. $ 数量为偶（去注释后，跳过 \$）
 6. 禁用命令扫描：\documentclass \usepackage \begin{document} \newcommand \tag \cite
 7. UTF-8 BOM / CRLF / U+FFFD 乱码
 8. markdown 粗体 **
"""
import sys, re, io, os, glob
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"<本地路径>"
WORK = os.path.join(ROOT, "work")
CHUNKS = os.path.join(WORK, "src", "chunks")

EXPECT = {
    "defn": [str(i) for i in range(1, 9)],     # 定义 1–8
    "prop": ["1", "2", "3"],                   # 命题 1–3
    "lem":  ["1"],                             # 引理 1
    "thm":  [str(i) for i in range(1, 10)],    # 定理 1–9
}
ENVNAME = {"defn": "定义", "prop": "命题", "lem": "引理", "thm": "定理"}
PAGES = [str(i) for i in range(1, 11)]

files = sorted(glob.glob(os.path.join(CHUNKS, "*.tex")))
print("chunk files:", len(files))

problems = []
found = {k: [] for k in EXPECT}
pages_found = []
all_begin, all_end = [], []

for f in files:
    name = os.path.basename(f)
    raw = io.open(f, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append(("BOM", name, 0))
    if b"\r\n" in raw:
        problems.append(("CRLF", name, 0))
    txt = raw.decode("utf-8", errors="replace")
    if "\ufffd" in txt:
        problems.append(("U+FFFD", name, txt.count("\ufffd")))
    lines = txt.splitlines()
    stripped = []
    for i, ln in enumerate(lines, 1):
        code = re.sub(r"(?<!\\)%.*$", "", ln)
        code = re.sub(r"<本地路径>|[^|]*\|", "", code)
        stripped.append(code)
        for k in EXPECT:
            for m in re.finditer(r"<本地路径>" + k + r"\}\{([^}]*)\}", code):
                found[k].append(m.group(1).strip())
        for m in re.finditer(r"<本地路径>", code):
            problems.append(("TAG_FORBIDDEN", name, i))
        mm = re.search(r"%\s*\[原文\s*p\.\s*(\d+)", ln)
        if mm:
            pages_found.append(mm.group(1))
    code_txt = "\n".join(stripped)
    for bad in (r"\documentclass", r"\usepackage", r"\begin{document}", r"\newcommand", r"\cite", r"\bibliography"):
        for _ in re.finditer(re.escape(bad), code_txt):
            problems.append(("FORBIDDEN", name, bad))
    ob, cb = code_txt.replace("\\{", "").replace("\\}", "").count("{"), \
             code_txt.replace("\\{", "").replace("\\}", "").count("}")
    if ob != cb:
        problems.append(("BRACES", name, f"{ob} vs {cb}"))
    d = code_txt.replace(r"\$", "")
    if d.count("$") % 2:
        problems.append(("DOLLAR", name, d.count("$")))
    begins = re.findall(r"<本地路径>]+)\}", code_txt)
    ends = re.findall(r"<本地路径>]+)\}", code_txt)
    all_begin.extend(begins)
    all_end.extend(ends)
    if re.search(r"(?<!\\)\*\*[^*\n]+\*\*", code_txt):
        problems.append(("MD_BOLD", name, "**"))

print("\n=== 0. 环境配对（全部 chunk 合并计数，跨文件环境只在此判定） ===")
bc, ec = Counter(all_begin), Counter(all_end)
env_ok = True
for k in sorted(set(bc) | set(ec)):
    if k == "document":
        continue
    if bc[k] != ec[k]:
        env_ok = False
        print(f"  !! {k}: begin {bc[k]} / end {ec[k]}")
if env_ok:
    print("  全部环境 begin/end 计数一致（含跨块的 itemize/proof）")

print("\n=== 1. 编号定理类 ===")
ok_all = True
for k, exp in EXPECT.items():
    got = found[k]
    missing = [x for x in exp if x not in got]
    extra = [x for x in got if x not in exp]
    dup = [x for x in exp if got.count(x) > 1]
    status = "OK" if not (missing or extra or dup) else "!!"
    if missing or extra or dup:
        ok_all = False
    print(f"  {ENVNAME[k]}: 原文 {len(exp)} 条；tex 中 {len(got)} 条 -> {status}"
          + (f" MISSING={missing}" if missing else "")
          + (f" EXTRA={extra}" if extra else "")
          + (f" DUPLICATE={dup}" if dup else ""))

print("\n=== 2. 页码标记 % [原文 p.N] ===")
missing_pages = [p for p in PAGES if p not in pages_found]
print("  缺失页码标记:", missing_pages if missing_pages else "无（p.1–p.10 齐全）")
if missing_pages:
    ok_all = False

print("\n=== 3–8. 其他问题 ===")
if problems:
    for p in problems:
        print("  ", p)
    ok_all = False
else:
    print("  无问题")

print("\n=== 结论 ===")
if not env_ok:
    ok_all = False
print("  PASS" if ok_all else "  FAIL（见上）")
sys.exit(0 if ok_all else 1)
