# 自同构群 $\operatorname{Aut}(\mathcal D_X,i_X)$

> `mloc/concept/automorphism-group-of-dx` · type=concept · track=A · status=draft · verification=source-only

**别名**：automorphism group of the sheaf of differential operators、$\operatorname{Aut}(\mathcal D_X,i_X)$、闭 1-形式的参数化

## 摘要

自同构由闭 $1$-形式 $\omega$ 决定：$\varphi(\xi)=\xi-\omega(\xi)$，且 $\mathrm{Aut}(\mathcal D_X,i_X)\cong Z^1(X)$。

## 问题

保持 $\mathcal O_X$ 的 $\mathcal D_X$ 自同构有多少个，它们被什么数据完全决定？

## 定义

$\operatorname{Aut}(\mathcal D_X,i_X)$ 指满足 $\varphi\circ i_X=i_X$ 的 $k$-代数层自同构 $\varphi$ 构成的乘法群；$Z^1(X)=\Gamma(X,Z^1_X)$ 是闭 $1$-形式在加法下构成的群。第 1 章引理 1.1 与第 1 章引理 1.2 合起来说：对应 $\varphi\mapsto\omega$（其中 $\omega(\xi)=-\varphi(\xi)(1)$，$\xi\in T_X$）是这两个群之间的同构，逆映射为 $\omega\mapsto\varphi_\omega$，$\varphi_\omega(\xi)=\xi-\omega(\xi)$。

记号：$\omega(\xi)=-\varphi(\xi)(1)$；$\operatorname{Gr}\varphi$：$\mathcal D_X$ 阶数滤过的分次部分；$[\ ,\ ]$：换位子；$Z^1(X)$ 用加法记号。

## 要点

- $\varphi$ 在 $\mathcal O_X$ 上是恒等，故 $[\varphi(\xi),f]=\xi(f)$；由此 $\varphi(\xi)(f)=\xi(f)+f\varphi(\xi)(1)$，可见 $\varphi$ 与「原向量场」只差一个乘函数的修正项。
- 修正项 $\omega(\xi)=-\varphi(\xi)(1)$ 自动是 $1$-形式；$\varphi$ 与换位子相容迫使 $d\omega=0$——闭性不是额外假设，是由函子性逼出来的。
- $\varphi$ 保持 $\mathcal D_X$ 的阶数滤过且 $\operatorname{Gr}\varphi=\mathrm{id}$，故 $\varphi$ 可逆；所以 $(D_X,i_X)$ 的「自同态」自动是「自同构」。
- 反向：任意闭 $1$-形式 $\omega$ 通过 $\varphi(\xi)=\xi-\omega(\xi)$ 延拓成自同构；$d\omega=0$ 恰好是保持换位子所需的全部条件。
- 同构把「加法群」与「乘法群」对上：$\varphi_{\omega_1}\circ\varphi_{\omega_2}=\varphi_{\omega_1+\omega_2}$，故 $Z^1(X)$ 的加法对应自同构的复合。

## 公式

$$\varphi(\xi)=\xi-\omega(\xi),\qquad \omega(\xi)=-\varphi(\xi)(1)$$

$$\varphi(\xi)(f)=\xi(f)+f\,\varphi(\xi)(1)$$

$$d\omega(\xi\wedge\eta)=\xi(\omega(\eta))-\eta(\omega(\xi))-\omega([\xi,\eta])=0$$

$$\operatorname{Aut}(\mathcal D_X,i_X)\xrightarrow{\ \sim\ }Z^1(X)$$

$$\varphi_{\omega_1}\circ\varphi_{\omega_2}=\varphi_{\omega_1+\omega_2}$$

## 相关定理

### 第 1 章引理 1.1（自同态由闭 $1$-形式决定）

设 $\varphi$ 是 $(\mathcal D_X,i_X)$ 的自同态。则存在 $X$ 上的闭 $1$-形式 $\omega$，使得对任意局部向量场 $\xi\in T_X$ 有 $\varphi(\xi)=\xi-\omega(\xi)$，并且 $\varphi$ 由 $\omega$ 完全确定。特别地，$\varphi$ 是 $(\mathcal D_X,i_X)$ 的自同构。

证明状态：`complete`

1. 对 $f\in\mathcal O_X$、$\xi\in T_X$ 有 $[\varphi(\xi),f]=[\varphi(\xi),\varphi(f)]=\varphi([\xi,f])=\xi(f)$。
   - 为什么：$\varphi$ 是保持 $i$ 的代数层态射，它固定 $\mathcal O_X$ 且保持换位子。
