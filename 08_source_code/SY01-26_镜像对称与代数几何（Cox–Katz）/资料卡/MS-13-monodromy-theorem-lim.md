---
id: MS-13
zh: 单值性定理与极限混合 Hodge 结构
en: monodromy theorem and limiting mixed Hodge structure
aliases: [单值性定理, 极限混合 Hodge 结构, LMHS, 极限 Hodge 滤过, 单值性权滤过]
layer: L1
prereqs: [MS-12]
sources:
  - "A 级：Cox–Katz 1999, §5.1.3, PDF p.98（[Landman] 单值性定理、T_j 的定义）"
  - "A 级：Cox–Katz 1999, §5.1.4, PDF p.99（[Schmid] 幂零轨道定理；式 (5.3)–(5.4)；三条性质）"
  - "A 级：Cox–Katz 1999, §5.1.5, PDF p.99–101（留数 Res(∇)、T 幺幂 ⇔ Res 幂零、指标方程）"
  - "A 级：Cox–Katz 1999, §5.2, PDF p.101–103（最大幺幂、式 (5.5)、Hodge–Tate 特化）"
  - "A 级：Landman 1973, On the Picard-Lefschetz transformations, Trans. Amer. Math. Soc. 181, 89–126（定理号待核）"
  - "A 级：Schmid 1973, Variation of Hodge structure: the singularities of the period mapping, Invent. Math. 22, 211–319（定理号待核）"
  - "B 级：Cox–Katz 1999, §5.1.3–5.1.4 节内定义（书内节号，PDF p.98–99）"
status: draft
review: {drafter: agent-228, reviewer: lead, blindtest: pending}
glossary_refs: [monodromy, maximally unipotent, nilpotent, quasi-unipotent, variation of Hodge structure, Hodge filtration]
symbols_refs: ['$T_j$', '$N_j = \log T_j$', '$\bar F^\bullet$', '$F_{\mathrm{lim}}^\bullet$', '$W_\bullet$', '$\bar\nabla_{\delta_j} = -\frac{1}{2\pi i} N_j$']
updated: 2026-11-20
---

# MS-13 单值性定理与极限混合 Hodge 结构

*页码约定：本卡书内页码一律为本书 **PDF 物理页**（= 译本 `\SourcePage{N}` = 印刷页 + 23）；外部文献用原书页码或定理号。*

## 1. 一句话

退化族的局部单值性拟幺幂，故能取其极限滤过得极限混合 Hodge 结构。

## 2. 为什么需要它

- **它把「周期在边界怎么变」变成代数数据。** 大复结构极限处 t→i∞，周期积分不再单值解析；单值性定理保证 T_j 拟幺幂（PDF p.98），于是 N_j=log T_j 有定义且幂零，才能写出 exp(−(1/2πi)Σ_j log(z_j)N_j) 型的典范延拓并在边界点取值得 F_lim（§5.1.4，PDF p.99）。
- **它给出退化时的「Hodge 数」。** 退化纤维的上同调不再是纯 Hodge 结构，必须换成 (W_•,F_lim) 这套混合数据；CY 三维最大幺幂时更塌缩为 Hodge–Tate（式 mum-top-splitting，PDF p.103），这正是镜像映射里选出规范坐标的依据。
- **它是第 5 章全部计算的入口。** 式 (5.3) ∇̄_δ=−(1/2πi)N 把 Gauss–Manin 联络的延拓与 N 绑定（PDF p.99）；§5.2 据此推出 Ω(0),NΩ(0),N²Ω(0),N³Ω(0) 是一组基（PDF p.103），最大幺幂判据、Yukawa 耦合与 PF 方程指标判据都从这里出发。
- **权滤过 W_• 是全书的通用语言。** 第 5 章 §5.2 与第 6 章 A 模型 Hodge 结构变分都用 F_lim（chapter06.tex:1200 的 F^d_lim，PDF 页待核）；最大幺幂点讨论再引 [Deligne2 §6]（PDF p.128）。

## 3. 定义（全假设）

设定与假设逐条写全（均见 §5.1.1、§5.1.3–5.1.4，PDF p.97–99）：

