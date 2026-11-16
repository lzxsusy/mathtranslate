# $\mathbb R^2$ 上相容复结构的参数化

> `geoq/example/compatible-complex-structures-on-r2` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：$\omega_1$-相容复结构在平面上有多少个，它们构成的空间是什么形状？

## 一句话

在 $(\mathbb R^2,\omega_1)$ 上，相容复结构由一个自由参数与一个正参数刻画，整族同胚于可缩的上半平面。

## 设定

取 $V=\mathbb R^2$、$\omega_1=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$。设 $J=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ 是 $\omega_1$-相容复结构，即满足 $J^2=-I$、$J\in\operatorname{Sp}(2)$、且 $\omega_1(-,J-)$ 正定。

## 计算

**第 1 步**：由 $J\in\operatorname{Sp}(2)=\operatorname{SL}(2)$ 得 $\det J=1$；再由 $J^2=-I$ 与 Cayley–Hamilton 恒等式 $J^2-(\operatorname{tr}J)J+(\det J)I=0$ 得 $-I-(\operatorname{tr}J)J+I=0$，即 $(\operatorname{tr}J)J=0$，故 $\operatorname{tr}J=0$。

> 为什么：二阶矩阵满足自己的特征多项式；把 $J^2=-I$、$\det J=1$ 代进去，$J\neq0$ 迫使迹为零。

**第 2 步**：于是 $J=\begin{pmatrix}a&b\\c&-a\end{pmatrix}$，$\det J=-a^2-bc=1$，即 $bc=-1-a^2$。因 $b\neq0$（否则 $-a^2=1$ 无实解），可解出 $c=-(1+a^2)/b$。

> 为什么：迹零只给对角元反号，行列式给一条约束；$b=0$ 会与实数域冲突。

**第 3 步**：把参数改写成书上的形式：令 $b\mapsto-b$，得 $J=\begin{pmatrix}a&-b\\ \dfrac{1+a^2}{b}&-a\end{pmatrix}$，$a\in\mathbb R$、$b\neq0$。它的迹为零、行列式为 $1$，由 Cayley–Hamilton 即 $J^2=-I$。

> 为什么：只是换参数名，代数约束不变；迹零加行列式 $1$ 是 $J^2=-I$ 的等价条件。

**第 4 步**：算正定性：$\omega_1J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}a&-b\\ \frac{1+a^2}{b}&-a\end{pmatrix}=\begin{pmatrix}\frac{1+a^2}{b}&-a\\-a&b\end{pmatrix}=:G$，它对称；二阶对称矩阵正定当且仅当左上元为正且 $\det G>0$。

> 为什么：Sylvester 判据：顺序主子式全为正。这里 $\det G=\frac{1+a^2}{b}\cdot b-a^2=1$ 恒为正。

**第 5 步**：故正定 $\iff\frac{1+a^2}{b}>0\iff b>0$（因 $1+a^2>0$）。于是 $\mathcal J=\left\{\begin{pmatrix}a&-b\\ \frac{1+a^2}{b}&-a\end{pmatrix}\ \middle|\ a\in\mathbb R,\ b>0\right\}$，由 $(a,b)$ 唯一决定。

> 为什么：$1+a^2$ 恒正，符号完全由 $b$ 决定；参数与矩阵一一对应，故这是完整参数化。

## 结果

$\mathcal J\cong\mathbb R\times(0,\infty)$（上半平面），是二维可缩空间；每个 $J$ 的 $g_J$ 矩阵为 $\begin{pmatrix}\frac{1+a^2}{b}&-a\\-a&b\end{pmatrix}$，正定当且仅当 $b>0$。

## 复核

(i) 取 $a=0,b=1$ 得 $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=J_0$，与标准例子吻合；(ii) 取 $a=1,b=1$ 得 $J=\begin{pmatrix}1&-1\\2&-1\end{pmatrix}$，直接算 $J^2=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}$；(iii) 取 $b=-1$ 得 $J=-J_0$，$g_J=-I$ 负定，说明 $b>0$ 不可省；(iv) 维数 $2=n(n+1)$（$n=1$），与 $\dim\mathcal J=\dim\operatorname{Sp}(2)-\dim\operatorname{U}(1)=3-1=2$ 一致。

## 易错点

- $b>0$ 不能丢：$b<0$ 给出的矩阵仍满足 $J^2=-I$、仍保 $\omega_1$，只是 $g_J$ 负定，因此不相容。
- $J$ 与 $-J$ 都是复结构（对应相反的复结构），但只有一个是相容的；判断相容必须验正性，不能只看 $J^2=-I$。
- 参数化不唯一：把 $b$ 换成 $-b$ 与把 $a$ 换成某函数都能重写同一族，比较不同教材时先对齐 $g_J$ 的符号。

## 用到哪些概念

- [相容复结构与可缩性](../concepts/compatible-complex-structure.md)
- [辛群 $\operatorname{Sp}(V)$](../concepts/symplectic-group.md)

## 相关卡

- [标准辛基下的相容复结构](../examples/standard-compatible-complex-structure.md)
- [$\mathcal L(\mathbb R^2)=\mathbb{RP}^1$ 上的马斯洛夫指标](../examples/maslov-index-rp1.md)

## 出处

- §5.1.1 例 5.1.10，p.254（PDF p.255），源码 `ch05a.tex:280-295`
