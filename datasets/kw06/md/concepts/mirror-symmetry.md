# 镜像对称（本文版本）

> `kw/concept/mirror-symmetry` · 轨道 D · 二维、膜与算子 · 状态 dev

> **先自测**：镜像对称在这篇文章里怎样从 S-对偶推出来，SYZ 图像又给出什么几何内容？

## 一句话

二维 sigma 模型的等价：A-模型与 B-模型互换。本文中 S-对偶把它实现为 $B_J(M_H(G))\cong A_K(M_H({}^LG))$，再复合 $I$ 得 $J$ 中的镜像对。

## 定义

镜像对称指一对靶空间上的 A-模型与 B-模型等价。本文的版本是 $B_J(M_H(G,C))\cong A_K(M_H({}^LG,C))$：在 $\Psi=\infty$ 取 B-模型、作 S-对偶到 $\Psi=0$ 取 A-模型；再复合自同构 $I$，就得到复结构 $J$ 中 $M_H(G)$ 与其镜像的配对。

**记号**：$I,J,K$：$M_H$ 上的三个复结构；$\mathcal B$：Hitchin 纤维化的底；$\Xi$：对偶底之间的映射。

## 要点（为什么需要它）

1. 它是 §5 的主结论，把四维 S-对偶在二维的残余变成几何对偶：$A\leftrightarrow B$。
2. SYZ 图像把它几何化：Hitchin 纤维化的纤维是复环面，$S$ 给出 $\Xi:\mathcal B\to{}^L\mathcal B$ 与纤维上的对偶环面互换。
3. Table 2 给出六种膜类型的互换表，是 §9–§11 里逐项对照的依据。
4. 对单连通单 Lie 型，$n_g=1$ 且 $\Xi$ 为恒等，镜像对的差异藏在纤维的复结构里。

## 核心公式

$$
$B_J(M_H(G,C))\ \cong\ A_K(M_H({}^LG,C))$$\Psi\ \mapsto\ -\frac{1}{n_g\Psi},\qquad \Psi=\infty\ \leftrightarrow\ \Psi=0$
$$

$$
$\Psi\ \mapsto\ -\frac{1}{n_g\Psi},\qquad \Psi=\infty\ \leftrightarrow\ \Psi=0$
$$

## 定理与证明（或缺口）

### S-对偶在二维给出镜像对称

取 $\Psi=\infty$（$t=\mathrm i$）时二维极限是复结构 $J$ 中的 B-模型；S-对偶把 $\Psi$ 送到 $\Psi'=-1/(n_g\Psi)=0$，其二维极限是复结构 $K$ 中靶空间 $M_H({}^LG,C)$ 的 A-模型；两者是同一四维理论的两个描述，故 $B_J(M_H(G,C))\cong A_K(M_H({}^LG,C))$。

1. 在 $\Psi=\infty$ 取二维极限。
   - *为什么*：该点 $t=\mathrm i$，扭化给出复结构 $J$ 中的 B-模型。
2. 作用 S-对偶。
   - *为什么*：$S$ 把 $\Psi$ 作分式线性变换，$\infty$ 必落到 $0$。
3. 在 $\Psi=0$ 取二维极限。
   - *为什么*：该点得到复结构 $K$ 中 $M_H({}^LG,C)$ 上的 A-模型。
4. 两极限相等，得 $B_J\cong A_K$。
   - *为什么*：它们都是同一个四维扭化理论在二维的约化。

出处：`B p.70`

## 常见误解

- 把镜像对称说成两个流形同构；它只是两套二维量子场论的等价，几何上体现为 Hitchin 纤维化的对偶环面。
- 把 $I$（$\varphi\mapsto\mathrm i\varphi$）与 $S$（换 $\Psi$、换对偶群）混为一谈。
- 以为 SYZ 的 $\Xi$ 总是非平凡；单连通单 Lie 型时它就是恒等映射。

## 相关卡

[A-模型（A 扭化 sigma 模型）](../concepts/a-model.md) · [B-模型（B 扭化 sigma 模型）](../concepts/b-model.md) · [S-对偶](../concepts/s-duality.md) · [S-对偶 = 镜像对称（全文心脏）](../derivations/sdual-mirror.md)

## 出处（印刷页）

- B p.70（B p.70）
- B p.71（B p.71）
- B p.76–77（B p.76–77）

> 说明：A=原文 p.70 的三步推导与 p.71 的表；B=把 $I$ 复合读成“$J$ 中的镜像对”；C=$n_g$、$\Xi$ 恒等的细节。
