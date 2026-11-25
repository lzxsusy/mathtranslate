# 交付总览（README）

《Grassmannians, Moduli Spaces and Vector Bundles》中译本（170 页、9 篇论文）精读与审校成果。

## 一句话

9 章导读 + 159 条批注 + 58 条 errata + 9 章笔记 + 90 张资料卡（概念 73 / 例子 17），全部经 `tools\check_chapter.py`（0 FAIL）与 `_cards_grassmann\tools\validate_cards.py --strict`（0 error）。

## 章级成果

| 章 | 篇名 | 中译页 | 已有译注 | 导读(字) | 批注 | errata | 笔记(字) | 卡片候选 | 状态 |
|---|---|---|---|---|---|---|---|---|---|
| ch1 | Hitchin 的射影平坦联络、Toeplitz 算子与 TQFT 曲线算子的渐近展开 | 7–29 | 8 | 1492 | 16 | 10 | 1773 | 10 | partial |
| ch2 | Koszul 上同调及其在模空间中的应用 | 30–54 | 14 | 1676 | 16 | 5 | 2100 | 15 | partial |
| ch3 | Reider 定理与 Thaddeus 对再探 | 55–71 | 5 | 1412 | 18 | 6 | 1735 | 9 | partial |
| ch4 | 丛的奇异模空间中的相交配对 | 72–81 | 3 | 1957 | 19 | 7 | 2662 | 7 | partial |
| ch5 | Beilinson–Drinfeld 格拉斯曼流形与辛纽结同调 | 82–93 | 7 | 2124 | 18 | 10 | 2934 | 10 | partial |
| ch6 | 曲线上层的模空间的算术方面 | 94–115 | 13 | 1691 | 18 | 8 | 1817 | 10 | partial |
| ch7 | 代数曲线上 α-稳定凝聚系的存在性 | 116–134 | 6 | 1996 | 18 | 3 | 2029 | 10 | partial |
| ch8 | 阿贝尔簇上的正则性 III：与一般消没的关系及应用 | 135–159 | 18 | 1609 | 19 | 5 | 2066 | 11 | partial |
| ch9 | 可约曲线上的向量丛及应用 | 160–170 | 7 | 1712 | 17 | 4 | 2305 | 7 | partial |
| 合计 | — | 7–170 | 81 | 15669 | 159 | 58 | 19421 | 89 | — |

## 怎么读

1. 先读 `产出\导读\00-全书导读.md`：九篇如何成为一本书、三条阅读路线。
2. 再按章读 `产出\导读\chNN-导读.md`（这一章干什么 / 读前须知 / 怎么读 / 核心结果 / 术语）。
3. 精读时对照 `产出\批注\chNN-批注.md`（位置 + 原文摘录 + 批注 + 类型）与 `产出\批注\chNN-errata.tsv`。
4. 想自己做题/补证明，看 `产出\笔记\chNN-笔记.md`（主线 / 关键构造 / 补全 / 疑问 / 延伸）。
5. 查概念用 `_cards_grassmann\md\INDEX.md`（或 `cards\` 下 JSON），按轨道 A/1–9 检索。

## 目录

| 路径 | 内容 |
|---|---|
| `产出\导读\` | 00-全书导读 + 9 章导读 |
| `产出\批注\` | 9 章批注、9 份 errata、00-审校总表.tsv、00-修订补丁.md |
| `产出\笔记\` | 9 章读书笔记 |
| `产出\汇总\` | 本文件、审校方法、交叉引用、术语增补、9 份章报告与卡片候选 |
| `_cards_grassmann\` | 资料卡库（SCHEMA、taxonomy、cards、索引） |
| `tools\` | preflight / 抽取译注 / 页码工具 / 逐章验收 / errata 合并 / 卡片计划 |

## 统计

| 项 | 数 |
|---|---|
| 精读页数（中译正文） | 164（p.7–170；前言 6 页另计） |
| 导读汉字 | 15669 |
| 批注条数 | 159 |
| errata 条数 | 58（formula 5、numbering 2、original-error 22、term 11、translation-error 14、typo 4） |
| 笔记汉字 | 19421 |
| 资料卡 | 90（概念 73 / 例子 17） |
| 已有译注复核 | 81 条，0 条改判 |

## 未完成 / partial

以下各章主体完成，但有个别推导/文献缺口，已在各章 report 的「存疑」里写明：

- **ch1**：见 `产出\汇总\ch01-report.md` 的「存疑」小节。
- **ch2**：见 `产出\汇总\ch02-report.md` 的「存疑」小节。
- **ch3**：见 `产出\汇总\ch03-report.md` 的「存疑」小节。
- **ch4**：见 `产出\汇总\ch04-report.md` 的「存疑」小节。
- **ch5**：见 `产出\汇总\ch05-report.md` 的「存疑」小节。
- **ch6**：见 `产出\汇总\ch06-report.md` 的「存疑」小节。
- **ch7**：见 `产出\汇总\ch07-report.md` 的「存疑」小节。
- **ch8**：见 `产出\汇总\ch08-report.md` 的「存疑」小节。
- **ch9**：见 `产出\汇总\ch09-report.md` 的「存疑」小节。

## 复现

```
python tools\preflight.py                  # 环境与页表自检
python tools\check_chapter.py --all        # 九章质量门
python tools\merge_errata.py               # 合并 9 份 errata
python _cards_grassmann\tools\validate_cards.py --strict
python _cards_grassmann\tools\build_index.py
python tools\build_summary.py              # 重新生成本文件与修订补丁
```
