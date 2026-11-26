# sandvik25 生产说明（五步）

本包从底本 Sandvik, *The Arkhipov–Bezrukavnikov Equivalence*（BunG Seminar, 2025-01-29，13 页）生产 27 张资料卡（21 概念 + 6 推导），全部只用仓库内工具与原文 PDF，不复制任何既有译文。

## 第 1 步：抽取原文并建立页锚

- 底本无 LaTeX 源码，PDF 文本层可抽取。用 pymupdf 逐页导出：

```python
import fitz
doc = fitz.open("BunG_Seminar_2025-01-29_ArkhipovBezrukavnikov_Equivalence.pdf")
out = []
for i, page in enumerate(doc, 1):
    out.append(f"===== PDF p.{i} =====")
    out.append(page.get_text())
open("工程文件/work/原文/fulltext.txt", "w", encoding="utf-8").write("\n".join(out))
```

- 印刷页 = PDF 页（偏移 0），因为底本没有封面独立编页。13 页、26,992 字符。
- 先按 `grep -n "^[0-9]\. \|^[0-9]\.[0-9]\."` 切出节边界，再逐节读；`anchor` 一律写 `A p.N`。
- 原文 8 条编号公式 (1)–(8)、19 条定理类陈述、14 条脚注，逐条登记进 `工程文件/BRIEF.md` 的对账表。

## 第 2 步：定轨道与 id 清单

- 轨道照原文结构切：`O` 总览（§1）、`A` 中心层与 Wakimoto 层（§2）、`B` Springer 侧与三造函子（§3）、`C` Iwahori–Whittaker 侧（§2.6、§4）、`D` 主等价（§5）。
- **先定 id 清单、再写卡**：`related` 只能引用清单内的 id，否则 `lint_cards.py --strict` 报「related 指向不存在」。
- 最终清单：概念 21 张（O2/A6/B5/C6/D2）、推导 6 张（A1/B2/C2/D1）。

## 第 3 步：用生成器写卡

- 不手写 JSON：`workflow/gen_cards.py` 提供 `card(kind, slug, **kw)`、`src(pages, anchor, section)`、`write_cards(cards)`；每个轨道一个 `cards_*.py`，导入后只定义 dict，末尾 `if __name__ == "__main__": CARDS.update(X); write_cards(X)`。
- 好处：LaTeX 反斜杠不用二次转义，字段拼写由共用函数保证一致，重跑幂等。
- 写卡时逐条核对 `SCHEMA.md` 的硬约束；`summary` ≤120 汉字是最常踩的一条（公式会被剥掉，但汉字数按剥后算）。
- `theorems[].proof.status` 取 `gap` 的，`gap_note` 必须写清「原文哪句话表明省略」，例如 §3.4 的原话 "can be checked rather explicitly, and is omitted"。

## 第 4 步：三道校验

```bash
cd datasets/sandvik25
python tools/lint_cards.py cards --strict   # 期望末行 cards=27 ... errors=0 + OK: 0 error
python tools/build_index.py                 # 重建 index.jsonl（27 行）
python tools/render_md.py                   # 重建 md/（index.md + 27 篇）
```

- `--strict` 会检查 `related` 可解析；开发期用 `--allow-missing` 先过字段关，收尾必须跑 `--strict`。
- 改了卡就重跑生成器再跑三道校验，**不要手改 `cards/*.json`**（下次重跑会被覆盖）。

## 第 5 步：登记与对账

- `datasets/README.md` 的包表格加一行（包名、内容、卡数、轨道、状态）。
- `RELEASE_REGISTER.csv` 加 SY02-40 一行；`03_translations_meta/SY02-40/投稿信息.md` 写底本与权利说明。
- 中译本与本包同批：`08_source_code/SY02-40_Arkhipov–Bezrukavnikov等价（Sandvik BunG讲义）/`，成品 21 页，`资料卡/00-速览.md` 指向本包。
- 最后 `python 04_playbook/tools/make_stats.py --write` 刷新统计。

## 已知空白（本包不掩盖）

底本本身是讨论班讲稿的 expository notes，多处只给引用不给证明；本包用 `proof.status = "gap"` 与 `gaps[]` 如实标出，集中在 `MAP.md` 末尾的表里。若后续要补，优先补 §3.4 的下降（全文最大省略）与 §4.5 的拟极小情形。
