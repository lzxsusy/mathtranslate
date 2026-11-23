# 扭微分算子层

> `mloc/concept/twisted-sheaf-of-differential-operators` · type=concept · track=A · status=draft · verification=source-only

**别名**：twisted sheaf of differential operators、扭层、$(\mathcal D,i)$

## 摘要

带结构映射 $i:\mathcal O_X\to A$ 的代数层，局部同构于 $(\mathcal D_X,i_X)$；扭的自由度全在 $i$ 上，同构类由 $H^1(X,Z^1_X)$ 分类。

## 问题

两个层局部都同构于 $\mathcal D_X$，它们的差别究竟在哪里，为什么这些差别恰好被 $H^1(X,Z^1_X)$ 分类？

## 定义

设 $X$ 是特征 $0$ 的代数闭域 $k$ 上的光滑代数簇。考虑二元组 $(A,i)$，其中 $A$ 是 $X$ 上带单位元的结合 $k$-代数层，$i:\mathcal O_X\to A$ 是保持单位元的 $k$-代数态射；二元组的态射要求与 $i$ 交换。$(\mathcal D_X,i_X)$ 本身是这样一个对象（$i_X$ 是自然包含）。若 $X$ 有开覆盖 $\{U\}$，使每个 $(\mathcal D|_U,i|_U)$ 都与 $(\mathcal D_U,i_U)$ 同构，则称 $(\mathcal D,i)$ 是 $X$ 上的扭微分算子层。这里的同构必须是 $k$-代数层同构 $\psi$，并且满足 $\psi\circ i=i_U$——只要求「环层同构」是不够的。

记号：$(\mathcal D,i)$：扭层；$i_X:\mathcal O_X\to\mathcal D_X$：自然包含；$T_X$：切层；$Z^1_X$：闭 $1$-形式构成的层；$Z^1(X)=\Gamma(X,Z^1_X)$。

## 要点

- 「扭」就是换一个 $i$：$A$ 作为抽象 $k$-代数层局部固定为 $\mathcal D_X$，允许改变的只是结构映射 $i$；把 $i$ 换成 $i^{\prime}$ 而保持乘法不变，等价于把向量场的提升改成 $\xi\mapsto\xi-\omega(\xi)$（$\omega\in Z^1(X)$），这正是第 1 章引理 1.1 的内容。
- 局部同构必须同时匹配 $i$，所以「$\mathcal D$ 与 $\mathcal D_X$ 作为环层同构」本身不构成扭层的数据；数据是那个与 $i$ 相容的局部同构族。
- 扭的粘合数据是闭 $1$-形式的上闭链：三重叠上 $\omega_{jl}=\omega_{jk}+\omega_{kl}$，换局部平凡化时 $\omega'=\omega+d\rho$，故给出 $H^1(X,Z^1_X)$ 中一个类（第 1 章定理 1.3）。
- $\mathcal D_X$ 自身（$i=i_X$）对应 $0\in H^1(X,Z^1_X)$；用可逆层 $L$ 扭得的 $\mathcal D_L$ 对应 $H^1(d\log)(i(L))$（第 1 章命题 1.4）。
- 扭不改变分次环层：仍有 $\operatorname{Gr}\mathcal D\cong S(T_X)$，改变的只是 $T_X$ 嵌入 $\mathcal D$ 的方式；因此 $\mathcal D$ 作为 $\mathcal O_X$-模局部自由，阶数滤过与 $\mathcal D_X$ 的一致。

## 公式

$$(\mathcal D|_U,i|_U)\cong(\mathcal D_U,i_U)$$

$$\psi\circ i=i_U$$

$$\xi\mapsto\xi-\omega(\xi)\qquad(\omega\in Z^1(X))$$

$$t(\mathcal D,i)\in H^1(X,Z^1_X)$$

$$t(\mathcal D_X,i_X)=0$$

## 相关定理

### 第 1 章定理 1.3（扭层的分类）

映射 $t$ 给出 $X$ 上扭微分算子层的同构类与 $H^1(X,Z^1_X)$ 的元素之间的双射。

证明状态：`complete`

