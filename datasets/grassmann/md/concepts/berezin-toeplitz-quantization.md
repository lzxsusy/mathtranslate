# Berezin–Toeplitz 形变量子化

> `grassmann/concept/berezin-toeplitz-quantization` · 轨道 1 · Hitchin 联络与 TQFT · 状态 draft

> **先自测**：为什么 Toeplitz 算子乘积的渐近展开能定义一个结合且满足对应原理的星积？

## 一句话

紧 Kähler 流形上以 Toeplitz 算子乘积的渐近展开定义的形变量子化，其系数是双微分算子，一阶项给出 Poisson 括号。

## 定义

设 $(M_\sigma,\omega)$ 是紧 Kähler 流形，$\mathcal{L}$ 为其预量子化线丛，$\pi_\sigma^{(k)}$ 是到 $H^0(M_\sigma,\mathcal{L}_\sigma^k)$ 的 $L^2$ 正交投影，$T_f^{(k)}=\pi_\sigma^{(k)}\circ(f\cdot)$。Schlichenmaier 展开说存在双微分算子 $c_\sigma^{(l)}$ 使 $$T_{f_1}^{(k)}T_{f_2}^{(k)}\sim\sum_{l\ge0}T_{c_\sigma^{(l)}(f_1,f_2)}^{(k)}k^{-l}.$$ 把 $k^{-1}$ 换成形式参数 $h$，定义 $$f\star_\sigma^{\mathrm{BT}}g=\sum_{l\ge0}c_\sigma^{(l)}(f,g)h^l,$$ 称 $\star_\sigma^{\mathrm{BT}}$ 为 $(M_\sigma,\omega)$ 的 **Berezin–Toeplitz 形变量子化**。

**记号约定**：$h$ 是与能级倒数 $k^{-1}$ 对应的形式参数；$c_\sigma^{(0)}(f,g)=fg$，$c_\sigma^{(1)}(f,g)-c_\sigma^{(1)}(g,f)=-i\{f,g\}$。

## 要点（为什么需要它）

- $c_\sigma^{(0)}=fg$ 保证一阶退化就是普通乘法，故常数函数 $1$ 是单位。
- 一阶反对称部分给出 Poisson 括号 $\{f,g\}$，这正是「形变量子化」的对应原理。
- 各 $c_\sigma^{(l)}$ 都是双微分算子，所以 $\star_\sigma^{\mathrm{BT}}$ 是**微分**形变量子化，而非一般的形式星积。
- 把 $k^{-1}$ 换成 $h$ 不是数值代入：Toeplitz 展开用 $k^{-1}$，而定理 6、7 的误差用 $(k+n/2)^{-1}$，两者差标号平移 $\phi(h)=2h/(2+nh)$。

## 关键公式

$$
f\star_\sigma^{\mathrm{BT}}g=\sum_{l\ge0}c_\sigma^{(l)}(f,g)h^l
$$

$$
c_\sigma^{(0)}(f,g)=fg,\qquad c_\sigma^{(1)}(f,g)-c_\sigma^{(1)}(g,f)=-i\{f,g\}
$$

## 定理与证明（或缺口）

### 定理 11（Karabegov–Schlichenmaier）

由 $f\star_\sigma^{\mathrm{BT}}g=\sum_lc_\sigma^{(l)}(f,g)h^l$ 定义的乘积是 $(M,\omega)$ 的一个微分形变量子化：它结合、以 $1$ 为单位，且一阶项满足上述对应原理。

**证明状态：只引出处，原书不重证**


出处：中译 p.21（§3 定理 11，引 Karabegov–Schlichenmaier）

## 易错点

- 把 $\star_\sigma^{\mathrm{BT}}$ 当作与 Kähler 结构无关：系数 $c_\sigma^{(l)}$ 依赖 $\sigma$；只有经形式平凡化共轭得到的 $\star=P^{-1}(P\star^{\mathrm{BT}}P)$ 才与 $\sigma$ 无关（命题 2）。
- 把 $k^{-1}$ 直接当 $h$ 代入定理 6：那里展开参数是 $(k+n/2)^{-1}$，直接代换会漏掉 $\tilde c^{(2)}=c^{(2)}+\frac n2c^{(1)}$ 一类的标号修正。

## 相关卡

- [Toeplitz 算子](../concepts/toeplitz-operator.md)
- [形式 Hitchin 联络](../concepts/formal-hitchin-connection.md)
- [抛物丛与抛物次数](../concepts/parabolic-bundle.md)

## 出处

- ch1 §3 Berezin–Toeplitz 形变量子化；中译 p.21（英文 PDF p.24），源码 `chapters/ch01.tex:641`
