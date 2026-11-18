# Hurwitz 移动与变异

> `seidel/deriv/mutation` ｜ track C ｜ draft

**目标**：说明：沿匹配路径的 Hurwitz 移动在消失圈层面是 Dehn twist，在范畴层面是例外聚集的变异。

**自测**：为什么辫群作用下的 Hurwitz 移动，恰好是例外聚集的变异？

## 前提

- Lefschetz 纤维化 $\pi:X\to\C$，临界值 $z_1,\ldots,z_m$，匹配路径连接它们。
- 消失圈 $V_i$ 构成 $\F(X_{t_0})$ 的例外聚集。

## 步骤

1. **两条匹配路径若只差一次 Hurwitz 移动，则对应的消失圈相差一次 Dehn twist。**  
   为什么：Hurwitz 移动是辫群关系的几何实现；Dehn twist 是 monodromy。  
   锚点：原书 p.272 §17k（证据 B）

2. **在 $H^0(\Tw\B)$ 中，沿 $V_i$ 的 Dehn twist 对应变异函子 $\mathbb{L}_{V_i}$。**  
   为什么：这是 Seidel 的「Dehn twist = 变异」定理。  
   锚点：原书 p.272 §17k（证据 B）

3. **变异把例外聚集 $(V_1,\ldots,V_m)$ 换成另一个例外聚集，且保持生成的三角范畴。**  
   为什么：变异是三角范畴的自等价。  
   锚点：原书 p.272 §17k（证据 B）

4. **故 PL 数据的 Hurwitz 移动与范畴数据的变异是同一操作的两面。**  
   为什么：两边都由同一个 Dehn twist 驱动。  
   锚点：原书 p.272 §17k（证据 B）

## 结果

Hurwitz 移动 $\leftrightarrow$ 变异；PL 组合数据与 Fukaya 范畴的代数数据由此对应。

## 缺口

- 变异依赖例外对象的选择；不同选择给出不同的变异函子。

## 易错点

- Dehn twist 与变异相差一个平移/符号约定，比较时须统一。
- Hurwitz 移动作用在匹配路径上，不作用在临界值本身。
- 例外聚集的变异不是逐对象的直和操作，而是锥的替换。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§17k，p.272–273（原书 p.272 §17k）

关联：`seidel/concept/matching-cycle`、`seidel/concept/vanishing-cycle`、`seidel/deriv/lefschetz-induction`

来源说明：据原书 §17k（p.272–273）转述；「Dehn twist = 变异」的完整陈述见 §17。
