# -*- coding: utf-8 -*-
"""把 cards/ 渲染成 index.jsonl 与 md/INDEX.md。

    python tools\\build_index.py
"""
import os
import io
import sys
import json
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
MD = os.path.join(ROOT, "md")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

TRACK_NAME = {
    "A": "A · 基础（跨章）", "1": "1 · Hitchin / TQFT", "2": "2 · Koszul 上同调",
    "3": "3 · Reider / Thaddeus", "4": "4 · 相交上同调", "5": "5 · Beilinson–Drinfeld",
    "6": "6 · 算术方面", "7": "7 · α-稳定凝聚系", "8": "8 · M-正则性", "9": "9 · 可约曲线",
}


def main():
    files = sorted(glob.glob(os.path.join(CARDS, "*", "*.json")))
    cards = []
    for p in files:
        with open(p, encoding="utf-8") as f:
            cards.append(json.load(f))

    def key(c):
        return (str(c.get("track", "Z")), str(c.get("type", "")), c.get("id", ""))

    cards.sort(key=key)

    os.makedirs(MD, exist_ok=True)
    with open(os.path.join(ROOT, "index.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for c in cards:
            row = {
                "id": c.get("id"), "type": c.get("type"), "title": c.get("title"),
                "track": c.get("track"), "summary": c.get("summary"),
                "status": c.get("status"), "source": (c.get("sources") or [{}])[0],
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    lines = ["# 格拉斯曼资料卡索引", "",
             "共 %d 张：概念 %d、例子 %d。由 `tools/build_index.py` 生成，别手改。" % (
                 len(cards), sum(1 for c in cards if c.get("type") == "concept"),
                 sum(1 for c in cards if c.get("type") == "example")), ""]
    tracks = []
    for c in cards:
        if c.get("track") not in tracks:
            tracks.append(c.get("track"))
    for t in tracks:
        lines += ["## " + TRACK_NAME.get(t, str(t)), "",
                  "| id | 标题 | 类型 | 状态 | 中译页 |", "|---|---|---|---|---|"]
        for c in [x for x in cards if x.get("track") == t]:
            s = (c.get("sources") or [{}])[0]
            lines.append("| `%s` | %s | %s | %s | %s |" % (
                c.get("id"), c.get("title"), c.get("type"), c.get("status"),
                s.get("pages_zh", "")))
        lines.append("")
    with open(os.path.join(MD, "INDEX.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    print("index.jsonl + md/INDEX.md：%d 张卡（%s）" % (
        len(cards), ", ".join("%s=%d" % (t, sum(1 for c in cards if c.get("track") == t)) for t in tracks)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
