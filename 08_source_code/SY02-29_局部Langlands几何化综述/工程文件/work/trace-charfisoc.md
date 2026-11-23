# trace-charfisoc —— 决策流水（§5–§7，p.29–p.36）

记录每个拿不准的地方：原文 → 我的处理 → 依据。凡「符号级」判断都以 `工程文件/work/pages/pNNN.png` 的放大裁图为依据。

## A. 页锚与分页

1. p.29 → `\srcpage{29}` 紧贴 `\section{特征层性质}`。
   依据：该页正文自 §5 标题起；页顶两行属 §4 收尾，归 s06，不在本块译。
2. p.30 → `\srcpageinl{30}`，插在「给定有限维 $E$-向量空间的自同构，| 按其特征多项式的根的绝对值……」的括号内部。
   依据：页界确在句中（页面图像 p.030 首行接「as a product」）。`\srcpageinl` 按 SPEC 用于句中页界。
3. p.31 → `\srcpage{31}` 紧贴 `\section{F-等晶体……}`。
   依据：p.31 页顶仍是 §5 的注 5.1–5.4（已译入 s07，不重复），全页 90% 属 §6，故页首归 s08。**这是与 s06/s07 唯一可能的锚点重叠点，已在报告中标出。**
4. p.32 → `\srcpage{32}` 放在 `\mathbf{A}^+` 显示式之后、「仍然定义一个 $\oo_E$-adic 空间」之前。
   依据：页界在 `…\setminus V([\varpi_R])` 与 `仍然定义` 之间，正好是一段被公式隔开的续句处。
5. p.33 → `\srcpage{33}` 在「我们由此推出一个函子」之前。
   依据：页界（p.033 首行 = 「of an F-isocrystal …」）在该句前。
6. p.34 → `\srcpage{34}` 在「我们由此推出以下结论」之前。
   依据：p.34 首行就是 `We thus deduces the following.`；初稿误置于页末两条 bullet 前，已改正。
7. p.35 → `\srcpageinl{35}`，插在「若 $K_p$ 是我们的超特殊子群，| 则这就是 Kottwitz 整模型……」之间。
   依据：p.34 末行断在 `subgroup`，p.35 首行接 `this is the generic fiber`。
8. p.36 → `\srcpage{36}` 在 `\begin{remark}[尖点性条件的动机]` 之前。
   依据：p.35 末行止于 `see [2].`，p.36 首行即 Remark 7.3。

## B. 符号级核对（逐条对图像）

1. p.29 (3) 求和下标：$\rho\in\widehat{S}_\varphi$（`\widehat`，不是 `\widetilde`），条件 $\rho|_{Z(\widehat G)^\Gamma}=\kappa(b)$。
2. p.29 $\nu_\delta:\mathbb{D}\to G$：$\mathbb{D}$ 是 blackboard（`\mathbb{D}`），不是 `\mathbf`。
3. p.30 分解式下标同为 $\kappa(\delta)$；Frobenius 作用印作 $\oplus_\rho\lambda_\rho\pi(\delta)$——**不是** $\pi_\rho(\delta)$；照录并出注。
4. p.30 迹的归一化因子是 $\frac{1}{\mathrm{vol}(K\delta K)}\mathbf 1_{K\delta K}$（`K\delta K`，不是 `K_\delta K`）。
5. p.31 $IC_\mu=\overline{\QQ}_\ell(\langle\rho,\mu\rangle)[\langle2\rho,\mu\rangle]$；扭转为 $\overline{\QQ}_\ell(1/2)$。
6. p.32 $\mathrm{B}^+_{cris}(R^\circ/\varpi_R)=H^0_{cris}(\Spec(R^\circ/\varpi_R)/\Spec(\ZZ_p),\mathcal O)[1/p]$；$A_{cris}$ 为 $W(R^\circ)\bigl[[\varpi_R^n]/n!\bigr]_{n\ge1}$ 的 $p$-adic 完备化（Teichmüller 括号在分子）。
7. p.32 夹逼式：$\Gamma(\mathcal Y_{[1/p^p,1]})\subset\mathrm B^+_{cris}\subset\Gamma(\mathcal Y_{[1/p^{p-1},1]})$。
8. p.32 $\delta(\varphi(y))=\delta(y)^{1/p}$。
9. p.32 命题 6.1 的空间下标为 $\mathcal Y_{(R,R^+),]0,1[}$（区间下标带括号，整段放在 `_{...}` 里）。
10. p.33 定理 6.4 的箭头是 $\xrightarrow{\sim}$：`Spec(\oo_F/\varpi_F) \xrightarrow{\ \sim\ } \Bun_{X_F}`。
11. p.33 命题 6.7 的正合列末项是 $i_*\omega_{\widetilde H_D}[1/p]$（下标 $\widetilde H_D$，tilde 在 H 上、D 再降一级）。
12. p.34 命题 6.11：首项 $\omega^\vee_{\widetilde H}[1/p]$（**下标只有 $\widetilde H$，无 D**），末项 $\omega_{\widetilde H_D}[1/p]$（有 D）；箭头标号 $\alpha^\vee_{\widetilde H_D}(1)$，tilde 在 H 上而非 α 上。10 倍放大裁图确认后改正了初稿的 $\widetilde\alpha$。
13. p.34 推论 6.10：$\mu(z)=\mathrm{diag}(\underbrace{z,\dots,z}_{d\text{-times}},1,\dots,1)$；$\overleftarrow h$/$\overrightarrow h$ 用 `\overleftarrow/\overrightarrow`。
14. p.35 交换图：节点 $\mathrm{Sh}^\flat_\infty$、$\mathcal F\ell^\diamond_\mu$、$\mathrm{Hecke}^\mu$、$\Bun_G$、$\Bun_G\times\Spa(\QQ_p)^\diamond$、$\Spa(E)^\diamond$；箭头 $\pi^\diamond_{HT}$、$g$、$i$、$\overleftarrow h$、$\overrightarrow h$、$(x_1,can)$，方块标记用 `\square`。
    坑：tikz-cd 标签含逗号必须加花括号 `"{(x_1,can)}"'`，否则报 `I think the culprit is a tikzcd arrow in cell`（已在独立探针中验证）。
