# -*- coding: utf-8 -*-
"""v1/v2 正文比对：v1 抽文 → external/v1txt/，再与 txt/04 逐页比对。"""
import re
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
V1 = HERE / "0809.0305v1.pdf"
V1TXT = HERE / "v1txt"
V2TXT = ROOT / "txt" / "04"


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def main():
    V1TXT.mkdir(exist_ok=True)
    doc = fitz.open(V1)
    pages = []
    for i, page in enumerate(doc, 1):
        t = page.get_text()
        (V1TXT / f"p{i:03d}.txt").write_text(t, encoding="utf-8")
        pages.append(t)
    print(f"v1 pages = {doc.page_count}")
    v2 = [ (V2TXT / f"p{i:03d}.txt").read_text(encoding="utf-8") for i in range(1, 73) ]
    # 逐页找 v2 页在 v1 中的最佳位置（正文页码对齐）
    v1n = [norm(t) for t in pages]
    offset_hits = {}
    for i in range(1, 73):
        n2 = norm(v2[i - 1])
        if len(n2) < 200:
            continue
        probe = n2[:600]
        best = None
        for j, t in enumerate(v1n):
            if probe in t:
                best = j + 1
                break
        offset_hits[i] = best
    pairs = [(k, v) for k, v in offset_hits.items() if v]
    print("对齐样本（v2页 -> v1页）:", pairs[:8], "...", pairs[-8:] if len(pairs) > 8 else "")
    # 全文字符流比对：去掉参考文献部分
    def strip_refs(t):
        return t.split("References")[0]
    body2 = strip_refs("".join(v2))
    body1 = strip_refs("".join(pages))
    n1, n2 = norm(body1), norm(body2)
    print(f"正文归一化长度 v1={len(n1)} v2={len(n2)} 差={len(n2)-len(n1)}")
    # 找第一处不同
    k = 0
    while k < min(len(n1), len(n2)) and n1[k] == n2[k]:
        k += 1
    print(f"前 {k} 字符相同；v1 从此处起：{body1[-200:] if False else ''}")
    print("v1 片段:", repr(body1[max(0, k // 1 - 0) : ])[:0])
    # 反查位置：用 v1 原文找 k 附近的英文
    print("相同前缀在 v1 页码：", end="")
    acc = 0
    for i, t in enumerate(pages, 1):
        acc += len(norm(t))
        if acc > k:
            print(i)
            break
    print("v2 第 1 页与 v1 第 1 页相同？", norm(v2[0]) == norm(pages[0]))
    # 参考文献条数
    def nrefs(t):
        return len(re.findall(r"^\[\d+\]", t, re.M))
    print("v1 参考文献条目（正则）:", sum(nrefs(t) for t in pages))
    print("v2 参考文献条目（正则）:", sum(nrefs(t) for t in v2))
    # 逐页差异表
    print("\n页数对照（v2: 长度 | v1 同位置长度）")
    for i in range(1, 73):
        j = offset_hits.get(i)
        if j is None:
            print(f"p{i:03d}: 未在 v1 找到对应页")
            continue
        a, b = len(norm(v2[i - 1])), len(norm(pages[j - 1]))
        flag = "" if a == b else f" 差 {a-b:+d}"
        print(f"p{i:03d} -> v1 p{j:03d}  {a} vs {b}{flag}")


if __name__ == "__main__":
    sys.exit(main())
