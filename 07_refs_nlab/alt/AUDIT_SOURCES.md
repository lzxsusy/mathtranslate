# 来源真实性抽查报告（第一批）

抽样范围：已交付各讲 `src/chapters/lecture*.tex` 中的 `\znote{}` / `\znoteplain{}`。
抽法：每讲顺时针均匀取 5 条（不足 5 条全查），共 **53 条**（L1 5、L2 5、L3 5、L6 5、L10 5、L12 3、L13 5、L14 5、L17 5、L18 5、L21 5）。
核查动作：①URL 实际可访问性（`curl -sS -o /dev/null -w '%{http_code}'`）；②nLab 页面 `Last revised` 与注文所写日期逐字比对；③打开页面正文读定义，判断是否真讲注文所说的概念；④教材类核对书名/章号/版次/丛书是否见于 `work/_BIB.tsv` 与对应讲 references，有无凭空页码/定理号；⑤`\znoteplain` 是否确写「无外部依据」且内容仅为上下文推断。

统计：**PASS 45 / WARN 7 / FAIL 1**（共 53 条）。
链接层面：**31 个 URL 全部 HTTP 200**；除 L12:113 外，所有注文声称的 nLab `Last revised` 与页面实际日期**逐条一致**。

| 讲 | 概念 | 等级 | 来源 | 结果 | 证据（一句话） |
|---|---|---|---|---|---|
| L1:22 | 完美域 perfect field | B | nLab "perfect field" (2017-07-21) | PASS | Definition 原文 "A field F is perfect if every algebraic extension of F is separable"，与注文一致 |
| L1:45 | 可分闭包 separable closure | B | nLab "separable closure" (2026-04-15) | PASS | Definition 给出 $K_S\simeq\{x\in\bar K\mid x\text{ 在 }K\text{ 上可分}\}$ |
| L1:79 | 分裂域 splitting field | B | nLab "splitting field" (2026-06-08) | PASS | Definition 完整：$f$ 在 $E$ 中分裂且 $E$ 由根生成，同构意义下唯一 |
| L1:139 | Dirichlet $L$-级数 | A+B | Ireland–Rosen 第 16 章；nLab "L-function" (2024-07-07) | **WARN** | 章号 16 与 references 的 `Chapter 16` 一致；但 "2nd ed., GTM 84" 在书目里不存在（书目只写 "Springer-Verlag New York, Inc. in 1990"） |
| L1:176 | 射有限完备化 $\widehat{\Z}$ | B | nLab "profinite group" (2025-07-01) | PASS | Definition: "pro-object in finite groups"，与 $\varprojlim_n\Z/n\Z$ 表述相容 |
| L2:4 | 理想类群 | B | nLab "ideal class group" (2018-05-11) | PASS | Definition 即分式理想模主理想 $=\mathrm{Pic}(\operatorname{Spec}\OO_K)$ |
| L2:13 | 分歧指数 | A | Neukirch 第 I 章 §8 | PASS | `_BIB.tsv` L2 条目写明 "Chapter I §8,§9"；无页码/定理号 |
| L2:19 | 完全分裂 | A | Neukirch 第 I 章 §9 | PASS | 章号在书目内，格式合规 |
| L2:111 | Artin 映射 | A | Cassels–Fröhlich 第 VII 章 | PASS | `_BIB.tsv` L2 有 "Chapter VII"，未加页码 |
| L2:159 | 射线类群 | A | Neukirch 第 VI 章 | PASS | 章号在书目内 |
| L3:9 | 局部整体原理 | A | Neukirch 第 VI 章 | PASS | 章号在书目内 |
| L3:23 | 局部域 | A | Neukirch 第 V 章 | PASS | 章号在书目内 |
| L3:71 | 范数子群 | A | Neukirch 第 V 章 | PASS | 章号在书目内 |
| L3:92 | 阿代尔环 | A | Cassels–Fröhlich 第 II 章 | PASS | 章号在书目内 |
| L3:96 | 伊代尔群 | A | Cassels–Fröhlich 第 II 章 | PASS | 章号在书目内 |
| L6:8 | 模形式 | B | nLab "modular form" (2025-03-13) | PASS | 页面原文 "Modular forms are also often called _classical automorphic forms_"，注文「按 nLab 的说法」有据 |
| L6:16 | Hecke 同余子群 | A | Bump《Automorphic Forms and Representations》 | PASS | `_BIB.tsv` L6 Bump 条目无章号，注文亦未写章，合规 |
| L6:47 | $q$ 展开 | B | nLab "modular form" (2025-03-13) | PASS | 页面有 Fourier 展开 $f(z)=\sum a_n e^{2\pi i n z}$，$q=e^{2\pi iz}$ 由此而来 |
| L6:60 | Eisenstein 级数 | B | nLab "Eisenstein series" (2014-03-26) | PASS | 页面 2225 字符，正文含 $G_4,G_6$、$g_2,g_3$、$\Delta$、$j$ 的材料 |
| L6:88 | 新/旧形式空间之别 | — | `\znoteplain` | PASS | 明写「上下文推断，无外部依据」，内容确为上下文区分 |
| L10:4 | 局部系统 | B | nLab "local system" (2025-04-10) | PASS | Definitions 完备，并述与 flat connection 的 Riemann–Hilbert 关系 |
| L10:26 | 有限平展覆盖 | B | nLab "etale morphism of schemes" (2026-07-03) | PASS | Definition 列出 "flat + unramified"、smooth of relative dimension 0 等等价条件 |
| L10:35 | Hausdorff 假设 | — | `\znoteplain` | PASS | 明写「上下文推断，无外部依据」，讨论射有限群的分离性假设，标记正确 |
| L10:107 | Nagata / 维数假设 | — | `\znoteplain` | PASS | 明写「上下文推断，无外部依据」，内容为假设补正的推断 |
| L10:146 | 外单值表示 | B | nLab "monodromy" (2026-11-09) | **WARN** | 页面全文无 `outer` / `Out(`（0 hits），只讲 $\pi_1(X,x)$ 在纤维上的作用；$\operatorname{Out}(\pi_1(F_x,y))$ 的表述无来源支撑 |
| L12:50 | Hecke 对应 | B | nLab "Hecke correspondence" (2026-09-07) | PASS | 页面定义对应 $\mathrm{Bun}_n\leftarrow\mathcal H_x^i\to\mathrm{Bun}_n$ 及积分变换 |
| L12:107 | 几何 Langlands 对应 | B | nLab "Langlands program" (2024-03-28) | PASS | 页面含 geometric Langlands 与 Fourier–Mukai 段落 |
| L12:113 | Hecke 特征层 | B | nLab "Hecke eigensheaf"（无 Last revised） | PASS | Idea 原文 "taken to a tensor-multiple of itself under the integral transform induced by a Hecke correspondence"；页面 footer 仅 "Created on July 2, 2014"，注文自述「未标注 Last revised」属实 |
| L13:4 | Verdier 对偶 | B+A | nLab "Verdier duality" (2026-08-11)；Peters–Steenbrink Ch. 13 §13.1 | PASS | 页面给出 $\mathbb D_X=\mathrm R\mathcal Hom(-,\omega_X)$；教材章号与 `_BIB.tsv` 一致 |
| L13:115 | 反常层 | B | nLab "perverse sheaf" (2026-10-16) | PASS | 页面给出支撑/余支撑条件与 $\operatorname{Perv}(X)$ 为阿贝尔范畴 |
| L13:141 | $t$ 结构 | B | nLab "t-structure" (2023-04-20) | PASS | 页面给出 $(D^{\le0},D^{\ge0})$ 公理与心为阿贝尔范畴 |
| L13:211 | 左右正合约定 | — | `\znoteplain` | PASS | 明写「约定不是定理」「（上下文推断，无外部依据）」，标记正确 |
| L13:215 | 交复形 / 中间延拓 | B | nLab "intersection cohomology" (2023-05-07) | PASS | Idea 讲 perversity 与奇异空间上同调，支撑递归截断构造 |
| L14:2 | Riemann–Hilbert 对应 | B | nLab "Riemann-Hilbert correspondence" (2024-08-09) | PASS | 页面陈述 D 模与可构造层/反常层的等价 |
| L14:31 | 凝聚 $D$ 模 | A+B | Peters–Steenbrink Ch. 13 §13.3–§13.6；nLab "coherent D-module" (2021-10-01) | **WARN** | nLab 该页仅 582 字符，Idea 只有 "coherent D-module (...)" 短语，**无定义**，不支撑「$\mathcal D_X$ 非凝聚 $\OO_X$-模」；教材部分合规 |
| L14:56 | 左右模修正项 | — | `\znoteplain` | PASS | 明写「（上下文推断，无外部依据）」，内容为原书含混表述的提示 |
| L14:101 | 转移双模 | — | `\znoteplain` | **WARN** | 虽标「上下文推断，无外部依据」，正文却给出译者自补的显式公式（$\mathcal D_{X\to Y}$、$\mathcal D_{Y\leftarrow X}$、$f_+$ 的导出写法），超出「上下文推断」范围 |
| L14:180 | 完整 $D$ 模 | B | nLab "holonomic D-module" (2014-02-16) | PASS | Idea 原文 "holonomic if its characteristic variety is of dimension n"，并述特征簇 Lagrange |
| L17:13 | 平坦联络 | B | nLab "flat connection" (2023-06-04) | PASS | 页面述 $R(\nabla)=0$ 与局部系统/Riemann–Hilbert 的对应 |
| L17:89 | 对偶环面 $T^\vee$ | B | nLab "abelian variety" (2026-09-26) | **WARN** | 该页正文只在 "Related concepts" 列出 Cartier duality / dual abelian group scheme，**无 $T^\vee=V^*/\Lambda^*$ 的定义** |
| L17:89 | 极化 / 主极化 | B | nLab "polarization" (2026-01-25) | **FAIL** | 页面开宗明义 "This entry is about polarization of phase spaces (or of any symplectic manifold)"，讲辛流形极化；注文讲的却是阿贝尔簇极化 $\varphi_{\mathcal L}:A\to A^\vee$——标题沾边、含义不同 |
| L17:99 | Fourier–Mukai 变换 | B | nLab "Fourier-Mukai transform" (2025-10-21) | PASS | 页面给出 $\Phi_K(E)=\mathrm Rq_*(p^*E\otimes^{\mathrm L}K)$ 及核 $\mathcal P$ 的等价性 |
| L17:149 | $\theta$ 与 $\theta^{-1}$ 的约定 | — | `\znoteplain` | PASS | 明写「（上下文推断，无外部依据）」，内容为两处丰沛方向的对照 |
| L18:5 | 根数据 | A | Springer《Reductive Groups》pp.3–27 | PASS | `_BIB.tsv` L18 条目即 Proc. Symp. Pure Math. 33 Part 1, pp.3–27，页码与书目一致 |
| L18:17 | 根系 | A | Springer《Reductive Groups》pp.3–27 | PASS | 同上 |
| L18:54 | 约化群 | A | Springer《Reductive Groups》pp.3–27 | PASS | 同上 |
| L18:118 | 相对根系 / $k$-秩 | A | Springer《Reductive Groups》pp.3–27 | PASS | 同上 |
| L18:124 | Langlands 对偶群 | B | nLab "Langlands dual group" (2014-09-07) | **WARN** | 该页仅 1343 字符，正文只有 "See at Langlands correspondence"、术语考据与参考文献，**无 $G^\vee$ 的定义** |
| L21:15 | 仿射 Grassmannian | B | nLab "affine Grassmannian" (2023-08-15) | PASS | 页面述 $G(\mathcal K)/G(\mathcal O)$ 与格模型 |
| L21:25 | ind 概形 | B | nLab "ind-scheme" (2023-11-11) | PASS | Idea 给出滤过正向极限 $\varinjlim X_n$ 的定义 |
| L21:66 | 环群 | B | nLab "loop group" (2026-03-21) | PASS | 页面区分拓扑 $\mathcal LG$ 与代数 $G(\mathcal K)$ 两层含义 |
| L21:68 | 中心扩张 | B | nLab "group extension" (2026-02-23) | PASS | Definition 原文 "If $A\hookrightarrow\hat G$ factors through the center … central extension" |
| L21:92 | Cartan 分解 | B | nLab "Bruhat decomposition" (2024-07-11) | **WARN** | 该页只定义 $G=\bigsqcup_w BwB$，全文无 `Cartan` 字样（0 hits）；注文主句 $ \operatorname{Gr}=\bigsqcup_\lambda\operatorname{Gr}_\lambda$「又称 Cartan 分解」无来源支撑，nLab 仅能支撑对照的 Bruhat 胞腔句 |

