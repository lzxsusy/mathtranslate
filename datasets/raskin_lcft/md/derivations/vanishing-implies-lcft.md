# 消没定理如何推出上同调型局部类域论

> `raskin_lcft/deriv/vanishing-implies-lcft` ｜ track C ｜ reviewed

**目标**：证明：若消没定理成立，则 $(L^\times)_{tG}\simeq(\mathbb Z[-2])_{tG}$，从而 $K^\times/NL^\times\cong G^{\mathrm{ab}}$。

**自测**：为什么「某个复形同伦等价于零」能一步给出 lcft 的同构，而不用再算任何群？

## 前提

- $L/K$ 是局部域有限 Galois 扩张，$G=\mathrm{Gal}(L/K)$；$K^{\mathrm{unr}}$ 为最大非分歧扩张。
- 已知 $(K^{\mathrm{unr}})^\times$ 的 $G$-结构（Frobenius 作用）。

## 步骤

1. **写 $L^{\mathrm{unr}}=L\otimes_K K^{\mathrm{unr}}$，它是完全分歧部分与 $K^{\mathrm{unr}}$ 的复合。**  
   为什么：这一步把「$L$ 的上同调」换成「$G$ 在 $L^{\mathrm{unr}}$ 上的作用」，使 $G$ 的作用变成半线性的。  
   锚点：原书 p.66（证据 A）

2. **用 15.1/15.2 说明 $(K^{\mathrm{unr}})^{\sigma=1}=K$，即不变量恰好是 $K$。**  
   为什么：这是「Frobenius 作用」与「$K$ 的代数元」之间的对照，为下一步替换做准备。  
   锚点：原书 p.66（证据 A）

3. **对 $(L^{\mathrm{unr}})^\times$ 用消没定理 15.5：$[(L^{\mathrm{unr}})^\times]_{tG}\simeq0$。**  
   为什么：这正是消没定理的内容，也是全书的引擎。  
   锚点：原书 p.67（证据 A）

4. **由正合列 $1\to K^{\mathrm{unr},\times}\to (L^{\mathrm{unr}})^\times\to\cdots$ 取 Tate 上同调，得 $(L^\times)_{tG}\simeq(\mathbb Z[-2])_{tG}$（定理 14.2）。**  
   为什么：消没使中间项消失，只剩「$\mathbb Z$ 平移两次」。  
   锚点：原书 p.63（证据 A）

5. **取 $i=0$：$\widehat H^0(G,L^\times)\cong\widehat H^{-2}(G,\mathbb Z)=G^{\mathrm{ab}}$，即 $K^\times/NL^\times\cong G^{\mathrm{ab}}$（推论 18.14 / 定理 1.5）。**  
   为什么：$\widehat H^{-2}(G,\mathbb Z)$ 的 Tate 周期 2 计算给出 $G^{\mathrm{ab}}$。  
   锚点：原书 p.80（证据 B）

## 结果

$(L^\times)_{tG}\simeq(\mathbb Z[-2])_{tG}$，从而 $\widehat H^i(G,L^\times)\cong\widehat H^{i-2}(G,\mathbb Z)$，特别 $K^\times/NL^\times\cong G^{\mathrm{ab}}$。

## 缺口

- 第 4 步的正合列在原文里被拆成 15.6 的四项正合列与 14.6 的序列两处，接缝处需要核对（本卡按 14.6 的顺序写）。
- 「$\widehat H^{-2}(G,\mathbb Z)=G^{\mathrm{ab}}$」在原文用周期 2 与 13.11 两次引用，未给统一证明。

## 易错点

- 把 $(L^{\mathrm{unr}})^\times$ 与 $L^\times$ 混用：消没定理讲的是前者。
- 把「同伦等价于 0」当成「同调为 0 的逐项断言」：前者更强，正是取极限时需要的那一档。

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 14 讲 Tate 上同调与 K^unr，p.62–65（原书 p.62）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 15 讲 消没定理蕴含上同调类域论，p.66–69（原书 p.66）
- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 18 讲 范数群与 Kummer 理论，p.76–80（原书 p.76）

关联：`raskin_lcft/concept/vanishing-theorem`、`raskin_lcft/concept/tate-cohomology-unbounded`、`raskin_lcft/concept/lcft-main-theorem`

来源说明：步骤按底本论证顺序重写；provenance 见 SCHEMA（A 原文显式 / B 原文略写由邻页补 / C 译者补证）。
