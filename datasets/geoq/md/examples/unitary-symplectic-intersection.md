# $\operatorname{Sp}(2n)\cap\operatorname{O}(2n)=\operatorname{U}(n)$ 的显式实现

> `geoq/example/unitary-symplectic-intersection` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：$\operatorname{Sp}(2n)\cap\operatorname{O}(2n)=\operatorname{U}(n)$ 能否写成一条具体的矩阵公式？

## 一句话

把 $A+iB$ 映为实分块矩阵 $\begin{pmatrix}A&-B\\B&A\end{pmatrix}$，它同时辛且正交，且这一对应是酉群与该交集之间的双射。

## 设定

取 $A,B\in M_n(\mathbb R)$，令 $\Phi=\begin{pmatrix}A&-B\\B&A\end{pmatrix}$，并把 $\mathbb C^n$ 与 $\mathbb R^{2n}$ 按 $z=x+iy\leftrightarrow(x,y)$ 等同，使 $A+iB$ 对应 $\Phi$。要证：$A+iB\in\operatorname{U}(n)$ 当且仅当 $\Phi\in\operatorname{Sp}(2n)\cap\operatorname{O}(2n)$，且对应是双射。

## 计算

**第 1 步**：展开酉性条件：$(A^T-iB^T)(A+iB)=(A^TA+B^TB)+i(A^TB-B^TA)=I_n$，故 $A^TA+B^TB=I_n$ 且 $A^TB=B^TA$。

> 为什么：复数相等即实部、虚部同时相等；注意 $(iB)^*=-iB^T$，共轭带来转置与负号。

**第 2 步**：先算 $\Phi^T\omega_n$：$\Phi^T=\begin{pmatrix}A^T&B^T\\-B^T&A^T\end{pmatrix}$，右乘 $\omega_n=\begin{pmatrix}0&I\\-I&0\end{pmatrix}$ 得 $\Phi^T\omega_n=\begin{pmatrix}-B^T&A^T\\-A^T&-B^T\end{pmatrix}$。

> 为什么：右乘 $\omega_n$ 交换两个列块并给其中一块添负号，逐块读即可。

**第 3 步**：再右乘 $\Phi$：$\Phi^T\omega_n\Phi=\begin{pmatrix}-B^TA+A^TB&-B^T(-B)+A^TA\\-A^TA-B^TB&-A^T(-B)-B^TA\end{pmatrix}=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}$，其中用了 $A^TB=B^TA$ 与 $A^TA+B^TB=I_n$。

> 为什么：左上、右下两个块正好是步骤 1 的反对称组合，右上、左下是 $A^TA+B^TB$ 及其负值。

**第 4 步**：再算 $\Phi^T\Phi=\begin{pmatrix}A^TA+B^TB&-A^TB+B^TA\\-B^TA+A^TB&B^TB+A^TA\end{pmatrix}=I_{2n}$。

> 为什么：四个块同样只用步骤 1 的两条关系：对角块是 $I_n$，交叉块为零。

**第 5 步**：反向设 $\Phi=\begin{pmatrix}A&B\\mathbb{C}&D\end{pmatrix}\in\operatorname{Sp}(2n)\cap\operatorname{O}(2n)$。由命题 5.1.7，$\Phi\in\operatorname{U}(V)$（关于 $J_0$），即 $\Phi J_0=J_0\Phi$。比较 $\Phi J_0=\begin{pmatrix}B&-A\\D&-C\end{pmatrix}$ 与 $J_0\Phi=\begin{pmatrix}-C&-D\\A&B\end{pmatrix}$ 得 $B=-C$、$D=A$，故 $\Phi$ 必为 $\begin{pmatrix}A&-B\\B&A\end{pmatrix}$。

> 为什么：$J_0$ 的分块结构把「与 $J_0$ 交换」翻译成四条块等式，其中两条非平凡，恰好给出块形。

**第 6 步**：此时 $\Phi^T\Phi=I_{2n}$ 的四个块就是步骤 1 的两条方程（$A^TA+B^TB=I_n$、$A^TB-B^TA=0$），即 $A+iB$ 酉。映射 $A+iB\mapsto\Phi$ 与其逆都显式，故为双射。

> 为什么：块形确定后正交条件只剩酉性；两个方向都写成了公式，故交集与酉群一一对应。

## 结果

$\operatorname{Sp}(2n)\cap\operatorname{O}(2n)=\left\{\begin{pmatrix}A&-B\\B&A\end{pmatrix}\ \middle|\ A+iB\in\operatorname{U}(n)\right\}\cong\operatorname{U}(n)$，维数 $n^2$ 与 $\dim\operatorname{U}(n)=n^2$ 相符。

## 复核

(i) $n=1$：$\Phi=\begin{pmatrix}a&-b\\b&a\end{pmatrix}$，$\det\Phi=a^2+b^2=|a+ib|^2$，故 $\Phi\in\operatorname{Sp}(2)\cap\operatorname{O}(2)\iff a^2+b^2=1\iff a+ib\in\operatorname{U}(1)$；(ii) 取 $n=2$、$A=\frac1{\sqrt2}I_2$、$B=\frac1{\sqrt2}I_2$，直接乘得 $\Phi^T\omega_4\Phi=\omega_4$ 与 $\Phi^T\Phi=I_4$；(iii) 数参数：$A,B$ 共 $2n^2$ 个实参数，酉性给 $n^2$ 个独立方程（$A^TA+B^TB=I_n$ 是 $\frac{n(n+1)}2$ 个对称方程，$A^TB-B^TA=0$ 是 $\frac{n(n-1)}2$ 个反对称方程），剩下 $n^2=\dim\operatorname{U}(n)$。

## 易错点

- 分块形状是 $\begin{pmatrix}A&-B\\B&A\end{pmatrix}$（左下 $B$、右上 $-B$）；写成 $\begin{pmatrix}A&B\\-B&A\end{pmatrix}$ 对应的是 $A-iB$，两者互为转置/共轭，不要混。
- 两个条件不可互相代替：$\Phi\in\operatorname{Sp}$ 验 $\Phi^T\omega_n\Phi=\omega_n$，$\Phi\in\operatorname{O}$ 验 $\Phi^T\Phi=I_{2n}$；只验一个不足以说明落在交集中。
- 公式依赖 $J_0$ 的选取（把复数 $i$ 送到 $J_0$）；若改用另一个相容复结构，同一个酉群会被共轭成另一组矩阵。

## 用到哪些概念

- [辛群 $\operatorname{Sp}(V)$](../concepts/symplectic-group.md)
- [相容复结构与可缩性](../concepts/compatible-complex-structure.md)

## 相关卡

- [标准辛基下的相容复结构](../examples/standard-compatible-complex-structure.md)
- [$n=1$ 时 $\operatorname{Sp}(2)=\operatorname{SL}(2)$](../examples/sp2-equals-sl2.md)

## 出处

- §5.1.1 例 5.1.8，p.253（PDF p.254），源码 `ch05a.tex:208-231`
