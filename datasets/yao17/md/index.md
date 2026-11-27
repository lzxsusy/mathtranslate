# Yao《一般线性群的局部 Langlands 对应》（yao17）资料卡索引

共 29 张：概念卡 23 张、推导卡 6 张。


## 轨道 Weil–Deligne 侧


**概念卡**

- [φ-半单（Frobenius 半单）与引理 1.2](concepts/frobenius-semisimple.md) —— 在 ρ(I_K) 有限时，ρ 半单 ⇔ 任一 Frobenius 提升的半单性；由此把「φ-半单」定为 LLC 目标范畴的条件。
- [Tate 的局部 L 因子与 ε 因子、定理 1.3 的存在唯一性](concepts/tate-epsilon.md) —— Tate 对拟特征标给出 L(χ) 与显式 ε(χ,ψ,dx)；Langlands 把它唯一延拓到 W_K 的表示上，要求对特征是 Tate 的、短正合列乘性、0 次归纳。
- [Grothendieck 单值化定理、WD 函子与惯性类型](concepts/wd-functor.md) —— 引理 1.5 把 ℓ 进表示化成 exp(t_ℓ(σ)N)；推论 1.7 的 WD 函子给出 Rep_L(G_K)≃wd^{ℓ-int}，惯性类型则丢掉 N 只留 I_K 上的结构。
- [Weil–Deligne 表示的导子 c(ρ)、L 因子与 ε 因子](concepts/wd-invariants.md) —— c(ρ)=c(ρ')+dim V^{I_K}−dim(ker N)^{I_K}；L 与 ε 只用 (ker N)^{I_K} 与 V^{I_K}/(ker N)^{I_K} 上的 Frobenius 作用。
- [Weil–Deligne 表示 (ρ, N) 及其基本性质](concepts/wd-representation.md) —— (ρ,N) 中 ρ 是 I_K 上有限像的连续表示，N 满足 σNσ^{-1}=q^{-v_K(σ)}N；N 必幂零，半单情形下 (ρ,N)≅⊕Sp_m(r)。
- [Weil 群 W_K、惯性群、野惯性群与驯特征标](concepts/weil-group.md) —— W_K 是 I_K 与 Frobenius 整数幂的半直积；t 把 I_K/P_K 同构到 ∏_{l≠p} Z_l，共轭作用即分圆特征标。

**推导卡**

- [从 ℓ 进表示造出 (ρ, N)：引理 1.5 的构造五步](derivations/wd-from-galois.md) —— 把 ℓ 进表示先模 ℓ、再沿惯性群的 ℓ 进商分解，取 N=log ρ(σ) 即得 Weil–Deligne 表示。

## 轨道 自守侧


**概念卡**

- [定理 2.5（光滑不可约 ⇒ 容许）、引理 2.6 与 Harish-Chandra 特征标](concepts/harish-chandra-character.md) —— 光滑不可约必容许；GL_n 的光滑不可约表示或一维或无穷维，一维者必为 χ∘det；Θ_π(f)=Tr π(f) 由正则半单处的局部常值函数 χ_π 表示。
- [Hecke 代数 H(G)、双陪集子代数与 「光滑表示 ≃ 非退化 Hecke 模」](concepts/hecke-modules.md) —— H(G) 是紧支局部常值函数的卷积代数；引理 2.1 给出 Rep^∞_G ≃ 非退化 H(G)-模，引理 2.2 把容许性换到有限维 H(G//K)-模上。
- [超尖点表示：J_P(π)=0 与矩阵系数的紧支性](concepts/jacquet-supercuspidal.md) —— π 超尖点指对所有真抛物 P 有 J_P(π)=0；等价地所有矩阵系数在 G⁰ 上紧支（模中心紧支）。它们是容许表示的积木。
- [抛物诱导、Jacquet 函子与模特征标 δ 的正规化](concepts/parabolic-induction.md) —— 朴素 J~ 与 I~ 由 ψ_! 与 ind∘ψ* 给出且伴随；乘上模特征标 δ^{±1/2} 得到正规化的 J、I，保证幺正性不被破坏。
- [球面 Hecke 代数与 Satake 同构、非分歧表示](concepts/satake.md) —— H(G//C) 交换，且 ≅ C[t_1^{±1},…,t_n^{±1}]^{S_n}；故不可约容许 π 的 π^C 或为 0 或一维，「非分歧」即 π^C≠0。
- [光滑表示、容许表示与反变对偶](concepts/smooth-admissible.md) —— 光滑指每个向量的稳定子开；容许再要求每个开子群的固定向量空间有限维。反变对偶 V∨ 取「稳定子开」的线性泛函。

**推导卡**

- [超尖点判据：π 非超尖点 ⇒ 可嵌入某真抛物诱导（引理 2.10 的证明链）](derivations/supercuspidal-criterion.md) —— 若 J_P π ≠ 0，取不可约商 σ 并用伴随性把 π 嵌进 I_P σ；σ 非超尖点则再降，直到 σ 超尖点。

## 轨道 分类与不变量


**概念卡**

- [导子 c(π)、深度、JPPS 的 ε 公式与深度 0 对照图](concepts/conductor-depth.md) —— ε(π,s,ψ)=q^{−(c(π)+n·n(ψ))s}ε(π,0,ψ)；深度 0 的 π 对应驯分歧的 r_n(π)，非分歧对应 ρ|I_K=0 且 N=0。
- [一般（generic）表示、Whittaker 模型与定理 3.6](concepts/generic-whittaker.md) —— generic 指 π|U_n 上有非零的 θ_ψ-同态；Zelevinsky 定理说它等价于段两两不 linked，故缓增必 generic。
- [本质 L^r、平方可积、缓增：定理 3.2、3.3 与推论 3.4](concepts/square-integrable-tempered.md) —— 本质平方可积 ⇔ π=Q(Δ) 单段；缓增 ⇔ 每段都平方可积；两者之间还有本质 L^{2+ε} 的连续层级。
- [超尖点支撑与 Steinberg 表示 St_n](concepts/supercuspidal-support.md) —— 超尖点支撑是 Q 与 Z 共有的唯一无序超尖点组；取 Δ=[|·|^{(1−n)/2},…,|·|^{(n−1)/2}] 时 Z(Δ)=triv、Q(Δ)=St_n（自对偶）。
- [Zelevinsky 段 Δ(π,m)、linked/precedes 与 (∗) 条件](concepts/zelevinsky-segment.md) —— 段是 Asc_n 中有限区间 [π,π(1),…,π(m−1)]；两段 linked 指互不包含但并仍是段，precedes 再加 π1<π2；(∗) 禁掉 i<j 的 precede。

**推导卡**

- [深度 0 的五条等价链：从 π^K ≠ 0 一路推到 N = 0](derivations/depth-zero-chain.md) —— 非分歧↔π^K≠0↔rec 非分歧↔ρ|I_K=0 且 N=0；Iwahori-球面↔ρ|I_K=0；深度 0↔驯分歧。
- [GL₂ 的四类表示如何对应到 Weil–Deligne 表示](derivations/gl2-llc-cases.md) —— 超尖点↦不可约 (ρ,0)；主序列↦(χ₁⊕χ₂,0)；triv⊗χ↦(χ⊕χ(1),0)；St₂(χ)↦(χ⊕χ(1),N)。
- [把 LLC 从超尖点归纳到一般表示：rec_n = ⊕ Sp_{m_i} ∘ rec_{n_i}](derivations/induction-to-supercuspidal.md) —— 由 BZ 把 π 写成 Q(Δ₁,…,Δ_r)，再对每个段用 Sp_{m_i}(rec_{n_i}(π_i))，底层 ρ 是 rec_{n_i}(π_i)(j) 的直和。

## 轨道 惯性 Langlands 与类型


**概念卡**

- [Bernstein 分量、惯性等价与定理 4.2 的直积分解](concepts/bernstein-decomposition.md) —— Rep^∞_n 直积分解为各 Bernstein 分量 R(L,ς)；分量相等 ⇔ 惯性等价，Bernstein 中心就是 (L,ς) 的惯性等价类。
- [惯性对应：Bernstein 中心 ↔ Weil–Deligne 惯性类型（引理 4.3–4.5）](concepts/inertial-correspondence.md) —— π 与 π′ 同 Bernstein 分量 ⇔ rec(π)|I_K ≅ rec(π′)|I_K；generic 时更强：同一 Galois 惯性类型 ⇒ π|K ≅ π′|K。
- [类型（type）、K-型与极小 K-型；Bushnell–Kutzko 型的区别](concepts/type-and-k-type.md) —— σ 是 (L,ς) 的类型，若「π|_K 含 σ ⇔ π∈R(L,ς)」；只要求单向的是 K-型，π 上维数最小者为极小 K-型。

**推导卡**

- [惯性对应怎么从 Bernstein 分量推出来：BZ 分类 → 超尖点 → 引理 4.3](derivations/inertia-from-bernstein.md) —— 把 π 写成 Q(Δ₁..Δ_r) 后限制到 I_K，只剩各段超尖点的 rec，再用引理 4.3 逐个分离分量。

## 轨道 总览与主陈述


**概念卡**

- [定理 3.1：Bernstein–Zelevinsky 对 GL_n 容许表示的七条分类](concepts/bz-classification.md) —— 用段 Δ 造出 Q(Δ) 与 Z(Δ)，任何不可约表示唯一地是 Q(Δ_1,…,Δ_r)，且 Q 侧对 (∗)-置换不变。
- [定理 2.14：超尖点、本质平方可积、一般表示在对应下的像](concepts/llc-finer-properties.md) —— rec_n 把超尖点送成不可约、把本质平方可积送成不可分解、把一般表示送成 ad 的 L 因子在 s=1 无极点。
- [局部 Langlands 对应：定理 2.13 的五条性质](concepts/llc-statement.md) —— rec_n 把 GL_n(K) 的不可约容许表示双射到 n 维 Frobenius 半单 Weil-Deligne 表示，由五条性质唯一刻画。
