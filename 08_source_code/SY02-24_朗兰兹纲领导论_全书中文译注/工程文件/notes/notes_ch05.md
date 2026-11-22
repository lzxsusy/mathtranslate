# 第 5 章 通读笔记

底本：E. de Shalit, *L-Functions of Elliptic Curves and Modular Forms*，
Bernstein–Gelbart 编《An Introduction to the Langlands Program》第 5 章。
PDF 94–113，印刷页 89–108。页图 `work/pages/ch05/p0094.png`–`p0113.png`
（文件名即 PDF 页；mutool 本次输出沿用 PDF 页号，未从 0001 重编）。

## 三句话主旨

1. 本章把第 4 章末尾的椭圆曲线 L 函数讲成一条完整的逻辑链：复环面—代数定义—同源与自同态—Tate 模—Weil 配对—好归约—Euler 乘积。
2. 再用模曲线 X₀(N) 的雅可比簇 J₀(N)、Hecke 代数与 Eichler–Shimura 同余关系，说明模形式的 L 函数满足函数方程，从而把 Hasse–Weil 猜想化归为模性。
3. 最后陈述 Shimura–Taniyama–Weil 猜想（每一条 Q 上椭圆曲线都同源于某个 E_f），并交代 1995–2001 年的证明史。

## 逐节内容地图

- 引言（p.89）：从上一章的 Artin 表示过渡到 ℓ 进表示；基域限制为 Q，代数簇取亏格 1 曲线，指标 i 取 1。
- §1 椭圆曲线。1.1 复情形：E_τ=C/(Z+Zτ)，℘ 函数，(1.4) Weierstrass 方程，(1.6) 函数域，(1.7) 判别式，群律的几何描述。
- 1.2 一般域：光滑射影几何不可约亏格 1 加 F 有理点；Mordell–Weil；与 Jacobian、Picard 簇的典范同构；Abel–Jacobi 定理。
- 1.3 自同态环：同源次数 (1.9)，对偶同源 (1.10)，CM 与二次虚域，特征 p 的超奇异/常，Deuring 定理，次数是二次函数 (1.11)。
- §2 ℓ 进表示。2.1 Tate 模 (2.1)，char p 时 T_pE 为 Z_p 或 0；det T_ℓ(α)=deg α (2.2)；Serre 的开像定理；Faltings 定理。
- 2.2 Weil 配对：e_N 的构造 (2.7)–(2.8)，复情形规范化 (2.6)，det ρ_ℓ=χ_ℓ (2.9)，V_ℓ 与 V̌_ℓ≅V_ℓ(−1)。
- 2.3 好/坏归约：概形定义，极小 Weierstrass 方程，乘性/加性/半稳定，结点与尖点；Ogg–Néron–Shafarevich 判别法（定理 2.3），惯性群三行表（p.97）。
- §3 Hasse–Weil L 函数。3.1 定义 (3.1)–(3.7)，a_p 与 Hasse 界 (3.2)–(3.4)，三条注记 (a)(b)(c)(d)：étale 上同调、zeta 函数 (3.8)–(3.10)、函数域、几何 Frobenius (3.11)。
- 3.2 导子：四条指数规则（好/乘性/加性 p≥5/p=2,3）。
- 3.3 完备 L 函数 (3.12)，Hasse–Weil 猜想 (3.13)，BSD 与消失阶。
- 3.4 CM 情形：O_K≅End(E/K) (3.14)，Hecke 特征 ψ (3.15)–(3.16)，N=d_K N𝔣 (3.17)，L(ψ,s) (3.18)，L(E/Q,s)=L(ψ,s) (3.19)。
- §4 模曲线与雅可比簇。4.1 Y₀(N)=Γ₀(N)\ℌ (4.1)–(4.2)，模解释 (4.3)，尖点，典范模型（Kronecker–Shimura、Igusa、Deligne–Rapoport），ω_f=2πif dz (4.4)–(4.5)。
- 4.2 模雅可比簇：T_ℓJ₀(N) (4.6)，好归约与无分歧 (4.7)。
- 4.3 Hecke 代数：对应与 γ:Jac(X)→Jac(X′) (4.8)–(4.9)，T_p 对应，N 为素数 (4.10)，半单与本征形式基。
- §5 Eichler–Shimura 同余关系。5.1 φ_E:E→E^(p) (5.1)，对偶 φ̃ (5.2)，F 与 V (5.3)–(5.4)，定理 5.1：T̃_p=F+V (5.5)。
- 5.2 推论：Weil 1948 的 RH for curves，特征值 λ_i,λ̄_i 与 a_{p,i}，Euler 因子 (5.6)，推论 5.2（Shimura、Carayol）：L(X₀(N),s)=∏L(f_i,s) (5.7)–(5.9)。
- §6 一致化与 STW 猜想。6.1 有理 Hecke 代数 (6.1)，投影 e_f 与商 E_f，定理 6.1，Ogg 的导子定理。
- 6.2 猜想 6.2（STW），Weil 逆定理（定理 6.3）与扭 (6.2)，Taylor–Wiles 1995，Diamond–Taylor–Conrad–Breuil 补全；复函数论表述。
- 参考文献 [1]–[11]（p.107–108）。

