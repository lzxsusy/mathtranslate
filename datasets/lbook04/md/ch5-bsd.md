# Birch–Swinnerton-Dyer 猜想

> `lbook04/concept/ch5-bsd` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** 为什么「$L(E,1)=0$ 的阶」能数出有理点群的秩，而首项系数还要乘上 regulator 与 Sha？

**一句话：** BSD 断言 $L(E,s)$ 在中心 $s=1$ 的零点阶等于 $E(\mathbb Q)$ 的 Mordell–Weil 秩，并给出首项系数与 regulator、Sha、扭转点的精确公式；它是 Clay 千禧问题之一。

**别名：** `BSD 猜想`、`秩与消失阶`、`Hasse–Weil 猜想`

## 定义

完备 $L$ 函数 $\Lambda(E,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s)$ 满足 $\Lambda(E,s)=\pm\Lambda(E,2-s)$（Hasse–Weil 猜想，$\mathbb Q$ 上现为定理）。BSD 猜想：$\operatorname{ord}_{s=1}L(E,s)=\operatorname{rank}E(\mathbb Q)$；更强地 $L(E,s)\sim c(s-1)^r$，$c$ 含 $|\mathrm{Sha}(E/\mathbb Q)|$、regulator、扭转点群阶与实周期。解析秩 $0$ 情形（$L(E,1)\ne0\Rightarrow$ 秩 $0$）由 Kolyvagin 等证明；解析秩 $1$ 由 Gross–Zagier 加 Kolyvagin 证明。

**记号：** $\Lambda(E,s)$：完备 $L$ 函数；$N$：导子；$r=\operatorname{rank}E(\mathbb Q)$；$\mathrm{Sha}(E/\mathbb Q)$：Tate–Shafarevich 群；$\operatorname{Reg}$：regulator；$\Omega_E$：实周期；$c_p$：Tamagawa 数。

## 要点

- $(3.12)$ 用 $\Gamma(s)$（不是 $\Gamma(s/2)$）与 $N^{s/2}$ 配套，使函数方程中心落在 $s=1$（权 $2$）。
- $(3.13)$ $\Lambda(E,s)=\pm\Lambda(E,2-s)$ 是 Hasse–Weil 猜想；$\mathbb Q$ 上由模性（Wiles 等）成为定理。
- BSD 有两层：弱形式（消失阶 $=$ 秩）与强形式（首项系数公式）。
- 已知情形：解析秩 $0\Rightarrow$ 代数秩 $0$（Kolyvagin）；解析秩 $1\Rightarrow$ 代数秩 $1$（Gross–Zagier $+$ Kolyvagin）。

## 公式

$$
\Lambda(E,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s)
$$

$$
\Lambda(E,s)=\pm\Lambda(E,2-s)
$$

$$
\operatorname{ord}_{s=1}L(E,s)=\operatorname{rank}E(\mathbb Q)
$$

$$
\frac{L^{(r)}(E,1)}{r!}=\frac{|\mathrm{Sha}|\cdot\operatorname{Reg}\cdot\prod_p c_p}{|E(\mathbb Q)_{\mathrm{tors}}|^2}\,\Omega_E
$$

## 易错点

- $\Gamma(s)$ 与 $\Gamma(s/2)$ 不能互换：权 $2$ 的椭圆曲线用 $\Gamma(s)$、中心 $s=1$；误用 $\Gamma(s/2)$ 会把中心挪走。
- BSD 的弱形式与强形式不同：消失阶只给秩，首项系数公式还涉及 Sha 与 regulator；不要用「$L(E,1)=0\iff$ 无穷多有理点」一句概括。

## 批注

**〔背景直觉〕为什么中心是 $1$**　权 $2$ 的 $L$ 函数对应 $s\leftrightarrow2-s$ 的对称轴 $s=1$。对一般权 $k$ 的模形式中心在 $s=k/2$；§5.2 的 $L(f,s)$ 与本卡 $(3.12)$ 差一个平移 $(k-1)/2$，比较时要注意。

**〔含糊点拨〕猜想还是定理**　Hasse–Weil 函数方程在 $\mathbb Q$ 上已是定理（模性 $+$ 局部计算），但 BSD 本身仍开放；书中「猜想 3.1」指函数方程，BSD 只在 §3.3 的注与 §6.2 语境出现，不要混为一条。

## 相关

[[ch5-elliptic-l]]、[[ch5-gross-zagier]]、[[ch5-eichler-shimura]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3.3，原书 pp. 99–100（PDF pp. 104–105）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:346-370`
