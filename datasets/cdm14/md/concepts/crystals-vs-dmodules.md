# 晶体与 D-模：经典等价

> `cdm14/concept/crystals-vs-dmodules` · 轨道 E · 与 D-模的关系 · 状态 dev

> **先自测**：晶体为什么能取代 D-模，成为「奇异底空间上也能定义」的替代品？

## 一句话

经典有限型 $X$ 上，右晶体范畴等价于右 D-模的导出范畴，左晶体等价于左 D-模；等价与遗忘函子相容。

## 定义

设 $X$ 为经典有限型概形。定理（§5.5）：$\Crys^r(X)\simeq D\text{-}\mathrm{mod}^r(X)$，$\Crys^l(X)\simeq D\text{-}\mathrm{mod}^l(X)$。

**记号**：$D\text{-}\mathrm{mod}^r(X)$ 为右 D-模的导出范畴。

## 要点（为什么需要它）

1. 证明路线：Zariski 下降 → 经典 Kashiwara 化到光滑仿射 → 命题 2.4.4 化到左晶体/左 D-模 → 命题 4.7.3 化为心上的范畴 → 引理 5.4.3 比较单子。
2. 两条边都是「$\QCoh(X)^\heartsuit$ 上某个单子的模」：$\mathrm{Diff}_X$ 与 $\oblv^l\circ\ind^l$。
3. 等价与 $\oblv^r$、$\Psi_X$ 等遗忘函子相容（构造使然），故可逐层比较。
4. 注释 5.5.6：等价与光滑经典概形之间的拉回相容。

## 核心公式

$$\Crys^r(X)\simeq D\text{-}\mathrm{mod}^r(X),\qquad \Crys^l(X)\simeq D\text{-}\mathrm{mod}^l(X)$$

## 定理与证明（或缺口）

### 晶体–D-模等价（§5.5）

$X$ 经典有限型时，$\Crys^r(X)\simeq D\text{-}\mathrm{mod}^r(X)$。

> 证明状态：**sketch**。第 2 步「垂直箭头 t-正合」用到命题 4.7.3、2.4.4、4.4.2 三条，原文用图 (5.3) 一次性说明。

出处：`A p.47`

## 常见误解

- 等价是导出范畴的等价，不是 Abel 范畴的等价；心上等价才是第 4 步。
- 右晶体对应右 D-模，左对左；$\omega$ 的平移不要丢。
- 只对经典有限型 $X$；DG 概形上没有 D-模的经典定义。

## 相关卡

[核 $D^l_X$ 与微分算子层 $\mathrm{Diff}_X$](../concepts/diff-operators.md) · [$\Crys^r(X)$ 是其心上的导出范畴](../concepts/abelian-heart.md) · [§5.5 的证明：晶体 = D-模的六步](../derivations/cdm-equiv.md) · [$\Upsilon$：左晶体与右晶体的比较](../concepts/upsilon-comparison.md)

## 出处（印刷页）

- A p.47–49（A p.47）

> 说明：A=§5.5.1–5.5.6；最没把握处：等价与遗忘函子相容性的确切表述。
