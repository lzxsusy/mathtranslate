# Tate 上同调（有限群）

> `raskin_lcft/concept/tate-cohomology` ｜ track B ｜ reviewed

**一句话**：把通常上同调在 i=0 处用范数替换，得到对一切整数 i 有定义的 Ê⁰、Ê¹；好处是 Tate 长正合列可以穿过 −1。

**自测**：为什么非要把 Ĥ⁰ 定义成 M^G/NM，而不是通常的 H⁰=M^G？这个「商掉范数」到底买到了什么？

## 定义

对有限群 $G$ 与 $G$-模 $M$，定义 $\widehat H^0(G,M)=M^G/NM$（$N=\sum_{g\in G}g$），$\widehat H^i(G,M)=H^i(G,M)$（$i\ge1$），$\widehat H^{-1}(G,M)=\ker N/I M$。有限群时这些群构成一条以 $\widehat H^0,\widehat H^1$ 为中枢的长正合列（断言 6.16）。

记号：$\widehat H^0=M^G/NM$；$\widehat H^{-1}=\ker N/IM$；$I$ 为增广理想。

## 要点

- 「商掉 NM」使范数映射在 $\widehat H^0$ 上变成零，于是 $\widehat H^0\to\widehat H^1$ 的蛇形连接可以无阻地接上。
- 有限群时 $\widehat H^i$ 与通常上同调只差 $i=-1,0$ 两处；这是把「周期 2」现象放进统一框架的代价。
- 长正合列（6.16）是全部计算工具：Herbrand 商的乘性、lcft 的消没都只用它。
- 第 7 讲的 $\widehat H^i(G,M)$（循环群显式复形）第 6 讲的抽象定义在 Tate 复形框架下等价。

## 公式

\widehat H^0(G,M)=M^G/NM
\widehat H^{-1}(G,M)=\ker N/IM

## 定理与证明

### 断言 6.16（Tate 长正合列）

短正合列 $0\to M'\to M\to M''\to 0$ 诱导出 $\cdots\to\widehat H^i(G,M')\to\widehat H^i(G,M)\to\widehat H^i(G,M'')\to\widehat H^{i+1}(G,M')\to\cdots$ 的正合列。

（sketch；来源：原书 p.28）


缺口：由通常上同调长正合列与 $\widehat H^{-1},\widehat H^0$ 的定义拼接；$i=-1,0$ 两处需单独验证连接映射。

## 易错点

- 把 Ĥ⁰ 与 H⁰ 混用：两者只在 Tate 语境里差一个 NM
- 以为 Ê^i 对 i>0 也是新东西：i≥1 时 Ê^i=H^i
- 在非循环群上套用周期 2 的说法：周期 2 只对循环群成立

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 6 讲 正合列与 Tate 上同调，p.24–28（原书 p.24）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 7 讲 链复形与 Herbrand 商，p.29–31（原书 p.29）

关联：`raskin_lcft/concept/herbrand-quotient`、`raskin_lcft/concept/hilbert-theorem-90`、`raskin_lcft/concept/tate-cohomology-unbounded`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
