# -*- coding: utf-8 -*-
"""Gate 1 静态检查：tag 完整性（全局 + 分块）/ 花括号 / 环境配对 / $ 偶偶 / 禁用命令 / 编码 / 页标记"""
import os, re, sys, glob, collections

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
TAGS = os.path.join(ROOT, "work", "tags.txt")

# 分块 → PDF 页区间（与 BRIEF 一致）
CHUNKS = {
    "fm": (5, 18), "ch01a": (21, 30), "ch01b": (31, 44), "ch01c": (45, 53),
    "ch01d": (54, 70), "ch02a": (71, 82), "ch02b": (83, 96), "ch02c": (97, 102),
    "ch02d": (103, 112), "ch02e": (113, 119), "ch03a": (121, 130),
    "ch03b": (131, 136), "ch03c": (137, 145), "future": (147, 154),
    "references": (155, 160),
}
BAKED = set()   # 编号烙在图里的公式（如有）
# OCR 漏检但确实存在的编号（已知项，见 TIMELINE §五）
KNOWN_EXTRA = {"1.10", "2.35", "3.8"}

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

def load_tags():
    """返回 [(tag, pdfpage)]"""
    rec = []
    if not os.path.exists(TAGS):
        return rec
    for line in read(TAGS).splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            rec.append((parts[0].strip(), int(parts[1])))
    return rec

def check_file(path, all_tags):
    t = read(path)
    body = strip_comments(t)
    name = os.path.basename(path)[:-4]
    problems = []
    with open(path, "rb") as f:
        if f.read(3) == b"\xef\xbb\xbf":
            problems.append("UTF-8 BOM")
    if "\ufffd" in t:
        problems.append("U+FFFD")
    depth = 0; bad = False
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                bad = True; break
    if depth != 0 or bad:
        problems.append(f"brace imbalance ({depth})")
    ob = re.findall(r'<本地路径>]*)\}', body)
    eb = re.findall(r'<本地路径>]*)\}', body)
    if collections.Counter(ob) != collections.Counter(eb):
        problems.append(f"env mismatch +{dict(collections.Counter(ob)-collections.Counter(eb))} -{dict(collections.Counter(eb)-collections.Counter(ob))}")
    dollars = len(re.findall(r'(?<!\\)\$', body))
    if dollars % 2:
        problems.append(f"odd $ ({dollars})")
    for bad_cmd in [r'\\documentclass', r'<本地路径>', r'\\usepackage', r'<本地路径>', r'<本地路径>', r'<本地路径>', r'<本地路径>']:
        if re.search(bad_cmd, body):
            problems.append("forbidden " + bad_cmd.replace("\\\\", "\\"))
    if "**" in body:
        problems.append("markdown **")
    if "\u3000" in body:
        problems.append("U+3000")
    tags = re.findall(r'<本地路径>]*)\}', body)
    dup = [k for k, v in collections.Counter(tags).items() if v > 1]
    extra = [x for x in tags if x not in all_tags and x not in BAKED and x not in KNOWN_EXTRA]
    return name, problems, tags, dup, extra, t

def main():
    tlist = load_tags()
    all_tags = {t for t, _ in tlist}
    if not os.path.isdir(CH):
        print("no chunks dir"); return
    files = sorted(glob.glob(os.path.join(CH, "*.tex")))
    got = set()
    any_prob = False
    print(f"chunks={len(files)}  tags_ref={len(all_tags)}")
    for f in files:
        name, problems, tags, dup, extra, t = check_file(f, all_tags)
        got.update(tags)
        # 分块 tag 核对
        rng = CHUNKS.get(name)
        detail = ""
        if rng:
            exp = {tg for tg, pg in tlist if rng[0] <= pg <= rng[1]}
            miss = sorted(exp - set(tags), key=lambda s: (int(s.split('.')[0]), int(s.split('.')[1])))
            ex = sorted(set(tags) - exp)
            detail = f" exp={len(exp)} got={len(tags)}"
            if miss:
                detail += f" MISS={miss}"
            if ex:
                detail += f" EXTRA={ex}"
        if dup or extra:
            problems.append(f"dup={dup} extra={extra}")
        if problems:
            any_prob = True
            print(f"[{name}] " + "; ".join(problems) + detail)
        else:
            print(f"[{name}] ok  tags={len(tags)}" + detail)
    missing = sorted(all_tags - got, key=lambda s: (int(s.split('.')[0]), int(s.split('.')[1])))
    print(f"\ntags_in_tex={len(got)}  tags_ref={len(all_tags)}")
    if missing:
        bych = collections.defaultdict(list)
        for m in missing:
            bych[m.split('.')[0]].append(m)
        print("MISSING tags（尚未翻译/OCR 漏检）:")
        for ch in sorted(bych, key=int):
            print(f"  ch{ch}: {', '.join(bych[ch])}")
    else:
        print("MISSING tags: none")
    # 页标记覆盖
    marks = set()
    for f in files:
        for m in re.finditer(r'% \[原文 p\.(\d+)\]', open(f, encoding="utf-8").read()):
            marks.add(int(m.group(1)))
    lack = [p for p in range(1, 141) if p not in marks]
    print(f"page markers: {len(marks)} 个；正文 p.1–140 缺: {lack if lack else 'none'}")
    print("STATUS:", "FAIL" if any_prob else "OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
