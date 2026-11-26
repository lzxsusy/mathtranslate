# 无界复形的 Tate 上同调

> `raskin_lcft/concept/tate-cohomology-unbounded` ｜ track C ｜ reviewed

**一句话**：对无界复形，用同伦余不变商 X_hG 与 Hom 复形 X^hG 定义整数次上（下）同调，H_1(G,Z)=G^ab 是第一个例子。

**自测**：为什么第 12 讲之后必须放弃「二周期」的初等图像，改用在无界复形上定义 H_i(G,X)？

## 定义

设 $X$ 是 $G$-模复形（无界）。取 $P_G^{\mathrm{can}}\to\mathbb Z$ 的投射消解，令 $X_{hG}=P_G^{\mathrm{can}}\otimes_G X$（同伦余不变商）、$X^{hG}=\operatorname{Hom}_G(P_G^{\mathrm{can}},X)$。定义 $H_i(G,X)=H^{-i}(X_{hG})$、$H^i(G,X)=H^i(X^{hG})$；Tate 上同调进入复形层面。

记号：$X_{hG}=P_G^{can}\otimes_G X$；$H_i(G,X)=H^{-i}(X_{hG})$。

## 要点

- 同伦余不变商是「先消解再模掉」，与朴素的 $X/IX$ 只在一阶以内相同，但天生适合无界复形。
- $H_1(G,\mathbb Z)=G^{\mathrm{ab}}$（断言 13.11）：最小但最说明问题的计算，也把「同调」与「群论」接上。
- 断言 13.13（$P_G\to L^\times[2]$ 是 Tate 上同调同构）就是 lcft 的复形化陈述，14.2 是它的局部版本。
- 这套语言让「消没」可以被表述成「某复形同伦等价于 0」——第 15–17 讲的目标。

## 公式

H_i(G,X)=H^{-i}(X_{hG})
H_1(G,\mathbb Z)=G^{\mathrm{ab}}

## 定理与证明

### 断言 13.11（H₁(G,Z)=G^ab）

$H_1(G,\mathbb Z)=G^{\mathrm{ab}}$。

（sketch；来源：原书 p.60）


缺口：用 bar 消解 $\mathbb Z[G^{n+1}]$ 直接算 $X_{hG}$ 的一阶同调。

### 断言 13.13（复形版 lcft）

设 $L/K$ 是局部域的有限 Galois 扩张，$G=\mathrm{Gal}(L/K)$，则 $P_G\\to L^\times[2]$ 在 Tate 上同调上是同构；等价地 $(L^\\times)_{tG}\\simeq(\\mathbb Z[-2])_{tG}$。

（sketch；来源：原书 p.61）


缺口：这是第 14 讲定理 14.2 的前身，证明留到消没定理之后。

## 易错点

- 把 X_hG 当成普通余不变商 X_G=X/IX：后者只是零阶
- 以为 H_i(G,X) 只在 i≥0 有定义：无界复形允许任意整数
- 把「同伦余不变商」与「导出函子」混同：前者是复形层面的构造

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 13 讲 同伦余不变商、交换化与 Tate 上同调，p.57–61（原书 p.57）

关联：`raskin_lcft/concept/tate-cohomology`、`raskin_lcft/concept/vanishing-theorem`、`raskin_lcft/concept/lcft-main-theorem`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
