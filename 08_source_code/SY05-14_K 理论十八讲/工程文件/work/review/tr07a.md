# tr07a.tex 交叉校对报告

- 校对对象：`work/src/chunks/tr07a.tex`（原文 **pp.87–98**；§15 高阶代数 K 理论 pp.87–88、§16 第一讲 pp.89–98）
- 校对：tr-03（交叉校 tr-07 的块）；日期 2026-11-06
- 依据：`work/pages/p087.png–p098.png`（200 dpi，唯一真值）+ `work/split/p087–p098.txt`（仅用于定位）+ 500/700/800/900/1000/1200/1400/1600 dpi 裁图复核（存于 `work/tmp/r13*–r36*` 的 PNG/中间文本）+ 已构建的 `work/src/main.pdf`（86 页，2026-11-06 22:43 构建）用于版式复核
- 铁律遵守：**未改动 tr07a.tex 及任何他人文件**，本报告是唯一产出；所有改动建议均给出可直接替换的文本，由 Lead 落改。
- **版本说明**：本报告针对 `tr07a.tex` 的 **2026-11-06 22:36:19 版**（27,944 字节、240 行，sha256 `ae1512af01ebeab62af9417dc23f5eb5de73bc38ea3602316263d56f77dab132`）。校对期间该文件与 `preamble.tex` 被做过一次规范化（`–`→`--`、`\ker`→`\Ker`），`preamble` 已新增 `\Ker` 宏，故现版 `\Ker` 可编译（22:43 构建成功）；本报告的行号与所引文本均**已对现版逐行复核**。

---

## 一、结论摘要

**总体判定：正文内容 PASS，需 2 项「必须改」（1 处中文语病、1 处 tikzcd 标签方位与原文不符），另有 11 项可选改。**

| # | 检查项 | 结果 |
|---|---|---|
| 1 | 编号定理类完整性 | **全部正确**：定义 1–3、定理 1–2、断言 1–3、引理 1–5、推论 1–4、命题 1–2，类型与号数逐条与原文一致，每节从 1 起，无缺号/重号/错型；另 12 个 `proof` 与 13 处原文 "Proof" 的对应关系正确（多出的 1 处是 `Proof of Serre-Swan Theorem:` 标题，按体例作 `\para`） |
| 2 | 公式逐符号 | 17 组展示式全数对照 200 dpi 页图；其中 20 条关键式（含 tikzcd、p.94 Hom 式、p.92 $nd_0$、p.98 的 $F_x$ 分解）再以 500–1600 dpi 裁图复核。**17 条完全一致**；p.90 交换图 **1 处标签方位不符**（见 M2）；另 2 条展示式漏句末句号（O1、O2） |
| 3 | 漏译 | **无**：12 页逐段（按 split 文本切段）对照，无整句/整段/脚注缺失；p.87→p.88、p.89→p.90、p.90→p.91、p.93→p.94、p.94→p.95、p.96→p.97、p.97→p.98 七处页交界均无重复无缺口 |
| 4 | 边界接缝 | **干净**：块首 `% [原文 p.87]` + `\section{高阶代数 K 理论}` 紧接 tr06a（p.86 末）；块末 p.98 最后一段与 tr08a 的 `\section{第二讲（Whitehead 群与 Steinberg 群）}` 之间无过渡句、无残留（已在 main.pdf 上直接看到接缝处） |
| 5 | 术语 | 与 `glossary.tsv` 一致（Grothendieck 群、投射模、幂等、Serre–Swan 定理、Whitehead 群/挠、幺半群、正合、截面、子丛等）；19 条新术语建议补表（第五节），未发现同一英文多译的实质冲突 |
| 6 | 结构 | 2 个 `\section` 标题与 BRIEF 冻结表**逐字一致**（程序逐字符比对）；`\tag` = **0**；环境/花括号/`$`/`\[…\]` 全部平衡（去注释后深度归零）；无 BOM、无 CRLF、无 U+FFFD；`work/tools/check.py` 全库 **PASS**（22 section、130 页标记、207 条批注） |

**待落改**：必须改 **2** 项（M1、M2）；可选改 **11** 项（O1–O11）。

---

## 二、编号定理类完整性表（逐页对 200 dpi 页图）

### §15（pp.87–88）

原文两页**无任何编号定理类**，仅 7 个自然段（第 5 段跨 p.87–88，p.88 再起 2 段）。译文 L8、L11、L13、L15、L17、L20、L23 七段齐全，无编号、无 `\para` —— 与原文一致 ✓。

### §16（pp.89–98，号数从 1 重新起）

