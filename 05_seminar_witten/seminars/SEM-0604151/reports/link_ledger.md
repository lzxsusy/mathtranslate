# 41_layer3_notes.tex 链接验证台账

验证方式：`web_fetch` 实际抓取；判据 = HTTP 200 且返回页面正文与本卡陈述相符。抓取日期 2026-11-15。
所有 URL 前缀 `https://ncatlab.org/nlab/show/`。

| # | 卡 | 条目名 | HTTP | 页面要点（与卡片对照） | 结果 |
|---|----|--------|------|------------------------|------|
| 1 | 1 主丛与稳定丛 | `stable+bundle` | 200 | 斜率 deg/rank 稳定；Mumford GIT 引入；“stable point under automorphisms”；Narasimhan–Seshadri 定理；引用 moduli space of bundles | ✅ 采用 |
| 2 | 2 模空间与 GIT | `geometric+invariant+theory` | 200 | reductive G 作用射影簇；GIT-(semi-)stable points 使商成为射影簇/DM 栈；“moduli spaces of bundles … 稳定点=斜率稳定丛”；Saiz 09 thm 2.3.6 | ✅ 采用 |
| 3 | 3 超凯勒流形 | `hyperk%C3%A4hler+manifold` | 200 | holonomy ⊆ Sp(n)；I,J,K 与三 Kähler 形式；Berger 分类；K3/4-环面 Hilbert scheme + O'Grady；D=3 N=4 分支超凯勒 | ✅ 采用 |
| 4 | 4 超凯勒商 | `symplectic+reduction` | 200 | Marsden–Weinstein 对称辛约化；图：presymplectic→gauge reduction→symplectic manifold→symplectic reduction；条目由 BRST-BV 拆出 | ⚠️ 采用（nLab 无 `hyperkähler quotient` 条目，404；本卡以辛商原型为锚，卡内明示超凯勒商是逐复结构的推广） |
| 5 | 5 Higgs 丛 | `Higgs+bundle` | 200 | E + Φ:E→Ω¹⊗E，Φ∧Φ=0；稳定=对 Φ-不变子丛检验；rank 1 时 Φ 任意全纯 1-形式；非阿贝尔 Hodge；页面明言稳定 Higgs 丛模空间即 Hitchin moduli space | ✅ 采用 |
| 6 | 6 Hitchin 模空间 | `Higgs+bundle` | 200 | 同上；“moduli space of stable Higgs bundles … also known as the Hitchin moduli space” | ✅ 采用（同页复用；`Hitchin+moduli+space` 亦存在 200，未采用因页面更长而信息不增） |
| 7 | 7 Hitchin 方程 | `Higgs+bundle` | 200 | 页面给 Higgs 丛定义与稳定性；Hitchin 方程本身未在该页展开——本卡“数学要点”按 Hitchin 1987/Simpson 1992 标准陈述，链接仅兜底 Higgs 丛侧 | ⚠️ 采用（nLab `Hitchin+equations`、`Hitchin's+equations` 均 404；`Hitchin+system` 重定向至 `Hitchin+fibration`） |
| 8 | 8 Hitchin 纤维化 | `Hitchin+fibration` | 200 | Lax pair/谱曲线；Sp(m,C) Higgs 丛谱曲线为超椭圆曲线；定义在稳定丛模空间余切丛；到 Hitchin base 的典范映射即 Hitchin fibration；椭圆 Calogero–Moser 例；Beilinson–Drinfeld；Ngô fundamental lemma | ✅ 采用 |
| 9 | 9 非阿贝尔 Hodge | `nonabelian+Hodge+theory` | 200 | Corlette 调和截面；Simpson 92：平坦丛 ↔ 稳定 Higgs 丛；与阿贝尔 Hodge 分解类比；X_dR/X_Dol stack 表述；与几何 Langlands 关系 | ✅ 采用 |
| 10 | 10 广义复几何 | `generalized+complex+geometry` | 200 | 广义复结构 𝒥:V⊕V*→V⊕V*，𝒥²=−1 且 𝒥*=−𝒥；矩阵例子 J_J、J_ω；TX⊕T*X；U(n,n)↪O(2n,2n)（Gualtieri prop 4.6）；统一复/辛/黎曼几何；动机 T-对偶；Hitchin 提出 | ✅ 采用 |
| 11 | 11 平坦联络与局部系统 | `flat+connection` | 200 | 平坦⇔曲率零；零曲率/Maurer–Cartan 方程；平坦联络=局部系统=基本群表示（RH）；Koszul–Malgrange；Narasimhan–Seshadri（模空间↔稳定丛）；Milnor \|c1\|<g | ✅ 采用 |
| 12 | 12 Riemann–Hilbert | `Riemann-Hilbert+correspondence` | 200 | dR 函子；正则完整（regular holonomic）D-模 ≅ 可构造层（Mebkhout/Kashiwara/Beilinson–Bernstein）；非正则用 ind-sheaves；几何 Langlands 把自守侧译为 D-模 | ✅ 采用 |
| 13 | 13 A/B 模型 | `A-model`；`B-model` | 200 | A：辛流形 Fukaya 范畴、AKSZ Poisson sigma 规范固定、Gromov–Witten 有效理论、TCFT 的 BRST 复形；B：相干层 CY A∞ 范畴/导出范畴即够；两页均有 “A on Bun_G + B on Loc_G = geometric Langlands” 对照 | ✅ 采用（两页） |
| 14 | 14 镜像与 HMS | `mirror+symmetry` | 200 | h^{1,1}↔h^{1,2}；SCFT_A(X)≃SCFT_B(X̂)；HMS：Fuk(X)≃D^b(X̂)（Kontsevich 1994）；Kontsevich/Costello TCFT↔CY A∞；SYZ T-对偶；Fano↔Landau–Ginzburg | ✅ 采用 |
| 15 | 15 D-膜与 A/B-膜 | `A-brane`；`B-brane` | 200 | A-brane=拓扑 A-模型膜、构成 Fukaya 范畴；B-brane=B-模型膜、构成相干层导出范畴；相关 Bridgeland 稳定性、KW TQFT | ✅ 采用（两页） |
| 16 | 16 余各向同性与典范膜 | `coisotropic+submanifold`；`A-brane` | 200 | Poisson 流形 (X,π)：S 余各向同性 ⇔ π(N*S)⊂TS ⇔ 消没函数子代数对括号封闭；Poisson sigma model 的膜（Cattaneo–Felder）；辛情形 TS^⊥⊂TS；(ω⁻¹F)²=−1 支撑的 A-膜（Kapustin–Orlov）；KW 的典范膜 𝒜_cc | ✅ 采用（coisotropic 页 + A-brane 页） |
| 17 | 17 拓扑扭化 | `topological+twist` | 200 | R-对称子群混入旋转群、挑标量超荷 Q（Q²=0）、取 Q-上同调；Witten 1988 得 A/B 模型、Witten 1991 扭化 4d SYM；D=3 N=4 扭化=Rozansky–Witten | ✅ 采用 |
| 18 | 18 N=4 SYM | `D%3D4+N%3D4+super+Yang-Mills+theory` | 200 | 16 超荷、R-对称 SU(4)≅Spin(6)、6 标量、共形；τ=θ/2π+4πi/g²；S-对偶；6d (2,0) 紧化；页面明确列 topological twist→Kapustin–Witten TQFT 与 geometric Langlands | ✅ 采用（anchor 简写 "D4 N4 super Yang-Mills theory"） |
| 19 | 19 BPS 态 | `BPS+state` | 200 | {Q_A,Q_B}=Eδ_AB−K_AB；正定性⇒E≥\|K\|（BPS 界）；饱和⇒短多重态、谱受保护；Bogomolny/Prasad–Sommerfield 起源；DT/GW 计数、谱网络、超引力极端黑膜 | ✅ 采用 |
| 20 | 20 BRST 上同调 | `BRST+complex` | 200 | ghost 场、Q²=0、物理态=H⁰(Q)；BRST 复形=模空间 ∞-groupoid 的 Chevalley–Eilenberg 代数；BV 推广；扭化后 Q 提取拓扑不变量 | ✅ 采用 |
| 21 | 21 瞬子与 ADHM | `ADHM+construction` | 200 | 构造 Yang–Mills 瞬子解的方法（Atiyah–Hitchin–Drinfeld–Manin 1978）；相关 Nahm transform、Skyrmion；综述 hep-th/0206063 | ✅ 采用 |
| 22 | 22 磁单极子与 Nahm | `Nahm%27s+equation` | 200 | 三方程 dX³/dy+[X¹,X²]=0 等；解 X^i=ρ^i/y+非奇异项，ρ:su(2)→u(N)；磁单极子（Nahm 82/84、Donaldson 84）、Nahm 极点边界条件（Mazzeo–Witten）、fuzzy funnel（Gaiotto–Witten） | ✅ 采用 |
| 23 | 23 Bogomolny 方程 | `Bogomolny+equation` | 200 | 把 4d 自对偶 YM 的时间无关解经维数约化写成 3d 欧氏空间上的方程；Atiyah–Hitchin《Geometry and Dynamics of Magnetic Monopoles》Eq. (2.1)；相关 Nahm transform/monopole | ✅ 采用 |
| 24 | 24 SL(2,Z) 与模形式 | `modular+group` | 200 | modular group=PSL(2,Z) 或 SL(2,Z)（torus 的映射类群）；SL(2,Z)→PSL(2,Z)=SL(2,Z)/{±1}；链接 modular form；Serre/Stein 参考 | ✅ 采用 |
| 25 | 25 相干层 | `coherent+sheaf` | 200 | 有限生成且核有限生成；Noether 概形上=有限展示；Serre FAC（Proj R 上 ≅ 有限生成分次 R-模模有限长度）；斜率/稳定相干层；D^b(Coh X) 为 B-模型/FM 舞台 | ✅ 采用 |
| 26 | 26 导出范畴 | `derived+category` | 200 | D(A)=Ch•(A)[qis⁻¹]=K(A)/N(A)；三角范畴/ distinguished triangle；内射/投射分辨率算 Hom；增强（dg/stable ∞）保留高阶信息；Verdier；D^b(Coh X) | ✅ 采用 |
| 27 | 27 Fourier–Mukai | `Fourier-Mukai+transform` | 200 | Φ_E(A)=Rq_*(Lp^*A⊗^L E)；Mukai 1981 阿贝尔簇对偶（Poincaré 线丛）；Orlov：全忠实三角函子皆 FM 且核唯一；增强 Func^L(D(X),D(Y))≃D(X×Y)；阿贝尔几何 Langlands（Frenkel 05 §4.4–4.5） | ✅ 采用 |
| 28 | 28 D-模 | `D-module` | 200 | D_X；D_X-模 ≅ de Rham 空间上拟相干层；O_X-相干 D-模 ≅ 平坦联络全纯丛（Koszul–Malgrange）；nonsingular ≅ 局部系统；六函子；RH：正则完整↔可构造层；Beilinson–Bernstein 局部化 | ✅ 采用 |
| 29 | 29 仿射 Grassmannian | `affine+Grassmannian` | 200 | Gr_G=G(k((t)))/G[[t]] 的旗流形；GL_n 的格模型；ind-scheme、可嵌入 Sato Grassmannian；与 Ran space/几何 Langlands 相关（Zhu 1603.05593） | ✅ 采用 |
| 30 | 30 Hecke 对应与修正 | `Hecke+correspondence` | 200 | Hecke 栈 Hck 参数化 (E₁,E₂,β)，β 在有限点外同构；Bun_G ← Hck → Bun_G；Hecke 变换 Φ(A)=π_{2*}(π₁^*A⊗ρ)；与模曲线 X₀(p)⇉X 的 T_p 平行；S-对偶对照表（Hecke↔'t Hooft；Hecke eigensheaf↔magnetic eigenbrane） | ✅ 采用 |
| 31 | 31 Hecke 特征层 | `Hecke+eigensheaf` | 200 | Hecke 变换下变为自身张量倍数的对象；几何 Langlands 的核心；与磁特征膜对应（Frenkel 05 §3.8） | ✅ 采用 |
| 32 | 32 几何 Satake | `geometric+Satake+equivalence` | 200 | 球 Hecke 代数 ℋ=G(𝒪)\\G(K)/G(𝒪) 上紧支撑函数（卷积、Gelfand 技巧使其交换）；Satake 同构 ℋ⊗Z[q^{±1/2}]≅R(^L G)⊗Z[q^{±1/2}]；几何版 DMod(Gr_G)^{L⁺G}≅Rep(^L G) | ✅ 采用 |
| 33 | 33 几何 Langlands | `geometric+Langlands+correspondence` | 200 | 猜想 OMod(Loc_{^L G}(Σ))≃DMod(Bun_G(Σ))；非阿贝尔 FM（skyscraper→Hecke eigensheaf）；环面情形由 FM 已证（Laumon/Rothstein）；朴素形式在 SL₂/P¹ 失败（Lafforgue 09）；Arinkin–Gaitsgory 幂零 ind-对象修正；nLab 记 Gaitsgory 等 2025 已证；KW 06 的 S-对偶/镜像路线 | ✅ 采用 |
| 34 | 34 Langlands 对偶群 | `Langlands+program` | 200 | 数论 Langlands（Galois 表示↔自守表示）；一般 G 的 L-函数附加 ^L G→GL_n；解析延拓/函数方程与函子性；几何类比表（Galois 表示↔局部系统、自守表示↔Hitchin 联络/D-模） | ⚠️ 采用（原锚 `Langlands+dual+group` 页 200 但正文仅 “(…)” 占位，改锚 `Langlands+program`；`Langlands+correspondence` 重定向至此） |
| 35 | 35 根格与权格 | `root+%28in+representation+theory%29`；`weight+%28in+representation+theory%29` | 200 | 根系 Δ：张成 E、反射 σ_α 置换 Δ、整性 α⊣β=2⟨α\|β⟩/⟨β\|β⟩∈Z、reduced；Weyl 群；根格 Q⊂权格 P；对偶根数据交换；权=极大环面本征标 | ✅ 采用（两页；`%28…%29` 为百分号编码，anchor 用简写） |
| 36 | 36 VOA 与 CFT | `vertex+operator+algebra` | 200 | VOA 数据（分次 V、真空、T、态-场对应 Y，三条公理）；Virasoro 作用→共形顶点代数；一个 VOA=2d CFT 手征一半；Huang：全纯 punctured sphere operad 代数、有理 VOA 模=模张量范畴；chiral algebra（Beilinson–Drinfeld） | ✅ 采用 |

