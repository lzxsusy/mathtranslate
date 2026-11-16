# U05 复算报告

**复算员**：P5（R8）　**对象**：KW 2006（WIT-0604151）§6（pp.78–102）、§7（pp.103–115）、§8（pp.116–123）
**对照**：`work/rounds/U05/report_v1.md`（下称"报告"）
**材料**：逐页文本 `source/text/p{N+1:03d}.txt`（文件 p{N+1} = 印刷页 N）；页图目录仅存 p.35–38、p.60–61、p.67、p.70–71 共 9 张，**U05 范围（p.78–p.123）无页图**（无 p.83、p.84、p.95、p.121 等图）。
**判定标度**：A = 与原文一致/可直接验证；B = 可补全但未在原文逐项写出；C = 推断/约定级；D = 与原文不符。
**总判定**：五项中 1、3、5 的原文事实与报告转述基本正确（1 的报告"符号差"为假警报、3 的报告缺关键澄清、5 的报告缺显式化）；2、4 需要补算并改述。**问题：高 0、中 4、低 5**（E1–E9）。

---

## 1. 't Hooft 算子奇点：(6.8) ⟹ (6.9) 与通量归一化

### 1.1 问题
(1) 由 (6.8) 的 F 奇点条件出发，验证 (6.9) 的 φ 奇点；(2) 说明 F ∼ (i/2)⋆₃d(1/r) 的归一化如何给出 ∮_{S²} iF/2π = 1；(3) 核报告自报的"∮F₀ = −2πi 符号差"；(4) 页图缺失下的判断。

### 1.2 原文（引文 ≤120 字符）
- p.82（`p083.txt`）：(6.7) `F = (i/2) ⋆ d(1/|x⃗|)`；"then ∫_Y iF/2π = 1"；"This is the singular Dirac monopole."；F 近 S 发散为 `F ∼ (i/2)⋆₃d(1/r)`，电荷 m 时 `F ∼ (im/2)⋆₃d(1/r)` 给出 `T(0)(m)`。
- p.83（`p084.txt`）：(6.8) `(F + dφ)_+ = (F − dφ)_− = 0`；"These equations are not satisfied if F has the Dirac monopole singularity and φ is non-singular."；"we should take φ = (i/2|x⃗|)ds"；(6.9) `F = (i/2)⋆₃d(1/|x⃗|), φ = (i/2|x⃗|)ds`。
- p.25（`p026.txt`）：(3.29) `(F − φ∧φ + tDφ)_+ = 0`，`(F − φ∧φ − t^{-1}Dφ)_− = 0`，`D*φ = 0`；t=1、abelian 即 (6.8)。p.23：χ_± 为 selfdual/anti-selfdual 部分，故 (X)_± 是 SD/ASD 投影，P_±=(1±⋆₄)/2。
- p.85–86（`p086.txt`）：(6.10) `I_θ = i(Ψ/4π)∫Tr F∧F`；(6.11) `ǫ₄ = ds∧ǫ₃`；(6.12) `ǫ₄ = ds∧dr∧dVol = −dr∧ds∧dVol`（(6.6) `ǫ₃ = dr∧dVol`）。
- p.86（`p087.txt`）：(6.13) `δ_T Ĩ_θ = (imΨ/2π)∫_{∂Vε}F₀∧δ_TÂ`；"As the outward normal ... is −d/dr, ... ∂Vε must be oriented by ds∧dVol"。
- p.86–87（`p088.txt`）："the integral of F0 over a fiber is −2πi"；(6.14) `δ_T I_θ = mΨ∮_S δ_TÂ`；(6.15)(6.16)；"gauge-invariant if and only if n is an integer. So n = −mΨ must be an integer"；(6.17) `(m n) → (m n) [d −b; −c a]`。

### 1.3 逐步推导
**(a) (6.8) 的等价形式.** 设 t=1、abelian（φ∧φ=0），由 (3.29) 得 (6.8)。记 P_±=(1±⋆₄)/2，则 (6.8) ⟺
```
F + dφ = −⋆₄(F + dφ),   F − dφ = +⋆₄(F − dφ)
```
两式相加、相减得等价组
```
F = −⋆₄ dφ,     dφ = −⋆₄ F      (⋆₄²=1 于 2-形式)
```
所以 (6.8) 说的是"F 与 dφ 互为（带号的）Hodge 对偶"，**而不是**"F 的奇点沿法向、φ 的奇点沿切向、在法向平面里相互抵消"这类几何图像（后者是报告 §2.1.2 的措辞，不精确，见 E2）。

**(b) (6.9) 满足 (6.8).** 取坐标 (x,y,z,s)，r=√(x²+y²+z²)，ǫ₃=dr∧dVol=dx∧dy∧dz（S² 的 dVol=r²sinθ dθ∧dφ）：
```
F = (i/2)⋆₃d(1/r) = (i/2)·(−1/r²)dVol = −(i/2r²)dVol
φ = (i/2r)ds,  dφ = (i/2)d(1/r)∧ds
⋆₄(dφ) = −F,  ⋆₄F = −dφ   （当 ǫ₄ = ds∧dr∧dVol）
```
关键在 ⋆₄ 的定向：文本 (6.11)(6.12) 取 **ds 在前**的 ǫ₄=ds∧dr∧dVol。若改用通常的 dx∧dy∧dz∧ds 定向（ǫ₄=−ds∧dr∧dVol），⋆₄ 整体变号，(6.8) 不成立。我用显式分量 Hodge 星算了一遍（附录 A）：
```
eps4 = ds^eps3 (text)      : (F+dφ)_+ == 0 ? True  ; (F−dφ)_- == 0 ? True
eps4 = dx^dy^dz^ds (ds-last): (F+dφ)_+ == 0 ? False ; (F−dφ)_- == 0 ? False
F == −star_text(dφ) ? True ; dφ == −star_text(F) ? True
```
**结论：(6.8)+(6.9) 自洽，但这是 (6.11)–(6.12) 的 ds-first 定向约定的一部分；离开该约定公式不成立。** 这一点原文没有单独强调，报告的 §2.1.2/§5.1 也没识别（E1、E2）。

**(c) 通量归一化.** 由 (b)：
```
∮_{S²}F = ∫ (−i/2) sinθ dθ∧dφ = −(i/2)·4π = −2πi
∮_{S²} iF/2π = 1,    ∮_{S²} c₁(L) = 1
```
电荷 m：`F ∼ (im/2)⋆₃d(1/r)` ⟹ `∮ iF/2π = m`，即 `T(0)(m)`。任务单写的 "∮F/2π=1" **量纲/因子有误**，正确为 `∮ iF/2π = 1`（即 ∮F = −2πi）；报告转述 `∮_Y iF/2π = 1` 是对的。