1. **族。** π:X→S 是光滑态射（相对维数 n），S 光滑拟射影复流形，t∈S 为基点，X_t=π^{−1}(t)。
2. **补成正规交叉退化。** 存在 S̄ 光滑紧化，D=S̄−S=∪_j D_j 是正规交叉除子；局部取坐标 z_1,…,z_r 使 D={z_1⋯z_r=0}，可设 S=(Δ*)^r、S̄=Δ^r、边界点 p=0（PDF p.98–99）。**不假设 D_j 互不相交**，只要求交截正规。
3. **局部系统与单值表示。** H=R^nπ_*C 是 S 上局部系统（等价说法：带平坦联络 ∇ 的向量丛 F^0=R^nπ_*C⊗O_S）；在基点纤维 H_t 上得表示 ρ:π_1(S,t)→GL(H_t)。对每个 j 取逆时针绕 D_j 的小回路 γ_j，T_j:=ρ([γ_j]) 称**绕 D_j 的单值性**（monodromy，书 §5.1.3 同时叫它 Picard–Lefschetz 变换）；共轭意义下只依赖 D_j、不依赖 γ_j 与基点的选取。
4. **Hodge 结构变分。** F^p⊂F^0 为 Hodge 滤过（p=n,…,0），∇(F^p)⊂F^{p−1}⊗Ω_S^1（Griffiths 横截性），H_Z⊂H 为整系数子层；四元组 (H,∇,H_Z,F^•) 即 Hodge 结构变分（PDF p.97）。
5. **幺幂假设（关键）。** §5.1.4 只处理 T_j **幺幂**（T_j−I 幂零）的情形。单值性定理只给拟幺幂，故一般需先做基变换 t=s^m（局部）去掉有限阶部分（§5 第 5 行）；**若不作此假设，N_j=log T_j 仍可定义，但 exp 公式与 F_lim 的陈述要带有限群作用，本书不展开。**
6. **N_j。** 幺幂时 N_j:=log T_j=Σ_{k≥1}(−1)^{k+1}(T_j−I)^k/k 是**有限**和并幂零（因 (T_j−I)^{n+1}=0，k>n 项为零；PDF p.98–99）。多变量时取 N:=Σ_j a_j N_j（a_j>0）。
7. **典范延拓。** F^p 到 S̄ 的延拓 F̄^p 称**典范延拓**，若对每个平坦多值截面 s，exp(−(1/2πi)Σ_j log(z_j)N_j)s 是单值的且延拓为 F̄^p 的截面；此性质唯一刻画 F̄^p（[Deligne1]；PDF p.99）。
8. **极限 Hodge 滤过。** F_lim^p:=F̄^p|_0，即延拓子丛在边界点 0∈Δ^r 处取值；由此得 F_lim^p/F_lim^{p+1} 等分次，以及 N_j(F_lim^p)⊂F_lim^{p−1}（PDF p.99）。
9. **单值性权滤过。** 滤过 W_0⊂W_1⊂⋯⊂W_{2n}=H_t 由 N 定义（式 (5.4)）：W_0=im(N^n)，W_1=im(N^{n−1})∩ker N，W_2=im(N^{n−2})∩ker N+im(N^{n−1})∩ker(N²)，…，W_{2n−1}=ker(N^n)；一般项公式本书指向 [Griffiths2]。**要求** N 幂零、N(W_k)⊂W_{k−2}；书断言该滤过与 a_j>0 的取法无关（未证，见 §11）。
10. **极限混合 Hodge 结构（LMHS）。** 满足 §5 第 3 行三条性质的一对 (W_•,F_lim^•) 称 H_t 上的**极限混合 Hodge 结构**；它只依赖 (N_j,F_lim) 的局部数据，不依赖紧化的选法与回路的代表（[Schmid]；PDF p.99）。

**本书用法。** Cox–Katz 把「单值性定理」当作 [Landman] 的黑箱结论（PDF p.98，只引不证），而 F_lim 的存在性另立 [Schmid] 幂零轨道定理（PDF p.99）——两条定理分工明确，标准教材常把后者也归到「单值性定理」名下，本书不合并；此外本书把 T_j 又称 Picard–Lefschetz 变换，而本库把后者专指 T(γ)=γ±⟨γ,δ⟩δ 的公式，本卡按本书口径保留两种叫法，仅 §4 用到矩阵层面。

## 4. 最小例子（能算出）

**椭圆曲线的节点退化（n=1）。** 取 E_t: y²=x(x−1)(x−t)，t∈Δ*=Δ∖{0}；t=0 时退化为节点三次曲线，n=1、rk H¹(E_t)=2。记 δ 为**消失圈**（t→0 时收缩为节点），γ 为补圈，取定取向使下述矩阵成立。

