# -*- coding: utf-8 -*-
"""从 src/chunks/*.tex 提取 % [Tutor Note: ...] 批注（支持多行），生成 审校批注汇总.md。"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
CHUNKS = os.path.join(ROOT, "src", "chunks")
OUT = os.path.join(ROOT, "审校批注汇总.md")

CHUNK_INFO = {
    "c00": "p001（原书 p.127）",
    "c01": "p002–p003（原书 p.128–129）",
    "c02": "p004–p005（原书 p.130–131）",
    "c03": "p006–p007（原书 p.132–133）",
    "c04": "p008–p010（原书 p.134–136）",
    "c05": "p011–p013（原书 p.137–139）",
    "c06": "p014–p016（原书 p.140–142）",
    "c07": "p017–p019（原书 p.143–145）",
    "c08": "p020–p021（原书 p.146–147）",
    "c09": "p022–p025（原书 p.148–151）",
}

PAGE_RE = re.compile(r"原书 p\.(\d+)")


def extract_notes(text):
    """Return list of (page_hint_or_None, note_text)."""
    lines = text.splitlines()
    notes = []
    cur_page = None
    i = 0
    while i < len(lines):
        line = lines[i]
        m = PAGE_RE.search(line)
        if m:
            cur_page = m.group(1)
        if "[Tutor Note:" in line:
            # collect continuation lines
            buf = []
            first = line
            while True:
                seg = re.sub(r"^\s*%\s?", "", first).strip()
                buf.append(seg)
                if "]" in seg:
                    break
                i += 1
                if i >= len(lines):
                    break
                first = lines[i]
                if not first.strip().startswith("%"):
                    break
            joined = " ".join(buf)
            start = joined.find("[Tutor Note:")
            body = joined[start + len("[Tutor Note:"):]
            end = body.rfind("]")
            if end >= 0:
                body = body[:end]
            notes.append((cur_page, re.sub(r"\s+", " ", body).strip()))
        i += 1
    return notes


def main():
    out = []
    total = 0
    per = {}
    for name in sorted(CHUNK_INFO):
        path = os.path.join(CHUNKS, name + ".tex")
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        notes = extract_notes(text)
        if notes:
            per[name] = notes
            total += len(notes)

    out.append("# 审校批注汇总")
    out.append("")
    out.append("> 植田一石《ミラー対称性と K3 曲面》中文译注本 · 共 **%d 条** `%% [Tutor Note: …]`" % total)
    out.append("> 本文件由 `collect_notes.py` 从 `src/chunks/*.tex` 自动生成；改批注后请重新生成，禁止手改。")
    out.append("> 批注只记录「照原文、不擅改」的疑点与约定，正文一律按原文（或按 Lead 裁定的统一体例）排印。")
    out.append("")
    for name, notes in per.items():
        out.append("## %s（%s）" % (name, CHUNK_INFO.get(name, "")))
        out.append("")
        for i, (page, note) in enumerate(notes, 1):
            page_s = "原书 p.%s" % page if page else "页界处"
            out.append("%d. 【%s】%s" % (i, page_s, note))
        out.append("")
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print("wrote", OUT, "notes:", total)


if __name__ == "__main__":
    main()
