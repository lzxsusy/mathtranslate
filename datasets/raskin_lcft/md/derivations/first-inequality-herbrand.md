# 第一不等式的证明：χ(C_E)=n

> `raskin_lcft/deriv/first-inequality-herbrand` ｜ track E ｜ reviewed

**目标**：证明定理 20.9(1)：若 $E/F$ 是次数 $n$ 的循环扩张，则 $\chi(C_E)=n$。

**自测**：为什么把 C_E 换成 A_{E,S}^× 后能算出 n，而 E_S^× 那一项的贡献必须用格论（20.14）单独处理？

## 前提

- $E/F$ 是整体域的次数 $n$ 循环扩张，$G=\mathrm{Gal}(E/F)$。
- $S$ 是含全部分歧素位与无限素位的有限集，且 $\mathbb A_{F,S}^\times F^\times=\mathbb A_F^\times$（引理 20.12）。

## 步骤

1. **由断言 20.10 把 $\widehat H^i(G,\mathbb A_{E,S}^\times)$ 拆成 $\bigoplus_{v\in S}\widehat H^i(G,(E\otimes_F F_v)^\times)$，$v\notin S$ 的项由 8.5 消没。**  
   为什么：局部化：整体上同调 = 有限多个局部上同调之和，这是「S-阿代尔」定义的直接后果。  
   锚点：原书 p.88（证据 A）

2. **对每个 $v$ 用局部 lcft 算 $\chi((E\otimes_F F_v)^\times)=[E_w:F_v]$，乘起来得 $\chi(\mathbb A_{E,S}^\times)=\prod_{v\in S}[E_w:F_v]$。**  
   为什么：局部情形已经由 lcft 解决（每个 $v$ 上是局部域扩张）。  
   锚点：原书 p.88（证据 A）

3. **构造正合列 $0\to E_S^\times\to\mathbb A_{E,S}^\times\to C_E\to0$（断言 20.13），用蛇引理证明右端映射 $\psi$ 是同构。**  
   为什么：这是把 $C_E$ 换成更好算的 $\mathbb A_{E,S}^\times$ 的桥；$\psi$ 同构说明 $C_E$ 的商与 $\mathbb A_{E,S}^\times$ 的商一致。  
   锚点：原书 p.89（证据 A）

4. **对上述正合列取 Herbrand 商：$\chi(C_E)=\chi(\mathbb A_{E,S}^\times)/\chi(E_S^\times)$。**  
   为什么：乘性（引理 7.6）把问题拆成两项。  
   锚点：原书 p.90（证据 B）

5. **用引理 20.14（循环群作用下的两个不变格 Herbrand 商相等）算 $n\cdot\chi(E_S^\times)=\prod_{v\in S}[E_w:F_v]$，代入上一步得 $\chi(C_E)=n$。**  
   为什么：$E_S^\times$ 是格，$\chi$ 不为 1，只能靠「格之间」的比较来定。  
   锚点：原书 p.90（证据 A）

## 结果

$\chi(C_E)=n$，即 $\#\widehat H^0(G,C_E)/\#\widehat H^1(G,C_E)=n$；配合第二不等式得 $\#\widehat H^0=n$，即 gcft 主定理。

## 缺口

- 第 3 步的蛇引理只给出「$\psi$ 同构」，但 $\psi$ 与 Herbrand 商的关系需要 20.13 图表的交换性，原文用「$\varphi$ 既满又单」一句带过。
- 第 5 步要求 $E_S^\times$ 与某个格之间能用 20.14；原文对「哪个格」未明说，本卡按「$E_S^\times$ 的 $\mathbb Z$-格结构」理解。
- 整体域有无限素位时 $E_S^\times$ 的秩计算要用 Dirichlet 单位定理，原文只引用。

## 易错点

- 把 $\chi(C_E)=n$ 当成「$\#C_E/N(C_E)=n$」：$\chi$ 是 $\widehat H^0/\widehat H^1$ 之比，还需要 $\widehat H^1=0$ 才能下结论。
- 漏掉 $v\notin S$ 的消没：那样 $\chi$ 会变成无穷。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 20 讲 第一不等式的证明，p.86–91（原书 p.86）

关联：`raskin_lcft/concept/herbrand-quotient`、`raskin_lcft/concept/idele-class-group`、`raskin_lcft/concept/vanishing-theorem`

来源说明：步骤按底本论证顺序重写；provenance 见 SCHEMA（A 原文显式 / B 原文略写由邻页补 / C 译者补证）。
