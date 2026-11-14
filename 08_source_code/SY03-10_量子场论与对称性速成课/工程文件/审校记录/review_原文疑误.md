# 原文疑误与记号不一致汇总

**原则**：以下各条均为译者逐页对照原 PDF（文字层 + 高倍渲染图）发现的问题。
**译本一律照录原文、不擅自修改公式**，仅在对应位置的 `% [Tutor Note: …]` 中说明并给出
可替换写法；本汇总供教授核对原书（AMS/作者主页版本）时参考。
页码格式："PDF p.N" 为 PDF 页序号，"printed p.N−1" 为页脚页码。

---

## 第 1 章（PDF p.2–6）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 1.1 | PDF p.3 | "in quanatum field theory" | 笔误，应为 *quantum* |
| 1.2 | PDF p.6 | "These examples play an fundamental role" | 语法笔误，应为 *a* fundamental role |
| 1.3 | PDF p.4 | $\mathcal{E}\neq\prod_{p\in X}E_p$ | 用"≠"表示"截面空间不是逐点纤维的任意选择"，非严格集合论陈述，已在批注解释 |

## 第 2 章（PDF p.7–14）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 2.1 | PDF p.7（定义 2.1） | $d_nd_{n+1}=0$ | 按复合次序应为 $d_n\circ d_{n-1}=0$（等价 $d^2=0$）；下文正用它推出 $\operatorname{Im}(d_{n-1})\subset\ker(d_n)$，疑笔误 |
| 2.2 | PDF p.7–8、13 | $(C^{\bullet},d)$ 与 $(C^{*},d)$、$(\Omega^{*}(U),d)$ 与 $(\Omega^{\bullet}(U),d)$ 混用 | 原文上标记号不统一（实心圆点/星号），非排版错误；译本照录 |
| 2.3 | PDF p.7–13 | $H_{dR}^{P}$（大写 $P$）与 $H^{p}$（小写 $p$）混用 | 同上，原文记号不一致 |
| 2.4 | PDF p.8 | "$\vec n_x$ is tangent at $\mathcal{K}$" | 表述含糊：外法向应是 $\partial\mathcal{K}$ 的法向，而非 $\mathcal{K}$ 的切向；照译+批注 |
| 2.5 | PDF p.9（例 2.5） | $\iiint_K$ 下标作正体 $K$，而 $\iint_{\partial\mathcal{K}}$ 作花体 | 同一页记号不一致（例 2.4 统一用花体 $\mathcal{K}$） |
| 2.6 | PDF p.13（定义 2.9） | 第二式印作 $\partial_t^{*}(\alpha)$ | 按上下文（流 $\varphi_t$ 的拉回）应为 $\varphi_t^{*}(\alpha)$，疑笔误 |
| 2.7 | PDF p.13（定义 2.10） | $\iota_V(\dd x^{i_1})\wedge\cdots\wedge\dd x^{i_p}$ | 按内积定义，第二项起应为 $\dd x^{i_2}\wedge\cdots$；原文省略号处隐含该修正，照录+批注 |
| 2.8 | PDF p.14 | $\varphi_{-\infty}:\R^n\to\{0\}\in\R^n$ | "∈"应为"⊂" |
| 2.9 | PDF p.14 | $\alpha=\dd(\int\iota_V(\varphi_t^{*}(\alpha)\dd t))$ | 少一个右括号且 $\dd t$ 落入 $\iota_V$ 括号内；按下一行 $\beta$ 的定义应读作 $\dd(\int\iota_V(\varphi_t^*(\alpha))\,\dd t)$ |
| 2.10 | PDF p.12 | $\varphi^{-1}=\varphi_{-t}$ | 不严谨，应理解为 $\varphi_t^{-1}=\varphi_{-t}$ |

