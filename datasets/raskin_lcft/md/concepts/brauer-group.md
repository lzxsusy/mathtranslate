# 布劳尔群

> `raskin_lcft/concept/brauer-group` ｜ track E ｜ reviewed

**一句话**：Br^coh(K)=H²(Gal(K̄/K),K̄^×) 与中心可除代数的相似类群 Br^csa(K) 同构，非阿基米德局部域上二者都同构于 Q/Z。

**自测**：为什么「H² 里的 2-上闭链类」能和「中心单代数的相似类」是同一个东西？

## 定义

$\mathrm{Br}^{\mathrm{coh}}(K/L)=H^2(\mathrm{Gal}(L/K),L^\times)$，取极限得 $\mathrm{Br}^{\mathrm{coh}}(K)=H^2(\mathrm{Gal}(\overline K/K),\overline K^\times)$。另一侧 $\mathrm{Br}^{\mathrm{csa}}(K)$ 是中心可除 $K$-代数的相似类群（$A\sim A'$ 若 $M_n(A)\cong M_m(A')$）。定理 19.16 断言二者典范同构；局部域上 $\mathrm{Br}^{\mathrm{coh}}(K)\cong\mathbb Q/\mathbb Z$（推论 19.5）。

记号：$\mathrm{Br}^{\mathrm{coh}}(K/L)=H^2(G,L^\times)$；$\mathrm{Br}(K)=\mathrm{Br}^{\mathrm{coh}}(K)\cong\mathrm{Br}^{\mathrm{csa}}(K)$。

## 要点

- lcft 的同构把 $H^2(G,L^\times)$ 算成 $\frac{1}{[L:K]}\mathbb Z/\mathbb Z$（断言 19.4），取极限即 $\mathbb Q/\mathbb Z$。
- 「$n^2$ 维中心可除代数」与「$n$ 次扩张」的对应（19.15/19.19/19.20）是 Br 与范数群字典的代数影子。
- 断言 19.17：$n^2$ 维中心可除代数的同构类数为 $\varphi(n)$——这是 $\mathbb Q/\mathbb Z$ 的 $n$-挠部分的计数。
- Br 的作用：第 21–23 讲的阿廷/布劳尔互反律完全在 Br 里表述，第二不等式就是 $H^1(G,C_E)=0$。

## 公式

\mathrm{Br}^{\mathrm{coh}}(K/L)=H^2(G,L^\times)
\mathrm{Br}^{\mathrm{coh}}(K)\cong\mathbb Q/\mathbb Z\quad(K\ \text{非阿基米德局部域})

## 定理与证明

### 推论 19.5（局部域布劳尔群）

设 $K$ 是非阿基米德局部域，则 $\mathrm{Br}^{\mathrm{coh}}(K)\cong\mathbb Q/\mathbb Z$。

（sketch；来源：原书 p.82）


缺口：用断言 19.4 的交换方块取逆向极限。

### 定理 19.16（Br^coh ≅ Br^csa）

对域 $K$，$\mathrm{Br}^{\mathrm{coh}}(K)\cong\mathrm{Br}^{\mathrm{csa}}(K)$，且相对版本 $\mathrm{Br}^{\mathrm{coh}}(K/L)\cong\mathrm{Br}^{\mathrm{csa}}(K/L)$ 亦然。

（sketch；来源：原书 p.84）


缺口：由 Crossed-product 构造与「分裂域 = 极大交换子代数」的对应得到；完整证明不在讲义范围。

## 易错点

- 把 Br^coh 当成 Br^csa 的定义：两者同构是定理 19.16，不是定义
- 以为 Br(K) ≅ Q/Z 对一切域成立：只对非阿基米德局部域（及整体域的有理版本）成立
- 混淆 Br(K/L)=ker(Br(K)→Br(L)) 与 Br^coh(K/L)=H²(G,L^×)

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 19 讲 布劳尔群，p.81–85（原书 p.81）

关联：`raskin_lcft/concept/tame-ramification`、`raskin_lcft/concept/vanishing-theorem`、`raskin_lcft/concept/lcft-main-theorem`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
