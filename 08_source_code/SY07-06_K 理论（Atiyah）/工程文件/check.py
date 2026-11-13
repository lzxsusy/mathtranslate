# -*- coding: utf-8 -*-
"""Gate 1 静态检查：页标记覆盖 / tag / 陈述编号重复 / 花括号 / 环境配对 / $ 偶偶 / 禁用命令 / 编码"""
import os, re, sys, glob, collections

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")

# 分块 → PDF 页区间（与 BRIEF 一致）
CHUNKS = {
    "ch01a": (1, 8), "ch01b": (9, 18), "ch01c": (19, 28),
    "ch02a": (29, 38), "ch02b": (39, 48), "ch02c": (49, 58),
    "ch02d": (59, 70), "ch02e": (71, 81),
    "ch03a": (83, 92), "ch03b": (93, 102), "ch03c": (103, 109),
    "appA": (111, 120),
    "appB1": (121, 132), "appB2": (133, 144), "appB3": (145, 154), "appB4": (155, 162),
    "appC1": (163, 174), "appC2": (175, 184), "appC3": (185, 190),
    "kaisetsu": (191, 202),
    "fm": (0, 0),
}
BLANK = {82, 110}   # 空白页（原书页），不写页标记
SKIP = {"smoke", "index_notes"}


def read(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def strip_comments(t):
    out = []
    for line in t.splitlines():
        m = re.search(r'(?<!\\)(?:\\\\)*%', line)
        if m:
            line = line[:m.end() - 1]
        out.append(line)
    return "\n".join(out)


def check_file(path):
    t = read(path)
    body = strip_comments(t)
    name = os.path.basename(path)[:-4]
    problems = []
    with open(path, "rb") as f:
        if f.read(3) == b"\xef\xbb\xbf":
            problems.append("UTF-8 BOM")
    if "\ufffd" in t:
        problems.append("U+FFFD")
    if "\r" in t:
        problems.append("CRLF")
    depth = 0
    bad = False
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                bad = True
                break
    if depth != 0 or bad:
        problems.append(f"brace imbalance ({depth})")
    ob = re.findall(r'<本地路径>]*)\}', body)
    eb = re.findall(r'<本地路径>]*)\}', body)
    if collections.Counter(ob) != collections.Counter(eb):
        problems.append("env mismatch +%s -%s" % (dict(collections.Counter(ob) - collections.Counter(eb)),
                                                  dict(collections.Counter(eb) - collections.Counter(ob))))
    dollars = len(re.findall(r'(?<!\\)\$', body))
    if dollars % 2:
        problems.append(f"odd $ ({dollars})")
    for bad_cmd in [r'\\documentclass', r'<本地路径>', r'\\usepackage', r'<本地路径>',
                    r'<本地路径>', r'<本地路径>', r'<本地路径>']:
        if re.search(bad_cmd, body):
            problems.append("forbidden " + bad_cmd)
    if re.search(r'[\u4e00-\u9fff]\*\*|\*\*[\u4e00-\u9fff]', body):
        problems.append("markdown **")
    if "\u3000" in body:
        problems.append("U+3000")
    tags = re.findall(r'<本地路径>]*)\}', body)
    dup = [k for k, v in collections.Counter(tags).items() if v > 1]
    # 陈述环境编号
    stmts = re.findall(r'<本地路径>|theorem|lemma|proposition|corollary|example|remark|problem|notation|formulaenv)\*?\}\{([^}]*)\}', body)
    # 页标记
    pages = sorted({int(m.group(1)) for m in re.finditer(r'% \[原文 p\.(\d+)\]', t)})
    rng = CHUNKS.get(name)
    page_info = ""
    if name == "fm":
        pages = [1]  # fm 用罗马页码，只要求有标记
        rng = None
    if rng:
        expect = [p for p in range(rng[0], rng[1] + 1) if p not in BLANK]
        lack = [p for p in expect if p not in pages]
        extra = [p for p in pages if p not in expect]
        page_info = f" pages={len(pages)}/{len(expect)}"
        if lack:
            problems.append(f"缺页标记 {lack}")
        if extra:
            problems.append(f"越界页标记 {extra}")
    done = "% CHUNK " + name + " DONE" in t
    return name, problems, tags, stmts, page_info, done


def main():
    files = sorted(glob.glob(os.path.join(CH, "*.tex")))
    if not files:
        print("no chunks"); return 0
    allstmt = collections.defaultdict(list)
    still = False
    for f in files:
        name = os.path.basename(f)[:-4]
        if name in SKIP:
            continue
        name, problems, tags, stmts, page_info, done = check_file(f)
        for kind, num in stmts:
            allstmt[num].append(name)
        if not done:
            problems.append("缺 DONE 标记")
            still = True
        if problems:
            print(f"[{name}] " + "; ".join(problems) + page_info)
        else:
            print(f"[{name}] ok  tags={len(tags)} stmts={len(stmts)}{page_info} DONE")
    dup = {k: v for k, v in allstmt.items() if len(v) > 1}
    if dup:
        print("\n[提示] 同号陈述（原书本身可能有重号，需核对页图；不同 chunk 出现同号才是错误）：")
        for k, v in sorted(dup.items()):
            print("  ", k, v)
    print("\nSTATUS:", "INCOMPLETE" if still else "ALL CHUNKS DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
