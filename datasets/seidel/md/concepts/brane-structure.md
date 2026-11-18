# 膜结构

> `seidel/concept/brane-structure` ｜ track B ｜ draft

**一句话**：把实值分次与 Pin 结构一起加在 Lagrangian 上；它使 Floer 复形有整数分次、模空间有定向。

**自测**：为什么单有 Lagrangian 子流形还不够，还要额外加「膜结构」？

## 定义

$L$ 上的膜结构是一对 $(\alpha^\#,P^\#)$：实值分次 $\alpha^\#:L\to\R$ 满足
$$e^{2\pi i\alpha^\#(x)}=\alpha_M(T_xL),$$
其中 $\alpha_M$ 是平方相位映射；$P^\#$ 是 $TL$ 的 Pin 结构。等价地，它是 $L$ 到抽象膜空间
$$\mathrm{Gr}(V)^\#\longrightarrow K(\Z,1)\times K(\Z/2,2)$$
的一个提升点 $\Lambda^\#$，第一个因子记录 Maslov 类 $\mu$，第二个记录 $w_2$。

记号：$K(\Z/2,2)$ 的分类给出 $w_2$；Pin 结构是 $O_n$ 的 $\Z/2$ 中心扩张，与系数域的特征无关。

## 要点

- 膜结构 $=$ 分次 $+$ 相对 Pin 结构；两者分别负责 Floer 复形的分次与模空间的定向。
- $n\ge3$ 时 $\mathrm{Gr}(V)^\#$ 是 $\mathrm{Gr}(V)$ 的 $2$-连通覆叠；$n=1$ 时 $\pi_1=\Z/2,\pi_2=0$，$n=2$ 时 $\pi_1=0,\pi_2=\Z$。
- 全书默认所有对象带膜结构；忘记它会使 $\mu^1$ 的符号与分次失去意义。

## 公式

$$\mathrm{Gr}(V)^\#\to K(\Z,1)\times K(\Z/2,2),\qquad \Lambda^\#\mapsto(\mu,w_2)$$
$$e^{2\pi i\alpha^\#(x)}=\alpha_M(T_xL),\qquad P^\#\text{ 是 }TL\text{ 的 Pin 结构}$$

## 定理与证明

### 膜结构给出 Floer 复形的整数分次

若 $L_0,L_1$ 带膜结构，则 $CF^*(L_0,L_1)$ 有整数分次，且 $\mu^1$ 的次数为 $1$。

（sketch；来源：原书 p.179–182 §12e–12f）

1. 分次 $\alpha_i$ 给出每个交点 $x$ 的整数 $\mu(x)=\alpha_1(x)-\alpha_0(x)$。  
   为什么：交点处两条 Lagrangian 的相位差取整即分次。
2. 条带模空间的维数等于 $\mu(x)-\mu(y)-1$；维数 $0$ 的条带满足 $\mu(y)=\mu(x)-1$。  
   为什么：指数定理把模空间维数写成 Maslov 指标差。
3. Pin 结构给每条条带的定向线一致定向，故 $\mu^1$ 的矩阵元带确定符号。  
   为什么：定向线的相容性来自相对 Pin 结构。

缺口：细节见原书 §11h、§12e–12f。

## 易错点

- Pin 结构不是 Spin 结构；对不可定向的 Lagrangian，只能用 Pin。
- 膜结构的两个障碍是 Maslov 类 $\mu_L\in H^1(L)$ 与 $w_2(TL)\in H^2(L;\Z/2)$；后者是 Pin 结构的绝对障碍。
- $K$ 的特征不影响膜结构本身；$\operatorname{char}K=2$ 时 $\pm1$ 的符号消失，但分次仍由相位提升给出，并不退回 §8 的无分次版本。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§11h–11j、§12f，p.163–182（原书 p.163 §11h）

关联：`seidel/concept/maslov-index`、`seidel/concept/fukaya-category`、`seidel/concept/exact-lagrangian`

来源说明：据原书 §11h–11j（p.163–171）与 §12f（p.179–182）转述；译者注 A06-xx。
