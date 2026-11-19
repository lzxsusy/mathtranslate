# 全书总览：晶体是 de Rham 预栈上的层

> `cdm14/concept/overview` · 轨道 总览 · 状态 dev

> **先自测**：为什么把晶体定义成 $X_{\mathrm{dR}}$ 上的层，而不是先定义平坦连接？

## 一句话

把晶体定义为 de Rham 预栈上的（归纳）凝聚层，在导出代数几何里重建左/右 D-模、t-结构与扭化。

## 定义

对预栈 $X$，左晶体是 $X_{\mathrm{dR}}$ 上的拟凝聚层，右晶体是 $X_{\mathrm{dR}}$ 上的归纳凝聚层；$X_{\mathrm{dR}}$ 是把测试环先约化、再取 $X$ 的预栈。

**记号**：$X_{\mathrm{dR}}(S)=X({}^{\mathrm{cl,red}}S)$；$\Crys^l(X)=\QCoh(X_{\mathrm{dR}})$，$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$。

## 要点（为什么需要它）

1. 光滑簇上左晶体范畴等价于左 D-模（§5.5），所以晶体是 D-模的导出推广：奇异底空间、非线性对象都能定义。
2. 右晶体必须用 $\IndCoh$：右实现的 $t$-结构与推前函子性更好（§0.2、§4.2）。
3. 任意 DG 概形上左右晶体经 $\Upsilon$ 等价（命题 2.4.4），于是 $\Crys(X)$ 带两个实现，拉回 $f^\dagger$ 同时与 $f^*$、$f^!$ 相容。
4. 本文只做局部理论：拉回、下降、两个 $t$-结构、与 D-模的等价；推前 $f_{\mathrm{dR},*}$ 与 correspondence 范畴留待 [GR2]。
5. 扭化（§6）把 gerbe 的数据加到 $X_{\mathrm{dR}}$ 上，扭晶体（§7）是带这种 twist 的晶体。

## 核心公式

$$\Crys^l(X):=\QCoh(X_{\mathrm{dR}}),\qquad \Crys^r(X):=\IndCoh(X_{\mathrm{dR}})$$

## 定理与证明（或缺口）

### 晶体与 D-模（经典情形）

$X$ 为经典有限型概形时，$\Crys^r(X)$ 等价于右 D-模的导出范畴，$\Crys^l(X)$ 等价于左 D-模的导出范畴。

> 证明状态：**sketch**。第 2 步的「化为单子的模」在原文 §5.5.5 只是一句话，细节散在命题 4.7.3 与 §5.4。

出处：`A p.47`

## 常见误解

- 晶体不是「带平坦连接的向量丛」：它允许奇异底空间、允许取值在层的范畴里。
- 左、右晶体的 $t$-结构相差一个维数平移（命题 4.4.2），混用会把 $\le 0$ 与 $\le -n$ 搞反。
- $\Crys(X)$ 的「两个实现」不是两个不同范畴，而是同一范畴的两条遗忘函子。

## 相关卡

[de Rham 预栈 $X_{\mathrm{dR}}$](../concepts/dr-prestack.md) · [左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](../concepts/left-crystal.md) · [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md) · [晶体与 D-模：经典等价](../concepts/crystals-vs-dmodules.md)

## 出处（印刷页）

- A p.2–8（A p.2）
- A p.47–48（A p.47）

> 说明：A=原书 §0.1–0.3 的纲领与 §5.5 的等价；最没把握处：把 §5.5.5 的单子论证压成一句话。
