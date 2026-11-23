# 用线丛扭

> `mloc/concept/twist-by-line-bundle` · type=concept · track=A · status=draft · verification=source-only

**别名**：twist of a twisted sheaf by an invertible module、$\mathcal D_L$、可逆模扭

## 摘要

用线丛扭：$\mathcal D_L$ 是 $L\otimes\mathcal D$ 的微分自同态层，$t(\mathcal D_L)=t(\mathcal D)+H^1(d\log)(i(L))$。

## 问题

怎样用线丛把一个扭层再扭一次，为什么扭两次等于用张量积扭，而 $t$ 的变化正好是 $d\log$ 的像？

## 定义

把 $\mathcal D$ 看作关于左乘的 $\mathcal O_X$-模，作 $L\otimes_{\mathcal O_X}\mathcal D$；它对第二个因子上的右乘是右 $\mathcal D$-模，故可取其局部微分自同态层 $\mathcal D_L$。$\mathcal D_L$ 是 $k$-代数层，$L\otimes\mathcal D$ 的 $\mathcal O_X$-模结构给出 $i_L:\mathcal O_X\to\mathcal D_L$。局部化到 $L|_U\cong\mathcal O_X|_U$ 上可见 $\mathcal D_L|_U\cong\mathcal D_X|_U$，故 $(\mathcal D_L,i_L)$ 是扭层，称为 $\mathcal D$ 关于 $L$ 的扭。

记号：$(\mathcal D_L,i_L)$；$i(L)\in H^1(X,\mathcal O_X^*)$；$H^1(d\log)$；$d\log s=s^{-1}ds$；$\mathcal D_L=\varinjlim_n\operatorname{Diff}_n(L,L)$。

## 要点

- $\mathcal D_L$ 的构造只用 $L$ 的可逆性（局部 $\cong\mathcal O_X$），不需要 $L$ 上的联络或平坦结构；$d\log$ 作用在过渡函数上，而不是作用在 $L$ 的截面上。
- 第 1 章引理 1.7：$(\mathcal D_X)_L\cong\mathcal D_L$，即用线丛扭 $\mathcal D_X$ 得到的正是 $L$ 的微分自同态层——这给出扭的「几何」实现。
- 第 1 章命题 1.8 的加法公式：$t(\mathcal D_L)=t(\mathcal D)+H^1(d\log)(i(L))$；取 $\mathcal D=\mathcal D_X$（$t=0$）即第 1 章命题 1.4。
- 第 1 章命题 1.9：$(\mathcal D_L)_{L'}\cong\mathcal D_{L'\otimes L}$，扭的合成对应线丛的张量积；与第 1 章命题 1.8 相容：$d\log$ 是群同态。
- 第 1 章命题 1.10：$(\mathcal D_L)_\phi\cong(\mathcal D_\phi)_{\phi^*(L)}$——扭与逆像可交换，这条在第 2 章把扭层沿轨道搬运时反复用到。

## 公式

$$L\otimes_{\mathcal O_X}\mathcal D\ \text{的局部微分自同态层}\ \mathcal D_L$$

$$t(\mathcal D_L)=t(\mathcal D)+H^1(d\log)(i(L))$$

$$(\mathcal D_L)_{L'}\cong\mathcal D_{L'\otimes_{\mathcal O_X}L}$$

$$(\mathcal D_L)_\phi\cong(\mathcal D_\phi)_{\phi^*(L)}$$

$$\mathcal D_L=\varinjlim_n\operatorname{Diff}_n(L,L)$$

## 相关定理

### 第 1 章引理 1.7（$(\mathcal D_X)_L\cong\mathcal D_L$）

设 $L$ 是光滑代数簇 $X$ 上的可逆 $\mathcal O_X$-模。则微分算子层 $\mathcal D_X$ 的扭 $(\mathcal D_X)_L$ 自然同构于 $\mathcal D_L$。

证明状态：`complete`

1. 设 $I_X$ 是 $\mathcal D_X$ 中由 $T_X$ 生成的左理想，有 $\mathcal O_X$-模正合列 $0\to I_X\to\mathcal D_X\to\mathcal O_X\to0$；与 $L$ 张量得 $0\to L\otimes I_X\to L\otimes\mathcal D_X\to L\to0$。
   - 为什么：$\mathcal D_X/\mathcal D_XT_X\cong\mathcal O_X$（由 $T_X$ 与 $\mathcal O_X$ 生成 $\mathcal D_X$ 且阶数 0 部分为 $\mathcal O_X$）；$L$ 可逆故张量保持正合。
2. 该正合列是 $(\mathcal D_X)_L$-模的正合列，因此存在从 $(\mathcal D_X)_L$ 到 $\mathcal D_L$ 的自然态射。
   - 为什么：$\mathcal D_L$ 是微分自同态层：右 $\mathcal D_X$-模 $L\otimes\mathcal D_X$ 的自同态由它在 $L$ 上的作用刻画，正合列给出这个作用。
3. 局部取 $L\cong\mathcal O_X$，两边都化为 $\mathcal D_X$，故该态射在每个局部模型上可逆：$\operatorname{Gr}$ 部分为恒等。
   - 为什么：$\operatorname{Gr}$ 是 $\mathcal O_X$-线性的，局部平凡化把两边同时送到 $\mathcal D_X$，故 $\operatorname{Gr}$ 为同构。
