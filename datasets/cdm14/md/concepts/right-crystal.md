# 右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$

> `cdm14/concept/right-crystal` · 轨道 B · 左/右晶体、IndCoh 与 Kashiwara · 状态 dev

> **先自测**：右晶体为什么必须用 $\IndCoh$ 而不能用 $\QCoh$？

## 一句话

右晶体是 de Rham 预栈上的归纳凝聚层，用 $f^!$ 作拉回；它比左晶体多了 $t$-结构与推前的函子性。

## 定义

设 $Y\in\PreStk_{\mathrm{laft}}$。定义 $\Crys^r(Y):=\IndCoh^!_{Y_{\mathrm{dR}}}=\lim_{S\in(({}^{<\infty}\DGSch_{\mathrm{aff,aft}})_{/Y_{\mathrm{dR}}})^{\mathrm{op}}}\IndCoh(S)$。对象是给每个 $S\to Y_{\mathrm{dR}}$ 指定 $\mathcal F_S\in\IndCoh(S)$，并对每个 $f:S'\to S$ 指定同构 $f^!(\mathcal F_S)\simeq\mathcal F_{S'}$。

**记号**：$\oblv^r_Y:\Crys^r(Y)\to\IndCoh(Y)$；$f^{\dagger,r}:\Crys^r(Y_2)\to\Crys^r(Y_1)$。

## 要点（为什么需要它）

1. $\IndCoh$ 的推前是 $*$-推前、拉回是 $!$-拉回，恰好给出右 D-模所需的函子性；$\QCoh$ 给不出。
2. $\Crys^r$ 的拉回 $f^{\dagger,r}$ 与 $\oblv^r$ 及 $f^!$ 交换（2.3.10 的方块 (2.3)）。
3. $\oblv^r$ 保守（引理 2.3.12）：一个右晶体是否为零，可以逐点用 $\IndCoh$ 判断。
4. $Y$ 经典形式光滑时 $\Crys^r(Y)\simeq\mathrm{Tot}(\IndCoh(Y_\bullet/Y_{\mathrm{dR}}))$（引理 2.3.11）。

## 核心公式

$$\Crys^r(Y)=\lim_{S\in(({}^{<\infty}\DGSch_{\mathrm{aff,aft}})_{/Y_{\mathrm{dR}}})^{\mathrm{op}}}\IndCoh(S)$$

## 定理与证明（或缺口）

### $\oblv^r$ 保守（引理 2.3.12）

函子 $\oblv^r_Y:\Crys^r(Y)\to\IndCoh(Y)$ 保守：$\oblv^r_Y(\mathcal M)\simeq0$ 蕴含 $\mathcal M\simeq0$。

> 证明状态：**sketch**。第 3 步「全化的保守性」原文只引用 [GR1] 与 [IndCoh]，未写出谱序列。

出处：`A p.21`

## 常见误解

- 右晶体的拉回是 $f^!$，不是 $f^*$：$f^!$ 只对最终余连接的态射才与 $\IndCoh$ 相容。
- $\Crys^r$ 的下标必须限制在 eventually coconnective 的仿射 DG 概形：非最终余连接时 $\IndCoh$ 的极限性质会坏。
- 右晶体不是「支撑在闭子概形上的层」；Kashiwara 给出的是「在开补上为零」的刻画。

## 相关卡

[左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](../concepts/left-crystal.md) · [$\Upsilon$：左晶体与右晶体的比较](../concepts/upsilon-comparison.md) · [Kashiwara 引理：闭浸入上的晶体即开补上为零的晶体](../concepts/kashiwara.md) · [右 $t$-结构：晶体上的「那个」$t$-结构](../concepts/right-t-structure.md)

## 出处（印刷页）

- A p.18–21（A p.18）

> 说明：A=§2.3 定义、引理 2.3.11/2.3.12；最没把握处：保守性证明第三步的谱序列收敛。
