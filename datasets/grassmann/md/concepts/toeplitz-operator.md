# Toeplitz 算子

> `grassmann/concept/toeplitz-operator` · 轨道 1 · Hitchin 联络与 TQFT · 状态 draft

> **先自测**：为什么「乘 f 再投影」得到的 Toeplitz 算子，其乘积展开能编码 Kähler 流形的全部变形信息？

## 一句话

把函数乘上截面再投影回全纯截面所得的算子；其乘积的渐近展开定义了 Berezin–Toeplitz 星积。

## 定义

设 $(M_\sigma,\omega)$ 紧 Kähler，$\mathcal{L}$ 预量子化线丛，$\pi_\sigma^{(k)}:C^\infty(M,\mathcal{L}^k)\to H^0(M_\sigma,\mathcal{L}_\sigma^k)$ 是 $L^2$ 正交投影。对 $f\in C^\infty(M)$ 定义 $$T_{f,\sigma}^{(k)}:H^0(M_\sigma,\mathcal{L}_\sigma^k)\to H^0(M_\sigma,\mathcal{L}_\sigma^k),\qquad T_{f,\sigma}^{(k)}(s)=\pi_\sigma^{(k)}(fs),$$ 称 $T_{f,\sigma}^{(k)}$ 为 $f$ 的 **Toeplitz 算子**。

**记号约定**：$(s_1,s_2)=\int_M\langle s_1,s_2\rangle\frac{\omega^n}{n!}$ 是 $L^2$ 内积；$\pi^{(k)}$ 关于它对第二变量共轭线性。

## 要点（为什么需要它）

- $T_f^{(k)}$ 是 $\operatorname{Hom}(\mathcal{H}^{(k)},\mathcal{H}^{(k)})$ 的光滑截面，并限制为 $\operatorname{End}(H^{(k)})$ 的截面。
- 它不是乘法算子：先乘 $f$ 再投影，故 $T_fT_g\ne T_{fg}$，只在首项 $c^{(0)}=fg$ 上一致。
- 式 (14)–(17) 把 $\pi^{(k)}\nabla_X$ 与 $T_{\delta(X)}$ 联系起来，是全部渐近计算的引擎。
- 定理 10：$T_{f_1}T_{f_2}\sim\sum_lT_{c^{(l)}(f_1,f_2)}k^{-l}$，$c^{(0)}=f_1f_2$，误差 $O(k^{-(L+1)})$。

## 关键公式

$$
T_{f,\sigma}^{(k)}(s)=\pi_\sigma^{(k)}(fs)
$$

$$
T_{f_1}^{(k)}T_{f_2}^{(k)}\sim\sum_{l=0}^{L}T_{c^{(l)}(f_1,f_2)}^{(k)}k^{-l}+O(k^{-(L+1)})
$$

## 定理与证明（或缺口）

### 定理 10（Schlichenmaier）

对任意 $f_1,f_2\in C^\infty(M)$ 与任意 $L$，$T_{f_1,\sigma}^{(k)}T_{f_2,\sigma}^{(k)}=\sum_{l=0}^{L}T_{c_\sigma^{(l)}(f_1,f_2)}^{(k)}k^{-l}+O(k^{-(L+1)})$，其中 $c_\sigma^{(l)}$ 是双微分算子，$c^{(0)}=f_1f_2$。

**证明状态：只引出处，原书不重证**


出处：中译 p.20（§3 定理 10，引 Schlichenmaier）

## 易错点

- 把 $T_f^{(k)}$ 当成 $f$ 的乘法算子：它作用在 $H^0$ 上且带投影，忽略 $\pi$ 会把 $T_fT_g$ 误算成 $T_{fg}$。
- 对式 (16) 取共轭时把 $\nabla_X$ 写成 $\nabla_{\bar X}$：Hermite 内积对第二槽共轭线性，正确式子是 $(\nabla_X)^*=-\nabla_{\bar X}-\delta(\bar X)$。
- 用 (14) 直接复合 $\pi$ 推 (17)：应先对 $s\in H^0$ 用 $\nabla_{\bar X}s=0$，只剩 $-\delta(\bar X)s$，否则符号出错。

## 相关卡

- [Berezin–Toeplitz 形变量子化](../concepts/berezin-toeplitz-quantization.md)
- [曲线算子](../concepts/curve-operator.md)
- [抛物丛与抛物次数](../concepts/parabolic-bundle.md)

## 出处

- ch1 §3 Toeplitz 算子的定义；中译 p.19（英文 PDF p.22），源码 `chapters/ch01.tex:543`
