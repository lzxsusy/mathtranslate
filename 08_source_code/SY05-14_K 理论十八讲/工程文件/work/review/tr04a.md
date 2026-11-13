# tr04a.tex 交叉校对报告

- **校对对象**：`work/src/chunks/tr04a.tex`（原文 pp.53–62，§7 第六讲 / §8 解析 K 理论 / §9 第一讲，译者 tr-04）
- **底本**：Ioannis P. Zois, *18 Lectures on K-Theory*, arXiv:1008.1346v1（PDF 页号 = 印刷页码）
- **素材**：`work/pages/p053.png–p062.png`（200 dpi 全页）、`work/split/p053–p062.txt`（仅用于定位）、500–900 dpi 裁图、PyMuPDF 字体级 span 扫描
- **纪律**：本报告只读 tr04a.tex，**未修改**该文件或任何他人文件；所有「必须改」项由 Lead/tr-04 落改
- **报告文件**：`work/review/tr04a.md`

---

## 一、结论摘要

| 检查项 | 结论 |
|---|---|
| 1 编号定理类 | **逐条与原文一致**（含原文重号）。§9 内两个「定理 1」经页图与字体级核验确认是**原文重号，不是译者编号错误**（详见 §二） |
| 2 公式逐符号 | 抽查 **16 条**（远超 8 条），内容全部一致；仅存在「原文斜体/大写 → 译本正体/小写」的**体例规范化差异**（不影响数学内容，见 §八 O3–O5） |
| 3 漏译 | **无整句/整段缺失**；§8 总起 3 句完整。仅「斜体强调」覆盖不全（2 处整句 + 1 处展示式），见 §四 |
| 4 边界接缝 | p.52→p.53、p.62→p.63 均切在 section 边界，**无重复、无缺口**（见 §五） |
| 5 术语 | 与 `glossary.tsv` 一致；glossary 有 12 个缺项建议补入（Calkin 代数、蛇引理等，见 §六） |
| 6 结构 | 三节标题与 BRIEF §3 **逐字一致**；`\tag` = 0；页标记 p.53–p.62 各 1 次、顺序正确；p.53 的 **Definition.** 确为**无编号**（粗体，非 `\begin{defn}`），tr-04 用 `\para{定义.}` 处理正确 |
| 需改统计 | **必须改 4 项**（1 语义 + 2 斜体缺失 + 1 列表标记字体）；**可选改 8 项**；另有 1 项全局记号体例需 Lead 裁决 |

结构自检数值：`\begin/\end` 18/18；花括号 191/191；`$` 550 个且逐行成对；`\[`/`\]` 49/49；UTF-8 无 BOM（首字节 `% =`）、LF（CR=0）、无 U+FFFD；无 `\documentclass/\usepackage/\begin{document}/\newcommand/\tag/**/$$/equation/align`。

> **版本说明**：tr04a.tex 在本校对期间（22:30:52）被 Lead 的批量操作更新过一次（与 c00、c-intro、tr05a、tr06a、tr09a 同一秒被写，属全项目批量改动）。本报告已按**更新后版本**（282 行、18,426 字节）复核：页标记 p.53–p.62、三个 `\section`、21 个 `\emph`、全部公式行（§三表内各行）以及 §七 的 4 个替换串**均未改变**；变化仅为字节级（`$` 总数 558→550，即 4 段行内数学被简化），均不落在本报告引用或核对的行内，故全部结论对当前版本有效。

**总体评价**：tr04a 属高质量译块——逐页对译完整、公式几乎逐符号还原，并且**特意保留了原文的 3 处笔误**（p.59 连续逆靶空间印作 $(\mathrm{Im}T)\to(\mathrm{Im}T)^\perp$；p.60 末式印作 $\frac{1}{2\|S\|}x$ 缺范数号；p.60 定义 5 印作「If ∈ Fred(H)」缺主语），批注（Tutor Note）质量高且可验证。落地只需 4 处小改。

---

## 二、编号完整性表（逐页对 200 dpi 页图 + 字体级粗体核验）

