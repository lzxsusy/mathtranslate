# 扭化不变量 $t(\mathcal D)$

> `mloc/concept/twisting-invariant-t` · type=concept · track=A · status=draft · verification=source-only

**别名**：twisting invariant、$t(\mathcal D)$、扭层的上同调类、Cech 上闭链

## 摘要

局部平凡化给出的闭 $1$-形式上闭链定义出 $t(\mathcal D)\in H^1(X,Z^1_X)$，它与平凡化无关；用线丛扭时加 $d\log$，沿态射拉回时变成 $Z^1(\phi)$。

## 问题

怎样从一个扭层算出一个只依赖同构类的不变量，它在用线丛扭与沿态射拉回时如何变化？

## 定义

对扭层 $(\mathcal D,i)$ 取开覆盖 $\mathcal U=(U_j)$ 与局部同构 $\psi_j:(\mathcal D,i)|_{U_j}\to(\mathcal D_{U_j},i_{U_j})$；过渡自同构 $\varphi_{jk}=\psi_j\psi_k^{-1}$ 由第 1 章引理 1.2 对应闭 $1$-形式 $\omega_{jk}\in Z^1(U_j\cap U_k)$。三重叠上 $\varphi_{jl}=\varphi_{jk}\circ\varphi_{kl}$ 给出 $\omega_{jl}=\omega_{jk}+\omega_{kl}$，即 $\omega=(\omega_{jk})\in Z^1(\mathcal U,Z^1_X)$；换局部平凡化只把 $\omega$ 换成 $\omega+d\rho$。于是得到与平凡化无关的类 $t(\mathcal D,i)\in H^1(X,Z^1_X)$。

记号：$Z^1_X$：闭 $1$-形式层；$H^1(X,Z^1_X)$：以 $Z^1_X$ 为系数的第一 Čech 上同调；$d\log:\mathcal O_X^*\to Z^1_X$，$f\mapsto f^{-1}df$；$\operatorname{Pic}(X)=H^1(X,\mathcal O_X^*)$；$i(L)$：$L$ 的类；$Z^1(\phi):H^1(Y,Z^1_Y)\to H^1(X,Z^1_X)$。

## 要点

- 上闭链是加法记号的：$\omega_{jl}=\omega_{jk}+\omega_{kl}$（不是乘法），换平凡化时 $\omega'=\omega+d\rho$；与线丛的上闭链 $s_{jl}=s_{jk}s_{kl}$ 对照时不要混淆群运算。
- $d\log(f)=f^{-1}df$ 把 $\mathcal O_X^*$ 的乘法翻译成闭 $1$-形式的加法，$H^1(d\log)$ 把 Picard 群送进 $H^1(X,Z^1_X)$。
- 第 1 章命题 1.4：$t(\mathcal D_L)=H^1(d\log)(i(L))$——用线丛 $L$ 扭时 $t$ 正好加上 $L$ 的 $d\log$ 像；特别地 $t(\mathcal D_X)=0$。
- 第 1 章命题 1.5：$t(\mathcal D_\phi)=Z^1(\phi)(t(\mathcal D))$，即 $t$ 与态射拉回相容；这是 $t$ 作为「上同调类」而非「任意不变量」的标志。
- $t$ 是完备不变量：第 1 章定理 1.3 说 $t$ 是单射，同构类由 $t$ 完全决定（构造与单射的细节见「扭微分算子层」一卡）。

## 公式

$$\omega_{jl}=\omega_{jk}+\omega_{kl}$$

$$\omega'=\omega+d\rho,\qquad \rho\in C^0(\mathcal U,Z^1_X)$$

$$d\log f=f^{-1}df$$

$$t(\mathcal D_L)=H^1(d\log)(i(L))$$

$$t(\mathcal D_\phi)=Z^1(\phi)(t(\mathcal D))$$

## 相关定理

### 第 1 章命题 1.4（线丛扭的 $t$）

对 $X$ 上任意可逆 $\mathcal O_X$-模 $L$，$t(\mathcal D_L)=H^1(d\log)(i(L))$。

证明状态：`complete`

1. 取开覆盖 $\mathcal U=(U_i)$ 使 $L|_{U_i}\cong\mathcal O_X|_{U_i}$，取同构 $\alpha_i:L|_{U_i}\to\mathcal O_X|_{U_i}$，令 $s_{jk}=\alpha_j\alpha_k^{-1}(1)\in\mathcal O_X^*(U_j\cap U_k)$；则 $(s_{jk})$ 是代表 $i(L)$ 的 $1$-上闭链。
   - 为什么：可逆层的过渡函数给出上闭链：$\alpha_j=s_{jk}\alpha_k$，而 $s_{jl}=s_{jk}s_{kl}$ 即 $i(L)$ 的余圈条件。
2. $\alpha_i$ 通过 $\psi_i(u)=\alpha_i\circ u\circ\alpha_i^{-1}$ 给出 $(\mathcal D_L)|_{U_i}\to\mathcal D_X|_{U_i}$ 的同构。
   - 为什么：共轭把 $L$ 的微分自同态层搬到 $\mathcal O_X$ 的微分自同态层，即 $\mathcal D_X$。
