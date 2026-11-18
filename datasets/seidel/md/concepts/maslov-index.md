# Maslov 指标与分次

> `seidel/concept/maslov-index` ｜ track B ｜ draft

**一句话**：Lagrangian 子空间环路绕固定子空间的拓扑绕数；对带分次的 Lagrangian，它给出每点的整值相位，决定 Floer 复形的分次。

**自测**：为什么 Floer 复形能按整数分次，而一般的 Lagrangian 只能给出模 2 分次？

## 定义

设 $V$ 是 $2n$ 维辛向量空间，$\Lambda(V)$ 是 Lagrangian Grassmannian。取固定 Lagrangian $V_0$。对环路 $\Lambda:S^1\to\Lambda(V)$，其 Maslov 指标 $\mu(\Lambda)$ 是 $\Lambda$ 与 $\{\Lambda:\dim(\Lambda\cap V_0)=k\}$ 的各层相交数（带符号）之和。
对 Lagrangian $L\subset M$，若存在连续函数 $\alpha:L\to\R$ 使
$$e^{2\pi i\alpha(x)}=\det^2(T_xL)\quad(\text{相对某平凡化}),$$
则称 $\alpha$ 为 $L$ 的分次；$[d\alpha]\in H^1(L;\Z)$ 即 Maslov 类。

记号：$\alpha$ 只在相差整数意义下确定；$\mu(x)$ 是交点 $x$ 处两分次之差（取整）。

## 要点

- $L$ 可分次当且仅当 Maslov 类 $[d\alpha]=0$；单连通 $L$ 自动可分次。
- 交点分次 $\mu(x)$ 使 $\mu^1$ 降次 $1$；这是 Floer 复形成为分次复形的根据。
- 没有分次时只剩相对分次（模 $2$ 或模 $N$），A∞ 结构的符号也随之退化。

## 公式

$$\mu(\Lambda)=\sum_k \#(\Lambda\pitchfork\Sigma_k)\,\mathrm{sign}$$
$$\mu(x)=\alpha_1(x)-\alpha_0(x)\in\Z$$

## 定理与证明

### 分次存在的障碍是 Maslov 类

紧致 Lagrangian $L$ 存在分次当且仅当 $[d\alpha]=0\in H^1(L;\Z)$。

（complete；来源：原书 p.150–157 §11）

1. 必要性：若 $\alpha$ 单值，则 $d\alpha$ 是整体定义的一形式，其周期为整数，故 $[d\alpha]\in H^1(L;\Z)$ 且为恰当类对应的整数周期。  
   为什么：$lpha$ 的单值性给出周期的整值性。
2. 充分性：若 Maslov 类为零，沿路径积分 $d\alpha$ 得到单值函数。  
   为什么：零类意味着沿任意闭环的积分为零，积分与路径无关。
3. 由 $\det^2$ 的定义，$\alpha$ 满足 $e^{2\pi i\alpha}=\det^2$。  
   为什么：构造时已按此相位方程取 $lpha$。

## 易错点

- $\alpha$ 与 $\alpha+k$ 给出同一分次，交点分次只在相差整体常数意义下确定。
- Maslov 类的符号约定与 $\det^2$ 的复相位约定必须与全书统一，否则 $\mu(x)$ 整体差符号。
- $n=1$（曲线）时 Maslov 指标退化，需单独处理；这也是定理 A 排除 $n=1$ 的技术原因之一。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§11，p.150–157（原书 p.150 §11）

关联：`seidel/concept/floer-complex`、`seidel/concept/brane-structure`、`seidel/deriv/mu-d-grading`

来源说明：据原书 §11（p.150–157）转述；译者注 A06-xx。