4. 由第 1 章引理 1.1，扭层之间的态射若 $\operatorname{Gr}$ 为恒等则是同构。
   - 为什么：第 1 章引理 1.1 说明 $(D_X,i_X)$ 的任何自同态都自动可逆；局部可逆 + 滤过相容即整体同构。

### 第 1 章命题 1.8（$t$ 的加法公式）

设 $\mathcal D$ 是光滑代数簇 $X$ 上的扭微分算子层，$L$ 是可逆 $\mathcal O_X$-模。则 $t(\mathcal D_L)=t(\mathcal D)+H^1(d\log)(i(L))$。

证明状态：`complete`

1. 取开覆盖 $\mathcal U=(U_i)$ 与同构 $\alpha_i:L|_{U_i}\to\mathcal O_X|_{U_i}$、$\psi_i:(\mathcal D,i)|_{U_i}\to(\mathcal D_X,i_X)|_{U_i}$，令 $s_{jk}=\alpha_j\alpha_k^{-1}(1)$。
   - 为什么：可逆层与扭层可同时局部平凡化，取公共加细即可。
2. 令 $\sigma_i=\alpha_i\otimes\psi_i:(L\otimes\mathcal D)|_{U_i}\to\mathcal D_X|_{U_i}$，它是 $\mathcal O_X$-模同构且与右 $\mathcal D$-作用相容；由 $T\mapsto T(1)$ 得 $\tau_i:\mathcal D_L|_{U_i}\to\mathcal D_X|_{U_i}$。
   - 为什么：$T\mapsto T(1)$ 把「看作右 $\mathcal D_X$-模的 $\mathcal D_X$」的微分自同态与 $\mathcal D_X$ 等同，故 $\tau_i$ 是自然同构。
3. 计算得 $\tau_j(u)=s_{jk}\varphi_{jk}(\tau_k(u))s_{jk}^{-1}$；令 $\rho_{jk}(v)=s_{jk}\varphi_{jk}(v)s_{jk}^{-1}$，则 $\tau_j=\rho_{jk}\circ\tau_k$。
   - 为什么：把 $\sigma_j(s\otimes v)=s_{jk}\varphi_{jk}(\sigma_k(s\otimes v))$ 代入 $\tau_j$ 的定义并整理。
4. 对 $\xi\in T_X$ 计算 $\rho_{jk}(\xi)=s_{jk}(\xi-\omega_{jk}(\xi))s_{jk}^{-1}=\xi-s_{jk}^{-1}ds_{jk}(\xi)-\omega_{jk}(\xi)$。
   - 为什么：用 $s\xi s^{-1}=\xi-s^{-1}\xi(s)$ 并把 $s^{-1}ds$ 与 $\omega_{jk}$ 相加。
5. 故 $\mathcal D_L$ 的上闭链是 $\omega_{jk}+s_{jk}^{-1}ds_{jk}$，即 $t(\mathcal D_L)=t(\mathcal D)+H^1(d\log)(i(L))$。
   - 为什么：两条上闭链逐项相加，对应上同调类相加；$s_{jk}^{-1}ds_{jk}=d\log s_{jk}$。

### 第 1 章命题 1.9（扭的合成）

设 $\mathcal D$ 是 $X$ 上的扭微分算子层，$L,L'$ 是可逆 $\mathcal O_X$-模。则 $(\mathcal D_L)_{L'}$ 自然同构于 $\mathcal D_{L'\otimes L}$。

证明状态：`complete`

1. 有 $\mathcal O_X$-模与右 $\mathcal D$-模的同构 $L'\otimes L\otimes\mathcal D=(L'\otimes\mathcal D_L)\otimes_{\mathcal D_L}(L\otimes\mathcal D)$。
   - 为什么：张量积的结合律；$\mathcal D_L$ 的定义就是 $L\otimes\mathcal D$ 的微分自同态层，故右作用相容。
2. 故 $(\mathcal D_L)_{L'}$ 在第一个因子上的右作用与 $\mathcal D$ 的右作用交换，给出自然态射 $(\mathcal D_L)_{L'}\to\mathcal D_{L'\otimes L}$。
   - 为什么：微分自同态的函子性：右模同构诱导自同态层的映射。
3. 局部两边的模型都是 $\mathcal D_X$，态射的 $\operatorname{Gr}$ 为恒等；由第 1 章引理 1.1 它是同构。
   - 为什么：局部平凡化下 $L,L'$ 都可逆，同构逐块验证，$\operatorname{Gr}$ 恒等保证整体可逆。

## 易错点

- $\mathcal D_L$ 不是 $L\otimes\mathcal D$ 本身，而是它的微分自同态层；$L\otimes\mathcal D$ 只是右 $\mathcal D$-模，本身不是环层。
- 第 1 章命题 1.8 的加法是 $H^1(X,Z^1_X)$ 中的加法；若误写成乘法或把 $d\log$ 当成 $\operatorname{Pic}$ 中的运算，符号会全错。
- 第 1 章命题 1.10 里必须写 $\phi^*(L)$ 而不是 $L$：扭与逆像交换时线丛要沿 $\phi$ 拉回。

## 相关卡

- `mloc/concept/twisting-invariant-t`
- `mloc/concept/twisted-sheaf-of-differential-operators`
- `mloc/concept/dual-twisted-sheaf`
- `dmod/concept/inverse-image-functor`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[6]（PDF [10]） · `源码/chapters/ch01.tex:200-221（扭的构造、第 1 章引理 1.7、第 1 章命题 1.8）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[7]（PDF [11]） · `源码/chapters/ch01.tex:250-264（第 1 章命题 1.9 与命题 1.10）`
