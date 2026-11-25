# 曲线算子

> `grassmann/concept/curve-operator` · 轨道 1 · Hitchin 联络与 TQFT · 状态 draft

> **先自测**：曲线算子为什么不能用「乘一个和乐函数」来理解，而必须看成配边给出的线性映射？

## 一句话

沿曲面内定向简单闭曲线切开、按标号缝合得到的 TQFT 算子；它是配边值，不是函数乘法算子。

## 定义

设 $\Sigma$ 是亏格 $g\ge2$ 的闭定向曲面，$p\in\Sigma$，$\lambda_0^{(d)}$ 是 $p$ 处的特殊标号；$\Lambda_k^{(n)}$ 为能级 $k$、秩 $n$ 的标号集。对 $\Sigma-\{p\}$ 中的定向简单闭曲线 $\gamma$ 与 $\lambda\in\Lambda_k^{(n)}$，**曲线算子**是线性映射 $$Z_k^{(n,d)}(\gamma,\lambda):Z_k^{(n)}(\Sigma,p,\lambda_0^{(d)})\to Z_k^{(n)}(\Sigma,p,\lambda_0^{(d)}),$$ 定义为配边 $\Sigma\times I$、链环 $\gamma\times\{\tfrac12\}\sqcup\{p\}\times I$ 与标号 $\{\lambda,\lambda_0^{(d)}\}$ 的 TQFT 值。

**记号约定**：$I=[0,1]$；$\gamma\times\{\tfrac12\}$ 悬在 $\Sigma\times I$ 内部，$\{p\}\times I$ 是竖直的边界链环。

## 要点（为什么需要它）

- 它是配边值：$\gamma\times\{\frac12\}$ 在 $\Sigma\times I$ 中间，算子由「切开—缝合」定义，而非乘以 $h_{\gamma,\lambda}$。
- 沿 $\gamma$ 取标号 $\lambda$、沿 $p\times I$ 取 $\lambda_0^{(d)}$，两个标号共同决定算子。
- 沿 $\gamma$ 切开得 $\Sigma'$，TQFT 公理给出 $Z(\gamma,\lambda)$ 在直和分解下对角，特征值为 $S_{\lambda,\mu}/S_{0,\mu}$。
- 定理 4：$k\to\infty$ 时 $Z_k(\gamma,\lambda)$ 收敛到 Toeplitz 算子 $T_{h_{\gamma,\lambda}}^{(k)}$。

## 关键公式

$$
Z_k^{(n,d)}(\gamma,\lambda)=Z_k^{(n,d)}\bigl(\Sigma\times I,\ \gamma\times\{\tfrac12\}\sqcup\{p\}\times I,\ \{\lambda,\lambda_0^{(d)}\}\bigr)
$$

$$
Z^{(k)}(\gamma,\lambda)=\bigoplus_{\mu}S_{\lambda,\mu}(S_{0,\mu})^{-1}\operatorname{Id}
$$

## 定理与证明（或缺口）

### 定理 4（Andersen）

对任意一维定向子流形 $\gamma$ 与任意标号 $\lambda$，$\lim_{k\to\infty}\|Z_k^{(n,d)}(\gamma,\lambda)-T_{h_{\gamma,\lambda}}^{(k)}\|=0$。

**证明状态：提纲（有缺口）**


> **缺口**：文中只给主要思想：用 Kac 13.8.9 的 $S$ 矩阵显式 $S_{\lambda,\mu}/S_{0,\mu}=\lambda(e^{-2\pi i(\check\mu+\check\rho)/(k+n)})$ 把特征值化为 Bohr–Sommerfeld 条件，再引 [A1] 的极限非负极化；逐项范数估计与 [A7] 的细节未写出。


出处：中译 p.11（§1 定理 4，证明思路见 152–158 行，细节在 [A7]）

## 易错点

- 把 $Z_k^{(n,d)}(\gamma,\lambda)$ 当成 $h_{\gamma,\lambda}$ 的乘法：两者只是渐近相等（定理 4），有限 $k$ 时曲线算子一般不与乘法交换。
- 把 77 行的 $Z^{(k)}(\gamma,\lambda)$ 当成另一个对象：译注 1 指出这是 $Z_k^{(n,d)}$ 的误印，波及 66、69、71、73、75、77 行。
- 只按 $\gamma$ 的标号 $\lambda$ 计算而漏掉 $\lambda_0^{(d)}$：沿 $p\times I$ 的标号决定算子作用在哪个直和分量上。

## 相关卡

- [沿曲线的因子化：SU(2) 能级 1 的维数核对](../examples/factorization-along-a-curve.md)
- [Toeplitz 算子](../concepts/toeplitz-operator.md)
- [因子分解性质](../concepts/factorization-property.md)

## 出处

- ch1 §1 曲线算子的定义；中译 p.8（英文 PDF p.11），源码 `chapters/ch01.tex:47`