---

## 必须改的条目

### FAIL（1 条，必须改）

**L17:89 · 极化 / 主极化 —— 来源张冠李戴**
nLab `polarization` 是辛流形/相空间极化，与阿贝尔簇极化无关。已核实可用的正确替代来源（2026-11-14 实抓，HTTP 200）：

- MathWorld "Abelian Variety Polarization"，`https://mathworld.wolfram.com/AbelianVarietyPolarization.html`
- 页面正文原文："an isogeny that, over an algebraic closure, is induced by an ample line bundle"、"It is principal when it is an isomorphism"——与注文 $\varphi_{\mathcal L}:A\to A^\vee$、主极化即同构的说法完全吻合。

建议改为：
`[来源：MathWorld 词条「Abelian Variety Polarization」，\url{https://mathworld.wolfram.com/AbelianVarietyPolarization.html}（2026-11-14 访问）。]`

### WARN（7 条，建议改）

1. **L1:139**：删去书目中不存在的 "2nd ed., GTM 84"，改按 references 原样写 `Ireland--Rosen, \textit{A Classical Introduction to Modern Number Theory}, 第 16 章（本讲参考文献）`；nLab "L-function" 部分可保留。
2. **L10:146**：nLab "monodromy" 只支撑「单值表示」主句，`Out(\pi_1(F_x,y))` 的外作用表述无来源。建议删掉该断言，或在句末标「（外单值版本的表述为译者说明）」。
3. **L14:31**：删去 nLab "coherent D-module" 半句（页面无定义），只留 `Peters--Steenbrink, \textit{Mixed Hodge Structures}, Ch. 13 §13.3--§13.6（本讲参考文献）`；若要保留网络来源，改引 nLab "D-module"。
4. **L14:101**：`\znoteplain` 里的转移双模显式公式属译者推导，不是上下文推断。建议删去公式，或明确改写「以下为译者推导，原书未给出」。
5. **L17:89 对偶环面**：nLab "abelian variety" 无对偶环面定义。建议改引 nLab "Cartier duality"（2025-10-19，正文含群概形上的对偶定义），或按 alt 库 `dual_torus.md` 口径转 `\znoteplain`。
6. **L18:124**：nLab "Langlands dual group" 无 $G^\vee$ 定义。建议改引本讲参考文献 `T.A. Springer, \textit{Reductive groups}, Proc. Symp. Pure Math. 33 Part 1, pp.~3--27（本讲参考文献）`（A 级，与本讲其余四条一致）。
7. **L21:92**：nLab "Bruhat decomposition" 只能支撑对照的 $G=\bigsqcup BwB$ 句；「Cartan 分解」一词建议不挂该来源，改 `\znoteplain` 说明为文献习称，或另找含 $G(\mathcal O)$ 轨道分解的文献（需单独核）。