**(d) (6.13) ⟹ (6.14) 的符号.** 先把 ∂Vε 的定向算清：
```
i_{∂_r}(ds∧dr∧dVol) = −ds∧dVol   （ds 在 dr 前，缩并贡献 (−1)^1）
⇒ i_{−∂_r}(ds∧dr∧dVol) = +ds∧dVol  （与文本"∂Vε 由 ds∧dVol 定向"一致）
```
再算被积 3-形式（∂Vε=S¹_s×S² 上用定向 ds∧dθ∧dφ）：
```
F₀ = f dθ∧dφ (f=−(i/2)sinθ),  δ_TÂ = a(s)ds
F₀∧δ_TÂ = f a dθ∧dφ∧ds = + f a ds∧dθ∧dφ     （(θ,φ,s)→(s,θ,φ) 为偶置换）
∫_{∂Vε}F₀∧δ_TÂ = (∮δ_TÂ)·∫_{S²}F₀ = ∮δ_TÂ·(−2πi)
δ_T Ĩ_θ = (imΨ/2π)·(−2πi)∮δ_TÂ = +mΨ∮_S δ_TÂ
```
与印出的 (6.14) **完全一致**。也就是说：
- `∫_{fiber}F₀ = −2πi` 是正确的，且它已经是负号；
- 从 (6.13) 到 (6.14) 没有额外的楔积负号；
- 报告 §5.2 自报的"差一个负号"来自两处之一的符号滑落（把 i_{−∂_r}ǫ₄ 算成 −ds∧dVol，或以为 F₀∧ds 换序要加 −）。这是**假警报**（E1）。
- 真正需要写明的是 (d) 的第一行定向缩并，而不是"怀疑 −2πi 已含负号"。

**(e) (6.15)(6.16) 闭合与 (6.17).** 由 (6.14)：δ_T e^{−I_θ} = −mΨ e^{−I_θ}∮δ_TÂ；又 δ_T exp(mΨ∮Â) = mΨ exp(mΨ∮Â)∮δ_TÂ；故 (6.16) 的两项相消。(6.16) 里的算子是 `exp(mΨ∮Â)exp(−I_θ) = exp(−n∮Â)exp(−I_θ)`，n=−mΨ；规范不变性要求 n∈Z，即 Ψ=−n/m∈Q。(6.17) 对 (a,b,c,d)∈SL(2,Z) 验证（附录 C，用 Ψ'=(aΨ+b)/(cΨ+d)、n'=−m'Ψ'）：
```
T=(1,1,0,1): Ψ'=Ψ+1, (m,n)->(m, n−m),  n'+m'Ψ' = 0
S=(0,−1,1,0): Ψ'=−1/Ψ, (m,n)->(−n, m),  n'+m'Ψ' = 0
S²=(ST)³=−I
```
报告 §5.3 说 (6.17) 次序未验，此项可以销掉（E5）。

### 1.4 具体算例
见附录 A（Hodge 星分量验算，取 x=(0.3,0.4,0.7)）、附录 B（通量数值 + 定向符号）、附录 C（(6.17) 的 T、S 两情形）。A 的输出给出"文本定向 True/True，ds-last False/False"；B 给出 `∮iF₀/2π = 1.000000`、`δ_T I_θ = +6.283·mΨ`（= mΨ·∮δ_TÂ，∮δ_TÂ=2π）；C 给出 `n'+m'Ψ' ≈ 0`（T、S 均为 0 或 4×10⁻¹⁶）。

### 1.5 与报告比
- 报告 §2.1.2 正确引用 (6.7)–(6.9)（A），但把 (6.8)→(6.9) 判为"可直接代入验证"的 (B) 级补全，同时 §5.1 又自承没逐项算清——**自相矛盾**；而且没有指出该验证依赖 ds-first 定向（本轮算出的关键）。
- 报告 §2.1.3 抄 (6.13)、(6.14) 无误，但把"用纤维上 ∫F₀=−2πi"当作关键，未做 (6.12) 的缩并定向；§5.2 自报"差一负号"，实际不差（E1）。
- 报告 §6 第 4 条怀疑 p.84 一带 (6.11)(6.12) 有 OCR 缺行：**不成立**，(6.12) 文本完整、自洽，风险只在"contracting the outward normal"一句的符号实现。

### 1.6 判定
**(A)** (6.8)-(6.9) 在 ds-first 定向下自洽；(6.14) 与 (6.12)-(6.13) 自洽，∮F₀=−2πi 正确；(6.17) 自洽。**报告"符号差"为假警报**，且其 (6.8)→(6.9) 的"已验"标记与 §5.1 矛盾。页图：U05 无页图，此结论由逐页文本 + 公式编号连续性 + 显式分量验算支撑；若需页图复核，应补 p.83、p.84 的图。

---

## 2. B′ = XB 与"特征值是向量空间"

### 2.1 问题
U(1)+点电荷（或自由 chiral）例子里，膜 B 上挂 Wilson 线 W_q（电荷 q），算子作用后膜变成什么？为什么规范不变性要求变成 B⊗V，而不是"乘一个数"？E_q(R)|_x 的秩？

### 2.2 原文
- p.95（`p096.txt`）：(6.21) `Oψ = λψ`；"a complex eigenvalue does not make sense in this situation"；"what plays the role of an 'eigenvalue' is a vector space V"；对每个膜 B 与向量空间 V 定义新膜 B⊗V（Chan-Paton 丛 W→W⊗V）；"it is much better to think of the 'eigenvalue' as a vector space V, not just its integer dimension k"；(6.22) `XB = B ⊗ V`；(6.24)(6.25) `X_pB = B⊗V_p`，V_p 为 C 上平坦丛的纤维；OPE (6.26)–(6.29)。
- p.119–121：Wilson 作用 (8.7) `U → U⊗E_p(R)`；§8.2 (8.10) `U_x⊗E_q(R) = U_x⊗E_q(R)|_x`；"the 'eigenvalue' ... being the vector space E_q(R)|_x"（p.121）。
- p.122："E_p(R) is holomorphic in each of the complex structures on M_H"（超凯勒商可证）；S=γ×p 的 Wilson 保 (B,B,B)。

### 2.3 逐步推导
**(a) 膜怎么变.** Wilson 线 W_q(R) 的作用是把膜的 Chan-Paton sheaf 张量上 E_q(R)（(8.7)）。U(1)、电荷 q 时 E_q(R)=L^q（L 为 M_H×C 上的 universal line bundle；M_H(U(1),C)=T*Jac(C)，L 是 Poincaré 线丛的拉回）。于是
```
B 的 CP sheaf U  ↦  U ⊗ L^q
点膜 U_x（skyscraper） ↦  U_x ⊗ L^q = U_x ⊗ (L^q|_x) = U_x ⊗ C
```
膜（作为 sheaf）不变，但"本征值"是复直线 `V = L^q|_x`；q 变时 L^q|_x 作为 x 处平坦线丛 L|_x 的纤维随 q 变化。

**(b) 为什么是 B⊗V 而不是乘一个数.**
1. 算子在膜范畴上实现为**张量积函子**（(8.7) 的来源是 (8.1)–(8.6)：Wilson 线插入外部电荷，沿 S 的平行移动进入边界耦合；整出 A_Σ,φ_Σ 后 CP 丛被张量）。张量积函子的"本征对象"只能满足 `U⊗E ≅ U⊗V`（V 固定），不存在 U↦λU 这种"乘数"作用——若真有，等价于 V=C 且选定 E 的平凡化。
2. U(1) 时 V 是**复直线**：只有再选一个平凡化（一个非零截面/相位）才得到数 λ；不同 q 的相位没有典范比较，故只能保留为向量空间。
3. 非阿贝尔 R：dim V=dim R>1，`U⊗E` 的秩是 rank U·dim R，"乘一个数"在秩上就不可能（秩变了）；H_{B̃,B⊗V}=H_{B̃,B}⊗V 的维数也按 dim V 变化。
4. 自由 chiral 类比（C 级）：对带 U(1) 流代数的自由 chiral 代数，Wilson 线插入等价于乘一个顶点算子 e^{iq∮A}，它在电荷格上做**平移**；若把 brane 的模块按电荷分解，作用不是对角化的数而是模块之间的映射，"本征值"只能是模块（向量空间）。这与 (6.26)–(6.29) 的 OPE 结构一致。

