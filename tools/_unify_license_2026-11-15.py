# -*- coding: utf-8 -*-
"""2026-11-15 许可统一：把全库「语料 CC BY 4.0 + 译文 CC BY-NC-SA 4.0」双轨表述
统一为「全库 CC BY 4.0，欢迎训练/蒸馏/商用」。只改许可句，不动正文。"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WRITE = "--write" in sys.argv

OLD_SPLIT = "语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。"
NEW_SPLIT = "语料使用口径以 DATASHEET 与 LICENSE 为准：全库统一 CC BY 4.0，明确欢迎用于训练、蒸馏与商用（署名即可）。"

OLD_SPLIT2 = "语料使用口径以 DATASHEET 为准（CC BY 4.0，欢迎训练与蒸馏）。"
NEW_SPLIT2 = "语料使用口径以 DATASHEET 与 LICENSE 为准：全库统一 CC BY 4.0，明确欢迎训练、蒸馏与商用（署名即可）。"

OLD_NOTRAIN = "本项目语料默认不用于训练，要用须先整库审计并经 Lead 书面批准。"
NEW_NOTRAIN = "本库语料统一 CC BY 4.0，明确欢迎用于训练、蒸馏与商用（署名即可），无需另行申请许可。"

RULES = [(OLD_SPLIT, NEW_SPLIT), (OLD_SPLIT2, NEW_SPLIT2), (OLD_NOTRAIN, NEW_NOTRAIN)]

SKIP_DIRS = {".git", "01_corpus_zh", "02_trajectories", "06_sessions_raw", "assets", "_corpus_backups"}

changed, hits = [], 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        if not fn.endswith(".md"):
            continue
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p, ROOT)
        if rel in ("LICENSE", "CHANGELOG.md", "AUDIT_2026-11-15.md"):
            continue
        try:
            s = io.open(p, encoding="utf-8").read()
        except Exception:
            continue
        orig = s
        for a, b in RULES:
            if a in s:
                n = s.count(a)
                s = s.replace(a, b)
                hits += n
                changed.append((rel, a[:18], n))
        if s != orig and WRITE:
            io.open(p, "w", encoding="utf-8", newline="\n").write(s)

print("files affected:", len({c[0] for c in changed}), "replacements:", hits, "write:", WRITE)
from collections import Counter
for k, v in Counter(c[1] for c in changed).items():
    print("  ", k, v)
for rel, _, n in changed[:5]:
    print("   e.g.", rel, n)

# 残留检查
left = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        if not fn.endswith(".md"):
            continue
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p, ROOT)
        if rel in ("LICENSE", "CHANGELOG.md", "AUDIT_2026-11-15.md", "DATASHEET.md", "README.md"):
            continue
        s = io.open(p, encoding="utf-8", errors="ignore").read()
        if "默认不用于" in s or "BY-NC" in s:
            left += 1
            print("   LEFT:", rel)
print("files still carrying old wording:", left)
