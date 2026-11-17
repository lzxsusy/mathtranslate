# D-模

> `kw/concept/d-module` · 轨道 E · Langlands 与翻译器 · 状态 dev

> **先自测**：D-模在本文里从哪来，为什么说 A-膜给出 D-模只是“大致上”成立？

## 一句话

微分算子层上的模，几何 Langlands 的右端。本文论证 $K$ 中每张 A-膜给出 $\mathcal D_{K_M^{1/2}}$ 的模层，$\Psi=h$ 时就是普通 D-模。

## 定义

D-模是微分算子层 $\mathcal D_X$ 上的模；在光滑情形等价于带平坦联络的层。本文中 $K$ 里的每张 A-膜 $B'$ 的 $(B_{c.c.},B')$-strings 是 $(B_{c.c.},B_{c.c.})$-strings 代数上的模，而后者是 $K_M^{1/2}$ 上的微分算子层，于是 $B'$ 给出一个 D-模。

**记号**：$\mathcal D_X$：$X$ 上的微分算子层；$B_{c.c.}$：c.c. 膜；$K_M^{1/2}$：$M_H$ 上 $K$ 的全纯线丛的平方根。

## 要点（为什么需要它）

1. 它是几何 Langlands 的右端，也是 §11 要补的那一环：type F 膜在 $M_H(G)$，D-模在 $M(G)$。
2. c.c. 膜是翻译器：它的开弦代数是微分算子，任意 A-膜借它变成 D-模。
3. $\Psi=h$ 时弦代数就是普通微分算子，D-模解释最干净；$\Psi=\mathrm i\mathrm i$ 是另一特殊值，不可混淆。
4. D-模可看成余切丛非交换形变上的 B-膜，这给出另一种视角。

## 核心公式

$$
$\mathcal D_X\text{-}\mathrm{mod}$$[\kappa,f]=-\mathrm i(\Im\tau)^{-1}\kappa(f),\qquad \hat p_\alpha=-\frac{\mathrm i}{\Im\tau}\frac{\partial}{\partial q^\alpha}$
$$

$$
$[\kappa,f]=-\mathrm i(\Im\tau)^{-1}\kappa(f),\qquad \hat p_\alpha=-\frac{\mathrm i}{\Im\tau}\frac{\partial}{\partial q^\alpha}$
$$

## 定理与证明（或缺口）

### K 中每张 A-膜给出 D-模

设 $B_{c.c.}$ 为 c.c. 膜，则对任意 $K$ 中的 A-膜 $B'$，$(B_{c.c.},B')$-strings 是 $\mathcal D_{K_M^{1/2}}$-模。

> 证明状态：**sketch**。原文 p.196 用 claim/argue 语气；层化只对 $T^*V$ 型开集严格，Moyal 乘积的收敛性未完成（原文 p.190 承认），故只能算 sketch。

出处：`B p.196`

## 常见误解

- 把 D-模当成向量空间上的模；D-模是层，作用要逐开集定义。
- 把“A-膜 ⇒ D-模”当成函子性定理；原文只给单向构造，层化也未完成。
- 忘记 $\Psi=h$ 才是普通 D-模；$\Psi=\mathrm i\mathrm i$ 是镜像对称的特殊值。

## 相关卡

[典范余各向同性膜（c.c. 膜）](../concepts/canonical-coisotropic-brane.md) · [几何 Langlands 对应](../concepts/geometric-langlands.md) · [Hecke 特征层](../concepts/hecke-eigensheaf.md) · [c.c. A-膜、开弦代数与 A-膜→D-模](../derivations/a-to-dmod.md)

## 出处（印刷页）

- B p.184（B p.184）
- B p.196（B p.196）
- B p.205–206（B p.205–206）

> 说明：A=原文 p.184 的定义与 p.196 的“A-膜给 D-模”论证；B=把 strings 代数的模读成 D-模层；C=$\Psi=h$ 与 $\Psi=\mathrm i\mathrm i$ 的区分。
