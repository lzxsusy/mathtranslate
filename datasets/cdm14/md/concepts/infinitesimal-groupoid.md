# 无穷小群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$

> `cdm14/concept/infinitesimal-groupoid` · 轨道 C · 下降性质与归纳函子 · 状态 dev

> **先自测**：为什么晶体可以用这个群胚上的「等变层」来计算？

## 一句话

$X\to X_{\mathrm{dR}}$ 的 Čech 神经给出群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$，它的每一项是主对角线的形式完备化。

## 定义

设 $X\in\DGIndSch_{\mathrm{laft}}$。令 $X_\bullet/X_{\mathrm{dR}}$ 为 $X\to X_{\mathrm{dR}}$ 的 Čech 神经；每一项 $X_i/X_{\mathrm{dR}}$ 是 $X_i$ 沿主对角线的形式完备化。称 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$ 为 $X$ 的无穷小群胚。

**记号**：$p_s,p_t:X\times_{X_{\mathrm{dR}}}X\to X$ 为两个投影。

## 要点（为什么需要它）

1. 群胚的两个结构映射 $p_s,p_t$ 都是 ind-固有的，因此 $p_i^!$ 有左伴随 $(p_i)_*^{\IndCoh}$（[GR1, 推论 2.8.3]）。
2. 命题 3.1.3：$\Crys^r(X)\to\mathrm{Tot}(\IndCoh(X_\bullet/X_{\mathrm{dR}}))$ 是等价——晶体就是该群胚上的「全化等变层」。
3. 证明的关键：对每个 $S\to X_{\mathrm{dR}}$，$S\times_{X_{\mathrm{dR}}}X\to S$ 是 ind-固有且满的（3.1），再用 [GR1, 引理 2.10.3] 的 $\IndCoh$ 下降。
4. 这个群胚把「无穷小接近」编码成几何对象：两个 $S$-点无穷小接近，当且仅当它们在 $X_{\mathrm{dR}}$ 中的像相同。

## 核心公式

$$X\times_{X_{\mathrm{dR}}}X\;\rightrightarrows\;X,\qquad \Crys^r(X)\xrightarrow{\sim}\mathrm{Tot}\big(\IndCoh(X_\bullet/X_{\mathrm{dR}})\big)$$

## 定理与证明（或缺口）

### 晶体是群胚上的全化等变层（命题 3.1.3）

对 $X\in\DGIndSch_{\mathrm{laft}}$，$\Crys^r(X)\to\mathrm{Tot}(\IndCoh(X_\bullet/X_{\mathrm{dR}}))$ 是等价。

> 证明状态：**sketch**。第 1 步「ind-固有满」的验证依赖形式完备化的具体模型，原文只引 [GR1]。

出处：`A p.26`

## 常见误解

- 这不是通常的群胚（对象层面），而是 $\infty$-群胚对象；「等变」要理解为全化，不是取不变子对象。
- $X$ 可以是 ind-概形，此时 $X_\bullet/X_{\mathrm{dR}}$ 的每一项仍是 DG ind-概形，不是概形。

## 相关卡

[右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md) · [晶体满足 h-下降](../concepts/h-descent.md) · [右晶体的归纳函子 $\ind^r_X$](../concepts/induction-right.md)

## 出处（印刷页）

- A p.25–26（A p.25）
- A p.26（A p.26）

> 说明：A=§3.1 的定义与命题 3.1.3；最没把握处：$X$ 为 ind-概形时形式完备化的层次。