| # | 页 | 原文（页图） | 译文（行号） | 判定 |
|---|---|---|---|---|
| 1 | 89 | **Definition 1.** Let A be a unital ring… | `\begin{defn}{1}`（L34） | ✓ |
| 2 | 90 | **Definition 2.** A (left) A−mod P is called *finitely generated*… | `\begin{defn}{2}`（L55） | ✓ |
| 3 | 91 | **Definition 3.** We define the 0th K-group… | `\begin{defn}{3}`（L81） | ✓ |
| 4 | 90 | **Theorem 1.** The following are equivalent: 1./2. | `\begin{thm}{1}`（L59） | ✓ |
| 5 | 93 | *Theorem 2:* If P ∈ P_A, then … | `\begin{thm}{2}`（L125） | ✓ 类型/号数正确（原文排斜体+冒号，见「特别复核 a」） |
| 6 | 94 | **Claim 1.** The functor Γ(−) "respects" isomorphisms… | `\begin{claim}{1}`（L149） | ✓ |
| 7 | 94 | **Claim 2.** Γ(E) is a f.g.p. C(X)-mod… | `\begin{claim}{2}`（L151） | ✓ |
| 8 | 94 | **Claim 3.** All f.g.p. C(X)-mod's can be "realised"… | `\begin{claim}{3}`（L153） | ✓ |
| 9 | 94 | **Lemma 1.** If X is normal, suppose U is a neighborhood… | `\begin{lem}{1}`（L158） | ✓ |
| 10 | 94–95 | **Lemma 2.** If X is normal and if s ∈ Γ(E) with s(x)=0, then there ｜*页界*｜ exist elements… | `\begin{lem}{2}`（L171，页标记 L172 插在陈述中间） | ✓（跨页位置正确，见第八节） |
| 11 | 96 | **Lemma 3.** If X is compact and Hausdorff… | `\begin{lem}{3}`（L194） | ✓ |
| 12 | 96 | **Lemma 4.** For any complex vector bundle E → X… | `\begin{lem}{4}`（L203） | ✓ |
| 13 | 96 | **Lemma 5.** Let t₁,…,t_k be sections… | `\begin{lem}{5}`（L209） | ✓ |
| 14 | 94 | **Corollary 1.** If X is normal, then for any x ∈ X… | `\begin{cor}{1}`（L163） | ✓ |
| 15 | 94 | **Corollary 2.** If X is normal, f, g : E → E′ … | `\begin{cor}{2}`（L167） | ✓ |
| 16 | 95 | **Corollary 3.** Let I_x be the two-sided ideal… | `\begin{cor}{3}`（L178） | ✓ |
| 17 | 95 | **Corollary 4.** Let X be normal and let E and E′ be to complex vector bundles… | `\begin{cor}{4}`（L186） | ✓（原文 "to" 应为 "two"，已批注 L188） |
| 18 | 95 | **Proposition 1.** If X is normal, then given any C(X)-map… | `\begin{prop}{1}`（L182） | ✓ |
| 19 | 97 | **Proposition 2.** Let f : E → E′ be a vector bundle map. Then T.F.A.E.: (1)–(4) | `\begin{prop}{2}`（L214） | ✓（四项用 `label=(\arabic*)`，与原文 (1)(2)(3)(4) 一致） |
| 20 | 97 | *Remark:* Without any hypothesis…（**无编号、斜体**） | `\para{注：}`（L231） | ✓ 未自造编号（正确）；与 p.98 的「Remark 1」关系见「特别复核 b」 |

**原文无编号但需保留的结构（全部到位）**

- **Proof 13 处 → 12 个 `proof` 环境 + 1 个标题**：p.93 `Proof of Serre-Swan Theorem:` 在原文是**粗体标题**（不是 amsthm 的 "Proof:"），译文作 `\para{Serre--Swan 定理的证明：}`（L136）**正确**；其余 12 处分别为 Lemma 1（L161）、Cor 1（L165）、Cor 2（L169）、Lemma 2（L176）、Cor 3（L180）、Prop 1（L184）、Cor 4（L189）、Lemma 3（L197）、Lemma 4（L205）、Lemma 5（L211）、Prop 2（L224）、Claim 3（L234）。
- **粗体/斜体小标题**：p.92 `Examples:`（粗体）→ `\para{例：}`（L108）✓；p.93 `Proof of Serre-Swan Theorem:`（粗体）→ `\para{…的证明：}`（L136）✓；p.93 `[Aside Note: …]`（斜体方括号）→ `\emph{［旁注：…］}`（L134）✓；p.97 `Remark:`（斜体）→ `\para{注：}`（L231，见 O3）。
- **结论：无缺号、无重号、无错型、无自造编号。**

### 特别复核 a：p.93 的 "Theorem 2:"

页图（1600 dpi 复核）确为 **斜体 "Theorem 2:"**、冒号收尾，整条陈述（"If P ∈ P_A, then P ≃ a₁ ⊕ … ⊕ aₙ, where the a_i's are fractional. Hence K₀A = ℤ ⊕ Pic(A)."）**通体斜体**，与该节其余定理的粗体体例不一致。
- 号数：紧接 p.90 的 Theorem 1，**确为定理 2**（不是新增序列、不是笔误号）。
- 类型：内容是一条**定理**（Dedekind 整环上投射模分解 + K₀ 结构），用 `\begin{thm}{2}` **正确**；斜体只是原文排版不一致，译文按项目体例出粗体并由 L124 批注说明 —— **处理正确，无须改动**。

