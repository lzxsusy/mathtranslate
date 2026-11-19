# 左晶体的归纳函子与最终余连接假设

> `cdm14/concept/induction-left` · 轨道 C · 下降性质与归纳函子 · 状态 dev

> **先自测**：为什么左晶体需要「最终余连接」这个额外假设？

## 一句话

左晶体一般不能写成 $\QCoh$ 的全化；只有最终余连接的 DG 概形才成立，此时可借 $\Upsilon$ 定义 $\ind^l_X$。

## 定义

对最终余连接的 DG 概形 $X$，定义 $\ind^l_X:=(\Upsilon_{X_{\mathrm{dR}}})^{-1}\circ\ind^r_X\circ\Upsilon_X:\QCoh(X)\to\Crys^l(X)$。

**记号**：$\Upsilon_X:\QCoh(X)\to\IndCoh(X)$ 为 $\otimes\omega_X$。

## 要点（为什么需要它）

1. 光滑经典 $X$ 时 $\Crys^l(X)\simeq\mathrm{Tot}(\QCoh(X_\bullet/X_{\mathrm{dR}}))$（引理 1.2.4 的直接推论）；一般 DG 概形不成立。
2. 反例：$X=\Spec(k[\alpha])$，$\deg\alpha=-2$（例 3.4.5）——非最终余连接时 $\QCoh$ 的全化会漏掉信息。
3. 命题 3.4.3：$X$ 最终余连接时 $\Crys^l(X)\to\mathrm{Tot}(\QCoh(X_\bullet/X_{\mathrm{dR}}))$ 是等价。
4. 引理 3.4.7：此时 $(\ind^l_X,\oblv^l_X)$ 是伴随对；命题 3.4.11：还是单子的。

## 核心公式

$$\ind^l_X:=(\Upsilon_{X_{\mathrm{dR}}})^{-1}\circ\ind^r_X\circ\Upsilon_X,\qquad \ind^l_X\dashv\oblv^l_X$$

## 定理与证明（或缺口）

### 最终余连接时的全化等价（命题 3.4.3）

$X$ 最终余连接的 DG 概形时，$\Crys^l(X)\to\mathrm{Tot}(\QCoh(X_\bullet/X_{\mathrm{dR}}))$ 是等价。

> 证明状态：**sketch**。第 2 步「收缩」的确切含义（$\Upsilon$ 的右伴随 $\Xi^\vee$ 的作用）原文只引用 [IndCoh]。

出处：`A p.29`

## 常见误解

- 最终余连接不能去掉：例 3.4.5 就是反例。
- $\ind^l_X$ 的定义依赖 $\Upsilon$ 可逆，所以只在有等价的地方可用。
- 去掉最终余连接后 $\ind^l_X$ 仍可定义，但不再是 $\oblv^l_X$ 的左伴随（注 4.6.10）。

## 相关卡

[左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](../concepts/left-crystal.md) · [右晶体的归纳函子 $\ind^r_X$](../concepts/induction-right.md) · [$\Upsilon$：左晶体与右晶体的比较](../concepts/upsilon-comparison.md) · [粗糙归纳与 Gorenstein 条件](../concepts/coarse-induction.md)

## 出处（印刷页）

- A p.29–30（A p.29）

> 说明：A=§3.4 的命题 3.4.3、3.4.6、3.4.11 与例 3.4.5；最没把握处：第 2 步「收缩」的准确机制。