## 第 3 章（PDF p.15–22）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 3.1 | PDF p.16（例 3.5） | 变分第三行末缺 $\dd t$（前两行有） | 漏排 |
| 3.2 | PDF p.16 | "Euler–Lagrangian equation" | 通行名称是 Euler–Lagrange equation；原文如此，照译+批注 |
| 3.3 | PDF p.19 | $\frac{\dd}{\dd t}H=\partial_pH\,\dot p+\partial_q\,\dot q$ | 第二项漏 $H$：按 Hamilton 方程应为 $\partial_qH\,\dot q$；同页末式 $-\partial_pH\partial_qH+\partial_qH\partial_pH=0$ 可印证 |
| 3.4 | PDF p.19 | $\mathcal{X}_a$ 与同段 $\mathcal{X}_\alpha$ 混用 | 疑 $a$ 为 $\alpha$ 之误 |
| 3.5 | PDF p.20（例 3.11） | $\delta_{\tilde\epsilon}S=\int\tilde\epsilon\,\frac{\dd}{\dd t}H$ | 按 $H=p\dot q-\mathcal{L}$ 应得 $-\int\tilde\epsilon\,\frac{\dd H}{\dd t}$；若按原文正号则与紧随的 $\tilde J=H$ 矛盾，疑符号笔误 |

## 第 4 章（PDF p.23–30）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 4.1 | PDF p.23 末式 | $(d_{\mathrm{CE}}c^{\alpha_1})\cdots\gamma^{\alpha_p}$ | 按 Leibniz 法则首项应为 $(d_{\mathrm{CE}}c^{\alpha_1})c^{\alpha_2}\cdots c^{\alpha_p}$；原文出现 $\gamma^{\alpha_p}$，疑笔误 |
| 4.2 | PDF p.26–27（例 4.11） | 括号公式上指标全印成 $i$ | 应为 $\alpha^j_J\partial_j\beta^i_M-\beta^j_M\partial_j\alpha^i_J$；$\beta$ 的展开式漏印 $\otimes$ |
| 4.3 | PDF p.25–27（例 4.10） | 流形先记 $X$，后文公式一律小写 $x$ | 记号不一致 |
| 4.4 | PDF p.25 | "an useful" | 语法笔误 |
| 4.5 | PDF p.27 | "Chevally-Eilenberg" | 应为 Chevalley–Eilenberg |
| 4.6 | PDF p.28 | "ifferential" | 漏字母，应为 differential |

## 第 5 章（PDF p.31–47）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 5.1 | PDF p.39（对照表） | 左栏 $(A^{-1})^{ij}$ | 与前文 $(Q^{-1})^{ij}$ 不一致；按上下文应为 $Q^{-1}$ |
| 5.2 | PDF p.39–40 | 公式用 $2s$、图注/下文用 $2m$ | 记号不一致（同一参数） |
| 5.3 | PDF p.35（定义 5.4） | $\gamma$ 与 $\Gamma$ 混用 | 图与映射记号未区分 |
| 5.4 | PDF p.35 | "edgesfor" | 漏空格，应为 "edges for" |
| 5.5 | PDF p.40 | "meanful" | 应为 meaningful |
| 5.6 | PDF p.33 | 展示公式 $(*)$ 无编号，仅正文以"(*) "引用 | 原文体例，译本用 `\tag*{$*$}` 保留该标记 |
| 5.7 | PDF p.41 | $\langle O\rangle$ 分子用 $S_0[\gamma]$、分母写 $S[\gamma]$ | 疑分母应为 $S_0[\gamma]$（或 $S$ 与 $S_0$ 记号未统一） |
| 5.8 | PDF p.46 | 热核分母写 $(2\pi t)^2$ | $\R^4$ 上标准热核为 $(4\pi t)^{-2}$，疑差因子 16，直接影响 $\log\epsilon$ 系数，已批注请核对原书 |
| 5.9 | PDF p.45–46 | "it can shown that"、"possibley"、"in physics in the momentum cut-off" | 英文笔误（应为 be shown / possibly / is the） |