**(c) 秩.** E_q(R)|_x = 复结构 J 下 universal bundle 限制到 x×C 所得的 flat G_C-丛 E|_x 在表示 R 中的纤维（p.122）：
```
rank E_q(R)|_x = dim R
```
点膜处 H_{B̃,B_x⊗V} 的维数 = dim V = dim R（对 U(1) 电荷 n：1）。

### 2.4 具体算例
附录 E：U(1) n=1；SU(2) fund=2、adj=3；SU(3) fund=3；E6 fund=27。零膜在 x 处 H=C，作用后 H=C^{dim R}；dim V>1 时不存在标量本征值。

### 2.5 与报告比
- 报告 §2.1.5 对 (6.21)(6.22)、B⊗V、V_p 平坦丛的转述正确（A）。
- 报告没有算 E_q(R)|_x 的秩，也没有用 U(1)/自由 chiral 做具体算例（任务单 item 2 要求）——(B) 级缺口（E7）。
- 报告 §2.3.2 的 U(1) 重建里"L^n|_x 一维 ⇒ 特征值是复直线"正确，但没有把它接回"为什么不能是数"的一般论证。

### 2.6 判定
**(A)** (6.21)-(6.22) 的转述与 U(1) 结论正确；**(B)** 秩与"非数"的论证需补（已补：rank=dim R；标量仅在 dim V=1 且选平凡化时存在）。

---

## 3. §7 的中心与离散通量

### 3.1 问题
G=SU(N)：Z(G)=Z_N 与 S-对偶对 (e,m)∈Z_N×Z_N 的作用矩阵，验证 Wilson↔'t Hooft；universal bundle 的阻碍 ζ 落在 H²(M,Z) 还是 H²(M,Z_N)？为什么 e₀=0 才有 universal bundle？

### 3.2 原文
- p.103（`p104.txt`）：G 紧、connected、simply-connected、simple；Z=π₁(G_ad)；Table 3；simply-laced 时 Z=Λ∨/Λ。
- p.104：(7.1) `Υ: Z×Z→U(1)` 对称 perfect pairing；(7.2) `Υ(a,b)=exp(2πi⟨a,b⟩)`；"A Gad-bundle E on M has a characteristic class ξ(E) that takes values in H²(M,Z)"；Gad=SO(3) 时 ξ=w₂。
- p.105–106：(7.3)–(7.6)；M=S¹×W，`H²(M,Z)=H¹(W,Z)⊕H²(W,Z)`，ξ=a⊕m；(7.7)(7.8) e∈Hom(H¹(W,Z),U(1))，m∈H²(W,Z)，E≅M；(7.9) `S: H_{e,m}→H_{−m,e}`，同时 τ→−1/τ。
- p.109–110：(7.12) `Θ_kiΘ_jkΘ_ij = f_ijk ∈ Z`；"The element ζ is known to be non-trivial; it is the obstruction"；(7.13) `ζ = ξ(E_ad)`；p.110："the f_ijk define the class ζ = ξ(E_ad) ∈ H²(M_H(Gad,C),Z)"。
- p.111–114：(7.18)–(7.24)；`b_{e₀}=e₀(ζ)∈H²(M_H(Gad),U(1))`；p.113："for e0 ≠ 0, the Chan-Paton bundle ... is a twisted vector bundle, twisted by b_{e0}=e0(ζ)"；"the universal bundle E_̺ in the representation ̺ is an example of a twisted vector bundle"；p.114："be0 is trivial when restricted to a point, so zerobranes exist for any e0"。

### 3.3 逐步推导
**(a) 中心与配对.** G=SU(N) 单连通，G_ad=PSU(N)，Z:=π₁(G_ad)=Z_N=Z(G)。配对 `Υ(a,b)=exp(2πi ab/N)`（把 a,b∈Z_N 用整数代表元表示；独立于代表元的选择）。它的对偶群 Z∨=Hom(Z_N,U(1))≅Z_N。

**(b) S-对偶对 (e,m).** (7.9) 在 (e,m) 坐标中即
```
S : (e,m) ↦ (−m, e)      ⟺  2×2 矩阵 [[0,−1],[1,0]]（作用在列向量 (e,m)^T）
T : (e,m) ↦ (e+m, m)     ⟺  [[1,1],[0,1]]
```
直接验算（附录 D）：
```
S² = −I, (ST)³ = −I,  Υ(Sv,Sw) = Υ(v,w)（对所有 v,w∈Z_N×Z_N，N=2,3,4,5,7 均通过）
S(1,0) = (0,1)
```
`S(1,0)=(0,1)` 正是"纯电（Wilson）↔ 纯磁（'t Hooft）"：Wilson 线 W 的标签 (e,m)=(1,0) 在 S 下变成 't Hooft 线 T 的标签 (0,1)。(6.17) 的行向量版（b3 第 6 条、附录 C）与 (7.9) 只差记号次序（(6.17) 用 (m,n)=(m,e) 排列，其中 n 是 exp(−n∮Â) 的系数），两者都满足 S²=(ST)³=−I。

**(c) ζ 落在哪里.** 原文 p.104 明确 ξ(E)∈H²(M,Z)，其中 **Z=π₁(G_ad) 是有限群**（不是整数）。对 SU(N)：Z_N，故
```
ζ = ξ(E_ad) ∈ H²(M_H(G_ad,C), Z_N)
```
它是"G_ad-丛提升为 G-丛"的阻碍（(7.12) 的闭链 f_ijk 定义 ζ，再证 ζ=ξ(E_ad)）；不是 H²(M,Z) 的整数系数。报告 §2.2.1/§2.2.2 只写 "H²(M,Z)" 而未点明 Z 是有限中心，容易被读成整数系数——这是 (中) 级问题（E3）。

**(d) e₀=0 与 universal bundle.** e₀∈Z∨=(Z_N)∨，b_{e₀}=e₀(ζ)∈H²(M_H,U(1))。"universal bundle 存在（无扭量）"等价于 `e₀(ζ)=1`。而 ζ 是 H²(·,Z_N) 中的非平凡类（(7.12) 后文："ζ is known to be non-trivial"），其阶为 N（生成 Z_N 的类），故
```
e₀(ζ) = exp(2πi e₀/N) = 1  ⟺  e₀ = 0 mod N
```
即 **只有 e₀=0 时 Chan-Paton 丛是普通丛（untwisted），universal bundle 以真丛形式存在**；e₀≠0 时只能要 twisted bundle（扭量 b_{e₀}=e₀(ζ)），此时 E_̺（中心特征等于 e₀ 的不可约表示 ̺ 的 universal bundle）就是扭量为 b_{e₀} 的 twisted bundle（p.113）。另一方面任何 e₀ 都有 twisted 零膜（p.114：B-field 限制到点是平凡的）。

