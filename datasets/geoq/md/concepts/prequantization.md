# 预量子化线丛

> `geoq/concept/prequantization` · 轨道 D · 几何量子化机器 · 状态 draft

> **先自测**：预量子化的曲率为什么必须等于 −(i/ℏ)ω？它满足狄拉克原理的哪几条，又为什么还不是真正的量子化？

## 一句话

用带相容联络的厄米线丛把经典可观测量提升为截面算子 Q(f)=iℏ∇_{V_f}+f；曲率锁定为 −(i/ℏ)ω 保证括号关系，但希尔伯特空间仍太大。

## 定义

辛流形 $(M,\omega)$ 上的预量子化线丛，是指一个厄米线丛 $(\mathcal{L},\langle-, -\rangle)$ 连同与内积相容的联络 $\nabla$，使得 $\nabla$ 的曲率 2-形式满足 $F_\nabla=-\frac{i}{\hbar}\omega$。给定它之后，对每个光滑函数 $f$ 定义算子 $Q(f)=i\hbar\nabla_{V_f}+f$，作用在 $\mathcal{L}$ 的光滑截面上，其中 $\nabla_f:=\nabla_{V_f}$ 是沿哈密顿向量场 $V_f$ 的协变导数。

**记号约定**：$\nabla_X$ 表示沿向量场 $X$ 的协变导数；$\Gamma(M,\mathcal{L})$ 是 $\mathcal{L}$ 的光滑截面空间；$\langle s_1|s_2\rangle=\int_M\langle s_1,s_2\rangle\,\frac{\omega^n}{n!}$ 是整体厄米内积。约定内积关于第一个变量共轭线性、关于第二个变量复线性。

## 要点

- 曲率条件不是装饰：只有 $F_\nabla=-\frac{i}{\hbar}\omega$ 才能让曲率项与泊松括号项在 $[Q(f),Q(g)]$ 中相消，从而得到 $[Q(f),Q(g)]=i\hbar Q(\{f,g\})$。
- $Q(1)=1$ 自动成立，$\mathbb{R}$-线性也显然；自伴性来自联络与厄米内积的相容性，加上哈密顿流保持刘维尔体积 $\omega^n/n!$。
- 预量子化只满足狄拉克原理的 Q1–Q4，不满足 Q5：$L^2(M,\mathcal{L})$ 的截面同时依赖全部 $2n$ 个相空间变量，而且 $Q(f)$ 对任意 $f$ 都只是一阶微分算子。
- 预量子化线丛是否存在是拓扑问题：$\frac{i}{2\pi}F_\nabla$ 是 $\mathcal{L}$ 的第一陈类，必须为整上同调类；反过来，整性也是存在性的充分条件。
- 完整量子化 = 预量子化 + 极化（砍掉一半变量）+ 半形式修正（补上马斯洛夫相位）；预量子化只是这条流水线的第二步。

## 关键公式

$$
$F_\nabla=-\frac{i}{\hbar}\omega$
$$

$$
$Q(f)=i\hbar\nabla_{V_f}+f$
$$

$$
$[Q(f),Q(g)]=i\hbar Q(\{f,g\})$
$$

$$
$\langle Q(f)s_1|s_2\rangle=\langle s_1|Q(f)s_2\rangle$
$$

$$
$\frac{1}{2\pi\hbar}[\omega]\in H^2(M;\mathbb{Z})$
$$

## 定理与证明

### 预量子化满足 Q1–Q4

设 $(\mathcal{L},\langle-, -\rangle,\nabla)$ 是 $(M,\omega)$ 上的预量子化线丛，$Q(f)=i\hbar\nabla_f+f$。则 $Q$ 是 $\mathbb{R}$-线性的（Q1），$Q(1)=1$（Q2），每个实函数 $f$ 的 $Q(f)$ 关于整体厄米内积自伴（Q3），且 $[Q(f),Q(g)]=i\hbar Q(\{f,g\})$（Q4）。

**完整证明**

1. 展开 $[Q(f),Q(g)]=[i\hbar\nabla_f+f,\,i\hbar\nabla_g+g]$。利用 $[\nabla_f,g]=V_f(g)=\{f,g\}$、$[f,\nabla_g]=-\{f,g\}$，并把 $[\nabla_f,\nabla_g]$ 换成 $\nabla_{\{f,g\}}+F_\nabla(V_f,V_g)$，得到 $[Q(f),Q(g)]=i\hbar Q(\{f,g\})+(i\hbar)^2F_\nabla(V_f,V_g)+i\hbar\{f,g\}$。
   - *为什么*：先把协变导数的交换子化为「沿泊松括号的导数 + 曲率」；这一步只用联络的定义，不涉及曲率取值。
2. 代入 $F_\nabla=-\frac{i}{\hbar}\omega$，并用 ${f,g}=\iota_{V_f}\iota_{V_g}\omega=-\omega(V_f,V_g)$，得 $(i\hbar)^2F_\nabla(V_f,V_g)=i\hbar\omega(V_f,V_g)=-i\hbar\{f,g\}$。于是多余的两项 $i\hbar\{f,g\}$ 与 $-i\hbar\{f,g\}$ 相消，剩下 $[Q(f),Q(g)]=i\hbar Q(\{f,g\})$。
   - *为什么*：这是曲率条件的唯一用处：它把曲率项精确调成泊松括号项的反号，从而恢复量子括号关系。
