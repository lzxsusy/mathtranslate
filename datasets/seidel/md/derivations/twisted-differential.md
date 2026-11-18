# 扭曲复形的微分为何平方为零

> `seidel/deriv/twisted-differential` ｜ track A ｜ draft

**目标**：证明：在 $\Tw\A$ 中，$d_T=d+\delta$ 满足 $d_T^2=0$ 当且仅当 $\delta$ 满足广义 Maurer–Cartan 方程。

**自测**：为什么扭曲复形的微分不是 $d+\delta$ 的简单相加，而要求 $\delta$ 解 MC 方程？

## 前提

- $\A$ 是 A∞ 范畴，$X=\bigoplus_i V^i\otimes X_i$，$\delta\in\hom^1(X,X)$ 严格下三角。
- $\Tw\A$ 的复合由 $\A$ 的 $\mu^r$ 与张量因子的组合给出（原书 (3.20)）。

## 步骤

1. **$d_T^2=(d+\delta)^2=d^2+d\delta+\delta d+\delta^2$。**  
   为什么：直接展开；$d$ 是 $\A$ 诱导的微分。  
   锚点：原书 p.44 §3l（证据 A）

2. **$d^2=0$ 且 $d\delta+\delta d$ 是 $\delta$ 的微分 $d_{\Tw}\delta$。**  
   为什么：$\Tw\A$ 的微分按分次 Leibniz 规则作用。  
   锚点：原书 p.44 §3l（证据 A）

3. **$\delta^2$ 不是零：它等于 $\mu^2(\delta,\delta)$ 加上高阶修正；一般地，$d_T^2=\sum_{r\ge1}\mu^r(\delta,\ldots,\delta)$。**  
   为什么：这是 $\Tw\A$ 复合公式 (3.20) 的直接推论；$r$ 项对应 $\delta$ 的 $r$ 次复合。  
   锚点：原书 p.44 §3l（证据 B）

4. **故 $d_T^2=0$ 等价于 $\sum_{r\ge1}\mu^r(\delta,\ldots,\delta)=0$，即 $\delta$ 的 MC 方程。**  
   为什么：移项即得；严格下三角保证求和有限。  
   锚点：原书 p.44 §3l（证据 A）

## 结果

$d_T^2=0\iff \delta$ 满足广义 MC 方程；这就是扭曲复形的定义条件。

## 缺口

- 下三角性是求和有限的关键；一般 $\delta$ 的 MC 方程只是形式级数。

## 易错点

- 把 $\delta^2$ 当成零会漏掉 $\mu^2(\delta,\delta)$ 项，锥的微分就不再平方为零。
- $d\delta+\delta d$ 的符号依赖 $\delta$ 的次数为 $1$；写成 $d\delta-\delta d$ 会错。
- MC 方程含所有 $r\ge1$，不只是 $d\delta+\delta^2$；高阶项在 $\A$ 非 dg 时出现。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§3l，p.43–44（原书 p.43–44 §3l）

关联：`seidel/concept/twisted-complex`、`seidel/deriv/mapping-cone`、`seidel/concept/a-infinity-category`

来源说明：据原书 §3l（p.43–44）与译者注 A05-09 转述；(3.20) 的展开为本书约定下的标准计算。