| # | PDF 页 | 原文（页图所见） | 原文编号 | tr04a 环境/写法 | 结论 |
|---|---|---|---|---|---|
| 1 | p.53（§7） | **Definition.** The *Hopf invariant* … | **无编号** | `\para{定义.}` | ✓ 正确（原文确为无号粗体，不应给 `\begin{defn}`） |
| 2 | p.53（§7） | **Theorem 1.** If λ_f is odd, then n=1,2,4. | 1 | `\begin{thm}{1}` | ✓ |
| 3 | p.56（§9） | **Theorem 1** (Linear Algebra). | 1 | `\begin{thm}{1（线性代数）}` | ✓ 本节第一个定理 |
| 4 | p.57（§9） | **Definition 1.** A Hilbert space … | 1 | `\begin{defn}{1}` | ✓ |
| 5 | p.57（§9） | **Definition 2.** A linear map … | 2 | `\begin{defn}{2}` | ✓ |
| 6 | p.58（§9） | **Definition 3.** A linear operator T is called *compact* … | 3 | `\begin{defn}{3}` | ✓ |
| 7 | p.58（§9） | **Proposition 1.** Let B(H) … | 1 | `\begin{prop}{1}` | ✓ |
| 8 | p.58（§9） | **Definition 4.** A bounded linear operator … is called *Fredholm* … | 4 | `\begin{defn}{4}` | ✓ |
| 9 | p.59（§9） | **Theorem 1.** (Atkinson) The following are equivalent: | **1（重号）** | `\begin{thm}{1（Atkinson）}` | ✓ **原文重号**（详见下） |
| 10 | p.60（§9） | **Definition 5.** If ∈ Fred(H), … | 5 | `\begin{defn}{5}` | ✓ |
| 11 | p.61（§9） | **Proposition 2.** If T₀,T₁ ∈ Fred(H) … | 2 | `\begin{prop}{2}` | ✓ |
| 12 | p.62（§9） | **Corollary 1.** If T is Fredholm and K compact … | 1 | `\begin{cor}{1}` | ✓ |

**关于「§9 内两个定理 1」的裁决（Lead 点名项）**

- **结论：原文重号，不是译者编号有误。** tr-04 按「号数照原文」保留并已在 p.56 批注中说明（tr04a.tex L129），**无需改动**。
- **判断依据（三重）**：
  1. p.56 页图**中部**（y≈288，位于 §8 标题与 §8 那一段之后）才是 §9 标题「**9** Lecture 1 (Some preliminaries from Functional Analysis, the Index of Fredholm Operators)」，而 **Theorem 1 (Linear Algebra).** 在 y≈580、位于该标题之后 —— 故该定理属于 §9；
  2. p.59 页图上部（y≈168，紧接 "One has the following fundamental result:" 之后）明确印作「**Theorem 1.** (Atkinson) The following are equivalent:」，PDF 文字层同为 `Theorem 1. (Atkinson)`；
  3. PyMuPDF 字体级扫描（CMBX12 粗体 span）：p.56 y=580 为「Theorem 1」，p.59 y=168 为「Theorem 1.」——两处标号均为粗体，号数均印作 1。
- 附带核验：p.56 的「(Linear Algebra)」与 p.59 的「(Atkinson)」在原文均为**正体（非粗体）**，只有「Theorem 1」是粗体；译本把括号说明纳入环境参数后变粗（见 §八 O2，建议保留）。
- 若按「每节从 1 起」的规则，p.59 本应为「定理 2」；但 STYLE_GUIDE 要求号数照原文、缺号/跳号写入回报，因此**保留重号 + 批注说明**是正确处理。建议 Lead 在《译注汇总》中保留这条说明。

---

## 三、公式逐符号核对表

抽查 16 条（页图 200 dpi 全页 + 关键处 700–900 dpi 裁图复核）。结论列：「✓」= 符号、上下标、花体、箭头、括号全部一致。