### 特别复核 b：p.97 未编号 "Remark:" 与 p.98 "Remark 1"

页图逐字确认：
- **p.97 末尾**印的是 *Remark:*（斜体、**无编号**、无粗体），紧接的 □ 结束 Proposition 2 的证明；
- **p.98** 印的是 "Apply **Remark 1** at the end of the proof of Proposition 2 to f and 1 − f respectively…"。

→ **不一致确在原文，不是译者错引**。译文处置：p.97 用 `\para{注：}`（不编号，符合「不得自造编号」），p.98 照译「注 1」，并在 L230 批注点明二者关系 —— **处理正确，无须改动**。（若 Lead 想彻底消歧，只能在 p.98 的「注 1」后加「（即上页末尾那条注）」，但这已由批注覆盖，正文不必动。）

---

## 三、公式逐符号核对表（抽查 20 条，覆盖本块全部复杂式）

| # | 页 | 公式（原文，页图转录） | 译文（行号） | 复核 dpi | 判定 |
|---|---|---|---|---|---|
| 1 | 89 | `F = P ⊕ Q`（定义 1 展示式，无标点） | L35 `\[ F = P \oplus Q \]` | 200 | ✓ 一致 |
| 2 | 90 | `Q = ker(p),`（带逗号） | L40 `\[ Q = \Ker(p), \]` | 800 | ✓ 一致（含逗号；原文 `ker` 小写、译文 `\Ker` 为正体算子，属项目体例：preamble 已定义 `\newcommand{\Ker}{\operatorname{Ker}}`，无需改） |
| 3 | 90 | **提升性质交换图**：上 `P --h--> N`（h 在箭头上方）、左竖 `‖`、右竖 `↓` 且 **f 在竖线右侧**、下 `P --g--> M`（**g 在箭头上方**） | L46–51 tikzcd：`P \arrow[r,"h"] \arrow[d,equal] & N \arrow[d,"f"]` / `P \arrow[r,"g"'] & M` | 900（页图）+ 300（main.pdf 渲染） | **✗ 一处不符**：h 上 ✓、左 ‖ ✓、f 右 ✓、方向全对 ✓；但 **g 被 `"g"'` 排到了箭头下方**（已用 main.pdf 22:43 版渲染确认）→ **M2** |
| 4 | 90 | `x = a₁x₁ + a₂x₂ + … + aₙxₙ.` | L56 | 200 | ✓ 一致 |
| 5 | 90 | `P ⊕ Q = Aⁿ.` | L63 | 200 | ✓ 一致 |
| 6 | 91 | `e = e²` ；`P = Aⁿe` | L66 / L68 `\[ e = e^2 \]` / `\[ P = A^n e \]` | 200 | ✓ 一致（`A^ne` 与 `A^n e` 仅空格差，渲染相同） |
| 7 | 91 | `[P] + [Q] = [P + Q].`（**有句号**） | L77 `\[ [P] + [Q] = [P + Q] \]` | 900 | ✗ 漏句末句号 → **O1** |
| 8 | 91 | `K₀A := abelian group completion of Iso(P_A).` | L82 `\[ K_0A := \operatorname{Iso}(P_A)\ \text{的阿贝尔群完备化}. \]` | 800 | ✓ 内容一致（原文英文式改写为中文式，语义与符号位置无误） |
| 9 | 91 | `[a + b] = [a] + [b].`（**有句号**） | L92 `\[ [a + b] = [a] + [b] \]` | 900 | ✗ 漏句末句号 → **O2** |
| 10 | 92 | `a + b = nd₀`（第 3 种构造；原文下标确为 **d₀**，非 a₀） | L98 `$a + b = nd_0$` | 900 | ✓ 忠实照录 + L103 批注指出应为 a₀ —— 处置正确 |
| 11 | 92 | `I* = I × I/∼`（行内）；`I* = I × ℕ/∼`（展示式）；`(a,n)∼(a′,n′) ⇔ ∃n∈ℕ : a+n′a₀ = a′+na₀` | L96 / L99 / L100 | 200 | ✓ 一致 |
| 12 | 92 | `K₀𝔽 = ℤ.` / `Iso(P_ℤ) = ℕ,` / `K₀ℤ = ℤ.` | L111 / L114 / L116 | 200 | ✓ 一致（含第 2 条末尾逗号） |
| 13 | 94 | `Hom(E, E′) ≃ Hom_{C(X)}(Γ(E), Γ(E′)))`（**多 1 个右括号**：程序计数 5 开、6 闭） | L155 | 1400 | ✓ 忠实保留：译文该式 ASCII 括号 6 开 7 闭，**同样多 1 个**，与原文一致；L157 批注正确 |
| 14 | 95 | `Γ(E)/[I_xΓ(E)] ≃ π⁻¹(x)`，`s ↦ s(x)` | L178 | 200 | ✓ 一致 |
| 15 | 96 | `E ⊕ E′ ≃ Cⁿ_X` ；`f : Cⁿ_X ≃ E ⊕ E′ → E.` | L198 / L200 | 200 | ✓ 一致（含末式句号） |
| 16 | 96 | `t_i(y) = Σ_j a_{ij}(y)s_j(y)`，`y ↦ a_{ij}(y)`：`U → GL_n(ℂ)` | L211 | 200 | ✓ 一致 |
| 17 | 98 | `F_x(Cⁿ_X) = F_x(E) ⊕ F_x(E′)`；`dim F_x(E) = h`、`dim F_x(E′) = k` | L234 | 200 | ✓ 一致（原文 `dimF_x` 连排、斜体，译文作正体算子 `\operatorname{dim}`，属体例） |
| 18 | 98 | `dim F_y(E) + dim F_y(E′) = h + k`（无标点，下接 "is a constant"） | L235 | 200 | ✓ 一致 |
| 19 | 93 | `P ≃ a₁ ⊕ a₂ ⊕ … ⊕ aₙ`；`K₀A = ℤ ⊕ Pic(A)`（定理 2 正文内，斜体） | L125 | 1400 | ✓ 一致 |
| 20 | 93 | `[F, Q] < ∞`（**斜体 F、Q**，非黑体）；`𝔽` 为数域、`A` 为 ℤ 在 𝔽 中的整（闭）包 | L122 `$[F, Q] < \infty$`、`$\F$` | 1400 | ✓ 一致（已 1400 dpi 复核：`[F,Q]` 确为斜体，`𝔽` 确为 blackboard——译文分用 `$F,Q$` 与 `\F` 正确） |