## 备注

- 所有 31 个 URL 均返回 200，日期无一处对不上（唯一无日期的 L12:113 与注文自述一致），说明施工员抄录 `Last revised` 是照实抄的；本轮问题全部集中在**「页面在讲别的东西」**与**「书目之外的版次/丛书号」**两类。
- 教材类（A 级）四条纯教材支撑（L18 四条 Springer）书名、页码与 `_BIB.tsv` 完全一致，无凭空页码/定理号。

---

# 来源真实性抽查报告（第二批）

抽样范围：第一批未覆盖的 12 讲 `src/chapters/lecture*.tex` 中的 `\znote{}` / `\znoteplain{}`（L4、L5、L7、L8、L9、L11、L15、L16、L19、L20、L22、L23）。
抽法：每讲顺时针均匀取 5 条（不足 5 条全查；同一行有两个注时两个都查），共 **57 条**（L4 5、L5 6、L7 5、L8 5、L9 4、L11 5、L15 5、L16 4、L19 5、L20 5、L22 4、L23 4）。
核查动作：①URL 实际可访问性（Python `urllib` 直取，记录 HTTP 状态与字节数）；②nLab 页面 `Last revised` 与注文所写日期逐字比对（含 "September  9, 2026" 这种双空格格式）；③打开页面正文读定义/首个正文段，判断是否真讲注文所说的概念；④教材类核对书名/章号/版次/丛书号是否只用了本讲 references 里有的；⑤`\znoteplain` 是否确写「无外部依据」且内容仅为上下文推断。

