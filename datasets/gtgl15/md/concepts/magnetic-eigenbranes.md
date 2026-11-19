# 磁本征膜

> `gtgl15/concept/magnetic-eigenbranes` · 轨道 C · 膜、线算符与本征膜 · 状态 dev

> **先自测**：为什么“对 't Hooft 线本征”的膜恰好是 Hitchin 纤维上的秩 1 $A$-膜，而不是别的几何对象？

## 一句话

§4 猜测并在 §5 验证：$G$ 侧对 't Hooft 线本征的磁本征膜正是 $F$ 型膜，即 Hitchin 纤维上的秩 1 $A$-膜配平坦 Chan–Paton 线丛。

## 定义

磁本征膜是使 't Hooft 线 $T({}^Lw,p)$ 作用为 $B\mapsto B\otimes V$ 的膜。猜测（$\S4.2$ 末）与 $\S5$ 的验证：它们就是 $F$ 型膜——支撑在 Hitchin 纤维 $F$ 上、对 $K$ 是 $A$-膜（$\omega_K$-Lagrangian）、带秩 1 平坦 Chan–Paton 线丛 $\mathcal L$；由 $F$ 是复环面、$\mathcal L$ 全纯且 $c_1=0$ 带平坦联络，它同时对 $I$ 是 $B$-膜、对 $J,K$ 是 $A$-膜，即 $(B,A,A)$ 型。Hecke 修正保持特征多项式（eq (4.35)），故 't Hooft 把纤维映到自身；在一般纤维上所有希格斯丛稳定，故修正可逐纤维定义。$\S5.2$ 算出作用 $\hat U=\sum_i\Phi_i^*(U)$，$\S5.3$ 用平移本征丛证明本征性，$\S5.4$ 得 eq (5.8) $T({}^Lw,p)B=B\otimes(\oplus_i\mathcal N_i)$。

**记号**：$F$；$\mathcal L$（平坦 Chan–Paton）；$\Phi_i$（Hecke 修正）；$\oplus_i\mathcal N_i$；$(B,A,A)$。

## 要点（为什么需要它）

1. 磁本征膜的候选是 F 型膜：支撑整条 Hitchin 纤维 + 秩 1 平坦 Chan–Paton 线丛。
2. 关键机制：Hecke 修正保持特征多项式，所以 't Hooft 作用不会把纤维 $F$ 移到别的纤维。
3. 一般纤维上每个希格斯丛稳定（脚注 17），因此“任意不稳定化”的 Hecke 修正在这里被限制为纤维内操作。
4. 秩 1 平坦线丛在复环面上对平移不变：$f_e^*\mathcal L=\mathcal L\otimes\mathcal N_{f_e}$，由此得到本征性（eq (5.4)–(5.7)）。
5. $\S5.4$：eq (5.8) 给出本征值 $\oplus_i\mathcal N_i$，具体数值在 §7 算出（$U(1)$ 时 $\otimes_i\mathcal L_p^{d_i}$）。

## 核心公式

$$
$$T({}^Lw,p)B=B\otimes\left(\bigoplus_i\mathcal N_i\right)\qquad(\text{磁本征膜})$$$$\hat U=\Phi'^*(U)\oplus\Phi''^*(U)\ \ (U(2)),\qquad \hat U=\sum_i\Phi_i^*(U)\ \ (U(N))$$
$$

$$
$$\hat U=\Phi'^*(U)\oplus\Phi''^*(U)\ \ (U(2)),\qquad \hat U=\sum_i\Phi_i^*(U)\ \ (U(N))$$
$$

## 定理与证明（或缺口）

### $F$ 型膜是磁本征膜

支撑在 Hitchin 纤维上、带平坦 Chan–Paton 线丛的秩 1 $A$-膜对 't Hooft 线本征。

> 证明状态：**sketch**。原文 $\S5$ 在一般纤维、minuscule 权与非分歧点 $p$ 的假设下验证；非 minuscule 需要 monopole bubbling，原文未处理。

出处：`A p.56`

## 常见误解

- 磁本征膜是 $(B,A,A)$ 型；不要写成 $(B,B,B)$（那是零维膜）。
- F 型膜支撑在整条纤维上，不是单点；这是它与零维膜（电本征膜）的对偶差别。
- 本征性依赖 $c_1(\mathcal L)=0$（有平坦联络）；有曲率的线丛没有平移不变联络，不构成本征膜。
- 高秩 Chan–Paton 不产生新磁本征膜（$\S5.4$）：它们只是固定向量空间乘一个秩 1 本征丛。

## 相关卡

[$\mathbf F$ 型膜](../concepts/type-f-brane.md) · [本征膜](../concepts/eigenbranes.md) · [电本征膜](../concepts/electric-eigenbranes.md) · [赫克修正与赫克变换](../concepts/hecke-modification.md) · [磁本征膜的赫克本征值（$U(1)$ 与 $SU(N)$）](../derivations/magnetic-hecke-eigenvalue.md)

## 出处（印刷页）

- A p.54–55（A p.54）
- A p.56–57（A p.57 eq (5.2)）
- A p.59（A p.59 eq (5.8)）

> 说明：A=原文 $\S5.1$ 的猜测、$\S5.2$ 的 eq (5.1)(5.2)、$\S5.3$ 的平移本征丛、$\S5.4$ 的 eq (5.8)；B=把“保持特征多项式→纤维内映射→本征”整理成三步；C=$(B,A,A)$ 型标签按 $\S5.1$ 的表述补。最没把握处：脚注 17 关于稳定性的论证原文只有一句。