| # | 页 | 原文（页图核验） | tr04a 位置 | 结论 |
|---|---|---|---|---|
| 1 | p.53 | $S^{4n-1}\xrightarrow{f}S^{2n}\to S^{2n}\cup_f C^{4n}=X.$ | L15 | ✓（$C$ 为斜体、非 ℂ；`\xra{f}`、`\cup_f`、行末句点一致；900 dpi 见 rv53a） |
| 2 | p.53 | $\tilde K^0(X)=\Z\oplus\Z$；$i^*(x)=u_{2n}$；$x^2:\ i^*(x^2)=0$ | L18–28 | ✓ |
| 3 | p.54 | $\Psi^2(x)=2^n x+ay$；$\Psi^3(x)=3^n x+by$ | L51、L53 | ✓ |
| 4 | p.54 | $\Psi^k(y)=\Psi^k(p^*(u_{4n}))=p^*(\Psi^k(u_{4n}))=p^*(k^{2n}u_{4n})=k^{2n}y$ | L55 | ✓ |
| 5 | p.54 | $\Psi^2(x)\mapsto\Psi^2(u_{2n})=2^n u_{2n}$；$\Psi^3(x)\mapsto\Psi^3(u_{2n})=3^n u_{2n}$ | L57、L59 | ✓（$\mapsto$ 与页图 ↦ 一致） |
| 6 | p.54 | $\Psi^6(x)=\Psi^3(\Psi^2(x))=6^nx+(2^nb+3^{2n}a)y$；$\Psi^6(x)=\Psi^2(\Psi^3(x))=6^nx+(2^{2n}b+3^na)y$ | L61、L62 | ✓（800 dpi 见 rv54b） |
| 7 | p.54 | $2^nb+3^{2n}a=2^{2n}b+3^na\iff2^n(2^n-1)b=3^n(3^n-1)a$ | L64 | ✓ |
| 8 | p.54 | $\Psi^2(x)=x^2\bmod 2=\lambda_fy\bmod 2=y\bmod 2\Rightarrow a$ odd | L66 | ✓ 内容一致（原文 mod 斜体、译本 `\bmod` 正体；见 O4；900 dpi 见 rv54a） |
| 9 | p.55 | $S^3\to S^2,\ S(\C^2)=S^3\to S^2=\C P^1,(z_1,z_2)\mapsto[z_1,z_2]$；$S^7\to S^4,\dots$；$S^{15}\to S^8,\ S(\mathbb{O}^2)=\dots$ | L77–79 | ✓（ℂ/ℍ/𝕆 花体、变量 z/q/k 一致） |
| 10 | p.56 | $0\to\ker T\to V_0\xrightarrow{T}V_1\to\coker T\to0$；$\coker T=V_1/\operatorname{Im}T=V_1/T(V_0)=(\operatorname{Im}T)^\perp$ | L113、L115 | ✓（900 dpi 见 rv56a；`Im`→`im` 大小写见 O3） |
| 11 | p.56 | $[\ker T]-[V_0]+[V_1]-[\coker T]=0$ | L118 | ✓ |
| 12 | p.57 | $[V_0]-[V_1]=[\ker T]-[\coker T]$；$\|Tx\|\le c\|x\|,\ \forall x\in H$ | L133、L144 | ✓ |
| 13 | p.57 | $\|T\|=\sup\langle Tx,y\rangle$，$\|x\|=\|y\|=1$ | L148–149 | ✓（原文 sup 斜体、`< >`；译本 `\sup` 正体、`\langle\rangle`；见 O5） |
| 14 | p.58 | $\|T-F\|<\epsilon$（∀ε>0） | L163 | ✓（`\epsilon` 与页图同为 lunate ε；800 dpi 见 rv58a） |
| 15 | p.59 | $(ST-I)|_{\ker T}=-I|_{\ker T}$；$\|ST-I-F\|<1/2$；$\|STx-x\|\le(1/2)\|x\|$ | L200、L204、L206 | ✓ |
| 16 | p.60 | $\|STx\|\ge(1/2)\|x\|$；$\|Tx\|\ge\frac{1}{2\|S\|}x$；$\operatorname{Im}T=T(\ker F)+T((\ker F)^\perp)$ | L212、L214、L216 | ✓（**900 dpi 复核 rv60a：分母确为双竖线 $2\|S\|$；右端确缺 $\|x\|$ 的范数号**——原文如此，译本照排，批注 L239 已指出） |
| 17 | p.60 | $\operatorname{Ind}T:=\dim(\ker T)-\dim(\coker T)=[\ker T]-[\coker T]\in\Z$ | L223 | ✓（900 dpi 见 rv60c；`Ind`→`ind`，见 O3） |
| 18 | p.60 | $0\to\ker T_1\to\ker T_0T_1\to\ker T_0\to\coker T_1\to\coker T_0T_1\to\coker T_0\to0$ | L233 | ✓（项序完整） |
| 19 | p.61 | $S_t:H\to H\oplus\C^n$；$x\mapsto(T_tx,P_{\ker T_{t_0}}x)$；$\operatorname{Ind}S_t=\operatorname{Ind}T_t-n$；$Q_nT_{t_0}:H\to H_n$；$\operatorname{Ind}(Q_nT_{t_0})=\operatorname{Ind}T_{t_0}+m$ | L256–264 | ✓（900 dpi 见 rv61a） |
| 20 | p.62 | $\operatorname{Ind}(T+K)=\operatorname{Ind}T$ | L275 | ✓ |

