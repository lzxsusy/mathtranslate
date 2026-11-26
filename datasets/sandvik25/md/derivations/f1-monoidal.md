# 函子 I 为什么是幺半的

> `sandvik25/deriv/f1-monoidal` · 轨道 B · Springer 侧与三造函子 · 状态 dev · 4 步

> **要回答的问题**：把 $V$ 的张量与 $\lambda$ 的加法同时处理时，为什么两条乘法互不干扰？

## 一句话

$F_1(V\otimes k_{T^\vee}(\lambda))=Z(\mathrm{Sat}(V))\star_I\mathbb W_\lambda$ 的两条乘法来源：中心的交换性（定理 2.4.1(3)）与 Wakimoto 层的加法性（命题 2.5.2(3)）。

## 目标

由定理 2.4.1(3) 与命题 2.5.2(3) 推出 $F_1(V\otimes V'\otimes k_{T^\vee}(\lambda+\mu))\cong F_1(V\otimes k_{T^\vee}(\lambda))\star_I F_1(V'\otimes k_{T^\vee}(\mu))$。

## 前提

- $\mathrm{Sat}$ 是幺半等价：$\mathrm{Sat}(V\otimes V')\cong\mathrm{Sat}(V)\star\mathrm{Sat}(V')$。
- 定理 2.4.1(3)：$Z(\mathcal F)$ 与任意 $\mathcal G\in\mathcal D^b_c(I\backslash\mathrm{Fl}_G)$ 在 $\star_I$ 下交换。
- 命题 2.5.2(3)：$\mathbb W_\lambda\star_I\mathbb W_\mu\cong\mathbb W_{\lambda+\mu}$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 左边：$F_1(V\otimes V'\otimes k_{T^\vee}(\lambda+\mu))=Z(\mathrm{Sat}(V\otimes V'))\star_I\mathbb W_{\lambda+\mu}=Z(\mathrm{Sat}(V)\star\mathrm{Sat}(V'))\star_I\mathbb W_{\lambda+\mu}$。 | $\mathrm{Sat}$ 幺半，$k_{T^\vee}$ 的乘法是加法。 | `A p.7` | A·原文明确写了 |
| 2 | 右边：$F_1(V\otimes k(\lambda))\star_I F_1(V'\otimes k(\mu))=Z(\mathrm{Sat}(V))\star_I\mathbb W_\lambda\star_I Z(\mathrm{Sat}(V'))\star_I\mathbb W_\mu$。 | 按定义展开。 | `A p.7` | A·原文明确写了 |
| 3 | 用定理 2.4.1(3) 把 $\mathbb W_\lambda$ 与 $Z(\mathrm{Sat}(V'))$ 交换，得 $Z(\mathrm{Sat}(V))\star_I Z(\mathrm{Sat}(V'))\star_I\mathbb W_\lambda\star_I\mathbb W_\mu$。 | 中心性允许中心层穿过任意对象；$\mathbb W_\lambda$ 是 $I$-等变层，正在适用范围内。 | `A p.7` | A·原文明确写了 |
| 4 | 再用 $Z$ 的幺半性（定理 2.4.1(1)）合并前两项，用命题 2.5.2(3) 合并后两项，得 $Z(\mathrm{Sat}(V)\star\mathrm{Sat}(V'))\star_I\mathbb W_{\lambda+\mu}$，与第 1 步相同。 | 两次合并各用一条乘法，互不干扰；这就是「两条乘法可以正交使用」的含义。 | `A p.7` | A·原文明确写了 |

## 结论

$F_1$ 的幺半性 = 中心性（把 $\mathbb W$ 挪过去）+ $Z$ 幺半（合并）+ $\mathbb W$ 加法（合并）。

## 缺口

- 单位对象的兼容（$1\mapsto\mathcal O$ 型的自然同构）原文未提，本推导也未覆盖。

## 最容易讲错的地方

- 交换的次序不能反：中心性说的是中心层可以穿过别的对象，而不是任意两个对象可交换。
- 若把 $\mathbb W_\lambda$ 换成 $\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$ 再做同一推导，需要额外的 $t$-正合性输入，不能直接照搬。

## 相关卡

[函子 I：$F_1\colon\mathrm{Rep}(G^\vee\times T^\vee)\to\mathcal P_I^{\mathrm{Wak}}$](../concepts/functor-f1.md) · [Wakimoto 层 $\mathbb W_\lambda$](../concepts/wakimoto-sheaves.md) · [Gaitsgory 中心函子 $Z$](../concepts/gaitsgory-central-functor.md)

## 出处（印刷页）

- A p.5–7（A p.7）

> 说明：引理 3.2.1 在 p.7；所引的两条乘法分别在 p.4（定理 2.4.1(3)）与 p.5（命题 2.5.2(3)）。
