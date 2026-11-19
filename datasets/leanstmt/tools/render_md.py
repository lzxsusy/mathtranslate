# -*- coding: utf-8 -*-
"""把 cards/ 渲染成 md/（人读版）。纯从卡片 JSON 渲染，不依赖 make_cards.py。"""
from __future__ import annotations

import glob
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def render(card: dict) -> str:
    src = card["source"]
    lean = card["lean"]
    ver = card["verification"]
    lines = [
        f"# {card['title']}",
        "",
        f"- 卡号：`{card['id']}`　轨道：{card['track']}　scope：`{card['scope']}`　验证：**{ver['status']}**",
        f"- 来源：{src['paper']}（{src['arxiv']}）{src['section']}，印刷页 {src['pages'][0]}–{src['pages'][1]}",
        f"- 锚点：{src['anchor']}",
        "",
        "## 原文陈述",
        "",
        f"> {card['natural_language']['zh']}",
        "",
        f"英文：{card['natural_language']['en']}",
        "",
        "## Lean 陈述",
        "",
        "```lean",
        lean["statement"],
        "```",
        "",
        f"文件 `{lean['file']}`，声明名 `{lean['name']}`；imports："
        + "、".join(f"`{i}`" for i in lean["imports"]),
        "",
        "## 依赖",
        "",
    ]
    if card["dependencies"]:
        for dep in card["dependencies"]:
            if isinstance(dep, str):
                lines.append(f"- {dep}")
            else:
                lines.append(f"- `{dep['name']}`（{dep['kind']}，`{dep['module']}`）")
    else:
        lines.append("- 仅用核心库/基础算术，无额外依赖")
    lines += ["", "## 假设", ""]
    lines += [f"- {h}" for h in card["hypotheses"]]
    lines += [
        "",
        "## 盲验回译",
        "",
        f"> {card['backtranslation']['zh']}",
        "",
        f"方法：{card['backtranslation']['method']}；验卡人：{card['backtranslation']['reviewer']}。",
        "",
        "## 备注与缺口",
        "",
        card["notes"],
        "",
    ]
    for g in card["gaps"]:
        lines.append(f"- 缺口：{g['reason']}（blocked_by: {g['blocked_by']}）")
    lines += [
        "",
        f"验证环境：{ver['toolchain']}，mathlib `{ver['mathlib_rev']}`，"
        f"检查日期 {ver['checked_at']}，`sorry` 数 {ver['sorry_count']}。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    md_dir = os.path.join(ROOT, "md")
    if not os.path.isdir(md_dir):
        os.makedirs(md_dir)
    n = 0
    for p in sorted(glob.glob(os.path.join(ROOT, "cards", "**", "*.json"), recursive=True)):
        card = json.load(io.open(p, encoding="utf-8"))
        out = os.path.join(md_dir, card["id"].split("/", 1)[1] + ".md")
        with io.open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(card) + "\n")
        n += 1
    print(f"wrote {n} markdown files to {md_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
