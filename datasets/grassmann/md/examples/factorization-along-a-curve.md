# 沿曲线的因子化：SU(2) 能级 1 的维数核对

> `grassmann/example/factorization-along-a-curve` · 轨道 1 · Hitchin 联络与 TQFT · 状态 draft

> **这张卡练什么**：沿非分离曲线切开后，因子化公式两边的维数为什么恰好相等，曲线算子的特征值又如何读出？

## 一句话

沿亏格 2 曲面的非分离闭曲线切开，用 SU(2) 能级 1 的 S 矩阵核对因子化公式两边的维数与曲线算子特征值。

## 背景定义

沿 $\gamma$ 把 $\Sigma$ 切开，并把得到的两条边界分别粘成点 $p_+,p_-$，记所得曲面为 $\Sigma'$。TQFT 公理断言 $$Z_k^{(n)}(\Sigma,p,\lambda_0^{(d)})\cong\bigoplus_{\mu\in\Lambda_k^{(n)}}Z^{(k)}(\Sigma',p_+,p_-,p,\mu,\mu^\dagger,\lambda_0^{(d)}),$$ 称为沿 $\gamma$ 的**因子化**；右端每一项对应沿 $\gamma$ 的一个边界标号 $\mu$。

## 设定

取 $\Sigma$ 为亏格 $2$ 的闭曲面，$\gamma\subset\Sigma-\{p\}$ 为非分离简单闭曲线。沿 $\gamma$ 切开并把两条边界分别粘成点 $p_+,p_-$，得 $\Sigma'$：亏格 $1$、带两个标记点 $p_\pm$ 的曲面。取 $n=2$、$k=1$、$d=0$，$\lambda_0$ 为真空标号，此时标号集为 $\{0,\tfrac12\}$。

## 计算

$SU(2)_1$ 的 $S$ 矩阵为 $S=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$。因子化公式给 $$Z_1(\Sigma,p,\lambda_0)\cong\bigoplus_{\mu}Z(\Sigma',p_+,p_-,\mu,\mu^\dagger).$$ 左端维数 $=\sum_\mu S_{0\mu}^{-2}=2\cdot(\tfrac1{\sqrt2})^{-2}=4$。右端 $\mu=0$ 扇区维数 $=\sum_\nu S_{0\nu}^2/S_{0\nu}^2=2$，$\mu=\tfrac12$ 扇区 $=\sum_\nu(S_{\frac12\nu}/S_{0\nu})^2=1+1=2$，合计 $4$，与左端吻合。曲线算子在每个扇区是标量 $S_{\lambda\mu}/S_{0\mu}$：$\lambda=\tfrac12$ 时特征值为 $+1$（$\mu=0$）与 $-1$（$\mu=\tfrac12$），故 $Z(\gamma)^2=\operatorname{Id}$、$\operatorname{tr}Z(\gamma)=2-2=0$。

## 要点

- 切开—粘合把 $Z(\Sigma)$ 写成两个扇区的直和，扇区标号 $\mu$ 就是沿 $\gamma$ 的边界条件。
- $\Sigma'$ 的亏格是 $g-1$ 而不是 $g$：非分离切口把亏格降一，同时留下两个标记点 $p_\pm$。
- 曲线算子在每个扇区是标量 $S_{\lambda\mu}/S_{0\mu}$，这是 TQFT 公理的直接推论。
- 维数核对同时验证了 $S$ 矩阵的正交归一与因子化公式的归一化。

## 关键公式

$$
Z_1(\Sigma)\cong\bigoplus_{\mu}Z(\Sigma',\mu,\mu^\dagger)
$$

$$
S=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad \sum_\mu S_{0\mu}^{-2}=4
$$

## 相关定理

- **沿曲线的因子化（式 (3)）**：沿非分离简单闭曲线 $\gamma$ 切开 $\Sigma$ 得 $\Sigma'$，则 $Z_k^{(n)}(\Sigma,p,\lambda_0^{(d)})\cong\bigoplus_{\mu\in\Lambda_k^{(n)}}Z^{(k)}(\Sigma',p_+,p_-,p,\mu,\mu^\dagger,\lambda_0^{(d)})$。

## 易错点

- 把 $\Sigma'$ 的亏格记成 $g$ 或忘掉两个标记点：$\Sigma'$ 是带 $p_\pm$ 的亏格 $g-1$ 曲面，标记点参与共形块。
- 把特征值写成 $S_{\lambda\mu}S_{0\mu}$：正确是商 $S_{\lambda\mu}/S_{0\mu}$，分母来自真空传播子。
- 在 $SU(2)_1$ 中把 $\mu=1$ 也算进来：能级 $1$ 只有 $\mu=0,\tfrac12$ 两个标号。

## 用到哪些概念

- [曲线算子](../concepts/curve-operator.md)
- [Verlinde 丛](../concepts/verlinde-bundle.md)

## 相关卡

- [曲线算子](../concepts/curve-operator.md)
- [Verlinde 丛](../concepts/verlinde-bundle.md)
- [因子分解性质](../concepts/factorization-property.md)

## 出处

- ch1 §1 式 (3) 因子化；中译 p.9（英文 PDF p.12），源码 `chapters/ch01.tex:66`