3. 由 $\psi_j(u)(f)=s_{jk}\psi_k(u)(s_{jk}^{-1}f)$ 得 $\psi_j(u)=s_{jk}\psi_k(u)s_{jk}^{-1}$，故 $\varphi_{jk}(D)=s_{jk}Ds_{jk}^{-1}$。
   - 为什么：直接代入 $\alpha_j=s_{jk}\alpha_k$ 并整理。
4. 作用在向量场：$\varphi_{jk}(\xi)=s_{jk}\xi s_{jk}^{-1}=\xi-s_{jk}^{-1}\xi(s_{jk})$，故 $\omega_{jk}=s_{jk}^{-1}ds_{jk}=d\log s_{jk}$。
   - 为什么：$s\xi s^{-1}=\xi-s^{-1}\xi(s)$ 是 $s^{-1}(\xi s)$ 的标准恒等式；$\omega_{jk}$ 正是 $d\log s_{jk}$。
5. 于是代表 $t(\mathcal D_L)$ 的上闭链是 $(d\log s_{jk})$，即 $H^1(d\log)(i(L))$。
   - 为什么：$d\log$ 是群层同态，作用在 $(s_{jk})$ 上给出以 $Z^1_X$ 为系数的上闭链。

### 第 1 章命题 1.5（与态射拉回相容）

设 $\phi:X\to Y$ 是光滑代数簇的态射，$\mathcal D$ 是 $Y$ 上的扭微分算子层。则 $t(\mathcal D_\phi)=Z^1(\phi)(t(\mathcal D))$。

证明状态：`complete`

1. 取 $Y$ 的开覆盖 $\mathcal U=(U_i)$ 与局部同构 $\psi_i:(\mathcal D,i)|_{U_i}\to(\mathcal D_Y,i_Y)|_{U_i}$（底本校注指出这里必须是 $Y$ 的覆盖），令 $V_i=\phi^{-1}(U_i)$ 覆盖 $X$。
   - 为什么：$\mathcal D$ 是 $Y$ 上的层，只有 $Y$ 的覆盖才能平凡化它；$V_i$ 才是 $X$ 的覆盖。
2. 提升 $\phi^\#(\psi_i)$ 给出 $(\mathcal D_\phi,i_\phi)|_{V_i}\to(\mathcal D_X,i_X)|_{V_i}$ 的同构，且 $\phi^\#(\psi_j)=\phi^\#(\varphi_{jk})\circ\phi^\#(\psi_k)$。
   - 为什么：提升的定义 $\phi^\#(\psi)(z)=\phi^*(\psi)\,z\,\phi^*(\psi^{-1})$ 保持复合，故过渡自同构随之提升。
3. 若 $\varphi_{jk}$ 对应 $Y$ 上的 $\omega_{jk}$，则 $\phi^\#(\varphi_{jk})$ 对应 $\phi^*\omega_{jk}$（在 $X$ 上）；于是 $X$ 上的上闭链是 $(\phi^*\omega_{jk})$。
   - 为什么：把 $\varphi(\xi)=\xi-\omega(\xi)$ 沿 $\phi$ 拉回，$\phi^*\omega$ 与提升后的自同构相伴——这正是讲义中逐项计算 $-\omega(\phi^{-1}\partial_i)$ 的结论。
4. $\omega\mapsto\phi^*\omega$ 诱导层态射 $\phi^{-1}(Z^1_Y)\to Z^1_X$，进而给出 $Z^1(\phi):H^1(Y,Z^1_Y)\to H^1(X,Z^1_X)$，故 $t(\mathcal D_\phi)=Z^1(\phi)(t(\mathcal D))$。
   - 为什么：上同调由层上链复形计算，层态射诱导上同调映射；此处取 $p=1$。

## 易错点

- 上闭链是加法记号（$\omega_{jl}=\omega_{jk}+\omega_{kl}$），而线丛的上闭链是乘法记号（$s_{jl}=s_{jk}s_{kl}$）；$d\log$ 正是把后者翻译成前者的桥。
- $t(\mathcal D_L)=H^1(d\log)(i(L))$ 中的 $H^1(d\log)$ 是上同调层面的映射，不是逐点的 $d\log$；不要在覆盖上把 $i(L)$ 与 $\omega$ 直接相加。
- 第 1 章命题 1.5 的 $Z^1(\phi)$ 方向是 $H^1(Y)\to H^1(X)$（沿 $\phi$ 拉回），别写成 $X\to Y$。

## 相关卡

- `mloc/concept/twisted-sheaf-of-differential-operators`
- `mloc/concept/automorphism-group-of-dx`
- `mloc/concept/twist-by-line-bundle`
- `mloc/concept/dual-twisted-sheaf`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[3]（PDF [7]） · `源码/chapters/ch01.tex:85-135（第 1 章定理 1.3、第 1 章命题 1.4 及证明）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[5]（PDF [9]） · `源码/chapters/ch01.tex:177-180（第 1 章命题 1.5）`