（表中 L 为 tr04a.tex 行号。裁图见 §九。）

---

## 四、漏译

**结论：无整句、无整段缺失。** 逐页对照 `work/split/p053–p062.txt` 与 200 dpi 页图：

- **p.53**：引言斜体句、"Let …"、两个展示式、"using the exact sequence for the pair …"、生成元段、i*/u₂ₙ 段、Definition. 及其方程、"One can prove …"、"One then has the following result:"、Theorem 1 —— 全有。
- **p.54**：证明中的 12 个展示式、"with generators, say x and y (one for each copy of Z)"、两处 Ψ⁶ 计算、⇔ 式、mod 2 链、"Whence from …"、"By direct calculation …"、"There are three classical Hopf maps:" —— 全有（含原文 "taht" 笔误，批注已说明）。
- **p.55**：三族 Hopf 映射、"where H denotes … (the octonions)"、"It follows from Theorem 1 above …"、"An analogous question is this: …"（含问句与数列展示式）、"The answer is also negative."、S¹/S³/S⁷ 与 "1×S⁷ ⊂ S⁷×S⁷ → S⁷ … parallelisable spaces … tangent bundles are trivial" —— 全有（`(U(1)` 的残句亦按原样保留）。
- **p.56**：**§8 总起完整**（3 句：动机问题「∞−∞ 是什么」／Fredholm 指标与指标定理／C*-代数 K 理论是 Connes 非交换几何的组成部分）；§9 标题、K₀(*)=ℤ 段、V₀,V₁ 段、正合列、coker 式、Theorem 1、"The theorem holds for any short exact sequence …" —— 全有。
- **p.57–p.62**：逐段核对（Def 1/2、范数式、Hilbert 基与 ∞×∞ 矩阵、"finite rank operator"、Def 3、K(H)、Q(H) 与 Calkin 代数、"I is **not** compact"、Prop 1 及证明、Def 4、Atkinson 及证明、Fred(H)、Def 5、指标基本性质与蛇引理正合列、Example 与 Ue₀=e₁/Ue₁=e₂、"etc"、ker U 与 coker U、Prop 2 及 a./b./c. 三种情形、p.62 的命题 2 复述与 Cor 1）—— 全部译出。

**唯一不完整处不是漏句，而是「强调（斜体）覆盖不全」**（已用字体级扫描全量核对，原文 pp.53–62 共 22 处文本斜体 + 1 处斜体展示式）：

