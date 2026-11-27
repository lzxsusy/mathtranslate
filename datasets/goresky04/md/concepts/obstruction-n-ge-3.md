# $n\ge3$ 的障碍：Shimura 簇不存在

> `goresky04/concept/obstruction-n-ge-3` · 轨道 C · 对应与障碍 · 状态 dev

> **先自测**：为什么把 $n=2$ 的证明照搬到 $n\ge3$ 会失效？

## 一句话

对 $n\ge3$，对应的 Shimura 簇不存在，模空间那一侧整个失效；原文说「这是本领域最大的谜团之一」。

## 定义

原文对 $n=3$ 写出类似的对象 $\GL(3,\bbQ)Z(\bbA)\backslash\GL(3,\bbA)/\sO(3)K_{\mathrm f}$，并指出它「根本不是代数簇，事实上它是一个（实）五维流形」。原因是：$\GL(3,\bbR)/(\sO(3)\cdot\bbR_{>0})$ 的维数是 $3\cdot2/2=3$，加上中心与紧子群后得到的商空间没有复结构。没有代数簇就没有平展上同调，Eichler–Shimura 的整条路线断掉。

**记号**：$\sO(3)$ 为 $\GL(3,\bbR)$ 的极大紧子群；$K_{\mathrm f}=\prod_p\GL(3,\bbZ_p)$。

## 要点（为什么需要它）

1. 缺的不是「信心」而是**几何对象**：$n=2$ 的证明是从模曲线的上同调读出 Galois 表示，$n\ge3$ 没有这个曲线。
2. 这不是技术困难，是结构性障碍：$\GL(n,\bbR)$ 的对称空间是 Hermitian 的当且仅当 $n=2$（对 $\GL(n)$ 而言）。
3. 几何朗兰兹的动机之一就是绕开这个障碍：不找 Shimura 簇，改在 $\Bun_G$ 上做几何（见 D 轨）。

## 核心公式

$$
$\GL(3,\bbQ)Z(\bbA)\backslash\GL(3,\bbA)/\sO(3)K_{\mathrm f}$：实五维流形，非代数簇$\dim\,\GL(3,\bbR)/(\sO(3)\cdot\bbR_{>0})=3$，加上中心与水平结构后总维数 $5$
$$

$$
$\dim\,\GL(3,\bbR)/(\sO(3)\cdot\bbR_{>0})=3$，加上中心与水平结构后总维数 $5$
$$

## 定理与证明（或缺口）

### 障碍（原文的观察）

对 $n\ge3$，$\GL(n)$ 的对称空间不是 Hermitian 对称空间，因此不存在与 $n=2$ 同类型的 Shimura 簇；Eichler–Shimura 路线不能直接推广。

> 证明状态：**sketch**。原文只写「根本不存在所需的 Shimura 簇」并称其为谜团；本卡按对称空间理论补出原因，原文没有展开。

出处：`A p.14`

## 常见误解

- 「$n\ge3$ 没有 Shimura 簇」不等于「$n\ge3$ 没有自守表示」：自守侧完全存在，缺的只是几何载体。
- 不要以为换个群就能绕开：原文 §8 说换群、换域、换范畴，但这已经离开「$\GL(n)$ 的原始猜想」，进入函子性与几何朗兰兹。

## 相关卡

[Shimura 簇：$n=2$ 的几何载体](../concepts/shimura-variety.md) · [Eichler–Shimura：$n=2$ 情形猜想的证明](../concepts/eichler-shimura-theorem.md) · [几何朗兰兹：把猜想搬到曲线上](../concepts/geometric-langlands.md)

## 出处（印刷页）

- A p.14–15（A p.14）

> 说明：对应原文 §7.2 全节；维数计算与 Hermitian 判据是译者按标准对称空间理论补的，原文只说结论。
