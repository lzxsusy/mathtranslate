# 讲义扩写计划（PLAN v1.0）：从 22 页到 90–100 页

> 为什么扩写：Witten 原文大量关键步骤只给一句（"one can show"、"it is easy to see"），
> 而河野/上野/Moore/Schottenloher/李思各补一块、互相不认账、归一化还彼此冲突。
> 本讲义的任务就是**把这些缝补齐、把约定对齐、把每一步写成可检验的推导**。

## 0. 分工与文件（写作用，互不重叠）

| 负责人 | 文件 | 内容 | 目标页 |
|---|---|---|---|
| Lead | ch01_intro, ch02_cs_action, ch11_categorification, ch12_boundary, main.tex, preamble.tex, appB, appC, appE | 导论/CS 作用量/范畴化/边界/集成/习题答案/文献注记 | 30 |
| historian | ch03_phase_space, ch04_prequantization | 相空间与辛商；预量子化、极化、半形式、行列式线丛 | 20 |
| bibliographer | ch07_wzw, ch08_surgery | WZW 工具箱/KZ；手术、S/T 矩阵、标架反常 | 20 |
| writer-1 | ch05_conformal_blocks, ch06_wilson_bwb | 共形块与射影平坦性；Wilson 线/穿刺点/BWB | 18 |
| writer-2 | ch09_verlinde, ch10_duality | Verlinde 两条路线；CS/WZW vs AdS₃/CFT₂ | 18 |
| archivist | appA_conventions, appD_errata | 符号表+约定对照（含五本书归一化换算）；勘误汇总 | 8 |
| verifier | 独立审读，不改正文 | 每章抽 4 处断言核锚点+判断定理/纲领，出 score | — |

Lead 负责最终集成：统一符号、删重复、补过渡、编译、查排版。

## 1. 缺口总清单（G = gap；每条都要求在正文补成推导或明确标"未找到证明"）

### ch03 相空间与辛结构
- G3.1 从 (3.1) 到 (3.2) 的 Legendre 变换：为什么 CS 作用量对时间一阶就给出泊松括号；符号与 $4\pi/k$ 因子的来源。[我们]
- G3.2 辛形式 $\omega=\frac{k}{4\pi}\int_\Sigma\mathrm{Tr}(\delta A\wedge\delta A)$ 的良定性：规范变换下不变（只差恰当项），$\Sigma$ 闭、$A$ 平凡化处如何定义。
- G3.3 高斯约束是第一类约束、生成规范变换的验证（含 $\varepsilon$ 的边界项）。
- G3.4 Marsden–Weinstein 辛商的三步（零集、商、辛形式下降），Atiyah–Bott 的适用条件。
- G3.5 $\dim\mathcal M=(2g-2)d$ 的推导（$\dim\mathrm{Hom}(\pi_1\Sigma,G)=2gd-(2g-2)d$ 的口径要交代）。
- G3.6 奇点：可约联络、稳定化子；为什么取"稳定点的商"或"抛物结构"。

### ch04 预量子化、极化、半形式
- G4.1 Weil–Kostant 预量子化定理陈述：$[\omega]\in H^2(M,\mathbb Z)$ ⇔ 线丛+联络；Witten 用行列式线丛**构造性绕过**整性（$\mathcal L$ 先存在，$[\omega]=c_1(\mathcal L^{\otimes k})$）——把这条写清楚。
- G4.2 行列式线丛 $\mathcal L=\det H^0(\Sigma;E)\otimes\det H^1(\Sigma;E)^*$ 的定义、Quillen 度规、其曲率 = $\frac{i}{2\pi}\omega$（Freed / Bismut–Freed 的陈述级引用）。
- G4.3 极化的定义（拉格朗日、可积、维数恒定）、Kähler 极化、Bohr–Sommerfeld 叶；为什么紧相空间不能用 $q,p$ 分离（$p_j$ 无界 vs $\mathcal M$ 紧）。
- G4.4 量子化 = 沿极化方向协变常数的截面；$H^0(\mathcal M_J,\mathcal L^{\otimes k})$ 有限维。
- G4.5 半形式修正 $K^{1/2}$（metaplectic）与 $k\to k+h^\vee$：给出 $K_{\mathcal M}$ 与 $K_{G/T}$ 的具体关系（$K_{G/T}=\mathcal L_{-2\rho}$ ⇒ $K^{1/2}=\mathcal L_{-\rho}$），并说明 $k+h^\vee$ 与 $c_2/2$ 的一致性；**本文未做此修正**要明说。
- G4.6 Narasimhan–Seshadri：平坦幺正联络 ↔ 稳定全纯丛；用它把 $\mathcal M$ 看成复 Kähler 簇。

### ch05 共形块与射影平坦
- G5.1 $\mathcal H_\Sigma^{(J)}$ 随 $J$ 的全纯依赖；"与 $J$ 无关"只到**射影**（p.370 原句），给出射影因子的来源（共形反常/标架）。
- G5.2 射影平坦联络 = Hitchin 联络（无标记点）/ KZ 联络（有标记点）的对应；平坦性谁证的（Segal / Hitchin）。
- G5.3 单值性 = 映射类群作用；为什么只有 $\mathbb P\mathcal H_\Sigma$ 典范。
- G5.4 Segal 模函子/共形块的定义（缝合、单位、张量），本文只到"对象级"。

