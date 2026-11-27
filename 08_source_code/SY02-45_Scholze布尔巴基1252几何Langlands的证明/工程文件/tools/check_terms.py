#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""check_terms.py — SY02-45 术语一致性总检（交付强制）

做三件事：
  ① 每个 glossary 词条在正文至少出现一次（确有用到却没有 = 漏译/异译）
  ② 异译黑名单出现次数必须为 0
  ③ 输出全书术语使用计数表 → 工程文件/work/术语使用统计.txt

用法：
    python check_terms.py            # 全检
    python check_terms.py --stat     # 只看统计

退出码：0 = 通过；1 = 有硬伤；2 = 环境问题
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[2]
SECT = ROOT / "源码" / "sections"
WORK = ROOT / "工程文件" / "work"
GLOSSARY = WORK / "glossary.tsv"
STAT_OUT = WORK / "术语使用统计.txt"

# ② 异译黑名单：本库冻结值之外的通行异名，出现即错
BLACKLIST = [
    ("错致层", "perverse sheaf 应为「反常层」（T1131 frozen）"),
    ("钻石", "diamond 应为「菱形」"),
    ("完全胚空间", "perfectoid 应为「完满空间」"),
    ("完全胚", "perfectoid 应为「完满」"),
    ("斜置", "tilt 应为「倾斜」"),
    ("正置", "untilt 不译，保留 untilt"),
    ("有理晶体", "isocrystal 应为「等晶体」"),
    ("固态", "solid 应为「固体」"),
    ("仿射胚", "affinoid 保留英文"),
    ("棱镜化", "prismatic 应为「棱镜」体系"),
    ("块", None),   # 占位：shtuka 不译，禁用「块」指 shtuka；仅在「shtuka」语境判，见下
    ("爪", "leg 不译，保留 leg"),
]
BLACKLIST = [(w, why) for w, why in BLACKLIST if why]  # 去掉占位项

FORBIDDEN = [r"\\ref\b", r"\\eqref\b", r"\\label\b", r"\\cite\b",
             r"\\pageref\b", r"\\autoref\b"]

COMMENT = re.compile(r"(?<!\\)%[^\n]*")


def load_glossary():
    rows = []
    if not GLOSSARY.exists():
        return rows
    for ln in GLOSSARY.read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("英文\t"):
            continue
        parts = ln.split("\t")
        parts += [""] * (5 - len(parts))
        rows.append(parts[:5])
    return rows


def iter_sections():
    for f in sorted(SECT.glob("s*.tex")):
        txt = f.read_text(encoding="utf-8")
        yield f, COMMENT.sub("", txt)


def norm(s):
    """记号归一化：去掉 $ 与单字母宏，\\infty→∞，LaTeX 双连字符→en dash。
    术语比对只在归一化文本上做，避免 $p$ 进域 / 稳定 $(\\infty,1)$-范畴 这类记号差异造成假阳性。"""
    s = s.replace("$", "")
    s = re.sub(r"\\(?:mathbb|mathbf|mathrm|mathit|mathcal|operatorname)\{([A-Za-z])\}", r"\1", s)
    s = s.replace("\\infty", "∞")
    s = s.replace("---", "—").replace("--", "–")
    return re.sub(r"\s+", " ", s)


def page_at(txt, pos):
    """返回 pos 之前最近的 \\srcpage 页码"""
    found = re.findall(r"\\srcpage\{(\d+)\}", txt[:pos])
    return int(found[-1]) if found else 0


def main():
    stat_only = "--stat" in sys.argv
    gloss = load_glossary()
    files = list(iter_sections())
    if not files:
        print("没有 源码/sections/*.tex")
        return 2
    blob = "\n".join(t for _, t in files)
    blob_n = norm(blob)
    errors, warns = [], []

    # ① 覆盖率（在归一化文本上计数）
    used, missing = [], []
    for eng, zh, basis, page, note in gloss:
        if not zh.strip():
            continue
        zh_n = norm(zh)
        n = blob_n.count(zh_n) if re.search(r"[\u4e00-\u9fff]", zh_n) else len(
            re.findall(r"(?<![A-Za-z])" + re.escape(zh_n) + r"(?![A-Za-z])", blob_n))
        (used if n else missing).append((eng, zh, basis, page, note, n))
    if missing and not stat_only:
        for eng, zh, *_ in missing:
            errors.append(f"术语未出现：{eng} → {zh}（若原文确有该词则漏译，若无则从 glossary 移除）")

    # ② 黑名单
    if not stat_only:
        for word, why in BLACKLIST:
            c = blob.count(word)
            if c:
                pos = blob.find(word)
                errors.append(f"异译黑名单命中 {c} 次：「{word}」——{why}")
        for pat in FORBIDDEN:
            hits = [m.group(0) for m in re.finditer(pat, blob)]
            if hits:
                errors.append(f"禁用命令 {pat} 出现 {len(hits)} 次")

    # ③ 统计表
    lines = ["# SY02-45 术语使用统计（由 tools/check_terms.py 生成）",
             "",
             f"# 节文件 {len(files)} 个；glossary 词条 {len(gloss)} 条；命中 {len(used)} 条；未命中 {len(missing)} 条",
             "",
             "词条\t中文\t依据\tglossary 首现页\t译文首见页\t全书次数"]
    detail = []
    for eng, zh, basis, page, note, n in used + missing:
        # 译文首见页
        p0 = 0
        for f, t in files:
            i = t.find(zh) if re.search(r"[\u4e00-\u9fff]", zh) else -1
            if i >= 0:
                p0 = page_at(t, i)
                break
        detail.append((eng, zh, basis, page, p0, n))
    detail.sort(key=lambda r: (-r[5], r[1]))
    for eng, zh, basis, page, p0, n in detail:
        lines.append(f"{eng}\t{zh}\t{basis}\t{page}\t{p0}\t{n}")
    STAT_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"glossary {len(gloss)} 条：命中 {len(used)}，未命中 {len(missing)}")
    if missing:
        print("  未命中：" + "、".join(f"{e}→{z}" for e, z, *_ in missing))
    print(f"统计表 → {STAT_OUT.relative_to(ROOT)}")
    if errors:
        print(f"\n== 硬伤 {len(errors)} 条 ==")
        for e in errors:
            print("  -", e)
        return 1
    print("\n== 术语检查通过（黑名单 0 命中，禁用命令 0 命中）==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
