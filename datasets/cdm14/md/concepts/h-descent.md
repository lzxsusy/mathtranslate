# 晶体满足 h-下降

> `cdm14/concept/h-descent` · 轨道 C · 下降性质与归纳函子 · 状态 dev

> **先自测**：为什么晶体的定义自动带来下降，而不需要额外公理？

## 一句话

$\Crys^r$ 把 h-拓扑（Zariski + 固有满）的覆盖送到全化极限；特别地满足 fppf 下降。

## 定义

$\DGSch_{\mathrm{aff,aft}}$ 上的 h-拓扑由 Zariski 覆盖与固有满覆盖生成。称函子 $\mathcal F$ 满足 h-下降，若对每个 h-覆盖 $S'\to S$，$\mathcal F(S)\to\mathrm{Tot}(\mathcal F(S'^\bullet/S))$ 是等价。

**记号**：$\Crys^r$ 视为 $(\DGSch_{\mathrm{aff,aft}})^{\mathrm{op}}\to\DGCat_{\mathrm{cont}}$ 的函子。

## 要点（为什么需要它）

1. 命题 3.2.2：$\Crys^r|_{\DGSch_{\mathrm{aff,aft}}}$ 满足 h-下降；平展下降显然（$\IndCoh$ 的 fppf 下降 [IndCoh, 推论 10.4.5]），固有满下降用双单纯对象与命题 3.1.3 两次。
2. 推论 3.2.4：满足 fppf 下降；推论 3.2.6：在 ${}^{<\infty}\DGSch_{\mathrm{aff,aft}}$ 上同样成立。
3. 推论 3.2.7：若 $Y_1\to Y_2$ 是 h-拓扑满射，则 $\Crys(Y_2)\to\mathrm{Tot}(\Crys(Y_1^\bullet/Y_2))$ 是等价（[Lu0, 推论 6.2.3.5]）。
4. 下降是后面所有「局部化到仿射、光滑、形式完备化」论证的许可证。

## 核心公式

$$\Crys^r(S)\xrightarrow{\sim}\mathrm{Tot}\big(\Crys^r(S'^\bullet/S)\big)\quad\text{对 h-覆盖 }S'\to S$$

## 定理与证明（或缺口）

### h-下降（命题 3.2.2）

函子 $\Crys^r:\DGSch_{\mathrm{aff,aft}}^{\mathrm{op}}\to\DGCat_{\mathrm{cont}}$ 满足 h-下降。

> 证明状态：**sketch**。第 2 步的双单纯对象构造在原文占一整段，这里只记其形状；交错方向与全化次序需照原文核对。

出处：`A p.26`

## 常见误解

- h-拓扑不是 fppf：固有满覆盖不是平展的，两者要分别处理再合并。
- 下降陈述里的 $\mathrm{Tot}$ 是 $\Crys^r$ 值的全化，不是 $\IndCoh$ 值的全化——两者由命题 3.1.3 联系。

## 相关卡

[无穷小群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$](../concepts/infinitesimal-groupoid.md) · [h-下降的证明：双单纯对象与两次全化](../derivations/h-descent-proof.md) · [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md)

## 出处（印刷页）

- A p.26–28（A p.26）

> 说明：A=§3.2 的命题 3.2.2 与三个推论；最没把握处：双单纯对象的下标方向。
