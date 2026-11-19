# 经典形式光滑的预栈

> `cdm14/concept/classically-formally-smooth` · 轨道 A · de Rham 预栈与晶体定义 · 状态 dev

> **先自测**：为什么「形式光滑」要用 $\pi_0$ 上的满射来定义，而不是用切空间？

## 一句话

每个测试映射 $S\to Y$ 都能在 $S$ 的既约化上、沿幂零方向自由延伸的预栈；此时 $Y_{\mathrm{dR}}$ 由 Čech 神经算出。

## 定义

若对 $S\in\DGSch_{\mathrm{aff}}$，映射 $\Maps(S,Y)\to\Maps({}^{\mathrm{cl,red}}S,Y)$ 在 $\pi_0$ 上满，则称 $Y$ 经典形式光滑。

**记号**：$\pi_0\Maps(S,Y)\twoheadrightarrow\pi_0\Maps({}^{\mathrm{cl,red}}S,Y)$。

## 要点（为什么需要它）

1. 满射在 $\pi_0$ 上，意味着每条定义在既约部分的映射都能沿幂零方向延拓——这正是形式光滑的无穷小 lifting 性质。
2. 光滑概形、以及许多 ind-概形都满足此性质；它是 §2.5 Kashiwara 与 §4 若干 $t$-结构结论的前提。
3. 此时 $|Y_\bullet/Y_{\mathrm{dR}}|\to Y_{\mathrm{dR}}$ 是同构（引理 1.2.4），晶体可用 Čech 神经的全化来计算（引理 2.1.7、2.3.11）。
4. 条件只约束 $\pi_0$，不要求 $\Maps$ 的更高同伦群满。

## 核心公式

$$\pi_0\Maps(S,Y)\twoheadrightarrow\pi_0\Maps({}^{\mathrm{cl,red}}S,Y)$$

## 定理与证明（或缺口）

### Čech 神经覆盖 $Y_{\mathrm{dR}}$（引理 1.2.4）

若 $Y$ 经典形式光滑，则 $|Y_\bullet/Y_{\mathrm{dR}}|\to Y_{\mathrm{dR}}$ 是 $\PreStk$ 中的同构。

> 证明状态：**sketch**。第 2 步的「有截面」只在 $\pi_0$ 层面得到，把 $\pi_0$ 的提升拼成 $\infty$-群胚层面的同构，原文说「由定义可得」，未展开。

出处：`A p.13`

## 常见误解

- 不是「$Y$ 光滑」：$Y$ 可以是 ind-概形或形式完备化，只要无穷小延伸性质成立。
- 条件只要求 $\pi_0$ 满，不要求单，也不要求更高同伦群。
- $|Y_\bullet/Y_{\mathrm{dR}}|$ 是几何实现，不是普通余极限，别写成 $\mathrm{colim}$ 了事。

## 相关卡

[de Rham 预栈 $X_{\mathrm{dR}}$](../concepts/dr-prestack.md) · [无穷小群胚 $X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$](../concepts/infinitesimal-groupoid.md) · [Kashiwara 引理：闭浸入上的晶体即开补上为零的晶体](../concepts/kashiwara.md)

## 出处（印刷页）

- A p.13（A p.13）

> 说明：A=1.2.3–1.2.4；最没把握处：把「由定义可得」的证明补成两步。
