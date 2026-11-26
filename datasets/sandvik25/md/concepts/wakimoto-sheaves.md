# Wakimoto 层 $\mathbb W_\lambda$

> `sandvik25/concept/wakimoto-sheaves` · 轨道 A · 中心层与 Wakimoto 层 · 状态 dev

> **先自测**：Wakimoto 层怎么由标准层与余标准层卷积出来，为什么它必须是「反序」的？

## 一句话

把 $\lambda=\lambda_1-\lambda_2$ 写成支配权之差，令 $\mathbb W_\lambda=\nabla_{\lambda_1}\star_I\Delta_{-\lambda_2}$：与选择无关、支撑在 $\mathrm{Fl}_{G,\lambda}$、且对加法幺半。

## 定义

对 $\lambda\in X^\vee$ 取 $\lambda_1,\lambda_2\in X^\vee_+$ 使 $\lambda=\lambda_1-\lambda_2$，定义反常层 $\mathbb W_\lambda:=\nabla_{\lambda_1}\star_I\Delta_{-\lambda_2}$。其中 $\Delta_w=j_{w!}k_{\mathrm{Fl}_{G,w}}[\ell(w)]$、$\nabla_w=j_{w*}k_{\mathrm{Fl}_{G,w}}[\ell(w)]$ 为 Bruhat 分层上的标准层与余标准层。

**记号**：$\mathrm{Fl}_G=\bigsqcup_{w\in W_{\mathrm{ext}}}\mathrm{Fl}_{G,w}$ 为 Bruhat 分解，$\ell$ 是准 Coxeter 长度；$\lambda\in X^\vee$ 与 $w_\lambda$ 在 §4.3 对应。

## 要点（为什么需要它）

1. 顺序很关键：$\nabla_{\lambda_1}\star\Delta_{-\lambda_2}$（余标准在前、标准在后）才使 $\mathbb W_\lambda$ 与分解无关；倒过来不成立。
2. 命题 2.5.2(3) 的 $\mathbb W_\lambda\star_I\mathbb W_\mu\cong\mathbb W_{\lambda+\mu}$ 把 $X^\vee$ 变成「卷积半群」，于是一切 Wakimoto 层都由基本块生成——这是函子 I 能定义在 $\mathrm{Rep}(T^\vee)$ 上的根据。
3. 支撑在 $\mathrm{Fl}_{G,\lambda}$（不是 $\mathrm{Fl}_{G,w_\lambda}$ 的一般并）：这正是 IW 侧的轨道结构，两侧按同一个 $\lambda$ 对齐，重数公式才可能成立。
4. 命题 2.5.1 的三条卷积公式是 Bruhat 分层的标准性质，但原文把它当作工具直接用，未证。

## 核心公式

$$
$\mathbb W_\lambda:=\nabla_{\lambda_1}\star_I\Delta_{-\lambda_2}$（$\lambda=\lambda_1-\lambda_2$，$\lambda_i\in X^\vee_+$）$\mathbb W_\lambda\star_I\mathbb W_\mu\cong\mathbb W_{\lambda+\mu}$$\Delta_x\star_I\nabla_{x^{-1}}\cong\Delta_e\cong\nabla_{x^{-1}}\star_I\Delta_x$
$$

$$
$\mathbb W_\lambda\star_I\mathbb W_\mu\cong\mathbb W_{\lambda+\mu}$
$$

$$
$\Delta_x\star_I\nabla_{x^{-1}}\cong\Delta_e\cong\nabla_{x^{-1}}\star_I\Delta_x$
$$

## 定理与证明（或缺口）

### 命题 2.5.1–2.5.2（卷积与 Mirković 性质）

(2.5.1) 长度可加时标准层/余标准层卷积仍为标准层/余标准层；$\Delta_x\star\nabla_{x^{-1}}\cong\Delta_e$；$\Delta_x\star\nabla_y$ 恒反常。(2.5.2) $\mathbb W_\lambda$ 与 $\lambda_i$ 的选取无关、支撑在 $\mathrm{Fl}_{G,\lambda}$、且对加法幺半。

> 证明状态：**gap**。原文只陈述；语言是 Bruhat 分层与 $!$/$*$ 扩张的常规推演，未展开。

出处：`A p.5`

## 常见误解

- 「与选择无关」需要 $\lambda_i$ 取成支配权；若允许任意 $\lambda_i$，标准层不一定是余标准层，卷积结果会变。
- $\mathbb W_\lambda$ 一般不是单层，也不是半单层：它是两个扩张的卷积，故只在 Grothendieck 群里才与 $\Delta^{\mathrm{IW}}_\lambda$ 对齐（定理 4.4.1 证明后的提醒）。

## 相关卡

[中心层的 Wakimoto 滤链（定理 2.5.3）](../concepts/wakimoto-filtration.md) · [反球模 $M^{\mathrm{asph}}$](../concepts/antispherical-module.md) · [函子 I：$F_1\colon\mathrm{Rep}(G^\vee\times T^\vee)\to\mathcal P_I^{\mathrm{Wak}}$](../concepts/functor-f1.md)

## 出处（印刷页）

- A p.5（A p.5）

> 说明：定义与命题 2.5.1–2.5.2 全在 p.5；$\lambda\mapsto w_\lambda$ 的对应在 §4.3（p.10）。