## 第 6 章（PDF p.48–60）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 6.1 | PDF p.49 | 正文两次写 $V\times\mathfrak{g}[-1]$，同段末积分却写 $\int_{V\times\mathfrak{g}[1]}$ | 前后不一致，疑为 $\mathfrak{g}[-1]$ |
| 6.2 | PDF p.49 | 序列 $0\to\mathcal{O}(V)^G\to\mathcal{O}(V)\to\mathfrak{g}^{\vee}\otimes\mathcal{O}(V)$ 称 "exact sequence" | 仅在 $H^0$ 处正合（连通 $G$），原文为简写，已批注 |
| 6.3 | PDF p.51 | $\theta_i\equiv\partial_j$ | 指标不匹配，应为 $\theta_i\equiv\partial_i$ |
| 6.4 | PDF p.52 | "SchoutenNijenhuis" | 缺连字符，应为 Schouten–Nijenhuis |
| 6.5 | PDF p.54（例 6.11） | $\deg(e_\alpha=-2)$ 括号错位 | 应为 $\deg(e_\alpha)=-2$ |
| 6.6 | PDF p.54 | $\{c^\alpha,e_\alpha\}=\delta^\alpha_\beta$ | 指标不匹配，应为 $\{c^\alpha,e_\beta\}=\delta^\alpha_\beta$ |
| 6.7 | PDF p.55 | $\delta(e_\alpha)=\tfrac12 f^{\gamma}_{\alpha\beta}c^\beta e_\gamma$，而紧随的向量场第二项 $\sum f^{\gamma}_{\alpha\beta}c^\beta e_\gamma\partial/\partial e_\alpha$ 无 $\tfrac12$ | 按 BV 括号计算第二项应无 $\tfrac12$，疑第一个 $\tfrac12$ 为笔误 |
| 6.8 | PDF p.56 | 前句 $C^{\bullet}(\mathfrak{g},\mathrm{PV}(X)\otimes\mathrm{Sym}(\mathfrak{g}[2]))$ 与后句 "acts on $\mathrm{Sym}(\mathfrak{g}[1])$" 移位不一致 | 疑 $\mathfrak{g}[1]$ 为 $\mathfrak{g}[2]$ |
| 6.9 | PDF p.56 | "A few moment thought" | 应为 moments |
| 6.10 | PDF p.59 | "cohomology clas" | 应为 class |
| 6.11 | PDF p.59 | $\tilde S^1-S^1$ 上标 $1$ | 疑为下标 $\tilde S_1-S_1$ |
| 6.12 | PDF p.56（定义 6.14） | "An degree 0 element" | 语法笔误，应为 A degree |

## 第 7 章（PDF p.61–70）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 7.1 | PDF p.61 | $\Delta_K$ 公式中两处 $\hat\alpha_i$ | 第二处应为 $\hat\alpha_j$（与求和的 $j$ 对应） |
| 7.2 | PDF p.62 | "intepretation" | 应为 interpretation |
| 7.3 | PDF p.64 | "correspons" | 应为 corresponds |
| 7.4 | PDF p.67（定义 7.8） | 首句缺谓语 "is" | "an effective perturbative quantization … is a family" |
| 7.5 | PDF p.67 | "a pictue" | 应为 picture |
| 7.6 | PDF p.67 | "Just as we have is the discussion…" | 多一个 is |
| 7.7 | PDF p.70 | "traded from $\Delta$" | 语义不清，疑为 derived / traced from |

