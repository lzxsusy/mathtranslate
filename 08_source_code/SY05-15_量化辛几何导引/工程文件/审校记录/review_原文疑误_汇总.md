# 原文疑误与审校记录汇总
本文件由各章译者提交的 `review_*.md` 自动汇总，逐条给出原书疑误、记号不一致与处理方式。正文中对应位置均有 `% [Tutor Note: 原文疑误——…]` 批注；译文原则上**保留原文写法**，仅加注说明，不擅改原书内容。


---

## 第 1 章 辛流形

# 审校记录：第 1 章 辛流形（Symplectic Manifold）

范围：原书印刷页 1–21，扫描 PDF p9–p29。
产出：`qsg/tex/ch01-s01.tex` … `ch01-s07.tex`；图 `qsg/figures/fig_p016_1.png`。

处理原则：凡确认的原书笔误，译文**保留原文写法**并加 `% [Tutor Note: ...]` 注释说明，同时在本文件记录。

---

## 一、确认的原文疑误（按页序）

| # | 位置 | 原文 | 疑点 | 建议改法 |
|---|------|------|------|----------|
| 1 | 印刷 p.2（PDF p.10）命题 1.1.1 证明 | “there exists some $(2k-1)$-form $\alpha$ … such that $\omega=\mathrm{d}\alpha$” | 由 $[\omega^k]=0$ 只能推出 $\omega^k=\mathrm{d}\alpha$；$\omega$ 非退化且在闭流形上，绝不可能恰当（否则 $\int_M\omega^n=0$ 与体积形式矛盾）。此外该句逗号后接大写 “Then”，亦为印刷失误。 | $\omega^k=\mathrm{d}\alpha$ |
| 2 | 印刷 p.4（PDF p.12）例 1.2.2 开头 | “Let $Q$ be a differentiable $n$-dimensional manifold $Q$.” | 句末重复符号 $Q$ | 删去第二个 $Q$ |
| 3 | 印刷 p.4（PDF p.12）定理 1.2.2（Weinstein） | “$(U,\omega_{\mathrm{can}}\|_U)$, where $U\subset T^*M$ is a neighborhood of the zero-section in the cotangent bundle $T^*L$” | 同一个 $U$ 既在 $T^*M$ 又在 $T^*L$ 中；$\omega_{\mathrm{can}}$ 只定义在 $T^*L$ 上 | $U\subset T^*L$ |
| 4 | 印刷 p.5（PDF p.13）例 1.2.3 | “Two different symplectic structures on $\Sigma_g$ are simply rescaling of each other.” | 严格地说应在「相差一个辛同胚 + 常数伸缩」的意义下理解（Moser 稳定性）；一般不存在常数 $c$ 使 $\omega_1=c\,\omega_2$ 逐点成立 | 表述加「在辛同胚与常数伸缩的意义下」限定 |
| 5 | 印刷 p.8（PDF p.16）命题 1.3.1 证明（(i) 的计算） | 第 3 行 $g\big(-\big(\sqrt{AA^{\mathrm T}}\big)^{-1}v,\ \big(\sqrt{AA^{\mathrm T}}\big)^{-1}Aw\big)$ | 由 $\omega(x,y)=g(Ax,y)$、$A^2=-\big(\sqrt{AA^{\mathrm T}}\big)^2$ 只能得到 $g\big(-\big(\sqrt{AA^{\mathrm T}}\big)v,\cdot\big)$；按原文写法第 4、5 行不成立（一般 $A^{-1}\neq-A$） | 指数改为 $-\big(\sqrt{AA^{\mathrm T}}\big)v$ |
| 6 | 印刷 p.15（PDF p.23）1.6 节开头的动机段 | “$Y_1=\mathrm{span}\langle x_1\rangle\subset\R^{2n}$ and $\omega_{\mathrm{std}}\|_N=0$”；其后“$\omega_{\mathrm{std}}\|_N=0$” | 通篇未定义 $N$，按上下文应为 $Y_1$、$Y_k$ | $\omega_{\mathrm{std}}\|_{Y_1}=0$、$\omega_{\mathrm{std}}\|_{Y_k}=0$ |
| 7 | 印刷 p.16（PDF p.24）命题 1.6.1 证明 | “if $\omega_p(v,\cdot)=0$ on $T_p^*L$” | 余向量 $\omega_p(v,\cdot)$ 应作用于切空间 | $T_pL$ |
| 8 | 印刷 p.16（PDF p.24）注 1.6.2 | “take $M=\R^{2n}$ and consider the product symplectic structure defined in (1.4), then the anti-diagonal $\overline\Delta_M=\{(x,-x)\}$ is Lagrangian, while $\Delta_M$ is not.” | 在 (1.4) 的和形式 $\pi_1^*\omega+\pi_2^*\omega$ 下，$\{(x,-x)\}$ 的切向量为 $(v,-v)$，代入得 $2\omega(v,w)\neq0$，故它\emph{不}拉格朗日；而在差形式 $\pi_1^*\omega-\pi_2^*\omega$ 下 $\Delta_M$ 与 $\overline\Delta_M$ 都拉格朗日。两种解读都与原文结论不符 | 和形式下应为「复共轭图像 $\{(x,\bar x)\}$ 拉格朗日、$\Delta_M$ 不拉格朗日」；差形式下应删去「而 $\Delta_M$ 不是」 |
| 9 | 印刷 p.18（PDF p.26）命题 1.7.1 证明 | $\mathcal{L}_{X_{H_t}}\omega=\mathrm{d}\iota_{X_{H_t}}\omega+\iota_{X_{H_t}}\mathrm{d}\omega=\mathrm{d}(\mathrm{d}H_t)=0$ | 按 (1.15) 的约定 $\iota_{X_{H_t}}\omega=-\mathrm{d}H_t$，中间项应为 $\mathrm{d}(-\mathrm{d}H_t)$；结论不变 | 补负号 |
| 10 | 印刷 p.20（PDF p.28）$X$ 的哈密顿性验证 | “$\omega_x(X(x),\cdot)=\mathrm{d}H_t(x)(\cdot)+\cdots=\mathrm{d}(H_t+G_t\circ\psi_t^{-1})(x)(\cdot)$” | 按 (1.15)，每一行的 $\mathrm{d}$ 前都应带负号（第一项为 $-\mathrm{d}H_t$，第二项 $\omega(Y,\cdot)=-\mathrm{d}G_t(Y)$），正确末行为 $-\mathrm{d}(H_t+G_t\circ\psi_t^{-1})$；结论（$X$ 由 $H_t+G_t\circ\psi_t^{-1}$ 生成）不变 | 全链补负号 |
| 11 | 印刷 p.20（PDF p.28）注 1.7.2(ii) | “flow $\varphi_{\tilde H}^t$ can be viewed as the **time-reserving** of $\varphi_H^t$” | 应为 time-reversing（时间反演） | time-reversing |
| 12 | 印刷 p.20（PDF p.28）练习 1.7.3 | “for any time-reparametrization $\alpha(t):[0,1]\to[0,1]$ where $\alpha(0)=0$” | 只给 $\alpha(0)=0$ 不足：为使 $\{\varphi_H^{\alpha(t)}\}$ 在 $t=1$ 有意义并使推论成立，还需 $\alpha(1)=1$ 且 $\alpha$ 单调不减 | 补 $\alpha(1)=1$、$\alpha$ 单调 |
| 13 | 印刷 p.11（PDF p.19）(ii) 面积的定义 | “The $\mathrm{Area}(u)$ … is locally defined by (1.10)” | (1.10) 只给出面积元（被积式），并非面积的积分表达式；属表述省略 | 可写成 $\Area(u)=\int\sqrt{\cdots}\,\dd x\dd y$ |
| 14 | 印刷 p.4（PDF p.12）定理 1.2.1 之后 | “the rigorous statement and its proof will be given in **Section 4.3 in Chapter 5**” | 「4.3 节」按本书记号必属第 4 章；原书目录：第 4 章 Moser's Argument 的 4.3 节为 Neighborhood Theorems（印刷 p.92），第 5 章 Floer Theory 的 5.3 节为 Homological Rigidity。故「Chapter 5」为笔误 | 第 4 章 4.3 节（**本译文已按目录证据直接更正**，并在正文加 Tutor Note；此为全章唯一一处改动原文处） |

## 二、术语与记号说明（已写入正文 Tutor Note）

- `//`：原书用以标记例子结束的记号，见 p.1 脚注；译文照排为 `//` 并在首个例子处保留脚注。
- $\mathcal{J}(M,\omega)$、$\Lambda_n$ 分别用花体 $\mathcal{J}$ 与 $\Lambda$，与原文一致；原书排版 $\mathcal{J}$ 与 $J$ 极易混淆，已在 1.3 节注明。
- (1.11) 中的 $\mathbf{1}_{n\times n}$ 按 SPEC 统一用 `\mathbf{1}`（不用 `\mathbb{1}`）。
- (1.13) 的辛球/辛柱约定：$B^{2n}(R)=\{\sum(x_i^2+y_i^2)\le R\}$，即半径为 $\sqrt R$；与常见「半径 $r$」写法差一个平方，已加 Tutor Note。
- 定理 1.3.1 的 Newlander–Nirenberg 上标 167、各处 [n] 均为原书文献编号，译文保留为 `\textsuperscript{}` 与 `[n]`。

## 三、待编辑确认

1. `preamble.tex` 未定义 `wfact`（“事实”环境）。本译文用 preamble 已有的 `\whead{事实}{1.3.1}` 手工排版（与 `ch02-s01.tex` 的做法一致）。若 Lead 认为宜增补环境，建议在 preamble 加
   `\newenvironment{wfact}[1]{\whead{事实}{#1}}{\par\medskip}`；否则无需改动。
2. 全书统一的 `//` 记号：第 2 章译文用了 `\hfill$\square$`，本章按原文用 `//`。若 Lead 要求全章统一，可批量替换。


---

## 第 2 章 辛拓扑中的物理

# 第 2 章审校记录（review_ch02.md）

范围：原书 Chapter 2 *Physics in Symplectic Topology*，印刷页 p.22–p.51，扫描 PDF p.30–p.59。
译者：ch02-physics。下表记录逐页核对中发现的**原文疑误/记号不一致**；凡在译文中保留原文
写法者，均在相应位置加了 `% [Tutor Note: ...]` 批注说明。表中「页」为印刷页码。

| # | 页 / 位置 | 原文（照录） | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | p.24, 例 2.1.1 的 Euler–Lagrange 方程 | `mg = d/dt m v_2(t)(γ(t),γ̇(t)) = m q̈_2(t)` | 由 (2.3) $L=\frac12m\|v\|^2-mgq_2$ 得 $\partial L/\partial q_2=-mg$，故左端应为 $-mg$；否则与「$q_2$ 为抛物函数、轨迹为抛物线（开口向下）」矛盾 | 左端改为 $-mg$ |
| 2 | p.25, 例 2.1.2 | `Γ^k_{ij} = Σ_{i=1}^{2} g^{kl}Γ_{lij}` | 求和指标应为 $l$；原文对 $i$ 求和，与左端自由指标 $k$、被求和式中的 $l$ 均不相容 | 改为 `Σ_{l=1}^{2} g^{kl}Γ_{lij}` |
| 3 | p.28, 命题 2.2.1 的证明开头 | `L = L(q,v) : T*R² → R` | 与定义 2.1.1、事实 2.1.1 冲突：$L$ 定义在切丛 $T R^2$ 上；落在 $T^*R^2$ 上的是其 Legendre 变换 $\mathcal{L}(L)$ | 定义域改为 $T R^2$ |
| 4 | p.32, 例 2.3.2 的反正向 | `ω_p(X_G(p),v) = −ω_p(v,X_G(p)) = dG_p(v) ≠ 0` | 由定义 1.7.1（$\dd G=-\iota_{X_G}\omega$）得 $\omega_p(X_G(p),v)=-\dd G_p(v)$，末项差一负号（不影响「$\ne0$」的结论） | 末项改为 $-\dd G_p(v)$ |
| 5 | p.39, 式 (2.29) | `... , ½\|z_n\|²) ∈ R^n_{≥0},` 之后语句多一个 `)` | 排版笔误：`⟨μ(z_1,…),v⟩ = H_v(r_1,…,r_n,θ_n))` 多一个右括号 | 删去多余 `)` |
| 6 | p.41, 定理 2.5.1 (i)(iii) | `a finite union of pairwise disjoint connected of submanifolds`；`denoted by im(u)` | (i) 多一个 `of`，应为 `connected submanifolds`；(iii) 中 `im(u)` 应为 `im(μ)` | 分别改为 `connected submanifolds`、`im(μ)` |
| 7 | p.47, §2.8 开头 | `one family of directions is given by the moment image im(u)` | `im(u)` 应为 `im(μ)`（同类错误在 p.47 出现两次） | 改为 `im(μ)` |
| 8 | p.50, 定理 2.8.1 (i) | `then L := F^{-1}(p) it is a Lagrangian torus` | 多余的 `it` | 删去 `it` |
| 9 | p.43, 例 2.6.1 中 $\{H,H_2\}$ | `Σ_{i=1}^{2}( ∂H/∂p_i ∂H_2/∂q_i − ∂H/∂q_i ∂H_2/∂p_i )` | (a) 空间 Kepler 问题应为 $\sum_{i=1}^3$（$i=3$ 项自动为零，故结果不变）；(b) 按 (2.8)、(2.5) 的约定 $\{F,G\}=\sum_i(\partial_{q_i}F\partial_{p_i}G-\partial_{p_i}F\partial_{q_i}G)$，上式的被求和式整体与之反号（结果仍为 0，不影响结论） | 上限改 3；被求和式按 (2.8) 重排 |
| 10 | p.43, 例 2.6.1 | `{A_1,A_2} = −A_3, {A_2,A_3} = −A_1, {A_1,A_3} = A_2` | 按 (2.8) 的标准括号，角动量满足 $\{A_1,A_2\}=A_3,\{A_2,A_3\}=A_1,\{A_1,A_3\}=-A_2$；原文三式整体反号，等价于采用了与 (2.8) 相反的括号约定。本段只需 $\{A_i,A_j\}\ne0$，结论不受影响 | 统一括号约定后取标准式，或明确声明相反约定 |
| 11 | p.33, 练习 2.3.2 | `limsup_{F',G' \xrightarrow{C^0} F,G} \|\{F_k,G_k\}\|_{C^0} > \|\{F,G\}\|_{C^0}` | 记号矛盾：正文给的是函数列 $F_k\to F$、$G_k\to G$，$\limsup$ 应取 $k\to\infty$（或 $\limsup_{F'\to F,G'\to G}\|\{F',G'\}\|$），而括号内却写 $F_k,G_k$ | 或改为 $\limsup_{k\to\infty}$，或把括号内改为 $F',G'$ |
| 12 | p.36, 例 2.4.4 | `X_A(q,p)=(Aq,Ap)` 是「由 $H_A(q,p)=q^{\mathrm T}Ap$ 生成的哈密顿向量场」 | 按 (2.4)（$\dd H=-\iota_{X_H}\omega_{\mathrm{can}}$）与 (2.5)，$X_{H_A}=(-Aq,-Ap)=-X_A$；即 $X_A$ 实际由 $-H_A$ 生成。原文与 (2.25)、(2.26) 的 $\mu=q\times p$ 只在与 (2.4) 相反的符号约定下自洽（(2.9) 的符号亦随之翻转） | 取 $H_A=-q^{\mathrm T}Ap$（此时 $\mu=-q\times p$），或整体声明相反的符号约定；建议以「$\mu=q\times p$ 是物理角动量」为准记忆结论 |
| 13 | p.45, §2.7 第 2 段 | `derived from such a symmetry, one derived a conservative` | 词语重复、语法不顺（非数学错误） | 改为 `one obtains a conservative` |
| 14 | p.47, §2.8 第 2 段 | `The discussion so far in fact rephrase the polar coordinates` | 主谓不一致（非数学错误） | 改为 `rephrases` |

