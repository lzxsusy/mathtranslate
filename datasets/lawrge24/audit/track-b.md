# LAWRGE 2024 notes — track B 外部来源核验

范围：`datasets/lawrge24/cards/concepts/` 中 `track` 为 `B` 的 8 张卡——
`raviolo-hecke`、`hecke-category`、`affine-grassmannian`、`geometric-satake`、
`derived-satake`、`spectral-action`、`koszul-duality`、`e3-structure`。

底本：LAWRGE 2024 NOTES（73 页工作坊笔记，Ben-Zvi / Sakellaridis / Venkatesh 主讲，
无 arXiv 版，自述“不完整、未校订”），PDF 取自 <https://www.hwilliams.net/lawrge2024.pdf>。
逐条结果见同目录 [`track-b.jsonl`](./track-b.jsonl)（21 行，一行一条断言）。

## 0. 结论摘要

| 指标 | 值 |
| --- | --- |
| 卡数 | 8 |
| 断言数 | 21（每卡 2–3 条） |
| 来源条目 | 44（11 个不同 URL：7 篇 arXiv 论文 + 4 个 nLab 页） |
| supported | 14 |
| partially-supported | 4 |
| unverifiable | 1 |
| conflict | 2 |
| severity critical / major / minor | 1 / 3 / 17 |

8 张卡里，`raviolo-hecke`、`affine-grassmannian` 全部断言有外部逐字支持；
`e3-structure` 与 `derived-satake` 各有一条**表述性冲突**（不是底本“没写清楚”，
而是底本给出的结论与外部权威文献相反）。没有发现“引文/定理编号张冠李戴”的问题，
冲突集中在一个概念上：**把 E₃-结构当成对称幺半结构**。

最需人工处理的 3 条：

1. **`e3-structure`：E₃ ⇒ 对称幺半 —— `conflict` / `critical`。**
   底本 p.35：“when n = 3, the first multiplication necessarily becomes commutative, so we get
   symmetric monoidal categories”，p.33 紧接着写 “In particular, A_G(R) is a symmetric monoidal
   category”。外部三处正面反对：BZSV p.345 “this is truly a noncommutative object, i.e., is not
   given by a symmetric monoidal (i.e., E∞) structure”；BZSV p.330 称 E₃ 是 “a derived weakening of
   the notion of symmetric monoidal category”；AG15 Rem. 12.4.3 说 IndCoh(Hecke_spec) “does not admit
   an E2-structure which is compatible with the factorizable structure, even if G is a torus”。nLab 的周期表（3-重幺半 ⇒ 对称幺半）只对**普通 (n,r)-范畴**成立，不适用于
   dg/∞-范畴——这正是底本把范畴论直觉搬到导出范畴上的地方。
2. **`derived-satake`：定理 7.10 的“对称幺半” —— `conflict` / `major`。**
   底本 p.37 写 “equivalence of symmetric monoidal categories”；BF08 p.7 只说 “monoidal triangulated
   categories”，AG15 Rem. 12.4.3 “only between mere monoidal categories: it is not compatible with the
   factorizable structure”，BZSV Rem. 6.6.2 “only of monoidal categories … absence of any ‘parity’
   correction”。三处外部文献口径一致：导出版本只到 monoidal，对称性属于 E₃ 层。
3. **`spectral-action`：朴素范畴等价为假 —— `partially-supported` / `minor`。**
   底本 p.36 说右边作用局部常值、左边“完全不局部常值”；BZSV §C.4 的准确版本是取**最大的局部常值
   子范畴**（spectrally decomposable part），且 de Rham 情形 “D(Bun_G)_spec = D(Bun_G) and the
   spectral projector is the identity”（p.408）——即底本那句话并非普遍成立，需按层论情形分别写。

## 1. 方法与底本对应

- 底本 pdf 的 73 页与卡内 source 页码（p.23 / p.33 / p.34 / p.35 / p.36 / p.37）逐一对过；
  `base_32_38.txt` 保留 §4/§7 的全文，用于逐字比对卡片转写。
- 主外部源：**BZSV, _Relative Langlands Duality_, arXiv:2409.04677**。作者群与底本主讲人重合，
  是这份 notes 的完整论文版；底本 §7 的核心内容对应 BZSV §6.6（derived Satake）、§13（raviolo /
  Koszul）、§16.2–§17.1（E₃ / factorization）、§C.4（spectral action）。