## 第 8 章（PDF p.71–76）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 8.1 | PDF p.71 | "k-vector sapce" | 应为 space |
| 8.2 | PDF p.72 | "algerba" | 应为 algebra |
| 8.3 | PDF p.72 | "We can associative a prefactorization" | 应为 associate |
| 8.4 | PDF p.72（例 8.2） | $\bigotimes_{\alpha\in K}a_k$ | 指标 $k$ 与 $\alpha$ 不一致，应为 $a_\alpha$ |
| 8.5 | PDF p.74（命题 8.7 证明） | $\{x_1,\dots,x_k\}$ | 按上下文应为 $\{x_1,\dots,x_n\}$ |
| 8.6 | PDF p.74 | "assigns compactly sections" | 应为 compactly supported sections |
| 8.7 | PDF p.74 末 | 两个求和各多一右括号，末项上标仅 $\boxtimes$ | 疑漏 $m$（前两项为 $\boxtimes^m$） |
| 8.8 | PDF p.75（定义 8.11） | 写 $U\subset X$，而底流形为 $M$ | 记号不一致 |
| 8.9 | PDF p.75 | "Costello-Gwillian" | 应为 Gwilliam |
| 8.10 | PDF p.76 | 链映射 $(C_\bullet((A[[\hbar]],b)$ 多一左括号 | 括号不匹配 |

## 第 9 章（PDF p.77–92）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 9.1 | PDF p.77–78 多处 | $C^{\infty}(x)$（小写 $x$） | 应为 $C^{\infty}(X)$ |
| 9.2 | PDF p.86 | "by Moayl product" | 应为 Moyal |
| 9.3 | PDF p.86 | $\lim_{\epsilon\to\infty}$ | 经核对原图确为 $\infty$（作者 RG 方向约定），非笔误，已在批注提醒勿擅改 |
| 9.4 | PDF p.86 | $\widehat\Omega^{\bullet}_{2n}\to\widehat\Omega^{-(\bullet+1)}_{2n}$ 的负次数写法 | 原文如此，易被误当排版错误；照录+批注 |
| 9.5 | PDF p.88 | 下降映射说明写 "on $P$"，公式却是 $(\Omega^{\bullet}(X;V_P),\nabla^\gamma)$ | 应为 on $X$ |
| 9.6 | PDF p.90（注 9.18） | $\operatorname{Hom}(\wedge^2,\mathfrak{gl})$ | 省略了 $\mathfrak{g}$，应为 $\operatorname{Hom}(\wedge^2\mathfrak{g},\mathfrak{gl})$ |
| 9.7 | PDF p.91 | $\partial_{\mathrm{Lie}}\operatorname{Tr}=\delta(-)$ | 简写，含义为 $\partial_{\mathrm{Lie}}\operatorname{Tr}$ 与 $\delta$ 作用于某元素相等 |
| 9.8 | PDF p.92 | 称 $\Theta$ 为 "canonical identity map" | 定义域/值域不同，应理解为商映射/典范等同 |

## 第 10 章（PDF p.93–101）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 10.1 | PDF p.93（真空公理） | $Y(|0\rangle,z)=1_{d\mathcal{V}}$ | 记号可疑（疑为恒等算子 $\mathrm{id}_{\mathcal{V}}$） |
| 10.2 | PDF p.94（局域性公理） | $\{Y(A,z)\}_{a\in\mathcal{V}}$ | 下标应为 $A\in\mathcal{V}$ |
| 10.3 | PDF p.98 | $\operatorname{Conf}_n$ 中 $p_i\neq p_i$ | 应为 $p_i\neq p_j$ |
| 10.4 | PDF p.99 | $\operatorname{Index}=[e^{\omega_\hbar/\hbar}\widehat A]$ | 与 PDF p.92 的 $e^{-\omega_\hbar/\hbar}$ 差一负号 |
| 10.5 | PDF p.96 | $a_i(\varphi)\in\omega^{0,\bullet}(E)$（小写 $\omega$） | 与场空间 $\Omega^{0,\bullet}(E)$ 记号不一致 |

## 参考文献（PDF p.101–103）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| R.1 | [21] | "BatalinVilkovisky" | 版面即缺连字符，应为 Batalin–Vilkovisky |
| R.2 | [34] | "14031474" | 疑为 1403–1474 |
| R.3 | [35] | "613645" | 疑为 613–645 |
| R.4 | [25] | "July 610, 1992" | 疑为 "July 6–10"（会议日期缺连字符） |
| R.5 | 多条 | 作者名后双句点（"S.."、"F.."、"G.."） | 原文排版如此，照录 |

---

## 附：非"疑误"但值得注意的原文记号约定（译本均原样保留）

1. **作用量符号**：Minkowski 号差下 $\ee^{\ii S/\hbar}$；Euclidean 化后 $\ee^{-S_E/\hbar}$（第 1 章批注）。
2. **de Rham 上同调**：$p$ 与 $P$ 混写（第 2 章），$H_c^p$ 紧支集版本。
3. **BV 括号**：$\{a,b\}=\Delta(ab)-(\Delta a)b-(-1)^{|a|}a\Delta b$，其中 $\Delta=\mathrm{Div}_\Omega$ 带负号约定（第 6 章批注）。
4. **OPE**：$A(z)B(w)=\sum_n (A_{(n)}B)(w)/(z-w)^{n+1}$（第 1、10 章批注；与部分文献 $n\to-n-1$ 只差重编号）。
5. **Moyal 积**：$f*_\hbar g=fg+\frac{\mathrm{i}\hbar}{2}\{f,g\}+O(\hbar^2)$（第 5、9 章批注；注意 $\hbar\to\mathrm{i}\hbar$ 的文献约定）。
6. **$\fint$**：原文"积分号加横杠"的正则化积分记号，本译本用 `\fint` 实现（第 10 章）。
