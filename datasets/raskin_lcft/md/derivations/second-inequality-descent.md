# 第二不等式的证明：从 p 阶循环扩张下降到任意扩张

> `raskin_lcft/deriv/second-inequality-descent` ｜ track E ｜ reviewed

**目标**：证明定理 22.3（第二不等式）：$E/F$ 是数域的次数 $n$ 循环扩张时 $H^1(G,C_E)=0$。

**自测**：为什么「H¹(G,C_E)=0」这条消没可以只在 p 阶循环扩张上验证，然后自动推广？

## 前提

- $E/F$ 是数域的次数 $p$ 循环扩张，$p$ 为素数；$G=\mathrm{Gal}(E/F)$。
- $S$ 含分歧与无限素位，$O_{F,S}^\times$ 为 $S$-单位。

## 步骤

1. **先用 23.1/23.2 把「$u\in\mathcal O_{F,S}^\times$ 是 $p$ 次幂」化为「各 $v\in S$ 处像是 $p$ 次幂」，并把 $\mathcal O_{F,S}^\times\cap\Gamma=(\mathcal O_{F,S}^\times)^p$ 建立起来。**  
   为什么：把整体条件局部化，才能在下一步用类群/局部域论证。  
   锚点：原书 p.101（证据 A）

2. **构造 $\Gamma=\prod_{v\in S}F_v^\times\times\prod_{v\in T}(\mathcal O_{F_v}^\times)^p\times\prod_{v\notin S\cup T}\mathcal O_{F_v}^\times$，用 23.3/23.5 证 $\Gamma\subseteq N(\mathbb A_E^\times)$。**  
   为什么：这是「范数群足够大」的显式下界：先用 $T$ 覆盖 $\Gamma$ 的 $p$ 次根。  
   锚点：原书 p.103（证据 A）

3. **取 $T$ 使 23.6/23.7 的 Frobenius 生成 $\mathrm{Gal}(F'/F)=(\mathbb Z/p)^{\#S}$，并由 23.8 使每个 $v\in T$ 在 $E$ 中分裂。**  
   为什么：分裂保证局部范数条件在 $T$ 处自动满足。  
   锚点：原书 p.103（证据 A）

4. **用 23.9 的局部判据：$x\in\mathcal O_{F,S\cup T}^\times$ 是 $p$ 次幂 ⟺ 各 $v$ 处是 $p$ 次幂；于是 $\Gamma\subseteq N(\mathbb A_E^\times)$。**  
   为什么：这一步把「$\Gamma$ 的元素都是范数」化成有限多个局部条件。  
   锚点：原书 p.104（证据 A）

5. **断言 23.10：由四角交换图（左侧复合 $=$ 乘以 $[F(\zeta_p):F]$）得 $\gamma$ 单射，从而 $\beta$ 单射，$\alpha$ 单射。**  
   为什么：图的作用是把 $E(\zeta_p)/F(\zeta_p)$ 上的已知结果（假设已成立）搬回 $E/F$。  
   锚点：原书 p.105（证据 A）

6. **断言 23.11：把数域上的 $p$ 阶循环情形推到任意扩张（先对 $p$-群，再用 Sylow 与「唯一 $p$ 子群」归纳）。**  
   为什么：任意有限扩张可由 $p$ 阶循环层叠出来，消没沿层叠保持。  
   锚点：原书 p.106（证据 B）

## 结果

定理 22.3：$H^1(G,C_E)=0$。等价地，$\mathrm{Gal}(E/F)^{\mathrm{ab}}\to C_F/N(C_E)$ 是满射（布劳尔互反律），从而 $\#\widehat H^0(C_E)\le n$，与第一不等式合起来给出 $=n$。

## 缺口

- 第 5 步的交换图在底本中左端用花括号把上、下两个 $\mathrm{Br}(F/E)$ 括在一起并标 $\times[F(\zeta_p):F]$，排版极易误读（见勘误卡 second-inequality-diagram）。
- 第 3 步「$T$ 的选取同时满足 23.6/23.8」需要 Dirichlet 定理与 Chebotarev 的弱形式，原文只引用习题。
- 23.11 的归纳中「每个 $p$ 群有正规循环商」用 17.1，未重述。

## 易错点

- 把 23.10 的图当成「两个同层箭头之间的映射」：那个标签是左列两条竖直箭头的复合。
- 以为第二不等式可以直接对任意 $n$ 循环做：必须先退到 $p$ 阶（这一步正是 23.11）。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 22 讲 阿廷与布劳尔互反律（下），p.96–100（原书 p.96）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 23 讲 第二不等式的证明，p.101–107（原书 p.101）

关联：`raskin_lcft/concept/brauer-group`、`raskin_lcft/concept/herbrand-quotient`、`raskin_lcft/concept/vanishing-theorem`

来源说明：步骤按底本论证顺序重写；provenance 见 SCHEMA（A 原文显式 / B 原文略写由邻页补 / C 译者补证）。