**(a) 单值性与 N 的具体矩阵。** Picard–Lefschetz：T(δ)=δ，T(γ)=γ+δ。在基 (δ,γ) 下（列向量为像）：
T=[[1,1],[0,1]]，N=T−I=[[0,1],[0,0]]，N²=[[0,0],[0,0]]。
于是 trace(T)=2、det(T)=1、特征多项式 (λ−1)²，T 幺幂；又 N²=0 故 log T=N−N²/2+⋯=N 为精确等式。

**(b) 定理的检验。** n=1 时单值性定理要求某个 m 使 (T^m−I)^{n+1}=(T^m−I)²=0；取 m=1：(T−I)²=N²=0 ✓。本例 m=1，幺幂指数（index of unipotency）实际为 2 = n+1（因 N≠0）。

**(c) 权滤过与极限 Hodge 数。** 由式 (5.4)（n=1）：W_0=im(N¹)=Cδ；W_1=im(N⁰)∩ker N=ker N=Cδ；W_2=H¹(E_t)。故 dim gr₀^W=1、dim gr₁^W=0、dim gr₂^W=1。按性质 ③，F_lim 在 gr₀ 上给权 0、在 gr₂ 上给权 2 的 Hodge 结构：gr₀ 型 (0,0)，gr₂ 型 (1,1)。极限 Hodge 数为 h^{0,0}=h^{1,1}=1（**注意不是**光滑纤维的 h^{1,0}=h^{0,1}=1）；F_lim^1=Cγ，F_lim^0=H¹，F_lim^2=0，即权 0⊕权 2 的 Hodge–Tate 型。

**(d) 周期的具体数字。** 局部模型 uv=t（节点邻域坐标），取 ω=du/u、消失圈 δ={|u|=|v|=√ε}（ε=|t|），则
∮_δ ω=∫_0^{2π} i dθ=**2πi**，归一化 (1/2πi)∮_δ ω=**1**。
N 的整数矩阵元 1 正是这个归一化周期。另一周期含对数：y_γ=(1/2πi)log t·∮_δω+h(t)=log t+h(t)（h 单值解析），绕行 t↦e^{2πi}t 使 y_γ↦y_γ+2πi=y_γ+y_δ，与 (a) 的 T 一致；t=(1/2πi)log q 的镜像坐标也由此来（§6.3，PDF p.172）。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | 单值性定理：存在整数 m≥1 使 (T_j^m−I)^{n+1}=0；故 T_j 拟幺幂、特征值全为单位根，幺幂指数 ≤ n+1 | PDF p.98，[Landman] | 中译作 m>0、英文 OCR 作 m≥0，见 §11 |
| 2 | 幂零轨道定理：F^p 有典范延拓 F̄^p，F_lim^p=F̄^p\|_0 存在，且 N_j(F_lim^p)⊂F_lim^{p−1} | PDF p.99，[Schmid] | 定义 7–8；F_lim 由 p 与 N_j 共同决定 |
| 3 | 式 (5.3)：∇̄_{δ_j}=−(1/2πi)N_j（δ_j=z_j∂/∂z_j），由截面的 exp 公式直接算出 | PDF p.99 | 详见 §6 D6 |
| 4 | 权滤过三性质：①N(W_k)⊂W_{k−2}；②N^k:W_{n+k}/W_{n+k−1}≅W_{n−k}/W_{n−k−1}；③F_lim 在 W_k/W_{k−1} 上给权 k 的 Hodge 结构 | PDF p.99，式 (5.4) | ③ 即 (W_•,F_lim) 为混合 Hodge 结构 |
| 5 | T 幺幂 ⇔ Res(∇) 幂零；Res 特征值 λ∈Q∩[0,1)；T 的特征值为 e^{−2πiλ}；重根给 log 项 | PDF p.99–101，[Deligne1] | 与指标方程配合：CY 三维判据见 §5.2 命题（PDF p.102–103） |
| 6 | CY 三维最大幺幂时 LMHS 是 Hodge–Tate：W_6/W_5=H^{3,3}，F_lim^p⊕W_{2p−1}=H³ | PDF p.103 | 得 Ω(0),NΩ(0),N²Ω(0),N³Ω(0) 为基 |

## 6. 推导流程（D1…D8）

