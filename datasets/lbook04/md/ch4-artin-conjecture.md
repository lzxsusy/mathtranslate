# Artin 猜想

> `lbook04/concept/ch4-artin-conjecture` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** Artin 猜想为什么不能由 Brauer 定理直接推出，它与 Langlands 纲领的关系是什么？

**一句话：** Artin 猜想：不含平凡成分的不可约表示 $\chi$，其 $L(\chi,s)$ 在全平面解析；它蕴含 $\zeta_K/\zeta_k$ 全纯，并归入 Langlands 纲领。

**别名：** `Artin's conjecture`、`整函数性`、`Aramata–Brauer`

## 定义

§5 的猜想 5.1：若特征 $\chi$ 不含平凡特征成分，则 $L(\chi,s)$ 是整函数。推论 5.2：$K/k$ 为 Galois 扩张时 $\zeta_K/\zeta_k$ 全纯。例 5.1（Aramata–Brauer）用增广表示把 $\zeta_K/\zeta_k$ 写成 $\prod_{\chi\ne1}L(\chi,s)^{\chi(1)}$，从而在 Galois 情形给出全纯性；非 Galois 情形 $\zeta_K/\zeta_k$ 的全纯性仍未决。Brauer 定理只给亚纯（系数可负，极点可能相消），要得解析必须证明不相消。Artin 猜想今天已归入 Langlands 纲领：$\chi$ 应对应 $\mathrm{GL}_n$ 的自守表示，$L(\chi,s)$ 应是自守 L 函数；二维情形对应权 $1$ 模形式（Deligne–Serre 正向、Weil 逆定理反向、Langlands–Tunnell 解决除二十面体外的所有类型）。

**记号：** $\chi$：Galois 表示的特征；$\zeta_K/\zeta_k$：Dedekind zeta 之比；增广表示：$\chi_{\mathrm{aug}}=\chi_{\mathrm{reg}}-1$；强 Artin 猜想：还要求 $L$ 来自自守表示。

## 要点

- 猜想只排除平凡成分：$\chi$ 含 $1$ 时 $L$ 有 $\zeta$ 的极点；去掉 $1$ 后应无极点。
- Brauer 分解给出亚纯，要得解析必须证明极点不相消；Aramata–Brauer 对 Galois 扩张给出 $\zeta_K/\zeta_k$ 的全纯性，但非 Galois 的整性未决。
- 与 Langlands 的联系：$\chi$ 应对应 $\mathrm{GL}_n$ 的自守表示，$L(\chi,s)$ 应是自守 L 函数，从而整/亚纯由自守表示理论给出。

## 公式

$$
L(\chi,s)\ \text{整}\qquad(\chi\ \text{不含平凡成分})
$$

$$
\zeta_K(s)/\zeta_k(s)=\prod_{\chi\ne1}L(\chi,s)^{\chi(1)}\ \text{全纯}\qquad(K/k\ \text{Galois})
$$

$$
L(\chi,s)=L(\pi,s)\qquad(\text{Langlands 对应}:\ \chi\leftrightarrow\pi)
$$

## 定理与证明

**猜想 5.1（Artin）**　设 $\chi$ 为 $G$ 的特征，且 $\chi$ 不含平凡特征作为成分。则 $L(\chi,s)$ 是全平面上的整函数。

1. $\chi$ 写成不可约特征的整系数组合，逐项由 Brauer 定理得亚纯。
1. 需证明在 $s=1$ 等处极点不相消——这正是猜想的内容，等价于 $\chi$ 对应自守表示。

> 跳步说明：书中明确说 Brauer 定理「只能给亚纯，不能给解析」；猜想 5.1 至今未决，只有一维（类域论）与部分二维情形已知。

*出处：ch04.tex:356-370（§5，猜想 5.1）*

## 易错点

- 把「$\chi$ 不可约」当成充分条件：不可约但含平凡成分（如 $\chi=1$）仍有极点；条件是没有平凡成分。
- 把强 Artin 猜想与 Artin 猜想混同：前者还要求 $L$ 来自自守表示（权 $1$ 模形式），后者只要求解析性。

## 批注

**〔背景直觉〕为什么二维情形重要**　§7 说明二维 Artin 表示对应权 $1$ 模形式：Deligne–Serre 给出正向构造，Weil 逆定理给出反向，Langlands–Tunnell 解决除二十面体外的所有类型。这是「Artin 猜想 $\Rightarrow$ 模性」的具体通道，也是 Wiles 证明费马大定理所用方法的祖先。

**〔含糊点拨〕二十面体情形**　定理 7.3 用 Tunnell 的拼写（原书作 Tunnel）。二十面体情形是唯一未被 Langlands–Tunnell 覆盖的二维射影类型，后来由 Taylor 等人的工作推进；书中把它列为「强 Artin 猜想」的开放案例。

## 相关

[[ch4-induction]]、[[ch4-artin-hecke]]、[[ch4-conductor-fe]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§5，原书 pp. 83–84（PDF pp. 89–90）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch04.tex:354-370`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§7，原书 pp. 85–87（PDF pp. 91–93）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch04.tex:442-482`
