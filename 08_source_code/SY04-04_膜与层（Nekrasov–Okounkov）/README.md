# SY04-04 《膜与层》（Membranes and Sheaves）中文译注本 · 校订版

N. A. Nekrasov、A. M. Okounkov *Membranes and Sheaves*（arXiv:1404.2323v1，2014，77 页正文）的整本中译，
2026-11-24 按 `04_playbook/07_整书对照校订流水线.md` 做了一轮**全文对照校订**：20 处文字改动、3 类编译修复，
资料卡五件套齐备。

## 底本

| 项 | 内容 |
|---|---|
| 原文题名 | *Membranes and Sheaves* |
| 作者 | Nikita A. Nekrasov、Andrei M. Okounkov |
| 出处 | arXiv:1404.2323v1（2014-04-09 提交），77 页正文，9 节，39 条参考文献 |
| 底本类型 | arXiv 预印本（未出版）：**原文不入仓**，按 `COMPLIANCE.md` 记 `原文级别=L4 禁入` |
| 中译 | 65 页（2026-11-24 重编译），`源码/MDT_zh.tex` 单文件 + `源码/figures/` 5 图 |

- 正文结构：1 简要导论 → 2 猜想的轮廓（含 11 维超引力与零次数 DT 计数）→ 3 DT 被积函数 → 4 膜的指标
  → 5 例子（约化局部曲线、双重曲线、光滑曲线单次相互作用、高秩 DT）→ 6 平方根的存在性 → 7 精化不变量
  → 8 指标顶点与精化顶点 → 9 附录（平衡引理）。
- 页映射：**原文 pN / 译本 pM**，节级对照见 `工程文件/BRIEF.md` 的「结构页表」。

## 规模与验收

| 项 | 数 |
| --- | ---: |
| 译本页数 | 65 |
| `\label` / `\ref` / `\eqref` | 129 / 71 / 95（与底本逐项相等） |
| 编号陈述 | 21（猜想 2、定义 1、命题 9、引理 7、定理 2） |
| 参考文献 | 39 条，键集与底本完全一致 |
| 校订 | 20 处文字（未译残片 4、译反 2、错译/术语 13、习语 1） |
| 编译 | `xelatex` 两遍：0 error、0 未定义引用、0 缺字；2 处不可见 Overfull、4 处 Underfull |

## 结构

```
源码/            MDT_zh.tex（单文件工程）、figures/（5 张图）、build.ps1
工程文件/        BRIEF.md、STYLE_GUIDE.md、00_开工必读.md、校对报告.md、work/glossary.tsv
资料卡/          00-速览、01-结果清单、02-论证地图、03-条款索引、04-术语文献勘误
```

## 编译

```powershell
cd 源码
powershell -NoProfile -ExecutionPolicy Bypass -File build.ps1
```

或在 `源码/` 下直接 `xelatex MDT_zh.tex` 连跑两遍（xelatex，MiKTeX/TeX Live 均可）。产物 `MDT_zh.pdf`，65 页。

## 这次校订改了什么

三类**编译 bug**（原 PDF 与源码对不上，源码在当前 LaTeX2e 下根本编不过）：

1. 158 处数学上下标后直接跟文本字体宏（`ds_\textup{TN}^2` 一类）→ `! Missing { inserted`，统一加花括号；
2. 第 526–533 行交换图 `tikzcd` 箭头指向空网格 → `No shape named tikz@f@1-3-2`，改回三行网格；
3. `\bPhi` 定义成 `\mathbf{\Phi}`，TU 编码下无希腊大写字形 → 6 条 `Missing character ^^H`，改 `\boldsymbol{\Phi}`。

**20 处译文改动**与理由逐条见 `工程文件/校对报告.md`，术语层面的归档见 `资料卡/04-术语文献勘误.md`。

## 为什么归在 SY04（弦论）

标题就是「膜」：M-理论（11 维超引力、M2/M5-膜）与 CY 三重流形上的层／DT 不变量之间的猜想与证据。
与 SY04-01《弦紧致化的几何工具》同属「弦论要用的几何」，与 `datasets/gw06` 一类 GW/DT 计数材料互为参照；
按 `17_仓库理念与上传规范.md` §6，弦论侧归 SY04，故取 **SY04-04**。

## 权利与撤下

- 底本为 arXiv 预印本，译文是演绎作品，权利归原作者；本库不代原作者授权，也不另设限制（检索、研究、教学、训练均可），权利人要求即撤。
- 自产部分（资料卡、校对报告、术语表、BRIEF/STYLE_GUIDE、脚本）为 CC BY 4.0。
- 依 R3，预印本类**成品 PDF 不入 git**，台账记 `成品级别=成品不公开`（本地交付）。若日后要公开，上传 AtomGit Release 后改为 `Release 外链` 并回填直链。
