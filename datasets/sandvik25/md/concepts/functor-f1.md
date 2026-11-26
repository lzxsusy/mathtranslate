# 函子 I：$F_1\colon\mathrm{Rep}(G^\vee\times T^\vee)\to\mathcal P_I^{\mathrm{Wak}}$

> `sandvik25/concept/functor-f1` · 轨道 B · Springer 侧与三造函子 · 状态 dev

> **先自测**：函子 I 为什么能定义在表示范畴上，幺半性由什么保证？

## 一句话

在表示范畴上直接定义 $V\otimes k_{T^\vee}(\lambda)\mapsto Z(\mathrm{Sat}(V))\star_I\mathbb W_\lambda$；定理 2.5.3 保证值域落在有 Wakimoto 滤链的中心层里，且它是幺半的。

## 定义

定义 $F_1\colon\mathrm{Rep}(G^\vee\times T^\vee)\to\mathcal P_I^{\mathrm{Wak}}$，$V\otimes k_{T^\vee}(\lambda)\mapsto Z(\mathrm{Sat}(V))\star_I\mathbb W_\lambda$，其中 $V\in\mathrm{Rep}(G^\vee)$、$\lambda\in X^\vee$。

**记号**：$\mathrm{Sat}\colon\mathrm{Rep}(G^\vee)\xrightarrow{\sim}\mathrm{Perv}(L^+G\backslash\mathrm{Gr}_G)$ 为几何 Satake 等价；$\mathcal P_I^{\mathrm{Wak}}\subset\mathcal P_I$ 为允许 Wakimoto 滤链的反常层。

## 要点（为什么需要它）

1. $F_1$ 的良定义靠两条：定理 2.5.3 保证 $Z(\mathrm{Sat}(V))$ 有 Wakimoto 滤链，引理 2.5.4 保证 $\mathcal P_I^{\mathrm{Wak}}$ 对 $\star_I$ 封闭。
2. 幺半性（引理 3.2.1）来自两处：定理 2.4.1(3) 的「$Z$ 落在中心」给出 $Z(\mathcal F)\star_I Z(\mathcal G)\cong Z(\mathcal F\star\mathcal G)$，命题 2.5.2(3) 给出 $\mathbb W_\lambda\star_I\mathbb W_\mu\cong\mathbb W_{\lambda+\mu}$。
3. 定义域是 $\mathrm{Rep}(G^\vee\times T^\vee)$ 而非 $\mathrm{Coh}(\widehat{\mathcal N}_X)$：这一步只用到「自由对象」这一小片，后面的函子 II 才把它扩张到整个自由凝聚层范畴。
4. 原文脚注 9 提醒：$k_{T^\vee}(\lambda)\mapsto\mathbb W_\lambda$ 单独是函子（$\mathrm{Rep}(T^\vee)\to\mathcal P_I$），但 Functoriality 仍需说明——所以 $F_1$ 的良定义不是自动的。

## 核心公式

$$
$F_1\colon\mathrm{Rep}(G^\vee\times T^\vee)\to\mathcal P_I^{\mathrm{Wak}},\quad V\otimes k_{T^\vee}(\lambda)\mapsto Z(\mathrm{Sat}(V))\star_I\mathbb W_\lambda$
$$

## 定理与证明（或缺口）

### 引理 3.2.1（幺半性）

$F_1$ 是幺半函子。

> 证明状态：**sketch**。原文只写「easy consequence」，未逐项核对约束（尤其是 $\mathbb W$ 的下标加法与 $V$ 的张量同时发生时）。

出处：`A p.7`

## 常见误解

- 把 $F_1$ 当成 $K$ 群层面的同构：$F_1$ 只是范畴层面的幺半函子，它到定理 5.0.1 之前都不是等价。
- $k_{T^\vee}(\lambda)$ 中的 $\lambda$ 与 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 中的 $\lambda$ 必须同号；若在 $T^\vee$ 与 $T$ 之间对偶时翻符号，$F_1$ 与 $F$ 就对不上。

## 相关卡

[中心层的 Wakimoto 滤链（定理 2.5.3）](../concepts/wakimoto-filtration.md) · [函子 II：经 Tannakian 重构把 $F_1$ 扩到 $\mathrm{Coh}_{\mathrm{free}}(\widehat{\mathcal N}_X)$](../concepts/functor-f2.md) · [函子 I 为什么是幺半的](../derivations/f1-monoidal.md)

## 出处（印刷页）

- A p.7（A p.7）

> 说明：定义与引理 3.2.1 均在 p.7；脚注 9 关于 functoriality 的提醒同页。
