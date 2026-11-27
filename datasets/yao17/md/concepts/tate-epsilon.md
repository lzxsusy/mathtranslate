# Tate 的局部 L 因子与 ε 因子、定理 1.3 的存在唯一性

> `yao17/concept/tate-epsilon` · 轨道 Weil–Deligne 侧 · 状态 dev

> **先自测**：Tate 的 ε 因子显式公式长什么样？定理 1.3 用哪三条公理把特征标情形唯一地延拓到高维表示？

## 一句话

Tate 对拟特征标给出 L(χ) 与显式 ε(χ,ψ,dx)；Langlands 把它唯一延拓到 W_K 的表示上，要求对特征是 Tate 的、短正合列乘性、0 次归纳。

## 定义

对拟特征标 $\chi\colon K^\times\to\mathbb C$，Tate 定义 $L(\chi)=(1-\chi(\varpi))^{-1}$（$\chi$ 非分歧），否则 $1$。固定非平凡加性特征标 $\psi$ 与 Haar 测度 $dx$，令 $d^\ast x=\|x\|^{-1}dx$、$\chi^\vee=\chi^{-1}\|\cdot\|$，则 Fourier 变换给出函数方程 $\int\hat f\chi^\vee d^\ast x/L(\chi^\vee)=\epsilon(\chi,\psi,dx)\int f\chi\,d^\ast x/L(\chi)$。显式地，取 $c\in K^\times$ 使 $v(c)=n(\psi)+c(\chi)$，则 $\epsilon(\chi,\psi,dx)=\|c\|^{-1}\chi(c)\operatorname{Vol}_{dx}(\mathcal O_K)$（非分歧）或 $\int_{c^{-1}\mathcal O_K^\times}\chi^{-1}(x)\psi(x)dx$（分歧）。

**记号**：$n(\psi)$ 是使 $\psi(\varpi^{-n}\mathcal O_K)=1$ 的最大整数（导子指数），$c(\chi)$ 是 $\chi$ 的导子；定理 1.3 的 $\epsilon(\cdot,\psi,dx)$ 在 $R(W_K)=K_0(\Rep W_K)$ 上有定义。

## 要点（为什么需要它）

1. Tate 的定理只管 $\GL_1$（即特征标）；高维时的 $\epsilon$ 不能靠积分显式写出，只能由公理刻画——这就是定理 1.3 的角色：Langlands 证明存在、Deligne 给短证明。
2. 公理 (2)「短正合列乘性」说明 $\epsilon$ 其实只依赖 $R(W_K)$ 里的类；这条加上 (1) 就足以把 $\epsilon$ 从特征标推到所有可约表示，是整套构造的引擎。
3. 公理 (3)「0 次归纳性」$\epsilon(\mathrm{ind}_{E/L}[r],\psi\circ\Tr_{L/K},\mu_L)=\epsilon([r],\psi\circ\Tr_{E/K},\mu_E)$ 是唯一性最吃劲的一条：它把不同扩域上的构造钉在一起。
4. $n(\psi)$ 与 $c(\rho)$ 一起出现的那条公式 $\epsilon(\rho\omega_s,\psi,dx)=(\#k)^{-(c(\rho)+n(\psi)\dim V)s}\epsilon(\rho,\psi,dx)$ 是后面 §3.6 里 JPPS 公式的原型。

## 核心公式

$$
$L(\chi)=(1-\chi(\varpi))^{-1}\ (\chi\ \text{非分歧}),\qquad L(\chi)=1\ (\chi\ \text{分歧})$$\frac{\int\hat f\chi^\vee\,d^\ast x}{L(\chi^\vee)}=\epsilon(\chi,\psi,dx)\cdot\frac{\int f\chi\,d^\ast x}{L(\chi)}$$\epsilon(\chi,\psi,dx)=\|c\|^{-1}\chi(c)\operatorname{Vol}_{dx}(\mathcal O_K)\ (\text{非分歧}),\qquad \int_{c^{-1}\mathcal O_K^\times}\chi^{-1}(x)\psi(x)\,dx\ (\text{分歧})$
$$

$$
$\frac{\int\hat f\chi^\vee\,d^\ast x}{L(\chi^\vee)}=\epsilon(\chi,\psi,dx)\cdot\frac{\int f\chi\,d^\ast x}{L(\chi)}$
$$

$$
$\epsilon(\chi,\psi,dx)=\|c\|^{-1}\chi(c)\operatorname{Vol}_{dx}(\mathcal O_K)\ (\text{非分歧}),\qquad \int_{c^{-1}\mathcal O_K^\times}\chi^{-1}(x)\psi(x)\,dx\ (\text{分歧})$
$$

## 定理与证明（或缺口）

### 定理 1.3（Langlands；Deligne 有短证明）

存在唯一函数 $\epsilon$ 把 $(K,\rho,\psi,dx)$ 送成 $\epsilon(\rho,\psi,dx)\in\mathbb C^\times$，使得 (1) 对特征是 Tate 的 $\epsilon$；(2) 对 $W_K$ 表示的短正合列乘性，从而下降到 $R(W_K)\to\mathbb C^\times$；(3) 对 0 次类满足归纳性。

> 证明状态：**cited**。底本引 [10] 只给存在性定理，未写证明；Deligne 的短证明也未展开。

出处：`A §1.1.10 p.6`

## 常见误解

- $\epsilon$ 依赖 $\psi$ 与 $dx$；底本在 (3) 里连测度一起变换（$\mu_L$ 对 $\mu_E$），否则归纳性不成立。
- 底本 Remark 明确说它的 $\epsilon$ 与 [10]（Tate）差一个因子 $q^{n(\psi)\dim V\cdot s}$：Tate 把它叫 $\epsilon$，本文的约定与 [11] 一致。读文献时必须先对齐这个惯例，否则 $\epsilon$ 差一个 $q$ 的幂。

## 相关卡

[Weil–Deligne 表示的导子 c(ρ)、L 因子与 ε 因子](../concepts/wd-invariants.md) · [导子 c(π)、深度、JPPS 的 ε 公式与深度 0 对照图](../concepts/conductor-depth.md) · [Weil 群 W_K、惯性群、野惯性群与驯特征标](../concepts/weil-group.md)

## 出处（印刷页）

- A p.6（A p.6）

> 说明：Tate 的 $L$/$\epsilon$ 与显式公式、定理 1.3 的三条公理照 p.6；「公理 (2) 是引擎」「(3) 是唯一性最吃劲的一条」是我们的判断。
