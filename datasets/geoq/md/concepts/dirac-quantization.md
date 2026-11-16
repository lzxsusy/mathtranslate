# 狄拉克量子化原理 Q1–Q5

> `geoq/concept/dirac-quantization` · 轨道 D · 几何量子化机器 · 状态 draft

> **先自测**：狄拉克原理的五条要求各是什么？为什么 Q4 是核心，而 Q1–Q3 与 Q5 与它彼此独立？

## 一句话

狄拉克把量子化定义为从经典可观测量到自伴算子的对应，并列出五条要求：实数线性、保单位、实函数自伴、括号关系、完全集保持。四条约束算子代数，第五条约束希尔伯特空间的大小。

## 定义

设 $(M,\omega)$ 是经典相空间。经典可观测量是光滑函数空间 $\mathrm{Obs}^{cl}=C^\infty(M)$，带泊松括号 $\{-, -\}$；量子可观测量是希尔伯特空间 $\mathbb{H}$ 上的一族算子 $\mathrm{Obs}^{q}$，带交换子 $[\mathcal{O}_1,\mathcal{O}_2]=\mathcal{O}_1\mathcal{O}_2-\mathcal{O}_2\mathcal{O}_1$。若一个函数 $g$ 与 $f_1,\dots,f_m$ 的泊松括号全为零就迫使 $g$ 是常数，则称 $\{f_1,\dots,f_m\}$ 是经典可观测量的完全集；量子侧用交换子作同样的定义，与所有 $\mathcal{O}_i$ 对易的算子只能是 $\mathbf{1}$ 的倍数。狄拉克量子化原理（Dirac's principle）要求一个对应 $Q:\mathrm{Obs}^{cl}\to\mathrm{Obs}^{q}$，$f\mapsto\hat f$，满足五条：Q1 $Q$ 是 $\mathbb{R}$-线性的；Q2 $\hat 1=\mathbf{1}$；Q3 实值函数的像自伴；Q4 对一切 $f,g$ 有 $[\hat f,\hat g]=i\hbar\widehat{\{f,g\}}$；Q5 完全集的像仍是完全集。

**记号约定**：$\hat f:=Q(f)$；$\hbar$ 是约化普朗克常数，在整个讨论中固定；$\{-, -\}$ 由辛形式 $\omega$ 决定；$\mathbf{1}$ 是 $\mathbb{H}$ 上的恒等算子；$\mathrm{Sym}$ 表示对称序平均；$P^{\le k}$ 是次数不超过 $k$ 的实多项式空间。

## 要点

- Q4 是唯一把经典与量子粘起来的条件：它把 $Q$ 说成李代数同态，其余四条都不产生这个等式。
- 把哈密顿向量场直接当成算子，$f\mapsto i\hbar V_f$，满足 Q1、Q3、Q4，却把 $1$ 送到 $0$，因此独自违反 Q2；补上 $+f$ 这一项就得到预量子化的 $Q(f)=i\hbar\nabla_f+f$。
- 外尔量子化 $\mathcal{W}_\hbar$ 满足 Q1–Q3，并在二次及以下的多项式上满足 Q4；修正项 $\frac{(i\hbar)^3}{24}\Lambda^3$ 从两个次数之和为 $6$ 的多项式开始出现。
- Q5 不是代数条件而是表示论条件：它要求 $\mathbb{H}$ 在算子族作用下足够不可约，这正是薛定谔表示满足而预量子化不满足的那一条。
- Q4 与 Q5 一般不能同时满足，这是下一张卡（格罗嫩沃尔德–范霍夫定理）的内容；因此实际做法是保住 Q1–Q4、放弃 Q5，再用极化把希尔伯特空间砍小。

## 关键公式

$$
$Q:\mathrm{Obs}^{cl}\to\mathrm{Obs}^{q},\qquad f\mapsto\hat f$
$$

$$
$[\hat f,\hat g]=i\hbar\widehat{\{f,g\}}$
$$

$$
$\mathcal{W}_\hbar(f)=\mathrm{Sym}\,f(\hat x,\hat p),\qquad \hat x^i=x^i,\quad \hat p_i=-i\hbar\partial_{x^i}$
$$

