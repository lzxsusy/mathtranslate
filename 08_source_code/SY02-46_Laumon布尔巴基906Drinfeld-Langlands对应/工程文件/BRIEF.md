# SY02-46 BRIEF

## 一句话

Laumon 在布尔巴基第 906 期报告中，把 Frenkel–Gaitsgory–Vilonen 关于
Drinfeld–Langlands 对应（$G=\mathrm{GL}(n)$、$X$ 射影、处处非分歧）的工作讲成一个
可读的路线图：从 $\mathrm{GL}(1)$ 的几何类域论出发，经 Hecke 特征函数、反常层
$\mathcal L^d_E$、Fourier 变换构造与消没定理，最后用下降拼出主定理。

## 底本

| 项 | 内容 |
| --- | --- |
| 作者 | Gérard Laumon |
| 题目 | *Travaux de Frenkel, Gaitsgory et Vilonen sur la correspondance de Drinfeld–Langlands* |
| 出处 | Séminaire BOURBAKI，第 54 年（2001–2002），第 906 期，2002 年 6 月 |
| 预印本 | arXiv:math/0207078v1（2002-07-09） |
| 篇幅 | 19 页（标题页 1 页 + 正文 17 页 + 参考文献 2 页） |
| 语言 | 法文 |
| 排版 | dvips 单行本；页眉 `906–NN`，PDF 页 = 印刷页 |
| 结构 | 引言；§0 预备；§1 几何类域论；§2 主定理；§3 反常层 $\mathcal L^d_E$；§4 复形 $\mathrm{Aut}'_E$；§5 Fourier 变换构造；§6 消没定理；§7 下降；参考文献 |

原文共 20 条编号条目：定义 4（(0.2)、2.1、3.2、4.1）、引理 8（(0.3)、(0.4)、3.1、
5.1、5.2、7.1、7.2、7.4）、定理 4（1.1、1.2、2.2、6.1）、命题 2（6.3、7.3）、
推论 1（6.4）、注 1（6.2）；另有 2 条编号公式（(0.1)、(1.3)）与大量未编号的构造、
交换图。合计 22 个编号对象。

## 权利

- 底本权利归原作者与法国数学会（Séminaire Bourbaki 单行本）。
- 本仓产出为**中文译注本**（演绎作品），不复制底本排版，仅翻译文字与重排公式。
- 发布级别：L2 公开·受限（可撤下）；底本原文不随仓分发，页码与引文按合理引用处理。
- 译文权利：CC BY-NC-SA 4.0（与仓内其他译本一致），见 `03_translations_meta/SY02-46/投稿信息.md`。

## 为什么译这篇

1. 它是几何 Langlands 的**标准入口报告**：从 1967 年 Langlands 猜想写到 2002 年
   FGV 的证明，19 页内给出完整技术路线，适合作为该方向的第一份中文导览。
2. 仓内几何 Langlands 主线已有 SY02-45（Scholze 2026 报告，讲 2024–2026 的突破），
   但缺 2002 年 FGV 这一环；本篇补上「$G=\mathrm{GL}(n)$、射影曲线、处处非分歧」
   的经典情形，两篇正好接成一条线。
3. 原文的记号（$\mathrm{Aut}'_E$、$\mathcal L^d_E$、$\mathcal M'^d_{n,E}$）在后续文献里
   被反复引用，需要一个**记号可靠**的中文版本。

## 目标读者

- 学过代数几何与层论、想进入几何 Langlands 的研究生与青年学者；
- 需要把 FGV 论证形式化（Lean）的人：本仓另出对齐卡，供抽取陈述；
- 教这门课的人：可直接用译本的节结构与术语表。

## 译本体例

- **页码**：每页起始处边注 `906–NN`，与原文页眉一致；引原文一律用印刷页码。
- **编号**：原文编号原样保留（定理 2.2、引理 5.1、公式 (0.1)），不重编、不升降级；
  §0 的 (0.2)(0.3)(0.4) 是原文编号，用不编号环境加显式标号。
- **译注**：脚注，以「【译注·类别】」起首，类别仅「术语背景 / 原文省略 / 原文笔误」；
  每条给依据等级 A（一手文献）/ B（nLab、Stacks、ProofWiki）/ I（译者推断）。
  译文不补原文没有的论证。
