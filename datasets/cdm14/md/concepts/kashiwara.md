# Kashiwara 引理：闭浸入上的晶体即开补上为零的晶体

> `cdm14/concept/kashiwara` · 轨道 B · 左/右晶体、IndCoh 与 Kashiwara · 状态 dev

> **先自测**：为什么「支撑在 $X$ 上的晶体」不需要真的定义支撑？

## 一句话

闭浸入 $i:X\hookrightarrow Z$ 上，$\Crys(X)$ 等价于 $\Crys(Z)$ 中在开补 $Z^\circ$ 上为零的对象。

## 定义

设 $i:X\hookrightarrow Z$ 是经典预栈层面的闭浸入，$j:Z^\circ\hookrightarrow Z$ 为补开浸入。令 $\Crys^r(Z)_X:=\ker\big(j^{\dagger,r}:\Crys^r(Z)\to\Crys^r(Z^\circ)\big)$。

**记号**：$i'^{\dagger,r}:\Crys^r(Z)_X\to\Crys^r(X)$ 为 $i^{\dagger,r}$ 的分解。

## 要点（为什么需要它）

1. $j^{\dagger,r}$ 有全忠实右伴随 $j_{\mathrm{dR},*}$，于是 $\Crys^r(Z)_X$ 是余局部化：右伴随为 $\mathcal M\mapsto\mathrm{Cone}(\mathcal M\to j_{\mathrm{dR},*}j^{\dagger,r}\mathcal M)[-1]$。
2. $i^{\dagger,r}\circ j_{\mathrm{dR},*}=0$，所以 $i^{\dagger,r}$ 通过 $\Crys^r(Z)_X$ 分解，得到 $i'^{\dagger,r}$。
3. 命题 2.5.6：$i'^{\dagger,r}$ 是等价。这就是「Kashiwara 引理内置于定义」的确切含义。
4. 左晶体有同样结论，只需把 $\IndCoh$ 换成 $\QCoh$、把 [GR1, 7.4.5] 换成 [GR1, 7.1.3]（注 2.5.7）。

## 核心公式

$$\Crys^r(Z)_X:=\ker\big(j^{\dagger,r}\big),\qquad i'^{\dagger,r}:\Crys^r(Z)_X\xrightarrow{\sim}\Crys^r(X)$$

## 定理与证明（或缺口）

### Kashiwara 等价（命题 2.5.6）

$i'^{\dagger,r}:\Crys^r(Z)_X\to\Crys^r(X)$ 是等价。

> 证明状态：**sketch**。第 3 步直接引用 [GR1, 命题 7.4.5]，本文未给证明。

出处：`A p.25`

## 常见误解

- 「在开补上为零」用的是 $j^{\dagger,r}$，不是 $j^*$；右晶体只有 $!$-拉回。
- $\Crys^r(Z)_X$ 是 $\Crys^r(Z)$ 的余局部化子范畴，不是局部化——别把箭头方向搞反。
- Kashiwara 等价依赖 $i$ 是闭浸入；开浸入只给出全忠实的 $j^{\dagger,r}$ 与其右伴随。

## 相关卡

[左晶体：$\Crys^l(Y)=\QCoh(Y_{\mathrm{dR}})$](../concepts/left-crystal.md) · [右晶体：$\Crys^r(X)=\IndCoh(X_{\mathrm{dR}})$](../concepts/right-crystal.md) · [命题 2.5.6 的证明：把 $\Crys^r(Z)_X$ 算成形完备化](../derivations/kashiwara-equiv.md)

## 出处（印刷页）

- A p.23–25（A p.23）
- A p.25（A p.25）

> 说明：A=§2.5.1–2.5.7；最没把握处：余局部化右伴随的符号与平移次数。