## 体裁

综述式讲义章节。作者是椭圆曲线与 p 进表示专家，行文密度高，公式编号 (x.y) 与定理编号（按节）并行。
大量断言不加证明，只给“为什么重要”与历史归属；注释性插入语（caution、warning、incidently）很多，
译文用破折号与括号保留。原文用 “we” 的口吻，译文用“我们”，但避免堆砌。

## 风险点

1. **公式全部来自页图**：pdftotext 把 ℘、λ、Γ、⊛ 等全打散，(1.4)–(1.7)、(2.6)–(2.10)、(3.9)–(3.13)、
   (5.2)–(5.6) 都逐符号回图核对过。逐条对照表见文末。
2. **符号易混**：℘（Weierstrass 函数）与 p（素数）；ℓ（小写 L）与 1；λ 与 λ̄；
   E（曲线）与 𝓔（Néron 模型/曲面）；𝔣（导子理想）与 f（模形式）。
3. **上标约定**：E^(p) 是系数提升 p 次幂，E^(p⁻¹) 是系数开 p 次方（书中 (5.2) 用后者），
   两者在超奇异时重合。译文保留原符号并出注。
4. **术语**：grossencharacter 统一作“Hecke 特征（Größencharakter）”；ordinary 作“常的”；
   reduction 作“归约”；conductor 作“导子”；correspondence 作“对应”。

## 疑点清单

1. **p.89 原书笔误**：`i = 0 or 2 give ζ(s) and ζ(s+1)`。按 Hodge/étale 上同调，H²(C,Q_ℓ)≅Q_ℓ(−1)，
   对应 ζ(s−1) 而非 ζ(s+1)。已照录并出注（注 1）。
2. **p.90 (1.7) 判别式**：书中 Δ=g₂³−27g₃²，而 (1.6) 三次式 4X³−g₂X−g₃ 的判别式是 16Δ。
   本章只用 Δ≠0，故不影响；已出注（注 3）说明两个约定的差别。
3. **p.101 水平结构**：H_τ=⟨1/N mod L_τ⟩ 依赖 L_τ 的基 (τ,1)，故出现的是 Γ₀(N) 而非 Γ⁰(N)。
   已出注（注 11）。
4. **p.97 三行表**：`dim (V_ℓ)_{I_p}` 的 0/1/0 是惯性不变子空间维数，不是“坏的程度”；
   加性归约可为潜在好归约。已出注（注 7）。
5. **p.98 导子指数**：p=2,3 加性归约时指数可高于 2（Swan 导子贡献），书中只说“可能更高”，
   未给上界；译文照录，未补具体数值。这是全章唯一未查证的疑点（Ogg 公式可逐例算出，但书中未展开）。
6. **p.104 (5.2) 记号**：E^(p⁻¹) 在英文文献中不常用，通常写作 Verschiebung V:E→E^(p⁻¹)；
   已出注（注 12）解释其含义与箭头方向。
7. **p.106 “Ogg has proved that the conductor of E_f is N”**：指 E_f 的算术导子等于解析导子 N；
   原文用括号点明，译文保留。
8. **p.107 “Sometimes in the late 50's”**：指 1950 年代后期，Shimura–Taniyama 猜想流传至 Princeton；
   译文作“50 年代后期”，不改写史实。
