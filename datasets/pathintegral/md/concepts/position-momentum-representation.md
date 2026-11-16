# 位置与动量表示（连续谱基）

> `pi/concept/position-momentum-representation` · 轨道 A · 基础与时间切片 · 状态 draft

> **先自测**：连续谱本征态不可归一，凭什么还能当基用，两种表示之间又靠什么相连？

## 一句话

把连续谱的位置、动量本征向量当形式基使用：δ 归一、完备性、平面波核，以及两套系数之间的傅里叶变换。

## 定义

位置算子 $\hat{\mathbf{x}}$ 的谱是连续的，本征向量 $|\mathbf{x}'\rangle$ 不平方可积，只能按 $\langle\mathbf{x}''|\mathbf{x}'\rangle=\delta(\mathbf{x}''-\mathbf{x}')$ 作广义归一。用它展开任意态，$|\psi\rangle=\int d^n\mathbf{x}\,\psi(\mathbf{x})|\mathbf{x}\rangle$，系数 $\psi(\mathbf{x})$ 即坐标波函数。动量本征向量取归一 $\langle\mathbf{p}''|\mathbf{p}'\rangle=(2\pi\hbar)^n\delta(\mathbf{p}''-\mathbf{p}')$，两组广义基通过平面波 $\langle\mathbf{x}|\mathbf{p}\rangle=e^{i\mathbf{x}\cdot\mathbf{p}/\hbar}$ 互化，展开系数因此互为傅里叶变换。

**记号约定**：$n$ 为空间维数，$\mathbf{x},\mathbf{p}\in\mathbb{R}^n$；$|\mathbf{x}\rangle,|\mathbf{p}\rangle$ 为广义本征向量；$\hbar$ 为约化普朗克常数。

## 要点

- 位置谱连续，本征向量只有 δ 型内积，范数无界，故只能当形式基，不能作希尔伯特空间中的向量。
- 完备性 $\int d^n\mathbf{x}\,|\mathbf{x}\rangle\langle\mathbf{x}|=1$ 与 $\frac{1}{(2\pi\hbar)^n}\int d^n\mathbf{p}\,|\mathbf{p}\rangle\langle\mathbf{p}|=1$ 是两套展开的共同支点。
- $\langle\mathbf{x}|\mathbf{p}\rangle=e^{i\mathbf{x}\cdot\mathbf{p}/\hbar}$ 就是平面波；取复共轭得 $\langle\mathbf{p}|\mathbf{x}\rangle=e^{-i\mathbf{x}\cdot\mathbf{p}/\hbar}$。
- 坐标波函数与动量波函数互为（差一个常数因子的）傅里叶变换，常数随归一约定走。
- 位置算子在坐标表象中是乘法，动量算子则实现为微分算子：$\langle\mathbf{x}|\hat{\mathbf{p}}|\psi\rangle=-i\hbar\partial_{\mathbf{x}}\psi(\mathbf{x})$。

## 关键公式

$$
\langle\mathbf{x}''|\mathbf{x}'\rangle=\delta(\mathbf{x}''-\mathbf{x}')
$$

$$
\langle\mathbf{p}''|\mathbf{p}'\rangle=(2\pi\hbar)^n\delta(\mathbf{p}''-\mathbf{p}')
$$

$$
\langle\mathbf{x}|\mathbf{p}\rangle=e^{i\mathbf{x}\cdot\mathbf{p}/\hbar}
$$

$$
\psi(\mathbf{x})=\frac{1}{(2\pi\hbar)^n}\int d^n\mathbf{p}\,e^{i\mathbf{x}\cdot\mathbf{p}/\hbar}\,\hat\psi(\mathbf{p})
$$

$$
\hat\psi(\mathbf{p})=\int d^n\mathbf{x}\,e^{-i\mathbf{x}\cdot\mathbf{p}/\hbar}\,\psi(\mathbf{x})
$$

## 定理与证明

### 位置基的完备性与波函数

$\int d^n\mathbf{x}\,|\mathbf{x}\rangle\langle\mathbf{x}|=1$；且对任意 $|\psi\rangle\in L^2(\mathbb{R}^n)$，有 $\psi(\mathbf{x})=\langle\mathbf{x}|\psi\rangle$，即波函数是态在位置基下的展开系数。

**完整证明**

