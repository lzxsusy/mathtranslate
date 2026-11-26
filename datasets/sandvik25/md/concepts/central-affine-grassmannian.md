# 中心仿射 Grassmann 簇 $\mathrm{Gr}^{\mathrm{cen}}_G$

> `sandvik25/concept/central-affine-grassmannian` · 轨道 A · 中心层与 Wakimoto 层 · 状态 dev

> **先自测**：中心仿射 Grassmann 簇的两条纤维各是什么，为什么它能同时承载仿射 Grassmann 簇与仿射旗簇？

## 一句话

一个带正则映射 $f\colon\mathrm{Gr}^{\mathrm{cen}}_G\to\mathbb C$ 的 ind-概形：一般纤维是 $\mathrm{Gr}_G$、特殊纤维是 $\mathrm{Fl}_G$，于是「仿射 Grassmann 簇形变到仿射旗簇」。

## 定义

$\mathrm{Gr}^{\mathrm{cen}}_G$ 是带正则映射 $f$ 的 ind-概形，满足 $f^{-1}(\mathbb C^\times)=\mathrm{Gr}_G\times\mathbb C^\times$ 与 $f^{-1}(0)=\mathrm{Fl}_G$。原文把 $f^{-1}(\mathbb C^\times)=\mathrm{Gr}_G\times\mathbb C^\times$ 与 $f^{-1}(0)=\mathrm{Fl}_G$ 两式并列（原文第二个 $\mathrm{Gr}^{\mathrm{cen},\times}_G$ 应为 $\mathrm{Gr}^{\mathrm{cen},0}_G$ 的排版笔误），并以之作为「$\mathrm{Gr}_G$ 到 $\mathrm{Fl}_G$ 的形变」。

**记号**：$\mathrm{Gr}_G=LG/L^+G$、$\mathrm{Fl}_G=LG/I$（fppf 层化）；$I$ 为对应 $B^-$ 的 Iwahori 子群。

## 要点（为什么需要它）

1. 整个构造的几何直觉：一般纤维上只有 $L^+G$ 的等变性、特殊纤维上多出 $I$ 的等变性，于是「从 $\mathrm{Gr}$ 走到 $\mathrm{Fl}$」= 从球等变降到 Iwahori 等变，正是 $p$ 进侧「从球 Hecke 走到 Iwahori Hecke」的几何翻译。
2. 它必须存在为一个**单一** ind-概形，否则附近循环无从谈起；原文脚注 5 说它可写成 $\mathbb A^1$ 上有限维簇的归纳极限。
3. 一般纤维是乘积 $\mathrm{Gr}_G\times\mathbb C^\times$ 而不是 $\mathrm{Gr}_G$：多出的 $\mathbb C^\times$ 正是 $\exp$ 的万有覆盖方向，$\Psi_f$ 的 $[-1]$ 位移就落在这里。
4. 定理 2.4.1(5) 用的映射 $\varpi\colon\mathrm{Gr}^{\mathrm{cen}}_G\to\mathrm{Gr}_G\times\mathbb C$ 不是 $f$：$\varpi$ 在 $\mathbb C^\times$ 纤维上是恒等、在 $0$ 纤维上退化为 $\pi\colon\mathrm{Fl}_G\to\mathrm{Gr}_G$。

## 核心公式

$$
$\mathrm{Gr}^{\mathrm{cen},\times}_G=f^{-1}(\mathbb C^\times)=\mathrm{Gr}_G\times\mathbb C^\times$$\mathrm{Gr}^{\mathrm{cen},0}_G=f^{-1}(0)=\mathrm{Fl}_G$
$$

$$
$\mathrm{Gr}^{\mathrm{cen},0}_G=f^{-1}(0)=\mathrm{Fl}_G$
$$

## 常见误解

- 原文 p.3 把特殊纤维一行也印成 $\mathrm{Gr}^{\mathrm{cen},\times}_G$，这是笔误；按上下文应为 $f^{-1}(0)=\mathrm{Fl}_G$。译本已改正并在译注中注明。
- 别把 $\mathrm{Gr}^{\mathrm{cen}}_G$ 当成 $\mathrm{Gr}_G\times\mathbb C$：后者的一般纤维是 $\mathrm{Gr}_G$、特殊纤维也是 $\mathrm{Gr}_G$，没有退化到 $\mathrm{Fl}_G$。

## 相关卡

[附近循环函子 $\Psi_f$](../concepts/nearby-cycles.md) · [Gaitsgory 中心函子 $Z$](../concepts/gaitsgory-central-functor.md)

## 出处（印刷页）

- A p.3（A p.3）

> 说明：两条纤维式出自 p.3；$\varpi$ 的构造在 p.4 定理 2.4.1 的证明里。