- 独立源（与底本、与 BZSV 均无共同作者）：Zhu 的 PCMI 讲义（arXiv:1603.05593）、
  Mirković–Vilonen（arXiv:math/0401222）、Bezrukavnikov–Finkelberg（arXiv:0707.3799）、
  Arinkin–Gaitsgory（arXiv:1201.6343）、Nocera（arXiv:2012.08504）、Nadler–Yun（arXiv:1611.04078）、
  以及 nLab 的 4 个条目。
- 每条断言尽量取 2 个来源；只有 `e3-structure` 的分歧点那条（外部无对应陈述）只列 1 个“用来证明
  检索范围”的来源。**同文档的两处不算独立来源**，这种情况在 `note` 里写明（R3、K1 等条）。
- 引文一律从 PDF / arXiv HTML / nLab 纯文本切出，未做转述；公式按论文排版转写（见 §6）。
  URL 均实际打开过（curl 或浏览器），打不开的记在 §5。

## 2. 来源清单

| 简称 | 条目 | URL |
| --- | --- | --- |
| BZSV | Ben-Zvi–Sakellaridis–Venkatesh, Relative Langlands Duality, arXiv:2409.04677 | <https://arxiv.org/abs/2409.04677> |
| AG15 | Arinkin–Gaitsgory, Singular support of coherent sheaves and the geometric Langlands conjecture, arXiv:1201.6343 | <https://arxiv.org/abs/1201.6343> |
| BF08 | Bezrukavnikov–Finkelberg, Equivariant Satake category and Kostant–Whittaker reduction, arXiv:0707.3799 | <https://arxiv.org/abs/0707.3799> |
| Zhu | Zhu, An introduction to affine Grassmannians and the geometric Satake equivalence, arXiv:1603.05593 | <https://arxiv.org/abs/1603.05593> |
| MV | Mirković–Vilonen, Geometric Langlands duality and representations of algebraic groups over commutative rings, arXiv:math/0401222 | <https://arxiv.org/abs/math/0401222> |
| Nocera | Nocera, A model for the E3 fusion–convolution product of constructible sheaves on the affine Grassmannian, arXiv:2012.08504 | <https://arxiv.org/abs/2012.08504> |
| NY | Nadler–Yun, Spectral action in Betti geometric Langlands, arXiv:1611.04078 | <https://arxiv.org/abs/1611.04078> |
| nLab-GS | nLab, Geometric Satake equivalence | <https://ncatlab.org/nlab/show/geometric+Satake+equivalence> |
| nLab-AG | nLab, Affine Grassmannian | <https://ncatlab.org/nlab/show/affine+Grassmannian> |
| nLab-KD | nLab, Koszul duality | <https://ncatlab.org/nlab/show/Koszul+duality> |
| nLab-KT | nLab, k-tuply monoidal (n,r)-category | <https://ncatlab.org/nlab/show/k-tuply+monoidal+%28n%2Cr%29-category> |

## 3. 逐卡结果

| 卡 | 断言 | verdict | 要点 |
| --- | --- | --- | --- |
| raviolo-hecke | 3 | 3 supported | Bun_G(R) 的等变 Gr 解释、双陪集粘接函数、Loc(R)=Loc(P¹) 均有逐字支持。 |
| hecke-category | 2 | supported ×1, partially ×1 | 范畴识别无问题；“三叠点碰撞”的卷积公式外部只有二重版本，底本自承定义域不严格。 |
| affine-grassmannian | 2 | 2 supported | ind-射影性、轨道分类与闭包射影均与 Zhu/MV 一致；`Shv(Gr)=Shv_{G(O)}(Gr)` 的记号需注意。 |
| geometric-satake | 3 | supported ×2, partially ×1 | 对称幺半等价、经典 Satake 有逐字支持；“两个纤维函子差 Koszul 符号律”是笔记综合。 |
| derived-satake | 3 | supported ×2, conflict ×1 | 等价本身被 AG15/BF08 支持；**“对称幺半”与三处外部文献冲突**。 |
| spectral-action | 2 | supported ×1, partially ×1 | 作用分解有支持；“左边完全不局部常值”需按 BZSV 的 spectrally decomposable 子范畴收窄。 |
| koszul-duality | 3 | supported ×2, partially ×1 | Ωĝ/Ĝ 与 Koszul 对偶均有支持；Perf/QCoh 的写法与 AG15 原文措辞有出入。 |
| e3-structure | 3 | supported ×1, conflict ×1, unverifiable ×1 | E₃ 结构存在（Nocera/BZSV 支持）；**“E₃⇒对称幺半”冲突**；分歧点断言外部无对应。 |

