# r-charfisoc —— §5 特征层性质 / §6 F-等晶体 / §7 局部整体相容（原文 p.29–p.36）

## 1. 交付

| 文件 | 内容 | 行数 | 页锚 |
|---|---|---|---|
| `源码/sections/s07-character.tex` | §5 The character sheaf property | 116 | `\srcpage{29}`、`\srcpageinl{30}` |
| `源码/sections/s08-fisoc.tex` | §6 F-Isocrystals, p-divisible groups and modifications | 291 | `\srcpage{31}`、`32`、`33`、`34` |
| `源码/sections/s09-compat.tex` | §7 Local/global compatibility | 98 | `\srcpageinl{35}`、`\srcpage{36}` |

- 页锚共 8 个，p.29–p.36 每页恰好一次：s07 取 29、30；s08 取 31、32、33、34；s09 取 35、36。
  - p.30、p.35 的页界都落在句中（p.30 断在括号内「按其特征多项式 | 分解为乘积」；p.35 断在「若 $K_p$ 是我们的超特殊子群，| 则这就是……」），故用 `\srcpageinl`。
  - **p.34 归 s08**：该页 85% 是 §6（推论 6.10 起至两条 bullet），§7 标题只在页脚；p.29 归 s07 同理（该页首页即 §5 标题，§4 尾巴不属本块）。
  - ⚠️ 若 s06-statement 也放了 `\srcpage{29}`，请 Lead 去重（本块以 §5 标题为 p.29 的页首）。
- 编译：`build.bat check sections/s07-character.tex cf`、`s08-fisoc.tex cf`、`s09-compat.tex cf` 均 **0 error**，无缺字、无 `??`、scriptpage 未出现在环境/脚注内。s08 余 1 处 0.36pt overfull（定义 6.8 行），肉眼不可见，未再压。
- 译注：s07 8 条（4 `\yizhu` + 4 `\yizhuw`）、s08 6 条、s09 6 条。

## 2. 编号对齐表

定理/注环境共用 `[theorem]` 计数器、按 `\section` 编号，故在 main.tex 中依 §1–§4 之后自然得到 5.x/6.x/7.x，与原文逐条一致。

| 原文 | 译文 | 类型 |
|---|---|---|
| Remark 5.1–5.4 | remark ×4（5.1–5.4） | 注 |
| Proposition 6.1 | proposition | 命题 |
| Remark 6.2 | remark | 注 |
| Corollary 6.3 | corollary | 推论 |
| Theorem 6.4 | theorem | 定理 |
| Remark 6.5 | remark | 注 |
| Hope 6.6 | `hope` 环境（preamble 已定义，印作「期望」） | 期望 |
| Proposition 6.7 | proposition | 命题 |
| Definition 6.8 | definition | 定义 |
| Remark 6.9 | remark | 注 |
| Corollary 6.10 | corollary | 推论 |
| Proposition 6.11 | proposition | 命题 |
| Proposition 6.12 | proposition | 命题 |
| Theorem 7.1 ([28]) | theorem，可选参数 `[{[28]}]` | 定理 |
| Remark 7.2 | remark | 注 |
| Remark 7.3（Motivation for the cuspidality condition） | remark[尖点性条件的动机] | 注 |
| Remark 7.4（Equal characteristic case） | remark[等特征情形] | 注 |
| Remark 7.5（ℓ=p） | remark[$\ell=p$] | 注 |

原文无编号公式；译文中所有 display 均不编号（`\[…\]`）。§6.1.1 / §6.1.2 按 SPEC 用 `\subsubsection*{6.1.1.\ …}`，编号写在标题里。

## 3. 译注

