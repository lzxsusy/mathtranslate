# 形式群

> `functoriality/concept/formal-group` ｜ track D ｜ draft

**一句话**：Seidel 把 QC*(M) 的 Maurer–Cartan 元按进环系数组织成取值于形式群的函子 MC(M)；群律由伪全纯球面计数给出，是新的辛不变量。

**自测**：为什么把 Maurer–Cartan 元从集合升级为取值于形式群的函子，会比单个不变量携带更多可比较的信息？

## 定义

按 Seidel 的用法，形式群是从进环到群的一个函子，它等价于一个形式群律。取 $\mathscr C:=\QC^*(M)$ 为 $M$ 的整系数量子上链复形的一个适当模型并视为 $\Ainf$-环，则 $MC(\mathscr C;-)$ 可以升级为从进环到群的函子，即形式群；这样得到取值于形式群的紧致单调辛流形不变量，记为 $MC(M)$。群结构由计数 $M$ 中某些伪全纯球面定义，动机来自拼接 Floer 理论中的复合双函子。

记号：$\mathscr A$：$\Ainf$-环；$N$：进环（无单位交换环，$N\to\varprojlim_m N/N^m$ 为同构）；$\mathscr A\widehat\otimes N$：逆极限 $\varprojlim_m\mathscr A\otimes(N/N^m)$。

## 要点

- Seidel 定义：$MC(\mathscr A;N)$ 是 $\mathscr A\widehat\otimes N$ 中 Maurer–Cartan 元的规范等价类集合，关于 $N$ 函子性。
- 取 $\mathscr C:=\QC^*(M)$，$MC(\mathscr C;-)$ 升级为从进环到群的函子；按 Seidel 的术语这就是形式群，记 $MC(M)$。
- 群律由计数 $M$ 中的伪全纯球面定义；其动机是复合双函子 $\mathscr C:(\Fuk(M_1^-\times M_2),\Fuk(M_2^-\times M_3))\to\Fuk(M_1^-\times M_3)$，在对角线上的乘积下降到 $MC(M)$ 后结合。
- 与量子 Steenrod 平方的联系：系数取 $q\mathbb F_p[q]/q^{p+1}$ 时，$MC$ 元上的 $p$ 次幂映射与量子 Steenrod 平方的 $t^{\frac{p-1}{2}}$ 分量相互交织。
- 这是转述 Seidel [Sei19] 的新不变量，性质与应用尚未充分探索。

## 公式

$\sum_{d\geq1}\mu_d(\gamma,\ldots,\gamma)=0$
$MC(\mathscr A;N)$
$\mathscr C:\bigl(\Fuk(M_1^-\times M_2),\Fuk(M_2^-\times M_3)\bigr)\longrightarrow\Fuk(M_1^-\times M_3)$

## 定理与证明

### MC(M) 的形式群结构（转述 Seidel [Sei19]）

设 $M$ 是紧致单调辛流形，$\mathscr C:=\QC^*(M)$ 视为 $\Ainf$-环。则 $MC(\mathscr C;-)$ 可升级为从进环到群的函子，即形式群，其取值记为 $MC(M)$。这是转述 Seidel 的构造，不是本文证明的定理。

（none；来源：原书 p.59 §5.6（转述 [Sei19]））


缺口：原文只转述 Seidel 的构造与动机，不重复其证明。

## 易错点

- 把 $MC(M)$ 当成普通的集合不变量：它取值于形式群（从进环到群的函子），额外结构正是重点。
- 以为 $MC$ 上的乘积一开始就结合：原文明确说下降到 $MC(M)$ 之前并不结合。
- 把进环理解成有单位的交换环：原文定义进环是无单位交换环，且 $N\to\varprojlim_m N/N^m$ 为同构。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§5.6，p.59–59（原书 p.59 §5.6）

关联：`functoriality/concept/maurer-cartan`、`functoriality/concept/hms`、`functoriality/concept/steenrod-operations`

来源说明：据中译本 §5.6（p.59）与译者注转述 Seidel [Sei19] 的形式群构造。
