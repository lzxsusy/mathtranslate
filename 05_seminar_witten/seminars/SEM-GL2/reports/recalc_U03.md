# U03 复算报告

对象：Kapustin–Witten 2006 §4「Compactification And Geometry Of Hitchin's Moduli Space」，印刷 pp.38–56（§4 标题在 `p039.txt:19`；§5 标题在 `p057.txt:17`）。页锚约定：印刷页 N ↔ `p{N+1:03d}.txt`。
本报告只做复算：五节各按「问题 → 原文依据 → 推导 → 数值/特例检验 → 与报告比 → 判定」写，「发现的问题清单」在末，附录 6 段 python 各自可独立跑出正文引用的数。

记号约定（与原文 (4.3)–(4.11) 一致；原文把 bar 印在下标上）：
z 为 C 的复坐标；A = A_z dz + A_z̄ dz̄，φ 为 ad(E)-值复一形式，φ_z、φ_z̄ 为其分量；D = d_A；F 为 A 的曲率。
D_z = ∂_z + [A_z, ·]，D_z̄ = ∂̄ + [A_z̄, ·]。ε 为 ad(E)-值零形式（无穷小规范参数）。

---

## 一、三组矩映射：从 (4.1) 到 (4.11)

### 1.1 问题
把 Hitchin 方程 (4.1) 的三个方程 F−φ∧φ=0、Dφ=0、D*φ=0 逐个识别为 (4.11) 中哪个矩映射的零点，并把 μ_J、μ_K 的**符号与组合方式**钉死（这是本单元最容易抄错的一处）；再说明复化商 G_ℂ 与实商 G 各在哪个复结构下使用。

### 1.2 原文依据
- (4.1)：F−φ∧φ=0，Dφ = D*φ = 0（印刷 p.39，`p040.txt` 第 1–9 行）。
- 母空间 W 与平直超凯勒度量 (4.2)；三个复结构 (4.3)(4.4)(4.5)；四元数关系 I^tJ^t = −J^tI^t = −K^t（印刷 pp.41–43，`p042.txt`–`p044.txt`）。
- 三个辛形式 (4.8)、复辛形式 (4.9)（印刷 p.44，`p045.txt`；式子在页图 PDF 第 45 页核对过）。
- 矩映射 (4.11)（印刷 p.46，`p047.txt`；页图 PDF 第 47 页核对）：
  μ_I = −(1/2π)∫_C Tr ε(F − φ∧φ)，
  μ_J = −(1/2π)∫_C |d²z| Tr ε(D_zφ_z̄ + D_z̄φ_z)，
  μ_K = −(i/2π)∫_C |d²z| Tr ε(D_zφ_z̄ − D_z̄φ_z)。
- 复矩映射 (4.20)：ν_I = μ_J + iμ_K = −(1/π)∫|d²z| Tr ε D_z̄φ_z，"holomorphic in structure I … depends only on A_z̄ and φ_z"（印刷 p.49，`p050.txt`）；(4.21)：ν_J = μ_K + iμ_I = −(i/2π)∫Tr ε F，F 是 𝒜 = A+iφ 的曲率（印刷 p.51，`p052.txt`）。
- 两种商操作 (I)/(II)（印刷 pp.49–51，`p050.txt`–`p052.txt`）。

### 1.3 逐步推导
**第 1 步：把 (4.1) 拆成 C 上的分量方程。** C 是复维 1，2-形式只有 (1,1) 分量，故
- (Dφ)_{zz̄} = D_zφ_z̄ − D_z̄φ_z（dz∧dz̄ 系数），(Dφ)_{z̄z} = −(Dφ)_{zz̄}，其余分量因 dz∧dz=0 恒为零。因此 **Dφ = 0 ⟺ D_zφ_z̄ − D_z̄φ_z = 0**。
- *φ = −i φ_z dz + i φ_z̄ dz̄（Hodge *，C 上 *dz = −i dz、*dz̄ = i dz̄），于是 (D*φ)_{zz̄} ∝ D_zφ_z̄ + D_z̄φ_z，**D*φ = 0 ⟺ D_zφ_z̄ + D_z̄φ_z = 0**。
- φ∧φ = (φ_zφ_z̄ − φ_z̄φ_z)dz∧dz̄ = [φ_z, φ_z̄]dz∧dz̄，故 **(F−φ∧φ = 0) ⟺ F_{zz̄} − [φ_z, φ_z̄] = 0**。

**第 2 步：矩映射由 ι_{V(ε)}ω = δμ 定出。** V(ε) 为无穷小规范变换（δA = −Dε，δφ = [ε,φ]）。把 (4.8) 的三个 ω 依次与 V(ε) 缩并（分部积分 + Tr 循环性），得到的形式必然是上面三个实函数的线性组合：
μ_I ∝ ∫Tr ε(F_{zz̄} − [φ_z,φ_z̄])，μ_J ∝ ∫|d²z|Tr ε(D_zφ_z̄ + D_z̄φ_z)，μ_K ∝ ∫|d²z|Tr ε(D_zφ_z̄ − D_z̄φ_z)。
即：**μ_I 管 F−φ∧φ；μ_J 管 D*φ；μ_K 管 Dφ**（各自差一个实系数）。

**第 3 步：用 (4.20) 的「I-全纯性」定符号。** 记 a := D_zφ_z̄，b := D_z̄φ_z。按 (4.11) 的符号，
μ_J + iμ_K = −(1/2π)∫[(a+b) + i·i(a−b)] = −(1/2π)∫[(a+b) − (a−b)] = −(1/π)∫ b = −(1/π)∫D_z̄φ_z，
正是 (4.20) 的 ν_I，而 b = D_z̄φ_z 只含 A_z̄ 与 φ_z，正是复结构 I 的全纯量。若把 μ_K 整体反号（即写成 −(i/2π)∫(D_z̄φ_z − D_zφ_z̄)），则 μ_J + iμ_K = −(1/π)∫ a = −(1/π)∫D_zφ_z̄，那是 I 下的**反全纯**量，与 (4.20) 矛盾。于是符号被唯一钉死：
**μ_K = −(i/2π)∫|d²z|Tr ε(D_zφ_z̄ − D_z̄φ_z) = +(i/2π)∫|d²z|Tr ε(D_z̄φ_z − D_zφ_z̄)**；
并且 **ν_I = μ_J + iμ_K ∝ D_z̄φ_z**（零点 ⟺ ∂̄_Aφ_z = 0，Hitchin pair 全纯条件），
**ν_J = μ_K + iμ_I ∝ (F−φ∧φ) + i(Dφ) = F_{A+iφ}**（零点 ⟺ 𝒜 = A+iφ 平坦，G_ℂ 平坦丛）。

