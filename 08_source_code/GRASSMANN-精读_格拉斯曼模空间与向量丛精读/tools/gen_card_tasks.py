# -*- coding: utf-8 -*-
"""由 tmp/cards-plan.tsv 生成 taxonomy.md、tmp/cards-ids.md 与 4 份卡片手任务书。

  python tools/gen_card_tasks.py
"""
import os
import sys
import io
import json
import glob
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(ROOT, "tmp", "cards-plan.tsv")
CARDS = os.path.join(os.path.dirname(ROOT), "_cards_grassmann", "cards")
TAX = os.path.join(os.path.dirname(ROOT), "_cards_grassmann", "taxonomy.md")

PAGES = {"1": "7", "2": "30", "3": "55", "4": "72", "5": "82",
         "6": "94", "7": "116", "8": "135", "9": "160", "A": "跨章"}
GROUP_NAME = {"甲": "甲组（A + ch1 + ch3）", "乙": "乙组（ch2 + ch7）",
              "丙": "丙组（ch5 + ch8）", "丁": "丁组（ch4 + ch6 + ch9）"}

TRACK_TABLE = """| track | 名称 | 覆盖 | 配额（概念） | 配额（例子） |
|---|---|---|---|---|
| A | 基础（跨章） | 模空间、稳定性、上同调、除子、线丛、Brill–Noether | 8–10 | 2 |
| 1 | Hitchin / TQFT | Hitchin 联络、Toeplitz、形变量子化、曲线算子 | 8 | 2 |
| 2 | Koszul 上同调 | K_{p,q}、合冲、闭链、四个猜想 | 12 | 3 |
| 3 | Reider / Thaddeus | Reider 定理、Thaddeus 对、稳定性 | 7 | 2 |
| 4 | 相交上同调 | 部分消奇异、ICT、等变上同调 | 6 | 1 |
| 5 | Beilinson–Drinfeld | 仿射/整体/卷积格拉斯曼、切片、纽结同调 | 8 | 2 |
| 6 | 算术方面 | Gerbe、扭曲层、Brauer 群、周期-指标、抛物丛 | 8 | 2 |
| 7 | α-稳定凝聚系 | 凝聚系、α-斜率、存在性、边界情形 | 8 | 2 |
| 8 | M-正则性 | GV-层、M-正则、Ishida、Fourier–Mukai | 9 | 2 |
| 9 | 可约曲线 | 斜率稳定、Hilbert 紧化、极限线性系 | 6 | 1 |

合计目标：概念 60–75，例子 15–20。"""

