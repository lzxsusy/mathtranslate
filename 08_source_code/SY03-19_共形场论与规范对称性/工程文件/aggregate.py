# -*- coding: utf-8 -*-
"""汇总工具（Lead 独占）：
  1) 从 src/b*.tex 抽 % [Tutor Note: ...] 批注，写 译注汇总.md
  2) 检查各章 \\tag{x.y} 连续性，报告缺号/重号/乱序
  3) 从 block-reports/*.md 抽 ERRATA 行，写 ERRATA.md
用法: python aggregate.py [--tags|--notes|--errata|--all]
"""
import os, re, sys, glob, io

ROOT = os.path.dirname(os.path.abspath(__file__))
BLOCKS = ["b00_preface", "b00_notation"] + ["b%02d" % i for i in range(1, 18)]


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def collect_notes():
    out = ["# \u8bd1\u6ce8\u6c47\u603b\uff08Tutor Notes\uff09", "",
           "\u672c\u6587\u4ef6\u7531 `aggregate.py` \u4ece `src/b*.tex` \u7684 LaTeX \u6ce8\u91ca\u81ea\u52a8\u62bd\u53d6\u3002",
           "\u683c\u5f0f\uff1a`[\u539f\u6587 p.N]` \u4e3a\u6279\u6ce8\u6240\u5728\u5370\u5237\u9875\uff1b\u6279\u6ce8\u7f16\u53f7\u4e3a\u5757\u5185\u5e8f\u53f7\u3002", ""]
    total = 0
    for name in BLOCKS:
        p = os.path.join(ROOT, "src", name + ".tex")
        if not os.path.exists(p):
            continue
        lines = read(p).split("\n")
        page = "?"
        notes = []
        i, n = 0, len(lines)
        while i < n:
            ln = lines[i]
            m = re.match(r"\s*%\s*\[\u539f\u6587 p\.(\S+?)\]", ln)
            if m:
                page = m.group(1)
            m2 = re.match(r"\s*%\s*\[Tutor Note:(.*)$", ln)
            if m2:
                parts = [m2.group(1).strip()]
                j = i + 1
                while j < n:
                    nxt = lines[j]
                    if re.match(r"\s*%\s*\[Tutor Note:", nxt) or re.match(r"\s*%\s*\[\u539f\u6587 p\.", nxt):
                        break
                    if not re.match(r"\s*%", nxt):
                        break
                    parts.append(re.sub(r"^\s*%\s?", "", nxt).strip())
                    j += 1
                txt = " ".join(x for x in parts if x)
                if txt.endswith("]"):
                    txt = txt[:-1].strip()
                notes.append({"page": page, "text": txt})
                i = j
                continue
            i += 1
        if not notes:
            continue
        out.append("## Block %s\uff08%d \u6761\uff09" % (name.upper(), len(notes)))
        out.append("")
        for i, nt in enumerate(notes, 1):
            t = re.sub(r"\s+", " ", nt["text"]).strip()
            out.append("%d. `[\u539f\u6587 p.%s]` %s" % (i, nt["page"], t))
        out.append("")
        total += len(notes)
    with open(os.path.join(ROOT, "\u8bd1\u6ce8\u6c47\u603b.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    print("\u8bd1\u6ce8\u6c47\u603b.md \u5199\u6bd5\uff0c\u5171 %d \u6761\u6279\u6ce8" % total)


def check_tags():
    bad = 0
    for ch in range(1, 7):
        seen = []
        src = ""
        for name in BLOCKS:
            p = os.path.join(ROOT, "src", name + ".tex")
            if not os.path.exists(p):
                continue
            text = read(p)
            for m in re.finditer(r"<本地路径>)\.(\d+)\}", text):
                if int(m.group(1)) == ch:
                    seen.append((int(m.group(2)), name))
        if not seen:
            continue
        nums = [n for n, _ in seen]
        dups = sorted({n for n in nums if nums.count(n) > 1})
        missing = [n for n in range(1, max(nums) + 1) if n not in nums]
        disorder = []
        prev = 0
        for n, name in seen:
            if n < prev:
                disorder.append((n, name))
            prev = max(prev, n)
        print("Ch%d: %d 条 tag，最大 (%d.%d)，缺号 %s，重号 %s，乱序处 %d"
              % (ch, len(nums), ch, max(nums), missing or "无",
                 dups or "无", len(disorder)))
        if missing or dups or disorder:
            bad += 1
    print("TAG-CHECK:", "OK" if bad == 0 else "PROBLEM（见上）")


def collect_errata():
    out = ["# ERRATA\uff08\u539f\u6587\u7b14\u8bef\u4e0e\u8bd1\u6ce8\u66f4\u6b63\uff09", "",
           "\u7531 `aggregate.py` \u4ece `block-reports/*.md` \u7684 `ERRATA` \u6bb5\u81ea\u52a8\u6c47\u603b\uff08\u4e00\u6761 = \u4e00\u4e2a\u7a7a\u884c\u5206\u9694\u7684\u6bb5\uff1b\u683c\u5f0f\uff1a\u9875/\u7f16\u53f7 | \u539f\u6587 | \u5e94\u4e3a | \u7406\u7531\uff09\u3002", ""]
    total = 0
    for p in sorted(glob.glob(os.path.join(ROOT, "block-reports", "*.md"))):
        lines = read(p).split("\n")
        items, grab, buf = [], False, []
        def flush():
            if buf:
                t = " ".join(buf).strip()
                t = re.sub(r"^(?:[-*\u2022]|\d+[.)])\s*", "", t).strip()
                if t:
                    items.append(t)
                del buf[:]
        for ln in lines:
            if re.match(r"\s*ERRATA", ln):
                flush()
                grab = True
                rest = re.split(r"[:\uff1a]", ln, 1)
                if len(rest) > 1 and rest[1].strip() not in ("", "\u65e0", "none", "-"):
                    buf.append(rest[1].strip())
                continue
            if grab:
                if re.match(r"\s*#{1,6}\s", ln) or re.match(r"\s*[A-Z]{4,}\s*[:\uff1a]", ln):
                    flush()
                    grab = False
                    continue
                s0 = ln.strip()
                if not s0:
                    flush()
                    continue
                if re.match(r"^(?:[-*\u2022]|\d+[.)])\s", s0):
                    flush()
                buf.append(s0)
        flush()
        if items:
            out.append("## %s" % os.path.basename(p).replace(".md", "").upper())
            for it in items:
                out.append("- %s" % it)
            out.append("")
            total += len(items)
    with open(os.path.join(ROOT, "ERRATA.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    print("ERRATA.md \u5199\u6bd5\uff0c\u5171 %d \u6761" % total)


def main():
    args = sys.argv[1:]
    if not args:
        args = ["--all"]
    if "--all" in args or "--tags" in args:
        check_tags()
    if "--all" in args or "--notes" in args:
        collect_notes()
    if "--all" in args or "--errata" in args:
        collect_errata()


if __name__ == "__main__":
    main()
