# 从模形式到平代环上的自守形式（(6.1.1)）

> `goresky04/deriv/adelic-equivalence` · 轨道 B · 自守侧 · 状态 dev · 5 步

> **要回答的问题**：为什么 $\SL(2,\bbZ)\backslash\he$ 与平代环的商是同一个空间？

## 一句话

把 $\SL(2,\bbZ)\backslash\he$ 写成 $\GL(2,\bbQ)Z(\bbA)\backslash\GL(2,\bbA)/\sO(2)K_{\mathrm f}$，模形式就变成平代环上的函数；这一步把古典对象交给整体表示论处理。

## 目标

证明 $X=\SL(2,\bbZ)\backslash\he\cong\GL(2,\bbQ)Z(\bbA)\backslash\GL(2,\bbA)/\sO(2)K_{\mathrm f}$，并说明模形式的自守条件在这个等同下怎么读。

## 前提

- $\GL(2,\bbA)=\GL(2,\bbR)\times\prod_p'\GL(2,\bbQ_p)$，$K_{\mathrm f}=\prod_p\GL(2,\bbZ_p)$。
- $\bbA$ 上的强逼近定理：$\GL(2,\bbQ)$ 在 $\GL(2,\bbA)$ 中的双陪集代表元可以取成有限平代部分。
- $\GL(2,\bbR)$ 的 Iwasawa 分解 $\GL(2,\bbR)=\sO(2)\cdot\bbR_{>0}\cdot N$，$\he\cong\GL(2,\bbR)/(\sO(2)\cdot\bbR_{>0})$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 先看实分量：$\he\cong\GL(2,\bbR)/(\sO(2)\cdot\bbR_{>0})$，左乘 $\GL(2,\bbR)$ 即 $\SL(2,\bbR)$ 在上半平面上的分式线性作用。 | 这给出「模形式定义在上半平面」的群论解释。 | `A p.11` | A·原文明确写了 |
| 2 | 加上有限平代分量：$\GL(2,\bbQ)$ 在 $\GL(2,\bbA)$ 中离散，$K_{\mathrm f}$ 是紧开子群，故 $\GL(2,\bbQ)\backslash\GL(2,\bbA)/K_{\mathrm f}$ 的连通成分对应到 $\SL(2,\bbZ)\backslash\he$ 的各个「层」。 | 有限素数的信息被 $K_{\mathrm f}$ 的固定向量吸收。 | `A p.11` | A·原文明确写了 |
| 3 | 取 $K_{\mathrm f}$-不变函数，等价于只依赖 $\GL(2,\bbR)$ 分量，即上半平面上的函数。 | 这一步把「整体对象」压回「古典对象」。 | `A p.11` | A·原文明确写了 |
| 4 | 再商掉中心 $Z(\bbA)$ 与 $\sO(2)$，得到 (6.1.1) 的等同。 | 中心与极大紧子群的作用不改变模形式的值。 | `A p.11` | B·原文暗示、我们补的中间步 |
| 5 | 在这个等同下，$\SL(2,\bbZ)$ 的自守因子对应到 $\sO(2)$ 的权作用，Hecke 算子 $T_p$ 对应到 $\GL(2,\bbQ_p)$ 上的双陪集算子。 | 说明等同不只保空间，还保算子。 | `A p.12` | B·原文暗示、我们补的中间步 |

## 结论

古典模形式与 $\GL(2,\bbA)$ 上的 $K_{\mathrm f}$-不变自守形式是同一批对象；Hecke 算子在两边对应，因此「特征值」这个概念在两边是同一个。

## 缺口

- 强逼近定理原文没有陈述，只在 (6.1.1) 前说「有一个自然的（虽然并不完全显然的）等同」；步 2 的离散性依赖它。

## 最容易讲错的地方

- 等同只在 $\GL(2)$ 上成立，$n\ge3$ 时 $\SL(n,\bbZ)\backslash\he_n$ 与平代商的对应仍成立，但缺少 Shimura 簇这个几何载体（见 §7.2）。
- 中心 $Z(\bbA)$ 不能随便去掉：不商掉它，$\GL(2,\bbQ)\backslash\GL(2,\bbA)$ 上的函数会多一个连续参数（中心特征）。

## 相关卡

[平代环与限制直积](../concepts/adele-ring.md) · [经典模形式](../concepts/modular-form-classical.md) · [自守形式与自守表示](../concepts/automorphic-representation.md)

## 出处（印刷页）

- A p.11–12（A p.11）

> 说明：步 1–3 对应原文 (6.1.1) 前的论述；步 4–5 的算子对应是译者按，原文只说「这个等同诱导同构」。