- 已正确用 `\emph` 还原的 **20 处**：p.53 引言句、p.53 *Hopf invariant*、p.55 *In the sequence of numbers*／*are there any other numbers?*／*The answer is also negative.*／*parallelisable spaces*、p.56 *what is infinity minus infinity*／*index*／*Fredholm*／*index theorems*／*noncommutative geometry*、p.57 *infinite*／*bounded*／*norm*／*Hilbert basis*、p.58 *finite rank operator*／*compact*／*Calkin algebra*／*Fredholm*、p.60 *Index*。
- **未还原的 2 处整句**：p.55 *It follows from Theorem 1 above that there no other such maps.*、p.60 *Intuitively one can say that the index measures … vanishes.* → 见 §七 M2、M3。
- **未还原的 1 处展示式**：p.55 *reals → complex → quaternions → Caley numbers* → 见 §八 O1（可选项）。

---

## 五、边界接缝

| 交界 | 上一块结尾 | 本块开头 | 结论 |
|---|---|---|---|
| tr-03 → tr-04（p.52/p.53） | `tr03a.tex` 末：p.52 Adams 运算性质的证明，`\[ \Psi^k(h\otimes\ldots\otimes h) = k^n(h\otimes\ldots\otimes h). \]` 后 `\end{proof}` + 2 条批注；最后一个页标记为 `% [原文 p.52]` | `tr04a.tex` 首：`% ===== 原文 pp.53–62 =====` → `% [原文 p.53]` → `\section{第六讲（…）}` → 斜体引言句 | ✓ 原文 p.52 以证明结束、p.53 以 §7 标题起；**无重复、无缺口**，页标记链 52→53 连续 |
| tr-04 → tr-05（p.62/p.63） | `tr04a.tex` 末：p.62 Corollary 1 的证明（`考虑 $T_t=T+tK$ 并应用命题 2。` + `\end{proof}` + 批注） | `tr05a.tex` 首：`% ===== 原文 pp.63–75 =====` → `% [原文 p.63]` → `\section{第二讲（Toeplitz 算子的指标、绕数与 K-同调）}` | ✓ 原文 p.62 只有命题 2 复述 + Cor 1 + 短证明；p.63 以 §10 标题起。**无重复、无缺口**，页标记链 62→63 连续 |

另核：tr04a 内部页标记 `p.53…p.62` 共 10 个、各出现 1 次、顺序正确，无漏页、无跳页。

---

## 六、术语

### 6.1 与 `glossary.tsv` 一致（抽查）

| 英文 | glossary | tr04a 用法 | 结论 |
|---|---|---|---|
| Adams operations | Adams 运算 | Adams 运算 | ✓ |
| Hopf invariant | Hopf 不变量 | Hopf 不变量 | ✓ |
| H-space | H-空间 | H-空间 | ✓ |
| Fredholm operator | Fredholm 算子 | Fredholm 算子 | ✓ |
| index | 指标 | 指标 | ✓ |
| quaternions / octonions | 四元数 / 八元数 | 四元数 / 八元数 | ✓ |
| dimension axiom | 维数公理 | 维数公理 | ✓ |
| exact sequence | 正合列 | 正合列 | ✓ |
| compact operator | 紧算子 | 紧算子 | ✓ |
| bounded operator | 有界算子 | 有界算子 | ✓ |
| Hilbert space | Hilbert 空间 | Hilbert 空间 | ✓ |
| inner product | 内积 | 内积 | ✓ |
| projection | 投影 | 投影 | ✓ |
| ideal | 理想 | 理想（「双边 $*$-理想」） | ✓ |
| C*-algebra | C*-代数 | $C^*$-代数（BRIEF 要求正文写法） | ✓ |
| unitary / division algebra | 酉的 / 可除代数 | 本篇未出现 | — |

### 6.2 glossary 缺项（建议 Lead 补入）

| 英文 | 建议中文 | 出现页 |
|---|---|---|
| Calkin algebra | Calkin 代数 | p.58 |
| noncommutative geometry | 非交换几何 | p.56 |
| finite rank operator | 有限秩算子 | p.58 |
| norm | 范数 | p.57 |
| Hilbert basis | Hilbert 基 | p.57 |
| closed graph theorem | 闭图像定理 | p.59 |
| snake lemma / serpent lemma | 蛇引理 | p.60 |
| short exact sequence | 短正合列 | p.56 |
| locally constant | 局部常值 | p.60、p.61、p.62 |
| orthonormal basis | 标准正交基 | p.61 |
| shift operator | 移位算子 | p.60–p.61 |
| interior point | 内点 | p.58 |
| parallelisable | 可平行化 | p.55 |
| cell | 胞腔 | p.53（仅批注） |
| index theorem | 指标定理 | p.56 |
| Caley numbers | Caley 数（原文拼作 Caley，应为 Cayley） | p.55 |

