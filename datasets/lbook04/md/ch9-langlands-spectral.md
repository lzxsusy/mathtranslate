# Langlands 谱问题：Eisenstein 级数与逆定理

> `lbook04/concept/ch9-langlands-spectral` · 轨 G GL_n 的 Langlands 纲领 · 状态 reviewed · 核验 source-only

**问题：** 为什么 $m=n$ 的 Rankin–Selberg 积分必须引入 Eisenstein 级数，而不能直接用两个尖点形式的 $L^2$ 内积？

**一句话：** $m=n$ 的积分需要第三函数——由 Schwartz 函数造的 Eisenstein 级数；其留数给出不变配对与非零性条件，逆定理则把「好」的扭 $L$ 函数反解为自守性。

**别名：** `Eisenstein 级数`、`谱理论`、`逆定理`、`留数配对`

## 定义

$m=n$ 时 $\int_{\mathrm{GL}_n(k)\backslash\mathrm{GL}_n(\mathbb{A})}\varphi\varphi'|\det g|^s\,dg$ 本质是 $L^2$ 内积，只在 $s$ 的特定值收敛，不能定义 $L$ 函数（608–617），但它的留数会以「内积」的形式重新出现。正确的做法是引入第三函数：取 $\Phi\in\mathcal{S}(\mathbb{A}^n)$、酉 idèle 类特征 $\eta$，令 $F(g,\Phi;s,\eta)=|\det g|^s\int_{\mathbb{A}^\times}\Phi(ae_ng)|a|^{ns}\eta(a)\,d^\times a$，再对 $P'_n(k)\backslash\mathrm{GL}_n(k)$（$P'_n=Z_nP_n$，分拆 $(n-1,1)$）求和得 Eisenstein 级数 $E$。用 Poisson 求和（通过 Theta 级数 $\Theta_\Phi(a,g)=\sum_{\xi\in k^n}\Phi(a\xi g)$）证 $E$ 亚纯、竖带有界、满足 $E(g,\Phi;s,\eta)=E(g^\iota,\widehat{\Phi};1-s,\eta^{-1})$，极点只可能在 $s=-i\sigma,1-i\sigma$。于是三重积分 $I(s;\varphi,\varphi',\Phi)$ 的留数给出 $\mathrm{GL}_n(\mathbb{A})$-不变配对；配对非零迫使 $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$，这就是定理 2.2。§5 的逆定理把同一机制反过来用：先假定一切扭 $L$ 函数「好」（整、竖带有界、标准函数方程），反解 Whittaker 函数，证明 $\Pi$ 拟自守——这正是 Hecke 逆定理在 $\mathrm{GL}_n$ 上的推广。

**记号：** $P_n$：棒状子群，$P_n\backslash\mathrm{GL}_n\cong k^n\setminus\{0\}$；$P'_n=Z_nP_n$：分拆 $(n-1,1)$ 的抛物子群；$\eta$：酉 idèle 类特征；$\Theta_\Phi$：Theta 级数；$\mathcal{T}(S;m)=\bigcup_{d=1}^m\mathcal{A}_0^S(d)$：用 $S$ 外无分歧的尖点表示作扭的集合。

## 要点

- $F$ 是 $\mathrm{Ind}_{P'_n}^{\mathrm{GL}_n}(\delta^{s-1/2}\eta)$ 的光滑截面，$E$ 是它的级数；两者不可混。
- Poisson 求和（Theta 表示）是解析延拓与函数方程的唯一入口；没有它，$E$ 只在 $\mathrm{Re}\,s>1$ 收敛。
- 留数非零 $\Rightarrow$ 存在 $\mathrm{GL}_n(\mathbb{A})$-不变配对 $\Rightarrow$ $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$；反过来该条件也保证 $s=1$ 处有极点（定理 4.2 后的两条观察）。
- 逆定理只需 $\pi'$ 跑遍 $\mathcal{T}(S;n-1)$（定理 5.1）；用 $\mathcal{T}(S;n-2)$ 可减弱假设（定理 5.2），类数一时还有 5.3 的细化。

## 公式

$$
F(g,\Phi;s,\eta)=|\det g|^s\int_{\mathbb{A}^\times}\Phi(ae_ng)|a|^{ns}\eta(a)\,d^\times a
$$

$$
E(g,\Phi;s,\eta)=\sum_{\gamma\in P'_n(k)\backslash\mathrm{GL}_n(k)}F(\gamma g,\Phi;s,\eta)
$$

$$
E(g,\Phi;s,\eta)=E(g^\iota,\widehat{\Phi};1-s,\eta^{-1})
$$

$$
\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}
$$

## 定理与证明

**定理 2.2（$m=n$ 的积分）**　$I(s;\varphi,\varphi',\Phi)$ 亚纯、竖带有界；极点全为单极点，且仅当 $\pi\cong\widetilde{\pi}'\otimes|\det|^{i\sigma}$ 时在 $s=-i\sigma,1-i\sigma$ 出现；满足函数方程，可分解时等于 Euler 乘积。

*出处：译文 §2.3*

**定理 5.1（逆定理）**　若 $\Pi$ 对一切 $\pi'\in\mathcal{T}(S;n-1)$ 都「好」，则 $\Pi$ 拟自守；$S=\varnothing$ 时 $\Pi$ 本身是尖点自守表示。

*出处：译文 §5*

## 易错点

- 把 Eisenstein 级数的解析性质当成「显然」：没有 Poisson 求和就得不到函数方程，$E$ 只在右半平面有定义。
- 以为「好」只要函数方程：逆定理要求整性、竖带有界、标准函数方程三条同时成立，缺一不可。
- 把 §2.3 的留数配对与 §2.2 的 $P_n$ 投影混淆：前者作用于两个尖点形式（三重积分），后者作用于一个函数再与另一个配对。

## 批注

**〔背景直觉〕谱理论为什么在这里出现**　$m=n$ 时 $L^2$ 内积本身就是 $L$ 函数在 $s=1$ 的留数，无法提供新信息；Eisenstein 级数把「两两配对」提升为「三重积分」，其留数才携带 $\pi$ 与 $\pi'$ 的耦合。§5 末尾把这套论证称为 Langlands 谱理论的弱形式。

## 相关

[[ch9-functional-equation]]、[[ch9-automorphic-representation]]、[[ch9-godement-jacquet]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§2.3，原书 pp. 206–211（PDF pp. 209–214）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch09.tex:601-784`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§5，原书 pp. 222–225（PDF pp. 225–228）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch09.tex:1406-1588`