**合计**：20 条检查中 **17 条完全一致**，1 条（#3 交换图）标签方位不符（M2），2 条（#7、#9）漏句末句号（O1、O2）。
> 说明：任务清单所述「p.96 的 $F_x$ 分解」在原文 pp.96 **并不存在** $F_x$（p.96 只有 Lemma 3/4/5，其"分解"是引理 5 证明里的局部基展开 `t_i(y)=Σ_j a_{ij}(y)s_j(y)`，已核对 #16 ✓）；真正的 $F_x$ 分解在 **p.98**（`F_x(Cⁿ_X)=F_x(E)⊕F_x(E′)`，已核对 #17 ✓）。两者均已逐一核对。

---

## 四、漏译检查（逐页对照 `work/split/p087–p098.txt`）

| 页 | 原文结构（按 split 切分） | 译文对应 | 判定 |
|---|---|---|---|
| 87 | 5 段（末段跨页） | L8、L11、L13、L15、L17 | ✓ 无缺 |
| 88 | 跨页句余部 + 2 段 | L17 末句 + L20、L23 | ✓ 无缺（跨页句合并在 p.87 段，未重复） |
| 89 | 标题 + 3 段 + 定义 1 | L26、L29、L31、L34 | ✓ 无缺 |
| 90 | 4 段 + 定义 2 + 定理 1（含 1、2 两项与图） | L39、L43、L53、L55、L59 | ✓ 无缺 |
| 91 | 定理 1 第 3 项 + 4 段 + 定义 3 + 三种构造的第 1 种 | L65、L74、L76、L81、L85、L87、L89、L91 | ✓ 无缺 |
| 92 | 构造 2、3 + 2 段 + Examples + 例 1、2 | L96、L98、L104、L106、L108、L110、L113 | ✓ 无缺 |
| 93 | PID 一句 + 例 3 + 定理 2 + 练习句 + 例 4 + 旁注 + 证明标题 + 2 段 + 2 个 bullet | L120、L122、L125、L127、L129、L134、L136、L137、L139、L141–142、L146 | ✓ 无缺（含 2 个 bullet） |
| 94 | 1 段 + 断言 1–3 + 1 段 + 引理 1/证 + 推论 1/证 + 推论 2/证 + 引理 2 起 | L146、L149、L151、L153、L155、L158、L161、L163、L165、L167、L169、L171 | ✓ 无缺 |
| 95 | 引理 2 余部 + 证 + 推论 3/证 + 命题 1/证 + 推论 4/证 + 1 段 | L173、L176、L178、L180、L182、L184、L186、L189、L191 | ✓ 无缺 |
| 96 | 引理 3/证 + 引理 4/证 + 1 段 + 引理 5/证 | L194–L211 | ✓ 无缺 |
| 97 | 跨页句余部 + 命题 2 + 长证明（含反例、三个方向、Remark） | L211 末句、L214、L224、L226、L228、L231 | ✓ 无缺 |
| 98 | 断言 3 的证明 + 末段 | L234–L236、L240 | ✓ 无缺 |

**原文 pp.87–98 无脚注、无图表（仅 1 张交换图，已核对）。未发现任何整句/整段缺失。**

---

## 五、术语检查（对照 `work/glossary.tsv`）

