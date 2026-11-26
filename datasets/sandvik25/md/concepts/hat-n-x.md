# 无穷小稳定化子 $\widehat{\mathcal N}$ 与 $\widehat{\mathcal N}_X$

> `sandvik25/concept/hat-n-x` · 轨道 B · Springer 侧与三造函子 · 状态 dev

> **先自测**：$\widehat{\mathcal N}_X$ 是怎么从 $\widetilde{\mathcal N}$ 造出来的，图 (4) 中三种映射各自负责什么？

## 一句话

把 $G^\vee/U^\vee$ 仿射完备化为 $X=\mathrm{Spec}\,\mathcal O(G^\vee/U^\vee)$，其无穷小万有稳定化子是 $\widehat{\mathcal N}_X$；$\widehat{\mathcal N}\subset\widehat{\mathcal N}_X$ 是开子簇，且 $\widehat{\mathcal N}$ 是 $\widetilde{\mathcal N}$ 上的 $T^\vee$-torsor。

## 定义

记 $\widehat{\mathcal N}$ 为 $\widetilde{\mathcal N}$ 在 $\mathfrak g^\vee\times_{G^\vee/U^\vee}\to G^\vee/B^\vee$ 下的原像；$X:=\mathrm{Spec}(\mathcal O(G^\vee/U^\vee))$ 为 $G^\vee/U^\vee$ 的仿射完备化，$G^\vee/U^\vee\subset X$ 开，$\partial X:=X\setminus G^\vee/U^\vee$。$G^\vee$ 在 $G^\vee/U^\vee$ 上作用的无穷小万有稳定化子即 $\widehat{\mathcal N}$；在 $X$ 上作用的无穷小万有稳定化子记为 $\widehat{\mathcal N}_X$，它是 $\mathfrak g^\vee\times X$ 的闭子概形，含 $\widehat{\mathcal N}$ 为开子簇。

**记号**：$\mathrm{Coh}^{G^\vee\times T^\vee}_{\mathrm{free}}(\widehat{\mathcal N}_X)$ 为形如 $V\otimes\mathcal O_{\widehat{\mathcal N}_X}$（$V\in\mathrm{Rep}(G^\vee\times T^\vee)$）的自由对象构成的全加法子范畴。

## 要点（为什么需要它）

1. 图 (4) 的三条边各有分工：$\widehat{\mathcal N}\to\widetilde{\mathcal N}$ 是 $T^\vee$-torsor（提供 $T^\vee$ 作用与权分解），$\widehat{\mathcal N}\hookrightarrow\widehat{\mathcal N}_X$ 是开浸入（提供可去掉的边界），三个竖直箭头都是闭浸入（提供支撑条件）。
2. 为什么要完备化：$G^\vee/U^\vee$ 本身不是仿射的，凝聚层没有足够好的整体截面；换成 $X$ 才能把 $\mathcal O(\widehat{\mathcal N}_X)$ 当交换代数用（§3.3 的 Tannakian 构造就靠它）。
3. $\partial X$ 是「被丢掉的部分」：命题 3.1.2 的商恰好按 $\partial X$ 上的支撑作零化，这就是等价能成立的关键。
4. $\mathrm{Coh}_{\mathrm{free}}$ 的下标 free 不是装饰：只有自由的 $V\otimes\mathcal O$ 才与表示范畴对应，一般凝聚层不在 Tannakian 像里。

## 核心公式

$$
$X=\mathrm{Spec}(\mathcal O(G^\vee/U^\vee)),\qquad \partial X=X\setminus G^\vee/U^\vee$$\widehat{\mathcal N}\to\widetilde{\mathcal N}$ 为 $T^\vee$-torsor，$\widehat{\mathcal N}\hookrightarrow\widehat{\mathcal N}_X$ 为开浸入
$$

$$
$\widehat{\mathcal N}\to\widetilde{\mathcal N}$ 为 $T^\vee$-torsor，$\widehat{\mathcal N}\hookrightarrow\widehat{\mathcal N}_X$ 为开浸入
$$

## 定理与证明（或缺口）

### 命题 3.1.2（去边界得等价）

有函子 $K^b\mathrm{Coh}^{G^\vee\times T^\vee}_{\mathrm{free}}(\widehat{\mathcal N}_X)\to\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$，它唯一地穿过三角范畴的等价 $K^b\mathrm{Coh}^{\dots}_{\mathrm{free}}(\widehat{\mathcal N}_X)/K^b\mathrm{Coh}^{\dots}_{\mathrm{free}}(\widehat{\mathcal N}_X)_{\partial X}\xrightarrow{\sim}\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$。

> 证明状态：**sketch**。第 2 步原文不写细节；$\partial X$-支撑的商与 $\widehat{\mathcal N}\subset\widehat{\mathcal N}_X$ 的开性互补，是这一步的实质内容。

出处：`A p.6`

## 常见误解

- $\widehat{\mathcal N}$ 与 $\widehat{\mathcal N}_X$ 只差一个边界，但范畴层面差别很大：前者只带 $T^\vee$ 的 torsor 结构，后者才是仿射的、可取其函数环。
- 「自由」是范畴层面的条件（对象形如 $V\otimes\mathcal O$），不是几何上的局部自由性；不要按字面理解成向量丛。

## 相关卡

[Springer 解消 $\widetilde{\mathcal N}$ 与线丛 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$](../concepts/springer-resolution.md) · [函子 II：经 Tannakian 重构把 $F_1$ 扩到 $\mathrm{Coh}_{\mathrm{free}}(\widehat{\mathcal N}_X)$](../concepts/functor-f2.md)

## 出处（印刷页）

- A p.6–7（A p.6）

> 说明：对象定义、图 (4) 与命题 3.1.2 在 p.6，证明开头与脚注 8 在 p.7。
