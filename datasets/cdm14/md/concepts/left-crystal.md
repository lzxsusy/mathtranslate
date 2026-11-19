# 左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$

> `cdm14/concept/left-crystal` · 轨道 B · 左/右晶体、IndCoh 与 Kashiwara · 状态 dev

> **先自测**：为什么左晶体的定义对任意预栈都成立，而右晶体要先假设 laft？

## 一句话

左晶体就是 de Rham 预栈上的拟凝聚层；它由「对每个 $S\to Y_{\mathrm{dR}}$ 给一个 $\QCoh(S)$ 中的对象」的下降数据描述。

## 定义

对任意预栈 $Y$，定义 $\Crys^l(Y):=\QCoh(Y_{\mathrm{dR}})=\lim_{S\in(\DGSch_{\mathrm{aff}}/Y_{\mathrm{dR}})^{\mathrm{op}}}\QCoh(S)$。等价地，$\Crys^l=\QCoh^*_{\PreStk}\circ\mathrm{dR}$，其中 $\QCoh^*_{\PreStk}$ 是把 $\QCoh$ 沿 $\DGSch_{\mathrm{aff}}\hookrightarrow\PreStk$ 作右 Kan 延拓。

**记号**：$\oblv^l_Y:\Crys^l(Y)\to\QCoh(Y)$；$f^{\dagger,l}:\Crys^l(Y_2)\to\Crys^l(Y_1)$。

## 要点（为什么需要它）

1. $\QCoh$ 对任意仿射 DG 概形都有定义，所以 $\Crys^l$ 不需要 laft 假设；右晶体要用 $\IndCoh$，才需要 laft 与最终余连接。
2. 下降描述：对象是给每个 $S\to Y_{\mathrm{dR}}$ 指定 $\mathcal F_S\in\QCoh(S)$，并对每个 $S'\to S$ 指定同构 $f^*(\mathcal F_S)\simeq\mathcal F_{S'}$，外加高阶融贯。
3. $f^{\dagger,l}$ 由 $\mathrm{dR}$ 的函子性与 $\QCoh^*$ 的拉回给出；若 $f$ 在既约经典预栈上已是同构，则 $f^{\dagger,l}$ 是等价（2.1.3）。
4. $Y$ 经典形式光滑时 $\Crys^l(Y)\simeq\mathrm{Tot}(\QCoh(Y_\bullet/Y_{\mathrm{dR}}))$（引理 2.1.7），这是把晶体当「无穷小 site 上的层」计算的入口。

## 核心公式

$$\Crys^l(Y):=\QCoh(Y_{\mathrm{dR}})=\lim_{S\in(\DGSch_{\mathrm{aff}}/Y_{\mathrm{dR}})^{\mathrm{op}}}\QCoh(S)$$

## 定理与证明（或缺口）

### 左晶体的下降描述（推论 2.1.4）

对 $\mathcal C\in\{\Sch_{\mathrm{aff}},\Sch_{\mathrm{aff,ft}},{}^{<\infty}\DGSch_{\mathrm{aff,aft}},\DGSch_{\mathrm{aff,aft}}\}$，$\Crys^l(Y)\to\lim_{X\in(\mathcal C_{/Y})^{\mathrm{op}}}\Crys^l(X)$ 是等价。

> 证明状态：**sketch**。共尾性到 $\mathcal C_{/Y}$ 的那一步依赖推论 1.3.7，原文只写「由推论 1.3.7 得到」。

出处：`A p.17`

## 常见误解

- $\oblv^l$ 只是遗忘函子，既不远忠也不保守（保守性要到 laft 情形才成立，引理 2.2.6）。
- 左晶体的拉回是 $f^*$ 型的，不是 $f^!$ 型——这是左右两套实现的第一处差别。
- 别把 $\Crys^l(Y)$ 与 $\QCoh(Y)$ 混同：$\mathrm{dR}$ 只保留无穷小信息，$\oblv^l$ 丢掉的是「沿 $Y\to Y_{\mathrm{dR}}$ 的下降数据」。

## 相关卡

[de Rham 预栈 $X_{\mathrm{dR}}$](../concepts/dr-prestack.md) · [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md) · [$\Upsilon$：左晶体与右晶体的比较](../concepts/upsilon-comparison.md) · [Kashiwara 引理：闭浸入上的晶体即开补上为零的晶体](../concepts/kashiwara.md)

## 出处（印刷页）

- A p.15–17（A p.15）
- A p.17–18（A p.17）

> 说明：A=§2.1–2.2 的定义与推论 2.1.4；最没把握处：下降数据里「高阶融贯」的准确表述。