## 说明

- 第 1–13 项中，凡涉及符号/公式者，译文**一律保留原文写法**并在对应位置以
  `% [Tutor Note: ...]` 指出正确形式与核对要点；第 13–14 项为文字问题，译文按语义通顺处理。
- 第 9、10、12 项相互关联：原文在 §2.6–§2.8 的若干计算中使用的是「与 (2.8) 相反的」
  括号/哈密顿向量场符号约定。凡遇「括号为零」的结论，符号不影响正确性；但读者若逐项
  重算会得到整体反号，核对时须固定一个约定并全章一致。
- 另有若干纯排版/语法小疵（如 p.51「Denote by e is the unit vector」多 `is`、p.52
  「the angular momentum A is equal to q×p」句法不顺），不影响数学内容，译文已按语义通顺
  处理，未逐条列出。


---

## 第 3 章 切触几何

# 审校记录：第 3 章 切触几何（Contact Geometry）

范围：原书印刷页 52–85，扫描 PDF 第 60–93 页。译文文件：
`qsg/tex/ch03-s01.tex` … `ch03-s07.tex`。

以下「原文疑误」在译文中**一律保留原文写法**并加 `% [Tutor Note: 原文疑误——…]`
批注；唯一例外是第 1 条（$\R^n\to\R^{2n+1}$）——它是纯记号笔误、不涉及任何公式内容，
译文直接按 $\R^{2n+1}$ 排印并加注说明。请教授复核。

---

## 一、已确认的疑误（硬错误，正文已加批注）

| # | 位置（印刷页 / PDF 页） | 原文 | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | 注 3.2.1，p.56 / p.64 | "there are other contact forms on $\R^n$" | 所列 $\alpha'$、$\alpha''$ 含 $x_i,y_i,z$ 共 $2n+1$ 个坐标，显系 $\R^{2n+1}$ 之误 | 改为 $\R^{2n+1}$（译文中已按 $\R^{2n+1}$ 处理并加注） |
| 2 | 图 3.3 及例 3.2.2，p.57 / p.65 | 图注标注 $\xi_{(x,\theta,z)}$ | 本例取柱坐标 $(r,\theta,z)$，下标首字母应为 $r$ | 改为 $\xi_{(r,\theta,z)}$（原图不改，译文加注） |
| 3 | 例 3.2.3，p.59 / p.67 | $\gamma_a=\{(z_1,0)\in\partial E(a,b)\mid |z_1|=a\}$；$\gamma_b$ 同 | 按 (3.7) 的 $E(a,b)$ 定义（$\lvert z_1\rvert^2/a+\lvert z_2\rvert^2/b\le1$），在 $\partial E$ 上取 $z_2=0$ 得 $\lvert z_1\rvert^2=a$，故应为 $\lvert z_1\rvert=\sqrt a$；周期 $\pi a,\pi b$ 与 (3.9) 一致，说明只是半径处笔误 | 改为 $\lvert z_1\rvert=\sqrt a$、$\lvert z_2\rvert=\sqrt b$ |
| 4 | 辛化段落，p.61 / p.69 | "the symplectization assembles $\R$-many contact manifolds $(M,\omega)$" | $M$ 是切触流形，其上并无辛形式 $\omega$ | 改为 $(M,\xi)$ |
| 5 | p.62 / p.70 公式 | $(\dd r\wedge\alpha+\dd\alpha)((v\partial/\partial r,R_\alpha,w),\eta)=v+\dd\alpha(v,\eta)$ | $v$ 是 $\partial_r$ 方向的标量，$\dd\alpha(v,\eta)$ 无意义；按上下文应为 $\dd\alpha(w,\eta)$，且 $\eta=R_\alpha$ 时该项为 $0$ | 改为 $\dd\alpha(w,\eta)$ |
| 6 | 式 (3.19)，p.64 / p.72 | $J(u(s,t))\frac{\partial u_\R}{\partial t}=\alpha(\frac{\partial u_M}{\partial s})$，随后写「即 $\frac{\partial u_\R}{\partial t}=-\alpha(\frac{\partial u_M}{\partial s})$」 | 两式符号不相容：由 $J(\partial_r)=R_\alpha$ 知左端对 $\alpha$ 求值即 $\frac{\partial u_\R}{\partial t}$，故第一式应为负号（或应写右端为 $-\alpha(\cdot)R_\alpha$） | 建议把中间式写成 $J(u)\frac{\partial u_\R}{\partial t}+\alpha(\frac{\partial u_M}{\partial s})R_\alpha=0$ |
| 7 | 式 (3.25)，p.69 / p.77 | $\varphi(t)\to\pm\infty\ (t\to\pm\infty)$ | 同一定义正文规定 $\varphi:\R\to(-1,1)$，且例中 $\varphi=\frac2\pi\arctan x$，极限为 $\pm1$ | 改为 $\varphi(t)\to\pm1$ |
| 8 | 定理 3.3.1，p.69 / p.77 | $u:(\dot\Sigma\setminus\Gamma,j)\to(SM,\dd(\ee^r\alpha),J)$ | 按本节记号 $\dot\Sigma=\Sigma\setminus\Gamma$ 已含刺点集，再减 $\Gamma$ 重复 | 改为 $(\dot\Sigma,j)$ |
| 9 | 例 3.4.3，p.73 / p.81 | "This corresponds to item (iii) in Remark 3.4.4" | 注 3.4.4 中第 (iii) 项是「$z'\ne0$ 而 $x'=0$，不可能」；描述前沿投影曲线终止的是第 (ii) 项（$z'=x'=0$） | 改为 item (ii) |
| 10 | p.77 / p.85 | "reveals a Hamiltonian feature of $\Op{Cont}_0(M,\omega)$" | 切触流形应记 $(M,\xi)$ | 改为 $\Op{Cont}_0(M,\xi)$ |
| 11 | 定义 3.7.1，p.83 / p.91 | "For a contact manifold $(M,\omega)$" | 同上 | 改为 $(M,\xi)$ |

## 二、存疑（需人工确认）

| # | 位置 | 原文 | 疑点 | 建议 |
|---|---|---|---|---|
| 13 | 定理 3.5.1，p.76 / p.84 | "for any closed contact manifold $(M,\xi)$, the contactomorphism group $\Op{Cont}(M,\xi)$ is a simple group" | 对闭流形被证明为单群的通常是恒等分支 $\Op{Cont}_0(M,\xi)$（Banyaga–Rybicki 型定理）。若字面指整个 $\Op{Cont}$，则当 $\Op{Cont}$ 不连通时，真子群 $\Op{Cont}_0$ 将在单群中成为非平凡正规子群，产生矛盾。原文紧接的一段也正是拿 $\Op{Cont}_0$ 与 $\Op{Ham}$ 作比较 | 建议按 $\Op{Cont}_0(M,\xi)$ 理解，或补充「当 $\Op{Cont}=\Op{Cont}_0$ 时」的连通性假设；译文中保留原文表述并加批注 |
| 14 | 命题 3.7.1 与例 3.7.2，p.84 / p.92 | 例 3.7.2 说「群 $\widetilde{\Op{Cont}_0}(M,\xi)$ 中存在正可缩环路」；命题说「$\Op{Cont}_0(M,\xi)$ 中不存在任何正的可缩环路」 | 两处所指的群不一致（万有覆叠 vs 底群）；实际上「正的可缩环路」应理解为 $\Op{Cont}_0$ 中的环路（作为 $\widetilde{\Op{Cont}_0}$ 中的类） | 统一表述为「$\Op{Cont}_0(M,\xi)$ 中的正的可缩环路」 |

## 三、非错误但易混的记号（译文加「记号提示」批注，未计入疑误）

| # | 位置 | 说明 |
|---|---|---|
| A | 例 3.2.1，p.55 / p.63 | $\alpha_{\mathrm{std}}\wedge(\dd\alpha_{\mathrm{std}})^n=\dd z\wedge\dd x_1\wedge\dd y_1\wedge\cdots$ 与直接计算相差常数因子 $n!$（$n=1$ 时恰为等式）；原文只关心非零性，故不算错，但逐符号核对时勿当恒等式 |
| B | §3.3，p.66–p.68 | 目标空间写作 $(M,\omega,J)$（沿用 §1.4 的一般辛流形记号），与本章作为切触流形的 $M$ 同名异义 |
| C | §3.2 注 3.2.3 段落，p.61 / p.69 | 「Liouville 流形」与「Liouville 域」交替出现，前者非紧、后者带边界，阅读时须区分 |
| D | 例 3.7.4，p.85 / p.93 | $(S^*_gM,\xi=\lambda_{\mathrm{can}}\rvert_{S^*_gM})$ 把切触结构 $\xi$ 直接写成切触形式；按 §3.2 (3.12) 的记号应理解为 $\xi=\ker(\lambda_{\mathrm{can}}\rvert_{S^*_gM})$ 或直接写 $(S^*_gM,\lambda_{\mathrm{can}})$ |

## 四、无法辨认的符号

无。全部 34 页均已逐页核对；公式 (3.1)–(3.45) 编号与原文一致（共 45 个编号公式）。

## 五、译文图片清单（16 幅，均按 300 dpi 从扫描页裁剪）

| 图号 | 文件 | 印刷页 / PDF 页 |
|---|---|---|
| 图 3.1 | `figures/fig_p063_1.png` | p.55 / p.63 |
| 图 3.2 | `figures/fig_p064_1.png` | p.56 / p.64 |
| 图 3.3 | `figures/fig_p065_1.png` | p.57 / p.65 |
| 图 3.4 | `figures/fig_p070_1.png` | p.62 / p.70 |
| 图 3.5 | `figures/fig_p073_1.png` | p.65 / p.73 |
| 图 3.6 | `figures/fig_p074_1.png` | p.66 / p.74 |
| 图 3.7 | `figures/fig_p074_2.png` | p.66 / p.74 |
| 图 3.8 | `figures/fig_p075_1.png` | p.67 / p.75 |
| 图 3.9 | `figures/fig_p076_1.png` | p.68 / p.76 |
| 图 3.10 | `figures/fig_p077_1.png` | p.69 / p.77 |
| 图 3.11 | `figures/fig_p080_1.png` | p.72 / p.80 |
| 图 3.12 | `figures/fig_p081_1.png` | p.73 / p.81 |
| 图 3.13 | `figures/fig_p082_1.png` | p.74 / p.82 |
| 图 3.14 | `figures/fig_p084_1.png` | p.76 / p.84 |
| 图 3.15 | `figures/fig_p091_1.png` | p.83 / p.91 |
| 图 3.16 | `figures/fig_p092_1.png` | p.84 / p.92 |


---

## 第 4 章 Moser 论证

# 第 4 章 审校记录（review_ch04.md）

范围：原书第 4 章 *Moser's Argument*，印刷页 86–100，扫描 PDF 第 94–108 页。
处理原则：译文**保留原文写法**并就地加 `% [Tutor Note: ...]` 说明；下表给出原文、页码、
疑点与建议改法，供教授定夺。标记「确信」者为可完全确定之笔误，「待核」者需对照作者原稿
或后续版本确认。

| # | 位置（印刷页 / PDF 页） | 原文 | 疑点 | 建议改法 | 把握 |
|---|---|---|---|---|---|
| 1 | p.87 / p.95，4.1 切触段落 | $(\psi_0)_*\xi_0=\xi_t$ | $\psi_0=\mathrm{id}$，左端恒为 $\xi_0$，除非 $\xi_t$ 恒等于 $\xi_0$，否则该式对一般 $t$ 不成立 | 改为 $(\psi_t)_*\xi_0=\xi_t$（与同页下文定理 4.1.2 的表述一致） | 确信 |
| 2 | p.88 / p.96，例 4.1.1 末段 | "contactomprhic" | 拼写错误 | "contactomorphic" | 确信 |
| 3 | p.89 / p.97，例 4.2.1 | "there exists $\beta\in H^1(M;\R)$ such that $\omega_1=\omega_0+\dd\beta$" | $H^1(M;\R)$ 的元素是上同调类，不能对其取外微分 $\dd\beta$ | 改为「存在 $1$-形式 $\beta\in\Omega^1(M)$ 使得 $\omega_1=\omega_0+\dd\beta$」 | 确信 |
| 4 | p.97 / p.105，定理 4.3.3 | $\varphi^*(\omega|_V)=\omega_{\mathrm{can}}|_V$ | $\varphi\colon U\to V$ 的定义域为 $U\subset T^*L$，而 $\omega_{\mathrm{can}}$ 是 $T^*L$ 上的形式；左端已是 $U$ 上的形式 | 右端改为 $\omega_{\mathrm{can}}|_U$ | 确信 |
| 5 | p.100 / p.108，引理 4.3.1 证明末式 | $=\dd\bigl(\int_0^1\varphi_t^*(\iota_{X_t}(\omega_1-\omega_0))\bigr)\,\dd t$ | $\dd t$ 被排在右括号之外。按定义 $\omega_1-\omega_0=\int_0^1\frac{\dd}{\dd t}\varphi_t^*(\omega_1-\omega_0)\dd t=\int_0^1\varphi_t^*\dd\iota_{X_t}(\omega_1-\omega_0)\dd t=\dd\bigl(\int_0^1\varphi_t^*\iota_{X_t}(\omega_1-\omega_0)\dd t\bigr)$，故 $\dd t$ 应在积分号内、右括号内 | 改为 $\dd\bigl(\int_0^1\varphi_t^*(\iota_{X_t}(\omega_1-\omega_0))\,\dd t\bigr)$ | 确信 |
| 6 | p.100 / p.108，引理 4.3.1 证明 | "$\varphi_t(\exp(q,v)):=\exp(q,tv)$，for any $(q,v)\in V$" | $\exp$ 只定义在 $U\subset NQ$ 上，且公式要求 $(q,tv)\in U$；$(q,v)\in V$ 中的 $V=\exp(U)$ 不是合适的作用域 | 改为 "for any $(q,v)\in U$" | 待核（可能只是记号混用） |
| 7 | p.100 / p.108，引理 4.3.1 证明末句 | "run Moser's argument for $\omega_t=\omega_0+t\,\dd\sigma$, where $t\sigma$ are the required 1-forms" | 若 $\omega_t=\omega_0+t\,\dd\sigma$，则按 (4.1) 所需的族是固定的 $\sigma_t\equiv\sigma$，而非 $t\sigma$；作者的用意应是「$\omega_t-\omega_0=\dd(t\sigma)$」 | 改为 $\sigma_t\equiv\sigma$；或改写为 $\omega_t=\omega_0+\dd(t\sigma)$ 并说明所需族为 $t\sigma$（两种写法需统一） | 待核 |
| 8 | p.87 / p.95，注 4.1.1 | "deformation of volume forms $\{\sigma_t\}$ ... where $\sigma_t$ is both non-degenerate and closed" | (i) 以 $\sigma_t$ 记体积形式族，与 (4.1) 的 $1$-形式 $\sigma_t$ 记号冲突；(ii)「非退化且闭」是辛形式的刻画，一般体积形式不必闭。结合定理 4.2.1 的准确表述，原意应是「把辛形式换成体积形式、把沿 $t$ 导数写成恰当形式，论证照样成立」 | 体积形式族改用 $\{\tau_t\}$；并核对「闭」这一条件是否必要 | 待核 |
| 9 | p.93 / p.101，定理 4.3.1 证明 | "$\varphi|_0=\mathbf 1$" | 作为集合 $\{0\}$ 上的「限制」记号略显含混，原意应为 $\varphi(0)=0$（在 $Q=\{0\}$ 上为恒等） | 可改写为 $\varphi(0)=0$，或统一使用 $\varphi|_Q=\mathbf 1$（$Q=\{0\}$） | 待核（记号问题） |
| 10 | p.100 / p.108 | "let us give the prove of Lemma 4.3.1" | 语法笔误（prove → proof） | 改为 "give the proof" | 确信（仅英文，不影响译文） |

