# Maslov 指标与分次

> `seidel/concept/maslov-index` ｜ track B ｜ draft

**一句话**：Lagrangian 子空间环路的拓扑绕数；它给出 Lagrange Grassmannian 的普适类，其为零是 Lagrangian 存在分次的障碍。

**自测**：为什么 Floer 复形能按整数分次，而一般的 Lagrangian 只能给出模 2 分次？

## 定义

设 $V$ 是 $2n$ 维辛向量空间，$\mathrm{Gr}(V)$ 是 Lagrangian Grassmannian。取固定 Lagrangian $V_0$。对环路 $\Lambda:S^1\to\mathrm{Gr}(V)$，其 Maslov 指标 $\mu(\Lambda)$ 是 $\Lambda$ 与各层 $\Sigma_k=\{\Lambda:\dim(\Lambda\cap V_0)=k\}$ 的带符号相交数之和。
对 Lagrangian $L\subset M$，若存在连续函数 $\alpha:L\to\R$ 使
$$e^{2\pi i\alpha(x)}=\frac{\vartheta_V(v_1\wedge\cdots\wedge v_n)^2}{|\vartheta_V(v_1\wedge\cdots\wedge v_n)|^2},$$
其中 $v_1,\ldots,v_n$ 是 $T_xL$ 的基、$\vartheta_V$ 是 $V$ 的复体积形式，则称 $\alpha$ 为 $L$ 的分次；其障碍是 Maslov 类 $\mu_L\in H^1(L;\Z)$。

记号：$\alpha$ 只在相差整数意义下确定；$\mu(x)$ 是交点 $x$ 处两分次之差（取整）。

## 要点

- $L$ 可分次当且仅当 Maslov 类 $\mu_L=0\in H^1(L;\Z)$；单连通 $L$ 自动可分次。
- 交点分次 $\mu(x)$ 使 $\mu^1$ 降次 $1$；这是 Floer 复形成为分次复形的根据。
- 没有分次时只剩相对分次（模 $2$ 或模 $N$），A∞ 结构的符号也随之退化。

## 公式

$$\mu(\Lambda)=\sum_k \#(\Lambda\pitchfork\Sigma_k)\,\mathrm{sign}$$
$$\mu(x)=\alpha_1(x)-\alpha_0(x)\in\Z$$

## 定理与证明

### 分次存在的障碍是 Maslov 类

紧致 Lagrangian $L$ 存在分次当且仅当 Maslov 类 $\mu_L\in H^1(L;\Z)$ 为零。

（complete；来源：原书 §11e–11j（p.157–171））

1. 必要性：若 $\alpha$ 单值，则 $e^{2\pi i\alpha}=\alpha_V(TL)$ 给出相位映射 $L\to S^1$ 的提升，故其障碍 $\mu_L$ 为零。  
   为什么：Maslov 类正是相位映射 $L\to S^1$ 的同伦障碍。
2. 充分性：若 $\mu_L=0$，相位映射 $L\to S^1$ 可提升为 $\tilde\alpha:L\to\R$，令 $\alpha=\tilde\alpha$。  
   为什么：$H^1(L;\Z)$ 中的障碍为零等价于存在这样的提升。
3. 由 $\alpha_V$ 的定义，$e^{2\pi i\alpha}=\alpha_V(TL)$ 按构造成立。  
   为什么：提升正是相位映射的单值化。

## 易错点

- $\alpha$ 与 $\alpha+k$ 给出同一分次，交点分次只在相差整体常数意义下确定。
- Maslov 类的符号约定与 $\det^2$ 的复相位约定必须与全书统一，否则 $\mu(x)$ 整体差符号。
- $n=1$ 时 $\mathrm{Gr}(V)\cong S^1$，Maslov 指标仍给出 $\pi_1\cong\Z$；$w_2:\pi_2\to\Z/2$ 的讨论在 $n=1,2$ 时需单独处理，定理 A 的 $n\ge1$ 并不排除 $n=1$。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§11e–11j，p.157–171（原书 p.157 §11e）

关联：`seidel/concept/floer-complex`、`seidel/concept/brane-structure`、`seidel/deriv/mu-d-grading`

来源说明：据原书 §11e–11j（p.157–171）转述；译者注 A06-xx。
