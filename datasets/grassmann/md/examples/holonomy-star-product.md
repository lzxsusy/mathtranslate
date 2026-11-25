# 和乐函数的星积与 Goldman 括号

> `grassmann/example/holonomy-star-product` · 轨道 1 · Hitchin 联络与 TQFT · 状态 draft

> **这张卡练什么**：两条曲线的和乐函数做星积，为什么首项是普通乘积、一阶修正却由 Goldman 括号给出？

## 一句话

把定理 8 的一阶星积公式用在两条曲线的和乐函数上，核对首项与 Goldman 括号项。

## 背景定义

设 $\gamma\subset\Sigma-\{p\}$ 为带标号 $\lambda$ 的简单闭曲线，$h_{\gamma,\lambda}$ 为对应的和乐函数。由形式平凡化定义 $$f\star g=P^{-1}\bigl(P(f)\tilde\star^{\mathrm{BT}}P(g)\bigr),$$ 称 $\star$ 为**和乐星积**；把它作用在两个和乐函数上，一阶项由 Goldman 括号 $\{\gamma_1,\gamma_2\}$ 给出。

## 设定

设 $\gamma_1,\gamma_2\subset\Sigma-\{p\}$ 是两条带标号的简单闭曲线，$h_{\gamma_i,\lambda_i}$ 为对应的和乐函数。取形式平凡化 $P_\sigma$，定义 $f\star g=P_\sigma^{-1}\bigl(P_\sigma(f)\tilde\star_\sigma^{\mathrm{BT}}P_\sigma(g)\bigr)$；由 $P$ 是平凡化可知 $\star$ 与 $\sigma$ 无关（命题 2）。

## 计算

定理 8 给 $f\star g=fg-\frac{i}{2}\{f,g\}h+O(h^2)$。取 $f=h_{\gamma_1,\lambda_1}$、$g=h_{\gamma_2,\lambda_2}$，用 Goldman 括号 $\{h_{\gamma_1,\lambda_1},h_{\gamma_2,\lambda_2}\}=h_{\{\gamma_1,\gamma_2\},\lambda_1\cup\lambda_2}$，得 $$h_{\gamma_1,\lambda_1}\star h_{\gamma_2,\lambda_2}=h_{\gamma_1,\lambda_1}h_{\gamma_2,\lambda_2}-\frac{i}{2}h_{\{\gamma_1,\gamma_2\},\lambda_1\cup\lambda_2}h+O(h^2).$$ 首项按 $c^{(0)}=fg$ 必须是乘积；中译 p.13（原书同页）该处印作 $h_{\gamma_1\gamma_2,\lambda_1\cup\lambda_2}$，与 $c^{(0)}=fg$ 及 $h_{\gamma_1}h_{\gamma_2}\ne h_{\gamma_1\gamma_2}$（相交时）都不相容。

## 要点

- 定理 8 的一阶项 $\{f,g\}$ 是 Poisson 括号，与 $c^{(1)}$ 的反对称化一致。
- Goldman 括号把两条曲线的相交数编码成第三条同伦类的和乐函数。
- 首项的两种写法只在 $\gamma_1=\gamma_2$ 等退化情形可能巧合一致；一般相交曲线不成立。
- 曲线算子乘积的渐近展开是这一公式的算子版本：$Z(\gamma_1)Z(\gamma_2)\sim T_{P(h_{\gamma_1})\tilde\star P(h_{\gamma_2})}$。

## 关键公式

$$
f\star g=fg-\tfrac{i}{2}\{f,g\}h+O(h^2)
$$

$$
\{h_{\gamma_1,\lambda_1},h_{\gamma_2,\lambda_2}\}=h_{\{\gamma_1,\gamma_2\},\lambda_1\cup\lambda_2}
$$

## 相关定理

- **定理 8**：由形式平凡化共轭得到的星积 $\star$ 满足 $f\star g=fg-\frac{i}{2}\{f,g\}h+O(h^2)$。

## 易错点

- 把首项写成 $h_{\gamma_1\gamma_2,\lambda_1\cup\lambda_2}$：中译 p.13 如此印刷，但 $c^{(0)}=fg$ 要求首项是 $h_{\gamma_1,\lambda_1}h_{\gamma_2,\lambda_2}$，相交曲线时二者不等（见 errata）。
- 把一阶项写成 $+\frac{i}{2}\{f,g\}h$：符号来自 $c^{(1)}(f,g)-c^{(1)}(g,f)=-i\{f,g\}$，反号会使 $f\star g-g\star f$ 变号。
- 直接用命题 3 的未修正表达式：原书在 876 行漏乘 $f_2$、$f_1$（译注 879），不修正则 $\nabla_{X_F''}$ 项无法在下一步消去。

## 用到哪些概念

- [Berezin–Toeplitz 形变量子化](../concepts/berezin-toeplitz-quantization.md)
- [曲线算子](../concepts/curve-operator.md)

## 相关卡

- [Berezin–Toeplitz 形变量子化](../concepts/berezin-toeplitz-quantization.md)
- [曲线算子](../concepts/curve-operator.md)
- [抛物丛与抛物次数](../concepts/parabolic-bundle.md)

## 出处

- ch1 §1 式 (6) 和乐星积；中译 p.13（英文 PDF p.16），源码 `chapters/ch01.tex:269`