**与 glossary 一致（抽查）**：K 理论 / 高阶代数 K 理论、Grothendieck 群、投射模（projective module）、幂等（idempotent）、有限生成（finitely generated）、幺半群（monoid）、自由阿贝尔群、理想（ideal）、挠（torsion → Whitehead 挠）、截面（section）、子丛（subbundle）、纤维（fibre）、向量丛、Serre–Swan 定理、Whitehead 群、初等矩阵、紧（compact）、正合（exact）、范畴/函子（category/functor）。**未发现同一英文多译的实质冲突。**

**不在 glossary、建议补表的新术语（19 条）**：

| english | 中文（译文用词） | 首现 |
|---|---|---|
| unital ring | 含幺环 | p.87 |
| skew-field | 除环 | p.92 |
| free module / based free module | 自由模 / 有基自由模 | p.89 |
| invariant basis property | 基不变性质 | p.89 |
| lifting property | 提升性质 | p.90 |
| local base | 局部基 | p.94 |
| exact category | 正合范畴 | p.88 |
| additive functor | 可加函子 | p.93 |
| ideal class group | 理想类群 | p.93 |
| fractional ideal | 分式理想 | p.93 |
| Dedekind domain | Dedekind 整环 | p.93 |
| group ring | 群环 | p.87 |
| normal topological space | 正规拓扑空间 | p.94 |
| two-sided ideal | 双边理想 | p.95 |
| group completion | 群完备化（阿贝尔群完备化） | p.91 |
| motivic cohomology | 动机上同调 | p.87 |
| surgery theory | 手术理论 | p.87 |
| simple homotopy theory | 单同伦论 | p.87 |
| finiteness invariant | 有限性不变量 | p.87 |

另：`Pic(A)`、`T.F.A.E.`、`f.g.p.` 保留原文缩写，与本项目惯例一致；`Hausdorff`、`Urysohn`、`Dedekind`、`Quillen–Suslin`、`Serre–Swan` 保留拉丁名 —— 均无需改。

---

## 六、必须改（2 项，含可直接替换文本）

### M1｜p.91（L87）中文语病：「对 (I*, φ) 只在规范同构的意义下确定」

- **位置**：`tr07a.tex` **第 87 行**。
- **原文**（p.91）：“… which is a universal homomorphism from I to some abelian group. **The pair (I*, φ) is only defined up to a canonical isomorphism.**”
- **现状**：「一般地，若 $I$ 是任意阿贝尔幺半群，则存在一个阿贝尔群 $I^*$ 连同同态 $\phi : I \to I^*$，它是从 $I$ 到某个阿贝尔群的泛同态。**对** $(I^*, \phi)$ 只在规范同构的意义下确定。」
  问题：介词「对」后无谓语可支配，整句缺主语（「对……只在……的意义下确定」不成句），且与原文 “The pair (I*, φ) is only defined up to …” 的主谓结构不符。
- **可直接替换文本**（整行替换即可）：

```latex
一般地，若 $I$ 是任意阿贝尔幺半群，则存在一个阿贝尔群 $I^*$ 连同同态 $\phi : I \to I^*$，它是从 $I$ 到某个阿贝尔群的泛同态。$(I^*, \phi)$ 只在规范同构的意义下确定。
```

（即：删去句首的「对」；其余一字不动。若愿意补足语气，可在句末加「（即只确定到典范同构）」，非必需。）

### M2｜p.90 交换图（L49）底边标签 g 的方位与原文相反

- **位置**：`tr07a.tex` **第 49 行**（`\[`…tikzcd…`\]` 内）。
- **原文**（p.90 页图，900 dpi 复核）：上排 `P —h→ N`，**h 在箭头之上**；左竖为 `‖`；右竖 `↓` 且 **f 在竖线右侧**；下排 `P —g→ M`，**g 在箭头之上**。即 h、g 均在各自箭头上方。
- **现状**：`P \arrow[r,"g"'] & M` —— 末尾的 `'` 把 g 翻到箭头**下方**（已用 22:43 构建的 `main.pdf` 渲染核对：图里 h 在上、f 在右、g 在下）。与原文不符。
- **可直接替换文本**（整行替换）：

```latex
P \arrow[r,"g"] & M
```

（即删去 `"g"` 后的那个 `'`。tikzcd 中 `r` 方向的标签默认在箭头上方，与原文一致；`'` 会翻到下方。其余三行 `P \arrow[r,"h"] \arrow[d,equal] & N \arrow[d,"f"] \\`、`\begin{tikzcd}`、`\end{tikzcd}` 均**正确，勿动**。）

---

## 七、可选改（11 项，均不影响内容正误；逐项给替换文本）

### O1｜p.91（L77）展示式漏原文句末句号

- 原文页图 900 dpi：`[P] + [Q] = [P + Q].`（有句号，句子在此结束，下一行 "The second set is in fact…"）
- 现状：`\[ [P] + [Q] = [P + Q] \]`
- 替换：`\[ [P] + [Q] = [P + Q]. \]`

