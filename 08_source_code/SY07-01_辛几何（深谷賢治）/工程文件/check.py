# -*- coding: utf-8 -*-
"""Gate 1 静态检查：tag 完整性 / 花括号 / 环境配对 / $ 偶偶 / 禁用命令 / 编码"""
import os, re, sys, glob, collections

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
TAGS = os.path.join(ROOT, "work", "tags.txt")

def read(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()

def strip_comments(t):
    out = []
    for line in t.splitlines():
        # 去掉未转义的 % 之后的内容（简化：偶数个反斜杠后的 % 才算注释）
        m = re.search(r'(?<!\\)(?:\\\\)*%', line)
        if m:
            cut = m.end() - 1
            line = line[:cut]
        out.append(line)
    return "\n".join(out)

def load_tags():
    tags = set()
    if not os.path.exists(TAGS):
        return tags
    for line in read(TAGS).splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if parts:
            tags.add(parts[0].strip())
    return tags

def check_file(path, all_tags):
    t = read(path)
    body = strip_comments(t)
    name = os.path.basename(path)
    problems = []
    # BOM
    with open(path, "rb") as f:
        raw = f.read(3)
    if raw == b"\xef\xbb\xbf":
        problems.append("UTF-8 BOM present")
    if "\ufffd" in t:
        problems.append("U+FFFD found")
    # braces
    depth = 0; bad = False
    for ch in body:
        if ch == "{": depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0: bad = True; break
    if depth != 0 or bad:
        problems.append(f"brace imbalance ({depth})")
    # environments
    ob = re.findall(r'<本地路径>]*)\}', body)
    eb = re.findall(r'<本地路径>]*)\}', body)
    if collections.Counter(ob) != collections.Counter(eb):
        d1 = collections.Counter(ob) - collections.Counter(eb)
        d2 = collections.Counter(eb) - collections.Counter(ob)
        problems.append(f"env mismatch begin-only={dict(d1)} end-only={dict(d2)}")
    # $ parity
    dollars = len(re.findall(r'(?<!\\)\$', body))
    if dollars % 2 != 0:
        problems.append(f"odd $ count ({dollars})")
    # 禁用命令
    for bad_cmd in [r'\\documentclass', r'<本地路径>', r'\\usepackage', r'<本地路径>', r'<本地路径>', r'<本地路径>', r'<本地路径>']:
        if re.search(bad_cmd, body):
            problems.append("forbidden: " + bad_cmd.replace("\\\\", "\\"))
    if "**" in body:
        problems.append("markdown ** found")
    # 全角空格
    if "\u3000" in body:
        problems.append("ideographic space U+3000")
    tags = re.findall(r'<本地路径>]*)\}', body)
    dup = [k for k, v in collections.Counter(tags).items() if v > 1]
    extra = [x for x in tags if x not in all_tags]
    return name, problems, tags, dup, extra

def main():
    all_tags = load_tags()
    if not os.path.isdir(CH):
        print("no chunks dir"); return
    files = sorted(glob.glob(os.path.join(CH, "*.tex")))
    got = set()
    total = 0
    any_prob = False
    for f in files:
        name, problems, tags, dup, extra = check_file(f, all_tags)
        total += len(tags)
        got.update(tags)
        if dup or extra:
            problems.append(f"tags dup={dup} extra={extra}")
        if problems:
            any_prob = True
            print(f"[{name}] " + "; ".join(problems))
    missing = sorted(all_tags - got, key=lambda s: (int(s.split('.')[0]), int(s.split('.')[1])))
    print(f"\nchunks={len(files)}  tags_in_tex={len(got)}  tags_in_ref={len(all_tags)}")
    if missing:
        print("MISSING tags (尚未翻译/漏抄):")
        bych = collections.defaultdict(list)
        for m in missing:
            bych[m.split('.')[0]].append(m)
        for ch in sorted(bych, key=int):
            print(f"  ch{ch}: {', '.join(bych[ch])}")
    else:
        print("MISSING tags: none")
    print("STATUS:", "FAIL" if any_prob else "OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
