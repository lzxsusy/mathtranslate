# sy0530 · 《模空间的几何与量子化》资料卡

SY05-30 的资料卡集。底本：Springer/Birkhäuser，*Geometry and Quantization of Moduli Spaces*，Advanced Courses in Mathematics – CRM Barcelona，2016（ISBN 978-3-319-33577-3，DOI 10.1007/978-3-319-33578-0）。

本卷只译**前言 + 第 2 章**（Schaffhauser，《克莱因曲面及其基本群讲义》，印刷页 67–108），所以卡片也只覆盖第 2 章；其余三章的任务书在工程目录 `工程文件/work/notes/`。

## 卡片清单

| slug | 题目 | 对应译稿 |
| --- | --- | --- |
| `real-riemann-surface` | Real 黎曼面与实结构 | ch02a.tex |
| `klein-surface-dianalytic` | 克莱因曲面与双解析结构 | ch02b.tex |
| `analytic-double` | 解析 double 与范畴等价 | ch02c.tex |
| `real-curve-topological-type` | 实曲线的拓扑型与 (g,k,a) | ch02b.tex |
| `real-fundamental-group` | 实曲线的基本群 π^R_1 | ch02e.tex |
| `semidirect-splitting` | 半直积分解与正合列的分裂 | ch02f.tex |
| `gamma-model` | 非实点基点的 Γ 模型 | ch02g.tex |
| `galois-real-covers` | 实覆盖的 Galois 理论 | ch02h.tex |
| `unitary-representation-variety` | 酉表示簇与实结构 κ | ch02i.tex / ch02j.tex |
| `sy0530/work` | 书目卡（四章总览） | foreword.tex |

## 口径

- 页码：`pages` 用**印刷页码**，`pdf_pages` 用**底本 PDF 页码**。第 2 章印刷页 = PDF 页 − 10。
- `anchor`：写着译稿 `源码/chapters/` 下的文件名与行号区间，可直接跳到译文。
- 可信度：本集全部 `status: reviewed` + `verification.status: source-verified`，因为每张卡的陈述都对照底本页面图像核过；**但不等于同行评审**——`verification.checks` 只说明「回原书核过」，不说明「数学上无争议」。
- `proof.status` 取 `full`（原书给全证明）/ `sketched`（原书给主线）/ `cited`（原书引文献）/ `absent`（原书未证）。

## 怎么用

- 要「这概念讲了什么」→ 读 `cards/concepts/<slug>.json` 的 `summary` + `definition` + `key_points`。
- 要「证明怎么走的」→ 读 `theorems[].proof.steps`，每步带 `why`。
- 要「容易错在哪」→ 读 `pitfalls`；要「背景直觉」→ 读 `annotations`。
- 要回原文 → `sources[].pages` / `pdf_pages`，或 `工程文件/work/en/ch02.txt` 对应页标记。

## 生成与校验

```bash
python tools/make_cards.py     # 写 cards/
python tools/gen_index.py      # 写 index.jsonl / verification.jsonl
```

`tools/check_cards.py` 校验字段完整性与 anchor 是否落在译稿行号范围之内。