$$
$[f,g]_*=f*_\hbar g-g*_\hbar f=i\hbar\{f,g\}+\frac{(i\hbar)^3}{24}\Lambda^3(fg)+\cdots$
$$

$$
$\{g,f_1\}=\cdots=\{g,f_m\}=0\ \Longrightarrow\ g=\mathrm{const}$
$$

## 定理与证明

### Q4 与李代数同态等价

设 $Q:C^\infty(M)\to\mathrm{Obs}^{q}$ 是 $\mathbb{R}$-线性映射，$\hbar\ne0$。则 Q4 对一切 $f,g$ 成立，当且仅当 $Q$ 是李代数同态 $(C^\infty(M),\hbar^{-1}\{-, -\})\to(\mathrm{Obs}^{q},\frac{1}{i\hbar}[-,-])$。Q2、Q3、Q5 各自与 Q4 独立：Q2 固定单位元，Q3 是 $*$-条件 $Q(\bar f)=Q(f)^{\dagger}$，Q5 要求完全集的像仍然完全。

**完整证明**

1. Q4 两边同除以非零的 $i\hbar$，得 $\frac{1}{i\hbar}[Q(f),Q(g)]=Q(\{f,g\})$。右端是「先取括号再量子化」，左端是「先量子化再取括号」，加上 Q1 保证的线性，这恰好是李代数同态 $(C^\infty(M),\hbar^{-1}\{-, -\})\to(\mathrm{Obs}^{q},\frac{1}{i\hbar}[-,-])$ 的定义。
   - *为什么*：除以 $i\hbar$ 只是把系数并进括号的定义里，可逆，不改变条件的内容。
2. 反向读同一个等式：若 $Q$ 是上述同态，把定义式乘以 $i\hbar$ 就回到 Q4。所以 Q4 与同态性互为充要条件。
   - *为什么*：两个方向是同一个等式的两种读法，不需要额外构造。
3. 其余四条与 Q4 互相独立。由 $\{1,g\}=0$，Q4 只给出 $[\hat 1,\hat g]=0$，故 $f\mapsto i\hbar V_f$ 满足 Q1、Q3、Q4 却把 $1$ 送到 $0$，破坏 Q2；括号看不见内积，故非酉表示照样满足 Q1、Q2、Q4，Q3 必须单独提出；Q5 约束的是 $\mathbb{H}$ 中不再残留对易量，与前四条没有逻辑蕴含。
   - *为什么*：每条失败方式都有具体反例，说明五个条件各自管一件不同的事。

来源：ch05b.tex:586-611（原书 p.280–281）

### 外尔量子化从两个三次多项式起违反 Q4

对 $\mathbb{R}^{2n}$ 上的多项式，外尔量子化满足 $\mathcal{W}_\hbar(f)\mathcal{W}_\hbar(g)=\mathcal{W}_\hbar(f*_\hbar g)$，故 $[\mathcal{W}_\hbar(f),\mathcal{W}_\hbar(g)]=\mathcal{W}_\hbar([f,g]_*)$，而 $[f,g]_*=i\hbar\{f,g\}+\frac{(i\hbar)^3}{24}\Lambda^3(fg)+\cdots$。当 $\deg f,\deg g\le2$ 时修正项为零，Q4 成立；但取 $f=x^3$、$g=p^3$ 得 $[x^3,p^3]_*=9i\hbar\,x^2p^2+\frac32(i\hbar)^3$，与 $i\hbar\{x^3,p^3\}=9i\hbar\,x^2p^2$ 相差非零常数，Q4 失效。

**完整证明**

1. 星乘积由双微分算子给出：$f*_\hbar g=f\exp(\frac{i\hbar}{2}\Lambda)g$，其中 $\Lambda=\overleftarrow{\partial_{x^i}}\overrightarrow{\partial_{p_i}}-\overleftarrow{\partial_{p_i}}\overrightarrow{\partial_{x^i}}$，每个导数对左右两个因子分别作用。
   - *为什么*：这是外尔对应的定义性质：对称序把函数乘法换成星乘积，$x$ 与 $p$ 的指数形式来自 BCH 公式。
