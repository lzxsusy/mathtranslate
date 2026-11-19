# 辛 Khovanov 同调

> `functoriality/concept/symplectic-khovanov` ｜ track D ｜ draft

**一句话**：Seidel–Smith 用辛流形 S_n 上的辫群作用与 Floer 上同调定义 Kh_symp；引理 44 处理 Markov 稳定化，定理 5.4 转述它与 Khovanov 同调在特征 0 下一致。

**自测**：辛 Khovanov 同调 Kh_symp 凭什么是一个纽结不变量，它又与 Khovanov 同调差在哪里？

## 定义

Seidel 与 Smith 对每个自然数 $n$ 构造辛流形 $\mathcal S_n$，带有 $n$ 个字母上的辫群的辛作用（精确到哈密顿同痕），即同态 $\Phi:\Braid_n\to\pi_0\operatorname{Symp}(\mathcal S_n)$，并在 $\mathcal S_n$ 中构造拉格朗日子流形 $L_n^{\Cap}$。对能写成 $n$ 股辫 $\beta$ 的闭包的定向纽结，定义 $\operatorname{Kh}_{symp}(\beta):=\HF^*(L_n^{\Cap},\Phi_\beta L_n^{\Cap})$。关键问题是证明它不依赖辫闭包表示，即确是纽结不变量。

记号：$\mathcal S_n$：Seidel–Smith 辛流形；$L_n^{\Cap}$：其中的拉格朗日子流形；$\Phi$：辫群在 $\mathcal S_n$ 上的辛作用。

## 要点

- 构造：辛流形 $\mathcal S_n$ 上的辫群作用，加上拉格朗日 $L_n^{\Cap}$ 的 Floer 上同调，得到 $\operatorname{Kh}_{symp}(\beta)$。
- 不变量性：Seidel–Smith 引理 44（命题 5.3）给出自然同构 $\HF^*(L,L')\cong\HF^*(\cup_1L,\tau_2\cup_1L')$，处理 Markov 稳定化；共轭则由哈密顿同痕实现。
- 定理 5.4（转述 [AS19]）：在特征 $0$ 的域上、把双分次合并为单分次后，$\operatorname{Kh}_{symp}$ 与 Jones 多项式的 Khovanov 范畴化一致。
- 难点：拉格朗日对应 $\cup_i$ 非紧，直接使用伪全纯拼接映射理论一直很困难；比较证明用到推论 5.2 的一个版本。

## 公式

$\Phi:\Braid_n\longrightarrow\pi_0\operatorname{Symp}(\mathcal S_n)$
$\operatorname{Kh}_{symp}(\beta):=\HF^*(L_n^{\Cap},\Phi_\beta L_n^{\Cap})$
$\HF^*(L,L')\cong\HF^*(\cup_1L,\tau_2\cup_1L')$

## 定理与证明

### 命题 5.3（转述 Seidel–Smith 引理 44）

给定 $\mathcal S_n$ 中的一对拉格朗日子流形 $L$ 和 $L'$，有自然同构 $\HF^*(L,L')\cong\HF^*(\cup_1L,\tau_2\cup_1L')$。这是转述自 [SS06] 引理 44 的结论。

（sketch；来源：原书 p.55 §5.2（转述 [SS06] 引理 44））

1. 在 $\mathcal S_n^-\times\mathcal S_{n+1}$ 中取以 $S^2$ 为纤维、沿 $\mathcal S_n$ 的一个副本干净相交的一对拉格朗日对应 $\cup_1,\cup_2$。  
   为什么：这两个对应把 Markov 稳定化翻译成拉格朗日对应。
2. 取 $\tau_2$ 为关于 $\cup_2$ 的纤维化 Dehn 扭转，则 Floer 群在 $\cup_1$ 推前与 $\tau_2$ 扭转下自然同构。  
   为什么：这正是引理 44 的内容，处理稳定化这一步。

缺口：原文只引用 [SS06] 引理 44，不重复其证明；它是不变量性证明的关键一步。

### 定理 5.4（转述 Abouzaid–Smith [AS19]）

在特征为 $0$ 的域上，纽结不变量 $\operatorname{Kh}_{symp}$ 与 Jones 多项式的 Khovanov 范畴化一致（在把双分次合并为单分次之后）。这是转述 [AS19] 的比较定理，不是本文结果。

（none；来源：原书 p.55 §5.2（转述 [AS19]））


缺口：原文只引用 [AS19] 的结论；比较证明依赖伪全纯拼接对应，本节未展开。

## 易错点

- 把 Kh_symp 直接等同于 Khovanov 同调：必须限定特征 $0$、合并双分次，并处理环面/辫闭包表示的差别（定理 5.4 是转述）。
- 以为命题 5.3 一条就给出不变量性：它只处理稳定化，共轭不变性与辫群作用的良定义另行验证。
- 把 $\cup_i$ 当成紧拉格朗日对应：它们以 $S^2$ 为纤维且非紧，直接使用拼接理论有实质困难。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§5.2，p.55–55（原书 p.55 §5.2）

关联：`functoriality/concept/khovanov-homology`、`functoriality/deriv/khovanov-matching`、`functoriality/concept/dehn-twist`

来源说明：据中译本 §5.2（p.55）转述 Seidel–Smith 构造与 [AS19] 比较定理；术语依译名表。
