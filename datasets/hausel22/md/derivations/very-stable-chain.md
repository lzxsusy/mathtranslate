# 非常稳定的四重等价链

> `hausel22/deriv/very-stable-chain` · 轨道 D · 幂零锥上的等变重数 · 状态 dev · 5 步

> **要回答的问题**：定理 3.2 与定理 3.3 的四个条件为什么能连成一条链？

## 一句话

从「上行流与芯只交于自身」出发，经闭性、$0$-纤维条件，逐步得到 Hitchin 映射在流上的 proper 性与有限性。

## 目标

把「非常稳定」「$W^+_\calE$ 闭」「$h^{-1}(0)\cap W^+_\calE=\{\calE\}$」「$h_\calE$ proper」「$h_\calE$ 有限」串成等价链。

## 前提

- $\calE\in\M^{s\T}$ 是光滑轨迹上的 $\T$-不动点，$W^+_\calE$ 是它的上行流。
- 芯 $\calC=\coprod_{\alpha}W^-_\alpha$ 是全部下行流之并，在 $\M$ 上其原像为幂零锥 $h^{-1}(0)_{red}$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 定义：$\calE$ 非常稳定 ⟺ $W^+_\calE\cap\calC=\{\calE\}$ ⟺ 不存在 $\beta\neq\calE$ 使 $W^+_\calE\cap W^-_\beta\neq\emptyset$。 | 芯是全部下行流之并，故与芯的交只含自身等价于与任何别的下行流不相交；后者又等价于 $\calE$ 在偏序 $\alpha\le\beta\iff W^+_\alpha\cap W^-_\beta\neq\emptyset$ 下的极大性。 | `A p.2236` | A·原文明确写了 |
| 2 | $\calE$ 非常稳定 ⟺ $W^+_\calE\subset X$ 闭。 | BB 分解是局部闭分解，流的边界必落在别的流中；非常稳定排除了这种边界，故闭。反之闭性迫使与紧的 $\calC$ 交成单点。 | `A p.2237` | A·原文明确写了 |
| 3 | $\calE$ 非常稳定 ⟺ $h^{-1}(0)\cap W^+_\calE=\{\calE\}$。 | $h^{-1}(0)$ 正是芯的原像（幂零锥），把第 1 步的定义改写即可。 | `A p.2238` | A·原文明确写了 |
| 4 | $\calE$ 非常稳定 ⟺ $h_\calE:W^+_\calE\to\calA$ proper。 | $h_\calE$ 的纤维是 $W^+_\calE$ 与 Hitchin 纤维的交；若 $0$-纤维是单点，则一般纤维有限，从而映射 proper。 | `A p.2238` | A·原文明确写了 |
| 5 | proper ⟺ 有限。 | 有限映射必 proper；反之在仿射靶上 proper 且拟有限即为有限（$\calA$ 是仿射空间，$h_\calE$ 拟有限由纤维有限给出）。 | `A p.2238` | B·原文暗示、我们补的中间步 |

## 结论

$\calE$ 非常稳定 ⟺ $W^+_\calE$ 闭 ⟺ $h^{-1}(0)\cap W^+_\calE=\{\calE\}$ ⟺ $h_\calE$ proper ⟺ $h_\calE$ 有限。

## 缺口

- 第 4 步「$0$-纤维单点 ⇒ 一般纤维有限 ⇒ proper」的推理原文只给结论，未证；$\T$-等变性把问题化归到 $0$ 纤维这一步也未写出。
- 第 5 步 proper ⇒ 有限 需要拟有限性，原文未单独说明。

## 最容易讲错的地方

- proper 性指的是限制映射 $h_\calE:W^+_\calE\to\calA$，不是整个 $h:\M\to\calA$。
- 闭性是 $W^+_\calE$ 在 $\M$ 中的闭性（Zariski 拓扑），不是「紧」；$\M$ 本身非紧。
- 四个条件的等价只在 $\calE\in\M^{s\T}$ 时成立，非光滑点处 BB 性质本身就可能失效。
- 把 $h^{-1}(0)$ 与芯混淆：芯是 $\M$ 的子簇，$h^{-1}(0)$ 是它的原像（取既约结构后两者常被等同，但严格说是原像）。

## 相关卡

[非常稳定 Higgs 丛](../concepts/very-stable-higgs-bundle.md) · [Białynicki–Birula 分解与上行流](../concepts/bialynicki-birula-attraction.md) · [等变重数 $m_\calE(t)$](../concepts/equivariant-multiplicity.md)

## 出处（印刷页）

- A p.2237（A p.2237）
- A p.2238（A p.2238）

> 说明：A=原文 §3.1.1 的定义与定理 3.2、§3.1.2 的定理 3.3；B=第 5 步 proper ⇔ 有限 的标准论证是我们补的；C=第 2 步「反之」方向我们按 BB 分解的局部闭性补全。最没把握处：第 4 步由 $0$-纤维推广到一般纤维的等变论证，原文未写。
