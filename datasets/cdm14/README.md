# 晶体与 D-模 资料卡（cdm14）

**一句话定位**：这是 Gaitsgory–Rozenblyum《Crystals and D-modules》（arXiv:1111.2087v4，65 页，2014）的中文资料卡。它把「晶体 = de Rham 预栈上的（归纳）凝聚层」这一纲领拆成 35 张可检索、可自测的卡：沿 §1–§7 依次处理 de Rham 预栈、左右晶体与 Kashiwara、下降与归纳函子、两个 $t$-结构、与 D-模的等价、扭化、扭晶体。

## 一张卡只回答一个问题

- **概念卡**三问：这是什么？为什么需要它？哪里容易讲错？
- **推导卡**两问：这条推导怎么走通？每一步凭什么（原文写了什么，哪里是我们补的）？

## 底本与规模

- **A** = Gaitsgory–Rozenblyum, *Crystals and D-modules*, arXiv:1111.2087v4，印刷页 1–65（**印刷页 = PDF 页**，引用一律写印刷页）。来源分级 A 即指该底本本身。
- **B** = 作者其他论文：[GR1] *DG indschemes*（arXiv:1108.1738）、[IndCoh] *Ind-coherent sheaves*（arXiv:1105.4857）、[Lu2] *Higher Algebra*；只作交叉参考，不替代原文页码。
- **C** = 经典原始文献（[Gr] Grothendieck、[BB] Beilinson–Bernstein、[Si] Simpson）；**D** = nLab / Stacks Project 白名单。B/C/D 用得很少，`sources[].text` 用对应字母标注。
- 规模：**35 张 = 27 概念卡 + 8 推导卡**，全部 `status: "dev"`。
- 权利：全部 `rights: "rewritten"`——中文重写；公式可照录；英文短引 ≤120 字符；不收录原文段落。

## 30 秒入口

| 想看什么 | 打开 |
| --- | --- |
| 全包骨架与阅读路径 | `MAP.md` |
| 按轨道浏览全部卡 | `md/index.md` |
| 机器可读轻量索引 | `index.jsonl` |
| 概念卡样例 | `cards/concepts/left-crystal.json`、`right-crystal.json`、`kashiwara.json` |
| 推导卡样例 | `cards/derivations/upsilon-equiv.json`、`kashiwara-equiv.json`、`cdm-equiv.json` |
| 字段规范 | `SCHEMA.md` |
| 生产流程 | `workflow/PRODUCTION.md` |

## 八条轨道

| 轨道 | 主题 | 位置 | 概念卡 | 推导卡 |
| --- | --- | --- | --- | --- |
| A | de Rham 预栈与晶体定义 | §1 | 3 | 1 |
| B | 左/右晶体、$\Upsilon$、Kashiwara | §2 | 4 | 2 |
| C | 下降与归纳函子 | §3 | 4 | 2 |
| D | $t$-结构 | §4 | 7 | 1 |
| E | 与 D-模的关系 | §5 | 3 | 1 |
| F | 扭化 | §6 | 3 | 1 |
| G | 扭晶体 | §7 | 2 | 0 |
| O | 总览 | 引言 | 1 | 0 |

## 这张卡是怎么做出来的（四步）

1. **定位原文页**：底本有文本层，`pdftotext` 抽取后按页切块（`工程文件/work/en_full.txt`，页锚 `===== BOOK PAGE n =====`）；印刷页 = PDF 页，公式号→页用正则统计。关键公式再用 `pdftoppm` 页图核对。
2. **定 id 清单**：按八轨列出 27 概念 + 8 推导的 id，先保证 `related` 只引用包内 id，再写卡。
3. **写卡**：一卡一 JSON，用 Python dict + `json.dumps(..., ensure_ascii=False, indent=2)` 生成（避免手写转义错误）；术语与中文译注本（`08_source_code/SY02-12_.../源码/`）一致，句子自己重写。
4. **质检**：lint → build_index → render_md；`--strict` 必须 0 error。

## 质检

```bash
cd datasets/cdm14
python tools/lint_cards.py cards --strict      # 必须 0 error
python tools/build_index.py                    # 生成 index.jsonl
python tools/render_md.py                      # 生成 md/
```

本包实际输出：

```text
cards=35 ids=35 dup=0 tracks={'A': 4, 'B': 6, 'C': 6, 'D': 8, 'E': 4, 'F': 4, 'G': 2, 'O': 1} errors=0
OK: 0 error
wrote .../datasets/cdm14/index.jsonl (35 cards: concept=27 derivation=8)
rendered 35 cards -> .../datasets/cdm14/md
```

## 已知限制

- 全部 `status: "dev"`：未经人类逐张认证；每张卡的 `provenance_note` 标了 A/B/C 的构成与**最没把握处**。
- 抽样非全量：35 张覆盖 §1–§7 的定理链，不是每节每式一卡；命题 5.2.4 的八个核、§6.6 的中心扩张等细节只并入相邻卡，未单独成卡。
- 中文表述为译者重写：术语与译注本一致，但句式不照抄译文。
- 页码来自页锚实测；个别 `anchor` 是区间级估计，无法逐式核对的地方已在 `provenance_note` 说明。
- 原文大量引用 [GR1]/[IndCoh]/[Lu2]，本包只按原文引用关系标注，未替读者补证；标 `sketch` 的证明即原文只给轮廓的地方。