## 已核对但判为无误的易混点

- p.91 / p.99，(4.12)：$\bigl[\frac{\dd}{\dd t}\omega_t\bigr]=\frac{\dd}{\dd t}[\omega_t]$ 的
  第一个等号确实来自「对任意 $2$-闭链 $C$ 可交换 $\frac{\dd}{\dd t}$ 与 $\int_C$」，不是笔误。
- p.91 / p.99，"（正确进路 I）" 中 $\Delta\tau_t=\dd(\delta\tau_t)\iff\delta(\dd\tau_t)=0$
  的等价性成立（因 $\Delta\tau_t=\dd\delta\tau_t+\delta\dd\tau_t$ 且 $\Delta\tau_t=\frac{\dd}{\dd t}\omega_t$）。
- p.96 / p.106，$\omega(Jv,Jw)=\omega(v,w)=0$ 与 $g_J(v,Jw)=\omega(v,-w)=-\omega(v,w)=0$
  均正确（用 $J^2=-\mathbf 1$ 与 $J$ 的 $\omega$-相容性）。
- p.97 / p.107，定理 4.3.3 证明中 $(\psi^*\omega)_{(q,0)}=-y_2^*(x_1)+y_1^*(x_2)$ 与
  $\omega_{\mathrm{can}}=y_1^*(x_2)-y_2^*(x_1)$ 一致，符号无误。
- p.96 / p.104，例 4.3.1 的流计算：$u=x/(1+t)$、$v=y$、$w=z-xyt/(1+t)$，时间 1 映射
  给出 $(x/2,y,z-xy/2)$，与 (4.20) 一致。

## 图目录（统一从扫描页 300 dpi 裁剪，置于 qsg/figures/）

| 文件 | 原书位置 | 说明 |
|---|---|---|
| `fig_p100_1.png` | p.92 | 引理 4.3.1 的交换图（无编号示意图） |
| `fig_p101_1.png` | p.93 | Figure 4.1 Darboux 定理 |
| `fig_p101_2.png` | p.93 | Figure 4.2 $V$ 上的辛结构 |
| `fig_p102_1.png` | p.94 | Figure 4.3 切触几何中的 Darboux 定理 |
| `fig_p105_1.png` | p.97 | Figure 4.4 管状邻域定理 |
| `fig_p106_1.png` | p.98 | Figure 4.5 $JTL$ 与 $TL$ 关于 $g_J$ 正交 |
| `fig_p108_1.png` | p.100 | Figure 4.6 乘积流形中 $f$ 的图像 |


---

## 第 5 章（上）Floer 理论 5.1–5.2

# 第 5 章前半（5.1 Morse 理论、5.2 持续模）原文疑误与待核清单

- 覆盖范围：印刷页 p.101–p.119，扫描 PDF p.109–p.127（5.2 节末尾两段文字位于 PDF p.128 顶部，按分工由本译者写入 `ch05a-s02.tex`）。
- 译文文件：`qsg/tex/ch05a-s01.tex`、`qsg/tex/ch05a-s02.tex`。
- 说明：下列「原文疑误」均在译文中保留原文写法，并加 `% [Tutor Note: ...]` 注释；「待核」项仅作提示，未改动原文语义。

| # | 位置（印刷页/PDF 页） | 原文 | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.101 / PDF 109 | 「denote by $\mathrm{Crit}(F)$ the critical points of $F$ on $X$ (i.e., $\mathrm{d}F(p)=0$ for any $p\in\mathrm{Crit}(X)$)」 | 括注中写成 $p\in\mathrm{Crit}(X)$，临界点集是函数 $F$ 的属性，应与 $X$ 无关 | 改为 $p\in\mathrm{Crit}(F)$ |
| 2 | p.106 / PDF 114 | 「Given the initial condition $t(-\infty)=p_2$ and $t(+\infty)=p_0$」 | $t$ 是定义域参数，流的端点应写成 $u(\pm\infty)$ | 改为 $u(-\infty)=p_2$、$u(+\infty)=p_0$ |
| 3 | p.106 / PDF 114 | 「$u(t)=(u_1(t),3\pi/2)$, where $u_1$ is solved from the second equation above」 | $u_1$ 只出现在第一个方程 $\dot u_1=-\cos u_1$ 中，应说「第一个方程」 | 改为 the first equation above |
| 4 | p.118 / PDF 126 | 例 5.2.4：「the persistence $\mathbf k$-module $\mathbb V_F$ in Example 5.1.10」 | $\mathbb V_F$ 是在例 5.2.2 中定义的；例 5.1.10 只定义了 Morse 同调群，尚未引入持久模 | 改为 Example 5.2.2 |
| 5 | p.118 / PDF 126 | 「enabling homological invisible generators to be investigated」 | 应为副词 homologically（同调不可见地） | 改为 homologically invisible generators |
| 6 | p.113 / PDF 121 | 定理 5.1.2：「$\mathrm{HM}_*\cong\mathrm{HM}_*$ for any field $\Z_2$」 | $\Z_2$ 已固定，「for any field」与 $\Z_2$ 冲突；结合注 5.1.4，本意应是「对任意系数域 $\mathbf k$」 | 改为 for any coefficient field $\mathbf k$（或删去 for any field） |
| 7 | p.115 / PDF 123 | 「introduced by G. Carlsson and A. Zamorodian [248]」，随后同一段又写 A. Zomorodian | 同一作者（Zomorodian）两种拼写 | 统一为 Zomorodian |
| 8 | p.101 / PDF 109 | 定义 5.1.1：「local coordinates $(x_i)_{i=1,\cdots,\dim M}$」 | 上下文流形记作 $X$、维数记作 $n$，唯此处用 $M$ | 记号不统一，建议改 $\dim X$ 或 $n$；译文照原文保留 |
| 9 | p.107 / PDF 115（待核，非定论） | 命题 5.1.1 后结论 (i)：「若 $\operatorname{ind}(x)-\operatorname{ind}(y)\geqslant1$，则 $\widetilde{\mathcal M}$ 与 $\mathcal M$ 非空」 | 维数公式只约束模空间维数，不能推出非空性；可证明的是一般方向 (iii)（非空 ⇒ 指标严格下降，见 Tutor Note 中的 $\R$-轨道论证）。(i) 是否另有作者未写出的论证，未能确认 | 保留原文，加 Tutor Note 提示读者注意 (i) 与 (iii) 的逻辑地位不同；请教授裁定是否需要加脚注 |
| 10 | p.116 / PDF 126（体例说明，非疑误） | 「Definition 5.1.2 [41,68,142]」等标题后紧跟文献编号 | 原书体例，译文照排（编号置于标题后） | 无需改动 |

## 体例与宏说明

1. **Fact 环境**：preamble 未提供 `wfact` 环境（且 preamble 禁改）。译文对「事实 5.1.1 / 5.1.2」采用与 `\whead` 等价的手工排版（`\textbf{事实 5.1.1}\quad`），编号照原文。若教授希望全书统一，可在 preamble 增加 `wfact` 后由 lead 统一替换。
2. **`\codim`**：preamble 未定义 `\codim`，译文中改用 `\operatorname{codim}`（不影响排版）。
3. **例/注末尾的 `//`**：原书用 `//` 标记例、注的结束，译文用 `\hfill$//$` 保留。
4. **图注**：12 幅插图均从扫描页按 300 dpi 裁剪（`qsg/figures/fig_pNNN_k.png`），图注为中文并标注原书图号、印刷页与 PDF 页。

## 自检结果

- `python qsg/tools/check.py ch05a`：覆盖 PDF p109–p127 共 19/19 页（另在 `ch05a-s02.tex` 末尾含 p128 顶部 5.2 收尾两段，故报「越界页标记 [128]」，属分工接缝，非缺页）；节 2、keytakeaways 2、Tutor Note 39、图 12、公式编号 14（(5.1)–(5.14)）；无 LaTeX 结构错误、无缺失图片、无重复 tag、无禁用命令。
- 另用临时文档（`preamble` + 本两文件，封面独立）以 XeLaTeX 试编译通过（17 页），无 Overfull/Underfull 警告、无 undefined control sequence。


---

## 第 5 章（下）Floer 理论 5.3–5.5

# 审校记录：第 5 章下（5.3–5.5，原书 p.120–p.140 / PDF p.128–p.148）

译者：ch05b-floer。对应源码：`qsg/tex/ch05b-s01.tex`（5.3）、`ch05b-s02.tex`（5.4）、
`ch05b-s03.tex`（5.5）。

体例：**原文照译、不改动**，疑点一律在译文中以 `% [Tutor Note: 原文疑误——…]` 标注；
下表汇总，供教授定夺。页码为**印刷页码**（括号内为 PDF 页码）。

---

## 一、实质性疑误（建议再版时修正）

| # | 位置 | 原文 | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | p.120（PDF p.128）例 5.3.1 | `H : [0,1] × S^1 → ℝ` | 本例题的底流形是 $S^2$（标准 2-球面），定义域不应是 $S^1$；上下文（球面上沿 $z$ 轴的旋转、$S^2$ 的 Betti 数 2）都指向 $S^2$ | 改为 `H : [0,1] × S^2 → ℝ` |
| 2 | p.120（PDF p.128）开头 | `#Crit(F) ⩾ Σ_i b_i(X; k)` | $X$ 全文未定义，此处应为底流形 $M$（同页猜想 5.3.1 用的是 $M$） | 改为 `b_i(M; k)` |
| 3 | p.132（PDF p.140）定理 5.4.1 末句 | `HF_*(M,ω,H,J) ≅ H_*(M;k), the classical homology groups of X` | $X$ 未定义，应为 $M$ | 改为 `of M` |
| 4 | p.133（PDF p.141）§5.5 第 2 段 | `... and co-vector p in the fiber over x` | 讨论的是秩 $n$ 的 $\mathbf{k}$-向量丛 $E\to M$，纤维为 $\mathbf{k}^n$，$p$ 是纤维中的**向量**而非余向量 | 改为 `vector p` |
| 5 | p.128（PDF p.136）命题 5.4.1 证明 | “第一项等于”后的链式等式 | 求导式第一项带负号 $-\int_{\mathbb{D}^2}\frac{d}{ds}(\cdots)^*\omega$，而“第一项等于”一行把外层负号丢掉了；链式等式其余各项与最终结论 (5.18) 均正确 | 在“第一项等于”一行前补负号：$-\int_{\mathbb{D}^2}\frac{d}{ds}(\tilde w(s,\cdot))^*\omega\big|_{s=0}=\cdots=-\int_0^1\omega(\xi,\dot x)\,dt$（或不改，但需读者自行补号） |
| 6 | p.136（PDF p.144）$S(t)^{\mathrm T}=S(t)$ 的链式等式 | 中间两行 $(A^{-1})^{\mathrm T}(\Omega A^{-1})'$、$(A^{-1})^{\mathrm T}\Omega\dot A^{-1}$、$\Omega A\dot A^{-1}$ | 按原样逐符号验算，中间两步难以成立（疑为排版/跳步）。结论 $S(t)^{\mathrm T}=S(t)$ 正确 | 建议改用一行式：对 $A^{\mathrm T}\Omega A=\Omega$ 求导得 $\dot A^{\mathrm T}\Omega A+A^{\mathrm T}\Omega\dot A=0$，故 $S^{\mathrm T}=-(A^{-1})^{\mathrm T}A^{\mathrm T}\Omega\dot AA^{-1}=S$ |
| 7 | p.139（PDF p.147）注 5.5.4 | 置于练习 5.5.1 **之前**，却使用参数 $\alpha$ | 该注的 $\alpha$ 是紧接着的练习 5.5.1 中 $H=\pi\alpha(x^2+y^2)$ 的参数；注在前、练习在后，阅读顺序倒置 | 建议把注 5.5.4 移到练习 5.5.1 之后（或改写为“见下题”） |

## 二、文字/拼写小误（不影响数学内容）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 8 | p.120（PDF p.128）猜想 5.3.1 显示式 | `#{fix points of the time-1 map φ_H^1}` | `fix` 应为 `fixed`（漏字）。译文按“不动点”处理 |
| 9 | p.120（PDF p.128） | `the full version this theory is built up in ...` | 漏 `of`：应为 `the full version of this theory` |
| 10 | p.125（PDF p.133）猜想 5.3.7 前 | `Hofer-Wyoscki-Zehnder` | `Wyoscki` 应为 `Wysocki`（P. Wysocki） |
| 11 | p.138（PDF p.146）例 5.5.7 | `It is a Morse function with the only critical point of H is 0` | 语法重复（`with the only critical point ... is 0`）；译文按“唯一临界点是 0”处理 |
| 12 | p.127（PDF p.135）命题 5.4.1 陈述 | `Crit(A_H) = {contractible closed Hamiltonian orbits of {φ_H^t}}` | 严格说 $\mathrm{Crit}(\mathcal{A}_H)\subset\Lambda_0M$ 是**环路**的集合，不是“轨道”的集合；二者在闭轨道意义下可对应，但 $\mathcal{A}_H$ 原本定义在 $(x,w)$ 上。译文照原文，已在 (5.17) 后与命题处加注说明良定义性 |
| 13 | p.132（PDF p.140）(5.22)/(5.23) | (5.22) 用系数域 $\mathbf{k}$，(5.23) 用 $\#_{\mathbb{Z}_2}$ | 两处系数约定不统一（(5.23) 的模 2 计数对应 $\mathbb{Z}_2$ 系数；一般 $\mathbf{k}$/$\mathbb{Z}$ 系数需相干定向）。已在译文批注中指出 |
| 14 | p.126（PDF p.134） | `for any smooth function f : S^2 → M` | $f^*\omega$ 需要的是映射；原文用 `function`，译文按“光滑映射”处理（不视为错误） |

