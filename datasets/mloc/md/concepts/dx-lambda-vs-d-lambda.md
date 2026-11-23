# $\mathcal D_\lambda$ 与 $\mathcal D_{X,\lambda}$：$\rho$ 平移

> `mloc/concept/dx-lambda-vs-d-lambda` · type=concept · track=B · status=draft · verification=source-only

**别名**：$\mathcal D_\lambda=\mathcal D_{X,\lambda+\rho}$、rho-shift、参数平移、最容易看漏的一处

## 摘要

$\mathcal D_\lambda=\mathcal D_{X,\lambda+\rho}$：第 2 章参数比第 1 章小 $\rho$，故 $\mathcal D_{-\rho}=\mathcal D_X$。

## 问题

第 2 章的 $\mathcal D_\lambda$ 与第 1 章的 $\mathcal D_{X,\lambda}$ 是同一套参数吗，$\rho$ 从哪里来，$\lambda=-\rho$ 为什么恰好给出 $\mathcal D_X$？

## 定义

第 1 章 §2：$\mathcal D_{X,\mu}=U^\circ/J_\mu$，$\mu\in I(\mathfrak b_0^*)$，$J_\mu$ 由 $s-\sigma_\mu(s)$（$s\in\mathfrak b^\circ$）生成。第 2 章：$\mathfrak h=\mathfrak b_x/\mathfrak n_x$ 是 Cartan 代数，$U(\mathfrak h)\cong\operatorname{Sym}(\mathfrak h^*)$；对 $\lambda\in\mathfrak h^*$，$I_\lambda$ 是由 $\lambda+\rho$ 决定的特征标 $\phi_\lambda:U(\mathfrak h)\to\mathbb C$ 的核（生成元为 $h-(\lambda+\rho)(h)\cdot1$），$\mathcal D_\lambda=\mathcal D_\mathfrak h/I_\lambda\mathcal D_\mathfrak h$，其中 $\mathcal D_\mathfrak h=U^\circ/\mathfrak n^\circ U^\circ$。书中的约定是 $\mathcal D_\lambda=\mathcal D_{X,\lambda+\rho}$，即第 2 章的参数比第 1 章小 $\rho$。

记号：$\rho=\frac12\sum_{\alpha\in\Sigma^+}\alpha$；$I(\mathfrak b_0^*)=(\mathfrak b_0^*)^{B_0}$；$\mathfrak h\cong\mathfrak b_0/\mathfrak n_0$；$\mathcal D_\mathfrak h=U^\circ/\mathfrak n^\circ U^\circ$；$\lambda\in\mathfrak h^*$。

## 要点

- 锚点一：第 1 章的 $\mu=0$ 给出 $\sigma_0=0$、$J_0=\mathfrak b^\circ U^\circ$，故 $\mathcal D_{X,0}=\mathcal D_X$。
- 锚点二：第 2 章的 $\lambda=-\rho$ 满足 $\lambda+\rho=0$，$I_{-\rho}=\mathfrak h U(\mathfrak h)$，故 $\mathcal D_{-\rho}=U^\circ/\mathfrak b^\circ U^\circ=\mathcal D_X=\mathcal D_{X,0}$。
- 两个锚点一致正说明 $\mathcal D_\lambda=\mathcal D_{X,\lambda+\rho}$；因此第 2 章的 $\mathcal D_0=\mathcal D_{X,\rho}$ 是被 $\rho$ 扭过的层，不是 $\mathcal D_X$——这是全书最容易看漏的一处。
- $\rho$ 出现在 $I_\lambda$ 的定义里：$\lambda$ 按 Verma 模最高权的习惯书写（中心特征标 $\chi_\lambda$ 对应最高权 $\lambda+\rho$），参数天然带 $\rho$ 平移；这不是新的几何扭，而是参数化约定。
- 换到第 2 章后所有公式同步平移：$\mathcal D_\lambda$-模的无穷小特征标是 $\chi_\lambda$（$\ker\chi_\lambda=\gamma^{-1}(I_\lambda)=J_\theta$，$\theta=W\lambda$），典范态射 $U_\theta=U(\mathfrak g)/J_\theta U(\mathfrak g)\to\Gamma(X,\mathcal D_\lambda)$ 在 §6 证为同构。

## 公式

$$\mathcal D_\lambda=\mathcal D_\mathfrak h/I_\lambda\mathcal D_\mathfrak h$$

$$\mathcal D_\lambda=\mathcal D_{X,\lambda+\rho},\qquad\lambda\in\mathfrak h^*$$

$$\mathcal D_{-\rho}=\mathcal D_{X,0}=\mathcal D_X$$

$$I_\lambda=\ker\bigl(\phi_\lambda:U(\mathfrak h)\to\mathbb C\bigr),\qquad\phi_\lambda\ \text{由}\ \lambda+\rho\ \text{决定}$$

## 相关定理

### 约定（$\mathcal D_\lambda=\mathcal D_{X,\lambda+\rho}$）的自洽性

