# 尖点函数

> `gaits04/concept/cuspidal` · 轨 B 尖点与 Langlands 对应 · 状态 reviewed · 核验 source-only

**问题：** 尖点性为什么写成「沿幂幺根积分等于零」？

**一句话：** 对每个标准抛物子群的幂幺根 $U$，$f$ 沿 $U(K)\backslash U(\mathbb A)$ 的积分恒为零，这样的光滑函数叫尖点函数。

**别名：** `cuspidal function`、`尖点性`、`constant term`

## 定义

回到自守情形，即商 $\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A)$。回忆：上述商空间上的函数 $f$ 称为尖点的，若对所有 $g\in\mathrm{GL}_n(\mathbb A)$ 及所有子群 $U$ 都有 $\int_{U(K)\backslash U(\mathbb A)}f(u\cdot g)\,\mu(u)=0$，其中 $U$ 取 $\mathrm{GL}_n$ 的标准抛物子群的幂幺根。记尖点函数构成的子空间为 $\operatorname{Funct}_{cusp}(\mathrm{GL}_n(K)\backslash\mathrm{GL}_n(\mathbb A))$。按定义，它关于 $\mathrm{GL}_n(\mathbb A)$ 的作用不变。可以证明该空间中每个元素都自动紧支撑。

**记号：** $U$：标准抛物子群的幂幺根；积分沿 $U(K)\backslash U(\mathbb A)$，用 $\mu$ 的相应测度。

## 要点

- 「对所有标准抛物子群」不能减到只对 Borel：$n\ge3$ 时中间抛物子群给出独立的条件。
- 积分沿 $U(K)\backslash U(\mathbb A)$ 而非 $U(\mathbb A)$：$U(K)$ 是离散子群，商上才有有限测度。
- 尖点函数自动紧支撑，这是原书直接引用的事实，证明不在本章。

## 公式

$$
\int_{U(K)\backslash U(\mathbb A)}f(u\cdot g)\,\mu(u)=0
$$

## 易错点

- 把「尖点」当成「在尖点处消失」的几何直观而不写积分条件：$n\ge2$ 时直观不足以给出可用的判据，§2.8 会给出等价的几何版本。

## 批注

**〔背景直觉〕尖点性 = 没有常数项**　沿 $U$ 积分就是「取常数项」：把 $f$ 沿幂幺方向平均掉。尖点函数就是所有常数项都为零的函数——它们不来自任何真抛物子群诱导上来的表示。§2.8 的 $r^n_{n_1,n_2}=0$ 是同一条件的几何翻译。

## 相关

[[global-hecke]]、[[constant-term]]

## 来源

- D. Gaitsgory《几何朗兰兹的非正式导论》，Bernstein–Gelbart 编《朗兰兹纲领导论》第 12 章，Birkhäuser 2004，pp. 269–281，§1.8，原书 pp. 272（PDF pp. 274）
  - 锚点：`08_source_code/SY02-13_Gaitsgory_几何朗兰兹非正式导论_中文译注/源码/chapters/ch12_sec1.tex:112-136（§1.8）`
