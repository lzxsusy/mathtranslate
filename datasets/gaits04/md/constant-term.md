# 常项算子与尖点性的几何判据

> `gaits04/concept/constant-term` · 轨 C 向量丛与 Hecke · 状态 reviewed · 核验 source-only

**问题：** 为什么尖点性可以只用「所有分拆的常项算子为零」来判定？

**一句话：** 用短正合列 $0\to M_1\to M\to M_2\to0$ 定义常项算子 $r^n_{n_1,n_2}=q_!p^*$；$f$ 尖点当且仅当对所有分拆 $n_1+n_2=n$（$n_1,n_2>0$）都有 $r^n_{n_1,n_2}(f)=0$。

**别名：** `constant term`、`r^n_{n1,n2}`、`cuspidality criterion`

## 定义

回到几何情形，用几何语言写出尖点条件。设 $n=n_1+n_2$ 是分拆。考虑短正合列 $0\to M_1\to M\to M_2\to0$ 的同构类集合 $\mathrm{Fl}^n_{n_1,n_2}$，其中 $M_1$ 与 $M_2$ 分别是秩 $n_1$ 与 $n_2$ 的向量丛。有自然映射 $p$ 与 $q$：$p$ 把短正合列送到 $M$，$q$ 送到 $(M_1,M_2)$，于是 $\mathrm{Bun}_n\xleftarrow{p}\mathrm{Fl}^n_{n_1,n_2}\xrightarrow{q}\mathrm{Bun}_{n_1}\times\mathrm{Bun}_{n_2}$。定义常项算子 $r^n_{n_1,n_2}:\operatorname{Funct}(\mathrm{Bun}_n)\to\operatorname{Funct}(\mathrm{Bun}_{n_1}\times\mathrm{Bun}_{n_2})$ 为 $f\mapsto q_!(p^*(f))$。现在容易看出：函数 $f$ 是尖点的，当且仅当对所有 $n_1+n_2=n$、$n_1,n_2>0$ 都有 $r^n_{n_1,n_2}(f)=0$。

**记号：** $\mathrm{Fl}^n_{n_1,n_2}$：短正合列的同构类集合；$p,q$：到 $\mathrm{Bun}_n$ 与 $\mathrm{Bun}_{n_1}\times\mathrm{Bun}_{n_2}$ 的投影；$r=q_!p^*$。

## 要点

- 分拆对应标准抛物子群：$M_1\subset M$ 就是 $M$ 的一个 $n_1$ 维子丛，正是抛物结构的几何版本。
- $r$ 与 §1.8 的沿 $U$ 积分是同一件事：$q_!$ 沿纤维求和即「取常数项」。
- 判据是「对所有分拆」，只查 $n_1=1$ 不够：$n\ge3$ 时需要中间抛物子群。

## 公式

$$
r^n_{n_1,n_2}=q_!\,p^*:\ \operatorname{Funct}(\mathrm{Bun}_n)\to\operatorname{Funct}(\mathrm{Bun}_{n_1}\times\mathrm{Bun}_{n_2})
$$

## 易错点

- 把 $r^n_{n_1,n_2}(f)=0$ 只对 $n_1=1$ 验证：这只排除极大抛物子群，排除不了中间的。

## 批注

**〔背景直觉〕常项 = 沿纤维求和**　在函数侧，「沿 $U$ 积分」与「沿 $q$ 的纤维求和」是同一个操作：$q$ 的纤维正是把 $M$ 映到 $(M_1,M_2)$ 的所有扩张，求和就是把 $M$ 的贡献按 $(M_1,M_2)$ 归并。到了层侧，$q_!$ 换成紧支撑推前（§3.4 用它定义「尖点本征层」）。

## 相关

[[cuspidal]]、[[eigensheaf]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§2.8，原书 pp. 276（PDF pp. 278）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec2.tex:80-95（§2.8）`