| # | 文件·位置 | 内容 | 来源 |
|---|---|---|---|
| 1 | s07 L7 | 下降数据 = 连同 Frobenius 作用的粘合；Weil 层即带此结构的层 | 原文 §5, p.29 |
| 2 | s07 L8 | $L=\widehat{E}^{\mathrm{un}}$ 是最大非分歧扩域之完备化，σ 为其 Frobenius | 原文 §2.2, p.19 |
| 3 | s07 L60 | $\rho(\delta)$ 原文未定义，应是 $\pi$ 延拓到 $G(L)$ 的表示在 δ 处的取值 | 译者按 |
| 4 | s07 L69 | 原文写 $\pi(\delta)$ 而非 $\pi_\rho(\delta)$，照录 | 译者按 |
| 5 | s07 L79 | 「Kottitz」应为 Kottwitz，照录原拼写 | 译者按 |
| 6 | s07 L85 | $J_\delta$ 模的迹即 $x_\delta^*\cF_\varphi$ 的迹，归一化后与 $1_{K\delta K}$ 一致 | 原文 |
| 7 | s07 L89 | minuscule 指 μ 的每个权在单根下系数为 1，保留英文 | 译者按 |
| 8 | s07 L93 | 扭转因子一半来自 $\langle2\rho,\mu\rangle$，与 ρ 无关 | 原文 |
| 9 | s08 L54 | 预完满 = 基变换到某完满域扩张后成为完满空间 | 译者按 |
| 10 | s08 L119 | $A_{cris}$ 的 divided power 结构使 $p$-adic 对数与 Frobenius 相容 | 译者按 |
| 11 | s08 L226 | 原文「the fact that we $\mathbb{D}(\widetilde H_{\mathbb Q})$ is…」多一「we」 | 译者按 |
| 12 | s08 L230 | 预叠 = 只取值于群胚、不要求下降 | 译者按 |
| 13 | s08 L238 | partially proper 保留英文 | 译者按 |
| 14 | s08 L242 | 原文「We thus deduces」动词形式有误 | 译者按 |
| 15 | s09 L6 | PEL = 极化 + 自同态 + level | 译者按 |
| 16 | s09 L37 | 原文「transfert」是法语拼法 | 译者按 |
| 17 | s09 L66 | 原文「([2].」缺右括号 | 译者按 |
| 18 | s09 L75 | HN = Harder–Narasimhan 分层 | 原文 §2.4 |
| 19 | s09 L82 | Igusa 簇是 Newton 分层各层上的覆盖 | 原文 [12],[20] |
| 20 | s09 L84 | Jacquet 函子沿抛物子群取幂零根基下的余不变量 | 译者按 |

## 4. 疑点

| 位置 | 原文 | 类型 | 处理 | 状态 |
|---|---|---|---|---|
| p.29 | 「coindices with the action of δ」 | 笔误（coincides） | 照字面译「与 δ 的作用一致」 | 已处理 |
| p.30 | 「Kottitz sign」 | 笔误（Kottwitz） | 照录并出注 | 待 Lead 定 |
| p.30 | $u\circ\pi(g)=\rho(\delta)^{-1}\circ\pi(g)\circ\rho(\delta)\circ u$ | $\rho(\delta)$ 全文未定义 | 照录，出注 | 待 Lead 定 |
| p.30 | Frob 作用写作 $\oplus_\rho\lambda_\rho\pi(\delta)$ | 疑应为 $\pi_\rho(\delta)$ | 照录，出注 | 待 Lead 定 |
| p.32 | 「the link between crsytalline $p$-adic Hodge theory」 | 笔误（crystalline） | 正常译「晶体 $p$-adic Hodge 理论」 | 已处理 |
| p.32 | 「the cristalline site」 | 笔误 | 同上 | 已处理 |
| p.32 | $\mathbb{D}_S=\mathcal Y_{S,[0,1[}\subset\mathcal Y_{S,]0,1[}=\mathbb{D}_S^*$ | 印刷如此；按集合论 $[0,1[\not\subset\,]0,1[$，仅在 $\delta$ 取不到 0 时成立 | 完全照页面排 | 待 Lead 定 |
| p.33 | 「fully faithfull」「faithfull topology」 | 笔误（faithful） | 正常译「全忠实」「忠实拓扑」 | 已处理 |
| p.33 | 「the fact that we $\mathbb{D}(\widetilde H_{\mathbb Q})$ is the covariant Dieudonné-module」 | 多一「we」 | 按通顺读法译，出注 | 已处理 |
| p.34 | 「We thus deduces」 | 笔误 | 译「由此推出」，出注 | 已处理 |
| p.34 | 「rationnal Tate module」 | 笔误（rational） | 译「有理 Tate 模」 | 已处理 |
| p.34 | 「Hodge-de-Rham periods」 | 大小写/连字符不统一 | 统一作 de Rham 周期 | 已处理 |
| p.34 | 「(yes, there is conflict of notations…but the other E is Q_p now)」 | 作者自述记号冲突 | 照译并保留插入语 | 已处理 |
| p.35 | 「([2].」 | 缺右括号 | 照录，出注 | 待 Lead 定 |
| p.36 | 「on should have」 | 笔误（one should） | 译「应当」 | 已处理 |
| p.36 | 「ask wether」 | 笔误（whether） | 正常译 | 已处理 |
| p.36 | 「for the ordinary b」 | ordinary（非基本）情形，术语未在 glossary | 保留英文「ordinary 的 $b$」 | 待 Lead 定 |
| p.35 | $\mathrm{Sh}^\flat_\infty$ 的上标 ♭ | 原文未解释 | 照录，不臆断含义 | 待 Lead 定 |
| p.35 | $R\pi_{HT*}$ 与 $R\pi_{HT,*}$ | 原文星号一律上标（拉回），无逗号 | 照录 | 已处理 |

## 5. 需要 Lead 处理的三件事

1. **stmaryrd 缺失**：`\llbracket`/`\rrbracket` 未定义（已试探确认）。s08 首部暂用局部 `\providecommand` 顶替；建议 preamble 加 `\usepackage{stmaryrd}`，之后可删掉 s08 的两行 `\providecommand`。
2. **`hope` 环境**：preamble 已定义并印作「期望」，s08 直接用 `\begin{hope}`，无需再加。
3. **p.29 页锚可能重复**：s06-statement 若也放了 `\srcpage{29}`，请去重（本块以 §5 标题为该页页首）。

## 6. 新增术语建议

| 原文 | 建议译名 | 依据 |
|---|---|---|
| character sheaf | 特征层 | glossary |
| F-isocrystal | F-等晶体 | glossary |
| p-divisible group | p-可除群 | glossary |
| modification | 修正 | glossary |
| Hodge filtration | Hodge 滤过 | glossary |
| Hodge–Tate period morphism | Hodge–Tate 周期态射 | glossary |
| de Rham period | de Rham 周期 | 仿上一行，本书统一 |
| stable distribution | 稳定分布 | glossary |
| spectral action | 谱作用 | glossary |
| adjacent cycles / nearby cycles | 邻近循环 | 学界惯例（$R\Psi_{\bar\eta}$ 保留符号） |
| HN-stratification | HN-分层（Harder–Narasimhan） | 原文 §2.4 已用「HN 分层」 |
| cuspidality condition | 尖点性条件 | 学界惯例 |
| Igusa variety | Igusa 簇 | 保留拉丁专名 |
| Jacquet functor | Jacquet 函子 | 保留拉丁专名 |
| alternate sum | 交代和 | 学界惯例 |
| preperfectoid | 预完满 | 仿 perfectoid=完满 |
| prestack | 预叠 | 仿 stack=叠 |
| Level (structure) | level（结构） | 全书保留英文 |
| ordinary $b$ | 保留 ordinary | 术语风险，见疑点表 |
