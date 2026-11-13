# 报告 A · 问题从哪来（S1 / T0）

> historian｜2026-11-13｜依据 `agenda.md` §1 的必答五问
> 锚点约定：`[原文 p.N]` = Witten 1989 原刊印刷页；`[eq x.y]` = 原刊公式号；`[河野 p.N]` = 中译本页码。

**一句话结论**：Atiyah 两问的"原文"本机不存在，我们手上只有 **Witten 在 p.351 的转述**；而本文对第二问的回应强度是 `assert`，不是 `prove`。本场所有分级都从这两点出发——这正好回答了主席开场写在白板上的那个问题：**物理等价 ≠ 数学定理**。

---

## 一、Atiyah 两问：表述、出处、谁在转述

| 项 | 内容 | 锚点 |
|---|---|---|
| 提问场合 | "In a lecture at the Hermann Weyl Symposium last year [1], Michael Atiyah proposed two problems for quantum field theorists." | [原文 p.351] |
| 第一问 | "to give a physical interpretation to Donaldson theory" | [原文 p.351] |
| 第二问 | "to find an intrinsically three dimensional definition of the Jones polynomial of knot theory" | [原文 p.351] |
| Atiyah 原始文献 | Atiyah, *New invariants of three and four dimensional manifolds*, in: The Mathematical Heritage of Hermann Weyl, Proc. Symp. Pure Math. **48**, AMS 1988, 285–299 | 本文文献 [1]，[原文 p.398] |
| **谁在转述** | **Witten**；且他主动降调："These two problems might roughly be described as follows."（"大致可以这样描述"） | [原文 p.351] |

**判断**：只能说"Witten 把 Atiyah 的两问转述为……"，不能说"Atiyah 的原话是……"。Atiyah 1988 本机无藏（`文献表.md` R01 标"无"），Witten 又只是"大致描述"，这已是**转述的转述**[^3]。

## 二、第一问谁解决了、何时、用什么

- 原文只有一句："It turned out that Donaldson theory does have a physical interpretation [4]." [原文 p.352]
- **谁**：Witten 本人——[4] 即 Witten, *Topological quantum field theory*, Commun. Math. Phys. **117**, 353 (1988) [原文 p.398]。
- **何时**：1988 年，与本文同年；[4] 的确切投稿日期本机未核。
- **用什么**：原文只给"physical interpretation"四个字，**没有**给机制；具体机制（扭曲 $\mathcal N=2$ 超对称杨–米尔斯）不在本文文字内，本机亦无 [4] 全文，只能算推断。
- **动词**：`turned out`（结果证明）——事后叙述，不是 "I proved"。这一点在质询时会用得上：连第一问，Witten 也没在这篇文章里说"证明了"。

## 三、"Jones 只有二维投影图定义"——具体缺什么

原文三句 [原文 p.352]：

1. "These objects are topological invariants of three dimensional situations, but one does not have an intrinsically three dimensional definition of them."
2. "The various elegant definitions ... all depend in some way on a two dimensional projection or slicing of the knot, give a two dimensional algorithm for computing them,"
3. "**and then prove that the result is independent of the projection or slicing that was used.**"

拆成三条缺陷：

| # | 缺的东西 | 具体表现 |
|---|---|---|
| ① | **输入不是三维对象** | 定义的第一步是"选一个投影/切片/辫表示"，而非"取一个三维流形与链环" |
| ② | **算法只在二维里跑** | 括号代数、态模型、R 矩阵——都是二维组合数据 |
| ③ | **不变性是事后定理** | 投影无关性要靠"再证明一次"补上，不在定义里 |

所以缺的**不是三维算法**（手术算法本文才给，[原文 p.383–384]），而是**定义层面的三维性**：不变性应当从定义直接读出来，而不是作为定理补回去。Witten 的类比落点也在这里——"就像 1930 年代的量子电动力学"：理论其实是相对论性的，但**表述**不显然相对论性 [原文 p.352]。

## 四、摘要的三个弱动词（英文原句逐句标注）

摘要（[原文 p.351]）共四句，动词强度递减：

| 原句（英文） | 动词 | 强度 | 落在哪 |
|---|---|---|---|
| "It **is shown** that 2+1 dimensional quantum Yang-Mills theory ... **is exactly soluble** and **gives** a natural framework for understanding the Jones polynomial ... in three dimensional terms." | is shown / is exactly soluble / gives | 弱：被动、无施动者；"framework"不是"identity" | (1.6) 定义 [原文 p.355–356]；可解性对应 §4 手术公式 (4.27)–(4.32) [原文 p.383–386] |
| "the Jones polynomial **can be generalized** from $S^3$ to arbitrary three manifolds, **giving** invariants ... **computable** from a surgery presentation." | can be generalized / computable | 弱：可能性 + 可计算性 | (4.27)(4.28) [原文 p.384]；(4.30)–(4.32) [原文 p.385–386] |
| "These results **shed** a surprising new light on conformal field theory in 1+1 dimensions." | shed | 最弱：纯比喻 | §5 [原文 p.394–397] |

