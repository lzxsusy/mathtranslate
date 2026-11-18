# BRIEF · SY01-25《同调镜像对称与环面纤维化》中译注本

## 1. 书目信息

| 项 | 内容 |
|---|---|
| 原文标题 | Homological mirror symmetry and torus fibrations |
| 作者 | Maxim Kontsevich, Yan Soibelman |
| 出处 | arXiv:math/0011041v2 [math.SG]，2001-06-04，66 页（letter 版） |
| 底本文件 | `C:\Users\admin\xwechat_files\wxid_x0ix6rgox7aq22_4797\msg\file\2026-11\Kontsevich_Soibelman_HMS_TorusFibrations.pdf` |
| 语言 | 英 → 中（简体） |
| 体例 | 中文译注本：译文 + 译注框 + 术语表 + 页码对照 + 勘误 |
| 成品 | `成品/Kontsevich-Soibelman_环面纤维化HMS_中文译注本.pdf` |

## 2. 文章结构与页码（底本页 = PDF 页；原始印刷页码自 p1 起，与 PDF 页一致）

| 节 | 原文标题（照录） | 页 |
|---|---|---|
| — | 标题、作者、单位 | 1 |
| §1 | Introduction | 1–3 |
| 1.1 | Homological mirror symmetry and degenerations | 1 |
| 1.2 | Content of the paper | 3 |
| §2 | Degenerations of unitary Conformal Field Theories | 4–12 |
| 2.1 | Moduli space of Conformal Field Theories | 5 |
| 2.2 | Physical picture of a simple collapse | 6 |
| 2.3 | Multiple collapse and the structure of the boundary | 7 |
| 2.4 | Example: Toroidal models | 8 |
| 2.5 | Example: WZW model for SU(2) | 9 |
| 2.6 | A-model and B-model of N = 2 SCFT as boundary strata | 10 |
| 2.7 | Mirror symmetry and the collapse | 11 |
| §3 | Calabi–Yau manifolds in the large complex structure limit | 13–21 |
| 3.1 | Maximal degenerations of Calabi–Yau manifolds | 13 |
| 3.2 | Monge–Ampère manifolds and duality of torus fibrations | 17 |
| 3.3 | Speculations about relations with non-archimedean geometry | 20 |
| §4 | A∞-algebras and A∞-categories | 22–27 |
| 4.1 | Two problems with the general definition | 22 |
| 4.2 | Non-unital A∞-algebras and A∞-categories | 22 |
| 4.3 | A∞-pre-categories | 23 |
| 4.4 | Example: directed A∞-pre-categories | 28 |
| §5 | Fukaya category and its degeneration | 28–35 |
| 5.1 | Fukaya category | 28 |
| 5.2 | Fukaya–Oh category for torus fibration | 32 |
| §6 | Morse–Smale complex and the category of Morse functions | 36–47 |
| 6.1 | Notations from Morse theory | 36 |
| 6.2 | Morse A∞-category of smooth functions | 37 |
| 6.3 | De Rham A∞-category of smooth functions | 40 |
| 6.4 | A∞-structure on a subcomplex | 41 |
| 6.5 | Projectors and homotopies in Morse theory | 44 |
| 6.6 | Proof of the theorem from 6.3 | 47 |
| §7 | A∞-structure for the derived category of coherent sheaves | 48–51 |
| 7.1 | Rigid analytic space | 48 |
| 7.2 | A∞-structure on coherent sheaves | 50 |
| §8 | Homological mirror conjecture | 52–58 |
| 8.1 | Mirror symmetry functor on objects | 52 |
| 8.2 | Spectrum of a morphism and the semigroup | 53 |
| 8.3 | Homological mirror symmetry for abelian varieties | 56 |
| §9 | Appendix: constructions in the case of complex numbers | 59–63 |
| 9.1 | Mirror symmetry functor on objects over C | 59 |
| 9.2 | Sectors in the space of Dolbeault forms | 61 |
| 9.3 | Semigroup φ^t | 63 |
| — | References | 63–66 |

## 3. 数学内容梗概（供译手把握语气，不得直接抄进正文）

§1 提出核心猜想：同调镜像对称应与「退化（大复结构极限/大辛结构极限）」相联系，并交代全文结构。
§2 从共形场论出发作物理motivation：CFT 模空间的边界分层由 A 模型与 B 模型构成，作者提出还存在一个
「T-分层」（环面模型/Narain 格），并用 WZW 模型 SU(2)、环面模型作例。§3 转向几何：Calabi–Yau 流形
的极大退化、Monge–Ampère 流形与对偶环面纤维化，猜想坍缩中的度量与整仿射结构相容。
§4 建立 A∞-代数/A∞-范畴/A∞-预范畴（非幺、横截性受控）的框架，§5 造 Fukaya 型 A∞-预范畴（含
Fukaya–Oh 的环面纤维化版本），§6 造 Morse–Smale / de Rham 侧 A∞-预范畴并证明二者等价（定理 2），
§7 在非阿基米德刚性解析空间上构造凝聚层导出范畴的 A∞-结构，§8 陈述同调镜像猜想并证明阿贝尔簇情形
（定理 4），§9 为复几何情形下的技术附录（Dolbeault 扇形分解、半群 φ^t）。

## 4. 工作纪律（必须遵守）

1. **底本**：只译 SY01-25 的底本 PDF；文字取 `工程文件/work/pages/pNNN.txt`，公式与排版核
   `工程文件/work/pages/pNNN.png`（`read_image` 看图）。文字层不可信是常态。
2. **术语**：`工程文件/work/glossary.tsv` 已冻结，不得另立译名；表外术语按《风格指南》§2 处理并登记。
3. **不臆造**：原文没有的话不补；原文的错误照译加注。宁可不顺，不可改数学。
4. **格式**：纯正文 chunk，环境名与宏见 `源码/preamble.tex`；不新增宏。
5. **报告**：每块写 `工程文件/reports/chNN.md`，含：完成范围（原文章节/页码）、页数对账（原文页数 vs 译稿对数）、
   新增术语、译注清单、存疑/勘误、未完成项。
6. **禁止**：不查黑名单站点（知乎/百度百科/CSDN/简书/公众号/B站笔记/AI 摘要）；不改 preamble；
   不动他人 chunk；不写 `\documentclass`。
