# Witten 2015 资料卡（gtgl15）

**一句话定位**：这是 Witten《More On Gauge Theory And Geometric Langlands》（arXiv:1506.04293v3，79 页 A4，未正式出版的预印本／讲义）的中文资料卡。它是 KW06 的续篇：不用 $S$-对偶，而用 Hitchin 系统的几何直接证明 §4 中那些膜是磁本征膜，并在 §7 计算 't Hooft 算符的赫克本征值。本包把这条主线拆成可检索、可自测、可打印的 40 张卡（30 概念 + 10 推导）。

## 一张卡只回答一个问题

- **概念卡**三问：这是什么？为什么需要它？哪里容易讲错？
- **推导卡**两问：这条推导怎么走通？每一步凭什么（原文写了什么，哪里是我们补的）？

## 底本与规模

- **A** = Witten, *More On Gauge Theory And Geometric Langlands*, arXiv:1506.04293v3，印刷页 1–78（PDF 页 = 印刷页 + 1；引用一律写**印刷页**）。来源分级 A 即指该底本本身。
- **B** = Kapustin–Witten 2006（arXiv:hep-th/0604151），只作交叉参考，不替代原文页码。
- **C** = Hitchin 1987 等原始文献；**D** = nLab / Stacks Project / EMS 白名单。B/C/D 在本包用得很少，`sources[].text` 用对应字母标注。
- 规模：**40 张 = 30 概念卡 + 10 推导卡**，全部 `status: "dev"`。
- 权利：全部 `rights: "rewritten"`——中文重写；公式可照录；英文短引 ≤120 字符；不收录原文段落。

## 30 秒入口

| 想看什么 | 打开 |
| --- | --- |
| 全包骨架与三条阅读路径 | `MAP.md` |
| 按轨道浏览全部卡 | `md/index.md` |
| 机器可读轻量索引 | `index.jsonl` |
| 概念卡样例 | `cards/concepts/hitchin-moduli.json`、`eigenbranes.json`、`magnetic-eigenbranes.json` |
| 推导卡样例 | `cards/derivations/compactify-to-sigma.json`、`magnetic-hecke-eigenvalue.json` |
| 字段规范 | `SCHEMA.md` |
| 生产流程 | `workflow/PRODUCTION.md` |

## 六条轨道

| 轨道 | 主题 | 概念卡 | 推导卡 |
| --- | --- | --- | --- |
| A | Hitchin 几何与谱曲线 | 12 | 5 |
| B | 对偶环面与 T-对偶 | 3 | 1 |
| C | 膜、线算符与本征膜 | 9 | 1 |
| D | 't Hooft 算符与赫克修正 | 2 | 1 |
| E | 行列式线丛与本征值 | 3 | 1 |
| O | 总览 | 1 | 1 |

## 这张卡是怎么做出来的（四步）

1. **定位原文页**：先用 `pdftotext` 抽取的 `EN_part1..4.txt`（页锚 `[[PDF p.N | printed p.M]]`，印刷页 = PDF 页 − 1）实测公式号→印刷页；关键公式再用 `pdftoppm` 页图核对。
2. **定 id 清单**：按六轨列出 30 概念 + 10 推导的 id，先保证 `related` 只引用包内 id，再写卡（本包 `related` 全部可解析）。
3. **写卡**：一卡一 JSON，用 Python dict + `json.dumps(..., ensure_ascii=False, indent=2)` 生成（避免手写转义错误）；术语与中文初译本（`源码/part1_zh.tex`–`part4_zh.tex`）一致，句子自己重写。
4. **质检**：lint → build_index → render_md；`--strict` 必须 0 error。

## 质检

```bash
cd datasets/gtgl15
python tools/lint_cards.py cards --strict      # 必须 0 error
python tools/build_index.py                    # 生成 index.jsonl
python tools/render_md.py                      # 生成 md/
```

本包实际输出：

```text
cards=40 ids=40 dup=0 tracks={'A': 17, 'C': 10, 'E': 4, 'B': 4, 'D': 3, 'O': 2} errors=0
OK: 0 error
wrote .../datasets/gtgl15/index.jsonl (40 cards: concept=30 derivation=10)
rendered 40 cards -> .../datasets/gtgl15/md
```

## 已知限制

- 全部 `status: "dev"`：未经人类逐张认证；每张卡的 `provenance_note` 标了 A/B/C 的构成与**最没把握处**。
- 抽样非全量：30+10 张覆盖 §1–§7 主线，不是每节每式一卡；`cameral cover`、`Pfaffian/theta` 在原文没有出现这两个术语（已全文检索确认），相关卡按背景补全并标 C 级。
- 中文表述为译者重写：术语与初译本一致，但句式不照抄译本源码。
- 页码来自页锚实测；个别 `anchor` 是区间级估计（如 `A p.8`），无法逐式核对的地方已在 `provenance_note` 说明。
- 原文只处理 minuscule 权、非分歧点、正则半单等假设情形；超出这些假设的部分在卡里标为 `gap` 或 `sketch`，不是被省略。