### O2｜p.91（L92）展示式漏原文句末句号

- 原文页图 900 dpi：`[a + b] = [a] + [b].`（第 1 条构造的句末，有句号）
- 现状：`\[ [a + b] = [a] + [b] \]`
- 替换：`\[ [a + b] = [a] + [b]. \]`

### O3｜p.97（L231）Remark 的体例：原文斜体，译文粗体

- 原文：*Remark:* （斜体、无编号）；译文：`\para{注：}`（粗体小标题）。
- 说明：STYLE_GUIDE §2 规定「原文的行内粗体小标题用 `\para`；句中强调用 `\emph`（原文斜体）」。此处原文为**斜体**而非粗体，严格按体例应作 `\emph{注：}`；但作为一段小标题，`\para` 的视觉效果更好，且与 p.98「注 1」的称引呼应。
- 建议：**保留现状**，仅在 L230 现有批注末尾补一句「原文用斜体 Remark:，此处按小标题体例作粗体」。若 Lead 要求严格照体例，可替换为：

```latex
\emph{注：} 在没有任何假设的情况下，本证明表明：若 $\operatorname{dim}F_x(\operatorname{Im}f) = n$，则在 $x$ 的某个邻域内对一切 $y$ 有 $\operatorname{dim}F_y(\operatorname{Im}f) \ge n$。
```
（注意：该行现与 `\end{proof}` 同处一行 L231，替换时保留行尾 `\end{proof}`。）

### O4｜p.98（L234 句内 "saﬃces"）原文拼写有误，译文正确但缺批注

- 原文（p.98 页图 800 dpi 复核）："By Proposition 2 above it **saﬃces** to show that …"，`saﬃces` 缺 `u`，应为 **suffices**。
- 现状：译文「只需证明 ……」**意思正确**，但 L238/L239 的批注未提这一处（全块其余拼写笔误基本都有批注）。
- 建议：在 L238 批注末追加一句（可直接粘贴到该批注 `]` 之前）：

```
；同段 "it saﬃces" 中 saﬃces 应为 suffices。
```

### O5｜p.90（L39–41）"namely Q = ker(p)" 原文语句粘连，译文照译但未加批注

- 原文："It follows from the above definition that P is the image of a projection p on F; the module endomorphism in F which is the identity on P and 0 on Q, **namely Q = ker(p)**, is idempotent and projects F to P."
- 说明：原文把「namely p」与「Q = ker(p)」挤成一句，字面读不通（自同态不可能"等于 Q = ker p"）。正确读法：该自同态即投影 **p**，而 **Q = ker p**。译文照译（保留 `\[ Q = \Ker(p), \]` 居中排版）**在忠实性上正确**，但读者会卡住。
- 建议：在 L39 前补一条批注（可直接插入）：

```
% [Tutor Note: p.90 "namely Q = ker(p)" 原文语句粘连：该自同态指的是投影 $p$，而 $Q = \ker p$ 是补充说明；照字面读不成立。译文保留原排版，读者按此理解即可。]
```

### O6｜p.98（L234）「引理 1.1.1」与 p.96（L197）「命题 1.1.1」的原文不一致，未点明

- 原文：p.96 作 "Recall that **Propositon** 1.1.1 states…"（另含拼写错误 Propositon）；p.98 作 "one would have by **Lemma** 1.1.1 that…"。同一交叉引用，原文一处称命题、一处称引理。
- 现状：译文分别作「命题 1.1.1」（L197）与「引理 1.1.1」（L234），**忠实照译但未说明**。
- 建议：在 L239 批注末追加：

```
；另：p.96 称「命题 1.1.1」，p.98 却称「引理 1.1.1」，原文自相矛盾，译文照原样保留。
```

### O7｜p.93（L125）定理 2 中 "fractional" 的补足

- 原文："… where the $a_i$'s are **fractional**."（省略了 ideals）
- 现状：译文补作「其中 $a_i$ 是**分式理想**」，语义正确、中文必需（单独「分式的」不成句）。
- 建议：在 L124 批注末追加半句说明是补足：

```
；另：原文 "the $a_i$'s are fractional" 省略了 ideals，译文补足为「分式理想」。
```

### O8｜p.89（L96）「第 1 章 1.1 节」与原文 "section 1.1"

- 原文："(This is the construction we used in **section 1.1** to define KX, the Grothendieck group of Vect(X))."
- 现状：「（这正是我们在**第 1 章 1.1 节**中用来定义 $K(X)$ 的构造…）」。加了「第 1 章」三字（第 1 章确为拓扑 K 理论，p.93 亦有 "section 1 of chapter 1" 的写法，可通）。
- 若要与原文严格一致，替换为：

```latex
（这正是我们在 1.1 节中用来定义 $K(X)$ 的构造，即 $\Vect(X)$ 的 Grothendieck 群。）
```
（低优先，可保留现状。）

