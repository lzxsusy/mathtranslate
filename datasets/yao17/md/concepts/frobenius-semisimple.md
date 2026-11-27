# φ-半单（Frobenius 半单）与引理 1.2

> `yao17/concept/frobenius-semisimple` · 轨道 Weil–Deligne 侧 · 状态 dev

> **先自测**：为什么「ρ 半单」可以换成「ρ(φ) 半单」来检验？这个等价用到了哪两条引理？

## 一句话

在 ρ(I_K) 有限时，ρ 半单 ⇔ 任一 Frobenius 提升的半单性；由此把「φ-半单」定为 LLC 目标范畴的条件。

## 定义

引理 1.1：(1) $H\triangleleft G$ 正规、$V$ 有限维，$\rho$ 半单 $\Rightarrow$ $\rho|_H$ 半单；(2) $[G:H]=r$ 在系数域中可逆时，$\rho$ 半单 $\iff$ $\rho|_H$ 半单。引理 1.2：设 $\rho(I_K)$ 有限、$L$ 代数闭，则 (1) 所有 $\rho(\sigma)$ 半单；(2) 任一 Frobenius 提升 $\rho(\phi)$ 半单；(3) $\rho$ 半单，三者等价。定义：$(\rho,N)\in\wd_K$ 称 $\phi$-半单（Frobenius 半单），若 $\rho$ 半单（等价地 $\rho(\phi)$ 半单）。

**记号**：$\rho^{\mathrm{ss}}$ 是 $\rho$ 的半单化；$(\rho^{\mathrm{ss}},N)$ 称 $(\rho,N)$ 的 $\phi$-半单化。

## 要点（为什么需要它）

1. 引理 1.2 的关键一步是：$\operatorname{im}\rho(I_K)$ 有限，故对每个 $\sigma$ 存在 $m>0$ 使 $\rho(\sigma^m)$ 落在 $\rho(W_K)$ 的中心——于是 $\rho(\sigma^{n'})=\rho(\phi^n)$，把问题归到 $\rho(\phi)$ 上。
2. 「$T^{m}$ 半单 ⇔ $T$ 半单」只在特征 0 成立，底本特意点明：这正是引理要求 $\operatorname{char}L=0$ 的原因，正特征下会失败。
3. 第二半用引理 1.1(2)：$\langle\rho(\phi)\rangle$ 在 $\rho(W_K)$ 中有限指数，指数在特征 0 中可逆，故 $\rho(W_K)$ 半单 ⇔ $\langle\rho(\phi)\rangle$ 半单。
4. 底本 Remark：$L$ 不必代数闭，此时把 (3) 换成「潜在半单」（换基后可对角化）；这也是为什么定义里写「$\rho$ 半单」而实际检验用 $\rho(\phi)$。
5. 注记 (1)：$\rho$ 不可约 $\Rightarrow N=0$（$\ker N$ 在 $W_K$ 下稳定）；注记 (2)：$\phi$-半单的对象一般不是 $\wd$ 的半单对象。

## 核心公式

$$
$\rho\ \text{半单}\iff \rho(\phi)\ \text{半单}\iff \rho(\sigma)\ \text{半单}\ \forall\sigma\in W_K$$\rho|_H\ \text{半单}\ \Longleftarrow\ \rho\ \text{半单}\quad(H\triangleleft G)$$\rho(\sigma^{n'})=\rho(\phi^{n})\quad(\text{用 }\operatorname{im}\rho(I_K)\text{ 有限})$
$$

$$
$\rho|_H\ \text{半单}\ \Longleftarrow\ \rho\ \text{半单}\quad(H\triangleleft G)$
$$

$$
$\rho(\sigma^{n'})=\rho(\phi^{n})\quad(\text{用 }\operatorname{im}\rho(I_K)\text{ 有限})$
$$

## 定理与证明（或缺口）

### 引理 1.2（φ-半单的三等价）

$\rho(I_K)$ 有限、$L$ 代数闭时，$\{\rho(\sigma)\}_{\sigma}$ 全半单、$\rho(\phi)$ 半单、$\rho$ 半单三者等价。

> 证明状态：**sketch**。底本只给 Sketch：先证每个 $\sigma$ 的某次幂落在中心（用 $\rho(I_K)$ 有限），再归到 $\rho(\phi)$，最后用引理 1.1(2)；「$T^m$ 半单 ⇔ $T$ 半单」的论证也略。

出处：`A §1.1.6 p.4–p.5`

## 常见误解

- 引理 1.2 要求 $L$ 代数闭；不代数闭时 (3) 要改成「潜在半单」，否则反例来自不可对角化的不可约 $L$-表示。
- $\phi$-半单时 $N$ 可以非零（$\Sp_m(r)$ 就是），所以「$\phi$-半单」不是「$N=0$」；两个条件在定理 2.13 的说法里分别由「Frobenius 半单」与「$N=0$」承担。

## 相关卡

[Weil–Deligne 表示 (ρ, N) 及其基本性质](../concepts/wd-representation.md) · [Grothendieck 单值化定理、WD 函子与惯性类型](../concepts/wd-functor.md) · [局部 Langlands 对应：定理 2.13 的五条性质](../concepts/llc-statement.md)

## 出处（印刷页）

- A p.4–5（A p.5）

> 说明：引理 1.1/1.2 与 $\phi$-半单的定义照 p.4–p.5；「为什么要求特征 0」与中心化论证的要点见 p.4 的 Sketch，解释部分是我们的判断。