### ch06 Wilson 线、穿刺点、BWB
- G6.1 Wilson 线在切开处变成穿刺点：$W_R(C)$ 与边界条件的对应（$A$ 在 $P$ 附近的奇异行为）。
- G6.2 (3.4) 是算符值约束的两个理由：右端不对易；点源奇异性（给出 $A\sim$ 单极型解）。
- G6.3 Borel–Weil–Bott：$H^0(G/T,\mathcal L_\lambda)=R_\lambda$（$\lambda$ 支配整权），为何**不加 $\rho$**；$\rho$ 属于 $K^{1/2}$；给 BWB 的证明思路（Weyl 特征标公式 / 指标定理）。
- G6.4 $G/T$ 的辛形式 $\omega_\lambda$（轨道方法，$G/T\cong\mathcal O_\lambda$，$\omega_\lambda(X,Y)=\frac12\langle\lambda,[X,Y]\rangle$）与 $[\omega_\lambda]=\lambda$。
- G6.5 扩大相空间 $\mathcal M_{\{P_i,R_i\}}$ 的构造；量子化后得共形块（引 Segal/TUY）。
- G6.6 可积条件 $2j\le k$（$SU(2)$）来自仿射代数（$\lambda\le k$），**不是** BWB 的推论。

### ch07 WZW 与共形场论工具箱
- G7.1 仿射 Kac–Moody：$\widehat{\mathfrak g}_k$、模、最高权表示、Sugawara 构造、$c=\frac{k\dim G}{k+h^\vee}$。
- G7.2 共形块的定义与维数；WZW 的 Ward 恒等式。
- G7.3 KZ 方程推导：null field + Ward ⇒ $\kappa\partial_{\bar z}\psi=\sum_{i<j}\frac{\Omega_{ij}}{z_i-z_j}\psi$，$\kappa=k+h^\vee$；与本文 §3.2 联络的关系。
- G7.4 融合规则与 Verlinde 代数；$N_{ijk}=\dim$（三点共形块）。
- G7.5 与本文符号的对照（$\ell$ vs $k$、$h^\vee$ 移位、$q$）。

### ch08 手术、S/T 矩阵、标架反常
- G8.1 手术表示：任意闭 3-流形可由 $S^3$ 沿链环手术得到；手术链环的 Kirby 移动。
- G8.2 手术公式 (4.28) 的推导：两种算法（先手术再算 CS / 先算链环不变量）对比。
- G8.3 $S$、$T$ 矩阵的来源：$S$ = 环面上的模变换，$T$ = 标架变换；$S^2=(ST)^3=C$。
- G8.4 标架反常：为什么 $Z$ 带 $e^{2\pi i c/24}$；Wilson 线的共形权相位；$c$ 与 $h_R$ 的公式。
- G8.5 (4.51) 的完整推导（$S$ 对角化融合规则的两种读法）。

### ch09 Verlinde
- G9.1 从手术公式到 (4.51) 的十步链（三处输入：手术律、$N_{abc}$ 定义、秩一性），逐步给式子。
- G9.2 融合规则 ⇒ $S$ 矩阵（Verlinde 代数对角化）；$S$ 矩阵 ⇒ 融合规则。
- G9.3 两种读法：物理推导（Witten）/ 数学证明（TUY 1989、Faltings 1994）；Moore–Seiberg 的地位。
- G9.4 $SU(2)$ 的显式 $S$ 与 $N$；$k=1,2$ 的表格复算。
- G9.5 截断：可积表示 $2j\le k$；$N_{111}=0$ 的例子。

### ch10 对偶
- G10.1 CS/WZW：态空间等同（$X\times S^1$ 上 $Z=\dim H_X$），为什么不是体/边界对偶。
- G10.2 AdS₃/CFT₂：Brown–Henneaux $c=3l/2G$，边界条件与全息字典；与本文无度规理论的区别。
- G10.3 唯一接触点"3d 引力 = CS"（非紧群、经典层面）；为什么是改写不是等同。
- G10.4 1988 年语境：全息还没出现（Maldacena 1997）；本文 p.397 只是动机链。

### ch11 范畴化（延伸，6 页）
- Khovanov 立方体构造；Euler 特征退回 Jones；函子性；物理来源 Witten 2011/KW 2007；本文无暗示。

### ch12 边界与读法（6 页）
- 本文五处留白；后世补齐表；三遍读法；开放问题清单（与 questions.jsonl 对应）。

## 2. 全书一致性要求（Integration 检查项）

1. 附录 A 的符号是唯一权威；正文出现新符号必须回填。
2. $k$ 的归一化：全文统一用本文 $L=\frac{k}{4\pi}\int\mathrm{Tr}(A dA+\frac23A^3)$；凡是引河野/Moore 的公式，必须换算后再写，并标 `[换算见 appA]`。
3. $h^\vee$、$c$、$q$ 的公式在三章以上出现时，必须用同一写法（从 appA 抄）。
4. 同一个事实只能在一处证明，其余章给交叉引用（`\cref` 或"见 §x.y"）。
5. 每章末必须能回答："本章补了原文哪几处缺口（G-x 编号）"。

## 3. 验收

- 页数 90–105（正文，不含附录）；每章 6–10 页。
- 0 编译错误；0 overfull > 5pt；每章至少 1 图或 1 表。
- 锚点：`check_anchors.py` 0 错误；verifier 每章抽 4 条，fabricated = 0 才收。
- 人类抽查：随机 5 页，能读懂、能复算。
