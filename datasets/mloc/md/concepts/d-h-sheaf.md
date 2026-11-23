# $\mathcal D_\mathfrak h$ 与 $U(\mathfrak h)$ 的作用

> `mloc/concept/d-h-sheaf` · type=concept · track=B · status=draft · verification=source-only

**别名**：$\mathcal D_\mathfrak h=U^\circ/\mathfrak n^\circ U^\circ$、$\varphi:U(\mathfrak h)\to\Gamma(X,\mathcal D_\mathfrak h)$、Harish-Chandra 同态

## 摘要

$\Gamma(X,\mathcal D_\mathfrak h)^G=U(\mathfrak h)$，$\mathcal D_\mathfrak h=U^\circ/\mathfrak n^\circ U^\circ$。

## 问题

把 $U^\circ$ 只对幂零根 $\mathfrak n^\circ$ 取商得到什么层，$U(\mathfrak h)$ 为什么能等同于它的 $G$-不变截面？

## 定义

$\mathfrak h=\mathfrak b_x/\mathfrak n_x$ 是 Cartan 代数（与 $x\in X$ 无关），$\mathfrak h^\circ=\mathfrak b^\circ/\mathfrak n^\circ=\mathcal O_X\otimes_\mathbb C\mathfrak h$。由第 2 章引理 1.1，$\mathfrak n^\circ U^\circ$ 是 $U^\circ$ 的双边理想层，令 $\mathcal D_\mathfrak h=U^\circ/\mathfrak n^\circ U^\circ$。$\mathfrak g^\circ\to\mathcal D_\mathfrak h$ 诱导 $\mathfrak h^\circ\to\mathcal D_\mathfrak h$，进而给出代数同态 $\varphi:U(\mathfrak h)\to\Gamma(X,\mathcal D_\mathfrak h)$；$H$ 的平凡性使诱导的 $G$-作用在 $\mathfrak h$ 上平凡，故 $\varphi(U(\mathfrak h))\subset\Gamma(X,\mathcal D_\mathfrak h)^G$。

记号：$\mathcal D_\mathfrak h$；$\varphi$；$\gamma:Z(\mathfrak g)\to U(\mathfrak h)$：Harish-Chandra 同态；$\Gamma(X,\mathcal D_\mathfrak h)^G$；$\bar{\mathfrak n}$：相对 Borel 的幂零根。

## 要点

- $\mathfrak h=\mathfrak b_x/\mathfrak n_x$ 是 $X$ 上平凡丛 $H=\mathcal B/\mathcal N$ 的整体截面，故 $U(\mathfrak h)$ 是「常数」对象；$B_x$ 在 $\mathfrak b_x/\mathfrak n_x$ 上平凡作用正是 $H$ 平凡的原因。
- 商只用 $\mathfrak n^\circ U^\circ$，不用 $\mathfrak b^\circ U^\circ$：故 $\mathcal D_\mathfrak h$ 比 $\mathcal D_X=U^\circ/\mathfrak b^\circ U^\circ$ 大，它保留 Cartan 方向的形式变量；$\mathcal D_\lambda$ 是在此基础上再对 $I_\lambda$ 取商。
- 第 2 章引理 1.2：$\varphi$ 单射（几何纤维上用 PBW），像在中心（对 $G$-作用求导知与 $\mathfrak g$ 的像交换，而 $\mathcal D_\mathfrak h$ 由 $\mathcal O_X$ 与 $\mathfrak g$ 生成）。
- 第 2 章引理 1.3：局部 $\psi:(\mathcal O_U\otimes U(\bar{\mathfrak n}))\otimes U(\mathfrak h)\cong\mathcal D_\mathfrak h|_U$（Bruhat 坐标 $U\cong\bar N$）；第 2 章推论 1.4：$\mathcal D_\mathfrak h$ 作为 $U(\mathfrak h)$-模局部自由。
- 第 2 章引理 1.5：$\varphi$ 满射，即 $\Gamma(X,\mathcal D_\mathfrak h)^G=U(\mathfrak h)$；第 2 章命题 1.6：$\varphi\circ\gamma$ 等于 $Z(\mathfrak g)$ 到 $\Gamma(X,\mathcal D_\mathfrak h)$ 的典范同态，即 Harish-Chandra 同态与 $\varphi$ 交换。

## 公式

