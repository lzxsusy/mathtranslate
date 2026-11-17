# 局部系统

> `kw/concept/local-system` · 轨道 E · Langlands 与翻译器 · 状态 dev

> **先自测**：局部系统与特征膜是什么关系，它为什么是几何 Langlands 的左端？

## 一句话

曲线 $C$ 上的局部常值层，等价于基本群表示 $\pi_1(C)\to G_{\mathbb C}$；电特征膜的特征值 $V_p$ 正拼成这样的局部系统。

## 定义

局部系统是 $C$ 上的局部常值层，等价于平坦向量丛，也等价于同态 $\rho:\pi_1(C)\to G_{\mathbb C}$。本文中它出现两处：电特征膜的特征值 $V_p$ 是 $C$ 上平坦丛的纤维；几何 Langlands 则以 $^L G_{\mathbb C}$ 的局部系统为出发点。

**记号**：$\pi_1(C)$：曲线基本群；$\rho$：单值表示；$V_p$：$p$ 处特征值。

## 要点（为什么需要它）

1. 它是几何 Langlands 的左端：$\pi_1(C)\to{}^LG_{\mathbb C}$ 对应 $\mathrm{Bun}_G$ 上的 Hecke 特征层。
2. 它是特征膜本征值的几何化身：$V_p$ 随 $p$ 拼成平坦丛，整体可带单值。
3. 它把算子特征值升级为基本群表示：全体 Wilson 算子的联合特征膜给出 $G_{\mathbb C}$ 局部系统（Tannaka）。
4. 电侧与磁侧的局部系统取值群不同，这是检验整套对应一致性的枢纽。

## 核心公式

$$
$\rho:\pi_1(C)\to G_{\mathbb C}$$X_pB\simeq B\otimes V_p,\qquad V_p\ \text{为平坦丛的纤维}$
$$

$$
$X_pB\simeq B\otimes V_p,\qquad V_p\ \text{为平坦丛的纤维}$
$$

## 定理与证明（或缺口）

### 特征膜给出局部系统

若 $B$ 是所有 Wilson 算子 $W_q(R)$ 的联合特征膜，则 $V_p$（$p\in C$）构成 $C$ 上平坦丛，从而给出同态 $\rho:\pi_1(C)\to G_{\mathbb C}$。

> 证明状态：**sketch**。原文 p.97 只证 $V_p$ 是平坦丛纤维并提到单值，p.122 直接把 $^L G_{\mathbb C}$ 局部系统作为几何 Langlands 输入；“用 Tannaka 还原”属整理（provenance B），原文未给。

出处：`B p.97 eq (6.25)`

## 常见误解

- 把局部系统当成普通向量丛；关键是平坦联络/局部常值，整体可有非平凡单值。
- 弄错取值群：$M_H(G)$ 一侧零膜给出 $G_{\mathbb C}$ 平坦丛，而几何 Langlands 的输入 $^L G_{\mathbb C}$ 局部系统来自 $^L G$ 一侧的零膜（经 S-对偶成为磁特征膜）。
- 忽略半稳定条件：$\vartheta$ 对应的点要半稳定才能当作 $M_H({}^LG)$ 的点。

## 相关卡

[特征膜（eigenbrane）](../concepts/eigenbrane.md) · [几何 Langlands 对应](../concepts/geometric-langlands.md) · [Wilson 算子](../concepts/wilson-operator.md) · [电特征膜 = 平坦 ^LG_C 联络](../derivations/electric-eigenbranes.md)

## 出处（印刷页）

- B p.97（B p.97 eq (6.25)）
- B p.122（B p.122）
- B p.4–5（B p.4–5）

> 说明：A=原文 p.97 的平坦丛与 p.122 的 $\pi_1\to{}^LG_{\mathbb C}$；B=把联合特征膜升级为局部系统（Tannaka 属整理）；C=电/磁两侧取值群的辨析。