3. $Q(1)=i\hbar\nabla_{V_1}+1$，而 $V_1=0$，故 $Q(1)=1$；$Q$ 对 $f$ 的线性来自 $\nabla$ 与乘法的线性。
   - *为什么*：验证 Q2 与 Q1；$V_1=0$ 因为 $\iota_{V_1}\omega=d1=0$ 且 $\omega$ 非退化。
4. 对实函数 $f$ 与紧支集截面 $s_1,s_2$，由 $\nabla_f\langle s_1,s_2\rangle=\langle\nabla_fs_1,s_2\rangle+\langle s_1,\nabla_fs_2\rangle$ 积分，并用刘维尔定理 $\mathscr{L}_{V_f}(\omega^n/n!)=0$ 分部积分，得 $\langle Q(f)s_1|s_2\rangle=\langle s_1|Q(f)s_2\rangle$。
   - *为什么*：自伴性需要把导数从 $s_1$ 移到 $s_2$；哈密顿流保体积使分部积分的边界项与体积导数项都消失。
5. 综合 1–4：$Q$ 满足 Q1、Q2、Q3、Q4。
   - *为什么*：四条性质各自独立验证完毕，结论成立。

来源：ch05b.tex:857-950（原书 p.285–286）

### 预量子化线丛的存在性判据

辛流形 $(M,\omega)$ 上存在预量子化线丛，当且仅当 $\frac{1}{2\pi\hbar}[\omega]$ 是整上同调类，即对每个闭曲面 $\Sigma\subset M$ 都有 $\frac{1}{2\pi\hbar}\int_\Sigma\omega\in\mathbb{Z}$。

**证明提纲**

1. 必要性：若 $\mathcal{L}$ 存在，则 $\frac{i}{2\pi}F_\nabla=c_1(\mathcal{L})$ 是第一陈类，陈类的整性给出 $\frac{i}{2\pi}\int_\Sigma F_\nabla\in\mathbb{Z}$；代入 $F_\nabla=-\frac{i}{\hbar}\omega$ 即得 $\frac{1}{2\pi\hbar}\int_\Sigma\omega\in\mathbb{Z}$。
   - *为什么*：陈类整性是线丛拓扑的基本事实，与联络选取无关。
2. 充分性：若 $\frac{1}{2\pi\hbar}[\omega]$ 整，则由陈类的分类定理，存在以 $\frac{i}{2\pi\hbar}\omega$ 为第一陈类的厄米线丛，再取相容联络使其曲率为 $-(i/\hbar)\omega$。
   - *为什么*：这一步把「上同调类」实现为「线丛 + 联络」，用的是线丛的分类定理，书中只作引用。

> **缺口**：充分性依赖「任何整上同调类都可实现为某复线丛的第一陈类」这一分类定理，书中未给出证明；本卡把它作为黑箱，只强调判据的用法。


来源：ch05b.tex:951-973（原书 p.286–287）

## 易错点

- 曲率符号不能写反：必须是 $F_\nabla=-\frac{i}{\hbar}\omega$。若写成 $+\frac{i}{\hbar}\omega$，Q4 会出现 $2i\hbar\{f,g\}$ 的多余项。
- 预量子化 ≠ 量子化。它满足 Q1–Q4 但不满足 Q5；把 $Q(f)$ 当成薛定谔算子会得出「所有算子都是一阶」的错误结论。
- 在平凡线丛 $\mathcal{L}=M\times\mathbb{C}$ 上取 $\nabla=d-\frac{i}{\hbar}\theta$ 时，曲率是 $F_\nabla=-\frac{i}{\hbar}d\theta$；只有当 $\omega=d\theta$ 恰当（如余切丛）时这才是预量子化线丛。
- 整体内积用 $\omega^n/n!$，不是 $\omega^n$；这个 $1/n!$ 是刘维尔体积的标准归一化，丢了会让自伴性计算出错。

## 相关卡

- [辛流形（symplectic manifold）](../concepts/symplectic-manifold.md)
- [可量子化条件（陈类整性）](../concepts/quantization-condition.md)
- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [量子希尔伯特空间与半形式修正](../concepts/quantum-hilbert-space.md)
- [量子算子与 P-保持条件](../concepts/quantum-operator.md)
- [余切丛总可量子化](../examples/cotangent-bundle-quantizable.md)
- [$S^2$ 的可量子化条件 $A\in\frac{\hbar}{2}\mathbb{Z}$](../examples/s2-quantization-condition.md)

## 出处

- §5.4.2 预量子化，p.284–285（PDF p.285–286），源码 `ch05b.tex:817-907`
- §5.4.2 定义 5.4.2 与自伴性，p.285–286（PDF p.286–287），源码 `ch05b.tex:880-950`