### 3.4 具体算例
附录 D 输出：N=2,3,4,5 时配对保持、S(1,0)=(0,1)、T(0,1)=(1,1)、S²(1,0)=(−1,0) mod N；`b_{e₀}=exp(2πi e₀/N)` 仅在 e₀=0 时为 1。N=2：ζ 阶 2，e₀∈{0,1}；N=3：e₀∈{0,1,2}，只有 e₀=0 无阻碍。

### 3.5 与报告比
- 报告 §2.2.1 引 Table 3、(7.1)–(7.9) 正确（A）；但没写 S 的矩阵、没做 SU(N) 显式验证（任务单 item 3 要求）。
- 报告 §2.2.2 的 ζ=ξ(E_ad)、twisted 扭量正确（A），但未澄清 Z 的系数群，也未给 e₀=0 的判据（E3）。
- 报告把 (7.9) 说成"S-对偶交换 E 与 M"并类比 (6.17)：方向正确，但没写出矩阵作用与 Wilson→'t Hooft 的具体验证（E7）。

### 3.6 判定
**(A)** Z=π₁(G_ad)=Z_N、S 矩阵、ζ∈H²(·,Z_N)、e₀=0 ⇔ 无阻碍，均可直接验证；报告事实层无硬错，但缺"Z 是有限中心"的澄清与显式矩阵（(B) 级缺口）。

---

## 4. §8：Wilson 作用在电特征膜上

### 4.1 问题
U(1) 情形 U↦U⊗E_p(R) 的显式"阶化"（任务单提到的"(8.x)/P 的空间=O(p)"）；验证 e₀→e₀+θ_R 与 m₀→m₀+ξ(^L R) 的符号；为什么这里只能对"电"干净。

### 4.2 原文
- p.116（`p117.txt`）：(8.1) `W_S(R) = P exp(−∫_S (A+iφ))`；"The effect ... is to add an external charge, in the representation R, whose trajectory in spacetime is S."
- p.117–119：(8.2)–(8.5)；E=(Φ×1)*Ê、𝒜 替换为 Φ_p*(Â)；(8.5) `W_R(S)=P exp(−∫_γ Φ_p*(Â))`。
- p.119（`p120.txt`）：(8.7) `U → U⊗E_p(R)`；E(R) 一般是 twisted bundle，扭量 θ_R(ζ)；"it is the character of the center of the gauge group determined by R"；`b_{e₀}=e₀(ζ)`，`ζ=ξ(E_ad)`；张量积使 b→b+θ_R(ζ)；"it changes the discrete electric field studied in section 7 by e0 → e0 + θR"；(8.8) `e₀ → e₀ + θ(^L R)`。
- p.120（`p121.txt`）：Fig.11 cobordism；`m₀ ∈ H²(C,π₁(G))`；'t Hooft 算子 T(^L R) 由 CP¹ 上的 G-丛 E(^L R) 构造，`ξ(^L R)=ξ(E(^L R))`；(8.9) `m₀ → m₀ + ξ(^L R)`；"This statement ... just comes from the behavior of the characteristic class under cobordism"。
- p.121（`p122.txt`）：E_p(R) 在每个复结构全纯；§8.2；p.122（`p123.txt`）：电特征膜 = 不同 e₀ 的 twisted 零膜之和（点点上扭量平凡）；磁特征膜 = 不同 m₀ 分量上的膜之和；"Hecke eigensheaves are supported on the union of all topological components of M(G,C)"。

### 4.3 逐步推导
**(a) U(1) 的显式版本（B 级重建；原文 §8 无 U(1) 小节，(8.x) 并不存在）.**
G=U(1)：M_H(U(1),C)=T*Jac(C)，universal line bundle = Poincaré 线丛 L 的拉回；rep=电荷 n∈Z，E(R)=L^{⊗n}，θ_n=n（中心特征）。
```
(8.7)  U ↦ U⊗L^n ;   点膜: U_x ⊗ L^n = U_x ⊗ L^n|_x ,  V = L^n|_x（复直线）
```
按电荷 n 的"阶化"：n=0 平凡、n>0 与 n<0 互为对偶；在 CP¹ 上 L=O(1)（L^n=O(n)，∫c₁=n）。任务单的"P 的空间=O(p)"应是"CP¹ 上的线丛=O(k)"这一事实：'t Hooft 算子在横截 S²≅CP¹ 上给出 U(1)-丛 O(m)，m=磁荷∈π₁(U(1))=Z；π₁ 的层面积分给出通量 m。**报告把 U(1) 重建标为 (B)/(C) 是恰当的**；但第①、⑤条有误（E3、E4）。

**(b) e₀→e₀+θ_R 的符号（+）.**
把 brane 的扭量记为 b（平坦 B-field）。张量积的过渡函数相乘，故扭量在 H²(·,U(1)) 中**相加**：
```
U  twisted by b,  E  twisted by θ_R(ζ)  ⇒  U⊗E  twisted by b + θ_R(ζ)
b_{e₀} = e₀(ζ)  ⇒  (e₀+θ_R)(ζ) = e₀(ζ)+θ_R(ζ)
```
由配对非退化（(7.1)）得 e₀ ↦ e₀+θ_R，**符号为正**。不是减号：张量积不会把扭量反号。

**(c) m₀→m₀+ξ(^L R) 的符号（+，但有约定级注记）.**
Fig.11 的 cobordism 论证：三维流形的边界 C ⊔ C′ ⊔ S²，G-丛的特征类在图示定向下满足 m₀(C′) = m₀(C) + ξ(S²)，故操作给 m₀ ↦ m₀+ξ(^L R)，符号为正（这是原文的陈述，且由 cobordism 不变性直接给出）。
**但**用 (7.24) S:(e₀,m₀)→(−m₀,e₀) 做一致性检查会发现：把对偶理论 (8.8)（e₀' 的 Wilson 平移）翻译到 G 侧，e₀'=−m₀，得到 m₀↦m₀−θ(^L R)。与 (8.9) 的 +ξ 对照，要求
```
ξ(^L R) = −θ(^L R)   （在 (7.1) 的 Υ-配对下识别 Z_N ≅ (Z_N)∨ 时）
```
对 Z₂（SU(2)）不可见；N>2 时才是可区分的符号约定。原文没有对此说明；报告完全没有核符号（E6）。这是原文的"约定级空白"，不是硬矛盾，但报告把它当 (A) 引用是不妥的。

**(d) 为什么只有"电"干净.**
- Wilson 算子是 **order operator**：有经典表达式 (8.1)-(8.6)，作用于膜 = 张量积 (8.7)，且 S=γ×p 时保 (B,B,B)（p.121–122；E_p(R) 在每个复结构全纯）⇒ 在膜范畴中逐点可算，零膜处由 (8.10) 自动满足。
- 't Hooft 算子是 **disorder operator**：它改变 m₀（拓扑类），作用后膜的支撑换到 M_H 的另一拓扑分量/Hitchin 纤维；膜范畴层面的对应是 **Hecke 对应**（不是张量积），需要 §9–§10；磁特征膜是不同 m₀ 分量上膜之和（p.122–123），数学侧即"Hecke 特征层支撑在所有拓扑分量之并"。
- 电侧之所以仍能"干净"到可算：精确地说电特征膜是不同 e₀ 的 twisted 零膜之和，但 B-field 限制到点是平凡的，各 e₀ 的零膜同构（p.123），局部计算（点支撑）不受扭量影响；磁侧没有这一简化。

