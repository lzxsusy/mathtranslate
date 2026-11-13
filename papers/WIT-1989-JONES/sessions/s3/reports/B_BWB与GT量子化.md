# S3-B：Borel–Weil–Bott 与 G/T 的几何量子化

**结论先行。**（i）"λ 不加 ρ"不是 Witten 的选择：BWB 的线丛 L_λ 由 B 的特征 λ 诱导，H⁰ 的权就是 λ；ρ 是**半形式修正**（K_{G/T}^{1/2}=L_{−ρ}）才产生的位移，Witten 只取预量子化线丛，故不位移。（ii）BWB 在此不是"算上同调"，而是**把量子算子插入换成经典相空间因子**：表示矩阵 T^a → G/T 上的经典函数，高斯约束 (3.4) → 经典方程。（iii）Wilson 线换成 S¹→G/T 泛函积分是**纲领，不是定理**（全用 should，并说"deferring a fuller treatment" [p.371]）。

## 一、五问

### 1. λ 为何不加 ρ；ρ 在哪

- **原文只到"量子化给回 R"**：p.372 "for each representation R one introduces a symplectic structure ω_R on G/T, such that the quantization … gives back the representation R." 全文无 H⁰(G/T,L_λ)=R，也无 λ/λ+ρ 之辨——该式子是我们补的。
- **数学上不加也合法**：L_λ=G×_B C_λ，全纯截面的 G-模即 V_λ；λ 已是表示的权，无第二个量可加 [nLab: Borel-Weil-Bott, 2025-11-06]。
- **ρ 只出现在别处**：① 半形式修正——T(G/T) 的权是正根，故 K=L_{−2ρ}，K^{1/2}=L_{−ρ}；做 metaplectic 修正就等价于 L_λ→L_{λ+ρ}，这是"加 ρ"的唯一机制，Witten 没做；② Weyl 维数公式 dim V_λ=∏_{α>0}(λ+ρ,α)/(ρ,α)；③ BWB 零化判据要"λ+ρ 正则"；④ 仿射化后 ρ → 能级平移 k→k+h∨（即 S2 的 e^{2πi/(N+k)}）。
- **数值检验**：SU(2) 时 G/T=CP¹，∫ω/2π=κ=2j，dim H⁰=κ+1=2j+1=dim V_{2j}，指标即 λ=2j [Moore (B.34) p.165]。

### 2. ω_R 的 de Rham 类为何"取 λ"

G/T≅余伴随轨道 O(λ)，Kostant–Kirillov 形式 ω_λ(X,Y)=½⟨λ,[X,Y]⟩ [Moore (B.36) p.165]；λ∈g* 本身就是这个类的代表，所以"取 λ"是轨道方法的定义而非选择。三条前提：① G/T 紧 Kähler（G_C/B 射影簇，Moore p.165 明言"既是紧流形又是 Kähler 流形"）；② λ 整 ⇒ [ω_λ/2π]∈H²(G/T,Z)，才有预量子化线丛（否则只剩 R/Z 类）；③ λ 支配 ⇒ H⁰≠0。原文对整性只字未提。

### 3. BWB 完整陈述；它替代哪一步

**陈述**（G 单连通半单、λ 整权、L_λ=G×_B C_λ→G/B）：若 λ+ρ 奇异则 H^q(G/B,L_λ)=0 ∀q；否则唯一 w∈W 使 w(λ+ρ) 支配正则，则 H^q=0（q≠ℓ(w)）且 H^{ℓ(w)}≅V_{w(λ+ρ)−ρ}。λ 支配时 w=e，得 H⁰=V_λ，其余零——即"除某个 Weyl 平移外上同调为零"。

**替代的那一步**：p.372 把相空间 M₀ **扩大**，在每个标记点添一份 G/T，并把 (3.4) 右端的 T^a_{(s)}（表示矩阵、量子算子）换成"G/T 上经典函数的量子化像"。于是约束 (3.4) 变成经典方程，约束后相空间是"Σ 上平坦 G 联络 + 在 P_i 处结构群约化到 T"（p.372 原话）。BWB 保证该经典因子的量子化正好还回 R_i，故"表示/算子插入"整段被"经典相空间因子"替代。

