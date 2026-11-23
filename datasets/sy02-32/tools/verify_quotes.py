#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""检查资料卡里的 sources[].quote 是否真在本工程原文里（逐字命中）。

与 ggl_文献库/tools/verify_pages.py 的区别：那个按 txt/<NN>/pNNN.txt 组织，
本工程原文是 01_pages/pNNN.txt（pdf 页 = 印刷页）。所以复制一份、换掉取文路径，
并顺带把 --strict 的含义定成「有问题就 exit 1」。

用法:
    python 资料卡/tools/verify_quotes.py 资料卡/cards [--root 工程根] [--strict] [--quiet]

检查三类问题：
  1. quote 在卡片声明的 pages 范围里搜不到（可能页码写错）；
  2. quote 在整个原文里都搜不到（引文不存在 / 抄错 / 编的）；
  3. quote 长度不在 12–120 字符、或含中文字符。
"""
import argparse
import glob
import io
import json
import os
import re
import sys

LIG = {
    "\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl",
    "\ufb05": "st", "\ufb06": "st",
}
KEEP = re.compile(r"[a-z0-9]+")
CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")


def norm(s):
    s = s or ""
    for k, v in LIG.items():
        s = s.replace(k, v)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    s = s.replace("\u00a0", " ")
    return "".join(KEEP.findall(s.lower()))


def _has_pages(root):
    """逐页文本可能在 01_pages/，也可能在 工程文件/work/src/（本工程即是，且不入仓）。"""
    return (os.path.isdir(os.path.join(root, "01_pages"))
            or os.path.isdir(os.path.join(root, "工程文件", "work", "src")))


def load_pages(root):
    pat = os.path.join(root, "工程文件", "work", "src", "p*.txt")
    pages = {}
    for p in sorted(glob.glob(pat)):
        m = re.search(r"p(\d+)\.txt$", os.path.basename(p))
        if not m:
            continue
        pages[int(m.group(1))] = norm(io.open(p, encoding="utf-8", errors="replace").read())
    return pages


def walk_cards(cards_dir):
    for p in sorted(glob.glob(os.path.join(cards_dir, "**", "*.json"), recursive=True)):
        try:
            yield p, json.load(io.open(p, encoding="utf-8"))
        except Exception as e:  # 坏 JSON 由 lint 管，这里跳过
            print("[skip] %s: %s" % (os.path.relpath(p, cards_dir), e))
            continue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="卡片目录，例如 资料卡/cards")
    ap.add_argument("--root", default="", help="工程根（默认从 target 往上找含 01_pages 的目录）")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    root = a.root
    if not root:
        cur = os.path.abspath(a.target)
        while cur and cur != os.path.dirname(cur):
            if _has_pages(cur):
                root = cur
                break
            cur = os.path.dirname(cur)
    if not root or not _has_pages(root):
        print("[error] 找不到 01_pages/ 或 工程文件/work/src/，请用 --root 指定工程根")
        return 2

    pages = load_pages(root)
    if not pages:
        print("[error] 01_pages/ 下没有 pNNN.txt")
        return 2

    total = bad_len = bad_cjk = miss_range = miss_all = 0
    problems = []
    for path, card in walk_cards(a.target):
        cid = card.get("id") or os.path.basename(path)
        for i, src in enumerate(card.get("sources") or []):
            q = src.get("quote")
            if not q:
                continue
            total += 1
            n = norm(q)
            pgs = src.get("pages") or []
            try:
                lo, hi = int(pgs[0]), int(pgs[1])
            except Exception:
                lo = hi = None
            tag = "%s sources[%d]" % (cid, i)
            if len(q) < 12 or len(q) > 120:
                bad_len += 1
                problems.append("%s quote 长度 %d 不在 12–120" % (tag, len(q)))
            if CJK.search(q):
                bad_cjk += 1
                problems.append("%s quote 含中文" % tag)
            if lo is None:
                if n not in "".join(pages.values()):
                    miss_all += 1
                    problems.append("%s quote 全局搜不到：%r" % (tag, q[:60]))
                continue
            hit = [p for p in range(lo, hi + 1) if p in pages and n in pages[p]]
            if hit:
                continue
            anyp = [p for p in sorted(pages) if n in pages[p]]
            if anyp:
                miss_range += 1
                problems.append("%s 页码不符：卡片写 p.%d–%d，实际 p.%s"
                                % (tag, lo, hi, ",".join(str(x) for x in anyp[:4])))
            else:
                miss_all += 1
                problems.append("%s 全局搜不到：%r" % (tag, q[:60]))

    if problems and not a.quiet:
        for p in problems:
            print("[!] " + p)
    print("[done] 核对 %d 条 quote：长度问题 %d、含中文 %d、页码不符 %d、搜不到 %d"
          % (total, bad_len, bad_cjk, miss_range, miss_all))
    if not problems:
        print("[ok] 全部 quote 在声明页范围内逐字命中")
    if a.strict and problems:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