1. 取开覆盖 $\mathcal U=(U_j)$ 与局部同构 $\psi_j:(\mathcal D,i)|_{U_j}\to(\mathcal D_{U_j},i_{U_j})$，过渡自同构为 $\varphi_{jk}=\psi_j\psi_k^{-1}$；由第 1 章引理 1.2，$\varphi_{jk}$ 由闭 $1$-形式 $\omega_{jk}\in Z^1(U_j\cap U_k)$ 完全决定。
   - 为什么：第 1 章引理 1.2 把「保持 $i$ 的自同构」与「闭 $1$-形式」一一对应，因此过渡数据可以逐块翻译成 $1$-形式。
2. 三重叠上 $\varphi_{jl}=\varphi_{jk}\circ\varphi_{kl}$，代入 $\varphi(\xi)=\xi-\omega(\xi)$ 得 $\omega_{jl}=\omega_{jk}+\omega_{kl}$，即 $\omega=(\omega_{jk})\in Z^1(\mathcal U,Z^1_X)$。
   - 为什么：这是 $\varphi$ 的复合公式之直接展开：$\xi-\omega_{jl}(\xi)=(\xi-\omega_{kl}(\xi))-\omega_{jk}(\xi-\omega_{kl}(\xi))$。
3. 换一组局部同构 $\psi_j'=\sigma_j\circ\psi_j$，设 $\sigma_j$ 对应 $\rho_j\in Z^1(U_j)$，则 $\omega'_{jk}=\omega_{jk}+\rho_j-\rho_k$，即 $\omega'-\omega=d\rho$；故 $(D,i)$ 在 $H^1(X,Z^1_X)$ 中的类与平凡化的选取无关。
   - 为什么：两条上闭链相差一个上边缘就定义同一个上同调类；取覆盖的加细不改变上同调类。
4. 单射：若 $t(\mathcal D)=t(\mathcal D')$，加细后可设 $\omega-\omega'=d\rho$。令 $\varphi_j''=\sigma_j\circ\varphi_j'$，则其过渡形式满足 $\varphi_{jk}''=\sigma_j\varphi_{jk}'\sigma_k^{-1}$，相应上闭链为 $\omega''=\omega'+d\rho=\omega$。于是 $\theta_j=\psi_j''^{-1}\circ\psi_j$ 在重叠上相等，粘成整体同构 $\mathcal D\cong\mathcal D'$。
   - 为什么：过渡形式相同即可逐点粘合局部同构，这正是层公理（局部定义、重叠相容）给出的整体化。
5. 满射：给定上闭链 $\omega\in Z^1(\mathcal U,Z^1_X)$，在各 $U_j$ 上取 $\mathcal D_{U_j}$ 作局部模型，用 $\varphi_{jk}(\xi)=\xi-\omega_{jk}(\xi)$ 作粘接数据；三重叠条件 $\omega_{jl}=\omega_{jk}+\omega_{kl}$ 保证 $\varphi$ 的余圈相容，粘成 $X$ 上局部同构于 $\mathcal D_X$ 的层，其 $t$ 类即 $\omega$。
   - 为什么：粘接的相容性正是 $\omega$ 的上闭链条件；粘出的层逐块与 $(\mathcal D_X,i_X)$ 同构，故是扭层。

## 易错点

- $A$ 与 $\mathcal D_X$ 作为环层同构，并不自动给出扭层的同构：同构必须与 $i$ 相容。忽略这一点会把所有扭层误认为同一个。
- 「局部同构于 $(\mathcal D_X,i_X)$」是存在性陈述，不是给定数据；因此 $t$ 的定义还要验证与局部平凡化的选取无关（见「扭化不变量 $t$」一卡）。
- $i$ 给出的是 $A$ 上的左 $\mathcal O_X$-模结构，换 $i$ 就换了 $\mathcal O_X$-模结构；不要把 $A$ 的环结构与这个模结构混为一谈。

## 相关卡

- `mloc/concept/automorphism-group-of-dx`
- `mloc/concept/twisting-invariant-t`
- `mloc/concept/twist-by-line-bundle`
- `mloc/concept/homogeneous-twisted-sheaf`
- `dmod/concept/dz-structure-sheaf`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[1]（PDF [5]） · `源码/chapters/ch01.tex:7-9（扭微分算子层的定义）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[3]（PDF [7]） · `源码/chapters/ch01.tex:85-105（第 1 章定理 1.3）`