### 4. Wilson 线→S¹→G/T：动机与地位

p.372 先把表示抬成本体："A representation R of a group G should be seen as a quantum object. This representation should be obtained by quantizing a classical theory." 若表示本身是量子化经典系统的产物，则 (1.5) 的 Tr_R P exp∮A 不该是外来插入，而应是同一泛函积分中的经典场。p.373："One should use the theorem to replace the Wilson lines (1.5) … with a functional integral over maps of the circle S into G/T (or … sections of a G/T bundle, twisted by … E). This gives a much more unified formalism."
**地位：方案。** 无陈述、无证明、无算式；不能写成"Witten 证明"。G/T 边界条件后来成为抛物/flag 结构的来源（[后人：Dimofte–Gaiotto–Gukov 1108.4389]），但本文止于提纲。

### 5. "只有可积表示才有非零截面"

**出处**是 p.372 的括号，非命题："In current algebra at level k, one only permits certain representations, the 'integrable ones'. If one formally tries to include other representations, the Ward identities show that they decouple [36]. According to Segal, … the appropriate line bundle over M_{P_i,R_i} has no non-zero holomorphic sections unless the R_i all correspond to integrable representations. … unless the representations R_i are all integrable, the zero vector is the only vector in the physical Hilbert space." p.373 重述："ℋ is zero unless the R_i correspond to integrable representations of the loop group."

**不是 BWB 的推论。** BWB 对一切支配整 λ 成立、无上限；能级上限来自仿射代数：河野命题 1.5 [河野 p.11]——k 正整数、0≤λ≤k ⇒ H_{k,λ} 可积，sl2 即 λ=2j≤k。原文只说 integrable，**"2j≤k"不在原文**。故这里有两套独立论证：Ward 恒等式 + Segal 代数几何。

## 二、与本地教材对照

| 断言 | 位置 | 关系 |
|---|---|---|
| G/T 紧 Kähler、ω_λ=½⟨λ,[·,·]⟩ | Moore B.3 p.165 | 补原文未写的公式 |
| SU(2)：∫ω/2π=2j、dim=2j+1 | Moore B.2.1 p.164–165 | 检验 λ 不位移 |
| 可积条件 0≤λ≤k | 河野 1.2 命题1.5 p.11 | 补原文"integrable" |
| 共形块 Hom_{g(p)}(⊗H_λ,C) 有限维 | 河野 1.4 p.19；Ueno ch3 p.43 | §3.4 Inv(⊗R_i) 的有限维影子 |
| 物理态丛、射影平坦 | Moore 2.2.13 p.58 | 对应 Witten p.370 |

## 三、最没把握的三点

1. **ρ↔半形式对接是我补的**：K_{G/T}=L_{−2ρ} 是标准事实，但"Witten 未做半形式修正"只是从他只说"quantization with symplectic structure"推断，原文无一字讨论；若他认为归一化已吸收，结论同、理由须改写。
2. **BWB 含 ρ 的完整陈述未逐字核**：nLab 只给 H⁰ 版，Kostant 1961 原文未读，公式凭标准记忆，标"未核"。
3. **"约化到 T"与"约化到 B"**：原文只说 reduction to T；紧 G 下 G/T≅G/B 可互译，但文中未辨析，我按等价处理。

## 四、锚点速查

- 表示=量子对象、BWB 引入 G/T、扩大相空间、T^a→经典函数、约化到 T：Witten p.372
- 可积性/退耦括号：p.372；§3.4 重述：p.373；"deferring"：p.371
- Wilson 线→S¹→G/T（纲领）：p.373；(3.5) 大 k 极限：p.373
- 半形式/ρ：我们补（K=L_{−2ρ}）；Weyl 维数公式：标准
- 河野 1.2 命题1.5 p.11；河野 1.4 p.19；Ueno ch2 p.33、ch3 p.43；Moore B.2.1 p.164、B.3 p.165、2.2.13 p.58；nLab BW/BWB 2025-11-06
