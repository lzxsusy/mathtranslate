# Gerbe 与 $B$-场（离散电/磁荷）

> `gtgl15/concept/gerbe-bfield` · 轨道 E · 行列式线丛与本征值 · 状态 dev

> **先自测**：为什么离散电荷（$Z_N$ 之类的拓扑荷）必须用 gerbe 而不是普通线丛来描述？

## 一句话

Gerbe 是线丛的上一层对象（局部平凡、两个平凡化差一线丛）；中心非平凡的对偶理论在模空间上带非平凡 gerbe，其平坦 $B$-场编码离散电/磁荷。

## 定义

Gerbe 是局部平凡的对象，两个局部平凡化之间差一个线丛；其分类群可取 $\mathbb C^*$、$U(1)$ 或 $\mathbb Z_n$（$\S6.3$）。例：$C$ 上 spin 结构的 $Z_2$ gerbe（两个 spin 结构差 $2$-阶线丛）；$C\times\mathrm{Pic}_c(C)$ 上万有线丛给出 $\mathrm{Pic}_c(C)$ 上的 gerbe。非平凡例：${}^LG$ 中心含 $\mathbb Z_n$ 时，$\MH({}^LG,C)$ 上有非平凡 $\mathbb Z_n$ gerbe（局部万有丛可平凡化、全局不存在）。带 gerbe 的丛叫 twisted bundle；其连接是 2-形式 $B$，换平凡化 $B\to B+F$。平坦（flat）twisted 线丛要求 $H=dB=0$ 且 $B/2\pi$ 的周期为整数。

**记号**：gerbe；$B$（2-形式）；$H=dB$；$\mathbb Z_n$；twisted bundle；平坦化。

## 要点（为什么需要它）

1. Gerbe 是比线丛高一层的“-1 层”丛：局部平凡、平凡化之间差线丛。
2. $C$ 上 spin 结构的 $Z_2$ gerbe 是把两个 spin 结构粘起来的最小例子（$\S6.3$ 例 1）。
3. 当 ${}^LG$ 有中心 $\mathbb Z_n$ 时，其对偶模空间上带非平凡 gerbe，这是本文唯一的非平凡 gerbe 例（$\S6.3$ 例 3）。
4. 平坦 $B$-场（$H=dB=0$、周期整数）正是离散电/磁荷的几何编码，对应 KW06 §7 的离散 $\theta$ 角。
5. twisted line bundle 上可以定义平坦联络与 theta 函数，但整体不存在普通线丛版本。

## 核心公式

$$
$$H=dB,\qquad \text{flat}:\ H=0,\ \ \frac{1}{2\pi}\oint_\gamma B\in\mathbb Z$$$$\text{gerbe 类}\in H^2(M,\mathbb Z_n)\quad(\text{中心 } \mathbb Z_n\text{ 的对偶理论})$$
$$

$$
$$\text{gerbe 类}\in H^2(M,\mathbb Z_n)\quad(\text{中心 } \mathbb Z_n\text{ 的对偶理论})$$
$$

## 定理与证明（或缺口）

### 非平凡 gerbe 的出现

若 ${}^LG$ 的中心非平凡，则 $\MH({}^LG,C)$ 上存在非平凡的 $Z_n$ gerbe；它不能整体平凡化。

> 证明状态：**gap**。原文 $\S6.3$ 例 3 只陈述结论并引用 [1] §7，未给完整拓扑证明。

出处：`A p.64`

## 常见误解

- gerbe 不是“线丛的丛”：平凡化之间差线丛，所以它没有普通截面。
- $B$ 是 2-形式，不是 1-形式规范场；平直性条件是 $dB=0$ 且周期整数。
- 离散 B-场与连续 $\theta$ 角不是一回事：前者是 gerbe 的平坦类，后者是 $\tau$ 的实部。
- 中心非平凡时万有丛本身不存在（twisted 版本才存在），不要把它当普通丛。

## 相关卡

['t Hooft flux 与 $PSU(N)$ 分量](../concepts/thooft-flux-psu.md) · [行列式线丛与配对 $\langle\mathcal L,\mathcal M\rangle$](../concepts/determinant-line-pairing.md) · [万有丛、万有希格斯丛与陈–帕顿丛](../concepts/universal-bundles.md) · [对偶环面纤维化与 T-对偶](../concepts/dual-torus-fibration.md) · [磁本征膜的赫克本征值（$U(1)$ 与 $SU(N)$）](../derivations/magnetic-hecke-eigenvalue.md)

## 出处（印刷页）

- A p.62–64（A p.63）
- A p.64（A p.64）
- A p.19（A p.19 eq (2.42)）

> 说明：A=原文 $\S6.3$ 的 gerbe 定义与三个例子、$\S2.6.6$ 的 $PSU(N)$ 对偶 gerbe；B=把平坦 $B$-场与离散电/磁荷对应起来；C=“gerbe 类 ∈ $H^2(M,\mathbb Z_n)$”的表述按 $\S6.3$ 例 3 补。最没把握处：例 3 的拓扑证明原文只有引用。
