# Tate 长正合列怎么组装

> `raskin_lcft/deriv/tate-long-exact` ｜ track B ｜ reviewed

**目标**：把通常上同调长正合列与 $\widehat H^{-1},\widehat H^0$ 的定义拼接，得到断言 6.16，并说明连接映射在两个特殊位置的来源。

**自测**：为什么 Ĥ⁰ 要定义成 M^G/NM，才能让长正合列「穿过 −1」？

## 前提

- $G$ 有限，$0\to M'\to M\to M''\to 0$ 是 $G$-模短正合列。
- $N=\sum_{g\in G}g$，$I=\ker(\mathbb Z[G]\to\mathbb Z)$。

## 步骤

1. **对 $i\ge1$ 直接用通常上同调长正合列：$\cdots\to H^i(M')\to H^i(M)\to H^i(M'')\to H^{i+1}(M')\to\cdots$。**  
   为什么：$i\ge1$ 时 $\widehat H^i=H^i$，无需改动。  
   锚点：原书 p.27（证据 A）

2. **在 $i=0$ 处把 $M^G$ 换成 $M^G/NM$：由于 $N$ 在 $M^G$ 上作用，商掉 $NM$ 后范数映射变成零。**  
   为什么：连接映射 $\widehat H^0\to\widehat H^1$ 的本质就是范数，商掉它才能让正合性成立。  
   锚点：原书 p.27（证据 A）

3. **在 $i=-1$ 处补 $\ker N/IM$：它是 $\widehat H^0$ 的左邻，使 $\widehat H^{-1}\to\widehat H^0$ 与范数衔接。**  
   为什么：这解释了为什么 $\widehat H^{-1}$ 是核、$\widehat H^0$ 是余核。  
   锚点：原书 p.27（证据 B）

4. **把 1–3 的片段接起来，验证两处新连接映射的核像相等，得到贯穿一切 $i\in\mathbb Z$ 的正合列（断言 6.16）。**  
   为什么：有限群时只需检查 $i=-1,0,1$ 三个位置，其余由 1 覆盖。  
   锚点：原书 p.28（证据 A）

5. **应用：对 $\chi$ 取阶即得乘性（引理 7.6）；对局部域取 $M=L^\times$ 即得消没定理的表述形式。**  
   为什么：整本书的所有计算都从这条长正合列出发。  
   锚点：原书 p.30（证据 B）

## 结果

断言 6.16 成立：短正合列诱导出 $\cdots\to\widehat H^i(M')\to\widehat H^i(M)\to\widehat H^i(M'')\to\widehat H^{i+1}(M')\to\cdots$ 的正合列。

## 缺口

- 原文对 $\widehat H^{-1}\to\widehat H^0$ 的「核 = 像」只做了示意，未逐项验证；本卡第 4 步把该验证列为待补。
- 若群非有限，$\widehat H^i$ 的整套构造要换成第 13 讲的无界复形版本，长正合列的证明不能照搬。

## 易错点

- 把 $\widehat H^0=M^G/NM$ 写成 $M^G$：长正合列在 $i=0$ 处立即断开。
- 以为连接映射只有 $\widehat H^0\to\widehat H^1$ 一处：$\widehat H^{-1}\to\widehat H^0$ 同样需要构造。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 6 讲 正合列与 Tate 上同调，p.24–28（原书 p.24）

关联：`raskin_lcft/concept/tate-cohomology`、`raskin_lcft/concept/herbrand-quotient`、`raskin_lcft/concept/vanishing-theorem`

来源说明：步骤按底本论证顺序重写；provenance 见 SCHEMA（A 原文显式 / B 原文略写由邻页补 / C 译者补证）。
