# 消没定理

> `raskin_lcft/concept/vanishing-theorem` ｜ track C ｜ reviewed

**一句话**：消没定理：[(L⊗_K K^unr)^×]_tG 同伦等价于 0；它是 lcft 的引擎，把范数群问题化为纯局部计算。

**自测**：为什么「某个复形同伦等价于零」这句话足以推出整个局部类域论？

## 定义

消没定理（定理 15.5）：设 $L/K$ 是局部域的有限扩张，则复形 $[(L\otimes_K K^{\mathrm{unr}})^\times]_{tG}$ 同伦等价于零，即它的一切 Tate 上同调消没。完全分歧情形（定理 15.3）是 $L^{\mathrm{unr}}=K^{\mathrm{unr}}$ 的特例。由它立即得消没定理的存在性推论：$\widehat H^i(G,L^\times)\cong\widehat H^{i+2}(G,\mathbb Z)$（即 lcft）。

记号：$[\,]_{tG}$ 表示 Tate 上同调意义下的同伦余不变商。

## 要点

- 消没是「复形层面」的：不只同调为零，而是整个复形同伦等价于零，这才允许把 $L^\times$ 换成 $\mathbb Z[2]$。
- 从消没到 lcft 只有一步：$\widehat H^i(L^\times)=\widehat H^{i-2}(\mathbb Z)$，取 $i=0$ 得 $K^\times/NL^\times\cong G^{\mathrm{ab}}$。
- 证明分三步：归约到 $p$-群（16.3）、归约到循环商链（17.1）、用 Herbrand 商与 $K_m$ 逼近做极限（17.2/17.3）。
- 它与第 23 讲的第二不等式是同一技术的两个用法：都用「不断上升到更大的域」把有限群问题化掉。

## 公式

[(L\otimes_K K^{\mathrm{unr}})^\times]_{tG}\simeq 0
\widehat H^i(G,L^\times)\cong\widehat H^{i-2}(G,\mathbb Z)

## 定理与证明

### 定理 15.5（消没定理）

设 $L/K$ 是局部域有限扩张，$G=\mathrm{Gal}(L/K)$，则 $[(L\otimes_K K^{\mathrm{unr}})^\times]_{tG}$ 无环（同伦等价于 0）。

（sketch；来源：原书 p.67）


缺口：第 16 讲把群归约到 $p$-群，第 17 讲用序链与范数逼近证 $p$-群情形。

### 定理 16.3（归约到 p-Sylow）

复形 $X_{tG}$ 无环当且仅当对 $G$ 的每个 $p$-Sylow 子群 $G_p$，$(X_{tG_p})$ 无环。

（sketch；来源：原书 p.70）


缺口：用「$H^i$ 的消没可在 Sylow 上检验」这一标准归约。

## 易错点

- 把「无环（acyclic）」当成「同调全零」在普通复形中的意思：这里的等价是复形层面的同伦等价
- 把 15.3（完全分歧）与 15.5（一般情形）当成同一个定理：前者是后者的特例
- 忽略 K^unr 的作用：它不是 K 的代数闭包，而是最大非分歧扩张

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 15 讲 消没定理蕴含上同调类域论，p.66–69（原书 p.66）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 16 讲 Tate 上同调群的消没，p.70–72（原书 p.70）

关联：`raskin_lcft/concept/tate-cohomology-unbounded`、`raskin_lcft/concept/lcft-main-theorem`、`raskin_lcft/concept/tame-ramification`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