统计：**PASS 53 / WARN 4 / FAIL 0**（共 57 条）。
链接层面：**32 个样本 URL 全部 HTTP 200**（另多抓 1 页备查，亦 200）；32 条 nLab 注文声称的 `Last revised` 与页面实际日期**逐条一致**（其中 10 条页面日期为 "Last revised on …" 长格式，取出后与注文年月日逐字相符）。MathWorld 一条只写访问日期，无版本日期可核，合规。

| 讲 | 概念 | 等级 | 来源 | 结果 | 证据（一句话） |
|---|---|---|---|---|---|
| L4:4 | 自守 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 本讲 references 即该书写明 Chapter 7（Kudla 撰），注文未加页码/定理号 |
| L4:161 | 自守形式 | B | nLab "automorphic form" (2026-09-09) | PASS | 页面正文即以 automorphic form 为题、含 modular form/theta 语境（42 处命中），日期一致 |
| L4:186 | 抛物子群 | B | nLab "parabolic subgroup" (2014-12-04) | PASS | Definition 原文 "a subgroup P⊂G is said to be parabolic if it is closed in Zariski topology and G/P projective"，并顺带定义 Borel |
| L4:192 | 中心特征标 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 书目/章号与 references 一致，无越界信息 |
| L4:192 | 尖点自守形式 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 同上 |
| L5:11 | $(\g,O)$-模 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 本讲 references 仅此一条（Chapter 7），注文未加页码 |
| L5:28 | 可容许 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 同上 |
| L5:55 | 限制张量积 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 同上 |
| L5:119 | 超尖点表示 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 同上 |
| L5:119 | 主系列表示 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 同上 |
| L5:140 | Satake 参数 | A | Bernstein–Gelbart 2004 第 7 章 | PASS | 同上 |
| L7:8 | 椭圆曲线 | B | nLab "elliptic curve" (2025-05-11) | **WARN** | 页面确有一般 Weierstrass 方程、判别式与 "Localization at 2 and 3"；但 "elliptic integral" 全文 0 命中，开头的名称来历句无页面支撑 |
| L7:29 | $j$ 不变量 | B | nLab "j-invariant" (2015-12-09) | PASS | 页面原文给出 $(j=0)\Leftrightarrow(g_2=0)$ 等边格 Aut $=\Z/6$、$(j=1728)\Leftrightarrow(1,i)\Z$ 格 Aut $=\Z/4$、其余 $\Z/2$、$j\to\infty$ 对应 $\Delta=0$ 结点 |
| L7:76 | Tate 模 | B | nLab "Tate module" (2014-09-16) | **WARN** | 页面只有 $T_p(A)=\lim_n A[p^n]$ 的定义与文献表；"Galois" 与 "Tate conjecture" 均 0 命中，Faltings 只出现在文献行 |
| L7:78 | 同源 | A | Silverman, \textit{The arithmetic of elliptic curves}, Springer 2009 | PASS | 书目即本讲 references（vol.~106, 2009），注文未写卷号/页码 |
| L7:95 | $\ell$ 进表示 | A+B | Silverman 2009；nLab "Galois representation" (2023-04-21) | PASS | 两条来源与 references/页面均一致（页面 29 处 Galois representation，日期相符） |
| L8:13 | 紧化 | B | nLab "compactification" (2025-08-19) | PASS | 页面定义紧化为「紧空间 $C$ + 稠密嵌入 $i:X\to C$」，并明言 "Many moduli spaces … have their natural compactifications" |
| L8:30 | 模曲线 | B | nLab "modular curve" (2015-07-21) | PASS | 页面即以模曲线为题，含 $\mathcal H/\Gamma$ 与模空间语境（7 处命中） |
| L8:87 | 模空间 | B | nLab "moduli space" (2025-10-21) | PASS | 页面有 Idea、Caveat、Definition、Coarse moduli space 各节，正对应注文的「细/粗模空间」说法 |
| L8:101 | Hecke 代数 | A | Diamond–Shurman GTM 228, Section 7.9 | PASS | references 恰写 Section 7.9（并另一条 Chapter 9），注文未越出 |
| L8:170 | Jacobian 簇 | B | nLab "Jacobian variety" (2026-09-26) | PASS | 页面原文 "the Jacobian is the moduli space of degree-0 line bundles … $\mathrm{Jac}(X)=\mathrm{Pic}^0(X)$" |
| L9:72 | 函数域 | B | nLab "function field" (2022-06-05) | PASS | 页面定义函数域为 $\OO(X)$ 的分式域，并给出 function field analogy 对照表（素位↔闭点、$\Spec\Z$↔$\A^1$） |
| L9:94 | 素位 | B | nLab "place" (2015-12-17) | PASS | 页面 Idea 原文 "A place … most common one is an equivalence class of (archimedean or non-archimedean) absolute values"，与注文一致 |
| L9:114 | 阿代尔环 | B | nLab "ring of adeles" (2025-07-01) | PASS | 页面原文 "restricted product of all formal completions $k_v$ … only a finite number of components have norm greater than 1" |
| L9:153 | 局部系统 | B | nLab "local system" (2025-04-10) | PASS | 页面 Definition 给出局部常值层与局部自由+平坦联络的等价说法 |
| L11:27 | Tate 层 | B | nLab "Tate twist" (2025-08-10) | PASS | 页面以 Tate twist 为题，给出 $\Z_\ell(1)=\varprojlim\mu_{\ell^n}$ 的构造 |
| L11:88 | UFD / 正合序列 | — | `\znoteplain` | PASS | 明写「（上下文推断，无外部依据）」，内容确为对原书假设的补正说明 |
| L11:110 | 向量丛 | B | nLab "vector bundle" (2025-10-21) | PASS | 页面 Definition 即局部自由模层 / $\GL_n$ 主丛 |
| L11:116 | 模叠 | B | nLab "moduli stack" (2023-04-16) | PASS | 页面以群胚值函子/叠为题，含 moduli problem 与叠公理 |
| L11:140 | 下降数据 | B | nLab "descent" (2024-09-12) | PASS | 页面含 descent data、descent morphism 与余循环条件 |
| L15:10 | 刚性化 | — | `\znoteplain` | PASS | 明写「（上下文推断，无外部依据）」，内容为 $\C^\times$-gerbe 与标架的上下文说明 |
| L15:36 | 对称幂 | B | MathWorld "Symmetric Power"（2026-11-14 访问） | PASS | 页面原文 "The $d$th symmetric power … quotient … identifying tensors that differ by a permutation of their factors"，并述特征 0 时等同不变张量 |
| L15:38 | Abel–Jacobi 映射 | B | nLab "Abel-Jacobi map" (2023-06-09) | PASS | 页面原文 "$\Div^0(X)\to J(X)$ … defined by integration. According to Abel's theorem, its kernel consists of the principal divisors" |
| L15:104 | 几何点与 $p$ | — | `\znoteplain` | PASS | 明写「（上下文推断，无外部依据）」，为短注，内容为记号说明 |
| L15:132 | 射有限完备化 | B | nLab "profinite group" (2025-07-01) | PASS | 页面给出有限群逆向极限、紧 Hausdorff 全不连通的等价刻画 |
| L16:18 | Artin 映射 | A | Neukirch, \textit{Algebraic Number Theory}, Grundlehren 322, 第 VI 章 | PASS | 注文自述取第 2 讲 references [N]；该书目逐字一致（Grundlehren 322, Chapter VI），无凭空页码/定理号 |
| L16:20 | Artin 互反律 | B | nLab "Artin reciprocity law" (2024-06-30) | PASS | 页面 Idea 原文 "Emil Artin's reciprocity law is a reciprocity law in class field theory for global fields…"，日期一致 |
| L16:45 | 特征标层 | — | `\znoteplain` | PASS | 明写「（上下文推断，无外部依据）」，三条定义要素均取自本讲定义 2.1 |
| L16:57 | Lang 同源 | — | `\znoteplain` | PASS | 同上，内容为引理 2.2 证明中的构造说明 |
| L19:13 | Bruhat 分解 | B | nLab "Bruhat decomposition" (2024-07-11) | PASS | 页面给出 $G=\coprod_{w\in W_0}BwB$ 与 $G=\coprod_{u\in W^J}BuP_J$，并定义 Schubert 簇 |
| L19:28 | 旗簇 | B | nLab "flag variety" (2026-09-28) | PASS | 页面以旗簇 $\mathcal B=G/B$ 参数化 Borel 子群为题（18 处命中） |
| L19:57 | 球面 Hecke 代数 | A | Satake, IHES Publ. Math. 18 (1963) 5–69 | PASS | references 逐字一致（含卷期页码），注文未加定理号 |
| L19:116 | Satake 同构 | A | Satake 同上 | PASS | 同上 |
| L19:129 | 带状球函数 | B | nLab "spherical function" (2024-08-07) | **WARN** | 页面正文只有「经典球调和」与「表示论中某些表示的矩阵元」两段；"zonal"、"Hecke"、"p-adic" 均 0 命中，未给带状球函数与 Hecke 特征函数的定义 |
| L20:106 | 局部 Langlands 对应 | A | Gelbart, Bull. AMS 10 (1984) 177–219 | PASS | references 逐字一致（期刊/卷/年/页码） |
| L20:108 | Langlands 函子性 | B | nLab "Langlands functoriality" (2022-11-23) | PASS | 页面 Idea 原文 "a $L$-homomorphism ${}^L G\to{}^L H$ … should induce a transfer" |
| L20:115 | 限制张量积记号 | — | `\znoteplain` | PASS | 明写「（上下文推断，无外部依据）」，内容为记号约定说明 |
| L20:125 | $L$ 函数 | A | Gelbart, Bull. AMS 10 (1984) 177–219 | PASS | references 逐字一致 |
| L20:142 | 未分歧表示 | A | Bernstein–Gelbart 2004 第 11 章（Cogdell） | PASS | references 的 Chapter 11 即 Cogdell 撰写，注文写明作者，合规 |
| L22:35 | 卷积积 | B | nLab "geometric Satake equivalence" (2024-07-22) | PASS | 页面 Idea 即球面 Hecke 代数与 $\operatorname{Gr}$ 上等变层/卷积积的对应 |
| L22:41 | 等变层 | B | nLab "equivariant sheaf" (2024-12-24) | PASS | 页面给出 $a^*\mathcal F\cong\operatorname{pr}^*\mathcal F$ 与余循环条件的定义 |
| L22:68 | 半小映射 | A | de Cataldo–Migliorini, \S4.2 | PASS | references 含 \S4.2，注文未越出 |
| L22:189 | 幺半范畴 | B | nLab "monoidal category" (2025-08-14) | PASS | 页面 Definition 含结合/单位约束与五边形、三角形公理 |
| L23:18 | 张量函子 | B | nLab "monoidal functor" (2026-01-26) | PASS | 页面给出张量函子须与结合/单位约束相容的定义 |
| L23:78 | 奇偶层 | A | Juteau–Mautner–Williamson, \textit{Parity sheaves}, \S2.2 | **WARN** | 注文给了 \S2.2，但本讲 references 只写 JAMS 27(4) 1169–1212, 2014，未给章节，章号超出书目 |
| L23:98 | 半单范畴 | B | nLab "semisimple category" (2023-06-18) | PASS | 页面给出「每个对象是单对象的直和」的定义 |
| L23:121 | Tannaka 对偶 | B | nLab "Tannaka duality" (2025-07-28) | PASS | 页面 Idea 为带纤维函子的刚性张量范畴由其自同构群重建 |

