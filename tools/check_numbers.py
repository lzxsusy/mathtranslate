# -*- coding: utf-8 -*-
r"""口径闸门：扫描说明文件，拦截已退役的数字写法。

背景：本仓库反复出现「同一件事 3–6 套数字」（手写数字 + 统计边界变化）。
`make_stats.py` 保证 README 统计块永远正确，本脚本负责**其余文档**。

用法：
    python tools/check_numbers.py            # 报告并 exit 1（有命中）
    python tools/check_numbers.py --list     # 只列出被扫描的文件
    python tools/check_numbers.py --fix-hint # 仅打印修复建议

规则：
- 只扫「说明文件」：仓库根的 *.md、04_playbook/*.md、datasets/README.md 与
  datasets/*/README.md、site/*.html、tools/build_site.py。
- 首 8 行内出现 `历史快照` 标记的文件整个跳过（历史记录允许保留旧数）。
- 命中退役数字 → 报 file:line 与命中词，exit 1。
- 退役清单与 `_meta/口径.md` §4 保持一致；改清单要两边一起改。
"""
import argparse
import glob
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 退役数字：(模式, 说明)
RETIRED = [
    (r"49[,，]?035", "旧语料段数（现 49,322）"),
    (r"49[,，]?038", "旧语料段数（L0 修正前）"),
    (r"47[,，]?469", "旧唯一段数（现 47,756）"),
    (r"42[,，]?153", "旧公式段数（现 42,396）"),
    (r"44[,，]?087", "旧干净子集段数（需重跑 make_train_subset.py）"),
    (r"4[,，]?035[,，]?682", "旧汉字数（现 4,055,500）"),
    (r"\b10[567]\s*部", "旧工程数（现 113 部）"),
    (r"\b9[235]\s*部", "旧工程数（现 113 部 / 100 部带源码）"),
    (r"9[03]0\s*张", "旧资料卡数（现 1,034 张）"),
    (r"996\s*[张条]", "旧资料卡数（现 1,034 张）"),
    (r"10[,，]?04[36]", "旧文件数"),
    (r"10[,，]?8[67][01]", "旧文件数（以 stats.json 为准）"),
    (r"442\.9\s*MB", "旧体积（含 Release 资产口径）"),
    (r"398\.6\s*MB", "旧体积"),
    (r"11[,，]?404\s*页", "无实测来源的页数估算"),
    (r"¥?0\.21\s*/\s*页", "分母不可复算的成本"),
]

FILES = []
for pat in ["*.md", "04_playbook/*.md", "datasets/README.md", "datasets/*/README.md",
            "site/*.html", "tools/build_site.py"]:
    FILES.extend(glob.glob(os.path.join(REPO, pat)))
FILES = sorted({os.path.normpath(p) for p in FILES})

HIST_MARK = "历史快照"


def is_historical(lines):
    return any(HIST_MARK in ln for ln in lines[:8])


def scan(path):
    try:
        lines = io.open(path, encoding="utf-8", errors="replace").read().splitlines()
    except OSError:
        return []
    if is_historical(lines):
        return []
    hits = []
    for i, ln in enumerate(lines, 1):
        for pat, why in RETIRED:
            for m in re.finditer(pat, ln):
                hits.append((i, m.group(0), why, ln.strip()[:110]))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list:
        print("扫描 %d 个文件：" % len(FILES))
        for f in FILES:
            print("  " + os.path.relpath(f, REPO))
        return 0

    total = 0
    bad_files = 0
    for f in FILES:
        rel = os.path.relpath(f, REPO).replace("\\", "/")
        hits = scan(f)
        if not hits:
            continue
        total += len(hits)
        bad_files += 1
        print("\n%s" % rel)
        for ln, word, why, ctx in hits:
            print("  %s:%d  [%s]  %s\n      %s" % (rel, ln, word, why, ctx))
    print("\n扫描 %d 个文件，%d 处退役数字，涉及 %d 个文件；口径定义见 _meta/口径.md"
          % (len(FILES), total, bad_files))
    if total:
        print("修法：把数字改成 _meta/stats.json 的当前值，或给历史文档加 `> **历史快照**` 标记。")
        return 1
    print("[OK] 说明文件中没有退役数字")
    return 0


if __name__ == "__main__":
    sys.exit(main())