- **D1 紧化与边界。** 把族平坦化，取 S̄ 光滑紧化使 D 正规交叉（§5.1.1–5.1.3，PDF p.97–98）；[Deligne1] 给出 F^0 的典范延拓 F̄^0。
- **D2 单值性表示。** 对每个 j 取小回路 γ_j，沿 [0,1] 作 ∇-平坦延拓得 T_j=ρ([γ_j])，其像给出单值群（PDF p.98）。
- **D3 拟幺幂。** 引用 [Landman]：存在整数 m≥1 使 (T_j^m−I)^{n+1}=0，故 T_j 拟幺幂、特征值为单位根（PDF p.98）。本书不证。
- **D4 去掉有限阶部分。** 局部基变换 t=s^m 后 T_j^m 成为新的单值性，此刻 T_j 幺幂；N_j=log T_j 为有限和且幂零（§5.1.4 假设，PDF p.99；[Deligne1]）。这一步是「拟幺幂 ⇒ 幺幂」的唯一成本。
- **D5 多变量与 F_lim。** 由 [Schmid] 幂零轨道定理：F̄^p 存在，F_lim^p=F̄^p|_0 存在且 N_j(F_lim^p)⊂F_lim^{p−1}；δ_j=z_j∂/∂z_j 时 Griffiths 横截性 ∇̄_{δ_j}(F̄^p)⊂F̄^{p−1} 给出线性映射 N_j:F_lim^p/F_lim^{p+1}→F_lim^{p−1}/F_lim^p（PDF p.99）。
- **D6 延拓与 N 的桥梁。** 对平坦多值 s，s̃=exp(−(1/2πi)Σ_j log(z_j)N_j)s 是 F̄^0 的截面；沿 δ_j 求导时 log(z_j) 的导数乘 z_j 恰为 1，得 ∇̄_{δ_j}s̃=−(1/2πi)N_j s̃，即式 (5.3)（PDF p.99）。
- **D7 权滤过。** 取 a_j>0、N=Σa_jN_j，按式 (5.4) 定义 W_•；逐项验证 N(W_k)⊂W_{k−2} 与 N^k:gr_{n+k}^W≅gr_{n-k}^W（PDF p.99；一般项证明见 [Griffiths2]）。
- **D8 结论与特化。** 性质 ③ 表明 gr_k^W 带权 k 的纯 Hodge 结构，故 (W_•,F_lim) 是混合 Hodge 结构（PDF p.99）；n=3 最大幺幂时由 N³≠0 得 W_5=ker N³、W_6=H³，再用 F_lim^p⊕W_{2p−1}=H³ 得 Hodge–Tate（PDF p.103）。

## 7. 常见误解与反例（≥2）

- **M1「单值性定理是说单值性平凡（基域单连通、回路不产生作用）」**——名字误导。定理内容是局部单值性**拟幺幂**，不是「没有单值性」。反例：E_t:y²=x³+t（t≠0，t=0 为尖点退化）的单值性不平凡（见 M2），却满足定理。
- **M2「拟幺幂就是幺幂（T^m=I 型）」**——定理只保证某个 T^m 幺幂。反例：y²=x³+t 经 t=s⁶ 平凡化，T 的阶为 6（特征值为 e^{±2πi/6}，本原 6 次单位根），T⁶=I 但 T≠I，故 T−I 不幂零；要让 §5.1.4 的公式直接可用必须先做基变换。**单值性定理 ⇒ N=log T 幂零只在幺幂假设下成立。**
- **M3「LMHS 是光滑纤维 Hodge 结构的连续极限，故 h^{p,q} 不变」**——错。§4 例中光滑纤维 h^{1,0}=h^{0,1}=1，而极限 Hodge 数 h^{0,0}=h^{1,1}=1，权重从纯 1 变成 0⊕2；「混合」二字正指这种跨权重的重组。
- **M4「F_lim 就是 F^p 在 t=0 处取值」**——错。F_lim 需要先用 N_j 扭一下（定义 7 的 exp 因子），否则随回路的对数项会出现；反例：§4(d) 中 y_γ 含 log t，不扭就无法在 0 处取值。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999 | p.98（§5.1.3） | 定义 T_j 并陈述单值性定理 [Landman]：(T_j^m−I)^{n+1}=0 |
| Cox–Katz 1999 | p.99（§5.1.4） | 典范延拓、F_lim、式 (5.3)、权滤过 (5.4) 与三条性质 |
| Cox–Katz 1999 | p.99–101（§5.1.5） | 留数 Res(∇)、T 幺幂 ⇔ Res 幂零、指标方程（判据的实际用法） |
| Cox–Katz 1999 | p.101–103（§5.2） | 最大幺幂 (T−I)⁴=0、N³≠0、式 (5.5)、命题 (i)(ii)、Hodge–Tate 特化 |
| SY01-24（Siebert 讲义） | 第 1 章，术语 #18（p.21）、#15（p.18） | #18 作「单值变换」——**冲突：**本书作「单值性」（《_冲突表》T1；§11 C1）。其「单值变换」指 PF 方程解的单值**群**，本书 §5.1.4 讲作用在 W_• 上的**算子** N=log T——**冲突：**对象不同（U2；§11 C2）。#15 作「消失循环」——**冲突：**本书作「消失圈」（T2；§11 C4） |
| SY01-25 资料卡 | 卡 04，§一核心术语、§二文献表 | §一 作「消没圈」（同 T2/§11 C4，见上）；§二 [LTY] 作「极大单值」「极大退化」——**冲突：**本书作「最大幺幂单值性」「最大幺幂边界点」，且该卡未给 MUM 的等价条件，无法逐条比对（§11 C3） |
| Landman 1973 | Trans. Amer. Math. Soc. 181, 89–126 | 单值性定理的原始出处（书引 [Landman]；定理号待核） |
| Schmid 1973 | Invent. Math. 22, 211–319 | 幂零轨道定理（书引 [Schmid]；定理号待核） |
| Deligne 1970 | Équations différentielles à points singuliers réguliers | 正则奇点与典范延拓（书引 [Deligne1]） |
| Deligne 1997（待核） | Local behavior of Hodge structures at infinity, in Mirror Symmetry II | 无穷远处 Hodge 结构的局部行为、Hodge–Tate（书引 [Deligne2]，§6 见 PDF p.128） |

