# Langlands 对偶群 $\G^\vee$

> `hausel22/concept/langlands-dual-group` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：为什么 $\SL_n$ 的对偶是 $\PGL_n$ 而不是 $\SL_n$？

## 一句话

复约化群的 Langlands 对偶就是把根数据里的格与对偶格互换所得的群；它的 Hitchin 系统是原群的镜像。

## 定义

复约化群的分类由根数据 $(X,\Phi,X^\vee,\Phi^\vee)$ 给出：秩 $n$ 的格 $X$、对偶格 $X^\vee$，以及根系 $\Phi\subset X$ 与余根系 $\Phi^\vee\subset X^\vee$。$\G$ 的 Langlands 对偶 $\G^\vee:=\G^L$ 就是以对偶根数据 $(X^\vee,\Phi^\vee,X,\Phi)$ 为根数据的约化群。例：$\GL_n^\vee\cong\GL_n$，$\SL_n^\vee\cong\PGL_n$。

**记号**：$\G,\G^\vee$；$X,X^\vee$；$\Phi,\Phi^\vee$；$\omega_k$（基本权）。

## 要点（为什么需要它）

1. 对偶只交换「格与对偶格」「根与余根」两件事，群本身的秩不变、维数不变。
2. $\SL_n$ 的格是权格 $\Z^{n-1}$ 的商结构，其对偶是 $\PGL_n$ 的余权格；所以 $\SL_n^\vee=\PGL_n$，反之亦然。
3. $\GL_n$ 是自对偶的（$\GL_n^\vee\cong\GL_n$），这正是原文主定理集中在 $\SL_n/\PGL_n$ 而与 $\GL_n$ 对照的原因。
4. 本文所有「镜像」都是「$\G$-Hitchin 系统」与「$\G^\vee$-Hitchin 系统」之间的镜像，而不是同一群的两种结构。
5. 对偶群决定镜像侧的基本权：$\mu\in X_+(\G^\vee)$ 与 $\G$ 的支配权是同一个格，见 §3.4 的 $\mu\in X_+(\G^\vee)=X^+(\G)$。

## 核心公式

$$
$$(X,\Phi,X^\vee,\Phi^\vee)\longmapsto(X^\vee,\Phi^\vee,X,\Phi)$$$$\GL_n^\vee\cong\GL_n,\qquad \SL_n^\vee\cong\PGL_n$$
$$

$$
$$\GL_n^\vee\cong\GL_n,\qquad \SL_n^\vee\cong\PGL_n$$
$$

## 定理与证明（或缺口）

### 对偶群的根数据刻画

以 $(X^\vee,\Phi^\vee,X,\Phi)$ 为根数据的复约化群 $\G^\vee$ 就是 $\G$ 的 Langlands 对偶；$\G^\vee$ 的支配特征格 $X_+(\G^\vee)$ 与 $\G$ 的支配权格 $X^+(\G)$ 重合。

> 证明状态：**sketch**。原文只用一句话给出定义，没有证明分类定理本身。

出处：`A p.2231`

## 常见误解

- 把 $\SL_n$ 的对偶说成 $\SL_n$：$\SL_n$ 是单连通的，其对偶是伴随型 $\PGL_n$。
- 把「对偶群」与「对偶表示」混淆：Langlands 对偶是群层面的，与表示的对偶无关。
- $\G^\vee$ 的秩与 $\G$ 相同、维数也相同，但中心不同（$\SL_n$ 的中心是 $\Z/n$，$\PGL_n$ 的中心平凡），这个差别正是 §2.4 里 $\Gamma=\Jac_C[n]$ 的来源。
- 原文写「对偶格 $X^\vee$ 中的根系 $\Phi\subset X$ 与余根系 $\Phi^\vee\subset X^\vee$」，读时注意 $\Phi$ 在 $X$ 里、$\Phi^\vee$ 在 $X^\vee$ 里，不要顺着句子读成都在 $X^\vee$ 里。

## 相关卡

[几何 Langlands 对应](../concepts/geometric-langlands-correspondence.md) · [Hitchin 系统](../concepts/hitchin-system.md) · [拓扑镜像对称](../concepts/topological-mirror-symmetry.md)

## 出处（印刷页）

- A p.2231（A p.2231）

> 说明：A=原文 §2.2 的定义与 $\GL_n,\SL_n$ 两个例子；B=把「中心不同」与 §2.4 的 $\Gamma$ 联系起来；C=「秩与维数不变」是标准事实，原文未写。最没把握处：$X_+(\G^\vee)=X^+(\G)$ 的等式原文只在 §3.4 顺带使用，未在此处说明。
