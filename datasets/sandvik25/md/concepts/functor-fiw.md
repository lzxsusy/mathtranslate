# 主函子 $F^{\mathrm{IW}}$ 与 Arkhipov–Bezrukavnikov 等价（定理 5.0.1）

> `sandvik25/concept/functor-fiw` · 轨道 D · 主等价 · 状态 dev

> **先自测**：主函子怎么把几何侧的对象送到 IW 侧，等价性由哪两步合成？

## 一句话

$F^{\mathrm{IW}}=\mathrm{Av}^{\mathrm{IW}}\circ F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$ 是等价：$V\otimes\mathcal O_{\widetilde{\mathcal N}}\mapsto Z^{\mathrm{IW}}(V)$、$\mathcal O_{\widetilde{\mathcal N}}(\lambda)\mapsto\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$。

## 定义

定义 $F^{\mathrm{IW}}\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\xrightarrow{F}\mathcal D^b\mathcal P_I\xrightarrow{\mathrm{Av}^{\mathrm{IW}}}\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$；由定理 4.4.1 与推论 4.3.2 也可写成 $\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\xrightarrow{F}\mathcal D^b\mathcal P_I\xrightarrow{\mathrm{Av}^{\mathrm{IW}}}\mathcal D^b\mathcal P_{\mathrm{IW}}\cong\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$。对象对应见式 (7)：$V\otimes\mathcal O_{\widetilde{\mathcal N}}\mapsto Z(\mathrm{Sat}(L_\lambda))\mapsto T^{\mathrm{IW}}(V)$、$\mathcal O_{\widetilde{\mathcal N}}(\lambda)\mapsto\mathbb W_\lambda\mapsto\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$。

**记号**：$T^{\mathrm{IW}}(V):=F^{\mathrm{IW}}(L_\lambda\otimes\mathcal O_{\widetilde{\mathcal N}})$ 是倾斜层（定理 4.5.1）；$\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$ 与 $\Delta^{\mathrm{IW}}_\lambda$ 不同构，但 $K_0$ 中同类。

## 要点（为什么需要它）

1. 式 (7) 的两行是整篇文章的「字典」：几何侧的自由对象对应倾斜层，线丛对应平均后的 Wakimoto 层。
2. 一个重要提醒（原文明确）：$\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$ **不是**标准层 $\Delta^{\mathrm{IW}}_\lambda$，两者只在 Grothendieck 群里相等——所以等价不是把生成元逐个送到标准层的「显然」对应。
3. 证明分两半：本质满射靠式 (7) 加常规同调代数；全忠实靠把 (8) 用五引理化到 $\mathcal F=\mathcal O_{\widetilde{\mathcal N}}$、$\mathcal G=V\otimes\mathcal O_{\widetilde{\mathcal N}}(\lambda)[n]$ 并显式计算 $\mathrm{Hom}$。
4. 脚注 14：$T^{\mathrm{IW}}(L_\lambda)\cong T^{\mathrm{IW}}_\lambda$（$\lambda\in X^\vee_+$）不是构造出来的，而是定理 5.0.1 的**推论**——这是等价强于「对象逐一对应」的直接证据。

## 核心公式

$$
$F^{\mathrm{IW}}=\mathrm{Av}^{\mathrm{IW}}\circ F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$$F^{\mathrm{IW}}(V\otimes\mathcal O_{\widetilde{\mathcal N}})\cong Z^{\mathrm{IW}}(V),\qquad F^{\mathrm{IW}}(\mathcal O_{\widetilde{\mathcal N}}(\lambda))\cong\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$
$$

$$
$F^{\mathrm{IW}}(V\otimes\mathcal O_{\widetilde{\mathcal N}})\cong Z^{\mathrm{IW}}(V),\qquad F^{\mathrm{IW}}(\mathcal O_{\widetilde{\mathcal N}}(\lambda))\cong\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$
$$

## 定理与证明（或缺口）

### 定理 5.0.1（Arkhipov–Bezrukavnikov）

$F^{\mathrm{IW}}\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$ 是范畴等价。

> 证明状态：**sketch**。第 1、2 步原文各一句「routine / 5-lemma」，第 3 步的「mostly straightforward」也未展开；本卡把它们拆成可核对的四步。

出处：`A p.12`

## 常见误解

- 把 $F^{\mathrm{IW}}$ 与「$F$ 复合实现函子」混同：后者落在 $\mathcal D^b(I\backslash\mathrm{Fl}_G)$，而 $F^{\mathrm{IW}}$ 落在 IW 范畴，中间差一个平均。
- 由 $\mathrm{Av}^{\mathrm{IW}}(\mathbb W_\lambda)$ 与 $\Delta^{\mathrm{IW}}_\lambda$ 在 $K_0$ 中相等，推出它们同构——这是原文特意警告的错误。

## 相关卡

[函子 III：$F\colon\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\to\mathcal D^b\mathcal P_I$](../concepts/functor-f3.md) · [IW 平均函子 $\mathrm{Av}^{\mathrm{IW}}$（定理 4.4.1）](../concepts/iw-averaging.md) · [中心层的 IW 像是倾斜层（定理 4.5.1）](../concepts/central-tilting.md) · [主定理的全忠实：$\mathrm{Hom}$ 两边的显式计算](../derivations/fully-faithful-hom.md)

## 出处（印刷页）

- A p.11–12（A p.12）

> 说明：式 (7) 在 p.11，定理 5.0.1 的证明与脚注 14 在 p.12。