## 9. 前置与后继

- **前置（队列登记）：MS-12**（单值性；本卡撰写时该卡尚未归档）。书内直接前提是 §5.1.1 的 Hodge 结构变分（PDF p.97）与 §5.1.3 的紧化/平坦化（PDF p.98）。
- **后继：** MS-14（消失圈，提供 §4 的局部模型）；MS-06（Picard–Fuchs，指标方程把本定理变成可计算判据）；§5.2 最大幺幂卡（式 (5.5)）；§6.2–6.3 镜像映射卡（F_lim 与 t=(1/2πi)log q）；第 6 章 A 模型 Hodge 结构变分卡（F^d_lim）；MS-19（q 与 t 的换算，U3）。
- **与 SY01-25 的接口：** 其 §五 明言非原文内容，本卡不引；§三/§四的勘误与存疑本卡只作线索，未并入。

## 10. 形式化接口（Lean 可 sorry）

```lean
-- 只列接口与关键假设，证明一律 sorry；Mathlib 无 Hodge/混合 Hodge 结构（版本待核）
import Mathlib.LinearAlgebra.Matrix.GeneralLinearGroup
import Mathlib.Analysis.Complex.Basic

namespace MirrorSymmetry

/-- 单值性定理 [Landman] 的结论形态（书 PDF p.98）：存在 m ≥ 1 使 (Tᵐ − I)^{n+1} = 0。 -/
def QuasiUnipotent (n : ℕ) {r : ℕ} (T : Matrix (Fin r) (Fin r) ℂ) : Prop :=
  ∃ m : ℕ, 0 < m ∧ (T ^ m - 1) ^ (n + 1) = 0

/-- 极限混合 Hodge 结构的接口：H 上 N 幂零，W 是单值性权滤过，F 是极限 Hodge 滤过。
    三条性质取自书 PDF p.99（式 (5.3)–(5.4)）；此处只写可检查的代数部分。 -/
structure LimMHS (n : ℕ) where
  H : Type
  [instAdd : AddCommGroup H]
  [instMod : Module ℂ H]
  T : H →ₗ[ℂ] H                            -- 单值性 T_j
  N : H →ₗ[ℂ] H                            -- N_j = log T_j
  W : ℤ → Submodule ℂ H                    -- 单值性权滤过 W_•
  F : ℤ → Submodule ℂ H                    -- 极限 Hodge 滤过 F_lim
  W_mono : Monotone W
  N_nilpotent : N ^ (n + 1) = 0            -- 幺幂 T ⇒ N^{n+1}=0
  N_lowers_W : ∀ k, Submodule.map N (W k) ≤ W (k - 2)   -- 性质 ①
  gr_Hodge : ∀ k, W k ≤ W (k + 1)          -- 性质 ③ 的占位：gr_k 上带权 k 的 Hodge 结构

/-- 书 PDF p.98：单值性定理（引用 Landman 1973，证明不在本书）。 -/
theorem monodromy_theorem (n : ℕ) {r : ℕ} (T : Matrix (Fin r) (Fin r) ℂ)
    (hT : IsUnipotent T) : QuasiUnipotent n T := by sorry

/-- 书 PDF p.99：极限 Hodge 滤过存在（引用 Schmid 1973 幂零轨道定理）。 -/
theorem limiting_hodge_exists (n : ℕ) (D : LimMHS n) : True := by sorry

/-- 式 (5.3)：∇̄_{δ_j} = −(1/2πi) N_j，此处以抽象联络与 N 的等式占位。 -/
theorem nabla_eq_N (n : ℕ) (D : LimMHS n) (δ : ℤ → ℂ) : True := by sorry

end MirrorSymmetry
```