在旗簇情形，把 $I(\mathfrak b_0^*)$ 与 $\mathfrak h^*$ 经限制 $\mu\mapsto\mu|_{\mathfrak c}$ 等同（$\mathfrak c\subset\mathfrak b_0$ 是 Cartan 子代数）。则第 2 章的 $\mathcal D_\lambda$（$\lambda\in\mathfrak h^*$）与第 1 章的 $\mathcal D_{X,\mu}$（$\mu\in I(\mathfrak b_0^*)$）满足：$\mathcal D_\lambda\cong\mathcal D_{X,\mu}$ 当且仅当 $\mu=\lambda+\rho$。特别地 $\mathcal D_{-\rho}=\mathcal D_X$，而 $\mathcal D_0=\mathcal D_{X,\rho}\ne\mathcal D_X$。

证明状态：`complete`

1. $\mathcal D_\lambda$ 在 $x_0$ 处的几何纤维是 $U(\mathfrak g)/(\mathfrak n_0U(\mathfrak g)+I_\lambda U(\mathfrak g))$。
   - 为什么：商层的几何纤维是纤维对理想取商；$\mathcal D_\mathfrak h$ 的纤维是 $U(\mathfrak g)/\mathfrak n_0U(\mathfrak g)$。
2. 对 $s\in\mathfrak b_0$，$\alpha(s)$ 在 $x_0$ 的值是 $s$ 在 $U(\mathfrak b_0)\to U(\mathfrak b_0)/\mathfrak n_0U(\mathfrak b_0)=U(\mathfrak h)\to U(\mathfrak h)/I_\lambda=\mathbb C$ 下的像，即 $\phi_\lambda(s)=(\lambda+\rho)(s)$。
   - 为什么：$I_\lambda$ 就是 $\phi_\lambda$ 的核，而 $\mathfrak n_0$ 是 $\mathfrak b_0$ 的理想，故先商去 $\mathfrak n_0$ 再商 $I_\lambda$。
3. 故 $\mathcal D_\lambda$ 的齐性参数 $\sigma:\mathfrak b^\circ\to\mathcal O_X$ 在 $x_0$ 处等于 $\lambda+\rho$（在 $\mathfrak n_0$ 上为 $0$、在 Cartan 上等于 $\lambda+\rho$）。
   - 为什么：$B_0$-不变形式在 $[\mathfrak b_0,\mathfrak b_0]=\mathfrak n_0$ 上为零，故由它在 Cartan $\mathfrak c$ 上的值决定；限制 $I(\mathfrak b_0^*)\to\mathfrak c^*\cong\mathfrak h^*$ 是线性同构。
4. 由第 1 章定理 2.4 的双射，$\mathcal D_\lambda\cong\mathcal D_{X,\mu}$ 当且仅当 $\mu=\lambda+\rho$；取 $\lambda=-\rho$ 得 $\mathcal D_{-\rho}\cong\mathcal D_{X,0}=\mathcal D_X$，取 $\lambda=0$ 得 $\mathcal D_0\cong\mathcal D_{X,\rho}$。
   - 为什么：第 1 章定理 2.4 把同构类与 $\sigma$（即 $\mu$）一一对应，而第 3 步已算出 $\sigma=\lambda+\rho$；所以平移被这条计算唯一确定，不是约定问题。

## 易错点

- 本卡的「自洽性」四步证明是据第 1 章定理 2.4 与 $I_\lambda$ 的定义补出的：讲义只在 ch02a.tex:125-131 以校注断言 $\mathcal D_\lambda=\mathcal D_{X,\lambda+\rho}$（「第 2 章的参数比第 1 章小 $\rho$」），未给证明；引用时按「推论」而非原书定理对待。
- 全书最容易出错的一处：$\mathcal D_0$（第 2 章）不是 $\mathcal D_X$，而是 $\mathcal D_{X,\rho}$；$\mathcal D_X$ 对应 $\lambda=-\rho$。
- 把第 1 章的 $\mathcal D_{X,\lambda}$ 与第 2 章的 $\mathcal D_\lambda$ 混用会整体错开 $\rho$：第 2 章关于 $\mathcal D_\lambda$-模的结论不能不加平移地搬回 $\mathcal D_{X,\lambda}$。
- $I_\lambda$ 由 $\lambda+\rho$ 决定（生成元 $h-(\lambda+\rho)(h)$），不是由 $\lambda$ 决定；读 $\gamma^{-1}(I_\lambda)$ 与 $\chi_\lambda$ 时若按 $\lambda$ 直接算中心特征标会漏掉 $\rho$。
- $\mathcal D_{-\rho}=\mathcal D_X$ 与 $\mathcal D_\mathfrak h$ 不是同一个层：后者是 $U^\circ/\mathfrak n^\circ U^\circ$，前者还要再对 $\mathfrak h^\circ$（即 $I_{-\rho}$）取商。

## 相关卡

- `mloc/concept/d-lambda-sheaf`
- `mloc/concept/homogeneous-twisted-sheaf`
- `mloc/concept/d-h-sheaf`
- `mloc/concept/twisted-sheaf-of-differential-operators`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 2 章 §1 旗簇上的齐性扭层 · p.[20]（PDF [24]） · `源码/chapters/ch02a.tex:112-131（$I_\lambda$、$\mathcal D_\lambda$ 与约定 $\mathcal D_\lambda=\mathcal D_{X,\lambda+\rho}$）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §2 齐性扭微分算子层 · p.[12]（PDF [16]） · `源码/chapters/ch01.tex:447-467（$\mathcal D_{X,\lambda}$、第 1 章命题 2.3、第 1 章定理 2.4）`
