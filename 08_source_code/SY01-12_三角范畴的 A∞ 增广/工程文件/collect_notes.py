# -*- coding: utf-8 -*-
r"""collect_notes.py —— 抽取 src/chunks/cNN.tex 里全部 \transnote{...}，生成 审校批注汇总.md。

用法（工程根目录）：
    python collect_notes.py

规则：
- 支持多行、可嵌套花括号的注文；
- 按块分组，尽量给出该注文之前最近的 `% ===== 原书 p.N =====` 标记作为原书页码；
- 输出统一 UTF-8（无 BOM），控制台只打印英文统计量，避免中文乱码。
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
CHUNKS_DIR = os.path.join(ROOT, "src", "chunks")
OUT = os.path.join(ROOT, "审校批注汇总.md")

CHUNK_TITLE = {
    "c00": "§1 導入（p.42–43）",
    "c01": "§2 A∞ 圏（p.44–46）",
    "c02": "§3 三角圏の構成（p.46–48）",
    "c03": "§4 主問題（p.48–50）",
    "c04": "§5 捻り積（p.50–53）",
    "c05": "§6 反例（p.53–54）",
    "c06": "§7 一意性（p.54–57）",
    "c07": "§8 おわりに ＋ 参考文献（p.57–58）",
}


def extract(text):
    """返回 [(pos, note_text), ...]，按出现顺序。"""
    out = []
    for m in re.finditer(r"<本地路径>*\{", text):
        i = m.end()  # 指向 { 之后
        depth = 1
        j = i
        while j < len(text) and depth:
            c = text[j]
            if c == "\\":
                j += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        out.append((m.start(), text[i:j - 1]))
    return out


def page_before(text, pos):
    """该位置之前最近的 `% ===== 原书 p.N =====` 里的 N。"""
    head = text[:pos]
    pages = re.findall(r"%\s*=+\s*原书\s*p\.\s*(\d+)", head)
    return pages[-1] if pages else "?"


def tidy(s):
    s = re.sub(r"\s*\n\s*", "", s.strip())
    return s


def main():
    files = sorted(f for f in os.listdir(CHUNKS_DIR) if re.fullmatch(r"c\d\d\.tex", f))
    lines = ["# 审校批注汇总（Tutor Notes）", ""]
    lines.append("> 本表由 `collect_notes.py` 从 `src/chunks/cNN.tex` 自动抽取，"
                 "供通读校对使用。页码为底本原书页码（= PDF 页 + 41）。")
    lines.append("")
    total = 0
    body = []
    for f in files:
        cid = f[:3]
        with io.open(os.path.join(CHUNKS_DIR, f), encoding="utf-8") as fh:
            text = fh.read()
        notes = extract(text)
        if not notes:
            continue
        body.append(f"## {cid} {CHUNK_TITLE.get(cid, '')}")
        body.append("")
        for k, (pos, raw) in enumerate(notes, 1):
            body.append(f"**{cid}-{k}**（原书 p.{page_before(text, pos)}）{tidy(raw)}")
            body.append("")
        total += len(notes)
    lines.append(f"合计 **{total}** 条。")
    lines.append("")
    lines.extend(body)
    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("notes:", total, "->", OUT)


if __name__ == "__main__":
    main()