**第 4 步：G 与 G_ℂ 的商在哪用。** 超凯勒商 W///G 有两种读法，取决于固定哪个复结构：
- **复结构 I**：{ν_I = 0} 上除 G_ℂ（操作 (II)）得 Hitchin pairs (E, φ)，φ = φ_z dz ∈ H⁰(C, K_C⊗ad E)；{μ_I = 0} 上除 G（操作 (I)）得 M_H；[20] 保证二者一致（稳定对一一对应，即 Kobayashi–Hitchin 型定理）。所以 **I 下用 G_ℂ 商得到的全纯对象 = Higgs bundle 模空间**。
- **复结构 J**：{ν_J = 0} 上除 G_ℂ 得 Y₀ = Hom(π₁(C), G_ℂ)/G_ℂ（平坦 G_ℂ 丛）；{μ_J = 0}（即 D*φ=0）上除 G 得 M_H；Corlette–Donaldson 定理给出 M_H ≅ Y（稳定同态模空间）(印刷 pp.50–51)。
- 一般 I_w（w ≠ 0,∞）：{复联络 A_z̄ − wφ_z̄, A_z + w⁻¹φ_z 平坦} 除 G_ℂ 都给出同一个 Y (印刷 p.52, `p053.txt`)。故 **复化商不是只属于某一个复结构，而是「对哪个复结构，就在那个结构的复矩映射零点上除 G_ℂ」**；实商总是配 μ_I 或 μ_J。

### 1.4 数值/特例检验
- 令 φ = 0：μ_J = μ_K = 0 自动成立 ⇒ M ⊂ M_H 在 J、K 下是 Lagrange 子流形，与原文印刷 p.52 一致（`p053.txt:31`："it is Lagrangian, since φ = 0 implies δφ = 0 and hence μ_J = μ_K = 0"）✓。
- 数值验证（附录 §A1）：取 360 组随机复 a、b，逐组检验 μ_J + iμ_K = −(1/π)∫·2b（即 ∝ D_z̄φ_z）与 μ_J − iμ_K = −(1/π)∫·2a；同时检验「报告版符号」会让组合落到 a 上（反全纯）——全部通过。
- 解析自洽：ν_I = μ_J + iμ_K 与 ν_J = μ_K + iμ_I 的表达式代入 (4.11) 后分别复现 (4.20)、(4.21) 右侧的常数（1/π 与 i/2π）✓。

### 1.5 与报告比
报告 §2.1.3 抄的 (4.11) 中，μ_K 写作 **−(i/2π)∫(D_z̄φ_z − D_zφ_z̄)**，与原文**反号**（报告见 `report_v1.md:142`）；随后 `report_v1.md:144` 的「核对」把 μ_J = 0 与 μ_K = 0「相加、相减」说成给出 D_z̄φ_z=0 与 D_zφ_z̄=0、"合起来恰是 D*φ=0"，也与原文逻辑不符（μ_J=0 单独就是 D*φ=0，不需要组合）。报告 §2.2.2 里「置 μ_J = 0（即 D*φ = 0）」是对的，所以是**同一份报告内部符号不一致**。

### 1.6 判定
**报告错，正确是 μ_K = −(i/2π)∫(D_zφ_z̄ − D_z̄φ_z)（即 +μ_K 与报告反号）；组合方式为 ν_I = μ_J + iμ_K ∝ D_z̄φ_z（I 全纯）、ν_J = μ_K + iμ_I ∝ F_{A+iφ}（J 全纯）；G_ℂ 商用在复矩映射零点、G 商用在实矩映射零点，I 下得 Hitchin pairs，J 下得平坦 G_ℂ 丛。** 三个方程与矩映射的对应：μ_I ↔ F−φ∧φ，μ_J ↔ D*φ，μ_K ↔ Dφ。

---

## 二、维数账

### 2.1 问题
自算 dim_ℂ M_H，对照原文 (4.22) 一带（印刷 p.49）的说法，并代入 G=SU(2)、g=2 给具体数；再指出报告若只写"维数是…"缺什么。

### 2.2 原文依据
- 无编号陈述：g > 1 时 M_H 是复维 **(2g−2)dim G** 的复流形，奇点对应可约解（印刷 p.39，`p040.txt:13`）。
- (4.24)：Σ_{i=1}^{r}(2d_i − 1) = dim G（d_i 为 G 的不变多项式次数）。
- dim H⁰(C, K_C^n) = (2n−1)(g−1)（印刷 p.54，`p055.txt:1`）。
- (4.25)：dim F = dim B = ½dim M_H = (g−1)dim G（印刷 p.54）。
- 第二纤维化 T*M ⊂ M_H 稠密（印刷 p.53，`p053.txt`–`p054.txt`）。
- 注：**(4.22) 不是维数公式**，它是单值矩阵 [[α, β], [0, α⁻¹]]（印刷 p.51），任务单把它当成维数出处是记错了；维数出处在 p.39。

### 2.3 逐步推导
三条互相独立的路线，全部给出同一答案。

**路线 A（Riemann–Roch，算 dim M）。** G-丛模空间 M 在稳定点处的切空间 = H¹(C, ad E)，且稳定 E 满足 H⁰(C, ad E) = 0（无非平凡自同态），故
dim_ℂ M = h¹(C, ad E) = −h⁰ + h¹ = −deg(ad E) + rk(ad E)(g−1) = (g−1)dim G。
（用 RR：h⁰ − h¹ = deg + rk(1−g)，deg(ad E) = 0。）

**路线 B（T*M 稠密）。** φ 的取值正好是 M 的余切空间 H⁰(C, K_C⊗ad E)（Serre 对偶把 H¹ ≅ H⁰(K⊗ad) 的对偶），所以 (E, φ) 全体 = T*M，且 T*M 在 M_H 中的补集高余维（印刷 p.53）。于是
dim_ℂ M_H = 2 dim_ℂ M = **2(g−1)dim G = (2g−2)dim G**。

**路线 C（Hitchin 纤维化自洽）。** B = ⊕_i H⁰(C, K_C^{d_i})，每项维数 (2d_i−1)(g−1)，用 (4.24)：
dim_ℂ B = Σ_i (2d_i−1)(g−1) = (g−1)Σ_i(2d_i−1) = (g−1)dim G = ½dim_ℂ M_H，
与 (4.25)「dim F = dim B = ½dim M_H」及路线 A、B 完全一致 ✓。

