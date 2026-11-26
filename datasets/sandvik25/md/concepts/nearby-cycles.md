# 附近循环函子 $\Psi_f$

> `sandvik25/concept/nearby-cycles` · 轨道 A · 中心层与 Wakimoto 层 · 状态 dev

> **先自测**：附近循环函子怎么定义，它的五条函子性质各自负责后面的哪一步？

## 一句话

对 $f\colon X\to\mathbb C$，把 $X^\times=f^{-1}(\mathbb C^\times)$ 上的层拉回、经万有覆盖、再取特殊纤维：$\Psi_f\mathcal F=(i^*j_*\exp_{X*}\exp_X^*\mathcal F)[-1]$。

## 定义

设 $X$ 为复代数簇，$f\colon X\to\mathbb C$ 为代数映射，$X^\times=f^{-1}(\mathbb C^\times)$、$X^0=f^{-1}(0)$。取指数映射 $\exp\colon\mathbb C\to\mathbb C^\times$ 与纤维积 $\widetilde X^\times=X\times_{\mathbb C^\times}\mathbb C$，得交换图 (3)。定义 $\Psi_f\colon\mathcal D^b_c(X^\times)\to\mathcal D^b_c(X^0)$，$\mathcal F\mapsto(i^*j_*\exp_{X*}\exp_X^*\mathcal F)[-1]$。

**记号**：$i\colon X^0\hookrightarrow X$、$j\colon X^\times\hookrightarrow X$ 为包含；系数取特征 $0$ 代数闭域 $k$。

## 要点（为什么需要它）

1. 定义里三层拉回–推前不是装饰：$\exp$ 把 $\mathbb C^\times$ 的万有覆盖摊开，$j_*$ 把 $X^\times$ 上的层延到 $X$，$i^*$ 再取到特殊纤维——这正是「局部系统单值」的几何版本。
2. 命题 2.2.2(2) 的 perverse $t$-正合性是中心函子能落在反常层里的唯一原因；没有它，$Z(F)$ 不知落在哪个三角范畴的哪一层。
3. 命题 2.2.2(4) 的紧合基变换是定理 2.4.1(5)（$\pi_*Z(F)\cong F$）的全部内容：把 $\varpi\colon\mathrm{Gr}^{\mathrm{cen}}_G\to\mathrm{Gr}_G\times\mathbb C$ 当紧合映射用。
4. 命题 2.2.2(5) 说常层沿投影的特殊化是常层，这是计算 $\Psi_{\mathrm{pr}_2}$ 的唯一显式工具。
5. (1) 之所以要单独列出，是因为 $\exp_X$ 不是代数映射，故「有界可构造」并非自动保持。

## 核心公式

$$
$\Psi_f\mathcal F:=(i^*j_*\exp_{X*}\exp_X^*\mathcal F)[-1]$$\Psi_f(\mathcal F\boxtimes k_{\mathbb C^\times}[1])\cong\mathcal F$（$f$ 为投影）
$$

$$
$\Psi_f(\mathcal F\boxtimes k_{\mathbb C^\times}[1])\cong\mathcal F$（$f$ 为投影）
$$

## 定理与证明（或缺口）

### 命题 2.2.2（五条性质）

(1) 有界可构造复形映到有界可构造复形；(2) 是 perverse $t$-正合的；(3) 光滑基变换相容；(4) 紧合基变换相容；(5) 沿投影的常层特殊化为原层。

> 证明状态：**gap**。原文只列性质并注明「不显然，因为 $\exp_X$ 不是代数映射」，证明交给 SGA 与 [AcRi]。

出处：`A p.3`

## 常见误解

- 定义里的 $[-1]$ 位移不能省：它把「单值的对数」摆到与权格相同的次数上，定理 2.4.1(2) 的 $t$-正合性依赖它。
- $\widetilde X^\times$ 是解析空间而非代数簇（原文脚注 2）：凡是引用代数几何定理的地方都要绕开它，只能用 $\exp$ 的解析性质。

## 相关卡

[中心仿射 Grassmann 簇 $\mathrm{Gr}^{\mathrm{cen}}_G$](../concepts/central-affine-grassmannian.md) · [Gaitsgory 中心函子 $Z$](../concepts/gaitsgory-central-functor.md) · [从附近循环造出中心函子，并证明它 $t$-正合](../derivations/nearby-cycles-to-central.md)

## 出处（印刷页）

- A p.2–3（A p.2）

> 说明：定义与命题逐条对应 p.2–3；交换图 (3) 在 p.2。
