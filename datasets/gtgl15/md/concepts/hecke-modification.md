# 赫克修正与赫克变换

> `gtgl15/concept/hecke-modification` · 轨道 D · 't Hooft 算符与赫克修正 · 状态 dev

> **先自测**：为什么一次单点的赫克修正只改变谱覆盖上线丛的局部因子，而完全不动希格斯场的特征值？

## 一句话

赫克修正在单点 $p$ 处改变全纯丛的局部结构（$E_-\to E_+$）；在谱覆盖上它只是给线丛乘一个 $\mathcal O(q_i)$，并保持特征多项式，从而作用在 Hitchin 纤维上。

## 定义

赫克修正在 $p\in C$ 处把全纯丛 $E_-$ 换成另一个丛 $E_+$，两者在 $C\setminus\{p\}$ 上同构、在 $p$ 处全纯结构不同。$U(1)$ 时是 $\mathcal O\mapsto\mathcal O(mp)$；$U(2)$ 的 minuscule 情形是 $E_+=\mathcal O(p)\oplus\mathcal O$；一般 $U(N)$ 是 $E_+=\bigoplus_i\mathcal O(n_ip)$。修正类型由 ${}^LG$ 的支配最高权（不可约表示 ${}^LR$）标号。包含 Higgs 时要求 $\varphi$-不变：在谱覆盖上对应 $L\mapsto L\otimes\mathcal O(q_i)$（eq (4.49)），即只改线丛不改 $y$；一般 $\varphi(p)$ 正则半单时恰有 $N$ 个 $\varphi$-不变修正（对应 $p$ 上方的 $N$ 个原像）。非 minuscule 时紧化的模空间含 monopole bubbling（Schubert cell/cycle）。

**记号**：$E_-\to E_+$；$p$；${}^LR$；$L\mapsto L(q_i)$；monopole bubbling。

## 要点（为什么需要它）

1. 赫克修正是单点操作：$E_-$ 与 $E_+$ 在 $C\setminus\{p\}$ 上同构。
2. 修正类型 ↔ ${}^LG$ 的支配最高权/不可约表示；minuscule 权时相应模空间是紧的（如 $\mathrm{Gr}(k,N)$）。
3. 含 Higgs 时要求 $\varphi$-不变，条件化为 $\varphi_-(p)\cdot b=0$（eq (4.41)），即 $b$ 是本征向量。
4. 谱覆盖上：$L\mapsto L\otimes\mathcal O(q_i)$ 只改线丛，故特征多项式不变，修正保 Hitchin 纤维。
5. 非 minuscule 时需 monopole bubbling 才能紧化；本文只处理 minuscule + 非分歧点。

## 核心公式

$$
$$E_-\ \rightsquigarrow\ E_+\ \ \text{at }p,\qquad E_+=E_-\ \text{在}\ C\setminus\{p\}\ \text{上}$$$$L\mapsto L\otimes\mathcal O(q_i),\qquad \operatorname{Tr}\varphi_+^s=\operatorname{Tr}\varphi_-^s$$
$$

$$
$$L\mapsto L\otimes\mathcal O(q_i),\qquad \operatorname{Tr}\varphi_+^s=\operatorname{Tr}\varphi_-^s$$
$$

## 定理与证明（或缺口）

### $\varphi$-不变修正的计数

若 $\varphi(p)$ 正则半单、$p$ 非分歧，则恰有 $N$ 个 $\varphi$-不变赫克修正，对应 $p$ 上方的 $N$ 个原像 $q_i$。

> 证明状态：**sketch**。一般（非平凡全纯型）情形的计数与 bubbling 原文未处理；此处仅非分歧、正则半单情形。

出处：`A p.52`

## 常见误解

- 赫克修正不是同构类变换：它改变 $p$ 处的局部基，$E_+$ 与 $E_-$ 在 $C\setminus\{p\}$ 同构但整体不同。
- $\varphi$-不变是额外条件，不是自动的：普通赫克修正会改变 $\varphi$ 的极点结构。
- 非 minuscule 权的模空间不紧，需要 monopole bubbling；把紧化空间当成普通 Grassmann 会错。
- $L\mapsto L(q_i)$ 只对非分歧点 $p$ 成立；分歧点处修正会与谱覆盖的局部结构纠缠。

## 相关卡

['t Hooft 算符](../concepts/thooft-operator.md) · [磁本征膜](../concepts/magnetic-eigenbranes.md) · [谱覆盖、判别式与分歧除子](../concepts/spectral-cover.md) · [阿贝尔化与 Prym 簇](../concepts/abelianization-prym.md) · ['t Hooft 算符 $\leftrightarrow$ $p$ 处赫克修正（$U(1)$）](../derivations/thooft-hecke-u1.md)

## 出处（印刷页）

- A p.39–43（A p.42 eq (4.17)）
- A p.43–45（A p.44 eq (4.19)）
- A p.48–54（A p.52 eq (4.45)）

> 说明：A=原文 $\S4.3$ 的赫克修正、$\S4.4.2$ 的 U(2) 例子、$\S4.5$ 的 $\varphi$-不变条件与计数（eq (4.45)(4.49)）；B=把计数写成三步；C=非 minuscule 的 bubbling 按 $\S4.4.2$ 的说明补。最没把握处：$\varphi$-不变条件在一般（非正则半单）情形的计数原文未给。