$$\mathcal D_\mathfrak h=U^\circ/\mathfrak n^\circ U^\circ$$

$$\varphi:U(\mathfrak h)\longrightarrow\Gamma(X,\mathcal D_\mathfrak h)$$

$$\Gamma(X,\mathcal D_\mathfrak h)^G=U(\mathfrak h)$$

$$\mathcal D_\lambda=\mathcal D_\mathfrak h/I_\lambda\mathcal D_\mathfrak h$$

$$(\mathcal O_U\otimes_\mathbb C U(\bar{\mathfrak n}))\otimes_\mathbb C U(\mathfrak h)\cong\mathcal D_\mathfrak h|_U$$

## 相关定理

### 第 2 章引理 1.2（$\varphi$ 单射且像在中心）

(i) $U(\mathfrak h)$ 到 $\Gamma(X,\mathcal D_\mathfrak h)^G$ 的自然态射 $\varphi$ 是单射。(ii) $\varphi$ 的像含于 $\mathcal D_\mathfrak h$ 的中心。

证明状态：`complete`

1. 设 $x\in X$。$\mathcal D_\mathfrak h$ 在 $x$ 处的几何纤维是 $T_x(\mathcal D_\mathfrak h)=U(\mathfrak g)/\mathfrak n_xU(\mathfrak g)$。
   - 为什么：商层的几何纤维是纤维对 $\mathfrak n_x$ 生成的理想取商。
2. $\varphi$ 与「在 $x$ 处取值」复合，得到 $U(\mathfrak h)\to U(\mathfrak b_x)/\mathfrak n_xU(\mathfrak b_x)\to U(\mathfrak g)/\mathfrak n_xU(\mathfrak g)$。
   - 为什么：$\mathfrak h\to\mathfrak b_x/\mathfrak n_x$ 是自然的同构；取值映射在纤维上就是这个复合。
3. 由 Poincaré--Birkhoff--Witt 定理，上述复合是单射；故 $\varphi$ 单射。
   - 为什么：取 $\mathfrak b_x$ 中的 Cartan $\mathfrak c$ 与正根，PBW 基给出 $U(\mathfrak c)\hookrightarrow U(\mathfrak g)/\mathfrak n_xU(\mathfrak g)$；局部自由层的态射在每根纤维单射即整体单射。
4. (ii) 对 $G$-作用求导知 $\varphi(U(\mathfrak h))$ 与 $\mathfrak g$ 在 $\mathcal D_\mathfrak h$ 中的像交换；而 $\mathcal D_\mathfrak h$ 由 $\mathcal O_X$ 与 $\mathfrak g$ 的像生成，故 $\varphi(U(\mathfrak h))$ 在中心。
   - 为什么：中心就是与全部生成元交换的元素；生成元是 $\mathcal O_X$（显然交换）与 $\mathfrak g$ 的像。

### 第 2 章引理 1.5（$\Gamma(X,\mathcal D_\mathfrak h)^G=U(\mathfrak h)$）

$U(\mathfrak h)$ 到 $\Gamma(X,\mathcal D_\mathfrak h)^G$ 的自然态射 $\varphi$ 是同构。

证明状态：`complete`

1. 由第 2 章引理 1.2(i)，$\varphi$ 单射，只需证满。
   - 为什么：已有单射，剩下逐点说明任一 $G$-不变截面落在像中。
2. 设 $s$ 是 $\mathcal D_\mathfrak h$ 的 $G$-不变整体截面，则 $s(x)$ 必须 $B_x$-不变；取 $\mathfrak b_x$ 中的 Cartan $\mathfrak c$，$s(x)$ 在 $U(\mathfrak g)/\mathfrak n_xU(\mathfrak g)$ 中关于 $\mathfrak c$ 的权为零。
   - 为什么：$B_x$ 是 $x$ 的稳定化子，$G$-不变意味着每点被 $B_x$ 固定；$\mathfrak c$ 的权分解使零权部分恰是 $B_x$-不变元。
3. 故 $s(x)$ 在 $U(\mathfrak h)$ 的像中，存在 $t\in\varphi(U(\mathfrak h))$ 使 $t-s$ 是 $G$-不变截面且在 $x$ 处为零；由 $G$-不变性它在每点为零。
   - 为什么：$X$ 是齐性空间，$G$-不变截面由它在一点的值决定。