> 说明：`Caley` 系原文将 **Cayley** 拼错；译本保留「Caley 数」并在 p.55 批注（L99）指出，符合「原文笔误照译 + 批注」规则，**不是术语错误**。

---

## 七、必须改（4 项，可直接替换）

### M1　p.60｜定理 1（Atkinson）证明 b.⇒a.｜「bounded below」误译

- **原文（p.60 页图）**：*"namely $T$ is bounded below on $KerF$, thus $T(KerF)$ is closed."*
- **现状（L215）**：`即 $T$ 在 $\ker F$ 上下有界，从而 $T(\ker F)$ 是闭的。但`
- **问题**：`bounded below` = **有下界 / 下方有界**；「上下有界」会被读成「上有界且有下界」，改变数学含义（此处的结论只是由 $\|STx\|\ge\frac12\|x\|$ 推出 $\|Tx\|\ge c\|x\|$，即下方有界）。
- **可直接替换**：
  ```latex
  即 $T$ 在 $\ker F$ 上有下界，从而 $T(\ker F)$ 是闭的。但
  ```

### M2　p.55｜整句斜体缺失

- **原文（p.55 页图；字体扫描：CMSL12 斜体整行）**：*"It follows from Theorem 1 above that there no other such maps."*
- **现状（L83）**：`由上面的定理 1 可知，不存在其他这样的映射。`（无 `\emph`）
- **问题**：原文整句斜体；同一块内相邻的斜体句（p.53 引言句、p.55 *The answer is also negative.*）均已用 `\emph`，此处漏，属体例不一致。
- **可直接替换**：
  ```latex
  \emph{由上面的定理 1 可知，不存在其他这样的映射。}
  ```

### M3　p.60｜整段斜体缺失

- **原文（p.60 页图；字体扫描：CMSL12 两行斜体）**：*"Intuitively one can say that the index measures how far an operator is from being invertible since for invertible operators the index vanishes."*
- **现状（L228）**：`直观上可以说，指标衡量一个算子离可逆有多远，因为对可逆算子指标为零。`
- **可直接替换**：
  ```latex
  \emph{直观上可以说，指标衡量一个算子离可逆有多远，因为对可逆算子指标为零。}
  ```

### M4　p.61｜命题 2 证明的列表标记应为粗体（并与本文件 p.59 自相矛盾）

- **原文（p.61 页图；字体扫描：CMBX12 粗体 `a.`/`b.`/`c.`）**：证明中三种情形标为 **a.**、**b.**、**c.**（粗体）
- **现状（L253）**：`\begin{enumerate}[label=\alph*.,leftmargin=2.2em,itemsep=3pt]` → 标记为细体；而同文件 p.59（L188）已正确使用 `label=\textbf{\alph*.}`
- **可直接替换**（只改 p.61 这一处，L188 不动）：
  ```latex
  \begin{enumerate}[label=\textbf{\alph*.},leftmargin=2.2em,itemsep=3pt]
  ```

> 以上 4 处替换串均在 tr04a.tex 中**唯一**（已用正文本匹配核验 count=1），可直接替换。

---

## 八、可选改（8 项）

### O1　p.55｜数列展示式斜体未还原（可选）

- **原文**：*reals → complex → quaternions → Caley numbers* 为斜体文本（CMSL12）
- **现状（L86）**：`\[ \text{实数}\to\text{复数}\to\text{四元数}\to\text{Caley 数} \]`（正体）
- **若要求逐字符还原**，可替换为：
  ```latex
  \[ \text{\emph{实数}}\to\text{\emph{复数}}\to\text{\emph{四元数}}\to\text{\emph{Caley 数}} \]
  ```
- **建议**：中文斜体效果有限，不改亦可；若改，与 M2/M3 一并算作「强调还原」。

