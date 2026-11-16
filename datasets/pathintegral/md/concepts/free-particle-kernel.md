# 自由粒子的精确核 $K_0$

> `pi/concept/free-particle-kernel` · 轨道 A · 基础与时间切片 · 状态 draft

> **先自测**：自由粒子的传播子为什么能精确算出，指数上的相位对应哪一条经典轨道？

## 一句话

自由粒子的费曼核可在动量基下化为一个高斯积分；算出的相位正是匀速直线轨道的作用量，系数给出 $n$ 维归一化。

## 定义

自由粒子只有动能，$\hat H_0=\hat{\mathbf{p}}^2/(2m)$。其费曼核记作 $K_0(\mathbf{x}'',t'';\mathbf{x}',t')=\langle\mathbf{x}''|e^{-i\hat H_0T/\hbar}|\mathbf{x}'\rangle$，其中 $T=t''-t'>0$。由于 $\hat H_0$ 在动量基下对角，插入动量完备性后只剩下一个复高斯积分，结果是一个闭式：$\left(\frac{m}{2\pi\hbar iT}\right)^{n/2}\exp\left[\frac{im(\mathbf{x}''-\mathbf{x}')^2}{2\hbar T}\right]$。指数里的量等于两端点间匀速直线轨迹的经典作用量。

**记号约定**：$T=t''-t'$ 为演化时长；$m$ 为质量；$\Delta\mathbf{x}=\mathbf{x}''-\mathbf{x}'$；$n$ 为空间维数。

## 要点

- 先在动量基里算 $\langle\mathbf{p}|e^{-i\hat H_0t/\hbar}|\mathbf{x}\rangle=e^{-ip^2t/(2m\hbar)}e^{-i\mathbf{x}\cdot\mathbf{p}/\hbar}$，算符便化成了数。
- 插入动量完备性后，$\mathbf{p}$ 的积分是标准复高斯，配方给出 $\exp[im(\Delta\mathbf{x})^2/(2\hbar T)]$。
- 高斯公式 $\int du\,e^{-au^2+bu}=\sqrt{\pi/a}\,e^{b^2/(4a)}$ 中 $a=iT/(2m\hbar)$ 为纯虚数，须靠解析延拓取收敛分支。
- 系数 $(m/(2\pi\hbar iT))^{n/2}$ 含 $i$ 的相位，是保证 $T\to0$ 时核趋于 $\delta(\mathbf{x}''-\mathbf{x}')$ 的关键。
- 把 $K_0$ 当作自由粒子的「精确」结果：不含近似，故可作为切片法每一小段的构件。

## 关键公式

$$
K_0(\mathbf{x}'',t'';\mathbf{x}',t')=\langle\mathbf{x}''|e^{-i\hat H_0T/\hbar}|\mathbf{x}'\rangle
$$

$$
\langle\mathbf{p}|e^{-i\hat H_0t/\hbar}|\mathbf{x}\rangle=e^{-ip^2t/(2m\hbar)}\,e^{-i\mathbf{x}\cdot\mathbf{p}/\hbar}
$$

$$
\int du\,e^{-au^2+bu}=\sqrt{\frac{\pi}{a}}\,e^{b^2/(4a)}
$$

$$
K_0=\left(\frac{m}{2\pi\hbar iT}\right)^{n/2}\exp\left[\frac{im(\mathbf{x}''-\mathbf{x}')^2}{2\hbar T}\right]
$$

$$
S_{cl}=\frac{m}{2T}(\mathbf{x}''-\mathbf{x}')^2
$$

## 定理与证明

### 自由粒子核的闭式

对 $\hat H_0=\hat{\mathbf{p}}^2/(2m)$，费曼核为 $K_0=\left(\frac{m}{2\pi\hbar iT}\right)^{n/2}\exp\left[\frac{im|\mathbf{x}''-\mathbf{x}'|^2}{2\hbar T}\right]$，$T=t''-t'$。

**完整证明**

1. 在 $\langle\mathbf{x}''|e^{-i\hat H_0T/\hbar}|\mathbf{x}'\rangle$ 中插入 $\frac{1}{(2\pi\hbar)^n}\int d^n\mathbf{p}\,|\mathbf{p}\rangle\langle\mathbf{p}|$。
   - *为什么*：动量基下 $\hat H_0$ 对角，指数算子可直接作用。
2. 用 $\langle\mathbf{p}|\hat{\mathbf{p}}=\mathbf{p}\langle\mathbf{p}|$ 得 $\langle\mathbf{p}|e^{-i\hat H_0T/\hbar}|\mathbf{x}'\rangle=e^{-iTp^2/(2m\hbar)}e^{-i\mathbf{x}'\cdot\mathbf{p}/\hbar}$，再乘 $\langle\mathbf{x}''|\mathbf{p}\rangle$，合并成 $e^{-iTp^2/(2m\hbar)+i(\mathbf{x}''-\mathbf{x}')\cdot\mathbf{p}/\hbar}$。
   - *为什么*：两个平面波因子合成一个，指数上只剩 $\mathbf{p}$ 的二次式与一次式。
3. 逐分量作高斯积分：$a=iT/(2m\hbar)$，$b=i(\mathbf{x}''_i-\mathbf{x}'_i)/\hbar$，于是 $b^2/(4a)=im(\mathbf{x}''_i-\mathbf{x}'_i)^2/(2\hbar T)$。
   - *为什么*：各分量解耦，$n$ 个一维积分相乘；配方把一次项吸收进平方。
4. 每个分量贡献因子 $\sqrt{m/(2\pi\hbar iT)}$，$n$ 次方后连同指数合并即得闭式。
   - *为什么*：常数因子与相位指数分别相乘，得到与 $n$ 维形式一致的归一。

来源：ch02a.tex:231-268（原书 p.84–85）

## 易错点

- 高斯积分里的 $a$ 是纯虚数，直接套实轴 $a>0$ 的收敛论证不合法；应理解为解析延拓或带 $+i\epsilon$ 的极限，否则积分不收敛。
- 相位不是「动能」：$m(\Delta\mathbf{x})^2/(2T)$ 是作用量，量纲为能量乘时间，写成 $T$ 的一次方就会丢掉 $1/T$。
- $n$ 维因子是 $(m/(2\pi\hbar iT))^{n/2}$ 的 $n$ 次幂形式，漏掉 $i$ 或把 $n/2$ 写成 $1/2$ 会破坏与 δ 函数极限的相容性。
- $K_0$ 是分布而非普通函数：它在 $T\to0$ 时发散成 δ，不能直接谈它的逐点值或 $L^2$ 范数。

## 相关卡

- [位置与动量表示（连续谱基）](../concepts/position-momentum-representation.md)
- [时间切片与复合律](../concepts/time-slicing.md)
- [虚时间与欧氏路径积分](../concepts/imaginary-time.md)

## 出处

- §2.2.1 自由粒子，p.84–85（PDF p.85–86），源码 `ch02a.tex:225-287`
