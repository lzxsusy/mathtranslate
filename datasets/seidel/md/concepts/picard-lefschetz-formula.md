# Picard–Lefschetz 公式

> `seidel/concept/picard-lefschetz-formula` ｜ track C ｜ draft

**一句话**：绕临界值一圈的单值在同调上的显式公式：沿消失圈做一次反射，$x\mapsto x\pm\langle x,\delta\rangle\delta$；它是 Dehn 扭转的同调影子。

**自测**：为什么绕一个临界点的单值只是一次「沿消失圈的反射」？

## 定义

设 $\pi:X\to\C$ 是 Lefschetz 纤维化，$0$ 是临界值，$\delta\subset F=\pi^{-1}(1)$ 是相应的消失圈（$\dim_\C F=n-1$，即 $\dim_\R F=2(n-1)$，故 $\delta\cong S^{n-1}$ 是中间维球面）。沿绕 $0$ 的正圈平行移动给出单值 $h\in\mathrm{Aut}(H_{n-1}(F))$。Picard–Lefschetz 公式说
$$h(x)=x+\varepsilon\,\langle x,\delta\rangle\,\delta,$$
其中 $\langle\cdot,\cdot\rangle$ 是 $H_{n-1}(F)$ 上的相交形式，$\varepsilon=\pm1$ 由维数与定向约定决定；在 $n=2$（曲面纤维、消失圈为曲线）的常用约定下 $\varepsilon=+1$。

记号：$F$ 是光滑纤维；相交形式在 $n$ 偶时反对称、$n$ 奇时对称；$\delta$ 的定向选取影响 $\varepsilon$ 的符号。

## 要点

- 公式把单值约化为「沿 $\delta$ 的一次 transvection/反射」：只有 $\delta$ 方向被改动，$\delta^\perp$ 上 $h$ 为恒等。
- $n$ 偶（相交形式反对称）时 $\langle\delta,\delta\rangle=0$，$(h-\mathrm{id})^2=0$，$h$ 是 transvection；$n$ 奇（对称）时 $\langle\delta,\delta\rangle=\pm2$，$h^2=\mathrm{id}$，$h$ 是反射。
- 几何上 $h\simeq\tau_\delta$（式 16.6）：公式是 Dehn 扭转在同调上的痕迹，链层次的对应物是扭曲函子与锥构造。
- 沿多条消失路径的复合 $\tau_{\delta_1}\cdots\tau_{\delta_m}$ 只依赖临界值的绕行次序，给出辫群 $\mathrm{Br}_m$ 在纤维上的表示；换特选基由 Hurwitz 移动联系，故整体单值不变。
- 与 vanishing-cycle / matching-cycle 卡的分工：那两张讲对象的几何构造，本卡讲 monodromy 对同调的显式作用。

## 公式

$$h(x)=x+\varepsilon\langle x,\delta\rangle\delta$$
$$\tau_\delta(x)=x+\langle x,\delta\rangle\delta\quad(n=2)$$
$$h=\tau_{\delta_1}\cdots\tau_{\delta_m}\in\mathrm{Aut}(H_{n-1}(F))$$

## 定理与证明

### Picard–Lefschetz 公式

设 $\pi:X\to\C$ 在 $0$ 附近只有一个非退化临界点，$\delta$ 为消失圈。则绕 $0$ 的单值 $h$ 在 $H_{n-1}(F)$ 上满足 $h(x)=x+\varepsilon\langle x,\delta\rangle\delta$，$\varepsilon=\pm1$。

（sketch；来源：原书 p.224 式 (16.6)（几何版本 $h_\gamma\simeq\tau_{V_\gamma}$）；同调公式为经典 Picard–Lefschetz 公式，原书未给证明）

1. 把环路收缩到临界值附近，单值只由局部模型 $z_0^2+\cdots+z_n^2$ 决定。  
   为什么：临界值外单值是局部常值的，同痕不改变它。
2. 在局部模型中 $\delta$ 是实部为零的球面；沿正圈平行移动返回时，$\delta$ 的定向翻转而 $\delta^\perp$ 不动。  
   为什么：消失圈的平行移动由 $\mathrm{Re}(z_0)$ 的符号决定，绕一圈恰好换号。
3. 任一闭链 $x$ 唯一分解为 $\delta$ 方向与 $\delta^\perp$ 部分；前者被反射，后者固定。  
   为什么：相交形式非退化，故正交分解唯一。
4. 合并得 $h(x)=x+\varepsilon\langle x,\delta\rangle\delta$。  
   为什么：反射把 $\delta$ 送到 $-\delta$，与公式在 $x=\delta$ 处一致。

缺口：原书 §16c 只给几何版本 (16.6) 并明说不给证明（p.224），同调版 $h(x)=x+\varepsilon\langle x,\delta\rangle\delta$ 属经典结论；$\varepsilon$ 的精确符号依赖 §16d 的定向约定。

### 复合单值与辫单值

对特选基 $\delta_1,\dots,\delta_m$，绕所有临界值一次的复合单值同痕于 $\tau_{\delta_1}\cdots\tau_{\delta_m}$；改变基只做 Hurwitz 移动，不改变复合的同痕类。

（sketch；来源：原书 p.283–284 §18g（复合单值=monodromy）、p.225–226 §16d（Hurwitz 移动与辫群））

1. 每个临界值局部贡献 $\tau_{\delta_k}$（式 16.6）。  
   为什么：单值在临界值附近局部化，局部模型与整体无关。
2. 沿大圈依次经过各临界值，复合为乘积；次序由路径上临界值的出现次序决定。  
   为什么：单值对路径有函子性，乘积次序不能交换。
3. Hurwitz 移动对应初等变异，乘积在同痕下不变。  
   为什么：辫群关系 $\tau_i\tau_{i+1}\tau_i=\tau_{i+1}\tau_i\tau_{i+1}$ 在几何上由匹配路径的移动实现。

缺口：辫群关系的几何验证见 §16d；这里只给路线。

## 易错点

- 符号 $\varepsilon$：不同教材的定向/相交形式约定差一个 $(-1)^{n(n-1)/2}$，照抄会得到相反符号；原书只在 §16c 给几何版 (16.6)，同调版的符号约定须自行与 §16d 对齐。
- 公式作用在 $H_{n-1}(F)$（消失圈维数 $n-1$），不是 $H_n$；$n=2$ 时作用在 $H_1$。
- $n$ 奇时 $h$ 是反射（$h^2=\mathrm{id}$），$n$ 偶时是 transvection（$(h-\mathrm{id})^2=0$）；不要一律说成「幂零」。
- PL 公式只给同调作用；链层次/Floer 层次要用 $h\simeq\tau_\delta$ 与扭曲函子，不能直接由公式读出。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§16c，p.223–224（原书 p.224 §16c）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§18g，p.283–284（原书 p.284 §18g）

关联：`seidel/concept/vanishing-cycle`、`seidel/concept/thimble`、`seidel/concept/lefschetz-fibration`、`seidel/deriv/mapping-cone`

来源说明：据原书 §16c（p.223–224）与 §18g（p.283–284）转述；译者注 A11-10；外部参考 nLab「Picard–Lefschetz theory」与 Seidel《Vanishing cycles and mutation》（arXiv:math/0007115）。