### 4.4 具体算例
SU(2)：R 为中心特征非平凡的表示（如 fund）时 θ_R 是 Z₂ 的非平凡特征；e₀∈{0,1}，e₀→e₀+θ_R 翻转；m₀ 同理。U(1)：e₀∈Z（若按 §7 的 Z∨=Hom(U(1),U(1))=Z），θ_n=n，形式地 e₀→e₀+n；但 U(1) 的 π₁(G_ad)=0 ⇒ ζ=0 ⇒ b_{e₀}=1 恒成立，扭量永远平凡（见 E3、E4）。rank 见附录 E。

### 4.5 与报告比
- 报告 §2.3.1 抄 (8.1)–(8.9) 准确（A）；(8.7) 的"E(R) 一般不存在为丛、只存在为 twisted bundle，扭量 θ_R(ζ)"转述正确。
- 报告 §2.3.2：②③④ 正确（M_H=T*Jac，L^n，(8.7)）；第①条"G=U(1) 时群中心就是 U(1) 本身"与 §7 的 Z=π₁(G_ad) 定义不符（U(1)：π₁(G_ad)=0）；第⑤条"e₀→e₀+n 公式形式上仍成立"不成立（ζ=0 ⇒ 无扭量 ⇒ 无 B-field 平移）——应标 (C) 形式类比（E3、E4）。
- 报告 §2.3.3 的 (8.10)、"特征值=E_q(R)|_x"、磁侧=不同 m₀ 分量之和、Hecke 层支撑并集：均与原文一致（A）；但未解释"为何磁侧必须走 Hecke、电侧为何能绕过"，也未核 (8.8)/(8.9) 符号（E6）。
- 报告 §5 没有列 e₀/m₀ 符号问题。

### 4.6 判定
**(A)+(B)+(C)**：U(1) 重建的正确部分是 (B)；第①⑤条改述后才是 (C) 形式类比；(8.8)/(8.9) 的 + 号可验证，但两者在 S-对偶下的相对符号带一个约定级负号，报告完全未核（(中) 级）。"只有电侧干净"报告已触及结论（A），缺机制说明（(B)）。

---

## 5. ϑ: π₁(C) → ^L G_C 为什么"厉害"

### 5.1 问题
从 §8.2 的构造出发：零膜作为电特征膜给出的表示是什么？为什么任意点都能算？与 (4.7) 的 Higgs 丛 moduli 是什么关系？g=0 或 g=1 的平凡性检查。

### 5.2 原文
- p.121–122（`p122.txt`）§8.2 末："In the geometric Langlands program, one begins with the group ^L G and a homomorphism ϑ : π₁(C) → ^L G_C"；要求 semistable（§4.2）；"The space of such homomorphisms is the Hitchin moduli space M_H(^L G,C)"；"So ϑ defines a point x(ϑ) in M_H(^L G,C)"；"If ϑ is irreducible, then x(ϑ) is a smooth point and a zerobrane B_{x(ϑ)} supported at x(ϑ) is an electric eigenbrane"；S-对偶 ⇒ M_H(G,C) 中支撑在 Hitchin 纤维 F、带 rank-1 flat CP 丛的膜（type F）；"a Hecke eigensheaf and also a holonomic D-module"；"at least a glimmering"。
- p.122–123：§11 计划：coisotropic A-brane ⇒ D-模。
- p.51（`p052.txt`）："parametrizes stable homomorphisms ϑ:π₁(C)→G_C"（Corlette–Donaldson 定理）。
- p.43（`p044.txt`）：(4.7) `I_w → I_{λ^{-1}w}` —— **这是 U₁ 在 CP¹_h 上的作用**，不是 Higgs 丛 moduli（任务单引文有误，E8）。
- p.50–51：(4.20)–(4.21) Hitchin pair 与 ν_J=0 ⇔ 𝒜=A+iφ 平坦。

### 5.3 逐步推导
**(a) 构造.** 取不可约（或 semistable）ϑ:π₁(C)→^L G_C。由 Corlette–Donaldson，semistable 同态的同构类 = M_H(^L G,C) 的点，复结构 J 下即平坦 ^L G_C-丛。所以 ϑ 定义点 x(ϑ)∈M_H(^L G,C)。取支撑在该点的零膜 B_{x(ϑ)}（CP sheaf = skyscraper U_x）。

**(b) 给出的表示.** Wilson 线 W_q(^L R) 作用（(8.7)），零膜处 (8.10)：
```
W_q(^L R) : U_x ↦ U_x⊗E_q(^L R) = U_x⊗E_q(^L R)|_x
⇒ 本征值 = V := E_q(^L R)|_x
```
取复结构 J，universal bundle 限制到 x×C 得平坦 ^L G_C-丛 E|_x→C（Hitchin 解 ↔ 平坦丛），其单值化就是 ϑ；在表示 ^L R 中取纤维：
```
V ≅ (^L R ∘ ϑ)(π₁(C))-module 的底层复向量空间，  dim V = dim ^L R
```
即零膜作为电特征膜给出的表示 = **ϑ 在表示 ^L R 中的那一份**：`V = ^L R∘ϑ`（更准确地说，V 是平坦丛 E|_x⊗^L R 在 q 处的纤维，带 π₁(C) 的 monodromy 作用）。q 变时 V 作为平坦丛纤维变化，这正是 §6.4 所说的"本征值必须是 C 上平坦丛的纤维"。

**(c) 为什么任意点都能算.**
- 零膜支撑是**点**，任何向量丛在点上都平凡（(8.10)），本征条件的"全纯平凡"自动满足——不需要解任何方程。
- x(ϑ) 光滑（ϑ 不可约 ⇒ 稳定 ⇒ 无自同构）⇒ 可经典积掉 A_Σ,φ_Σ（p.121 的说明），局部计算合法。
- 任意 q∈C：V_q 通过平坦丛的平行移动互相典范同构，故"任意点算都一样"，且结果只依赖 ϑ 与 ^L R。
- S-对偶：B_{x(ϑ)} 的 S-对偶给出 M_H(G,C) 中支撑在 Hitchin 纤维 F 上、带 rank-1 flat CP 丛的膜（type F）；"厉害"之处：一个纯 4d 输入（同态 ϑ）+ 点膜，经 S-对偶直接产生 Hecke 特征层式的对象，且本征值自动是 ^L R∘ϑ；§9–§10 再把 't Hooft 算子与 Hecke 算子对应起来。

**(d) 与 (4.7)/Higgs 丛 moduli 的关系.** 任务单把 (4.7) 说成「Higgs 丛 moduli」属误引：(4.7) 是 U₁ 在 CP¹_h 上的作用（λ 作用、w↦λ^{-1}w）。正确的锚是 §4.2 的 (4.20)–(4.21)（Hitchin pair、稳定性、ν_J）与 p.51 的 Corlette–Donaldson 定理。关系本身很直接：x(ϑ)∈M_H(^L G,C) 正是「ϑ 对应的平坦 ^L G_C-丛」在 moduli 中的点；限制 E|_{x×C} 就是该 Higgs/平坦丛，故 (b) 的 V 就是它的纤维在表示 ^L R 中的像。