9. **两项 Hasse 界的一致性（已排除）**：书中 (3.4) 的 Hasse 界写作 |a_p|≤2√p，而 (1.15) 写作 |1+q−#E(F_q)|≤2√q，
   两式相差 a_p=1+q−#E(F_q)，一致；无矛盾，无需出注。

## 新增术语（本章新增，补 STYLE.md 未收者）

| 英文 | 中文 | 备注 |
|---|---|---|
| elliptic curve | 椭圆曲线 | STYLE 已收 |
| isogeny | 同源 | 不用“同源映射” |
| dual isogeny | 对偶同源 | α̌ |
| endomorphism ring | 自同态环 | End(E) |
| complex multiplication (CM) | 复乘 | 首次出现给全称 |
| Tate module | Tate 模 | T_ℓE |
| Weil pairing | Weil 配对 | e_N |
| good / bad reduction | 好 / 坏归约 | |
| multiplicative / additive reduction | 乘性 / 加性归约 | semistable 半稳定 |
| node / cusp | 结点 / 尖点 | 曲线的奇点 vs 模曲线的尖点，同形异义 |
| conductor | 导子 | N，理想 𝔣 |
| Néron model | Néron 模型 | |
| inertia group | 惯性群 | I_p |
| cyclotomic character | 分圆特征 | χ_ℓ |
| odd representation | 奇表示 | 复共轭作用为 −1 |
| modular curve | 模曲线 | X₀(N), Y₀(N) |
| Jacobian | 雅可比簇 | J₀(N) |
| correspondence | 对应 | Hecke 对应 |
| eigenform | 本征形式 | normalized eigenform 规范本征形式 |
| newform / oldform | 新形式 / 旧形式 | Atkin–Lehner |
| q-expansion | q 展开 | |
| grossencharacter | Hecke 特征（Größencharakter） | 首次给原文，后文简称 Hecke 特征 |
| idèle class group | 伊代尔类群 | 与 ch06 统一 |
| Verschiebung | Verschiebung（转移） | 保留德文 |
| supersingular / ordinary | 超奇异 / 常的 | |
| potentially good reduction | 潜在好归约 | 注 8 |
| étale cohomology | étale 上同调 | 不译“埃塔勒” |
| Tate twist | Tate 扭转 | Q_ℓ(−1) |

## 页图核对记录（逐公式）