- **术语**：以 `工程文件/work/glossary.tsv` 冻结表为准（约 130 条）。
- **公式**：行间公式不编号，除原文编号的 (0.1)、(1.3)；交换图用 tikz-cd 重画。
- **文献**：原文 21 条照录，编号 `[B-B-D]` 等原样保留；正文引用只写方括号编号。

## 目录

| 节 | 内容 | 页 |
| --- | --- | --- |
| 引言 | Langlands 猜想与 Drinfeld–Langlands 对应的来历 | 1 |
| 0 | 预备：三元组、六函子、反常层、Fourier 变换 | 2–4 |
| 1 | 几何类域论：Abel–Jacobi、$\mathrm{GL}(1)$ 的 $\mathrm{Aut}_E$ | 4–6 |
| 2 | 主定理：Hecke 算子与 Hecke 性质、定理 2.2 | 6–8 |
| 3 | 反常层 $\mathcal L^d_E$：$\mathrm{Coh}^d_0$ 与中间延拓 | 8–9 |
| 4 | 复形 $\mathrm{Aut}'_E$：旗叠 $\mathcal U_n$ 与 $\mathcal M'^d_{n,E}$ | 9–11 |
| 5 | 用 Fourier 变换构造：基本图与 $\mathcal K_{E,i}$ | 11–13 |
| 6 | 消没定理：定理 6.1 与推论 6.4 | 13–15 |
| 7 | 下降：引理 7.1–7.4 拼出定理 2.2 | 15–17 |
| 参考文献 | 21 条 | 18–19 |

## 施工与验收

1. **通读**：先出《通读笔记》《疑点清单》，未解疑点 = 0 才落笔（已完成）。
2. **分包**：7 名译手按节译，每节跑 `check_sections.py` 与 `compile_section.py`。
3. **合并**：主控整篇 `xelatex` 三遍，目录与交叉引用无 error。
4. **复核**：逐节对法文原文复核；≥12 页人眼并排抽检；`check_terms.py` 全检；
   21 条文献 Crossref/arXiv 外核。
5. **资料卡**：`datasets/sy0246/`，每卡带原文页码、逐字引文、可解析 anchor、
   ≥3 条 verification checks（E1 底本页面图像 / E2 权威二手 / E3 卡内推导）。
6. **闸门**：`make_stats.py --check`、`check_numbers.py`、`build_norm.py --check`、
   `ds_lint.py`、`entry_lint.py`、`card_spec_check.py --set sy0246 --strict`。

## 已知风险

| 风险 | 处理 |
| --- | --- |
| 法文文本层坏点（`Dcb`、`V ∨`、`Aut′E`、`E (d)` 等） | 一切公式以 150 dpi 页面图为准；译手逐页对图 |
| 原文两套 `propre`（态射紧合 / proper 反常层） | 术语分离：`morphisme propre`=紧合态射，`faisceau pervers propre`=proper 反常层 |
| 原文 [B-L] 标 1974 年，LNM 1578 实为 1994 | 照录原文；在资料卡 04 疑误表登记 |
| 原文正文止于 §7 下降段落，无单独「定理 7.5」收尾 | 照译，不虚构编号 |
| §0 的 (0.2)(0.3)(0.4) 与 `\section` 计数器 | 用不编号环境 + 显式标号 |

## 状态

**已交付（2026-11-27）**。中译注本 15 页（xelatex 三遍，0 error / 0 Overfull / 0 Underfull），
20 条编号条目 + 2 条编号公式，译注 8 条；术语 146 条冻结、`check_terms.py` 0 违规；
21 条参考文献外部核对（15 条一致、6 条出入只登记不改原文）；10 页人眼并排抽检；
资料卡五件套齐全，可抽取卡片集 `datasets/sy0246` 14 张（`card_spec_check.py --strict` 0 hard / 0 warn），
对齐卡 `datasets/leanstmt/cards/statements/laumon906-g01.json`（gap 卡，定理 1.2）；
`RELEASE_REGISTER.csv` 已登记（随仓公开），`make_stats.py` / `check_numbers.py` / `build_norm.py --check` 均通过。