**(e) g=0 / g=1 平凡性检查.**
- g=0（C=CP¹）：π₁(C)=1，只有平凡 ϑ；Hitchin 方程的半稳定解必平凡（E 平凡、φ∈H⁰(O(−2)⊗End)=0）⇒ M_H(^L G,CP¹) = 单点。于是零膜唯一、V=^L R（平凡丛）为常向量空间 C^{dim ^L R}；Langlands 对应在此退化（没有非平凡的 Hecke 特征层）。**检查通过：一切平凡。**
- g=1（C=T²）：π₁(C)=Z²，ϑ ↔ 一对交换的 (A,B)∈^L G_C×^L G_C；M_H(^L G,T²) 是正维的（Hitchin 纤维为各向异性 torus，微分同胚于 (S¹)^{2 dim}），零膜不唯一；V_q 是平坦丛 E|_x⊗^L R 的纤维，任意 q 都同构（附录 F：交换的 diag monodromy 给出合法平坦丛，非交换则不存在）。**检查通过：构造仍在，但已非平凡；g=0 才是完全退化。**

### 5.4 具体算例
附录 F：g=1 取 A=diag(2,1/2)、B=diag(3,1/3)（SL(2,C) 中交换），AB−BA=0，平坦丛存在，纤维 C²；取非交换 (A,B) 则 AB−BA≠0，不存在平坦丛。g=0：π₁=1，唯一平坦丛，V=C^{dim R}。

### 5.5 与报告比
- 报告 §2.3.4 的转述（semistable、同态空间=M_H(^L G,C)、x(ϑ)、不可约⇒光滑、零膜 B_{x(ϑ)} 是电特征膜、S-对偶⇒type F、主断言=Hecke 特征层+holonomic D-模、"at least a glimmering"）：与原文一致（A），标 (A)+(C) 合理。
- 报告没有把本征值显式写成 ^L R∘ϑ 的表示（本复算的明确化），也没有做 g=0/g=1 检查；未纠正任务单 (4.7) 的误引（E8）。
- 报告 §2.3.4 说"原文只给 glimmering"是准确的（原文用 "at least a glimmering"）；把主断言标 (C) 合理。

### 5.6 判定
**(A) 转述 + (C) 推断**：报告此节无事实错误；本复算补出 (i) 本征值 = ^L R∘ϑ 的表示空间（dim ^L R），(ii) 任意点可算的三条理由（点支撑+平坦丛+光滑性），(iii) g=0/g=1 检查。任务单的 (4.7) 引文错误应记在任务单侧（E8），报告未纠正但亦未犯此错。

---

## 6. 发现的问题清单

| 编号 | 严重度 | 报告哪里错/缺 | 原文依据 | 怎么改 |
|---|---|---|---|---|
| **E1** | 中 | 报告 §5.2 自报 (6.13)→(6.14)"差一个负号"，并怀疑 `∫F₀=−2πi` 已含负号；§2.1.3 未做定向缩并 | p.86 (6.12) `ǫ₄=ds∧dr∧dVol`；p.86 缩并句；p.87 "integral of F0 over a fiber is −2πi" | **假警报**。按 i_{−∂_r}ǫ₄=+ds∧dVol、F₀∧δÂ=+f ds∧dθ∧dφ 计算，δ_TĨ_θ=(imΨ/2π)(−2πi∮)=+mΨ∮，与 (6.14) 自洽。删去"符号差"的怀疑，改为写出缩并的一行验算，并注明 ∮F₀=−2πi 本身正确。 |
| **E2** | 中 | 报告 §2.1.2 把 (6.8)→(6.9) 判为"可直接代入验证"的 (B)，但 §5.1 又自承未逐项算清（矛盾）；且未指出定向依赖 | p.83 (6.9)；p.85–86 (6.11)(6.12)；p.23 χ_± 定义 | 统一改为"已验算"(A)，并给出等价式 F=−⋆₄dφ、dφ=−⋆₄F 与显式分量/定向验算（附录 A）；明确 (6.8)+(6.9) 只在 ds-first 定向下成立。 |
| **E3** | 中 | 报告 §2.2.1/§2.2.2 写 ξ(E)、ζ∈H²(M,Z) 未说明 Z=π₁(G_ad)（有限中心）；SU(N) 时为 H²(·,Z_N)；未给 e₀=0 判据 | p.104 "ξ(E) ... takes values in H²(M,Z)"（Z=π₁(G_ad)）；p.110 "ζ=ξ(E_ad)∈H²(M_H(Gad,C),Z)"；p.113 twisted bundle | 补一句"Z=π₁(G_ad)=Z(G)（G 单连通）"；给出 ζ 的阶=N ⇒ b_{e₀}=exp(2πi e₀/N) ⇒ e₀=0 ⇔ untwisted universal bundle（附录 D）。 |
| **E4** | 中 | 报告 §2.3.2 ①"G=U(1) 时群中心就是 U(1) 本身"（与 §7 的 Z=π₁(G_ad) 定义冲突）；⑤"e₀→e₀+n 公式形式上仍成立"（U(1) 中 ζ=0，扭量恒平凡） | p.103 Z=π₁(G_ad)；p.104 ξ∈H²(M,Z)；p.119 b_{e₀}=e₀(ζ)；p.113 twisted | ①改为"U(1) 的 center 连续（=U(1)），但 §7 的 Z=π₁(G_ad)=0，故 §7 框架不适用"；⑤改为"形式类比 (C)：若硬把 center(U(1)) 当 Z，则 Z∨=Z 给出 e₀∈Z、θ_n=n、e₀→e₀+n；但此时 ζ=0，B-field 平移无物理内容"。 |
| **E5** | 低 | 报告 §5.3 (6.17) 矩阵次序未验证（在 Ψ=0 退化点试过失败） | p.86–87 (6.17)；n=−mΨ | 销项：T=(1,1,0,1)、S=(0,−1,1,0) 直接验算 n'=−m'Ψ' 成立（附录 C）；注意 Ψ=0 处 S 退化（分母），不是反例。 |
| **E6** | 低 | 报告未核 (8.8)/(8.9) 的符号；未注意两条式子在 (7.24) 下相对符号需约定 | p.119 (8.8)；p.120 (8.9) 与 Fig.11；p.111 (7.24) | 补注：e₀→e₀+θ_R 的 + 号来自扭量在张量积下相加；m₀→m₀+ξ 的 + 号来自 cobordism。用 (7.24) 翻译 (8.8) 到 G 侧得 m₀→m₀−θ(^L R)，与 (8.9) 对照要求 ξ(^L R)=−θ(^L R)（Υ-配对下；Z₂ 不可见）。属约定级，原文未说明，报告应按 (C) 标注。 |
| **E7** | 低 | 报告未给 E_q(R)|_x 的秩（=dim R）；未给 SU(N) 的 S/T 矩阵与 Wilson↔'t Hooft 显式验证；未做 U(1) 的显式阶化 | p.95 (6.22)；§8.2；p.106 (7.9) | 补：rank=dim R（附录 E）；S=[[0,−1],[1,0]]、T=[[1,1],[0,1]]、S²=(ST)³=−I、配对保持、S(1,0)=(0,1)（附录 D）；U(1)：E(R)=L^{⊗n}，CP¹ 上 O(m)（B 级重建，原文 §8 无 U(1) 小节）。 |
| **E8** | 低 | 任务单把 (4.7) 引作"Higgs 丛 moduli"；报告未纠正 | p.43 (4.7) 是 `I_w→I_{λ^{-1}w}`（U₁ 在 CP¹_h 上的作用）；正确锚为 §4.2 (4.20)-(4.21)、p.51 Corlette–Donaldson | 报告应在对应位置注明：Higgs moduli 的正确原文锚是 §4.2 与 p.51；报告未犯此错，但引用链应补。 |
| **E9** | 低 | 任务单写"∮_{S²}F/2π=1"；报告 §2.1.2 转述为 ∮iF/2π=1（正确），但未指出任务单的因子遗漏 | p.82 "∫_Y iF/2π = 1"；(6.7) 的 i/2 因子 | 报告可加一句"任务是 ∮iF/2π=1（即 ∮F=−2πi）；报告的转述正确"。 |