### O2　p.56 / p.59｜定理标题括号说明被加粗（建议保留）

- **原文**：**Theorem 1** (Linear Algebra).　/　**Theorem 1.** (Atkinson) —— 只有「Theorem 1」粗体，括号说明正体
- **现状**：`\begin{thm}{1（线性代数）}`、`\begin{thm}{1（Atkinson）}` → 环境 `\textbf{定理 #1.}` 使括号说明也变粗（成为「定理 1（线性代数）.」）
- **建议**：**保留现状**（中文体例可接受；改成 `\begin{thm}{1}（线性代数）` 会让标点位置变成「定理 1.（线性代数）」，未必更好）。仅记录差异。

### O3　记号大小写/正体（**全局体例，需 Lead 裁决，不建议 tr04a 单块改**）

- **原文**（pp.56–62 页图）：`ImT`、`KerT`、`IndT`、`Fred(H)`、`IndexT` 均为**数学斜体且首字母大写**（`cokerT` 小写）。
- **tr04a**（全文件出现次数，含批注）：`\im`(23)→渲染 `im`；`\ker`(34)→`ker`；`\ind`(21)→`ind`；`\mathrm{Fred}`(8)、`\mathrm{Index}`(2) 正体；`\coker`(13) 正体小写。
- **判断**：这是 `preamble.tex`（Lead 独占）中 `\im=\operatorname{im}`、`\ind=\operatorname{ind}` 的全局约定，tr04a 用宏本身**合规**；但与原文的**大写/斜体**不符。若只改 tr04a 会有 80+ 处且与其余块不一致，**风险高、不推荐**。若 Lead 要求全书逐字符还原，应在 preamble 层面统一（如另设 `\Im`、`\Ind`、`\Ker`），或全书统一改写。→ **决策项，不是 tr04a 的缺陷**。

### O4　p.54｜`\bmod` 与原文斜体 mod（建议保留）

- **原文**：`x^2 mod 2 = λ_f y mod 2 = y mod 2`（mod 为数学斜体）
- **现状**：`x^2\bmod 2=…`（正体 mod，间距更大）
- **建议**：保留 `\bmod`（语义明确、排版规范）。若坚持还原可改 `\ x^2\ mod\ 2\ `，但不推荐。

### O5　p.57｜`\sup` 与尖括号（建议保留）

- **原文**：`||T|| = sup < Tx, y >`（sup 斜体、尖括号为 `< >` 字符）
- **现状**：`\|T\|=\sup\langle Tx,y\rangle`（正体 sup、规范尖括号）
- **建议**：保留现译（更正确，且与全书算子正体体例一致）。仅记录。

### O6　p.56｜「异域的」（exotic）用词

- **原文**：*"generalised (or exotic) homology theory"*
- **现状（L108）**：`广义的（或「异域的」）同调理论`
- **建议**：改「奇异的」或「非寻常的」更贴切。可替换片段：
  ```latex
  因此它是广义的（或「非寻常的」）同调理论。
  ```

### O7　p.60｜「若 ∈ Fred(H)」照译缺主语（建议保留）

- **原文**：*"If ∈ Fred(H), then we define the Index of T…"*（原文缺主语 T）
- **现状（L222）**：`若 $\in\mathrm{Fred}(H)$，则定义…`（照原文，批注 L239 已说明）
- **建议**：保留（符合「原文笔误照译 + 批注」规则）。若 Lead 更看重可读性，可改 `若 $T\in\mathrm{Fred}(H)$`，但同时要把 L239 批注中「缺主语」一句改为说明译文补足——两种做法需二选一，**默认保留**。

### O8　批注增强（Tutor Note，不影响排版）