**关于「维数 = dim W − 4dim G」这个朴素算法。** 超凯勒商在有限维的规则是 dim_ℝ(X///H) = dim_ℝ X − 4dim H（三个实矩映射 3dim H，再加规范固定 dim H）。但 W 是无穷维（A、φ 是 C 上的场），W///G 中 G 也是无穷维映射群，「dim W − 4dim G」是形式上的 ∞−∞，**不能用**；正确的无穷维版本要用形变复形（上面路线 A）或 Atiyah–Hitchin 型指标计算。报告只引 p.39 的结论、不做这件事（见 E3）。

### 2.4 数值/特例检验
- G = SU(2)（dim G = 3），g = 2：dim_ℂ M_H = (2·2−2)·3 = **6**（实维 12）；dim_ℂ M = 3；dim_ℂ B = dim_ℂ F = 3。核对 (4.24)：SU(2) 只有 d₁ = 2，(2·2−1) = 3 = dim SU(2) ✓；(4.25)：3 = ½·6 ✓。
- 其它例子（附录 §A3 全表）：SU(3), g=2 → 2·1·8 = 16；G₂, g=2 → 2·14 = 28；E₈, g=2 → 2·248 = 496；SU(2), g=3 → 12。
- 对每个单李群用其不变多项式次数验证 Σ(2d_i−1) = dim G（附录 §A3 打印全部 OK），这是 (4.24) 的独立核对。

### 2.5 与报告比
报告 `report_v1.md:49` 直接引 p.39 的结论「复维 (2g−2)dim G」，`report_v1.md:275` 用 dim H⁰(K^n) = (2n−1)(g−1) 与 (4.24) 得到 dim B = (g−1)dim G = ½dim M_H——这一步对，但**只组织了路线 C**，没有路线 A（RR）与路线 B（T*M）的独立验证，也没有给 SU(2)、g=2 的具体数，更没有说明「dim W − 4dim G 在无穷维下不可用」。任务单要求的「自算 + 具体数」在报告里缺位。

### 2.6 判定
**正确值 dim_ℂ M_H = (2g−2)dim G；SU(2)、g=2 时 = 6（实 12），dim B = dim F = 3。报告结论数字对，但推导只有一条路线、无具体代入，属「只写维数是…而没给依据」（见 E3）。任务单把 (4.22) 当维数出处是笔误。**

---

## 三、复结构 I/J/K 的显式形式与全纯 2-形式

### 3.1 问题
给出 ω_I、ω_J、ω_K 的构造（谁和谁配对）；验证 ω_J + iω_K 是全纯 2-形式（注意：是复结构 **I** 下的，不是 J 下的，见 3.5/题面勘误 N1）；说明为什么 I 下的全纯结构就是 Hitchin 方程的解。

### 3.2 原文依据
- (4.8)：ω_I = −(i/2π)∫|d²z|Tr(δA_z̄∧δA_z − δφ_z̄∧δφ_z) = −(1/4π)∫Tr(δA∧δA − δφ∧δφ)；
  ω_J = (1/2π)∫|d²z|Tr(δφ_z̄∧δA_z + δφ_z∧δA_z̄)；
  ω_K = (i/2π)∫|d²z|Tr(δφ_z̄∧δA_z − δφ_z∧δA_z̄) = (1/2π)∫Tr δφ∧δA。
- (4.9)：Ω_I = ω_J + iω_K = (1/π)∫|d²z|Tr δφ_z∧δA_z̄；Ω_J = ω_K + iω_I = −(i/4π)∫Tr δ𝒜∧δ𝒜（原文简写 δA∧δA，须读作复化联络 𝒜 = A+iφ）；Ω_K = ω_I + iω_J。
- 型：ω_I 对 I 是 (1,1)；Ω_I 对 I 是 (2,0)，其余轮换；ω_I、ω_K 不依赖 C 的复结构，ω_J 依赖；Ω_I、Ω_K 依赖 C 的复结构，Ω_J 不依赖（印刷 p.44，`p045.txt`）。
- 依赖模式的判据：ω_I、ω_K 可写成坐标无关形式（不含 z、z̄ 的区分），ω_J 必须各取一个分量叉乘。

### 3.3 逐步推导
**第 1 步：确定各复结构下的全纯坐标。** 由 (4.6)：I_w 的全纯变量是 A_z̄ − wφ_z̄ 与 A_z + w⁻¹φ_z，w = −i ↔ J，w = 1 ↔ K，w → 0 给 I。
- I：w = 0，全纯坐标为 **(A_z̄, φ_z)**。交叉证据三条：Ω_I = (1/π)∫δφ_z∧δA_z̄ 必须是 (2,0) 型；原文 p.49 说 ν_I 只依赖 A_z̄ 与 φ_z；原文 p.55 说 H_a 是 φ_z 的函数、而 φ_z「is conjugate to A_z̄」（`p056.txt:7`，bar 在文本层丢失）。
- J：全纯坐标 **(A_z̄ + iφ_z̄, A_z + iφ_z)**。
- K：全纯坐标 **(A_z̄ − φ_z̄, A_z + φ_z)**。

**第 2 步：按型配对。** 在 I 下 δφ_z、δA_z̄ 是 (1,0)，δφ_z̄、δA_z 是 (0,1)。于是
- ω_I = −(i/2π)∫(δA_z̄∧δA_z − δφ_z̄∧δφ_z)：(1,0)∧(0,1) 型 ⇒ **(1,1)** ✓（Kähler 形式应有的型）。
- ω_J = (1/2π)∫(δφ_z̄∧δA_z + δφ_z∧δA_z̄)：(0,1)∧(0,1) = (0,2) 项 + (1,0)∧(1,0) = (2,0) 项 ⇒ 混型；ω_K = (i/2π)∫(δφ_z̄∧δA_z − δφ_z∧δA_z̄) 同样是混型，但两项系数带 i。

**第 3 步：组合相消。** 记 X := δφ_z∧δA_z̄（(2,0)），Y := δφ_z̄∧δA_z（(0,2)），则
ω_J = (1/2π)(Y + X)，ω_K = (i/2π)(Y − X)，故
ω_J + iω_K = (1/2π)(Y + X) + i·(i/2π)(Y − X) = (1/2π)(Y + X − Y + X) = **(1/π)X = (1/π)∫|d²z|Tr δφ_z∧δA_z̄ = Ω_I** ✓
（(0,2) 部分系数 1/2π + i·i/2π = 0 精确相消，(2,0) 部分 1/2π + i·(−i/2π) = 1/π）。这既复现 (4.9) 的系数 1/π，又证明 Ω_I 是 I 下的纯 (2,0) 形式 ⇒ 全纯辛形式。

**第 4 步：轮换。** Ω_J = ω_K + iω_I：在 J 下，u := A+iφ 的两个分量 u_z = A_z+iφ_z、u_z̄ = A_z̄+iφ_z̄ 是全纯的，代入得
Ω_J = −(1/2π)∫|d²z|Tr δu_z∧δu_z̄ = −(i/4π)∫Tr δ𝒜∧δ𝒜（𝒜 = A+iφ），是 J 下的纯 (2,0) 形式 ✓；同理 Ω_K 是 K 下的 (2,0)。三个 Ω 与三个 ω 的关系就是四元数结构的标准轮换。

**第 5 步：为什么 I 下的全纯结构 = Hitchin 方程解。** 复结构 I 把 W 分成「A_z̄ 与 φ_z 是全纯方向、A_z 与 φ_z̄ 是反全纯方向」。在 I 下，复矩映射 ν_I = 0 ⟺ D_z̄φ_z = 0，即 ∂̄_Aφ = 0：给定 ∂̄_A 就得全纯丛 E，φ_z dz 是 H⁰(C, K_C⊗ad E) 的截面——**(E, φ) 正是 Hitchin pair**。剩下的 μ_I = 0（F−φ∧φ=0）不是全纯方程，而是「给定全纯等价类后选取 Hermitian 度规」的实方程，由 Kobayashi–Hitchin/[20] 型定理对每个稳定对唯一可解。因此
M_H = {稳定 Hitchin pairs (E, φ)} /（复规范变换） 恰是 M_H 在复结构 I 下的全纯描述；Ω_I = (1/π)∫δφ_z∧δA_z̄ 就是这套全纯坐标下的辛形式（与 J 下的 (A+iφ) 全纯坐标给出另一套全纯描述 Y 相对偶）。

### 3.4 数值/特例检验
- 系数相消的精确算术（附录 §A2）：(2,0) 系数 1/2π + i·(−i/2π) = 1/π；(0,2) 系数 1/2π + i·(i/2π) = 0，打印为 0.0 ✓。
- 型计数复核：若按题面把 ω_J + iω_K 当作 J 下的形式，则 ω_J 在 J 下是 (1,1) 型（原文明说），(1,1) 不可能出现在 (2,0) 形式里——这构成一个纯型论的归谬，反证正确复结构是 I。
- 依赖模式自洽：Ω_I 含 dz 与 dz̄ 各一（通过 δA_z̄、δφ_z 的坐标依赖），依赖 C 的复结构 ✓；Ω_J = −(i/4π)∫Trδ𝒜∧δ𝒜 用坐标无关形式写成 ⇒ 不依赖 C 的复结构 ✓，与原文 p.44 的三条依赖声明逐条相符。

### 3.5 与报告比
报告 `report_v1.md:126` 写「Ω_I = ω_J + iω_K、…，Ω_I 对 I 是 (2,0) 型」——**正确**；`report_v1.md:187` 说「I 的全纯坐标正是 A_z̄ 与 φ_z」——**正确**。但 `report_v1.md:126` 把 (4.9) 的 Ω_J 照抄成 −(i/4π)∫Tr δA∧δA 而未注明这里 A 必须是**复化联络 𝒜 = A+iφ**（否则 Ω_J = ω_K + iω_I 不成立；见 E4）。另外报告没有从型论上验证 ω_J + iω_K 的相消，只引原文结论。

### 3.6 判定
**任务单的表述有一处错（N1）：ω_J + iω_K = Ω_I 是复结构 I 下的全纯 2-形式，不是 J 下的；J 下的全纯 2-形式是 Ω_J = ω_K + iω_I。** 报告关于 Ω_I 的型与全纯坐标的描述正确；Ω_J 抄录需补 𝒜 = A+iφ 的说明（E4）。ω_I、ω_J、ω_K 的配对方式见 3.3 第 2、3 步。

---

## 四、Hitchin 纤维化与完全可积

### 4.1 问题
用第一、二节结果算 Hitchin map 的像空间维数与纤维维数；给出「足够多对易哈密顿量」的计数（H^{1,0} 或特征多项式系数）；验证纤维在 Ω_I 下是 Lagrange 子流形（维数 + 闭性论证）。

### 4.2 原文依据
- (4.26)：H_a = ∫_C α_a ∧ Tr φ²，α_a ∈ H¹(C, T_C)（SU(2)，basis a = 1,…,3g−3）；一般 G 用不变多项式 P_i（次数 d_i）：H_{α,i} = ∫_C α P_i(φ)，α ∈ H¹(C, K_C^{1−d_i})（印刷 pp.54–55，`p055.txt`–`p057.txt`）。
- 完全可积：存在 ½dim M_H 个 I-全纯、代数独立、Ω_I-Poisson 交换的函数（印刷 p.54）。
- Poisson 交换的证明（印刷 p.55，`p056.txt:5–11`）：在 W 上 Ω_I 使 φ_z 与 A_z̄ 共轭、φ_z 与自身交换，而 H_a 只含 φ_z；再经 ν_I = 0 与 G_ℂ 商（辛约化保持 Poisson 交换性）下降到 M_H。
- (4.25)：dim F = dim B = ½dim M_H。
- 满射性：SU(2) 时解 Tr φ² = w 是 3g−3 个二次方程对 3g−3 个复变量，一般有 2^{3g−3} 个解（印刷 p.54）。
- Lagrange：纤维在 Ω_I（等价地实辛 ω_J、ω_K）下是 Lagrange 子流形；理由：中间维数的一族 Poisson 交换函数的零点集是 Lagrange（印刷 p.56，`p057.txt:8–15`）。另有 p.52 的特例：M ⊂ M_H 在 J、K 下 Lagrange（φ=0 ⇒ δφ=0 ⇒ μ_J=μ_K=0）。

### 4.3 逐步推导
**第 1 步：像空间维数。** dim_ℂ B = Σ_i dim H⁰(C, K_C^{d_i}) = Σ_i (2d_i−1)(g−1) = (g−1)dim G（用了 (4.24)）；由第二节 dim_ℂ M_H = 2(g−1)dim G，故 dim B = ½dim M_H ✓（(4.25)）。

**第 2 步：纤维维数。** π : M_H → B 满射、B 为 ½dim，故一般纤维复维 = dim M_H − dim B = ½dim M_H = (g−1)dim G（(4.25)）。数值上与 T*M 图像自洽：纤维方向 = φ 的谱数据（B 的坐标），垂直方向 ½dim M_H。

**第 3 步：对易哈密顿量的计数。** 取 B 上**线性坐标**为 H_a。计数：
- 个数 = dim_ℂ B = Σ_i(2d_i−1)(g−1) = (g−1)dim G = ½dim M_H ✓（正好是「可积系统需要一半维数」的数目）。
- SU(2)：Σ 只有一项 (2·2−1)(g−1) = 3g−3，H_a = ∫α_a∧Trφ²，α_a ∈ H¹(C,T_C)，dim H¹(C,T_C) = dim H⁰(C,K²) = 3g−3 ✓（Serre 对偶：H¹(C,T_C) ≅ H⁰(C,K_C²) 的对偶）。
- 代数独立：B 上线性函数在线性无关的 H_a 上独立 ✓。I-全纯：H_a 只含 φ_z，而 φ_z 在 I 下全纯 ✓。Poisson 交换：Ω_I 下 φ_z 与 A_z̄ 共轭、φ_z 之间交换，H_a 不含 A_z̄ ⇒ {H_a,H_b}_W = 0；辛约化（ν_I=0、除 G_ℂ）保 Poisson ⇒ 下降到 M_H 后仍交换 ✓。

**第 4 步：纤维是 Lagrange。** 设 F = π⁻¹(b)，dim_ℂ F = ½dim_ℂ M_H =: n（复维），实维 2n。F 由 n 个方程 H_k − h_k = 0 定义（H_k 为对易哈密顿量、h_k 常数）。
- **闭性**：Ω_I 是 M_H 上的全纯辛形式，dΩ_I = 0——它由 (4.9) 定义且 Ω_I = ω_J + iω_K，而 ω_J、ω_K 是超凯勒结构中的 Kähler 形式，均闭；超凯勒商保证它们下降到 M_H 上仍闭。故 Ω_I 可用来定义辛结构（不闭就没有 Lagrange 可言）。
- **各向同性**：H_k 的哈密顿向量场 X_k 满足 ι_{X_k}Ω_I = dH_k；因 {H_i,H_j} = 0，Ω_I(X_i,X_j) = {H_i,H_j} = 0。这些 X_k 张成 TF（对易流保 F，且一般点处 n 个独立流的轨道就是 F），故 TF 是 Ω_I-迷向的：Ω_I|_{F} = 0。
- **维数**：dim_ℝ F = 2n = dim_ℂ M_H = ½dim_ℝ M_H，已是极大迷向 ⇒ F 是 Lagrange ✓。
- 与实形式的等价：F 在 I 下是全纯子流形（Hitchin 纤维是 I-全纯可积系统的水平集），若 Ω_I|_F = 0，则 (ω_J + iω_K)|_F = 0，实部虚部分别为零 ⇒ ω_J|_F = ω_K|_F = 0，即 F 在实辛 ω_J、ω_K 下也 Lagrange ✓（与 p.56 的「or equivalently」一致）。

### 4.4 数值/特例检验
- SU(2)，g = 2：dim M_H = 6，dim B = dim F = 3 = ½·6 ✓；对易哈密顿量个数 3g−3 = 3 ✓；满射性计数：3 个二次方程、3 个变量 ⇒ 2³ = **8** 个解（附录 §A4 打印）。g = 3：dim M_H = 12，B = F = 6，2⁶ = 64。
- G₂，g = 2：dim M_H = 28，dim B = dim F = 14，对易 Hamiltonians 14 个（Σ(2d−1) = 3+11 = 14 = dim G₂ ✓）。
- 维数自洽：对每个群、每个 g，Σ_i (2d_i−1)(g−1) 都等于 (g−1)dim G（附录 §A4 全表 OK），且 2·dim B = dim M_H。

### 4.5 与报告比
报告关于 (4.25)、½dim M_H 个 H_a、(4.26)、Poisson 交换的四步复述、Lagrange 结论（含「等价地 ω_J、ω_K」）**均与原文相符**（`report_v1.md:275–301`）。报告的缺口是：没有给出 Lagrange 的「闭性 + 各向同性 + 维数」三段论（只引原文两行论证），也没有说明 3g−3 就是 dim B = dim H⁰(C,K²)（报告 `report_v1.md:341` 只写「3g−3 个二次方程给出 2^{3g−3} 个解」，未把这套计数与 (4.25) 的 dim B 挂上）。

### 4.6 判定
**报告在本节基本正确**；补充：像空间维数 (g−1)dim G、纤维维数同、对易哈密顿量个数同（= ½dim M_H），Lagrange 由「dΩ_I = 0（闭）+ 对易 ⇒ 各向同性 + dim F = ½dim M_H ⇒ 极大迷向」给出；SU(2)、g=2 时三数皆为 3，满射性给 8 个解。

---

## 五、T-对偶论证与 S-对偶接口

### 5.1 问题
原文 §4.3（印刷 pp.52–56）是如何在纤维上做 T-对偶的？给一个可算的 U(1) 纤维例子说明 T-对偶前后基/纤维的关系；再检查报告「S-对偶在 M_H 上变成镜像对称」是否在 §4 有支撑（还是提前用了 §5）。

### 5.2 原文依据（先给结论：§4 没有 T-对偶）
- §4.3 全文 `p053.txt:24`–`p057.txt:16`（印刷 pp.52–56）的实际内容只有：M ⊂ M_H 与 T*M 嵌入（p.52–53）、第二纤维化（p.53）、Hitchin 纤维化与 (4.24)(4.25)、满射性（2^{3g−3}）、完全可积 (4.26)、纤维是 Lagrange（p.56）。
- 对 §4 全段（`p039.txt`–`p057.txt`）检索 "T-dual / T dual / SYZ / mirror / S-dual"：**零命中**；"dual" 只作为普通形容词出现一次（p.55 "which is dual to H⁰(C,K²)"）。所以 §4 里没有 T-对偶论证，报告 `report_v1.md:17` 的第 6 条结论「本单元没有 T-对偶论证」**正确**。
- T-对偶/SYZ/镜像的真正出处是 §5：
  - §5.3（印刷 p.70，`p071.txt`）："S-duality implies that the B-model for M_H(G,C) in complex structure J is equivalent to the A-model for M_H(^L G,C) in complex structure K. If we combine S with a transformation I: φ → iφ … we get a mirror symmetry that maps the B-model in complex structure J to the A-model in complex structure J. So the complex manifolds M_H(G,C) and M_H(^L G,C) are a mirror pair in complex structure J."
  - §5.4（印刷 pp.70–74）：S 在底空间上经典作用 Ξ: B → ^L B。
  - §5.5（印刷 p.77，`p078.txt:1–5`）："This picture is SYZ duality between torus fibrations. … the operation S acts by a map Ξ: B → ^L B … together with a T-duality on the corresponding torus fibers. This is the usual SYZ picture of mirror symmetry"；对偶纤维 = G 与 ^L G 的 Hitchin 纤维（unitary 群由 Hausel–Thaddeus 证明，G₂ 由 Hitchin）；p.77 还给出「纤维上的 zerobrane ↔ 对偶纤维上的 brane」。
  - §5.4 开头（印刷 p.73，`p073.txt:16–19`）甚至明说：没有测纤维局域算符的类似物，所以 S-对偶「不可能经典地作用在纤维上」——"It hardly can, given its relation to mirror symmetry!"

### 5.3 逐步推导：U(1) 纤维上的 T-对偶（可算例子）
**第 1 步：单纤维（圆）的 T-对偶。** 半径 R 的圆，取 α′ = 1：动量 p = m/R，缠绕 w = nR，质量谱 ∝ (m/R)² + (nR)²；T-对偶 R → 1/R 交换 (m,n)。复化 Kähler 参数 ρ = B + iA（A 为面积）在 T-对偶下 ρ → 1/ρ…在无 B、方形环面的情形等价于椭圆曲线的复结构参数
τ = iR²（B = 0，方形），T-对偶后 τ′ = i/R² = −1/τ。数值：R = 2（τ = 4i）→ τ′ = i/4（R′ = 1/2 = 1/R）✓；R = 1（τ = i）是自对偶点 τ′ = −1/i = i ✓（附录 §A5 打印）。

**第 2 步：Hitchin 纤维。** Hitchin 纤维 F 是复环面（p.56："orbits are complex tori at least generically"）。对 U(1) 型纤维只需看一个复一维环面 E_τ；对 Γ = π₁(F) 的格 Λ，T-对偶把 Λ 换成对偶格 Λ^∨ = Hom(Λ, ℤ)（用平坦度量等同后），即 E_τ → E_{−1/τ}。基空间不动：T-对偶只作用在纤维上，底空间 B 由 S-对偶通过 Ξ: B → ^L B 映过去（§5.5）。**所以「基/纤维互换」不是 T-对偶的内容**：互换的是纤维环面与其对偶环面；字面上的「基与纤维互换」在 SYZ 里不出现（题面 N3）。
**第 3 步：非阿贝尔情形（SU(2) vs SO(3)）的可算维数。** SU(2) Hitchin 纤维 = 谱曲线 Σ（C 的 4g−4 点分支双覆盖）的 Prym 簇：
Riemann–Hurwitz：2g(Σ) − 2 = 2(2g−2) + (4g−4) ⇒ g(Σ) = 4g−3；
dim Prym = g(Σ) − g = **3g−3** = ½dim M_H(SU(2)) ✓（与 (4.25) 一致）。
对偶群 SO(3) = ^L SU(2) 的纤维是同一条 Σ 的对偶 Prym，维数相同 = 3g−3（Hausel–Thaddeus 的结论）。g = 2：g(Σ) = 5，Prym = 3，dim M_H = 6（附录 §A6 打印）。
**第 4 步：U(1) 的退化情形。** G = U(1)：M_H = T*Jac(C)（Jac(C) × H⁰(C,K)，复维 2g），主极化使 Jac(C)^∨ ≅ Jac(C)，故纤维 T-对偶回到自身（自对偶纤维化）；这解释了为什么对 abelian G，Hitchin 纤维化上的 T-对偶不产生新的镜像伙伴。

### 5.4 数值/特例检验
- 单环面：R = 2 → R′ = 1/2；R = 1 自对偶；一般 τ = 0.5+1.2i → τ′ = −1/τ，Im τ′ = Im τ/|τ|² = 1.2/1.69 ≈ 0.710 > 0（附录 §A5 打印）。
- Prym 维数：g = 2,3,4 → 3g−3 = 3,6,9 = ½dim M_H(SU(2)) = ½·(6,12,18) ✓（附录 §A6）。
- 底/纤维关系：Ξ: B → ^L B 只是底空间之间的映射（§5.4），T-对偶只改纤维 ⇒ 报告中任何「基/纤维互换」措辞都应改为「纤维换成对偶纤维、底空间经 Ξ 映到对偶底空间」。

### 5.5 与报告比
- 报告第 6 条结论「§4 没有 T-对偶论证」**正确**，`report_v1.md:305` 明确写了「B §4.3 没有 T-对偶论证」，并正确列出 §4 给的三个前提。
- 报告 `report_v1.md:328` 的「4d S-对偶 ⟹ A-模型(M_H(G), ω_K) ≅ B-模型(M_H(^L G), J) ⟹ 镜像对称」**在 §4 没有支撑，是提前使用 §5**（以及 C/D 讲义）；它自己标注了来源 (D p.15)(C p.4)(D p.17)，但没有把首要出处指到 B §5.3（印刷 p.70，`p071.txt`）与 §5.5（印刷 p.77，`p078.txt`）。这属于「引用层级」问题（E6），不是错误。
- 另：报告 `report_v1.md:17` 说 T-对偶/SYZ/镜像「在 C §3 (C p.4) 与 D §5.1–5.2 (D pp.15–17)」，只指了二手讲义，未指 B 自己的 §5.5；建议补上。

### 5.6 判定
**§4（含 §4.3）没有任何 T-对偶论证**：原文在这里只把纤维做成复环面并证明其在 Ω_I/ω_J/ω_K 下 Lagrange。T-对偶（SYZ）+ 镜像（M_H(G) 与 M_H(^L G) 在 J 下互为镜像）+ S-对偶作用在底空间，全部在 §5.3–5.5（印刷 pp.70–77）。报告的「§4 无 T-对偶」判断正确；「S-对偶在 M_H 上变成镜像对称」在 §4 无支撑、是提前用 §5。

---

## 发现的问题清单

### 报告（report_v1.md）的问题
**E1（高）(4.11) 中 μ_K 符号与原文相反。**
- 报告位置：`report_v1.md:142`：「μ_K = −(i/2π)∫_C |d²z| Tr ε( D_z̄φ_z − D_zφ_z̄ )」。
- 原文依据：印刷 p.46（`p047.txt`，页图 PDF47 已核对）」：μ_K = −(i/2π)∫_C |d²z| Tr ε(D_zφ_z̄ − D_z̄φ_z)。
- 正确是：μ_K = −(i/2π)∫(D_zφ_z̄ − D_z̄φ_z) = +(i/2π)∫(D_z̄φ_z − D_zφ_z̄)。报告那把 μ_K 整体反号。
- 后果/怎么改：报告的 μ_J + iμ_K 会算成 −(1/π)∫D_zφ_z̄，与它自己引的 (4.20)「ν_I = −(1/π)∫D_z̄φ_z、depends only on A_z̄ and φ_z」矛盾（内部不一致）。改法：把 μ_K 的括号内顺序改成 (D_zφ_z̄ − D_z̄φ_z)，并由此核对 ν_I = μ_J + iμ_K ∝ D_z̄φ_z、ν_J = μ_K + iμ_I ∝ F_{A+iφ}。

**E2（中）报告对 (4.11) 的「核对」句逻辑错误。**
- 报告位置：`report_v1.md:144`：「μ_J = 0 与 μ_K = 0 相加、相减分别给出 D_z̄φ_z = 0 与 D_zφ_z̄ = 0，合起来恰是 D*φ = 0」。
- 原文依据：印刷 pp.39、46、49–51。
- 正确是：**μ_J = 0 单独就是 D*φ = 0**（即 D_zφ_z̄ + D_z̄φ_z = 0，一条实方程）；**μ_K = 0 单独就是 Dφ = 0**（D_zφ_z̄ − D_z̄φ_z = 0）；把这两条实方程做线性组合才得到 D_zφ_z̄ = 0 与 D_z̄φ_z = 0（φ 的全纯与反全纯条件），等价地 ν_I = μ_J + iμ_K = 0。报告末句「合起来恰是 D*φ = 0」把 D*φ（单条实方程，就是 μ_J=0）与「Dφ=0 且 D*φ=0」（两条实方程，即 Hitchin 方程全部）混为一谈；并且由于 E1 的符号错误，按报告那把 μ_K 反号之后，μ_J 与 μ_K 的线性组合并不能给出它写的那两组方程。
- 怎么改：删掉该句，改成「μ_I=0 ⟺ F−φ∧φ=0；μ_J=0 ⟺ D*φ=0；μ_K=0 ⟺ Dφ=0；ν_I = μ_J+iμ_K=0 ⟺ ∂̄_Aφ=0（及其共轭 D_zφ_z̄=0）」。

**E3（中）维数账只有转述、缺独立依据与具体数。**
- 报告位置：`report_v1.md:49`（直接引 p.39 的 (2g−2)dim G）、`report_v1.md:275`（用 dim H⁰(K^n)=(2n−1)(g−1) 与 (4.24) 得 dim B，然后说「等于 dim M，也是 dim M_H 的一半」）。
- 缺什么：(a) 路线 A：dim_ℂ M = h¹(C, ad E) = (g−1)dim G（RR，稳定 E 上 h⁰ = 0）；(b) 路线 B：φ 是 M 的余切方向 ⇒ T*M ⊂ M_H 稠密 ⇒ dim M_H = 2dim M；(c) 说明「dim W − 4dim G」在无穷维下是 ∞−∞ 不能直接用；(d) SU(2)、g=2 的具体数：dim M_H = 6（实 12）、dim B = dim F = 3。
- 怎么改：补上 (a)(b)(c)，并加一行数值表（g=2,3；SU(2)、G₂ 等）。

**E4（低）Ω_J 照抄 (4.9) 未注明 A 是复化联络。**
- 报告位置：`report_v1.md:126`「Ω_J = −(i/4π)∫Tr δA∧δA」。
- 原文依据：印刷 p.44（`p045.txt`）。
- 正确是：该式中的 A 必须读作复化联络 **𝒜 = A + iφ**，即 Ω_J = −(i/4π)∫Tr δ𝒜∧δ𝒜；否则与 ω_K + iω_I 的定义不符（用 (4.8) 展开得 Ω_J = −(1/2π)∫|d²z|Tr(δA_z+iδφ_z)∧(δA_z̄+iδφ_z̄)，含 φ）。
- 怎么改：加括注「此处 A 为复化联络 A+iφ」。

**E5（低）对 (4.1) 的分量分解句错误。**
- 报告位置：`report_v1.md:49` 括号内：「F − φ∧φ = 0 是 F 的 (2,0) 与 (0,2) 部分为零，Dφ = 0 与 D*φ = 0 分别管 (1,0)、(0,1) 部分」。
- 原文依据：印刷 p.39（`p040.txt`：F−φ∧φ=0 与 Dφ=D*φ=0 由「取实部虚部」得到）。
- 正确是：C 是复维 1，任何 2-形式只有 (1,1) 分量（dz∧dz=0），故 F−φ∧φ=0 是 **(1,1)** 方程：F_{zz̄} − [φ_z,φ_z̄] = 0；Dφ=0、D*φ=0 是同一 (1,1) 型方程的实/虚（或对称/反对称）组合，它们等价于 ∂̄_Aφ_z = 0 与 ∂_Aφ_z̄ = 0，不存在「(2,0)/(0,2) 部分」「(1,0)/(0,1) 部分」的说法。
- 怎么改：改为上面的 (1,1) 表述。

**E6（低）T-对偶/镜像的首要出处没引到 B §5.3/§5.5。**
- 报告位置：`report_v1.md:17`、`:313–316`、`:328`：T-对偶/SYZ/镜像只引 C §3、D §5.1–5.2、D p.15–17。
- 原文依据：§5.3 印刷 p.70（`p071.txt`，"mirror pair in complex structure J"）、§5.5 印刷 p.77（`p078.txt`，"SYZ duality between torus fibrations … T-duality on the corresponding torus fibers"）。
- 怎么改：加引 B §5.3、§5.5 为第一出处；并注明「§4 无 T-对偶」的正确判断已有，只是要把「镜像对称」的支撑指向 §5 而不是让读者以为 C/D 是唯一来源。

**E7（低）(4.11) 的页锚差一页。**
- 报告位置：`report_v1.md:142` 末尾标「(B p.45)」。
- 原文依据：(4.11) 在印刷 **p.46**（`p047.txt`；页图 PDF 第 47 页页脚印「46」已核对）。报告对 (4.8)(4.9) 标的 p.44 是对的，只有 (4.11) 这一处差一页。
- 怎么改：把该处改成 `(B p.46)`。这不影响任何推导，只是页锚。

### 任务单/题面的问题（不是报告错误，单独列出）
**N1（题面）**「验证 ω_J + iω_K 是 **J** 下的全纯 2-形式」——错：ω_J + iω_K = Ω_I 是**复结构 I** 下的 (2,0) 形式；J 下的全纯 2-形式是 Ω_J = ω_K + iω_I。理由：ω_J 在 J 下是 (1,1) 型，不能出现在 (2,0) 形式中；且 (4.9) 明确 Ω_I = ω_J + iω_K 对 I 是 (2,0)。
**N2（题面）**「维数…与原文 (4.22) 一带（p.49）对照」——错：(4.22) 是单值矩阵（印刷 p.51），维数陈述在 p.39（无编号式），(4.25) 在 p.54。
**N3（题面）**「原文 §4.3 如何在纤维上做 T-对偶」和「T-对偶前后基/纤维互换」——§4 没有 T-对偶；且 T-对偶只把纤维换成对偶纤维（底空间经 Ξ: B → ^L B 映到对偶底空间），不是「基/纤维互换」（见 §5.3 一步步推导）。

---

## 附录：可重跑 python（每段独立可跑）

各段只用标准库；输出的数即正文引用的数。

### A1 三矩映射的组合与符号（对应 §1）
```python
# A1: combination algebra of (4.11): (D phi), (D * phi), nu_I = mu_J + i mu_K
import random
random.seed(20261117)
i = 1j
bad = 0
for _ in range(360):
    a = complex(random.uniform(-3,3), random.uniform(-3,3))   # D_z phi_zbar
    b = complex(random.uniform(-3,3), random.uniform(-3,3))   # D_zbar phi_z
    muJ = -(a + b)        # mu_J, common factor 1/(2 pi) dropped
    muK = -i*(a - b)      # mu_K as printed in (4.11)
    nuI = -b              # nu_I = -(1/pi) D_zbar phi_z   (4.20)
    if abs((muJ + i*muK) - 2*nuI) > 1e-9: bad += 1   # must equal 2*pi*nu_I = -2b
    if abs((muJ - i*muK) + 2*a) > 1e-9: bad += 1      # must equal -2a
print("source signs: 360 random checks, failures =", bad)
a, b = 1+1j, 0.5-2j
muK_report = -i*(b - a)                       # sign used in report_v1.md:142
print("report  mu_J+i mu_K =", -(a+b) + i*muK_report, " = -2a ->", -2*a)
print("source  mu_J+i mu_K =", -(a+b) + i*(-i*(a-b)), " = -2b ->", -2*b)
print("check: 2*pi*nu_I = -2b ->", -2*b)  # (4.20): nu_I = -(1/pi) D_zbar phi_z
print("(D phi)_zzbar = D_z phi_zbar - D_zbar phi_z =", a-b)
print("(D * phi)    ~ D_z phi_zbar + D_zbar phi_z =", a+b)
```

### A2 ω_J + iω_K 的型别相消（对应 §3）
```python
# A2: omega_J + i omega_K kills the (0,2) part and doubles the (2,0) part  -> (1/pi) X
i = 1j
k = 1.0/(2*3.141592653589793)          # 1/(2 pi)
# X = delta phi_z ^ delta A_zbar : type (2,0) ;  Y = delta phi_zbar ^ delta A_z : type (0,2)
wJ = {'X_(2,0)': k,  'Y_(0,2)': k}     # omega_J = k (X + Y)
wK = {'X_(2,0)': -i*k, 'Y_(0,2)': i*k} # omega_K = i k (Y - X)
OI = {key: wJ[key] + i*wK[key] for key in wJ}
print("(2,0) coefficient of omega_J+i omega_K =", OI['X_(2,0)'], " equals 1/pi?", abs(OI['X_(2,0)'] - 1/3.141592653589793) < 1e-15)
print("(0,2) coefficient =", OI['Y_(0,2)'], " must be 0")
from fractions import Fraction
# exact check in units of 1/pi:  (1/2)(X+Y) + i*(i/2)(Y-X) = X
cX = Fraction(1,2) + 1j*(1j*(-Fraction(1,2)))
cY = Fraction(1,2) + 1j*(1j*(Fraction(1,2)))
print("units of 1/pi: coefficient of X =", cX, " of Y =", cY)
```

### A3 维数账与 (4.24)（对应 §2）
```python
# A3: check (4.24) sum(2d-1) = dim G, then dim M_H, dim B, dim F
groups = {
 'SU(2)': (3,  [2]),
 'SU(3)': (8,  [2,3]),
 'SU(4)': (15, [2,3,4]),
 'SO(5)': (10, [2,4]),
 'Sp(4)': (10, [2,4]),
 'G2':    (14, [2,6]),
 'F4':    (52, [2,6,8,12]),
 'E6':    (78, [2,5,6,8,9,12]),
 'E7':    (133,[2,6,8,10,12,14,18]),
 'E8':    (248,[2,8,12,14,18,20,24,30]),
}
print("group   sum(2d-1)  dimG  match?")
for name,(dimG,degs) in groups.items():
    s = sum(2*d-1 for d in degs)
    print("%-8s %8d %6d   %s" % (name, s, dimG, 'OK' if s == dimG else 'FAIL'))
print()
print("dim_C M_H = 2(g-1)dimG ; dim_C M = dim B = dim F = (g-1)dimG")
for name in ('SU(2)','SU(3)','G2','E8'):
    dimG, degs = groups[name]
    for g in (2,3):
        dm = (2*g-2)*dimG; db = (g-1)*dimG
        print("  %-6s g=%d: dim_C M_H=%4d  dim_C M=dim B=dim F=%4d  2*B==MH? %s" % (name, g, dm, db, 2*db == dm))
dimG, degs = groups['SU(2)']; g = 2
print()
print("SU(2), g=2: dim_C M_H =", (2*g-2)*dimG, " (real dim", 2*(2*g-2)*dimG, "); dim_C B = dim_C F =", (g-1)*dimG)
print("RR check: dim_C M = h^1(C, ad E) = (g-1)dim G =", (g-1)*dimG)
```

### A4 纤维化/哈密顿量/满射性计数（对应 §4）
```python
# A4: Hitchin fibration counts: dim B = sum (2d_i-1)(g-1); surjectivity 2^(3g-3); Lagrange dims
groups = {'SU(2)': (3, [2]), 'SU(3)': (8, [2,3]), 'G2': (14, [2,6]), 'E8': (248, [2,8,12,14,18,20,24,30])}
print("g  group   dim M_H  half  dim B=dim F  #Hamiltonians=dim B")
for g in (2,3,4):
    for name,(dimG,degs) in groups.items():
        dimMH = (2*g-2)*dimG
        dimB = sum((2*d-1)*(g-1) for d in degs)
        assert dimB == (g-1)*dimG, (name, g)
        print("%d  %-6s %6d %5d %11d %18d" % (g, name, dimMH, dimMH//2, dimB, dimB))
print()
for g in (2,3,4):
    n = 3*g-3
    print("SU(2), g=%d: dim B = dim H^0(C,K^2) = 3g-3 = %d; %d quadratic equations in %d variables -> 2^%d = %d solutions" % (g, n, n, n, n, 2**n))
print()
for g in (2,3):
    dimMH = 6*g-6; n = dimMH//2
    print("SU(2), g=%d: dim_C F = %d, dim_R F = %d = dim_R M_H = %d  (maximal isotropic)" % (g, n, 2*n, dimMH))
```

### A5 单环面/单圆的 T-对偶数值（对应 §5）
```python
# A5: T-duality on a circle/elliptic curve:  tau -> -1/tau   (square torus tau = i R^2  <=>  R -> 1/R)
import cmath
def dual_tau(tau):
    return -1.0/tau
print("tau          tau'=-1/tau   Im(tau')>0   Im(tau')=Im(tau)/|tau|^2")
for tau in (4j, 2j, 1j, 0.5+1.2j, 1.5+0.4j):
    tp = dual_tau(tau)
    ok = abs(tp.imag - tau.imag/abs(tau)**2) < 1e-12
    print("%-12s %-13s %-11s %s" % (tau, tp, tp.imag > 0, ok))
print()
print("square torus tau = i R^2:  R = 2 -> tau = 4i -> tau' = i/4 -> R' = 1/2 = 1/R ; R = 1 -> tau = i -> tau' = i (self-dual)")
for R in (0.5, 1.0, 2.0, 4.0):
    tau = 1j*R*R
    tp = dual_tau(tau)
    Rp = cmath.sqrt(tp/1j).real
    print("R=%-4.1f tau=%-8s tau'=%-8s R'=%.6f  (1/R=%.6f)" % (R, tau, tp, Rp, 1.0/R))
```

### A6 Hitchin 纤维维数 = Prym 维数（SU(2) vs SO(3)）（对应 §5）
```python
# A6: Hitchin fiber dimensions = Prym dimension (SU(2)) vs dual (SO(3));  U(1) case
print("g  g(Sigma)=4g-3  dim Prym=g(Sigma)-g  half dim M_H = 3g-3  equal?  dim_C M_H  #solutions 2^dimB")
for g in (2,3,4,5):
    gS = 4*g-3
    prym = gS - g
    half = 3*g-3
    dimMH = 6*g-6
    print("%d %8d %16d %20d %8s %10d %18d" % (g, gS, prym, half, prym == half, dimMH, 2**half))
print()
print("U(1): M_H = T*Jac(C), dim_C = 2g; principal polarization gives Jac(C)^dual = Jac(C) -> self-dual fiber")
for g in (1,2,3):
    print("g=%d: dim_C M_H(U(1)) = %d, dim_C Jac = %d = dim_C dual Jac" % (g, 2*g, g))
```
