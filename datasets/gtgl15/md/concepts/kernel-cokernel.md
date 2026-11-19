# 核线丛与余核线丛

> `gtgl15/concept/kernel-cokernel` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：为什么本征值方程 $\varphi\psi=y\psi$ 的核与余核都是线丛，而它们的差别恰好是典范丛的幂？

## 一句话

沿谱覆盖，$\varphi-y$ 的核给出本征向量线丛 $\mathcal N$，余核给出线丛 $\mathcal L$；两者由 $\mathcal L\cong\mathcal N(\mathcal R)\cong\mathcal N\otimes\psi^*K^{N-1}$ 相联系。

## 定义

在 $D$ 上去掉分歧点后，$\varphi-y$ 的核是一维的，给出线丛 $\mathcal N$（本征向量）；把 $E$ 拉回到 $D$ 上，$\varphi-y$ 的余核是线丛 $\mathcal L$。局部模型（$2\times2$）为 $\varphi\sim\bigl(\begin{smallmatrix}0&z\\1&0\end{smallmatrix}\bigr)$、$y^2=z$，本征向量 $s=(y,1)$、余核生成元 $t=(1,0)$，且 $s=u+2yt$ 给出两者的过渡。由此得 $\mathcal L\cong\mathcal N(\mathcal R)\cong\mathcal N\otimes\psi^*K^{N-1}$。

**记号**：$\mathcal N$；$\mathcal L$；$\mathcal R$ 为分歧除子；$K$。

## 要点（为什么需要它）

1. $\mathcal N$ 是 $D$ 上本征向量的线丛：在非分歧点处 $E_p=\bigoplus_i\mathcal N_{q_i}$（$\S2.6.2$）。
2. $\mathcal L$ 是余核线丛；阿贝尔化用 $\mathcal L$ 重建 $E=\psi_*(\mathcal L)$，用 $\mathcal N$ 重建会错一个 twist。
3. $\mathcal L\cong\mathcal N(\mathcal R)$：核与余核的差别被分歧除子吸收。
4. 再把 $\mathcal R$ 与 $K$ 联系：$\mathcal L\cong\mathcal N\otimes\psi^*K^{N-1}$，这是计算次数的关键（$\S2.6.3$）。
5. 次数的计算给出 $c_0=N(N-1)(g-1)$，从而 $F_{SU(N)}=\Lambda^{-1}(\mathcal O)$。

## 核心公式

$$
$$\mathcal L\cong\mathcal N(\mathcal R)\cong\mathcal N\otimes\psi^*K^{N-1}$$$$E_p=\bigoplus_i\mathcal N_{q_i},\qquad E=\psi_*(\mathcal L)$$
$$

$$
$$E_p=\bigoplus_i\mathcal N_{q_i},\qquad E=\psi_*(\mathcal L)$$
$$

## 定理与证明（或缺口）

### 核与余核的关系

$\mathcal L\cong\mathcal N(\mathcal R)$，且进一步 $\mathcal L\cong\mathcal N\otimes\psi^*K^{N-1}$。

1. 在局部模型 $\varphi\sim\bigl(\begin{smallmatrix}0&z\\1&0\end{smallmatrix}\bigr)$ 中，$y^2=z$，本征向量 $s=(y,1)$ 与余核生成元 $t=(1,0)$ 满足 $s=u+2yt$。
   - *为什么*：这一步显式写出了过渡函数。
2. 局部过渡是乘以 $y^2$，即分歧除子 $\mathcal R$ 定义方程，故 $\mathcal L=\mathcal N(\mathcal R)$。
   - *为什么*：线丛的过渡函数相乘即得 twist。
3. $\mathcal R$ 的像与 $K^{N-1}$ 的除子类一致，故 $\mathcal N(\mathcal R)=\mathcal N\otimes\psi^*K^{N-1}$。
   - *为什么*：$\psi$ 的分歧除子类是 $\psi^*K^{N-1}$。

出处：`A p.13 eq (2.20)`

## 常见误解

- 核与余核不是同一个线丛：$\mathcal L\ne\mathcal N$，差一个分歧除子的 twist。
- $\mathcal N(\mathcal R)$ 里的 $\mathcal R$ 是 $D$ 上的分歧除子，不是 $C$ 上的判别式轨迹。
- 局部模型是 $2\times2$ 的，推广到 $N$ 时不能直接照抄过渡函数，要用行列式/典范丛论证。
- 次数条件 $c_0=N(N-1)(g-1)$ 是 $SU(N)$ 的，$U(N)$ 还要加 $c_1$ 项。

## 相关卡

[谱曲线](../concepts/spectral-curve.md) · [谱覆盖、判别式与分歧除子](../concepts/spectral-cover.md) · [阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · [稳定丛模空间与余切丛](../concepts/stable-locus.md) · [核与余核线丛的关系 $\mathcal L\cong\mathcal N(\mathcal R)$](../derivations/kernel-cokernel-relation.md)

## 出处（印刷页）

- A p.11–13（A p.13 eq (2.20)）
- A p.13（A p.13 eq (2.21)）
- A p.13–14（A p.13 eq (2.24)）

> 说明：A=原文 $\S2.6.1$ 的局部模型（eq (2.11)–(2.22)）与 $\S2.6.2$ 的阿贝尔化；B=把三步局部计算整理成证明；C=与 $K^{N-1}$ 的识别按 $\S2.6.3$ 的次数计算补全。最没把握处：$\mathcal R$ 与 $K^{N-1}$ 的除子类等式原文只给了结论式 (2.22)。