15. p.35 相容性公式：$R\pi_{HT*}(\overline{\QQ}_\ell[\dim\mathrm{Sh}])[\Pi^p]=m\cdot i^*\overleftarrow h^*\mathscr F_{\varphi_{\Pi_p}}$；星号是上标（拉回），$R\pi_{HT*}$ 无逗号。
16. p.36 注 7.5：$R\pi_{HT*}\widehat{\mathcal O}_{\mathrm{Sh}_\infty}$ 与 $R\pi_{HT*}\mathcal O^+_{\mathrm{Sh}_\infty}/p$；$\widetilde J_b=\mathbb{B}^{\varphi=p}$；$x_b^*\mathscr F_\varphi$。
17. p.36 邻近循环印作 $R\Psi_{\bar\eta}$（正体 R，不是 $R\Psi$ 斜体）。

## C. 术语与文体决策

1. 「F-isocrystal」→ F-等晶体（glossary）；「$\varphi$-equivariant vector bundle」→ $\varphi$-等变向量丛。
2. 「preperfectoid」→ 预完满：仿 perfectoid=完满（glossary 只给了 perfectoid）。
3. 「prestack」→ 预叠：与「叠」对举，$H^0$ 处注明只是预叠。
4. 「modification」→ 修正（glossary），故 6.3 节标题「$p$-可除群与向量丛的修正」。
5. 「partially proper」不译，保留英文并出注：中文「部分紧」易与紧化混淆。
6. 「Hecke」在叠名中保留斜体拉丁（$Hecke^\mu$），与全文其他节一致。
7. 「minuscule」保留英文（出注解释：$\langle\mu,\check\alpha\rangle\le1$ 型条件）。
8. 「ordinary 的 $b$」保留 ordinary：中文「常／通常的」在 $p$-可除群语境下容易被读成别的意思。
9. 「cuspidality condition」→ 尖点性条件（学界惯例，glossary 未收）。
10. 「HN-stratification」→ HN-分层，并在注里点明 Harder–Narasimhan。
11. 「alternate sum」→ 交代和；「Igusa variety」→ Igusa 簇；「Jacquet functor」→ Jacquet 函子。
12. 「Stable distribution」「spectral action」：glossary 虽收录（§5、§7 的页码标注），但本块正文并未出现这两个词，故未强行使用，留待其他块。

## D. 原文疑误（照录 + 出注，详见报告 §4）

coindices / Kottitz / 未定义的 $\rho(\delta)$ / $\pi(\delta)$ 与 $\pi_\rho(\delta)$ / crsytalline / cristalline / faithfull（两处）/ 「we $\mathbb D(\dots)$ is」/ 「We thus deduces」/ rationnal / Hodge-de-Rham / 「([2].」缺括号 / 「on should」/ wether。

## E. 编译与排版

1. `build.bat check` 的参数必须用正斜杠：`sections/s08-fisoc.tex`；反斜杠会被 MSYS 吃掉，报 `! Undefined control sequence <argument> "sectionss 08-fisoc.tex"`。
2. 单章 check 时 `\section` 记为 1，故定理显示为 1.x；并入 main.tex（§1–§4 在前）即为 6.x/7.x，无需手工改号。
3. 行内 `\dfrac` 会把行撑高（§5 迹公式），改 `\tfrac`。
4. 长不可断的行内公式 $\mathrm B^+_{cris}(R^\circ/\varpi_R)$ 造成 26pt overfull，改写为「有限型的射影模，它定义在 … 上」后消失。
5. 标题里的数学要包 `\texorpdfstring`，否则 hyperref 报 `Token not allowed in a PDF string`；已处理 s08 的 section 与两个 subsection。
6. s08 首部两行 `\providecommand{\llbracket}`/`\rrbracket` 是 stmaryrd 缺失的临时顶替，Lead 加 `\usepackage{stmaryrd}` 后可删。