| 公式 | 页图 | 核对结果 |
|---|---|---|
| (1.1)–(1.2) | p0095 | E_τ=C/(Z+Zτ)；矩阵作用 (aτ+b)/(cτ+d) |
| (1.3) | p0095 | ℘=1/z²+Σ(1/(z−ω)²−1/ω²) |
| (1.4)–(1.5) | p0095 | ℘′²=4℘³−g₂℘−g₃；g₂=60Σω⁻⁴，g₃=140Σω⁻⁶ |
| (1.6)–(1.7) | p0095 | C(E)≅C(X)[Y]/(Y²−4X³+g₂X+g₃)；Δ=g₂³−27g₃²≠0 |
| (1.8) | p0096 | z↦(℘(z),℘′(z))=(℘(z):℘′(z):1) |
| (1.9)–(1.11) | p0097 | deg=[F(E):α*F(E′)]；α̌∘α=deg(α)·1_E；n²−tr(α)n+deg(α) |
| (1.12)–(1.15) | p0098 | φ(x,y)=(x^q,y^q)；E(F_{qⁿ})=E(F̄)[φⁿ−1]；#E=1−(λⁿ+λ′ⁿ)+qⁿ；|1+q−#E|≤2√q |
| (2.1)–(2.4) | p0099 | T_ℓE=lim E[ℓⁿ]≅Z_ℓ²；det T_ℓ(α)=deg α；配对 T_ℓE×T_ℓE→T_ℓμ；T_ℓμ=lim μ_{ℓⁿ} |
| (2.5)–(2.10) | p0100 | L=Z+Zτ；⟨ℓ⁻ⁿ,ℓ⁻ⁿτ⟩=e^{2πi/ℓⁿ}；div 公式；e_N=g(x)/g(x+b)；det ρ_ℓ=χ_ℓ；GL(2,Q_ℓ) |
| (2.11) | p0102 | T_ℓE≅T_ℓẼ |
| (3.1)–(3.4) | p0102 | det(1−p^{−s}σ_p|(V_ℓ)_{I_p})^{−1}；a_p=λ+λ′，λλ′=p；(1−a_pp^{−s}+p^{1−2s})^{−1}；|a_p|≤2√p |
| (3.5)–(3.6) | p0103 | (1−a_pp^{−s})^{−1}；L_p=1 |
| (3.7)–(3.10) | p0103 | Euler 乘积；Z(Ẽ,t)=exp(−Σv_n tⁿ/n)；有理式；Z(Ẽ,p^{−s}) |
| (3.11) | p0104 | det(1−p^{−s}σ_p^{−1}|V̌_ℓ^{I_p})^{−1} |
| (3.12)–(3.13) | p0104 | Λ=N^{s/2}(2π)^{−s}Γ(s)L；Λ(E,s)=±Λ(E,2−s) |
| (3.14)–(3.18) | p0105 | O_K≅End(E/K)；ψ((α))=α；ρ_ℓ(σ_p)=ψ(p)；N=d_KN𝔣；L(ψ,s)=Σψ(a)Na^{−s} |
| (3.19) | p0106 | L(E/Q,s)=L(ψ,s) |
| (4.1)–(4.3) | p0106 | Y₀=Γ₀\ℌ；Γ₀ 定义；H_τ=⟨1/N mod L_τ⟩ |
| (4.4)–(4.6) | p0107 | f∈S₂(Γ₀(N))；ω_f=2πif dz；T_ℓJ₀≅Z_ℓ^{2g} |
| (4.7)–(4.10) | p0108 | ρ_ℓ:G_Q→GL(V_ℓJ₀(N))；γ:Jac(X)→Jac(X′)；γ([D])=[p′_*p^*D]；N 为素数 |
| (5.1)–(5.4) | p0109–p0110 | φ_E:E→E^(p)；E^(p⁻¹)←E:φ̃；Γ={(x,x^(p))}；F:x↦x^(p)，V:x↦px^(p⁻¹) |
| (5.5)–(5.6) | p0110 | T̃_p=F+V；∏(1−λ_ip^{−s})(1−λ̄_ip^{−s})=∏(1−a_{p,i}p^{−s}+p^{1−2s}) |
| (5.7)–(5.9) | p0110–p0111 | f_i=Σa_{n,i}qⁿ；L(f_i,s)；L(X₀(N),s)=∏L(f_i,s) |
| (6.1) | p0111 | ℋ=Q[…,T_p,…]⊂End(J₀(N))⊗Q |
| (6.2) | p0112 | L(E,χ,s)=Σa_nχ(n)n^{−s} |

## 编译自测

临时目录 `work/tmp_ch05/build/`：只取 `src/main.tex` 的导言（至 `\begin{document}` 前）加
`\mainmatter\setcounter{chapter}{4}\InputIfFileExists{chapters/ch05}{}{}`，仅纳入本章，xelatex 连跑三遍。

- 三遍均 exit 0，输出 18 页（`main_ch05.pdf`）。
- `grep "^!"`：0；`Undefined control sequence`：0；`LaTeX Warning`：0；`Overfull`：0；`Missing character`：0。
- 目视检查 18 页：章标题与作者行、节/小节号（1…6、1.1…6.2）、66 个公式号、14 条译注的来源行右对齐、
  参考文献 [1]–[11] 分段续编号，均正常。
- 已修排版：注 12 中的基域由 `\mathbb{F}_p` 改为 `\mathbb{F}_q`、(3.15)(3.17) 句中公式被拆成孤行、
  (5.6) 两行公式的对齐（改用 `gathered`）、`L 级数` 统一为 `L 函数`。
- 编号说明：本章不用 `\ob`，节/小节直接用 `\section`/`\subsection`。`src/main.tex` 已有
  `\renewcommand{\thesection}{\arabic{section}}`，故输出正是原书的 1…6 与 1.1…6.2；`\ob` 走独立
  计数器 `oblk`，只印全局序号，用在小节上会变成 7、8，与原书编号不符。
- 统计：`src/chapters/ch05.tex` 635 行，14 条 `annote`，66 个 `\tag`。
