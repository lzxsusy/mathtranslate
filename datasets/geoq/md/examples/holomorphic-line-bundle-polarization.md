# 全纯线丛上的凯勒极化

> `geoq/example/holomorphic-line-bundle-polarization` · 轨道 D · 几何量子化机器 · 状态 draft

> **这张卡练什么**：当预量子化线丛本身就是全纯线丛时，凯勒极化会给出什么样的量子希尔伯特空间？

## 一句话

对全纯线丛取相容联络，其反全纯分量就是 Dolbeault 算子；令辛形式为曲率的 $i\hbar$ 倍，预量子化自动成立，极化截面即全纯截面。

## 设定

设 $M$ 是复流形，$\mathcal{L}\to M$ 是带 Hermitian 度量 $h$ 与其相容联络 $\nabla$ 的全纯线丛。要求 $(i/2\pi)F_\nabla$ 给出 $M$ 上的辛形式，并令 $\omega=i\hbar F_\nabla$；极化取 $P=T^{0,1}M$。

## 计算

**第 1 步**：分解联络：$\nabla=\nabla^{1,0}+\nabla^{0,1}$，相容性保证 $\nabla^{0,1}=\bar\partial$，即 Dolbeault 算子。

> 为什么：与复结构相容的联络其 $(0,1)$ 分量必须与 $\bar\partial$ 一致，否则与全纯截面的定义冲突。

**第 2 步**：验证预量子化条件：由 $\omega=i\hbar F_\nabla$ 直接得 $F_\nabla=-\frac{i}{\hbar}\omega$；闭性来自比安基恒等式 $dF_\nabla=0$，即 $d\omega=i\hbar\,dF_\nabla=0$；非退化性由「$(i/2\pi)F_\nabla$ 定义辛形式」这一假设保证。

> 为什么：比例系数 $\hbar$ 是人为标定，只需把曲率与 $\omega$ 的比例调成 $-i/\hbar$。

**第 3 步**：极化条件：$\omega$ 是 $(1,1)$ 型，故 $P=T^{0,1}M$ 是拉格朗日分布；$\nabla_{\bar\partial}f=0$ 就是 $\bar\partial$-闭，对 $(0,0)$ 形式的截面而言即全纯。

> 为什么：在复流形上，沿 $(0,1)$ 方向协变导数为零与截面局部全纯是同一件事。

**第 4 步**：写出希尔伯特空间 $\mathbb{H}=H^0(M,\mathcal{L})$，内积 $\langle s_1,s_2\rangle=\int_Mh(s_1,s_2)\,\omega^n/n!$；$M$ 紧且 $\omega$ 正定时高阶上同调消失，$\mathbb{H}$ 有限维。

> 为什么：正线丛的高阶上同调消没（Kodaira 消没定理）使全纯截面空间有限维。

**第 5 步**：在 $\mathbb{CP}^1$ 上具体化：$\mathcal{L}=\mathcal{O}(k)$，图卡 $U$ 用坐标 $z$，$V$ 用 $w=1/z$，转移函数 $w^k$。截面写成 $(f(z),g(w))$，重叠区相容要求 $f(z)w^k=g(w)$，即 $g(w)=w^kf(1/w)$。

> 为什么：转移函数把两个局部表示连起来，$g$ 在 $w=0$ 全纯等价于 $f(1/w)$ 的极点阶数不超过 $k$。

**第 6 步**：由第 5 步，$f$ 是次数不超过 $k$ 的多项式，故 $\dim H^0=k+1$。

> 为什么：次数不超过 $k$ 的多项式构成 $k+1$ 维空间，且每个单项式都给出独立的整体全纯截面。

## 结果

全纯线丛的凯勒极化给出全纯截面空间 $H^0(M,\mathcal{L})$，$M$ 紧时有限维；在 $\mathbb{CP}^1$ 上取 $\mathcal{L}=\mathcal{O}(k)$ 得 $\dim H^0=k+1$，即 $\mathfrak{su}(2)$ 自旋 $k/2$ 的不可约表示。

## 复核

(i) 整性：$U$ 上 $\omega=ik\hbar\frac{dz\wedge d\bar z}{(1+|z|^2)^2}$，而 $\int_{\mathbb{CP}^1}\frac{i\,dz\wedge d\bar z}{(1+|z|^2)^2}=2\pi$，故 $\int_{\mathbb{CP}^1}\omega=2\pi\hbar k$，陈数为整数 $k$ ✓。(ii) 特例：$k=0$ 时只有常数截面，$\dim H^0=1$；$k=1$ 时 $\dim H^0=2$ ✓。(iii) 代回转移关系 $g(w)=w^kf(1/w)$：$f(z)=z^k$ 得 $g(w)=1$，全纯；$f(z)=z^{k+1}$ 得 $g(w)=1/w$，有极点，被排除 ✓。

## 易错点

- 转移函数的方向：$z=1/w$ 下 $\mathcal{O}(k)$ 用 $w^k$ 而不是 $z^k$，写反会得到 $\mathcal{O}(-k)$ 与反全纯截面。
- $\hbar$ 与曲率的位置：$\omega=i\hbar F_\nabla$ 意味着 $\hbar$ 越大辛形式越大；若写成 $\omega=\frac{i}{\hbar}F_\nabla$，整性条件会变成另一套标定，结论不同。
- 非紧流形上不能断言有限维：$\mathbb{C}$ 上取平凡丛时全纯函数无穷多。有限维来自紧性加正性，不是全纯线丛的普遍性质。

## 用到哪些概念

- [极化：实极化与凯勒极化](../concepts/polarization.md)
- [可量子化条件（陈类整性）](../concepts/quantization-condition.md)

## 相关卡

- [$\mathbb{C}^n$ 的凯勒极化与全纯截面](../examples/kahler-polarization-cn.md)
- [线丛张量幂与 $\hbar$ 的重新标定](../examples/tensor-power-line-bundle.md)
- [$S^2$ 的可量子化条件 $A\in\frac{\hbar}{2}\mathbb{Z}$](../examples/s2-quantization-condition.md)

## 出处

- §5.4.4 例 5.4.10，p.290–291（PDF p.291–292），源码 `ch05b.tex:1164-1219`