COMMON = """# 通用要求（每张卡都必须满足，`validate_cards.py` 会逐条查）

1. **只写你自己的卡**：`_cards_grassmann\\cards\\concepts\\<slug>.json` 或 `examples\\<slug>.json`，
   文件名必须等于 id 最后一段；除此之外只写 `产出\\汇总\\card<组>-report.md`。
   不许改别人的卡、不许改 SCHEMA/taxonomy/源文件/BRIEF/STATUS。
2. **以中译为准**：中文数学与公式一律照 `Grassmannians-精读\\source\\chapters\\chNN.tex`；
   PDF 文字层公式是碎的，只用来定位版面与页码。卡片里的 LaTeX 必须能在中译正文里找到对应说法。
3. 字段硬要求：
   - `id` = `grassmann/concept/<slug>` 或 `grassmann/example/<slug>`；`type` 与 id 一致；
     `title` 中文术语；`aliases` 数组（英文术语、常见别名）；
   - `track` 用任务书表格里给的，**不要自己改**；
   - `summary` **20–120 个汉字**（只数 CJK；英文术语不算），一句话说清「是什么 + 为什么重要」；
   - `question` 一个真会卡住读者的问题，**必须以「？」结尾**；
   - `definition.text` 用中译措辞 + 公式（`$...$`），`definition.notation` 写记号约定（别留空，空只是 warn 但要求写）；
   - `key_points` ≥3 条，每条一句、具体、不写套话；
   - `formulas` ≥1 条，每条 `$` 必须成对；
   - `theorems` ≥1 条：`{name, statement, source, proof}`。
     `proof.status` 三选一：`complete`（本章有证明，steps ≥2，每步 `{text, why}`，why 说清为什么这步成立）、
     `sketch`（有思路但缺一步，**必须**写 `gap_note` 说清缺哪一步、为什么补不出来）、
     `reference`（本章只引文献，`steps` 可空、`gap_note` 空）；
   - `pitfalls` ≥1 条：**真坑**（从该章批注/笔记里挑），写成「容易把 X 当成 Y，因为…」；
   - `related` ≥2 条，必须是 `tmp\\cards-ids.md` 里真实存在的 id（不许编），其中至少 1 条跨组；
   - `sources` ≥1 条：`book` 固定写 `Grassmannians, Moduli Spaces and Vector Bundles (Clay 14)`，
     `section` 写章内位置（如 `ch3 §4 定理 4.1`），`pages_zh`/`pages_en` 写页码，
     `anchor` 必须是 `chapters/chNN.tex:行号` 且**指向非空行、内容与卡片对应**（在候选行 ±20 行内校正）；
   - `rights` = `"rewritten"`，`status` = `"draft"`；
   - 全文不得出现本机绝对路径（`C:\\...`）、不得含 tab；JSON 里反斜杠写两个（`\\\\subseteq`→`\\subseteq`）。
     建议用 Python `json.dump(obj, f, ensure_ascii=False, indent=2)` 落盘，避免手写转义出错。
4. **页码怎么拿到**：该卡 anchor 附近的内容在 `产出\\批注\\chNN-批注.md` 里通常已有同一条，
   位置行写着「中译 p.X / 原书 p.Y / en PDF p.Z」，直接抄；找不到就按 `tools\\pdf_pages.py` 自己核。
5. **例子卡额外字段**：`concept_refs` ≥2 条（必须是概念卡 id）、`setup`（场景/数据/记号）、
   `computation`（把数算出来，带中间步骤与结果）。
6. **校验**：改完一批就跑
   `cd C:\\Users\\admin\\Downloads\\_cards_grassmann && python tools\\validate_cards.py`
   只看自己文件名的 ERROR/WARN 并修掉；别的组的报错不要动。
   （不要用 `--strict`：taxonomy 要等 Lead 最后收口。）
7. **report**：`产出\\汇总\\card<组>-report.md`，含：写了多少概念/例子、每张卡的一句话摘要、
   哪些 card 的 proof 只能 sketch 及原因、id/related 上遇到的冲突、3–5 条「存疑」。
"""


def load_plan():
    rows = []
    with open(PLAN, encoding="utf-8") as f:
        next(f)
        for ln in f:
            p = ln.rstrip("\n").split("\t")
            if len(p) >= 8:
                rows.append(dict(zip(
                    ["id", "type", "title_zh", "title_en", "track", "group", "chapter", "anchor"], p)))
    return rows


def seeds():
    out = []
    for p in sorted(glob.glob(os.path.join(CARDS, "*", "*.json"))):
        with open(p, encoding="utf-8") as f:
            c = json.load(f)
        out.append(c)
    return out