2. 两式相减：$[f,g]_*=f*_\hbar g-g*_\hbar f=2i\sin(\frac{\hbar\Lambda}{2})(fg)=i\hbar\Lambda(fg)-\frac{i\hbar^3}{24}\Lambda^3(fg)+\cdots$；首项就是泊松括号，因为 $\Lambda(fg)=\{f,g\}$。
   - *为什么*：减掉反序只剩 $\sin$ 的奇次项，偶次项（包括 $\hbar^2$ 阶）全部抵消，所以第一个修正项是 $\hbar^3$ 阶。
3. $\Lambda$ 的每一项取一个 $x$ 导数和一个 $p$ 导数，故 $\Lambda^3(fg)$ 要求 $\deg f+\deg g\ge6$。当 $\deg f,\deg g\le2$ 时总次数不超过 $4$，修正项为零，$[f,g]_*=i\hbar\{f,g\}$，Q4 成立。
   - *为什么*：这就是二次多项式上「外尔量子化看起来满足狄拉克原理」的原因，也说明障碍最早出现在总次数 $6$ 的情形。
4. 反例：$\Lambda(x^3p^3)=9x^2p^2$，$\Lambda^2(x^3p^3)=36xp$，$\Lambda^3(x^3p^3)=36$，故 $[x^3,p^3]_*=9i\hbar\,x^2p^2+\frac{36}{24}(i\hbar)^3=i\hbar\{x^3,p^3\}+\frac32(i\hbar)^3$。
   - *为什么*：这里 $x^3$ 与 $p^3$ 的混合偏导在最底层给出常数 $6\cdot6=36$，修正项因此不为零。
5. 外尔量子化在多项式上是单射（其逆由符号映射给出），故 $c=\frac32(i\hbar)^3\ne0$ 推出 $\mathcal{W}_\hbar(c)\ne0$，于是 $[\mathcal{W}_\hbar(x^3),\mathcal{W}_\hbar(p^3)]\ne i\hbar\mathcal{W}_\hbar(\{x^3,p^3\})$。
   - *为什么*：差异是一个非零常数算子，不能靠重新定义低次多项式上的 $Q$ 吸收掉，所以这是真正的障碍而不是约定问题。

来源：ch05b.tex:612-660（原书 p.281）

## 易错点

- 五条的编号与内容要一一对应：Q1 是实数线性，Q2 是 $\hat 1=\mathbf{1}$，Q3 是实函数自伴，Q4 是括号关系，Q5 是完全集。别把 Q2 说成「线性」，也别把 Q5 说成「算子两两对易」——Q5 说的是不存在同时与全部 $\hat f_i$ 对易的非平凡算子。
- $\mathcal{W}_\hbar$ 是一个具体的映射（外尔量子化），不是狄拉克原理要求的一般 $Q$。它满足 Q1–Q3，但只在低次多项式上满足 Q4，所以它本身不是 Q1–Q5 意义下的量子化；格罗嫩沃尔德–范霍夫定理禁止的正是「在 $P^{\le4}$ 上与 $\mathcal{W}_\hbar$ 一致又满足 Q4」的 $Q$。
- Q1 只要求实数线性，不要求复线性：若强行要求 $Q(if)=iQ(f)$，则实值函数的像不可能自伴（Q3），两条会直接冲突。

## 相关卡

- [格罗嫩沃尔德–范霍夫定理（Groenewold–Van Hove）](../concepts/groenewold-van-hove.md)
- [预量子化线丛](../concepts/prequantization.md)
- [海森堡李代数 $h_V$](../concepts/heisenberg-lie-algebra.md)
- [量子算子与 P-保持条件](../concepts/quantum-operator.md)

## 出处

- §5.4.1 狄拉克量子化原理（Q1–Q5 与完全集），p.280–281（PDF p.281–282），源码 `ch05b.tex:559-611`
- §5.4.1 外尔量子化与 Moyal 乘积，p.281（PDF p.282），源码 `ch05b.tex:612-661`