## 三、记号/约定提醒（非疑误，已写入 Tutor Note）

1. **符号约定**：本书取 $\iota_{X_F}\omega=-\dd F$（即 $\omega(X_F,\cdot)=-\dd F$），与不少教材的
   $\iota_{X_H}\omega=\dd H$ 差一符号；(5.17)–(5.21) 的符号均与此配套。核对时以 (5.18)、(5.20)、
   (5.21) 三式为锚点整体核对。
2. **辛非球面条件**：$c_1(\pi_2(M))=0$ 是简写，准确含义是 $c_1$ 在 Hurewicz 像
   $\operatorname{im}(h_2\colon\pi_2(M)\to H_2(M;\mathbb{Z}))$ 上为零。
3. **Conley–Zehnder 与 Robin–Salamon**：$\mu_{\mathrm{CZ}}$ 依赖哈密顿函数（经由 $(\varphi_H^t)_*$），
   沿轨道作定常扰动时只平移一个常数；$\mu_{\mathrm{CZ}}$ 一般不等于 Morse 指标（例 5.5.7：3 对 0）。
4. **谱不变量**：本节只用 Floer 同调的秩，未涉及作用量过滤；谱不变量（Viterbo–Oh）与持续模/条形码
   是保留过滤信息后的定量化对象，不可与 $\mu_{\mathrm{CZ}}$ 混淆（已在定理 5.4.1 后批注）。
