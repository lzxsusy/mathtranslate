# ind-概形上的右 $t$-结构

> `cdm14/concept/indscheme-t-structure` · 轨道 D · 晶体上的 t-结构 · 状态 dev

> **先自测**：为什么 ind-概形上的 $t$-结构要逐项定义，而不能直接用一个 $\IndCoh(X)$ 的 $t$-结构？

## 一句话

把 ind-概形 $X=\mathrm{colim}\,X_\alpha$ 上的右 $t$-结构逐 $\alpha$ 定义，并用闭浸入的 $t$-正合性把它与形式完备化对齐。

## 定义

设 $X=\mathrm{colim}_\alpha X_\alpha\in\DGIndSch_{\mathrm{laft}}$。用 $\Crys^r(X)\simeq\lim_\alpha\Crys^r(X_\alpha)\simeq\mathrm{colim}_\alpha\Crys^r(X_\alpha)$ 与伴随对 $((i_\alpha)_{\mathrm{dR},*},i_\alpha^{\dagger,r})$，定义 $\Crys^r(X)^{\ge0}$ 为 $\oblv^r_X(\mathcal M)\in\IndCoh(X)^{\ge0}$。

**记号**：$\IndCoh(X)$ 的 $t$-结构见 [GR1, §2.5]。

## 要点（为什么需要它）

1. 引理 4.3.3(a)：$\mathcal M\in\Crys^r(X)^{\ge0}$ 可以逐 $\alpha$ 用 $i_\alpha^{\dagger,r}$ 检测。
2. 引理 4.3.3(b)：$\Crys^r(X)^{\le0}$ 由 $(i_\alpha)_{\mathrm{dR},*}\Crys^r(X_\alpha)^{\le0}$ 生成——即紧对象来自有限层。
3. 引理 4.3.5：闭浸入 $i:X\hookrightarrow X'$（DG 概形到 ind-概形）的 $i_{\mathrm{dR},*}$ 是 $t$-正合的。
4. 引理 4.3.7：$X$ 在 $Z$ 中的形式完备化 $Y$ 与 $X$ 有相同的 $\Crys^r$，且 $t$-结构相容。

## 核心公式

$$\Crys^r(X)\simeq\lim_{\alpha}\Crys^r(X_\alpha)\simeq\mathrm{colim}_{\alpha}\Crys^r(X_\alpha)$$

## 定理与证明（或缺口）

### 形式完备化不改变 $t$-结构（引理 4.3.7）

$i:X\hookrightarrow Z$ 为闭浸入、$Y$ 为 $X$ 在 $Z$ 中的形式完备化、$i':X\to Y$，则 $i'^{\dagger,r}:\Crys^r(Y)\to\Crys^r(X)$ 是等价且与 $t$-结构相容。

> 证明状态：**sketch**。第 2 步「同一个核」需要在 $\Crys^r(Z)$ 层面比较，原文给了两种证明（Proof 1/Proof 2），此处只记结构。

出处：`A p.34`

## 常见误解

- $\Crys^r(X)\simeq\mathrm{colim}\,\Crys^r(X_\alpha)$ 是对紧对象成立的等价，不是对全体对象的余极限。
- ind-概形不是概形：$\IndCoh(X)$ 的 $t$-结构要单独定义（[GR1, §2.5]）。

## 相关卡

[右 $t$-结构：晶体上的「那个」$t$-结构](../concepts/right-t-structure.md) · [右晶体的归纳函子 $\ind^r_X$](../concepts/induction-right.md) · [Kashiwara 引理：闭浸入上的晶体即开补上为零的晶体](../concepts/kashiwara.md)

## 出处（印刷页）

- A p.33–35（A p.33）

> 说明：A=§4.3 的 4.3.1–4.3.7；最没把握处：lim 与 colim 的等价在紧对象层面的限制。