## 4. 需改卡清单

按优先级：

1. **`e3-structure`（critical）** — 改写 `definition` 第 2–3 句、`key_points[0]`、`formulas[0]`
   （`E_1⊂E_2⊂E_3 symmetric`）与 `pitfalls[1]`。正确表述：E₃ 是“幺半 + 因子化（E₂ 碰撞）”的导出
   结构，比对称幺半**弱**，Hecke 范畴在其上是非交换对象；对称幺半只在普通范畴/阿贝尔球面范畴里成立。
   可引 Nocera 摘要 + BZSV §17.1.2。
2. **`derived-satake`（major）** — `definition`、`key_points`、`formulas`、`pitfalls` 中出现“对称幺半”
   的地方统一降为 monoidal，并把对称性归到 E₃（与上一条一致）。同时按 AG15 原文把注 7.9 的
   `Coh ≃ Perf(ǧ*[2]/Ĝ)` 改成 `Coh ≃ Sph(G,x)^{loc.c}`、`IndCoh ≃ Sym(ǧ[−2])-mod`，再说明经
   Koszul 对偶得到卡的写法（见 K3 条）。
3. **`spectral-action`（minor）** — `definition` 末句与 `key_points[1]` 加 de Rham caveat：de Rham 情形
   整个范畴都是 spectrally decomposable（BZSV p.408），不能说“左边完全不局部常值”。
4. **`hecke-category`（minor）** — 注 7.1 的碰撞公式保留，但明确标注“底本自承推前定义域不严格”，
   严格版本指向 Zhu (5.1.3) 的二重卷积或 Nocera 的 E₃ 模型。
5. **`geometric-satake`（minor）** — 注 7.5 的“两个纤维函子差 Koszul 符号律”标为笔记综合；
   nLab 只确认对称幺半约束是额外 data，BZSV 反而说导出版本无 parity 修正。
6. **`affine-grassmannian`（minor）** — `formulas` 里 `Shv(Gr)=Shv_{G(O)}(Gr)` 建议写成
   `Shv_{G(O)}(Gr)`（或说明左边的约定），否则与“等变性不可省”的正文自相矛盾。
7. **`koszul-duality`（minor）** — K3 条的 Perf/QCoh 形式加一句“经 Koszul 对偶改写自 AG15 的
   Sph^{loc.c} / Sym(ǧ[−2])-mod”。
8. **`raviolo-hecke`** — 无需改动（3 条全部 supported）。

## 5. 不可核验与失败尝试

- **`e3-structure` 分歧点断言**（“at a ramified point x₀ … we do not have a E3-structure”）：只在底本
  p.33 出现。尝试过的入口：<https://arxiv.org/abs/2012.08504>（Nocera 摘要/正文只处理光滑曲线）、
  <https://ncatlab.org/nlab/show/factorization+algebra>（仅一般定义）、
  <https://ncatlab.org/nlab/show/En-algebra>（无相关陈述）。BZSV、AG15 亦无对应陈述，故记
  `unverifiable / minor`，不替底本补证明。
- **nLab raviolo 页**：<https://ncatlab.org/nlab/show/raviolo> 与
  <https://ncatlab.org/nlab/show/E-k+operad> 均返回同一 13214 字符的空模板页（无条目内容），
  未引用任何“raviolo”nLab 说法。
- **[AGK+20b]**（BZSV 引用的 étale spectral action 文献）：未取到原文，凡涉及它的陈述只按 BZSV 的
  转述记录，不单独作为来源。
- **BZSV v2**：arXiv 上只有 v1（v2 链接 404），本审计以 v1 为准。

## 6. 引用转录说明

- PDF 文本提取（PyMuPDF）会把数学字体映射成怪字符：`∪` → `š`、`E_∞` → `E8`、`≅` → `»`、
  `(…)` → `p…q`。凡引文中出现公式的，按**论文排版**转写，并在该条 `note` 里说明；纯文字引文
  保持提取原样（包括 “P1” 这种 PDF 实际印法）。
- 引文均 ≤200 字符；`…` 表示句中截断，不是省略原文内容。
- 每条 `sources` 里的 `stance` 写该来源“支持/削弱/反对”的具体对象，便于复核。
