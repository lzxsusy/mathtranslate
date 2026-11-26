# 五个范畴的等价图（推论 5.0.2）

> `sandvik25/concept/five-categories` · 轨道 D · 主等价 · 状态 dev

> **先自测**：这五个范畴之间哪些是等价、哪些只是单向函子，为什么偏偏这五个？

## 一句话

主定理连同 §4 的构造把五个范畴串成一个交换图：$\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\sim\mathcal D^b\mathcal P_I^{\mathrm{asph}}\sim\mathcal D^b\mathcal P_{\mathrm{IW}}\sim\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)\sim\mathcal D^b\mathcal P_I$。

## 定义

推论 5.0.2：存在范畴等价 $\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\sim\mathcal D^b\mathcal P_I^{\mathrm{asph}}\sim\mathcal D^b\mathcal P_{\mathrm{IW}}\sim\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$，且 $\mathcal D^b\mathcal P_{\mathrm{IW}}\cong\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$（推论 4.3.2），另有 $\mathcal D^b\mathcal P_I$ 通过全忠实函子嵌入其中。

**记号**：$\mathcal P_I=\mathrm{Perv}(I\backslash\mathrm{Fl}_G)$、$\mathcal P_I^{\mathrm{asph}}$ 为其 Serre 商、$\mathcal P_{\mathrm{IW}}$ 为 IW 反常层。

## 要点（为什么需要它）

1. 五个范畴分成三类几何来源：Springer 解消（凝聚层）、仿射旗簇（$I$-等变反常层）、IW 侧（Whittaker 扭曲的反常层）；等价把它们焊在一起。
2. 只有反球商与 IW 之间是「真」的等价链；$\mathcal D^b\mathcal P_I$ 只是通过全忠实函子参与，它本身更大。
3. 这个图是整篇文章的收束：A 轨给 Wakimoto 与中心层、B 轨给三造函子、C 轨给 IW 侧、D 轨给主等价，全部落在这张图里。
4. 图里没有 $\mathcal D^b(I\backslash\mathrm{Fl}_G)$：实现函子在 Iwahori 情形非等价（§3.4 末的警告），所以它不能进等价图。

## 核心公式

$$
$\mathcal D^b\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})\ \sim\ \mathcal D^b\mathcal P_I^{\mathrm{asph}}\ \sim\ \mathcal D^b\mathcal P_{\mathrm{IW}}\ \cong\ \mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$
$$

## 定理与证明（或缺口）

### 推论 5.0.2

上述五个范畴之间的等价关系成立。

> 证明状态：**sketch**。原文只画图并列等价，未给每条的独立论证；本卡按引用关系拆解。

出处：`A p.12`

## 常见误解

- 把 $\mathcal D^b\mathcal P_I$ 也写成等价的一端：它只通过全忠实嵌入参与，本身比反球商大。
- 误以为图是「同一范畴的五种描述」：五个范畴的底层几何各不相同，等价是跨几何的定理。

## 相关卡

[主函子 $F^{\mathrm{IW}}$ 与 Arkhipov–Bezrukavnikov 等价（定理 5.0.1）](../concepts/functor-fiw.md) · [反球商 $\mathcal P_I^{\mathrm{asph}}$](../concepts/antispherical-quotient.md) · [Iwahori–Whittaker 范畴 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$](../concepts/iw-category.md)

## 出处（印刷页）

- A p.12（A p.12）

> 说明：推论 5.0.2 的图在 p.12 末；各条等价的出处分别是定理 5.0.1、定理 4.4.1、推论 4.3.2。
