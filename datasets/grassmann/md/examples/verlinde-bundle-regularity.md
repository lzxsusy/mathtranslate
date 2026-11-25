# Verlinde 丛的正则性阈值

> `grassmann/example/verlinde-bundle-regularity` · 轨道 8 · 阿贝尔簇上的正则性 · 状态 draft

> **这张卡练什么**：为什么 Verlinde 丛的正则性阈值会是 $k\ge r+1$ 与 $k\ge2r+1$ 这种只依赖秩与次数的整齐形式？

## 一句话

Verlinde 丛 $E_{r,k}$ 是 $m$-$\Theta$-正则的阈值恰为 $k\ge r+1$、$(-1)$-$\Theta$-正则的阈值恰为 $k\ge2r+1$；于是 $k\ge r+1$ 时整体生成、$k\ge2r+1$ 时正规生成，重证 Popa 的结论。

## 背景定义

本例计算的是 $E_{r,k}$ 的 $m$-$\Theta$-正则阈值：按定义 7.23，$E_{r,k}$ 是 $m$-$\Theta$-正则的当且仅当 $E_{r,k}((m-1)\Theta)$ 是 $M$-正则的。因为 $E_{r,k}$ 半齐次（且多稳定，[Po]），引理 7.29 把这件事化成 $IT_0$ 消没，而 $IT_0$ 可在同源拉回下逐线丛检验。

## 设定

设 $C$ 是亏格 $g\ge2$ 的光滑曲线，$U_C(r,0)$ 是 $C$ 上秩 $r$、次数 $0$ 的半稳定向量丛模空间，$\det\colon U_C(r,0)\to J(C)$。取 $N\in\operatorname{Pic}^{g-1}(C)$ 与广义 theta 除子 $\Theta_N$，定义 $(r,k)$-Verlinde 丛 $$E_{r,k}:=\det_*\mathcal O_{U_C(r,0)}(k\Theta_N).$$ 目标是求 $E_{r,k}$ 成为 $m$-$\Theta$-正则与 $(-1)$-$\Theta$-正则的 $k$ 阈值，其中 $\Theta$ 是 $J(C)$ 的主极化。

## 计算

设 $r_J\colon J(C)\to J(C)$ 是乘 $r$ 映射。由 [Po] Lemma 2.3，$r_J^*E_{r,k}\cong\bigoplus_{r^{2g}}\mathcal O_{J(C)}(kr\Theta_N)$；又 $r_J^*\mathcal O_{J(C)}(\Theta_N)\equiv\mathcal O_{J(C)}(r^2\Theta_N)$，故 $$r_J^*\bigl(E_{r,k}((m-1)\Theta)\bigr)\cong\bigoplus_{r^{2g}}\mathcal O_{J(C)}\bigl((kr+r^2(m-1))\Theta_N\bigr).$$ 线丛 $\mathcal O_{J(C)}(a\Theta_N)$ 是 $M$-正则的 $\iff a\ge1$（$a\ge1$ 时充裕故 $IT_0$；$a=0$ 时 $h^1(\mathcal O_J)=\wedge^1H^1=\mathbb C^g\ne0$ 对一切 $\alpha$，$V^1=\widehat J$）。于是阈值由 $kr+r^2(m-1)\ge1$ 给出：$m=0$ 给 $k\ge r+\frac1r$，整数化即 $k\ge r+1$；$m=-1$ 给 $k\ge2r+\frac1r$，即 $k\ge2r+1$。

## 要点

- $E_{r,k}$ 半齐次且多稳定，故其正则性由『同源拉回 = 线丛直和』判定：$r_J^*E_{r,k}\cong\bigoplus_{r^{2g}}\mathcal O(kr\Theta_N)$。
- $M$-正则性在同源拉回下保持，而线丛 $\mathcal O_J(a\Theta_N)$ 是 $M$-正则的 $\iff a\ge1$（$a=0$ 时 $h^1(\mathcal O_J)=g$，$V^1=\widehat J$；$a\ge1$ 时充裕）。
- 于是 $E_{r,k}((m-1)\Theta)$ 是 $M$-正则的 $\iff kr+r^2(m-1)\ge1$：$m=0$ 给 $k\ge r+1$，$m=-1$ 给 $k\ge2r+1$。
- 用定理 7.24(1) 与推论 7.35：$k\ge r+1$ 时 $E_{r,k}$ 整体生成，$k\ge2r+1$ 时正规生成——正是 [Po] 命题 5.2 与定理 5.9(a)。
- 全部计算只用 $r_J^*\Theta_N\equiv r^2\Theta_N$ 与 $r_J^*E_{r,k}$ 的分解，没有解消或谱序列。

## 关键公式

$$
E_{r,k}:=\det_*\mathcal O_{U_C(r,0)}(k\Theta_N)
$$

$$
r_J^*E_{r,k}\cong\bigoplus\nolimits_{r^{2g}}\mathcal O_{J(C)}(kr\Theta_N),\qquad r_J^*\Theta_N\equiv r^2\Theta_N
$$

$$
E_{r,k}\ \text{是 }m\text{-}\Theta\text{-正则}\iff kr+r^2(m-1)\ge1
$$

## 相关定理

- **例 7.37（Verlinde 丛的正则性阈值）**：设 $E_{r,k}=\det_*\mathcal O_{U_C(r,0)}(k\Theta_N)$。则 $E_{r,k}$ 是 $0$-$\Theta$-正则的 $\iff k\ge r+1$，是 $(-1)$-$\Theta$-正则的 $\iff k\ge2r+1$。特别地 $k\ge r+1$ 时 $E_{r,k}$ 整体生成，$k\ge2r+1$ 时正规生成。

## 易错点

- 别把 $r_J^*E_{r,k}$ 的分解读成『$E_{r,k}$ 是线丛直和』：$r_J$ 是有限同源，拉回拆成线丛直和只说明 $E_{r,k}$ 半齐次；$E_{r,k}$ 本身仍是秩 $r$ 的丛。
- 阈值里的 $+1$ 来自『次数 $\ge1$』而不是 $\ge0$：$a=0$ 时 $h^1(\mathcal O_J)=g\ne0$，所以 $m=0$ 需要 $kr\ge r^2+1$，整数化后正是 $k\ge r+1$；写成 $k\ge r$ 会差一格。
- 别把两个阈值混起来：$k\ge r+1$ 只给整体生成，正规生成要 $k\ge2r+1$；中间那段 $r+1\le k\le2r$ 的丛整体生成但不正规生成。

## 用到哪些概念

- [$m$-$\Theta$-正则性](../concepts/m-theta-regular.md)
- [半齐次向量丛](../concepts/semihomogeneous-bundle.md)
- [$M$-正则层](../concepts/m-regular-sheaf.md)

## 相关卡

- [$m$-$\Theta$-正则性](../concepts/m-theta-regular.md)
- [半齐次向量丛](../concepts/semihomogeneous-bundle.md)
- [Verlinde 丛](../concepts/verlinde-bundle.md)

## 出处

- ch8 §7.3 例 7.37（Verlinde 丛的阈值）；中译 p.157（英文 PDF p.174），源码 `chapters/ch08.tex:974`