**总判定**：高 0 / 中 4 / 低 5。报告的事实转述大部分正确；主要缺陷集中在 (i) (6.13)-(6.14) 符号的自我怀疑（E1）、(ii) (6.8)-(6.9) 的"已验"标记与 §5.1 矛盾且缺定向（E2）、(iii) §7 的 Z 是有限中心这一关键澄清（E3）、(iv) U(1) 重建的第①⑤条（E4）。

---

## 附录：可重跑 python（≥5 段）

运行环境：任意 Python 3 + numpy。所有打印均为 ASCII。预期输出写在每段末尾。

### A. (6.8) ⟺ (6.9)：四维 Hodge 星与定向
```python
# A: check (F+dphi)_+ = (F-dphi)_- = 0 for (6.9), with orientation eps4 = ds^dr^dVol
def wedge(A,B):
    out={}
    for I,a in A.items():
        for J,b in B.items():
            if set(I)&set(J): continue
            seq=list(I)+list(J)
            inv=sum(1 for p in range(len(seq)) for q in range(p+1,len(seq)) if seq[p]>seq[q])
            key=tuple(sorted(seq)); out[key]=out.get(key,0)+((-1)**inv)*a*b
    return out
def sgn_perm(seq,O):
    pos=[O.index(i) for i in seq]
    inv=sum(1 for p in range(4) for q in range(p+1,4) if pos[p]>pos[q])
    return (-1)**inv
def star(F,O):
    out={}
    for I,c in F.items():
        J=tuple(sorted(set(range(4))-set(I)))
        out[J]=out.get(J,0)+sgn_perm(list(I)+list(J),O)*c
    return out
def clean(F): return {k:v for k,v in F.items() if v!=0}
def eq(F,G):
    F,G=clean(F),clean(G)
    return all(abs(F.get(k,0)-G.get(k,0))<1e-12 for k in set(F)|set(G))
x,y,z=0.3,0.4,0.7; r=(x*x+y*y+z*z)**0.5
ds={(3,):1}
alpha={(0,):-x/r**3,(1,):-y/r**3,(2,):-z/r**3}          # d(1/r)
def star3(v):
    out={}
    for I,c in v.items():
        J=tuple(sorted(set(range(3))-set(I)))
        seq=list(I)+list(J)
        inv=sum(1 for p in range(3) for q in range(p+1,3) if seq[p]>seq[q])
        out[J]=out.get(J,0)+((-1)**inv)*c
    return out
F=clean({k:0.5j*v for k,v in star3(alpha).items()})      # (i/2)*star3
dphi=clean(wedge({k:0.5j*v for k,v in alpha.items()},ds)) # (i/2) d(1/r)^ds
for name,O in [("eps4=ds^eps3 (text)",(3,0,1,2)),("eps4=dx^dy^dz^ds (ds last)",(0,1,2,3))]:
    Fp={k:F.get(k,0)+dphi.get(k,0) for k in set(F)|set(dphi)}
    Fm={k:F.get(k,0)-dphi.get(k,0) for k in set(F)|set(dphi)}
    Pp={k:0.5*(Fp.get(k,0)+star(Fp,O).get(k,0)) for k in Fp}
    Pm={k:0.5*(Fm.get(k,0)-star(Fm,O).get(k,0)) for k in Fm}
    print(name,": (F+dphi)+ == 0 ?",eq(clean(Pp),{}),"; (F-dphi)- == 0 ?",eq(clean(Pm),{}))
print("F == -star_text(dphi) ?",eq(F,clean({k:-v for k,v in star(dphi,(3,0,1,2)).items()})))
print("dphi == -star_text(F) ?",eq(dphi,clean({k:-v for k,v in star(F,(3,0,1,2)).items()})))
```
预期：
```
eps4=ds^eps3 (text) : (F+dphi)+ == 0 ? True ; (F-dphi)- == 0 ? True
eps4=dx^dy^dz^ds (ds last) : (F+dphi)+ == 0 ? False ; (F-dphi)- == 0 ? False
F == -star_text(dphi) ? True
dphi == -star_text(F) ? True
```

### B. 通量归一化与 (6.13)→(6.14) 的定向符号
```python
# B: int_S2 iF0/2pi = 1 ; delta_T I_th = + m*Psi*int_S dA  (matches (6.14))
import numpy as np
trap = getattr(np,"trapezoid",np.trapz)
th=np.linspace(0,np.pi,400001); ph=np.linspace(0,2*np.pi,2001)
I=trap(np.sin(th),th)*trap(np.ones_like(ph),ph)          # int_S2 dVol at r=1 = 4pi
F0=-0.5j*I                                              # -(i/2)*4pi = -2 pi i
print("int_S2 dVol =",round(I,6)," 4pi =",round(4*np.pi,6))
print("int F0 =",round(F0.real,6),"+",round(F0.imag,6),"i ; int iF0/2pi =",round(((1j*F0)/(2*np.pi)).real,6))
# local orientation: i_{-d/dr}(ds^dr^dVol) = + ds^dVol ; F0^dA = +f ds^dth^dph
dA=2*np.pi                                              # int_S dA
val=dA*F0
print("int_{dVeps} F0^dA =",round(val.real,6),"+",round(val.imag,6),"i")
print("delta I_th = (i m Psi/2pi)*that =",round(((1j*val)/(2*np.pi)).real,6),"*m*Psi  (= m*Psi*int dA)")
```
预期：
```
int_S2 dVol = 12.566371 4pi = 12.566371
int F0 = 0.0 + -6.283185 i ; int iF0/2pi = 1.0
int_{dVeps} F0^dA = 0.0 + -39.478418 i
delta I_th = 6.283185 *m*Psi  (= m*Psi*int dA)
```
（`6.283185 = 2π = ∮dA`；δ_T I_θ = +mΨ∮δ_TÂ 与 (6.14) 一致，故"符号差"不存在。）

