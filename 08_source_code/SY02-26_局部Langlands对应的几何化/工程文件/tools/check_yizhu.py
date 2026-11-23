# -*- coding: utf-8 -*-
"""check_yizhu.py —— 译注（\\yizhu / \\yizhuw）体检。

三件事：
1. 每条译注的文字是否真的出现在 PDF 里（防被行尾 % 注释掉、被环境吞掉）；
2. PDF 里是否存在「孤立脚注号」——某一行只剩一个上标数字，说明译注被排成了独立段落；
3. 统计译注条数，便于与源文件对照。

用法：
    python ../工程文件/tools/check_yizhu.py main.pdf
    python ../工程文件/tools/check_yizhu.py main.pdf --tex sections      # 只查指定目录的 tex
"""
import argparse
import glob
import io
import os
import re
import sys

CJK_RUN = re.compile(r"[\u4e00-\u9fff]{8,}")
YIZHU = re.compile(r"(?<!%)\\(yizhu|yizhuw)\{")


def arg1(s):
    i = s.index("{")
    d = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            d += 1
        elif s[j] == "}":
            d -= 1
            if d == 0:
                return s[i + 1:j]
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--tex", default="sections")
    args = ap.parse_args()

    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf

    doc = pymupdf.open(args.pdf)
    pages = [doc[i].get_text() for i in range(doc.page_count)]
    flat = re.sub(r"\s+", "", "".join(pages))

    # 1. 译注是否都在 PDF 里
    total, skip, miss = 0, 0, []
    texdir = args.tex
    if not os.path.isdir(texdir):
        texdir = os.path.join(os.path.dirname(os.path.abspath(args.pdf)), args.tex)
    for p in sorted(glob.glob(os.path.join(texdir, "*.tex"))):
        for no, line in enumerate(io.open(p, encoding="utf-8").read().split("\n"), 1):
            if line.lstrip().startswith("%"):
                continue
            for m in YIZHU.finditer(line):
                total += 1
                body = re.sub(r"\$[^$]*\$", "", arg1(line[m.start():]))
                runs = CJK_RUN.findall(body)
                if not runs:
                    skip += 1
                    continue
                key = max(runs, key=len)[:8]
                if key not in flat:
                    miss.append("  %s:%d  %s" % (os.path.basename(p), no, key))

    # 2. 孤立脚注号
    orphan = []
    for pno in range(doc.page_count):
        for b in doc[pno].get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                spans = [s for s in l["spans"] if s["text"].strip()]
                if len(spans) == 1:
                    t = spans[0]["text"].strip()
                    if re.fullmatch(r"\d+", t) and spans[0]["size"] < 9.5:
                        orphan.append("  第 %d 页：%s" % (pno + 1, t))

    print("[info] 源文件译注 %d 条（%d 条无可检索汉字，跳过）" % (total, skip))
    if miss:
        print("[FAIL] %d 条译注在 PDF 里找不到（多半被行尾 %% 注释掉或被环境吞了）：" % len(miss))
        print("\n".join(miss))
    else:
        print("[ok] 每条译注都能在 PDF 中找到")
    if orphan:
        print("[FAIL] %d 个孤立脚注号（译注被排成独立段落，需并回上一句末）：" % len(orphan))
        print("\n".join(orphan))
    else:
        print("[ok] 无孤立脚注号")
    sys.exit(1 if (miss or orphan) else 0)


if __name__ == "__main__":
    main()
