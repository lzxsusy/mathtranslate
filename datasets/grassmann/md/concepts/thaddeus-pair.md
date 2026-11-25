# Thaddeus 对

> `grassmann/concept/thaddeus-pair` · 轨道 3 · Reider 与 Thaddeus 再探 · 状态 draft

> **先自测**：Thaddeus 对为什么在曲线上用 $\Ext^1$，到了曲面上却要换成 $\Ext^2$？

## 一句话

曲线上的 Thaddeus 对是理想层对偶与线丛之间的扩张，其稳定性由斜率比较控制，退化情形由割线簇描述；曲面上则推广为倾斜心中的二项复形。

## 定义

设 $C$ 是光滑射影曲线，$L$ 是线丛，$Z,W\subset C$ 是有效除子。曲线上的 **Thaddeus 对**是指扩张 $\epsilon:0\to\mathcal I_W^\vee\to E_\epsilon\to L\otimes\mathcal I_Z\to0$，通常写作 $0\to\mathcal O_C(W)\to E_\epsilon\to L(-Z)\to0$，其中 $E_\epsilon$ 是秩 $2$ 的无挠凝聚层。当 $\deg L(-Z)>\deg\mathcal O_C(W)$ 且 $C\ne\mathbb P^1$ 时，一般（generic）扩张给出 Mumford 稳定的向量丛。

**记号约定**：$\mathcal I_W^\vee=\mathcal O_C(W)$ 在曲线上就是除子对应的线丛；$\phi:C\to\mathbb P(\operatorname H^0(C,K_C\otimes L(-Z-W))^\vee)$ 是自然线性系映射；曲面上把 $\mathcal I_W^\vee$ 换成移位对象 $\mathcal I_W^\vee[1]$。

## 要点（为什么需要它）

- 曲线情形两个线丛都平凡稳定，稳定性完全由斜率比较 $\mu(L(-Z))>\mu(\mathcal O_C(W))$ 决定。
- 不稳定的 $E_\epsilon$ 只能被提升为子丛的子线丛 $L(-Z')\subset L(-Z)$ 去稳定化，这些 $\epsilon$ 的轨迹恰是 $\phi$ 的像的割线簇。
- 曲面上对象换成 $0\to\mathcal I_W^\vee[1]\to E_\epsilon^\bullet\to L\otimes\mathcal I_Z\to0$，$E_\epsilon^\bullet$ 绝不是凝聚层。
- Serre 对偶把曲面版的 $\Ext^2$ 写成 $\operatorname H^0(S,K_S\otimes L\otimes\mathcal I_Z\otimes\mathcal I_W)^\vee$，$Z$ 与 $W$ 因此对称出现。

## 关键公式

$$
0\to\mathcal I_W^\vee\to E_\epsilon\to L\otimes\mathcal I_Z\to0
$$

$$
\deg L(-Z)>\deg\mathcal O_C(W)
$$

$$
\Ext^1_{\mathcal A_s}(L\otimes\mathcal I_Z,\mathcal I_W^\vee[1])\cong\operatorname H^0(S,K_S\otimes L\otimes\mathcal I_Z\otimes\mathcal I_W)^\vee
$$

## 定理与证明（或缺口）

### Thaddeus 对的存在性与退化描述

设 $C\ne\mathbb P^1$，$L$ 是 $C$ 上的线丛，$Z,W$ 是有效除子且 $\deg L(-Z)>\deg\mathcal O_C(W)$。则一般扩张 $0\to\mathcal O_C(W)\to E_\epsilon\to L(-Z)\to0$ 给出 Mumford 稳定的秩 $2$ 丛；不稳定的那些恰由 $\phi$ 的像的割线簇参数化。

**证明状态：只引出处，原书不重证**


出处：中译 p.56（§1，引 [Tha94]）

### 曲面 Thaddeus 对的 Ext 计算

设 $S$ 是曲面，$Z,W\subset S$ 是零维子概形，$0<s<1$。则在倾斜心 $\mathcal A_s$ 中 $\Ext^1_{\mathcal A_s}(L\otimes\mathcal I_Z,\mathcal I_W^\vee[1])\cong\operatorname H^0(S,K_S\otimes L\otimes\mathcal I_Z\otimes\mathcal I_W)^\vee$。

**证明状态：完整**

1. 把心内一阶扩张换成层上二阶扩张：$\Ext^1_{\mathcal A_s}(L\otimes\mathcal I_Z,\mathcal I_W^\vee[1])=\Ext^2_{\mathcal O_S}(L\otimes\mathcal I_Z,\mathcal I_W^\vee)$。
   - *为什么*：$\mathcal I_W^\vee[1]$ 是平移对象，倾斜心内的 $\Ext^1$ 等于原范畴的 $\Ext^2$。
2. 对 $n=2$ 用 Serre 对偶，得 $\Ext^2(L\otimes\mathcal I_Z,\mathcal I_W^\vee)\cong\operatorname H^0(S,K_S\otimes L\otimes\mathcal I_Z\otimes\mathcal I_W)^\vee$。
   - *为什么*：$\Ext^i(L\otimes\mathcal I_Z,\mathcal I_W^\vee)\cong H^{n-i}(K_S\otimes L\otimes\mathcal I_Z\otimes\mathcal I_W)^\vee$。


出处：中译 p.56（§1 末）

## 易错点

- 曲线版的 $\mathcal I_W^\vee=\mathcal O_C(W)$ 只在曲线上成立；曲面上 $\mathcal I_W^\vee[1]$ 是移位复形，不是层，不能按线丛去算次数。
- 只有一般扩张才稳定：特殊扩张会分裂，或落在割线簇 $\mathrm{Sec}^{d-1}-\mathrm{Sec}^{d-2}$ 上。
- $\deg L(-Z)>\deg\mathcal O_C(W)$ 是充分条件，且 $C=\mathbb P^1$ 时斜率论证要另作处理。

## 相关卡

- [Reider 定理](../concepts/reiders-theorem.md)
- [Bridgeland 稳定性条件](../concepts/bridgeland-stability-condition.md)
- [抛物丛与抛物次数](../concepts/parabolic-bundle.md)

## 出处

- ch3 §1 Thaddeus 对的定义；中译 p.56（英文 PDF p.61），源码 `chapters/ch03.tex:42`