## 11. 待核清单

- [ ] **C1 术语级冲突（SY01-24，#18 p.21）**：SY01-24 作「单值变换」，本书作「单值性」（《_冲突表》T1；`工程文件/校对/术语对照与冲突.md` 第 21 行已裁定本书用「单值性」）。本卡按裁定用「单值性」，只登记差异、不判优劣。→ §8 第 5 行。
- [ ] **C2（U2）单值性作用的对象**：SY01-24 的「单值变换」指 Picard–Fuchs 方程解的单值**变换群**；本书 §5.1.4 讲的是作用在权滤过上的**算子** N=log T（及 T 本身）。属对象不同而非谁错，交 MS-12/13 显式区分。→ §8 第 5 行。
- [ ] **C3（SY01-25 §二）「极大单值/极大退化」** vs 本书「最大幺幂单值性」「最大幺幂边界点」；其 [LTY] 条的精确条件未取到原文，无法确认是否与本书 (T−I)³≠0 / N³≠0 等价。→ §8 第 6 行。
- [ ] **C4（T2）「消没圈/消失循环」**：SY01-25 作「消没圈」、SY01-24 作「消失循环」，本书作「消失圈」（《_冲突表》T2 裁定「消失圈」）。→ §8 第 5–6 行。
- [ ] 单值性定理的 m：英文 OCR p098 作「m ≥ 0」，中译作「m > 0」；m=0 时 T⁰−I=0 使论断无意义，标准陈述应为 m ≥ 1。待对照原书印刷页 p.75 与 Landman 1973 原文定理号（《_冲突表》§三 已登记）。→ §5 第 1 行。
- [ ] Landman 1973（Trans. AMS 181, 89–126）的定理号/页码未核；本书只引作者名，未给编号。
- [ ] Schmid 1973（Invent. Math. 22, 211–319）幂零轨道定理的定理号未核；同上。
- [ ] 式 (5.4) 的一般项公式本书未给全（只写 W_0,W_1,W_2,W_{2n−1}，其余指向 [Griffiths2]）；「W_• 与 a_j>0 的取法无关」书中未证，需从 [Griffiths2] 或 Cattani–Kaplan–Schmid 1986 取原文核对。→ §3 定义 9、§7 M4。
- [ ] §5.1.5 中译「T 的特征值为 exp(−2πiλ)」与 OCR p100 的写法（同 MS-06 §11 已登记）符号不一致，影响 §5 第 5 行表述，暂按译本。
- [ ] §5.2 中「F_lim^p⊕W_{2p−1}=H³ ⇒ Hodge–Tate」只核到 PDF p.103；Hodge–Tate 结构的一般定义本书在何处给出、[Deligne2] 引文页码待核。
- [ ] §4 中 Picard–Lefschetz 公式 T(γ)=γ+δ 的符号与 §5.2 式 (5.5) 的矩阵方向（周期向量取转置作用）约定是否一致，待逐式核对；本卡固定 ⟨γ,δ⟩=1 并只用于演示矩阵结构。
- [ ] chapter06.tex:1200 的 F^d_lim（A 模型 Hodge 结构变分）书内页码未核（章起点 \SourcePage{136}）。
- [ ] 术语缺口：SY01-24（70 条）与 `glossary.tsv` 均未收「极限混合 Hodge 结构」「单值性权滤过」「幂零轨道定理」，建议补词条（交术语表维护）。
