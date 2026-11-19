# 特选截面

> `gtgl15/concept/distinguished-section` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：为什么每个特征多项式都能被一个统一的、由典范丛搭出来的希格斯丛实现？

## 一句话

特选截面 $\zeta:\mathcal V\to\MH$ 在每个 Hitchin 纤维里挑一个“标准”稳定希格斯丛（opers 的版本），$SU(2)$ 时 $\varphi$ 写成 companion 矩阵。

## 定义

对 $SU(2)$：取 $E=K^{1/2}\oplus K^{-1/2}$，$\varphi=\bigl(\begin{smallmatrix}0&w/2\\1&0\end{smallmatrix}\bigr)$，则 $\operatorname{Tr}\varphi^2=w$；$u\ne0$ 时可规范化为 $u=1,v=0$，每个纤维（模 $K^{1/2}$ 的选择）恰有一个这样的稳定对，故得截面 eq (2.46)。$SU(N)$：$E=\bigoplus_i K^{(N+1)/2-i}$，$\varphi$ 是 companion 矩阵（下对角线全为 1，首行是 $w_n/n$），$\operatorname{Tr}\varphi^n=w_n$（eq (2.50)）。一般 $G$：用 Kostant 的主 $SU(2)$ 嵌入，$\varphi$ 的像是主幂零元；这正是 opers [12] 的构造。对 adjoint 型（如 $E_8$），Kostant 像落在 $SO(3)$ 里，截面是真正典范的。

**记号**：$\zeta$；$K^{1/2}$；$w_n$；Kostant 主 $SU(2)$ 嵌入；opers。

## 要点（为什么需要它）

1. 截面把 $\mathcal V$（底）嵌回 $\MH$：每个特征多项式都有标准实现。
2. $SU(2)$ 与 $SU(N)$ 的显式构造是 companion 矩阵；这也是 Higgs 丛的“正则幂零”特例。
3. “nearly canonical”：$K^{1/2}$ 的选择（spin 结构）会影响 $E=\bigoplus K^{1/2-i}$ 的整数幂指标。
4. 对 adjoint 型群，Kostant 像落在 $SO(3)$ 而非整个 $G$，截面不依赖额外选择，是真正典范的。
5. 特选截面是 §5、§7 中希格斯场取特殊值时的参照点；也用于构造 't Hooft 算符的赫克修正。

## 核心公式

$$
$$\zeta:\mathcal V\to\MH,\qquad \varphi_\zeta=\begin{pmatrix}0&w/2\\1&0\end{pmatrix}\ \ (SU(2))$$$$\operatorname{Tr}\varphi_\zeta^n=w_n,\qquad E_\zeta=\bigoplus_{i=1}^{N}K^{(N+1)/2-i}$$
$$

$$
$$\operatorname{Tr}\varphi_\zeta^n=w_n,\qquad E_\zeta=\bigoplus_{i=1}^{N}K^{(N+1)/2-i}$$
$$

## 定理与证明（或缺口）

### 特选截面的存在性

$\zeta$ 是良定义的代数截面，在 $K^{1/2}$ 的两种选择下差一个平坦 2-阶线丛。

> 证明状态：**sketch**。唯一性与 opers 的对应原文引用 [12]，未给完整证明。

出处：`A p.20`

## 常见误解

- $E=K^{1/2}\oplus K^{-1/2}$ 本身不稳定（次数不对称），稳定的是希格斯对，不是底向量丛。
- 截面的“唯一性”只到 $K^{1/2}$ 的选取：两种 spin 结构给出差一个 2-阶线丛的截面。
- $SU(N)$ 的 companion 矩阵首行是 $w_n/n$ 不是 $w_n$，系数别丢。
- 对非 adjoint 型群（$SU(N)$ 等）截面不是完全典范的，因为它依赖 $K^{1/2}$；不要把它当作与对偶无关的基点。

## 相关卡

[希钦纤维化](../concepts/hitchin-fibration.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [谱覆盖、判别式与分歧除子](../concepts/spectral-cover.md) · [$\mathbf F$ 型膜](../concepts/type-f-brane.md) · ['t Hooft flux 与 $PSU(N)$ 分量](../concepts/thooft-flux-psu.md)

## 出处（印刷页）

- A p.20–22（A p.20 eq (2.45)）
- A p.22（A p.22）
- C p.59–126（C p.59）

> 说明：A=原文 $\S2.7$ 的 $SU(2)$/ $SU(N)$ 显式构造（eq (2.44)–(2.50)）与一般 $G$ 的 Kostant 嵌入；B=把“唯一性”与稳定性整理成两步；C=opers 的背景按 Hitchin 1987 补。最没把握处：$K^{1/2}$ 的奇偶讨论原文在 $\S2.6.3$、$\S3.2$ 分散出现。
