# 主定理的全忠实：$\mathrm{Hom}$ 两边的显式计算

> `sandvik25/deriv/fully-faithful-hom` · 轨道 D · 主等价 · 状态 dev · 6 步

> **要回答的问题**：为什么只需验证 $\mathcal F=\mathcal O_{\widetilde{\mathcal N}}$ 与 $\mathcal G=V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)[n]$ 这一种情形？

## 一句话

把 (8) 用五引理化到生成元后，两边都算成同一个数：$n=0$ 时为 $\dim V_{-\lambda}$，否则为 $0$。

## 目标

由生成元情形推出 $F^{\mathrm{IW}}$ 全忠实。

## 前提

- 引理 3.1.1：$\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$ 由 $\mathcal O_{\widetilde{\mathcal N}}(\lambda)$ 与 $V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)$（$\lambda\in X^\vee_+$）生成。
- 引理 2.5.4：$\mathcal P_I^{\mathrm{Wak}}$ 对 $\star_I$ 封闭。
- 定理 4.5.1：$(Z^{\mathrm{IW}}(V):\Delta^{\mathrm{IW}}_\lambda)=\dim V_\lambda$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 对 (8) 用五引理：只需对 $\mathcal F,\mathcal G$ 都是生成元的单项情形验证；由平移与 $\oplus$ 的兼容，进一步归为 $\mathcal F=\mathcal O_{\widetilde{\mathcal N}}$、$\mathcal G=V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)[n]$。 | 五引理把「任意两个对象的 $\mathrm{Hom}$」化成「生成元的 $\mathrm{Hom}$」，前提是知道 $F^{\mathrm{IW}}$ 在短正合列上同调意义兼容。 | `A p.12` | A·原文明确写了 |
| 2 | 左边：$\mathrm{Hom}(\mathcal O_{\widetilde{\mathcal N}},V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)[n])=\Gamma(\widetilde{\mathcal N},V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda))[n]$，其维数在 $n=0$ 时是 $V$ 的 $-\lambda$ 权空间、否则为 $0$。 | $\widetilde{\mathcal N}$ 上整体截面即 $V$ 按权 $\lambda$ 分解的部分（$\lambda$ 支配故只取非负侧）。 | `A p.12` | A·原文明确写了 |
| 3 | 右边：用 $F^{\mathrm{IW}}(\mathcal O_{\widetilde{\mathcal N}})=\Delta^{\mathrm{IW}}_0$、$F^{\mathrm{IW}}(V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda))\cong Z^{\mathrm{IW}}(V)\star_I\mathbb W_\lambda$ 代入，得 $\mathrm{Hom}(\Delta^{\mathrm{IW}}_0,Z^{\mathrm{IW}}(V)\star_I\mathbb W_\lambda[n])$。 | 这两个像是式 (7) 的直接读出。 | `A p.12` | A·原文明确写了 |
| 4 | 用伴随性把 $\mathbb W_\lambda$ 挪到左边：$\cong\mathrm{Hom}(\Delta^{\mathrm{IW}}_0\star_I\mathbb W_{-\lambda},Z^{\mathrm{IW}}(V)[n])$，再由命题 2.5.2 与式 (6) 化成 $\mathrm{Hom}(\Delta^{\mathrm{IW}}_{-\lambda},Z^{\mathrm{IW}}(V)[n])$。 | 这一步是全篇最关键的两行代数操作：把「与 $\mathbb W$ 作卷积」转成「标准层下标的平移」。 | `A p.12` | A·原文明确写了 |
| 5 | 由定理 4.5.1，该 $\mathrm{Hom}$ 的维数是 $Z^{\mathrm{IW}}(V)$ 中 $\Delta^{\mathrm{IW}}_{-\lambda}$ 的重数，即 $\dim V_{-\lambda}$（$n=0$）或 $0$。 | 重数公式在这里被当作「自由变量」使用：它把 IW 侧的重数直接读成表示侧的权维数。 | `A p.12` | A·原文明确写了 |
| 6 | 两边数值相等，(8) 是全忠实；结合本质满射得定理 5.0.1。 | 全忠实 + 本质满射 = 等价。 | `A p.12` | A·原文明确写了 |

## 结论

(8) 的左边 = $\dim V_{-\lambda}$（$n=0$）/ $0$；右边经伴随与式 (6) 化成同一重数，故 $F^{\mathrm{IW}}$ 全忠实。

## 缺口

- 第 1 步的「五引理」需要 $F^{\mathrm{IW}}$ 与三角结构的兼容性，原文只说「routine」；本推导未验证。
- 第 2 步的截面计算原文说「not hard to check」，仅给结果。

## 最容易讲错的地方

- 式 (6) 的 $\lambda$ 由 $W\cdot w=W\cdot w_\lambda$ 定，而第 4 步用的是 $\mathbb W_{-\lambda}$ 的平移；符号一旦取反，重数就对到 $\dim V_{\lambda}$ 而不是 $\dim V_{-\lambda}$。
- 「$n\neq0$ 时为 0」靠的是 $\widetilde{\mathcal N}$ 上那些线丛只有 $0$ 阶截面；换成更高阶的 $[n]$ 就会与非零的 Ext 混淆。

## 相关卡

[主函子 $F^{\mathrm{IW}}$ 与 Arkhipov–Bezrukavnikov 等价（定理 5.0.1）](../concepts/functor-fiw.md) · [中心层的 IW 像是倾斜层（定理 4.5.1）](../concepts/central-tilting.md) · [五个范畴的等价图（推论 5.0.2）](../concepts/five-categories.md)

## 出处（印刷页）

- A p.12（A p.12）

> 说明：式 (8) 与全部计算都在 p.12；本推导把原文四段压缩成六步并标出两处省略。