def write_taxonomy(rows, seed_cards):
    lines = ["# 卡片清单与轨道（taxonomy）", "",
             "> 本文件是 `validate_cards.py --strict` 的对照表：**用反引号写出的 id 必须真的有文件**。",
             "> Phase 3 由 Lead 汇总 `产出\\汇总\\cards-chNN.tsv` 后填表；卡手按此表施工。", "",
             "## 轨道", "", TRACK_TABLE, "",
             "## 命名", "",
             "- 概念卡：`grassmann/concept/<kebab-case-英文术语>`，如 `m-regular-sheaf`、`koszul-cohomology`。",
             "- 例子卡：`grassmann/example/<内容>`，如 `sl2-two-point-collision`。",
             "- 同一概念只许一张卡；近义术语进 `aliases`。跨章出现的同一对象归 `A` 轨道一张卡，`sources` 列多条。",
             "", "## 卡片清单", "",
             "<!-- 格式：| id | 标题 | 轨道 | 中译页 | 卡手 | -->", "",
             "| id | 标题 | 轨道 | 中译页 | 卡手 |", "|---|---|---|---|---|"]
    for c in seed_cards:
        lines.append("| `%s` | %s | %s | %s | 种子（Lead） |" % (
            c["id"], c["title"], c["track"], PAGES.get(c["track"], "—")))
    for r in rows:
        lines.append("| `%s` | %s | %s | %s | %s |" % (
            r["id"], r["title_zh"], r["track"], PAGES.get(r["track"], "—"), r["group"]))
    lines += ["", "合计：概念 %d 张（含 3 张种子）、例子 %d 张。" % (
        sum(1 for r in rows if r["type"] == "concept") + len(seed_cards),
        sum(1 for r in rows if r["type"] == "example")), "",
              "## 去重记录", "",
              "| 被并/被丢弃 | 处理 | 理由 |", "|---|---|---|",
              "| `grassmann/concept/alpha-stability`（ch7 候选） | 不单独建卡 | 与种子卡 `alpha-stable-coherent-system` 同一对象，进其 aliases |",
              "| `grassmann/concept/coherent-system`（ch7 候选） | 不建卡 | 已有种子卡 |",
              "| ch1 `Verlinde bundle`（概念）/ ch8 `Verlinde bundles`（例子） | 分别保留 | 一为构造、一为正则性阈值计算，内容不重复 |", ""]
    with open(TAX, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print("taxonomy.md 写入", len(rows) + len(seed_cards), "张卡片")


def write_ids(rows, seed_cards):
    lines = ["# 全部卡片 id 清单（related 只能用这里出现的 id）", "",
             "| id | 类型 | 标题 | 轨道 | 组 |", "|---|---|---|---|---|"]
    for c in seed_cards:
        lines.append("| `%s` | %s | %s | %s | 种子 |" % (c["id"], c["type"], c["title"], c["track"]))
    for r in rows:
        lines.append("| `%s` | %s | %s | %s | %s |" % (
            r["id"], r["type"], r["title_zh"], r["track"], r["group"]))
    with open(os.path.join(ROOT, "tmp", "cards-ids.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("tmp/cards-ids.md 写入", len(rows) + len(seed_cards), "行")


def write_tasks(rows):
    by = defaultdict(list)
    for r in rows:
        by[r["group"]].append(r)
    for g, items in by.items():
        items.sort(key=lambda r: (r["chapter"], r["id"]))
        t = ["# 卡片手任务书：%s" % GROUP_NAME[g], "",
             "你是这一组的卡片手。本组共 **%d 张卡**（概念 %d、例子 %d）。" % (
                 len(items), sum(1 for r in items if r["type"] == "concept"),
                 sum(1 for r in items if r["type"] == "example")), "",
             "## 开工先读", "",
             "1. `C:\\Users\\admin\\Downloads\\_cards_grassmann\\SCHEMA.md` 全文（字段规范，冲突时以它为准）",
             "2. `C:\\Users\\admin\\Downloads\\_cards_grassmann\\workflow\\PRODUCTION.md`",
             "3. `C:\\Users\\admin\\Downloads\\Grassmannians-精读\\tmp\\cards-ids.md`（全量 id，related 只能从这里取）",
             "4. 你负责各章的 `产出\\导读\\chNN-导读.md`、`产出\\笔记\\chNN-笔记.md`、`产出\\批注\\chNN-批注.md`",
             "5. 已有种子卡 3 张，看一张就知道语气与细致程度："
             "`_cards_grassmann\\cards\\concepts\\coherent-system.json`", "",
             "## 本组清单", "",
             "| # | id | 标题 | 章 | anchor |", "|---|---|---|---|---|"]
        for i, r in enumerate(items, 1):
            t.append("| %d | `%s` | %s | ch%s | `%s` |" % (
                i, r["id"], r["title_zh"], r["chapter"], r["anchor"]))
        t += ["", "每张卡开工时：先在 `source\\chapters\\ch%s.tex` 里定位 anchor 那一行，上下读 60–120 行，" % "{NN}",
              "把定义/定理的措辞抄准；再看该章批注里同一位置的条目（那里有中译/原书/英文 PDF 三个页码与坑）。", "",
              COMMON, "",
              "## 交付", "",
              "- 卡片 JSON 全部落盘且 `validate_cards.py` 里**你负责的文件** 0 error；",
              "- `产出\\汇总\\card%s-report.md` 写好；" % g,
              "- 最后用一段话回报：写了多少张、哪几张 proof 只能 sketch、踩过的坑。", ""]
        p = os.path.join(ROOT, "tmp", "cardtask-%s.md" % g)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(t))
        print("任务书", p, len(items), "张")


def main():
    rows = load_plan()
    sc = seeds()
    write_taxonomy(rows, sc)
    write_ids(rows, sc)
    write_tasks(rows)


if __name__ == "__main__":
    main()