1. **p.61（L269）**：`$\ind(Q_nT_{t_0})=\ind T_{t_0}+m$` 的 $m$ 原文未定义——可补算出 $m=n+1$：$Q_n$ 的核为 $\operatorname{span}\{e_0,\dots,e_n\}$（维数 $n+1$）、余核为 0，故 $\ind(Q_n)=n+1$，由可加性 $\ind(Q_nT_{t_0})=\ind T_{t_0}+(n+1)$。
2. **p.58（L182）**：「internal point 是 interior point 的**旧式说法**」措辞不确；建议改为「原文用 *internal point*（非标准说法），标准术语为 *interior point*（内点）」。
3. **p.59（L208）**：可补一句：原文说「上述连续双射有连续逆」，但连续性并未论证——作者引闭图像定理正是为补这个缺口（先由 (KerT)⊥→ImT 是连续双射，再用闭图像定理得逆连续），批注现只指出靶空间笔误，未点出这层逻辑。

> 另记录一处**不建议改**的体例差异：p.61 首行 `\[ \text{\emph{等等}} \]` 把 "etc" 排成展示式（原文 "etc" 也是单独一行的斜体词），可接受。

---

## 九、核对方法与被忽略的差异（证据清单）

**页图**：`work/pages/p053.png–p062.png`，全部 200 dpi 整页读图；关键公式另裁 500–900 dpi。

**500–900 dpi 裁图**（均在 `work/tmp/`）：

| 文件 | 目标 |
|---|---|
| rv53a.png | p.53 定义式 $S^{4n-1}\xrightarrow{f}S^{2n}\to\cdots$ |
| rv54a.png | p.54 `x² mod 2 = …` 链 |
| rv54b.png | p.54 $\Psi^6$ 计算式 |
| rv55a/b/c.png | p.55 斜体整句、问句与数列展示式 |
| rv56a.png | p.56 cokerT 式 |
| rv56i.png | p.56 §8 段斜体精确范围 |
| rv57a.png | p.57 $\|T\|=\sup\langle Tx,y\rangle$ |
| rv58a.png | p.58 定义 3 与 ε 字形 |
| rv59a.png | p.59 定理 1 标号（Atkinson） |
| rv60a.png | p.60 $\|Tx\|\ge\frac{1}{2\|S\|}x$（含双竖线与缺范数号） |
| rv60b.png | p.60 斜体整段 *Intuitively…* |
| rv60c.png | p.60 指标定义式 |
| rv61a.png | p.61 $x\mapsto(T_tx,P_{\ker T_{t_0}}x)$ |

**字体级扫描**（PyMuPDF，`work/tmp/rv_ital2.py`、`rv_bold.py`）：逐 span 提取 pp.53–62 的 CMR（正文）/CMMI（数学斜体）/CMSL·CMTI（文本斜体）/CMBX（粗体）/MSBM（ℤ 等）字体，据此得到**完整**的斜体清单（22 处 + 1 处展示式）与粗体清单（Definition/Theorem/Proposition/Corollary 标号、`Proof:`、`not`、`Example:`、a./b./c. 标记、节标题），用于：
- 确认 §9 两处「定理 1」都是粗体标号（原文重号的直接证据）；
- 确认原文斜体覆盖情况，得出 M2/M3/O1；
- 确认 p.58 「not」为粗体（译本用 `\textbf{不是}` ✓）；p.61 a./b./c. 为粗体（得出 M4）。

**结构化检查**：`\section` 3 个（与 BRIEF §3 逐字比较，`-ceq` 全等）；页标记 10 个；`\begin/\end` 18/18；`\tag` 0；`$` 550 逐行成对；花括号 191/191；`\[`/`\]` 49/49；UTF-8 无 BOM；LF（CR=0）；无 U+FFFD；无禁项。

---

## 十、声明

1. 本报告为**只读校对**结果：**未修改** `tr04a.tex`，也未修改任何他人文件；§七的替换文本请 Lead 或 tr-04 落改。（tr04a.tex 于 22:30:52 被 Lead 批量操作更新过一次，非本报告作者所为；本报告已按更新后版本复核，见 §一「版本说明」。）
2. 报告中所有页图判断均可复核：页图路径、裁图文件名、行号（Lxx 指 tr04a.tex 行号）已逐一给出。
3. 无「必须改」以外的疑点；O3（`\im/\ker/\ind` 大小写与正斜体）属全书级记号裁决，需 Lead 统一，tr04a 现状不构成错误。