4. 由第 2 章引理 1.3，$\mathcal D_\mathfrak h$ 作为（左乘的）$\mathcal O_X$-模局部自由，故 $t-s=0$，即 $s=t$。
   - 为什么：局部自由模的截面在每点为零即整体为零；于是 $\varphi$ 满射。

### 第 2 章命题 1.6（$\gamma$ 与 $\varphi$ 交换）

由自然代数同态构成的图表 $Z(\mathfrak g)\xrightarrow{\gamma}U(\mathfrak h)\xrightarrow{\varphi}\Gamma(X,\mathcal D_\mathfrak h)$ 与 $Z(\mathfrak g)\to\Gamma(X,\mathcal D_\mathfrak h)$ 的典范同态交换，即 $\varphi\circ\gamma$ 等于该典范同态。

证明状态：`complete`

1. 由第 2 章引理 1.3，$\mathcal D_\mathfrak h$ 关于左乘是局部自由的 $\mathcal O_X$-模，故只需逐点比较两个复合映射。
   - 为什么：局部自由模的态射由它在各点纤维上的值决定。
2. 对 $x\in X$，$T_x(\mathcal D_\mathfrak h)=U(\mathfrak g)/\mathfrak n_xU(\mathfrak g)$；$\varphi\circ\gamma$ 的纤维映射是 $U(\mathfrak g)\to U(\mathfrak b_x)/\mathfrak n_xU(\mathfrak b_x)\to U(\mathfrak g)/\mathfrak n_xU(\mathfrak g)$，而典范同态的纤维映射就是 $U(\mathfrak g)\to U(\mathfrak g)/\mathfrak n_xU(\mathfrak g)$。
   - 为什么：$\gamma$ 的定义是先在 $U(\mathfrak b_x)$ 上投影再与 $U(\mathfrak h_x)\cong U(\mathfrak h)$ 复合；$\varphi$ 在同一点正是 $U(\mathfrak h)\to U(\mathfrak b_x)/\mathfrak n_xU(\mathfrak b_x)$。
3. 两者在每点相同，故图表交换。
   - 为什么：第 1 步的逐点判据。

## 易错点

- $\mathcal D_\mathfrak h$ 不是 $\mathcal D_X$：$\mathcal D_X=U^\circ/\mathfrak b^\circ U^\circ$ 还要对 $\mathfrak h^\circ$ 取商；$\mathcal D_\mathfrak h$ 保留 Cartan 方向，所以 $\mathcal D_\lambda$ 要在它上面再商 $I_\lambda$。
- $\varphi$ 的像是 $G$-不变元，但「$G$-不变」在一点上只等于「$B_x$-不变」；证明满射时必须用 $B_x$-不变 ⇒ 零权 ⇒ 落在 $U(\mathfrak h)$ 的像，这一步用的是稳定化子，不是整体 $G$。
- $\gamma$ 由 $Z(\mathfrak g)\subset U(\mathfrak b_x)+\mathfrak n_xU(\mathfrak g)$ 的投影定义，与 $x$ 无关；把 $\gamma$ 与 $\varphi$ 的复合顺序写反会得到错误陈述。
- $\mathcal D_\mathfrak h$ 作为 $U(\mathfrak h)$-模局部自由（第 2 章推论 1.4），但作为 $\mathcal O_X$-模不是有限生成自由模；两种「局部自由」不要混。

## 相关卡

- `mloc/concept/borel-and-nilpotent-radical-sheaves`
- `mloc/concept/d-lambda-sheaf`
- `mloc/concept/dx-lambda-vs-d-lambda`
- `mloc/concept/homogeneous-twisted-sheaf`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 2 章 §1 旗簇上的齐性扭层 · p.[18]（PDF [22]） · `源码/chapters/ch02a.tex:35-55（$\mathcal D_\mathfrak h$ 的定义与第 2 章引理 1.2）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 2 章 §1 旗簇上的齐性扭层 · p.[19]（PDF [23]） · `源码/chapters/ch02a.tex:63-89（第 2 章引理 1.3、第 2 章推论 1.4、第 2 章引理 1.5）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 2 章 §1 旗簇上的齐性扭层 · p.[20]（PDF [24]） · `源码/chapters/ch02a.tex:91-110（Harish-Chandra 同态与第 2 章命题 1.6）`