### C. (6.17) 的 SL(2,Z) 行向量作用
```python
# C: (m n) -> (m n)[[d,-b],[-c,a]]  and  n = -m Psi  =>  n' = -m' Psi'
import numpy as np
def mul(g,h):
    a,b,c,d=g; e,f,gg,hh=h
    return (a*e+b*gg, a*f+b*hh, c*e+d*gg, c*f+d*hh)
def act(g,v):
    a,b,c,d=g; return np.array(v,dtype=float)@np.array([[d,-b],[-c,a]],dtype=float)
def weyl(g,psi):
    a,b,c,d=g; return (a*psi+b)/(c*psi+d)
T=(1,1,0,1); S=(0,-1,1,0)
for g,psi in [(T,0.3),(S,0.3),(T,-2.0),(S,2.0)]:
    m=3.0; n=-m*psi
    m2,n2=act(g,(m,n)); psi2=weyl(g,psi)
    print("g=%s psi=%.2f psi'=%.4f (m',n')=(%.3f,%.3f) n'+m'psi'=%.1e"%(g,psi,psi2,m2,n2,n2+m2*psi2))
print("S^2 =",mul(S,S)); ST=mul(S,T); print("(ST)^3 =",mul(mul(ST,ST),ST))
```
预期：
```
g=(1, 1, 0, 1) psi=0.30 psi'=1.3000 (m',n')=(3.000,-3.900) n'+m'psi'=4.4e-16
g=(0, -1, 1, 0) psi=0.30 psi'=-3.3333 (m',n')=(0.900,3.000) n'+m'psi'=0.0e+00
g=(1, 1, 0, 1) psi=-2.00 psi'=-1.0000 (m',n')=(3.000,3.000) n'+m'psi'=0.0e+00
g=(0, -1, 1, 0) psi=2.00 psi'=-0.5000 (m',n')=(6.000,3.000) n'+m'psi'=0.0e+00
S^2 = (-1, 0, 0, -1)
(ST)^3 = (-1, 0, 0, -1)
```

### D. SU(N)：中心、S/T 作用、配对保持、ζ 的阶
```python
# D: Z_N, S:(e,m)->(-m,e) , T:(e,m)->(e+m,m) , Upsilon((e,m),(e',m'))=exp(2pi i (e m'-m e')/N)
import numpy as np
def S_action(v,N):
    e,m=v; return ((-m)%N, e%N)
def T_action(v,N):
    e,m=v; return ((e+m)%N, m%N)
def pair(u,v,N):
    (e,m),(e2,m2)=u,v; return (e*m2-m*e2)%N
for N in [2,3,4,5,7]:
    ok=all(pair(S_action((e,m),N),S_action((e2,m2),N),N)==pair((e,m),(e2,m2),N)
           for e in range(N) for m in range(N) for e2 in range(N) for m2 in range(N))
    print("N=%d: Upsilon(Sv,Sw)=Upsilon(v,w): %s ; S(1,0)=%s ; T(0,1)=%s ; S^2(1,0)=%s"
          %(N,ok,S_action((1,0),N),T_action((0,1),N),S_action(S_action((1,0),N),N)))
for N in [2,3,4]:
    print("SU(%d): b_e0 = exp(2 pi i e0/%d); trivial only for e0 = %s"
          %(N,N,[e for e in range(N) if abs(np.exp(2j*np.pi*e/N)-1)<1e-12]))
```
预期：
```
N=2: Upsilon(Sv,Sw)=Upsilon(v,w): True ; S(1,0)=(0, 1) ; T(0,1)=(1, 1) ; S^2(1,0)=(1, 0)
N=3: ... S(1,0)=(0, 1) ; T(0,1)=(1, 1) ; S^2(1,0)=(2, 0)
N=4: ... S(1,0)=(0, 1) ; T(0,1)=(1, 1) ; S^2(1,0)=(3, 0)
N=5: ... S(1,0)=(0, 1) ; T(0,1)=(1, 1) ; S^2(1,0)=(4, 0)
N=7: ... S(1,0)=(0, 1) ; T(0,1)=(1, 1) ; S^2(1,0)=(6, 0)
SU(2): b_e0 = exp(2 pi i e0/2); trivial only for e0 = [0]
SU(3): ... trivial only for e0 = [0]
SU(4): ... trivial only for e0 = [0]
```

### E. 本征值的秩 = dim R
```python
# E: rank of E_q(R)|_x equals dim R ; scalar eigenvalue only if dim R = 1
for name,dimR in [("U(1) charge n",1),("SU(2) fund",2),("SU(2) adj",3),("SU(3) fund",3),("E6 fund",27)]:
    print("%-16s dim R = %2d ; rank of E_q(R)|_x = %2d ; H_{B,B_x} dim = 1 -> H_{B,B_x(x)V} dim = %2d"
          %(name,dimR,dimR,dimR))
print("scalar eigenvalue (V=C) is possible only when dim R = 1 and a trivialization of E_q(R) is chosen")
```
预期：
```
U(1) charge n    dim R =  1 ; rank of E_q(R)|_x =  1 ; H_{B,B_x} dim = 1 -> H_{B,B_x(x)V} dim =  1
SU(2) fund       dim R =  2 ; rank of E_q(R)|_x =  2 ; ... dim =  2
SU(2) adj        dim R =  3 ; ... 3
SU(3) fund       dim R =  3 ; ... 3
E6 fund          dim R = 27 ; ... 27
```

### F. g=0 / g=1：ϑ 与平坦丛的平凡性
```python
# F: g=0: pi1(S^2)=1 -> unique flat bundle ; g=1: pi1(T^2)=Z^2 -> commuting monodromies
import numpy as np
A=np.diag([2.0,0.5]); B=np.diag([3.0,1/3])               # commuting in SL(2,C)
print("g=1 commuting diag monodromies: AB-BA =",np.round((A@B-B@A).tolist(),12))
A2=np.array([[1,1],[0,1]],dtype=float); B2=np.array([[1,0],[1,1]],dtype=float)
print("non-commuting pair: AB-BA =",np.round((A2@B2-B2@A2).tolist(),12),"(no flat bundle with these monodromies)")
print("g=0: pi_1(S^2)=1 -> one flat bundle up to iso; V = C^dimR (trivial rep of pi_1)")
```
预期：
```
g=1 commuting diag monodromies: AB-BA = [[0.0, 0.0], [0.0, 0.0]]
non-commuting pair: AB-BA = [[1.0, 0.0], [0.0, -1.0]] (no flat bundle with these monodromies)
g=0: pi_1(S^2)=1 -> one flat bundle up to iso; V = C^dimR (trivial rep of pi_1)
```

### 复现说明
- 全部脚本本地可跑，无外部数据；A 的坐标为任意一般点（0.3,0.4,0.7），换点不改变布尔结果。
- B 中的 `trap` 兼容 numpy 1.x（`np.trapz`）与 2.x（`np.trapezoid`）。
- C、D、E、F 只用 numpy。所有结论均为精确有理/整数运算（A、B 为数值，误差 <1e-12）。

---

### 未完成/说明
- 任务单 item 4 提到的 §8 "(8.x) 显式阶化"在原文不存在（§8 无 U(1) 小节），本报告按 (B) 级重建处理，与报告 §2.3.2 的定位一致。
- 页图：U05 范围无页图（目录仅有 p.35–38、60–61、67、70–71 的图），因此 (6.8)-(6.9) 的"看法"以逐页文本 + 公式自洽 + 附录 A 的显式验算代替；如需要页图级复核，应补 p.83、p.84、p.95、p.121 的扫描。
- 报告 §5.4（§7.2 的 e₁、m₁ Künneth 分量）不在本复算五项内，未处理。