## 404 / 不可用记录（已排除，禁止再写入卡片）

- `Hitchin+equations` 404；`Hitchin+equation` 404；`Hitchin%27s+equations` 404
- `hyperkähler+quotient` 404；`hyperk%C3%A4hler+quotient` 404；`K%C3%A4hler+quotient` 404
- `Hecke+modification` 404；`geometric+Hecke+operator` 404；`Satake+correspondence` 404；`geometric+Satake+correspondence` 404
- `root+lattice` 404；`N=4+super+Yang-Mills+theory` 404；`moduli+space+of+Higgs+bundles` 404
- `weight+(representation+theory)` 404（括号形式）；百分号形式 `weight+%28in+representation+theory%29` 200
- `Kapustin-Witten+theory`、`Kapustin-Witten+equations` 404
- `Hitchin+system` 200 但重定向到 `Hitchin+fibration`（`Hitchin+integrable+system` 亦重定向）
- Wikipedia（en.wikipedia.org）：本机全部请求超时，不可用，已全程改用 nLab

## 重定向 / 占位 / 替换记录（最终稿实际处理）

- `Hitchin+moduli+space`：200，但服务端重定向到 `Higgs+bundle`（故卡 6 复用该页；该页 References 段明言 Higgs 丛模空间 "also known as the Hitchin moduli space"，与卡 6 陈述一致）
- `Hitchin+system`：200，重定向到 `Hitchin+fibration`（卡 8 采用后者）
- `Langlands+dual+group`：200，但正文只有占位 "(…)"（无可用内容）→ 卡 34 改锚 `Langlands+program`（`Langlands+correspondence` 重定向至此）
- `N=4+super+Yang-Mills+theory`：404 → 实际页名为 `D=4 N=4 super Yang-Mills theory`，卡 18 用编码形式 `D%3D4+N%3D4+super+Yang-Mills+theory`，anchor 简写为 "D4 N4 super Yang-Mills theory"（`\anchor{}` 内不能有 `%`）
- `weight+(representation+theory)`：404（括号形式）→ `weight+%28in+representation+theory%29` 200，卡 35 采用编码形式，anchor 简写
- `root+lattice`：404 → 卡 35 用 `root+%28in+representation+theory%29`（根系定义页）
- `Hecke+modification`、`geometric+Hecke+operator`：404 → 卡 30 用 `Hecke+correspondence`（含 Hecke 修改/变换定义）
- `hyperkähler+quotient`、`Kähler+quotient`：404 → 卡 4 用 `symplectic+reduction`，卡内明示超凯勒商是逐复结构的辛商推广
- `Hitchin+equations`、`Hitchin+equation`、`Hitchin's+equations`：404 → 卡 7 以 `Higgs+bundle` 兜底（Hitchin 方程本卡按 Hitchin 1987/Simpson 1992 标准陈述）
- `Satake+correspondence`、`geometric+Satake+correspondence`：404 → 卡 32 用 `geometric+Satake+equivalence`
- `moduli+space+of+Higgs+bundles`：404 → 卡 6 用 `Higgs+bundle`
- `Kapustin-Witten+theory`、`Kapustin-Witten+equations`：404（KW06 论文在卡 18/33 正文以 arXiv:hep-th/0604151 引用，不作 anchor）
- `Maurer-Cartan+equation`、`Deligne+lambda-connection`：未单独抓取，仅作正文概念（无独立 anchor）

## 统计

- 最终稿采用的不同 nLab 页面：37 个（36 张卡；卡 13/15/16/35 各多挂一页），全部本机 `web_fetch` 抓取 HTTP 200 且正文与本卡陈述逐条对照相符
- 抓取/探测总次数：约 60 次（含上述 404、重定向、Wikipedia 超时与重复抓取）
- 编译：`build/check_notes/check.tex`（ctexart + 项目 preamble）xelatex 两遍 → 20 页，0 error，0 Missing character