### O9｜p.94（L155）「即 $X$ 是正规拓扑空间」略生硬

- 原文："we prove it for the more general case **where X is a normal topological space** and to be more precise…"
- 现状：「（我们在更一般的情形下证明它，**即** $X$ 是正规拓扑空间；更确切地说，…）」
- 建议替换该小句为：「（我们在更一般的情形——$X$ 为正规拓扑空间——下证明它；更确切地说，…）」（低优先）

### O10｜p.90（L46–51）tikzcd 外层用 `\[ … \]` 包裹

- 现状：`\[` / `\begin{tikzcd}` … `\end{tikzcd}` / `\]`。
- 核实：**可编译，渲染正常**（main.pdf 22:43 版已验证该图位置、箭头、标签都正确，仅 M2 那一个 prime 需改）。STYLE_GUIDE §3 的示例是独立 `tikzcd`，故此处只是体例不统一，不是错误。
- 若 Lead 要求全库统一，可替换为：

```latex
\begin{center}
\begin{tikzcd}
P \arrow[r,"h"] \arrow[d,equal] & N \arrow[d,"f"] \\
P \arrow[r,"g"] & M
\end{tikzcd}
\end{center}
```
（低优先；**建议与 M2 一并落改**，改后不再有 `\[ \]` 包裹问题。）

### O11｜p.91（L81）定义 3 里两个「即」连用

- 现状：「…记作 $K_0A$，**即** $\operatorname{Iso}(P_A)$ 的阿贝尔群完备化（或我们在第 1 章用过的 Grothendieck 群 $\operatorname{Gr}$）），**即** \[ K_0A := … \]」——原文 "denoted K0A, the abelian group completion (or …) of Iso(P_A) ), **namely** …"，两处英文并非同一个词。
- 建议：把**第二个**「即」改为「也就是」（纯行文，低优先）：

```latex
（或我们在第 1 章用过的 Grothendieck 群 $\operatorname{Gr}$）），也就是
```

---

## 八、边界接缝与跨页句（含对译者说法的核实）

### 8.1 块两端

- **块首**：`% ===== 原文 pp.87--98 =====` → `% [原文 p.87]` → `\section{高阶代数 K 理论}`（L1–L6）。tr06a 结束于 p.86，**无重复、无缺口、无多余过渡句** ✓。
- **块末**：p.98 最后一段「于是，向量丛与有限生成投射模之间有着完全的类比……」（L240）之后即 tr08a 的 `\section{第二讲（Whitehead 群与 Steinberg 群）}`。已在 `main.pdf`（22:43 版）渲染页上直接看到该接缝：**tr07a 末段 → 立即是 §17 标题，无残留、无缺段** ✓。

### 8.2 各页交界的归属（逐处核对；其中 4 处是真正的跨页句）

| 交界 | 原文断点 | 译文处理 | 判定 |
|---|---|---|---|
| p.87→88 | "…plus construction he gave ｜ the general definition of the nth K-Group…" | 整句写在 p.87 段内（L17），p.88 标记后另起「若干年后…」 | ✓ 无重复无丢失（符合「开始者写完」） |
| p.89→90 | 定义 1 结束于 "is a free module F."（p.89） | 定义 1 在 p.89 段内完成（L34–36），p.90 标记在 L38 | ✓ |
| p.90→91 | 定理 1 第 2 项展示式 "P ⊕ Q = Aⁿ." 结束于 p.90 | 展示式 L63 后紧接 `% [原文 p.91]`（L64）再列第 3 项 | ✓ |
| p.91→92 | 第 1 种构造 "[a+b]=[a]+[b]." 结束于 p.91 | L92 后接 p.92 标记（L95）再列第 2 种 | ✓ |
| **p.93→94** | "Thus to ｜ prove the theorem, we have to prove three claims:" | 整句合写在 p.93（L146 末），p.94 标记（L148）在「断言 1」之前 | ✓ **无重复无丢失**；但注意：此处页标记是放在**句末**而非句中（与译者自述不符，见下） |
| **p.94→95** | 引理 2 陈述 "…with s(x) = 0, then there ｜ exist elements s₁,…" | **页标记 L172 插在 `\begin{lem}{2}` 环境内部、句中断处**（L171 末词「则存在」→ L172 标记 → L173「元素 $s_1,…$」） | ✓ 与原文断点一致；LaTeX 注释在环境内无语义影响 |
| **p.96→97** | "…this should hold for all y ｜ sufficiently close to x. From this fact the result follows. □" | 整句合写在 p.96（L211 末），p.97 标记（L213）在「命题 2」之前 | ✓ **无重复无丢失**；同样是句末放置 |
| p.97→98 | 命题 2 证明以 □ 结束（p.97 末） | p.98 标记（L233）在「断言 3 的证明」前 | ✓ |

### 8.3 对「页标记放在句中断处」说法的核实结论