三个"弱动词"取 **is shown / can be generalized / shed**（"gives" 同级，可并入第一句）。须知：摘要**从未出现** prove / demonstrate / establish。而 "is exactly soluble" 是形容词断言，不是动词，但它才是摘要里最强的一句——正文对应处也只到 `argue`（见下）。

## 五、G1–G5 的分级

| 目标 | 原文动词/措辞 | 分级 | 锚点 |
|---|---|---|---|
| G1 内蕴三维定义：$S^3$ 链环的 (1.6) 就是 Jones 及其推广 | "we will **assert**" | **断言** | [原文 p.356] |
| G2 CS 理论可精确求解 | "we will **argue** that it is exactly soluble" | **论证** | [原文 p.353] |
| G3 $\mathcal H_\Sigma$ 有限维、且与 $J$ 无关 | 有限维："will see"；平坦性："Segal 严格证明"，物理论证只是启发式 | **证明（有限维）/ 论证（平坦性，借 Segal 定理）** | [原文 p.366–367]；[p.369–370] |
| G4 任意 3-流形不变量的手术算法 | 无动词，直接给公式；一般手术的 $e^{2\pi i c/24}$ 追踪"另文" | **计算方案 + 承诺另文** | [原文 p.383–386]；[p.391] |
| G5 共形块 = 3d 理论 Hilbert 空间 | "can be **interpreted** as" | **论证** | [原文 p.368–369]；[p.396] |

**收口一句**：五个目标里，**没有一条**是对第二问本身的 `prove`；"证明"只出现在 G3 的有限维性（由辛体积有限得出）与 Segal 那条外部定理上。本场若有人把 G1 说成"Witten 证明了 (1.6) 等于 Jones 多项式"，即可按 agenda §8 的一票否决处理。

---

### 脚注

[^1]: **查阅 1（摘要英文原句）**：`s00-front.tex` 是译文，英文原句在 `witten1989\text\page-01.txt`（原刊扫描 OCR）：摘要在第 10–16 行，两问在第 17–20 行。逐句动词：`is shown`（L10–12）、`is exactly soluble`/`gives`（L11–13）、`can be generalized`/`computable`（L13–15）、`shed`（L15–16）——四句，无一个 prove/demonstrate。同页脚注 *（L37）表明本文是 "An expanded version of a lecture at the IAMP Congress, Swansea, July, 1988"。

[^2]: **查阅 2（河野序，两种方法写态空间）**：中译本序（[河野 p.4]，印刷页 iv）原话——"本书的主题——共形场理论与 Chern–Simons 理论的关系——也正是从 Chern–Simons 泛函出发、用两种方法写出态空间之后才被发现的。"紧接着一句即主席的开场引文："物理意义上的等价性，在几何学中未必是被证明了的事实。"**对应本文**：两种方法 = 路径积分（§2 弱耦合 + §4 手术）与正则/几何量子化（§3，"写出态空间" = $\mathcal H_\Sigma=L^{\otimes k}$ 的整体全纯截面 [原文 p.368]）；两路在 §5 合流为"$\mathcal H_\Sigma$ = 共形块空间" [原文 p.394–397]。河野把这句话放在"物理等价 ≠ 数学定理"的上下文里，与本报告第五节的动词分级同构。

[^3]: **查阅 3（Atiyah 无原文）**：Atiyah, *New invariants of three and four dimensional manifolds*（Proc. Symp. Pure Math. 48, 1988, 285–299）本机无藏（`文献表.md` R01 标"无"）。本报告所有 Atiyah 表述一律标注"转述（Witten, [原文 p.351]）"，不冒充原话；两问的措辞若有出入，以 Atiyah 原文为准，届时须回头改本报告。

[^4]: **查阅 4（时间线旁证，供质询用）**：本文是 1988 年 7 月 Swansea IAMP 报告的扩充版 [原文 p.351 脚注 *]，距收稿 1988-09-12 约两个月、距修改稿 09-27 约三个月。这两个月既有"报告后集中写成"的可能，也不排除"长期思考的收束"——单凭日期**无法判定**，除非找到更早的讲稿或通信。

---

### 待定（不进正文）

1. Atiyah 1988 的确切措辞、以及 Hermann Weyl 讨论会的年份（Witten 说 "last year"，是否为 1987）——须查 Proc. Symp. Pure Math. 48 原书。
2. [4] 中"物理地解释 Donaldson 理论"的具体机制（拓扑扭曲 $\mathcal N=2$ 超对称杨–米尔斯）：本机无 [4] 全文，属推断，未核。
3. 原文是否在任何一处把 "exactly soluble" 升级为 prove：我抽查 s00–s02、s07–s09 的中译与英文页，只见到 `argue`、`assert` 与具体计算，未见 prove；§4 其余各页未逐页核。
4. 河野引文取自中译本；日文原书（p.v）措辞未逐字核，若研讨班要逐字引日文需另核。