## 第二批必须改的条目

### FAIL

无。57 条中未发现来源张冠李戴到「页面在讲别的东西」的程度。

### WARN（4 条，建议改）

1. **L7:8 · 椭圆曲线**（`lecture07.tex:8`）：注文开头「名字来自计算椭圆弧长时出现的椭圆积分，曲线本身与椭圆无关」在 nLab 页面无任何对应（"elliptic integral" 0 命中）。建议删掉这一句，或改写成不带来源的普通说明（把该句移出 `[来源：…]` 覆盖范围），保留后半段「一般 Weierstrass 方程、判别式 $\Delta\ne0$」——这两点页面确有支撑。
2. **L7:76 · Tate 模**（`lecture07.tex:76`）：页面只有 $T_p(A)=\varprojlim A[p^n]$ 的定义与文献表，无 Galois 作用、无 Tate 猜想。建议把「Galois 作用也随之变成连续的矩阵作用」与「Tate 猜想（Faltings 1983 …）」两句删去，或改引本讲 references 里的 Silverman（A 级）作为该两句的来源；nLab 只用于定义句。
3. **L19:129 · 带状球函数**（`lecture19.tex:129`）：nLab "spherical function" 正文只有「经典球调和（Laplace 方程在球面上的解）」与「表示论中某些表示的矩阵元」两段，且明说 wikipedia 只覆盖经典情形；"zonal"、"Hecke"、"p-adic" 全部 0 命中，支撑不了注文关于双 $G(\OO_F)$ 不变、卷积算子特征函数的定义。建议改引本讲 references 的 Satake（`IHES Publ. Math. 18 (1963) 5--69`，A 级），或改用 `\znoteplain`。
4. **L23:78 · 奇偶层**（`lecture23.tex:78`）：注文写 `\S2.2`，但本讲 references 的 JMW 条目只到「JAMS 27(4), 1169--1212, 2014」，没有章节信息。建议删去 `\S2.2`（改为「（本讲参考文献）」），或在 references 中补该章节后保留。

## 第二批备注

- 链接与日期层面无一处问题：32 条样本 URL 全部 200，32 条 nLab 日期逐字相符，说明各讲施工员抄 `Last revised` 是照实抄的。
- 教材类（A 级，含 1 条 A+B）共 20 条，书名/章号/丛书号/卷期页码全部落在对应讲 references 之内；唯一跨讲引用是 L16:18 的 Neukirch（注文自述「见第 2 讲参考文献 [N]」，与该讲书目逐字一致，Lead 已批准）。
- 本轮问题集中在三类：**「页面只有标题与文献、正文不支撑注文的实质断言」**（L7:76、L19:129）、**「注文里有一句超出了所挂页面的范围」**（L7:8）、**「章号超出书目」**（L23:78）。
- 另有 6 条 `\znoteplain` 抽样复核（L11:88、L15:10、L15:104、L16:45、L16:57、L20:115）：正文均确写「（上下文推断，无外部依据）」，内容均为对原书表述/记号的上下文说明，未见「本可外查却标成无依据」的情形。
