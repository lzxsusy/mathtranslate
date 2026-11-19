# 万有丛、万有希格斯丛与陈–帕顿丛

> `gtgl15/concept/universal-bundles` · 轨道 C · 膜、线算符与本征膜 · 状态 dev

> **先自测**：为什么“在 $p$ 处取值”这件事需要万有丛，而它又什么时候不存在（只有 twisted 版本）？

## 一句话

万有丛 $\mathcal E\to C\times M$ 与万有希格斯丛 $\mathcal E_H\to C\times M_H$ 把一个点处的场编码成向量空间；陈–帕顿丛则是膜上的 sheaf，线算符作用通过它实现。

## 定义

设 $M$ 是 ${}^LG$ 丛的模空间，万有丛（universal bundle / Poincaré bundle）$\mathcal E\to C\times M$ 的限制 $\mathcal E|_{C\times\{m\}}$ 是 $m$ 对应的丛。把 $\varphi$ 也纳入，得到万有希格斯丛 $\mathcal E_H\to C\times M_H$，它在 $p\in C$ 处的纤维 $\mathcal E_H|_{p\times M_H}$ 是 $\MH$ 上的向量丛，编码场在 $p$ 的取值。给定表示 ${}^LR$ 的伴丛记 $\mathcal E_{H,{}^LR}$；中心作用非平凡时它只是 twisted bundle（gerbe 上）。膜的陈–帕顿丛（Chan–Paton bundle）是膜上的 sheaf $U$，作用 $U\mapsto U\otimes\mathcal E_{H,{}^LR}|_{p\times\MH}$ 实现 Wilson 线。

**记号**：$\mathcal E$；$\mathcal E_H$；$\mathcal E_{H,{}^LR}$；Chan–Paton 丛 $U$；twisted bundle。

## 要点（为什么需要它）

1. 万有丛把“模空间上的点”翻译成“$C$ 上的丛”：$\mathcal E|_{C\times\{m\}}\leftrightarrow m$。
2. 万有希格斯丛同时包含 $E$ 与 $\varphi$ 的数据；限制在 $p\times\MH$ 上得到 $p$ 处的场值。
3. 万有丛可能整体不存在：中心非平凡时存在 gerbe 障碍，只能取 twisted 版本（$\S6.3$）。
4. 陈–帕顿丛是膜的 data，不是规范丛：同一张膜可以带不同 rank 的 Chan–Paton 空间。
5. Wilson 线的作用就是把 Chan–Paton 丛张量上万有希格斯丛在 $p$ 处的纤维（eq (4.4)）。

## 核心公式

$$
$$\mathcal E\to C\times M,\qquad \mathcal E_H\to C\times M_H,\qquad \mathcal E_{H,{}^LR}=(E_H\times_{{}^LG}{}^LR)$$$$U\mapsto U\otimes\mathcal E_{H,{}^LR}|_{p\times\MH}$$
$$

$$
$$U\mapsto U\otimes\mathcal E_{H,{}^LR}|_{p\times\MH}$$
$$

## 定理与证明（或缺口）

### 万有丛的局部存在与障碍

万有丛在局部总存在；整体存在当且仅当中心作用不产生 gerbe 障碍。

> 证明状态：**sketch**。原文 $\S4.2$ 与 $\S6.3$ 分别陈述障碍，未给完整上同调证明。

出处：`A p.38`

## 常见误解

- 万有丛不是“所有丛的并”：它的底是 $C\times M$，限制到每个 $m$ 才是单个丛。
- 中心非平凡时万有丛不存在（只有 twisted 版本）；直接用普通丛计算会漏掉离散电荷。
- Chan–Paton 丛属于膜，不属于 4d 规范理论；它是 2d 边界条件的 data。
- 表示 ${}^LR$ 要取对偶群的表示（电侧），不要把 $G$ 与 ${}^LG$ 的表示混用。

## 相关卡

[电本征膜](../concepts/electric-eigenbranes.md) · [Gerbe 与 $B$-场（离散电/磁荷）](../concepts/gerbe-bfield.md) · [$\mathbf F$ 型膜](../concepts/type-f-brane.md) · ['t Hooft flux 与 $PSU(N)$ 分量](../concepts/thooft-flux-psu.md) · [线算符](../concepts/line-operators.md)

## 出处（印刷页）

- A p.37–39（A p.38 eq (4.4)）
- A p.63–64（A p.64）
- A p.15（A p.15 eq (2.32)）

> 说明：A=原文 $\S4.2$ 的万有丛/万有希格斯丛与 eq (4.4)、$\S6.3$ 的 gerbe 障碍；B=把局部存在与整体障碍写成两步；C=Chan–Paton 的范畴地位按 $\S4.1$ 的 sheaf 描述补。最没把握处：万有丛存在性的精确条件原文散见 $\S4.2$ 与 $\S6.3$。