译者的说法**只对 p.94→p.95 一处成立**。p.93→p.94 与 p.96→p.97 两处，页标记实际放在**句末**（译者在 p.93 末尾补全了 "Thus to prove the theorem, we have to prove three claims:"、在 p.96 末尾补全了 "…for all y sufficiently close to x. From this fact the result follows."）。
**这两种处理都符合 STYLE_GUIDE §8「跨页句开始者写完」**，且经逐字比对**没有重复、没有丢失**，因此**不需要改**；本报告只是更正说法，供 Lead 掌握实情。

---

## 九、核对过程中确认「原文确有笔误、译文处理正确」的清单（避免 Lead 误改）

以下 16 处经 500–1600 dpi 裁图逐字确认，**原文确实如此**，译文「照原样 + 批注」的处置**全部正确**，请勿按"常识"改正文：

| # | 页 | 原文笔误 | 译文处置 |
|---|---|---|---|
| 1 | 87 | trully / ingeneous / this later assumption | 译意 + L10 批注 ✓ |
| 2 | 88 | "mudulo torsion"（引号方向也反） | 译「模去挠」+ L22 批注 ✓ |
| 3 | 89 | 标题重复 "the the" | 按 BRIEF 定标题 + L28 批注 ✓ |
| 4 | 89 | abreviated | 译「简记」+ L28 批注 ✓ |
| 5 | 89 | 定义 1 的 "projctive"（**1600 dpi 复核：确无 e**） | 译「投射的」+ L28 批注 ✓ |
| 6 | 91 | 定义 3 多一个右括号 "Iso(P_A) )" | 保留「））」+ L80 批注 ✓ |
| 7 | 92 | 三种构造之 3 的 "nd_0"（应为 na₀） | 照录 nd₀ + L103 批注 ✓ |
| 8 | 92 | 例 2 "the category P^n_ℤ is the … group ℤⁿ"（范畴≠群） | 照译 + L118 批注 ✓ |
| 9 | 93 | Theorem 2 斜体+冒号；integral quotient（应为 closure）；[F,Q]；excercise | 照译 + L124 批注 ✓ |
| 10 | 94 | Hom 式多 1 个右括号 | 保留 + L157 批注 ✓（程序计数验证） |
| 11 | 95 | "let E and E′ be **to** complex vector bundles" | 译「两个复向量丛」+ L188 批注 ✓ |
| 12 | 96 | "**Propositon** 1.1.1" | 译「命题」+ L196 批注 ✓ |
| 13 | 97 | "so **thy** are linearly independent" | 译「它们」+ L223 批注 ✓ |
| 14 | 97/98 | Remark 无编号 vs p.98 称 "Remark 1" | 不编号 + L230 批注 ✓ |
| 15 | 98 | "E = Ker f = Im(1−f)"（与 E = Im f 矛盾） | 照译 + L238 批注 ✓ |
| 16 | 98 | 两处 "Cⁿ_X)" 多右括号 | 保留 + L239 批注 ✓ |

---

## 十、结论

1. **内容层面通过**：编号、公式、段落、术语、边界全部与原文对得上，无漏译、无错号、无自造内容；20 条批注质量高（多数为原文笔误的裁图复核结论，可直接采用）。
2. **只需落改 2 处**：M1（L87 中文语病，删一个「对」）、M2（L49 删 `"g"` 后的 `'`）。
3. 其余 11 项可选改中，**O1、O2（补两个句号）、O4/O5/O6/O7（补/扩批注）** 建议顺手一并落改；O3、O8、O9、O10、O11 属体例偏好，可不动。
4. 落改后可复跑 `work/tools/check.py`（当前全库 PASS）与 `build.ps1`（当前 main.pdf 86 页、日志无 LaTeX 错误）。

---

## 十一、落改复核（2026-11-06 22:51 增补）

**M1、M2 已由 Lead 落改并通过编译复核。**

- 现版 `tr07a.tex` 修改时间 2026-11-06 22:49:54，27,940 B（较校对版 27,944 B **恰少 4 B** = 「对」3 B + `'` 1 B）。
- 逐行比对（用 22:43 版构建镜像与本报告第五节记录的旧行快照对拍）：**全文件只有两行变化，正是 M1、M2**——
  - L49：`P \arrow[r,"g"'] & M` → **`P \arrow[r,"g"] & M`** ✓
  - L87：句首「对」已删，现为「…泛同态。$(I^*, \phi)$ 只在规范同构的意义下确定。」✓
  - 其余 238 行**逐字未动**，故本报告其余全部行号、公式行、批注行引用对现版继续有效。
- 版面复核：`main.pdf` 已于 22:51:10 重新构建（86 页、799,794 B）。渲染第 57 页（印刷页 53）的交换图确认：
  **h 在箭头上方、左竖为 ‖、f 在竖线右侧、g 在箭头上方** —— 与原文 p.90 页图**完全一致**，M2 修复生效。
- 尚未落改：O1、O2（两个展示式句末句号）与 O4–O7（补/扩批注）；O3、O8–O11 属体例偏好，可不动。这些均不影响编译与内容正误。
