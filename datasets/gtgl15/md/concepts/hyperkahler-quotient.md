# 超凯勒商与复结构 I、J、K

> `gtgl15/concept/hyperkahler-quotient` · 轨道 A · Hitchin 几何与谱曲线 · 状态 dev

> **先自测**：为什么希钦模空间能同时容纳希格斯丛与平坦联络两种看似不同的复结构？

## 一句话

$\MH$ 是平坦超凯勒空间 $\mathcal W=T^*\mathcal Y$ 对规范群 $G$ 的超凯勒商；三个复结构 $I,J,K$ 分别把 $\MH$ 读成希格斯丛、平坦联络和第三种模型。

## 定义

令 $\mathcal Y$ 为 $C$ 上 $G$-联络的空间，$\mathcal W=T^*\mathcal Y$ 带平坦超凯勒度量，$G=\mathrm{Maps}(C,G)$ 作用保持三个复结构 $I,J,K$。$\MH=\mathcal W/\!/\!/G$ 是三个矩映射 $\nu_I,\nu_J,\nu_K$ 的零集模去 $G$ 的超凯勒商。$\Omega_I=\omega_J+i\omega_K$ 是 $I$-全纯辛形式。

**记号**：$I,J,K$；$\omega_I,\omega_J,\omega_K$；$\Omega_I$；$G=\mathrm{Maps}(C,G)$。

## 要点（为什么需要它）

1. $\mathcal W$ 平坦、超凯勒；商之后 $\MH$ 仍是超凯勒的（Hitchin 的超凯勒商定理）。
2. 复结构 $I$：$I$-全纯坐标是 $(\bar\partial_A,\varphi)$，于是 $\MH$ 的点就是希格斯丛。
3. 复结构 $J$：$J$-全纯坐标是复联络 $\mathcal A=A+i\varphi$，其零曲率条件给出平坦联络。
4. 复结构 $K$：第三个模型只用于证明辛形式与 A-膜/B-膜的对应，实际计算一般回到 $I$ 或 $J$。
5. $\Omega_I=\omega_J+i\omega_K$ 同时是全纯 2-形式和辛形式；$\MH$ 的复维数由 Hitchin 纤维化给出：$\dim_\mathbb{C}\MH=2(g-1)\dim G$（§2.4 eq (2.6)），不是 $\dim G$。

## 核心公式

$$
$$\MH=\mathcal W/\!/\!/G,\qquad \Omega_I=\omega_J+i\omega_K$$$$F_{z\bar z}-[\varphi_z,\varphi_{\bar z}]=0,\qquad D_{\bar z}\varphi_z=0$$
$$

$$
$$F_{z\bar z}-[\varphi_z,\varphi_{\bar z}]=0,\qquad D_{\bar z}\varphi_z=0$$
$$

## 定理与证明（或缺口）

### 超凯勒商定理

超凯勒流形对保持超凯勒结构的群作矩映射商，得到的商空间仍是超凯勒流形，维数减 $3\dim G$（实维数）。

> 证明状态：**gap**。原文 $\S2.2$ 引用 [13][19]，未复述证明。

出处：`A p.4`

## 常见误解

- 商去的是复化规范群 $G_\mathbb{C}$（GIT 意义），不是紧群 $G$；两者维数差一倍。
- $\Omega_I$ 是 $I$-全纯辛形式，不是 Kähler 形式；不要和 $\omega_I$ 混淆。
- 三个矩映射不是三组独立实方程：一个实、两个复，合起来对应希钦方程。
- 在非稳定点处商有奇点，低能 σ-模型描述在这些点失效（$\S2.1$）。

## 相关卡

[希钦方程](../concepts/hitchin-equations.md) · [希钦模空间 $\MH$](../concepts/hitchin-moduli.md) · [辛形式 $\Omega_I$ 与耦合常数](../concepts/symplectic-form.md) · [二维 $\sigma$-模型与靶空间 $\MH$](../concepts/sigma-model-mh.md) · [希钦方程 = 超凯勒矩映射商](../derivations/hitchin-as-moment-map.md)

## 出处（印刷页）

- A p.4–6（A p.4 eq (2.1)）
- A p.6（A p.6 eq (2.4)）
- C p.59–126（C p.59）

> 说明：A=原文 $\S2.2$ 的 $\MH=\mathcal W/\!/\!/G$ 与 $\Omega_I=\omega_J+i\omega_K$；B=把 $J$ 复结构解释成复联络的平坦性；C=超凯勒商定理按 [13][19] 背景补全。最没把握处：$K$ 复结构在原文没有独立展开。