5. **Robin–Salamon 指标与 $c_1$ 的系数 2**：更换界定圆盘时
   $\mu_{\mathrm{CZ}}((x,w))-\mu_{\mathrm{CZ}}((x,w'))=2c_1(\overline{w}\#w')$，系数 2 源于
   Maslov 类与第一 Chern 类的换算；不同文献对 $\mu_{\mathrm{CZ}}$ 的规范化不同，引用时须核对。

---

## 四、译名与体例处理

- 5.5 节 "crossing" 译「交点」，"regular crossing" 译「正则交点」，"prime" 译「素的」。
- "Fact 5.5.1" 沿用全书体例写作 `\whead{事实}{5.5.1}`（preamble 无 Fact 环境）。
- 原文例末的 `//` 记号按全书体例排为 `\hfill$\square$`。
- p.120 页首（5.2 节末尾两段）由 ch05a 译者负责（已协调），本文件不重复。
- **待统一的术语**：GLOSSARY 规定 Morse theory 作「莫尔斯理论」，但 ch05a 与本章下半一致使用
  「Morse」（如「Morse 函数」「Morse 同调」「无穷维 Morse 理论」），而 ch06 一律用「莫尔斯」。
  本译者与 ch05a 保持章内一致，取「Morse」；全书统一时建议由 lead 决定后全局替换。

## 五、自检结果

```
python qsg/tools/check.py ch05b
  === ch05b  PDF p128-p148  文件 3 个 ===
  覆盖 21/21 页 | 节 3 | 要点 3 | 批注 35 | 图 11 | 公式编号 14
  结论：无问题
```

另用 TeX Live 2026 对三节做过独立试编译（`qsg/build/test_ch05b.tex`，17 页）：
无 `!` 错误、无缺字（Missing character）、无 >30pt 的 overfull hbox。


---

## 第 6 章 定量刻画

# 第 6 章「定量刻画」疑误记录（review_ch06.md）

记录范围：PDF p.149–p.179（印刷页 141–171）。每条给出原文、所在页（印刷页 / PDF 页）、
疑点与建议改法。均已在正文对应位置以 `% [Tutor Note: 原文疑误 ...]` 标注，译文保留
原文写法，未擅自改动。

| # | 印刷页 / PDF 页 | 原文（摘录） | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.144 / PDF p.152 | "to control the Hofer norm of the **communicator** $[\cdot,\cdot]$" | 数学上应为「换位子」commutator；communicator 无此义。 | 改为 "commutator"。 |
| 2 | p.146 / PDF p.154 | 例 6.1.3："if $M$ contains a Darboux ball $U$ of radius $3r$ (i.e. $U$ is $B^{2n}(3r)$), then ... $e(U)=\pi r^2$" | 与同例前半的 $e(B^{2n}(r))=\pi r^2$ 及注 6.1.4 的辛同胚不变性矛盾：应得 $e(U)=e(B^{2n}(3r))=9\pi r^2$。 | 疑为「半径 $3r$ 的 Darboux 球中半径 $r$ 的球（而非整个 $U$）满足 $e=\pi r^2$」；或把 $3r$ 误写。请核对 [221]。 |
| 3 | p.159 / PDF p.167 | 关键观察前："for the contact 1-form $\alpha(=\iota_{\lambda_{\mathrm{std}}}|_{\partial W})$" | 记号 $\iota_{\lambda_{\mathrm{std}}}$ 无定义；本节前文刚定义 $\alpha=\lambda_{\mathrm{std}}|_{\partial W}$，此处 iota 疑为 lambda 之误。 | 改为 $\alpha(=\lambda_{\mathrm{std}}|_{\partial W})$。 |
| 4 | p.167 / PDF p.175 | 例 6.3.5："when restricted at **grading 1** ... the barcode of $\mathbb{V}_W$ at **degree 0** is $\mathbb{B}(\mathbb{V}_W)|_{*=1}=\{(-\infty,0]\}$" | 前后不一致：同一句先称 grading 1，后称 degree 0，而记号 $\mathbb{B}(\mathbb{V}_W)|_{*=1}$ 与下文「grading covers $1,3,5,\cdots$」都指次数 1。 | "degree 0" 应为 "degree 1"。 |
| 5 | p.169 / PDF p.177 | 式 (6.25)：$\ln c_{\mathrm{SH}}(W)=$ "the most **left** endpoint of the intervals in the lowest degree in barcode $\mathbb{B}(\mathbb{V}_W)$" | 与随后计算 $c_{\mathrm{SH}}(B^{2n}(1))=e^{\ln 1}=1$ 矛盾：由例 6.3.5，最低次数区间为 $(-\infty,\ln r]$，其最左端点为 $-\infty$，只有取有限端点（右端点）$\ln r$ 才得 $e^{\ln r}=r$。例 6.4.1 交换图中也写作 "the left end point"。 | 疑为 "the most right endpoint"（或条形码过滤轴方向约定相反）。请核对原文/原图。 |
| 6 | p.168–169 / PDF p.176–177 | 定义 6.4.1 (c2)：$c(\lambda U)=\lambda c(U)$，$\lambda U:=\{\sqrt{\lambda}\cdot x\mid x\in U\}$；命题 6.4.1 证明中却用 $c(B^{2n}(r))=r\,c(B^{2n}(1))$、$w_G(\lambda U)=\sup\{\lambda r'\}=\lambda w_G(U)$ | 量纲不自洽：按 (c2) 的定义，$\lambda U=\{\sqrt\lambda x\}$ 使长度按 $\sqrt\lambda$ 缩放，故 $B^{2n}(r)=r^2 B^{2n}(1)$，应有 $c(B^{2n}(r))=r^2c(B^{2n}(1))$；同理 $w_G(\lambda U)=\sqrt{\lambda}\,w_G(U)$，$\sup$ 中应为 $\sqrt{\lambda}r'$ 而非 $\lambda r'$。全书其他处（例 6.1.3、$c_{\mathrm{SH}}(B^{2n}(1))=1$）又用「容量 = 半径」约定。 | 需统一约定：或取 $\lambda U=\{\lambda x\}$ 且 $c$ 为「面积型」，或保留 $\{\sqrt\lambda x\}$ 而把 $c(B^{2n}(r))=r^2c(B^{2n}(1))$ 与 $\sqrt\lambda$ 写对。建议核对原书此段。 |
| 7 | p.171 / PDF p.179 | "a work from Abbondandolo-**Editmar**-Kang [3]" | 作者姓名疑误：相关作者应为 O. Edtmair（Edtmair, 拼作 E-d-t-m-a-i-r）。 | 改为 "Abbondandolo-Edtmair-Kang"，并核对参考文献 [3]。 |
| 8 | p.151 / PDF p.159 | 例 6.2.5 证明中 "the second equality comes from (6.3) in **Example 6.2.3**" | (6.3) 实际陈述于**事实 6.2.2**；例 6.2.3 只是在其后应用 (6.3)，并未陈述该式。 | 改为 "Fact 6.2.2 中的 (6.3)"。 |

## 非疑误、但已加 Tutor Note 提示的易错点（不在此表重复）

- 定义 6.1.1 的两重下确界与 $H\mapsto H+c(t)$ 不影响 $\|H\|_{\mathrm{Hofer}}$；
- $d_{\mathrm{Hofer}}(\varphi,\psi)=\|\varphi^{-1}\psi\|$ 的次序与双不变性；
- 定理 6.1.2 证明中「$A$ 内部非空 ⇒ 存在支撑在 $A$ 中不交换的 $\varphi,\psi$」；
- 注 6.1.5（Usher）中 $\max/\min$ 由 $M$ 改为 $A$；
- (6.11)–(6.12) 的符号约定与 $f^*\dd\alpha\ge0$ 的推导；
- 命题 6.3.1 的极值原理证明与 (6.15) 的边界定向；
- 例 6.3.3 的斜率窗口 $-4<-\pi/(1-\varepsilon)<-\pi$ 在 $\varepsilon<1-\pi/4$ 时自洽；
- Viterbo 同构 (6.23) 中能量阈值 $\frac{a^2}{2}$ 的来源；
- ECH 容量、$N(a,b)$ 与四维嵌入问题。


---

## 第 7 章 杂论

# 第 7 章 审校记录（review_ch07）

底本：张俊、祝安铜《量化辛几何导引》英文版扫描件。章范围：印刷页 172--194，
扫描 PDF p.180--p.202。下文「印刷页」= PDF 页 − 8。

记录格式：位置 / 原文 / 疑点 / 建议改法。凡在译文中**保留原文写法**者，正文相应
位置均有 `% [Tutor Note: 原文疑误——…]` 批注。

---

## 一、确认为笔误 / 记号不一致

1. **PDF p.189（印刷页 181），Reeb 场验证**
   - 原文：`ν₁(p)a₁ + ν₁(p)a₂ = 0`
   - 疑点：第二个 `ν₁(p)` 应为 `ν₂(p)`。由式 (7.11) 直接读出的是
     `ν₁(p)a₁ + ν₂(p)a₂ = 0`；否则紧接着「`ι_{R_α}dα` 在任意
     `w ∈ T_z∂X_Ω` 上消失」不成立。
   - 建议：改为 `ν₁(p)a₁ + ν₂(p)a₂ = 0`。译文保留原文并加批注。

2. **PDF p.194（印刷页 186），定理 7.2.2 的证明梗概**
   - 原文：`where Z⁴(x₁) and Z⁴(x₁) denote symplectic cylinders with widths
     x₁ and x₂`
   - 疑点：第二个 `Z⁴(x₁)` 应为 `Z⁴(x₂)`，否则与 "widths x₁ and x₂"、图 7.10
     以及 `B⁴(r) ⊂ X_Ω ⊂ Z⁴(x₁) ∪ Z⁴(x₂)` 矛盾。
   - 建议：第二个改为 `Z⁴(x₂)`。译文保留原文并加批注。

3. **PDF p.196（印刷页 188），刘维尔类的长正合列**
   - 原文：`the inclusion i: L → W induces the following long exact sequence`
   - 疑点：`W` 应为 `X`。全段其余部分（长正合列、式 (7.16) 的积分区域）均用
     `X`；`H_2(X;R)=0` 的论证也只在 `X` 上成立，`W` 未定义。
   - 建议：改为 `i: L → X`。译文按 `X` 处理并加批注。

4. **PDF p.199（印刷页 191），命题 7.3.1 的证明**
   - 原文：新面积类第二个分量印作
     `Ω(e₂) − a(Ω(e₁) − Ω(e₂))`
   - 疑点：与紧接其前的 `aΩ(e₁) + (1−a)Ω(e₂)` 不符；按后者应为
     `Ω(e₂) − a(Ω(e₂) − Ω(e₁))`。只有修正后的形式才能推出原文下一不等式
     `Ω(e₂) − a(Ω(e₂)−Ω(e₁)) ≥ 2(Ω(e₁) − a(Ω(e₂)−Ω(e₁)))` 及结论
     `a ≥ Ω(e₁)/(Ω(e₂)−Ω(e₁)) − 1`。
   - 建议：改为 `Ω(e₂) − a(Ω(e₂) − Ω(e₁))`。译文保留原文并加批注。

5. **PDF p.195（印刷页 187），人名**
   - 原文：`J. C. Sikarov [208-209]`
   - 疑点：通行拼写为 Jean-Claude Sikorav（J.-C. Sikorav）。
   - 建议：正文改用「Sikorav」，缩写可作 `J.-C. Sikorav`。译文已按通行拼写
     处理并加批注。

6. **PDF p.191（印刷页 183），定义 7.2.2 (iii)**
   - 原文：`(see the third picture in See Figure 7.6)`
   - 疑点：`in See` 重复（`in` 与 `See` 并存）。
   - 建议：改为 `(see the third picture in Figure 7.6)`。

7. **PDF p.197（印刷页 189），例 7.3.2**
   - 原文：`For pair (r,s) = (1,2), it's hard to` ⏎ `if L = S¹(1)×S¹(2) or …`
   - 疑点：`hard to` 与下一行 `if` 之间显然缺一个动词（应为 `tell` 或
     `distinguish`），系排版/校对付印遗漏。
   - 建议：补为 `it's hard to distinguish if …`。译文按语义译为「很难分辨……」，
     并加批注。

## 二、语法 / 用词瑕疵（不影响数学内容）

8. **PDF p.186（印刷页 178），7.1 节末**
   - 原文：`the Floer homology applied to a Liouville domains in (an open)
     Liouville manifold`
   - 疑点：`a … domains` 单复数不一致。
   - 建议：改为 `a Liouville domain in …` 或 `Liouville domains in …`。

9. **PDF p.193（印刷页 185），例 7.2.6**
   - 原文：`T_min is obtained by the simple closed Reeb orbit occurs at the
     torus fiber μ⁻¹((ε,ε))`
   - 疑点：`is obtained by … occurs` 句法混乱。
   - 建议：改为 `T_min is attained by the simple closed Reeb orbit that occurs
     at the torus fiber μ⁻¹((ε,ε))`。译文按语义译为「由……给出」。

10. **PDF p.199（印刷页 191），命题 7.3.1 的证明开头**
    - 原文：`by subtracting an appropriate many e₁ to e₂`
    - 疑点：`an appropriate many` 与 `subtracting … to` 均不规范。
    - 建议：改为 `by subtracting an appropriate number of e₁ from e₂`。

11. **PDF p.197（印刷页 189），例 7.3.2**
    - 原文：`For pair (r,s) = (1,2)`
    - 疑点：缺冠词。
    - 建议：`For the pair (r,s) = (1,2)`。

## 三、体例说明（非原文错误）

12. **「Fact」环境**：导言区未定义 `wfact`。按本项目既有做法（参见 ch02/ch06），
    正文用 `\whead{事实}{编号}` 手工排版，编号与原文（事实 7.1.1、事实 7.3.1）
    保持一致，正文交叉引用统一作「事实 7.x.x」。

13. **环面凹 / 环面凸的命名**：原文 Definition 7.2.2 的命名与轮廓曲线的凸凹
    **相反**（toric concave 的轮廓曲线是凸曲线，toric convex 的反而是凹曲线），
    并非笔误，但极易误译误读。译文照原文保留「环面凹/环面凸」，并在定义后加
    Tutor Note 明确提示。

14. **图 7.2 与图 7.6 的互引**：p.178 原文写「其矩映射像（见图 7.6 最右图）」之处
    指的是图 7.6 最右（单调）图；但图 7.6 实际在 p.183 才出现，属前向引用，
    译文照译未改。

## 四、核查清单（逐符号）

- (7.1)--(7.8)：Floer 延拓映射、作用量偏移、过滤移位，已与 PDF p.181--p.185
  逐符号核对；注意 (7.6) 左端为 `A_{H₁} − A_{H₂}`（与 (7.5) 方向相反），(7.7)
  在 `H₁ ≥ H₂` 时给出过滤保持，均已核对。
- (7.9)--(7.14)：环面区域、矩映射像、Reeb 场、周期、容量判据，已与 PDF
  p.186--p.192 逐符号核对。`ν_i(p)p_i` 的因子 2、周期公式中的 `λ_pν_i(p)`、
  「坐标轴交点轨道周期 = 截距 × π」均已在批注中说明来历。
- (7.15)--(7.16)：刘维尔类与长正合列，已与 PDF p.195--p.196 逐符号核对；
  连接和记号按原文用 `Σ₁#Σ̄₂`（译文中为 `\#`）。
- 定理 7.3.1 的四个形状不变量公式：已与 PDF p.200 放大逐符号核对（含
  `x₂ ≥ 2x₁`、`x₁ < R/3`、`a > x₁ ≥ a/2`、`b/a ∈ N_{≥2}` 等边界条件）。


---

## 第 8 章 量子上同调

# 第 8 章审校记录（review_ch08.md）

范围：原书 Chapter 8 *Quantum Cohomology*。
本文件的条目 3–9 由 **第 8 章后半译者（ch08 后半：§8.5–§8.7，PDF p.225–p.238）** 记录；
条目 1–2 属 §8.4 末尾（同一 PDF 页 p.225），供前半译者核对。若前半译者另建了同文件，
请把本文件的条目合并（勿覆盖）。
「页」为印刷页码；PDF 页码 = 印刷页码 + 8。

| # | 页 / 位置 | 原文（照录/描述） | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | p.217（PDF 225），§8.4 末尾 | `then ℓ(x)+ℓ(−x) = (−a)+a = 0` | 定理 8.4.1 的结论是 $\ell(x)+\ell(x^{-1})\ge-c$，而 $\ell(-x)$ 对 Novikov 环元素无定义，应为 $\ell(x^{-1})$ | 改为 `ℓ(x)+ℓ(x⁻¹)` |
| 2 | p.217（PDF 225），§8.4 末尾 | `x* y = (−1)^{deg x deg y} y*x` 等超对称性 | 无错误；仅提示与 §8.7 量子乘积的符号约定须一致 | — |
| 3 | p.223（PDF 231），$\Phi$ 的改写 | 第一行内层求和写作 `Σ_{i=1}^{n} t_i e_i` | 基为 $\{e_0,\cdots,e_n\}$（$n+1$ 个元素），定义 (8.47) 亦作 $\sum_{i=0}^{n}$；此处应为 $i=0$ | 改为 `Σ_{i=0}^{n}` |
| 4 | p.225（PDF 233），定理 8.6.1 末句 | `for any 0 ≤ i, j ≤ n`（在 (8.49) 之后） | $i,j$ 已被求和为哑指标，此句重复且错误；应约束 $a,b,c,d$ | 改为 `for any 0 ≤ a,b,c,d ≤ n` |
| 5 | p.225（PDF 233），例 8.6.3 | `Φ₂₁₂ = Σ_{d≥2} N_d t₂^{3d−4}/(3d−4)! q^d e^{dt₁}` | 该式实为 $\Phi_{222}=\partial^3/\partial t_2^3\Phi$；真正的 $\Phi_{212}=\partial_{t_1}\partial_{t_2}^2\Phi=\sum_{d\ge1}N_d\,t_2^{3d-3}/(3d-3)!\,q^d\,d\,\ee^{dt_1}$（与 $\Phi_{122}$ 相同）。而 (8.50) 恰需 $\Phi_{222}$ | 下标改为 `Φ₂₂₂` |
| 6 | p.225（PDF 233），例 8.6.3 | `This holds trivially since Φ₀₀₀ = Φ₁₁₀ = 0 and Φ₁₀₁ = Φ₁₁₀ = 0.` | 与所给 $\Phi=\frac12t_0^2t_1+\ee^{t_1}q$ 不符：按此 $\Phi$ 有 $\Phi_{100}=\Phi_{010}=\Phi_{110}=1\ne0$，而 $\Phi_{000}=\Phi_{101}=0$。此时 (8.49) 的两端分别等于 $\Phi_{100}\Phi_{110}=1$ 与 $\Phi_{010}\Phi_{101}+\Phi_{110}\Phi_{100}=1$，等式仍成立，但并非「trivially」由所列零点得到 | 改为说明 $\Phi_{000}=\Phi_{101}=0$ 且 $\Phi_{100}=\Phi_{110}=1$，两端同为 1 |
| 7 | p.224（PDF 232），例 8.6.2(i) | 系数写作 `1/(2!1!)`、`1/(1!2!)` | 按 (8.47) 的重数因子应为 $1/(\alpha_0!\alpha_1!\alpha_2!)$，即 $1/(2!\,0!\,1!)$；原文省略了 $0!$，数值上无碍 | 补全为 `1/(2!0!1!)`、`1/(1!2!0!)` |
| 8 | p.228（PDF 236），例 8.7.1 | `c ∗ c ∗ ··· ∗ c = c ∗ cⁿ = T^L = T^L·1` | 记号不严谨（「$(n+1)$ 个 $c$ 相乘」写作 $c*c^n$），且未说明 $T^L$ 与 $T^{\omega(L)}$ 的约定 | 建议写为 $\underbrace{c*\cdots*c}_{n+1}=T^L\cdot1$ 并注明 Novikov 约定 |
| 9 | p.226（PDF 234），例 8.6.4 | `N₄ = 620, N₅ = 87304, N₆ = 26312976, N₇ = 14616808192` | 已用 (8.51) 复核：$N_4,N_5,N_6,N_7$ 与所列数值一致，无误（记录于此作为核对凭据） | — |

## 说明

- 第 3–6 项为实质性的公式/记号问题，译文中对应位置已加 `% [Tutor Note: ...]` 说明，
  并**保留原文写法**（第 5、6 项在批注中给出正确形式）。
- 第 7、8 项为记号不严谨，不影响结论；译文按语义通顺处理，未逐字照录分母。
- 第 9 项为正向核对记录，供审校者抽查递推公式 (8.51) 的实现是否正确。
- 其余细节：§8.7 中 PSS 映射 $\Phi_{\mathrm{PSS}}$ 的定义域写作
  $\mathrm{HF}_*(M,\omega,H,J)$，而定理 5.4.1 的原始记号可能带不同下标约定，
  译文按原书照录，读者可对照第 5 章核对。

---

# 附：第 8 章前半（§8.0–§8.4，PDF p.203–224）审校记录

由 **ch08b 前半译者（§8.0–§8.4，PDF p.203–p.224）** 追加；编号接上表（10 起）。
「页」为印刷页码；PDF 页码 = 印刷页码 + 8。对应源码：`ch08-s01.tex`（章首引言 + §8.1）、
`ch08-s02.tex`（§8.2）、`ch08-s03.tex`（§8.3）、`ch08-s04.tex`（§8.4）。

| # | 页 / 位置 | 原文（照录/描述） | 疑点 | 建议改法 |
|---|---|---|---|---|
| 10 | p.195（PDF 203），章首引言 | `this is the born of the quantum cohomology` | `born` 应为 `birth`（名词误用） | 改为 `birth` |
| 11 | p.195（PDF 203），同上 | `... from various symplectic machinery. therefore, only requiring ...` | 句号后 `therefore` 小写，前句句号应改为分号（或 `Therefore` 大写另起） | 标点/大小写修正 |
| 12 | p.195（PDF 203），同上 | `quantities rend off from various symplectic machinery` | `rend off` 疑为 `rendered off`（或 `descending from`）之误 | 改为 `rendered off` |
| 13 | p.196（PDF 204），例 8.0.1 末句 | `there is no uniform κ>0 satisfying the monotone condition (8.2)` | 单调条件应为 (8.1)；(8.2) 是 $\CP^n$ 上的具体计算 | 改为 `(8.1)` |
| 14 | p.198（PDF 206），§8.1(2) | `Λ^{k,R} ≅ k[T]. Here, k[T] either denotes the completion of the polynomial ring k[T] in the positive direction, or simply follows the standard name, the ring of Laurent series.` | 同一记号 $\mathbf{k}[T]$ 先后指形式幂级数环、多项式环与 Laurent 级数环，三者不同；正确的断言应为 $\Lambda^{\mathbf{k},\Z}\cong\mathbf{k}(\!(T)\!)$（形式 Laurent 级数域），其「正方向完备化」为 $\mathbf{k}[\![T]\!]$ | 分别记作 $\mathbf{k}[T]$、$\mathbf{k}[\![T]\!]$、$\mathbf{k}(\!(T)\!)$ |
| 15 | p.199（PDF 207），(8.6)–(8.7) | `x = Σ a_A T^A ... and t is a formal variable`；`x = Σ a_{(B,λ)} t^{(B,λ)} = Σ(Σ a_{(B,λ)} S^B) T^λ` | 形式变量同一式中先写 $T$、再写 $t$（正文亦作 `t`），前后不一致；按上下文应统一为 $T$ | (8.7) 左端 `t^{(B,λ)}` 改为 `T^{(B,λ)}`，正文 `t` 改为 `T` |
| 16 | p.199（PDF 207） | `Note that so far the sum Σ notations in (8.7) is just a formal sum` | 语法：`notations ... is` 应为 `are`；不影响数学内容 | 语法修正 |
| 17 | p.201（PDF 209），(8.10) | `x ⊥_{(R^n,|·|)} y if and only if |x+y| = |x| + |y|` | **实质错误**：Euclid 范数下正交应满足 $|x+y|^2=|x|^2+|y|^2$；线性关系 $|x+y|=|x|+|y|$ 刻画的是同向共线。作者似把非阿基米德判据 $\ell(x+y)=\max\{\ell(x),\ell(y)\}$（注 8.2.1）误「翻译」成了 Euclid 情形 | 改为 $|x+y|^2=|x|^2+|y|^2$（或 $|x-y|^2=|x|^2+|y|^2$），与注 8.2.1 的非阿基米德类比一致 |
| 18 | p.208（PDF 216），(8.21) 前 | `we will still have a diagram like (??)` | 原书交叉引用未解析，`(??)` 应为 (8.18)（定义 8.3.1 的交换图表） | 改为 `(8.18)` |
| 19 | p.206（PDF 214），定义 8.3.1 | `It is called multiply covered if there exists a J-holomorphic curve u' ... and a holomorphic map φ ...` | 未要求 $\deg(\varphi)\geqslant2$；若允许 $\varphi$ 为双全纯，则任何曲线都平凡地「多重覆盖」，概念失效 | 补上 $\deg(\varphi)\geqslant2$（或要求 $u$ 与 $u'$ 不等价） |
| 20 | p.212（PDF 220），例 8.3.3 | `... the class A = 2L can come from nodal curve ...` 及维数 $4+2\cdot(2\cdot(2+1))+2\cdot0-6-2=8$ | 数值核对无误（$4+12-6-2=8$）；记录作为 (8.28) 的正向核对凭据 | — |
| 21 | p.215（PDF 223），(8.32) | `deg(T) = 2n+2` | 与 $\deg(e_1^{n+1})=2n+2$、$c_1(T\CP^n)=n+1$ 一致，核对无误 | — |
| 22 | p.200（PDF 208） | `The extreme situations are either this subgroup is trivially 0 or is the entire 2Z` | 「this subgroup」指代不明（应为 $\deg$ 在 $H_2^S(M)$ 上取值所生成的子群）；语义可解，但表述含糊 | 建议改为「$\deg(T^A)$ 在 $H_2^S(M)$ 上取值所生成的子群要么平凡、要么为整个 $2\Z$」 |

## 前半部分说明

- 第 13、14、15、17、18、19 项为较实质的问题，译文中对应位置均已加
  `% [Tutor Note: ...]` 说明，并**保留原文写法**（第 17、19 项在批注中给出正确形式）。
- 第 10、11、12、16 项为文字/拼写小误，不影响数学内容，译文按语义通顺处理。
- 两半章的接缝已核对：§8.4 在 PDF p.224（印刷 p.216）并非结束，尚余 PDF p.225 的内容
  （定理 8.4.1 等）由后半译者续写；前半止于练习 8.4.1（p.224 末），无重复、无遗漏。
- 公式编号 $(\text{8.1})$–$(\text{8.35})$ 连续，与后半的 $(\text{8.36})$–$(\text{8.53})$
  无重复、无缺号（`check.py ch08` 全章 36/36 页、53 条编号、无重复）。


---

## 第 9 章（上）9.1–9.3

# 第 9 章上半 审校记录（review_ch09a.md）

范围：原书第 9 章 *Hard Stories on Lagrangians* 前半（9.1--9.3），印刷页 231–249，
扫描 PDF 第 239–257 页。9.4--9.7 由另一译者续写（ch09b）。

处理原则：译文**保留原文写法**并就地加 `% [Tutor Note: ...]` 说明；下表列出原文、
页码、疑点与建议改法。标记「确信」者为可确定之笔误，「待核」者需对照作者原稿确认。

| # | 位置（印刷页 / PDF 页） | 原文 | 疑点 | 建议改法 | 把握 |
|---|---|---|---|---|---|
| 1 | p.231 / p.239，章首导语 | "Often this provides surprisingly results" | 副词误作形容词 | "surprising results" | 确信 |
| 2 | p.235 / p.243，(ii) | "via the stereographic projection define by" | 语法笔误 | "defined by" | 确信 |
| 3 | p.235 / p.243，(i)--(ii) | "disk $B^2(2)$ ... with radius $\sqrt2$"，随后又写 $B^2(\sqrt2)$ | 同一对象两种记号 | 统一为半径 $\sqrt2$ 的圆盘记号（并据 (1.13) 核对 $B^2(r)$ 的确切定义） | 待核 |
| 4 | p.238 / p.246，例 9.2.2 | "It can be viewed it as an $A_\infty$-algebra" | 多一个 it | "It can be viewed as" | 确信 |
| 5 | p.239 / p.247，(9.15) | $\sum_{l_0,\cdots,l_k\geqslant0} m_{\cdots}(b^{\otimes l_1}\otimes x_1\otimes\cdots\otimes x_k\otimes b^{\otimes l_k})$ | 求和指标 $l_0,\cdots,l_k$ 共 $k+1$ 个，但单项式中只出现 $b^{\otimes l_1},\cdots,b^{\otimes l_k}$ 共 $k$ 个，$l_0$ 未出现 | 写成 $b^{\otimes l_0}\otimes x_1\otimes b^{\otimes l_1}\otimes\cdots\otimes x_k\otimes b^{\otimes l_k}$（或把指标改为 $l_1,\cdots,l_{k+1}$） | 待核 |
| 6 | p.239 与 p.240 / p.247 与 p.248，(9.16) | 两处均编号 (9.16) | 公式编号重复（p.239 末的展开式与 p.240 的 Maurer--Cartan 方程） | 其一改为 (9.17)，其后编号顺延；或在重印时修正 | 确信 |
| 7 | p.239 / p.247，(9.16) | 展开式末两行均含 $m_2(m_2(b\otimes x)\otimes b)$ | 同一项重复出现，且缺少按 $\hat m_1^b$ 展开应出现的 $m_2(b\otimes m_2(x\otimes b))$ | 核对 $m_2(b\otimes m_2(x\otimes b))$ 与 $m_2(m_2(b\otimes x)\otimes b)$ 两项 | 待核 |
| 8 | p.240 / p.248，(9.16) 的改写式 | 改写式与 (9.16) 逐项对照 | 改写式似漏掉 $m_2(m_2(b\otimes x)\otimes b)$、$m_2(b\otimes m_2(x\otimes b))$ 型项，且 $m_2(m_1(x)\otimes b)$ 只出现一次 | 逐项重算（建议按 $m_1(m_2(b\otimes x)+m_2(x\otimes b))$ 的 Leibniz 展开重排） | 待核 |
| 9 | p.240 / p.248，注 9.2.3 | $m_0(1)+m_1(b)+m_2(b,b)+\cdots$ | $m_2$ 的定义域是 $C\otimes C$，应写 $m_2(b\otimes b)$ | 改为 $m_2(b\otimes b)$ | 确信 |
| 10 | p.246 / p.254，(iv) 的开头 | "define the the following subset" | 多一个 the | "the following subset" | 确信 |
| 11 | p.246 / p.254，(9.23) | $\operatorname{supp}(H)\in[0,1]\times M\setminus R_L$ | 支撑集是集合，不能用 $\in$ | 改为 $\operatorname{supp}(H)\subset[0,1]\times M\setminus R_L$ | 确信 |
| 12 | p.248 / p.256，定理 9.3.1 的证明 | "the map $\widehat\Phi:\R^{2n}\to R_L$ defined by $\widehat\Phi(t_1,\cdots,t_n):=\cdots$" | 自变量只有 $n$ 个，定义域应为 $\R^n$；像落在 $R_L\subset L$ | 改为 $\widehat\Phi:\R^n\to R_L$（或 $\R^n\to M$） | 确信 |
| 13 | p.248 / p.256，定理 9.3.1 的证明 | "choose local coordinates $(x_1,\cdots,x_{2n})$ around $x$ such that $x_i\notin L^n$ for $i=1,\cdots,n$" | 字面不通：$x_i$ 是坐标函数，不能与子流形 $L^n$ 作「属于/不属于」比较。按图 9.7 与证明用途，应指这 $n$ 个坐标方向在 $x$ 处横截于 $L$ | 建议改为「使 $\partial/\partial x_1,\cdots,\partial/\partial x_n$ 与 $T_xL$ 一起张成 $T_xM$」或等价的横截性条件 | 待核 |
| 14 | p.248 / p.256，定理 9.3.1 的证明末 | "is non-degenerate.." | 双句点 | 删去多余句点 | 确信 |

## 已核对但判为无误的易混点

- (9.9) 中第二个矩阵为 $\operatorname{diag}(-1,-1,1)$，与 $R_{-s}$ 的关系
  $D R_s=R_{-s}D$ 成立（因 $d_3=-d_2$），故 (9.9) 无误。
- (9.3) 的 $\omega_{S^2}(v,w)=\langle p,v\times w\rangle$ 是单位球面标准面积形式；
  $B^2(2)$（半径 $\sqrt2$）的面积 $2\pi$ 与 $(S^2,\tfrac12\omega_{S^2})$ 的总面积一致，
  (ii) 的嵌入确为等面积同构（二维时等面积即辛同胚）。
- 事实 9.2.1 的包含方向为 $\mathcal M_{\mathrm{weak}}(\mu^{-1}(x))\supset H^1(\cdots)$，
  不是 $\subset$（弱界定上链的集合更大），原文无误。
- (9.18) 中 $v_i$ 为内法向量，故 $l_i(x)\geqslant0$（$x\in\Omega$），$T^{l_i(x)}$ 属于
  $\Lambda^{\mathbf{k},\Gamma_\omega}_{\geqslant0}$，与例 9.2.4 的显式计算一致。
- 例 9.2.4 中 $(0.5,0.5)$ 处四个超平面给出 $l_i=1/2$，故势函数四项均带 $T^{1/2}$，
  与原文一致。

## 体例说明（非原文疑误）

例 9.2.3（相对 Gromov–Witten 不变量）在原文中从 p.240 延续到 p.242，其间夹有
定理 9.2.1 与「Roughly speaking……」一段，段末以 `//` 结束。若把定理 9.2.1 置于例内
将造成环境嵌套上的混乱，故译文把例 9.2.3 收在 p.241 末「……在 $L$ 本身上进行的」处，
其后「为借助 $^{\mathrm{rel}}\mathrm{GW}_{\beta,k}$ 构造 $A_\infty$-代数……」一段
按正文处理，段末的 `//` 以 $\square$ 呈现。此系排版取舍，不影响文字内容。

## 编号核对- 公式编号 (9.1)–(9.25) 齐全；其中 (9.16) 在原文出现两次（见上表 #6）。译文中
  p.239 末的展开式用 `\tag{9.16}`，p.240 的 Maurer–Cartan 方程用 `\tag*{(9.16)}`
  以忠实呈现原文编号、同时避免 LaTeX 标签重复。
- 定理类编号：9.1 节 7 项、9.2 节 15 项（含事实 9.2.1、9.2.2）、9.3 节 16 项，
  共 38 项，均按原文标号。

## 图目录（300 dpi 裁自扫描页，置于 qsg/figures/）

| 文件 | 原书位置 | 说明 |
|---|---|---|
| `fig_p243_1.png` | p.235 | 图 9.1 $\{\varphi_G^t(p)\}$ 在 $S^2\times S^2$ 中的轨道 |
| `fig_p243_2.png` | p.235 | 图 9.2 半圆盘内的闭曲线 $\Gamma$ |
| `fig_p249_1.png` | p.241 | 图 9.3 带 $k$ 个标记点的 $J$-全纯圆盘 |
| `fig_p251_1.png` | p.243 | 图 9.4 由方程确定的超平面 |
| `fig_p252_1.png` | p.244 | 图 9.5 $(S^2\times S^2,\omega_{\mathrm{prod}})$ 矩像中的超平面 |
| `fig_p254_1.png` | p.246 | 图 9.6 经 $\varphi^{-1}$ 作用 |
| `fig_p256_1.png` | p.248 | 图 9.7 $M^{2n}$ 上的坐标与 $L^n\subset M^{2n}$ |


---

## 第 9 章（下）9.4–9.7

# 第 9 章后半（9.4–9.7）原文疑误与待核清单

- 9.4–9.5（PDF p258–p273）：译者 ch01-symplectic，条目待其追加（见文末）。
- 9.6–9.7（PDF p274–p289）：译者 ch05a-floer，条目见下。
- 说明：下列疑误均在译文中保留原文写法，并加 `% [Tutor Note: ...]` 注释。

## 9.6–9.7（PDF p274–p289）

| # | 位置（印刷页/PDF 页） | 原文 | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.269 / PDF 277 | 定理 9.6.1 证明中「where $d_C^{k+1}(c)\in C_{k+2}$ and $f^{k+1}(c)+d_D^k(d)\in D_{k+1}$」 | 本节通篇是\emph{上}链复形（$C^k$、$d^k$），此处却印成下指标 $C_{k+2}$、$D_{k+1}$ | 改为 $C^{k+2}$、$D^{k+1}$（译文照原文保留并加注） |
| 2 | p.271 / PDF 279 | (9.39) 后的「$C^\bullet(U_1+U_2)$」，同段又用 $U_1\cup U_2$ | 「$+$」在此意为并（链群相加），与 $\cup$ 记号混用，易误解为不交并 | 建议统一为 $C^\bullet(U_1\cup U_2)$，或在首次出现处说明 $U_1+U_2:=U_1\cup U_2$ |
| 3 | p.272 / PDF 280 | (9.40) 的三角链：首行 $Y\to0\to Z_1\to Y[1]$、次行 $E_2\to Z_1\to Z_2\to E_2[1]$、末行 $E_{k-1}\to Z_{k-1}\to X\to E_{k-1}[1]$ | 首行以 $Y$ 起、次行却以 $E_2$ 起（相当于把 $Y$ 记作 $E_1$），而「$E_i\in F$，$2\leqslant i\leqslant k-1$」又排除了 $E_1$；记号不闭合 | 待核：建议把 $Y$ 也记作 $E_1$（并写 $E_1=Y$），或统一说明 $E_1:=Y$、$E_k:=X$ |
| 4 | p.274 / PDF 282 | (9.42) 之前：「an embedding $\varphi:\T^n\hookrightarrow(\CP^n,\omega_{\mathrm{FS}})$ is called \emph{exact} if any embedded disk $(\mathbb D^2,\partial\mathbb D^2)\xrightarrow{f}(\CP^n,\varphi(\T^n))$ satisfies」 | 「嵌入圆盘」的边界应落在 $\varphi(\T^n)$ 上（原文由记号隐含），且应对\emph{所有}这样的圆盘成立；原文表述略松，但数学上可读 | 建议明确写「for every embedded disk with boundary in $\varphi(\T^n)$」；译文按原意译出 |
| 5 | p.278 / PDF 286 | 例 9.7.4 中 $X^+=\left((-\infty,0]\times\varphi(S^*_gL)\right)\cup_{\varphi(S^*_gL)}(X\setminus\varphi(D^*_gL))=X\setminus\varphi(0_L)$ | 第一个等号用到 $(-\infty,0]\times S^*_gL\cong D^*_gL\setminus0_L$ 的等同（沿 $\R$-方向伸缩），原文未说明 | 建议补一句「其中 $(-\infty,0]\times S^*_gL$ 经 $(r,\xi)\mapsto\ee^r\xi$ 等同于 $D^*_gL\setminus0_L$」 |
| 6 | p.280 / PDF 288 | 例 9.7.5：「$\mathrm{GW}^{\CP^n}_{L,3}(c^i,c^j,c^k)=1$ if $i+j+k=2n+1$（见事实 8.7.1）」 | 该分次条件依赖第 8 章（事实 8.7.1）的维数/分次约定；本译者无法在本章内独立验证 | 待核：请 ch08 译者核对事实 8.7.1 的编号与 $2n+1$ 条件是否一致 |
| 7 | p.279 / PDF 285 | (9.43)：$\omega_k$ 在 $\widetilde X^-$ 上取 $\ee^{-k}\omega$，在 $[-k,0]\times M$ 上取 $\dd(\ee^r\lambda)$ | 要在 $r=-k$ 处光滑衔接，需 $\omega=\dd\lambda$（或 $\omega=\dd(\ee^r\lambda)$）在 $M$ 的管状邻域内成立；原文默认这一标准设置 | 体例说明：非笔误，但建议在 (9.43) 前加一句「在 $M$ 的接触管状邻域内 $\omega=\dd(\ee^r\lambda)$」 |
| 8 | p.266 / PDF 274 | (9.36) 的嵌套写法「$\mathrm{Cone}(L_{k-1}\to\mathrm{Cone}(L_{k-2}\to\cdots)\cdots\to\mathrm{Cone}(L_2\to\mathrm{Cone}(L_1\to L'))\cdots)$」 | 省略号与括号的嵌套在原文中较含混（排版歧义），不易一眼读出迭代结构 | 建议改写为归纳式：$L^{(j)}=\mathrm{Cone}(L_j\to L^{(j-1)})$、$L^{(0)}=L'$，或加括号说明；译文照原文保留 |

## 体例与宏说明（9.6–9.7）

1. **交换图**：preamble 无 tikz/amscd 等绘图宏包（且禁改 preamble），故 9.6 节的 7 个交换图均用 `array` + `\xrightarrow`、`\big\downarrow`、`\swarrow` 手工排版，已逐页编译核对。
2. **插图**：9 幅（图 9.18–9.26）均从扫描页 300 dpi 裁剪为 `qsg/figures/fig_pNNN_k.png`，经 `read_image` 验证完整；图注为中文并标注原书图号、印刷页、PDF 页。
3. **`Fact` 环境**：本章未用到。
4. **原书 `//` 记号**：例 9.6.1–9.6.3、9.7.1–9.7.5 末尾沿用原书「//」结束记号（`\hfill$//$`）。

## 自检结果（本半 p274–p289）

- `python qsg/tools/check.py ch09b`：本半 **p274–p289 全部覆盖、无缺页、无结构错误、无重复 tag、无缺失图片、无禁用命令**；节 2、keytakeaways 2、Tutor Note 21、图 9、公式编号 11（(9.36)–(9.46)）。
- 试编译（`preamble` + ch09b-s03/s04）通过：14 页，零 Overfull/Underfull、零 undefined；测试文件已删除，未改 preamble/main/00-front 及他人文件。
- 注：整章 `check.py ch09b` 目前仍报缺 p258–p273，属 ch01-symplectic 的 ch09b-s01/s02 尚未完成（其 s01 已出现），非本半缺页。

## 9.4–9.5（译者 ch01-symplectic）

范围：印刷页 250–265，PDF p258–p273。文件 `qsg/tex/ch09b-s01.tex`（9.4，含 p258 顶部 §9.3 收尾）、
`qsg/tex/ch09b-s02.tex`（9.5）；插图 `qsg/figures/fig_p261_1.png` … `fig_p273_1.png` 共 10 幅
（图 9.8–9.17）。

### 跨节接缝说明

- PDF p258 顶部是 §9.3 的收尾（推论 9.3.1 及其证明、命题 9.3.1 证明的后 3/4 页），之后才出现
  「9.4 Distance Between Lagrangians (Large Scale)」。因 ch09a 只覆盖到 p257，该页由本译者承接，
  置于 `ch09b-s01.tex` 开头，并加 `% >>> p258` 标记。
- PDF p264 中部为 9.4 节末尾（`ch09b-s01.tex` 结束）与 9.5 节开头（`ch09b-s02.tex` 开始）的分界，
  两文件均带 `% >>> p264` 标记。
- PDF p274 顶部仍是 9.5 节内容（(9.36)、注 9.5.5），由 ch05a-floer 写入 `ch09b-s03.tex` 开头；
  本译者只写到 p273 页脚，无重复。

### 疑误清单

| # | 位置（印刷页/PDF 页） | 原文 | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.251 / p.259、p.252 / p.260 | 练习 9.4.1 的 (ii)「for $L(\kappa)$ obtained from **(a)** above」；(iii)「Deduce from **(a)** above」 | 本题小问标号为 (i)–(iv)，并无 (a)；按上下文均应为 (i) | 改为 (i) |
| 2 | p.252 / p.260 | 「given $r\in\mathbb{R}$, first construct $f_r\in C_c([0,1];\mathbb{R})$」，而上文简化定理要求 $r,s\in[0,\infty)$ | 定义域前后不一致；$r<0$ 时 $f_r\le0$，几何解释需对称处理 | 统一为 $r\ge0$（或说明 $r$ 任意、结论对 $\|r-s\|$ 成立） |
| 3 | p.254 / p.262 | 事实 9.4.1 (ii)「a Hamiltonian function $F:[0,1]\times M\to\mathbb{R}$」 | 本事实的辛流形是 $(\CP^1,\omega_{\mathrm{FS}})$，此处 $M$ 应为 $\CP^1$（沿用了第 1 章的通用记号） | $F:[0,1]\times\CP^1\to\mathbb{R}$ |
| 4 | p.255 / p.263、p.256 / p.264 | Alexander 技巧中用参数 $s$（$\psi_s$、$s\in[\epsilon,1]$），而 (9.33) 直接写 $\psi_\epsilon$ | 相当于在 (9.33) 处取 $s=\epsilon$，原文未交代这一替换 | 在 (9.33) 前说明「取 $s=\epsilon$」 |
| 5 | p.256 / p.264 | 「Since $H_t$ needs to be compactly **support**」 | 语法：应为 compactly supported | 语义译为「需具有紧支撑」 |
| 6 | p.257 / p.264 等多处 | 「homogenous quasi-morphism」 | 拼写：应为 homogeneous（齐次） | 译文统一按「齐次」处理 |
| 7 | p.262 / p.270 | 定义 9.5.2：「the fiber of the projection $\pi:V\to\mathbb{R}^2$ is $\bigcup_{i}([R,+\infty)\times\{s=i\}\times L_i)$」 | 该式给出的是**原像** $\pi^{-1}(\{t\ge R\})$，而非单点上的纤维；单点纤维应为 $L_i$ 或空集 | 改为「$\pi(V)\cap\{t\ge R\}=\bigcup_i([R,+\infty)\times\{s=i\})$，且 $\pi^{-1}([R,+\infty)\times\{s=i\})=[R,+\infty)\times\{s=i\}\times L_i$」 |
| 8 | p.259 / p.267 | 「$a(t),b(t)$ 是 $\mathbb{R}$ 上固定的函数……且 $\gamma(t)$ is smooth for $t\in[0,1]$」 | 按前后文 $\gamma$ 定义在整个 $\mathbb{R}$ 上，限定 $t\in[0,1]$ 与「$\mathbb{R}$ 上的函数」矛盾 | 应为「$\gamma(t)$ 在 $t\in\mathbb{R}$ 上光滑」 |
| 9 | p.264 / p.272 | $\mathrm{Mor}(L,L')$ 定义中「$V$ is a Lagrangian cobordism; $L_1\cdots,L_{k-1}$ are Lagrangians」 | 逗号缺失；且未说明 $k$ 可等于 1（此时即平凡配边） | 补逗号，并说明 $k=1$ 时 $L_1=\cdots=L_{k-1}=\varnothing$ |
| 10 | p.257 / p.265 | 引理 9.5.1 出处写作「(Proposition in 3.1.E in [180])」 | 编号体例怪异，应为「[180] 第 3.1.E 节中的命题」 | 已按此意译为「[180] 中命题 3.1.E」 |
| 11 | p.252 / p.260 | 简化定理写「嵌入 $\Phi:([0,\infty),|\cdot|)\hookrightarrow(\mathcal{O}(L),\delta_{\mathrm{CH}})$」，而定理 9.4.1 用 $C_c^\infty([0,1];\mathbb{R})$、证明中用 $C_c([0,1];\mathbb{R})$ | 三处定义域口径不同（非笔误，仅记，便于对照） | 无需改动 |

### 体例与术语（9.4–9.5）

1. **图**：图 9.8–9.17 共 10 幅，均按 150 dpi 页面图像素坐标裁剪、300 dpi 输出，
   `read_image` 逐幅验证完整无截断；图注为中文并标注原书图号、印刷页、PDF 页。
2. **术语**：Lagrangian suspension 译「拉格朗日悬浮」；Lagrangian surgery 译「拉格朗日手术」；
   quasi-morphism 译「拟同态」（与第 1 章一致）；defect 译「缺陷」；shadow 译「影子」；
   displaceable 译「可位移的」；cobordism category 译「配边范畴」；hom-set 译「同态集」；
   unit 译「单位」；scl 保留记号并注「换位子长度的齐次化」。人名 Chekanov、Hofer、Bavard、
   Alexander、Biran、Cornea 一律保留拉丁字母。
3. **`//` 结束记号**：例 9.5.1 末尾沿用原书「//」。
4. **$L_1\#_xL_2$**：原书用 $\#$ 记手术，译文保留（`\#`），并注意与「连通和 $\#$」区分。

### 自检结果（本半 p258–p273）

- `python qsg/tools/check.py ch09b`：**p258–p273 全部覆盖、无缺页、无结构错误、无重复 tag、
  无缺失图片、无禁用命令**；本半节 2、keytakeaways 2、Tutor Note 14、图 10、
  公式编号 (9.26)–(9.35) 共 10 个。
- 试编译（`preamble` + ch09b-s01/s02）通过：14 页，0 error，无 Missing character；测试文件
  在 `work/tmp/`，未改 preamble/main/00-front 及他人文件。


---

## 第 10 章（上）10.1–10.4

# 第 10 章前半「生成函数与层速成」疑误记录（review_ch10a.md）

记录范围：PDF p.290–p.306（印刷页 282–298，即 10.1、10.2 两节）。每条给出原文、
所在页（印刷页 / PDF 页）、疑点与建议改法。均已在正文对应位置以
`% [Tutor Note: 原文疑误 ...]` 标注，译文保留原文写法，未擅自改动。

| # | 印刷页 / PDF 页 | 原文（摘录） | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.286 / PDF p.294 | 式 (10.5)：$\psi_t^{(i)}=\varphi_{\frac{(i-1)t}{N}}\circ\varphi_{\frac{it}{N}}^{-1}$ | 按通常的复合次序取乘积 $\psi^{(1)}\circ\cdots\circ\psi^{(N)}$，对 $N=2$ 得 $\psi^{(1)}\circ\psi^{(2)}=\varphi_t^{-1}$，一般地也得到 $\varphi_t^{-1}$ 而非 $\varphi_t$。要使乘积伸缩相消为 $\varphi_t$，应取 $\psi_t^{(i)}=\varphi_{\frac{it}{N}}\circ\varphi_{\frac{(i-1)t}{N}}^{-1}$（或等价地把乘积的复合次序反过来）。 | 核对原书；若原书如此，建议改正为 $\varphi_{it/N}\circ\varphi_{(i-1)t/N}^{-1}$。 |
| 2 | p.287 / PDF p.295 | 命题 10.1.1："$F_2\colon\R^{2n}\times\R^{N_1}\to\R$ is the generating function of $\varphi_2$" | 同一命题中 $F_1\#F_2$ 的变量 $e_2\in\R^{N_2}$，故 $F_2$ 的定义域第二因子应为 $\R^{N_2}$。 | 改为 $F_2\colon\R^{2n}\times\R^{N_2}\to\R$。 |
| 3 | 3a. 296 / PDF p.304 | 核层茎的计算："$\ker(\mathbf{k}_X\to i_\ast(i^{-1}\mathbf{k}_X))_0$"，其中框架是 $Z=(0,1)\subset\R=Y$、$i\colon\R\setminus(0,1)\to\R$ | 环境空间是 $Y=\R$，所裁剪的常值层应为 $\mathbf{k}_Y$；此处 $X$ 疑为 $Y$ 之误（本节其余地方均用 $\mathbf{k}_Y$）。 | 改为 $\mathbf{k}_Y$；或统一说明 $X=Y=\R$ 的记号约定。 |
| 4 | p.298 / PDF p.306 | 例 10.2.11 末：$\bigl((\mathbf{k}_\R)_{(0,1]}\bigr)((a,b))=\mathbf{k}$ 若 "$a\in[0,1]$" | 按该段自身的计算，$a=1$ 时 $\bigl((\mathbf{k}_\R)_{(-\infty,1]}\bigr)((a,b))=\mathbf{k}$、$\bigl((\mathbf{k}_\R)_{(-\infty,0]}\bigr)((a,b))=0$，核为 $\mathbf{k}$；但若同时 $b\le 1$，区间 $(1,b)$ 为空，端点约定需与全书的「左开右闭」约定核对。疑应为 $a\in[0,1)$ 或需补充 $b$ 的条件。 | 核对原书端点约定（$(a,b)$ 为通常开区间还是 $(a,b]$）。 |
| 5 | p.287 / PDF p.295 | 定义 10.2.1："for any $U\in\Op(x)$" | 应为 $\Op(X)$（同一句前后均用 $\Op(X)$）。 | 改为 $\Op(X)$。 |

## 已加 Tutor Note 提示、但不算疑误的易错点

- 生成函数中「$\partial_eF=0$ 的临界纤维」与「对 $x$ 求导」的先后（定义 10.1.1）；
- 例 10.1.2 中 $F$ 即作用量泛函，$L=\operatorname{graph}(\dd F)$ 是 Hamilton--Jacobi
  方程的全局解，符号约定 $\lambda_{\mathrm{can}}=\sum p_i\dd q_i$；
- 定理 10.1.1 中「无穷远处为二次型」保证临界集的 properness；
- 例 10.1.3 中 $\tau$ 的辛同胚验证（$-\omega_{\mathrm{std}}\oplus\omega_{\mathrm{std}}$
  的负号位置）；
- 常值层 $=$ 常值预层的层化（$\mathbf{k}_X$ 并非常值预层 $U\mapsto\mathbf{k}^N$）；
- $\R_\gamma$ 上的层 $=$ 持续 $\mathbf{k}$-模（例 10.2.4 (iii)），并与定理 5.2.1 对照；
- 茎（stalk）与纤维（fiber）的区别：$\mathcal{F}_x$ 是邻域基上的正向极限（芽），
  纤维是 $\mathcal{F}_x/\mathfrak{m}_x\mathcal{F}_x$ 或局部自由时的
  $\mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\mathbf{k}$；
- 定理 10.2.1 中的 $\mathbf{k}_I$（裁剪常值层）与定理 5.2.1 中的 $\mathbf{k}_I$
  （区间型持续模）同名而所指不同。

---

## 10.3–10.4（PDF p.307–p.314；译者 ch05a-floer）

| # | 印刷页 / PDF 页 | 原文（摘录） | 疑点 | 建议 |
|---|---|---|---|---|
| 6 | p.305 / PDF p.313 | 定义 10.4.1 的等价关系：「there exists $F^\bullet\in\mathrm{Ob}(\mathcal A)$ such that the following diagram commutes」 | $F^\bullet$ 是复形（屋顶图中间的对象），应属 $\mathrm{Ob}(C(\mathcal A))$，而非 $\mathrm{Ob}(\mathcal A)$；否则无法定义 $q''$、$f''$ | 改为 $F^\bullet\in\mathrm{Ob}(C(\mathcal A))$（或 $\mathrm{Ob}(D(\mathcal A))$）；译文照原文保留并加 Tutor Note |
| 7 | p.305 / PDF p.313 | 「Definition 10.4.2 (Proposition)」 | 「定义 10.4.2」后括注「（命题）」，标签体例特殊（原书把一条泛性质命题作为定义陈述） | 体例问题，非笔误；译文保留为「定义 10.4.2（命题式定义）」 |
| 8 | p.304 / PDF p.312 | (10.19) 后：「Here, proper means the pre-image of a compact subset of $Y$ is also compact in $X$.」 | 该紧合性针对的是映射 $f:\operatorname{supp}(s)\to U$，故「紧子集」应是 $U$ 的紧子集（而非整个 $Y$ 的） | 建议写成「$U$ 的紧子集」；不影响 (10.19) 的数学内容 |
| 9 | p.299–300 / PDF p.307–308 | (10.15) 左侧记 $\check H^*$、右侧用指标 $n$ | 上下标约定混用（$*$ 与 $n$ 表示同一次数），原书惯用 $*$ 作占位 | 体例问题；译文照原文，注意 (10.15) 的 $n$ 即 $*$ 的取值 |
| 10 | p.299 / PDF p.307 | 注 10.2.5：「for any $s\leqslant t$ ... for any $s\leqslant t$」 | 同一限定语在相邻两句中重复出现 | 原文如此；译文合并重复，未改数学内容 |

**接缝说明（10.2 → 10.3）**：PDF p.307 顶部依次是图 10.3、承接 p.306 末句「It is in fact」的段落（"an interesting question to explore the relation between these two $\mathbf{k}_I$'s"）与**注 10.2.5**，之后才是 10.3 节标题。按分工这些内容由本译者写入 `ch10a-s03.tex` 开头（含 `% >>> p307` 标记）；已核对 `ch10a-s02.tex` 末尾未重复写入（其末行仅留一句接缝注释）。

**体例**：本章 10.3–10.4 的 2 幅插图（图 10.3、图 10.4）均从扫描页 300 dpi 裁剪为 `qsg/figures/fig_p307_1.png`、`fig_p310_1.png` 并经 `read_image` 验证；preamble 无 tikz，故定义 10.4.1 的「屋顶」交换图与定义 10.4.2 的三角形交换图用 `array` + `\swarrow`/`\nearrow`/`\big\uparrow` 手工排版。

**全章渲染提醒（非本章特有）**：preamble 中 `\newcommand{\Op}{\operatorname}`，因此 `\Op{Sh}` 渲染为 Sh、`\Op{supp}` 渲染为 supp；但若写成 `\Op(X)`，`\operatorname` 会把 `(` 当作参数，导致 "Op" 丢失（渲染成 "(X)"）。本译者文件已统一改用 `\operatorname{Op}(X)`；提醒其他章节（如 ch10b）排查同类写法。

## 自检结果（本半 p307–p314）

- `python qsg/tools/check.py ch10a`：本半 **p307–p314 全覆盖、无缺页、无结构错误、无重复 tag、无缺失图片、无禁用命令**；节 2、keytakeaways 2、Tutor Note 本半新增 14 条、图 2、公式编号 8（(10.13)–(10.20)）。
- 试编译（`preamble` + ch10a-s03/s04）通过：8 页，零 Overfull/Underfull、零 undefined；测试文件已删除，未改 preamble/main/00-front 及他人文件。

---

## 补充：PDF p315 上半页（10.4 节收尾）的补译（QA 缺口修复）

**缺口**：10.4 节的末尾——例 10.4.3 的 (ii)（$Rf_!$ 与 $R\Gamma_c$）、(iii)（$R\mathrm{Hom}$）、
$R\mathrm{Hom}$ 双函子、双复形 $C^{p,q}=\mathrm{Hom}_{\operatorname{Sh}(\mathbf{k}_X)}(\mathcal F^p,\mathcal G^q)$、
全复形 (10.21)、有界性说明与导出张量——位于 PDF **p315 上半页**。原先 ch10a 止于 p314、
ch10b 从 p315 的 §10.5 标题起笔，导致 (10.21) 及这半页无人翻译，且 `ch10b-s01.tex:227`
对 (10.21) 的引用悬空。

**修复**：已将 p315 上半页补译到 `qsg/tex/ch10a-s04.tex` **末尾**（不新建文件、不写
`\chapter`），开头加 `% >>> p315`；公式 (10.21) 用 `\begin{equation}\tag{10.21}…`；
例 10.4.3 的 (ii)(iii) 仍在其环境内（
已把原 p314 处的 `\end{wexam}` 移到 p315 半页末尾的 `\hfill$//$` 之后），与 s04 前文
的 $Rf_\ast$、双函子、双复形记号衔接；末尾止于 §10.5 标题之前（未写 `\section`）。

**Tutor Note**：新增 1 条（全复形 (10.21) 的微分构造 $d=d_h+(-1)^p d_v$ 与有界性；
提示原文未写出微分、读者需自行补符号约定）。

**ranges.json**：`ch10a` 的 `pdf` 由 `[290,314]` 扩为 `[290,315]`、`printed` 由
`[282,306]` 改为 `[282,307]`（接缝页 p315 与 ch10b `[315,342]` 重叠，与 ch05a/ch05b
的接缝处理一致）；`ch10b` 未改动。

**自检**：`python qsg/tools/check.py ch10a` → PDF p290–p315 共 **26/26 页全覆盖**、
无缺页、无结构错误、无重复 tag（21 个，(10.1)–(10.21)）、无缺失图片；`check.py ch10b`
仍 28/28 页通过。单章试编译（preamble + ch10a-s03/s04）通过：8 页，零警告。


---

## 第 10 章（下）10.5–10.8

# 审校记录：第 10 章 10.5–10.6（PDF p315–p330）

范围：原书印刷页 307–322，扫描 PDF 第 315–330 页（本半）。
译文文件：`qsg/tex/ch10b-s01.tex`（§10.5，p315–p321）、
`qsg/tex/ch10b-s02.tex`（§10.6，p321–p330）。
注意：§10.5 起于 PDF p315 中部（p315 上半页为 §10.4 末尾，归 ch10a 译者）；
§10.6 起于 PDF p321 下部。本半**不写** `\chapter`。

公式编号：本半覆盖 (10.22)–(10.37)，共 16 个编号公式，全部按原文 `\tag` 手工标注。

---

## 一、已确认的疑误（正文已加批注，保留原文写法）

| # | 位置（印刷页 / PDF 页） | 原文 | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | 例 10.6.5，p.319 / p.327 | "Proposition 10.6.1 above does not apply directly since $N_f\subset X$ is a closed domain (with codimension 0)" | $N_f$ 由 (10.35) 定义在 $X\times\R$ 中，故此处应为 $N_f\subset X\times\R$；写 $N_f\subset X$ 是把 $X\times\R$ 误写成 $X$ | 改为 $N_f\subset X\times\R$（译文按原文保留并加注） |
| 2 | 例 10.6.5 与命题 10.6.2，p.319–p.320 / p.327 | 闭区域的余法丛写作 $\nu^*_ZX=\{(z,p)\mid z\in\partial Z,\ p(n(z))>0\}\cup\{\cdots p(n(z))<0\}$，命题 10.6.2 亦只写 $p(n(z))<0$（或 $>0$） | 按余法丛定义还应同时要求 $p\lvert_{T_z\partial Z}=0$（即 $p$ 沿法向），否则集合含带切向分量的余向量，维数大于 $\dim X$ | 读作 $p=c\,n(z)$（$c>0$ 或 $c<0$）；建议印刷时补上 $p\lvert_{T_z\partial Z}=0$ |

## 二、需人工确认的记号

| # | 位置 | 说明 |
|---|---|---|
| A | 习题 10.6.3，p.322 / p.330 | $\mathbf{k}_{\mathrm{var}\,\Delta}$ 中的「var $\Delta$」在本书中未给出定义（可能指对角线的某种「变体」），译文保留原样，请教授确认术语 |
| B | p.309 / p.317 | "sheaf cohomology groups $H^*(X;\cdot)=R^*\Gamma(X,\cdot)$" 两个上标都印作 $*$（分次记法）；与 §10.3 中 $H^i=R^i\Gamma$ 的逐次记法并用，阅读时勿混淆 |
| C | p.307 / p.315 | (10.22) 中写作 $H^*(C^{\bullet};\mathbf{k})$，其「$;\mathbf{k}$」是系数记号，与 (10.23) 中 $H^i$ 的层次不同 |
| D | p.321 / p.329 | 齐次性陈述写作 "$\varphi^t_{\widetilde H}$ 是 $T^*X\times T^*R$ 上的 $\R_+$-齐次…"，但同段其他处用加点记号 $\dot T^*\R=T^*\R\setminus0_\R$；建议统一为 $\dot T^*\R$ |

## 三、本半的图与交换图处理

原书编号插图共 5 幅，均按 300 dpi 从扫描页裁剪并经 `read_image` 验证：

| 图号 | 文件 | 印刷页 / PDF 页 |
|---|---|---|
| 图 10.5 | `figures/fig_p322_1.png` | p.314 / p.322 |
| 图 10.6 | `figures/fig_p324_1.png` | p.316 / p.324 |
| 图 10.7 | `figures/fig_p325_1.png` | p.317 / p.325 |
| 图 10.8 | `figures/fig_p326_1.png` | p.318 / p.326 |
| 图 10.9 | `figures/fig_p328_1.png` | p.320 / p.328 |

§10.5 中另有 3 处**交换图**（p.309 的提升图、p.310 的梯形图、p.312 的截断复形图）
以及 p.310 的双复形图 (10.27)。这些是交换图而非扫描插图，已用 `array` 环境
按原图结构重排（(10.27) 保留 `\tag{10.27}`）；若要求与扫描图逐像素一致，请复核。

## 四、跨范围事项（需 lead 协调）

- **PDF p331 顶部**包含 §10.6 的收尾：「To end this section, let us post the
  following questions…」与 **Question 10.6.2**。该内容属于 §10.6，但落在本半
  页码范围 p315–p330 之外，本半未译。应由续写 10.7–10.8 的译者一并补入
  （建议放在 §10.6 末尾、§10.7 标题之前），否则会漏译。

## 五、无法辨认的符号

无。p315–p330 已逐页核对；关键公式 (10.22)–(10.37) 及 p.322 的 (10.33)、
p.327 的余法丛、(10.35)–(10.37)、p.329–p.330 的 $\widetilde H$ 与 GKS 定理
均已放大逐符号核对。

---

# 审校记录：第 10 章 10.7–10.8（PDF p331–p342）

范围：原书印刷页 323–334，扫描 PDF 第 331–342 页。
译文文件：`qsg/tex/ch10b-s03.tex`（§10.7，p331–p338）、
`qsg/tex/ch10b-s04.tex`（§10.8，p338–p342）。
本半**不写** `\chapter`；p331 顶部为 §10.6 的收尾（Question 10.6.2），已按 lead
协调意见补译在 s03 开头、`% >>> p331` 之后，ch10b-s02 未重复。

公式编号：本半覆盖 (10.38)–(10.55)，共 18 个编号公式，全部按原文 `\tag` 手工标注。
原书编号插图仅 1 幅（图 10.10），已按 300 dpi 裁剪为
`figures/fig_p334_1.png` 并经 `read_image` 验证。

## 六、本半已确认的疑误（正文已加批注，保留原文写法）

| # | 位置（印刷页 / PDF 页） | 原文 | 疑点 | 建议改法 |
|---|---|---|---|---|
| 3 | 命题 10.7.1 的证明，p.324 / p.332 | "Then take the direct limit for $U\in\Op(X,x)$. **Then Definition 10.6.1. Then** (10.42) **improve** the long exact sequence (10.44) to be…" | "Then Definition 10.6.1." 是残缺句（缺谓语/介词），且 "improve" 缺第三人称单数 | 改为 "Then by Definition 10.6.1, (10.42) improves the long exact sequence (10.44) to be…"（译文按语义补足为「再由定义 10.6.1」） |
| 4 | 层复合的 SS 计算，p.328 / p.336 | $SS(\pi_{23}^{-1}\mathcal G)=\{(x_1,y_2,\mathbf y,0,\eta_2,\eta_3)\mid (y_2,y_3,\eta_2,\eta_3)\in SS(\mathcal G),\ x_1\in X_1\}$ | 第三个分量印作 $y$，但按定义它应是 $X_3$ 中的坐标，即 $y_3$；否则与后文拉格朗日对应 (10.49) 的元组结构不符 | 改为 $y_3$（译文保留原文 $y$ 并加批注） |
| 5 | 例 10.8.2，p.332 / p.340 | 断言 $H^0((-\infty,0);\mathcal F)\simeq H^0((-\infty,1);\mathcal F)(=\mathbf k)$ | 紧随其后的计算给出两端均为 $0$（正合列 $0\to H^0\to\mathbf k\xrightarrow{\mathbf 1_{\mathbf k}}\mathbf k$），并非 $\mathbf k$；"(= \mathbf k)" 与计算矛盾 | 删去 "(= \mathbf k)"，或改为 "(=0)"（译文保留原文并加批注） |
| 6 | 命题 10.8.1 的证明，p.333 / p.341 | "$SS(Rq_*\mathcal F)\subset0_{X\times I}$" | $Rq_*\mathcal F$ 是底空间 $I$ 上的层，其奇性支撑应落在 $T^*I$ 内，故应为 $0_I$；$0_{X\times I}$ 维数不符 | 改为 $SS(Rq_*\mathcal F)\subset0_I$（译文保留原文并加批注） |
| 7 | 图 10.10 引出句，p.326 / p.334 | "We can explicitly draw the right-hand side of (10.45) **by** Figure 10.10." | 介词用词不当，应为 "in Figure 10.10" | 改为 "in Figure 10.10"（译文按「用图 10.10」处理，不另加批注） |
| 8 | 命题 10.7.2，p.325 / p.333 | "Here, the pullback of the co-vector $f^*(\eta)$ means that for any $v\in T^*Y$, we have $f^*(\eta)(v)=\eta(f_*(v))$." | $f^*(\eta)$ 是 $X$ 上的余向量，应与 \emph{切}向量配对；$v$ 应取在 $T_xX$，$f_*(v)$ 才有意义。原文 $v\in T^*Y$ 系笔误 | 改为 $v\in T_xX$（译文保留原文并加批注） |
| 9 | 命题 10.8.1 的证明，p.333 / p.341 | "This **in return** implies that $R\Gamma(X,\mathcal F|_{t=0})=R\Gamma(X,\mathcal F|_{t=1})$." | 应为 "in turn"（进而） | 改为 "in turn"（译文按「这又意味着」处理，不另加批注） |

## 七、记号与术语说明（非原文错误）

| 记号 | 说明 |
|---|---|
| `\dot T^*X` | 去零截面的余切丛 $T^*X\setminus0_X$；与 ch10b-s02 的约定一致 |
| $SS(\mathcal G)^a$ | 命题 10.7.3 (ii) 中上标 $a$ 专指「把余向量整体变号」，即 $SS(\mathcal G)^a=\{(x,-\eta)\mid(x,\eta)\in SS(\mathcal G)\}$；与 $-SS(\mathcal G)$ 的写法不同，校样时勿混 |
| $\Gamma_Z$ | 定义 10.7.1 中的新函子（式 (10.38)）；$Z$ 开时为正合，$Z$ 闭时仅左正合，故须写导出函子 $R\Gamma_Z$ |
| (10.44) 的三角形 | 原书排成三角交换图形；译文按 Mayer--Vietoris 长正合列的线性形式重排（同一序列），未裁剪为图 |
| 「传播」 | propagates 统一译「传播」；"propagates from $a$ to $b$" 译「从 $a$ 传播到 $b$」，与 ch10b-s02 一致 |
| Arnold--Givental | 人名保留拉丁字母；定理 10.8.1 标题译「余切丛上的 Arnold--Givental 猜想」 |

## 八、本半交叉引用核对清单

- (10.38)–(10.51) 属 §10.7；其中 (10.39)、(10.41)--(10.44) 为长正合列与
  Mayer--Vietoris 论证，(10.45) 为 $SS(R\pi_*\mathcal F)$ 的上界，
  (10.46) 层卷积、(10.48) 层复合、(10.49) 拉格朗日对应、(10.50) 函子性、
  (10.51) GKS 层量子化的 $SS$ 控制。
- (10.52)–(10.55) 属 §10.8；引理 10.8.1 的 (10.52)、定理 10.8.2 证明中的
  (10.53)、命题 10.8.2 的 (10.55)，以及 (10.54) 的时间重参数化。
- 文中引用：定理 10.5.1、推论 10.1.1、定理 10.6.1（含 (i)(ii)）、例 10.6.1--10.6.5、
  例 10.5.5、命题 10.7.2/10.7.3、定义 10.6.1/10.7.1、引理 10.8.1、
  定理 10.8.1/10.8.2、命题 10.8.1/10.8.2，以及 5.2/5.3 节的
  例 5.2.1、例 5.2.2、猜想 5.3.1、猜想 5.3.2、定理 1.5.1；均照原书编号，未作改动。
- 原书图 10.7 为 §10.6 所引（p.332 例 10.8.2 引用），图 10.10 为本半唯一插图。

## 九、无法辨认的符号

无。p331–p342 已逐页核对；关键公式 (10.38)–(10.55)、p.336 的层复合计算、
p.338 的 (10.51)、p.342 的提升公式与 $\nu_N^*(M\times\R)$ 均已放大逐符号核对。
