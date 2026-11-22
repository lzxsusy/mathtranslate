# Arthur–Selberg 迹公式

> `lbook04/concept/ch8-arthur-selberg` · 轨 T Tate 与迹公式 · 状态 reviewed · 核验 source-only

**问题：** 为什么在除代数 $D$ 上做迹公式，能证明 $\operatorname{GL}(2)$ 表示的自守性提升？

**一句话：** 在 $D_{\mathbb A}^\times$（$D$ 为次数 $p^2$ 的中心除代数）上取测试函数 $\varphi$，迹 $\operatorname{tr}T_\varphi$ 按共轭类展开；比较 $D^\times$ 与 $\operatorname{GL}(2)$ 的展开即得 Jacquet–Langlands 对应。

**别名：** `Arthur–Selberg trace formula`、`adelic 迹公式`、`twisted trace`

## 定义

设 $D$ 为 $F$ 上次数 $p^2$ 的中心除代数，$S$ 为使 $D_v$ 为除环的有限位集。取 $H$ 为 $D_{\mathbb A}^\times$ 上光滑、模 $Z$ 紧支的函数，$T_\varphi$ 为积分算子。定理 52（$(59)$）：$\operatorname{tr}T_\varphi=\sum_\gamma\operatorname{vol}(C_\gamma\backslash C_\gamma(\mathbb A))\int_{C_\gamma(\mathbb A)Z_{\mathbb A}\backslash D_{\mathbb A}^\times}\varphi(g^{-1}\gamma g)dg$；命题 53 把非中心共轭类对应到满足 $[F(\alpha):F]=p$ 且 $\forall v\in S$ $[F_v(\alpha):F_v]=p$ 的域扩张；定理 54 比较 $D$ 与 $\operatorname{GL}(2)$ 的迹，得 $\pi'$ 出现在 $E$ 的 $L^2$ 中，$(60)$ $\operatorname{tr}T_\varphi=\operatorname{tr}T'_{\varphi'}$。

**记号：** $D$：中心除代数；$D_{\mathbb A}^\times$；$C_\gamma$：中心化子；$S$：分歧位集；$\pi'$：$D^\times$ 的自守表示；$T_\varphi,T'_{\varphi'}$。

## 要点

- 迹公式的 adelic 版本把「共轭类」换成「中心化子的体积」，从而同时处理所有位。
- 命题 53 的域扩张条件 $[F(\alpha):F]=p$ 是 $p^2$ 次除代数的特征；局部条件 $\forall v\in S$ 保证 $\alpha$ 在分歧位生成域扩张。
- 定理 55（Jacquet–Langlands）：$\operatorname{GL}(2,\mathbb A)$ 自守 $\pi$ 是 $D_{\mathbb A}^\times$ 自守表示的提升 $\iff$ $\forall v\in S$，$\pi_v$ 平方可积。
- 对应保持 $L$ 函数与 $\varepsilon$ 因子（annote 2008–2014），故 $L$ 函数的函数方程可从 $D^\times$ 侧转回 $\operatorname{GL}(2)$。

## 公式

$$
\operatorname{tr}T_\varphi=\sum_\gamma\operatorname{vol}(C_\gamma\backslash C_\gamma(\mathbb A))\int_{C_\gamma(\mathbb A)Z_{\mathbb A}\backslash D_{\mathbb A}^\times}\varphi(g^{-1}\gamma g)\,dg
$$

$$
\operatorname{tr}T_\varphi=\operatorname{tr}T'_{\varphi'}
$$

## 易错点

- $S$ 不能取空集：若 $D$ 在所有位分裂，则 $D\cong M_2(F)$，对应退化为恒等；必须让 $D$ 在至少一个位是除环。
- 「平方可积」是局部条件：$\forall v\in S$，$\pi_v$ 平方可积（离散系列或超尖点），不是要求 $\pi$ 整体平方可积。

## 批注

**〔背景直觉〕为什么用除代数**　$D^\times$ 的迹公式比 $\operatorname{GL}(2)$ 少很多共轭类（非中心类只来自 $p$ 次域扩张），几何侧更简单；两边迹相等，就得到 $\operatorname{GL}(2)$ 侧某些表示的消失，即 Jacquet–Langlands。

**〔含糊点拨〕$p=2$ 的 theta 对应**　$p=2$ 时 $D$ 是四元数除代数，局部对应由 theta 对应 $\operatorname{GO}(4)\leftrightarrow\operatorname{GSp}(2)$ 实现，像是平方可积表示；这是定理 55 在 $p=2$ 的具体化（ch08.tex:1950 附近）。

## 相关

[[ch8-selberg-trace]]、[[ch8-langlands-entry]]、[[ch8-discrete-spectrum]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§10，原书 pp. 188–191（PDF pp. 191–194）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch08.tex:1844-2016`