1. 对任意 $|\chi\rangle,|\varphi\rangle$，按 $\psi_\chi(\mathbf{x})=\langle\mathbf{x}|\chi\rangle$ 的定义计算矩阵元：$\langle\chi|\left(\int d^n\mathbf{x}\,|\mathbf{x}\rangle\langle\mathbf{x}|\right)|\varphi\rangle=\int d^n\mathbf{x}\,\chi^*(\mathbf{x})\varphi(\mathbf{x})$。
   - *为什么*：把算子夹在两个任意态之间，位置基的矩阵元就是波函数乘积，不需要预先假设展开式。
2. 右端正是 $L^2$ 内积 $\langle\chi|\varphi\rangle$，故该算子与恒等算子有相同的全部矩阵元。
   - *为什么*：这是内积的定义，且对任意 $|\chi\rangle,|\varphi\rangle$ 都成立。
3. 内积非退化，矩阵元全部相同即算子相等，故 $\int d^n\mathbf{x}\,|\mathbf{x}\rangle\langle\mathbf{x}|=1$；展开式 $\psi(\mathbf{x})=\langle\mathbf{x}|\psi\rangle$ 是它的直接推论。
   - *为什么*：先证算子等式、再读矩阵元，避免了「用展开式证完备性」的循环。

来源：ch02a.tex:101-140（原书 p.82–83）

### 两种表示的傅里叶互化

设 $\hat\psi(\mathbf{p})=\langle\mathbf{p}|\psi\rangle$，则 $\psi(\mathbf{x})=\frac{1}{(2\pi\hbar)^n}\int d^n\mathbf{p}\,e^{i\mathbf{x}\cdot\mathbf{p}/\hbar}\hat\psi(\mathbf{p})$，且反向有 $\hat\psi(\mathbf{p})=\int d^n\mathbf{x}\,e^{-i\mathbf{x}\cdot\mathbf{p}/\hbar}\psi(\mathbf{x})$。

**完整证明**

1. 在 $\langle\mathbf{x}|\psi\rangle$ 中间插入 $\frac{1}{(2\pi\hbar)^n}\int d^n\mathbf{p}\,|\mathbf{p}\rangle\langle\mathbf{p}|$。
   - *为什么*：插入恒等算子不改变矩阵元，却把计算转到 $\hat{\mathbf{p}}$ 对角化的基上。
2. 用 $\langle\mathbf{x}|\mathbf{p}\rangle=e^{i\mathbf{x}\cdot\mathbf{p}/\hbar}$ 替换内积，得正变换式。
   - *为什么*：两基之间的变换核恰是平面波，这一步就是傅里叶核。
3. 反向在 $\langle\mathbf{p}|\psi\rangle$ 中插入位置完备性，用 $\langle\mathbf{p}|\mathbf{x}\rangle=e^{-i\mathbf{x}\cdot\mathbf{p}/\hbar}$，得逆变换。
   - *为什么*：复共轭把指数符号翻过来，两个方向互为逆变换。

来源：ch02a.tex:154-189（原书 p.83–84）

## 易错点

- δ 归一的态不能做范数估计：$\langle\mathbf{x}|\mathbf{x}\rangle$ 无界，把它当普通向量会得出无穷大的概率。
- 归一常数必须配套：书中用 $\langle\mathbf{x}|\mathbf{p}\rangle=e^{i\mathbf{x}\cdot\mathbf{p}/\hbar}$ 配 $\langle\mathbf{p}|\mathbf{p}'\rangle=(2\pi\hbar)^n\delta(\mathbf{p}-\mathbf{p}')$；若改用一维的 $\langle\mathbf{x}|p\rangle=e^{ipx/\hbar}/\sqrt{2\pi\hbar}$，则须配 $\langle p|p'\rangle=\delta(p-p')$，两套混用会差常数。
- 逆变换的指数符号容易写反：正变换带 $e^{-i\mathbf{x}\cdot\mathbf{p}/\hbar}$，把两个方向调换而不改符号会得到恒等式的错版本。
- 完备性中的「1」是恒等算子而非数字，省略积分测度后不能直接当作数值等式运算。

## 相关卡

- [费曼核与传播子](../concepts/feynman-kernel.md)
- [自由粒子的精确核 $K_0$](../concepts/free-particle-kernel.md)
- [时间切片与复合律](../concepts/time-slicing.md)

## 出处

- §2.1.2 位置与动量表示，p.82–84（PDF p.83–85），源码 `ch02a.tex:86-222`