2. 把上式作用于 $1$，得 $\varphi(\xi)(f)=\xi(f)+f\varphi(\xi)(1)$；令 $\omega(\xi)=-\varphi(\xi)(1)$，即 $\varphi(\xi)=\xi-\omega(\xi)$。
   - 为什么：由第 1 步移项：$f\varphi(\xi)(1)$ 就是与 $\xi$ 的差，而 $\omega$ 在函数上是 $\mathcal O_X$-线性的，故是 $1$-形式。
3. 展开 $\omega([\xi,\eta])=-\varphi([\xi,\eta])(1)$，用 $\varphi$ 保持换位子及第 2 步，得 $\omega([\xi,\eta])=\xi(\omega(\eta))-\eta(\omega(\xi))$。
   - 为什么：$\varphi([\xi,\eta])=\varphi(\xi)\varphi(\eta)-\varphi(\eta)\varphi(\xi)$，再把每一项按 $\varphi=\mathrm{id}-\omega$ 展开并作用于 $1$。
4. 于是 $d\omega(\xi\wedge\eta)=0$，即 $\omega$ 闭。
   - 为什么：第 3 步的恒等式正是 $d\omega=0$ 的坐标展开。
5. $\varphi$ 保持阶数滤过且 $\operatorname{Gr}\varphi=\mathrm{id}$，故 $\varphi$ 是自同构。
   - 为什么：滤过自同态若分次部分可逆，则逐阶归纳得 $\varphi$ 可逆（$\mathcal D_X$ 的滤过穷尽且各阶片段有限生成）。

### 第 1 章引理 1.2（$\operatorname{Aut}(\mathcal D_X,i_X)\cong Z^1(X)$）

自然态射 $\operatorname{Aut}(\mathcal D_X,i_X)\to Z^1(X)$ 是同构。

证明状态：`complete`

1. 单射：由第 1 章引理 1.1，$\varphi$ 由 $\omega(\xi)=-\varphi(\xi)(1)$ 完全确定，故对应是单的。
   - 为什么：$\varphi$ 在 $T_X$ 上已由 $\omega$ 的值唯一确定，而 $T_X$ 与 $\mathcal O_X$ 生成 $\mathcal D_X$。
2. 满射：给定闭 $1$-形式 $\omega$，定义 $\varphi(\xi)=\xi-\omega(\xi)$（$\xi\in T_X$）；它与 $\mathcal O_X$ 的换位子关系以及 $\varphi([\xi,\eta])=[\varphi(\xi),\varphi(\eta)]$ 都成立。
   - 为什么：前者由 $\varphi(f\xi)=f\varphi(\xi)$ 保证，后者正是 $d\omega=0$ 的重写。
3. 故 $\varphi$ 可延拓为 $(\mathcal D_X,i_X)$ 的自同态；由第 1 章引理 1.1，它实际是自同构。
   - 为什么：$\mathcal D_X$ 由 $\mathcal O_X$ 与 $T_X$ 生成，故在这两部分上给定且相容的映射唯一延拓成代数层态射。
4. 同态性：$\varphi_{\omega_1}\circ\varphi_{\omega_2}(\xi)=\xi-(\omega_1+\omega_2)(\xi)$，即复合对应加法。
   - 为什么：直接代入，两个修正项相加；这同时说明逆映射是 $\omega\mapsto-\omega$。

## 易错点

- 第 1 章引理 1.1 的 $\omega$ 是 $-\varphi(\xi)(1)$ 而不是 $\varphi(\xi)(1)$；符号弄反会使所有 $t$ 的公式差一个负号（与第 1 章命题 1.13 的 $-t$ 对照）。
- 「自同态自动是自同构」用的是 $\operatorname{Gr}\varphi=\mathrm{id}$ 与滤过的性质，不是抽象的环论：$\mathcal D_X$ 是非交换无限维环，一般自同态不必可逆。
- $Z^1(X)$ 是加法群：两个闭形式相加对应两个自同构复合；写成乘法时容易把 $\omega_1+\omega_2$ 误作 $\omega_1\omega_2$。

## 相关卡

- `mloc/concept/twisted-sheaf-of-differential-operators`
- `mloc/concept/twisting-invariant-t`
- `mloc/concept/dual-twisted-sheaf`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[1]（PDF [5]） · `源码/chapters/ch01.tex:13-32（第 1 章引理 1.1 及其证明）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[2]（PDF [6]） · `源码/chapters/ch01.tex:36-49（第 1 章引理 1.2 及其证明）`
