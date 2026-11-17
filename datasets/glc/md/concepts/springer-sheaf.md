---
id: glc/concept/springer-sheaf
type: concept
track: B
---

# 长度 $i$ 修改的 Springer 层

> $\operatorname{Spr}_i=\varphi_!\operatorname{IC}_{\widetilde{\operatorname{Mod}}_n^{-i}}$ 是反常层、互异点轨迹的中间延拓，其直和项为微小核。

**问题**：$\operatorname{Spr}_i$ 的三条性质是什么，它怎样实现外幂的交错投影？

## 定义

令 $\operatorname{Mod}_n^{-i}:=\{(\mathcal{V}'\hookrightarrow\mathcal{V})\mid\mathcal{V}/\mathcal{V}'\in\operatorname{Tor}^i\}$，并令 $\Delta_i:X\to X^{(i)}$ 为 $x\mapsto i\cdot x$，$H_n^{i,+}:=X\times_{X^{(i)}}\operatorname{Mod}_n^{-i}$；$H_n^{i,+}$ 通过允许支撑在 $x$ 处的非半单长度 $i$ 商，把微小对应紧化。有序（Springer）解消为 $\widetilde{\operatorname{Mod}}_n^{-i}:=\{\mathcal{V}_0\hookrightarrow\mathcal{V}_1\hookrightarrow\cdots\hookrightarrow\mathcal{V}_i\mid\length(\mathcal{V}_j/\mathcal{V}_{j-1})=1\ \ \forall j\}$，并有真态射 $\varphi:\widetilde{\operatorname{Mod}}_n^{-i}\to\operatorname{Mod}_n^{-i}$，$(\mathcal{V}_0\subset\cdots\subset\mathcal{V}_i)\mapsto(\mathcal{V}_0\subset\mathcal{V}_i)$，以及有序支撑映射 $r:\widetilde{\operatorname{Mod}}_n^{-i}\to X^i$。在互异点轨迹上，$\varphi$ 是有序支撑覆盖，并带有通过置换长度一商的次序给出的自然 $S_i$ 作用。Claim 断言 Springer 层 $\operatorname{Spr}_i:=\varphi_!\operatorname{IC}_{\widetilde{\operatorname{Mod}}_n^{-i}}$ 满足三条性质。

*记号*：$\operatorname{Tor}^i$：长度为 $i$ 的挠层；$X^{(i)}$：$X$ 的第 $i$ 次对称积；$\operatorname{IC}$：中间扩张层（反常层）；$d_i=i(n-i)$；$\operatorname{sgn}$：$S_i$ 的符号表示。

## 要点

- $\operatorname{Spr}_i$ 是反常层。
- $\operatorname{Spr}_i$ 是从互异点轨迹作出的中间延拓；在该轨迹上，它是与有序支撑覆盖及 $S_i$ 的正则表示相联系的局部系统。
- 交错直和项是微小核：$\operatorname{Hom}_{S_i}(\mathrm{sgn},\operatorname{Spr}_i)|_{\operatorname{Hecke}_n^i}\simeq\mathbb{Q}_\ell|_{\operatorname{Hecke}_n^i}[d_i](d_i/2)$，$d_i=i(n-i)$。
- 机制与通常的 Springer 层相同：解消为初等商排序，符号表示则提取外幂直和项。

## 关键公式

- $\operatorname{Spr}_i:=\varphi_!\operatorname{IC}_{\widetilde{\operatorname{Mod}}_n^{-i}}$
- $\operatorname{Hom}_{S_i}(\mathrm{sgn},\operatorname{Spr}_i)|_{\operatorname{Hecke}_n^i}\simeq\mathbb{Q}_\ell|_{\operatorname{Hecke}_n^i}[d_i](d_i/2),\qquad d_i=i(n-i)$
- $\widetilde{\operatorname{Mod}}_n^{-i}:=\{\mathcal{V}_0\hookrightarrow\cdots\hookrightarrow\mathcal{V}_i\mid\length(\mathcal{V}_j/\mathcal{V}_{j-1})=1\ \ \forall j\}$

## 定理与证明

### Claim 2.13.1（Springer 层的性质）（要点（有缺口））

Springer 层 $\operatorname{Spr}_i:=\varphi_!\operatorname{IC}_{\widetilde{\operatorname{Mod}}_n^{-i}}$ 满足：(1) $\operatorname{Spr}_i$ 是反常层；(2) $\operatorname{Spr}_i$ 是从互异点轨迹作出的中间延拓，在该轨迹上是与有序支撑覆盖及 $S_i$ 的正则表示相联系的局部系统；(3) 交错直和项是微小核，$\operatorname{Hom}_{S_i}(\mathrm{sgn},\operatorname{Spr}_i)|_{\operatorname{Hecke}_n^i}\simeq\mathbb{Q}_\ell|_{\operatorname{Hecke}_n^i}[d_i](d_i/2)$，$d_i=i(n-i)$。


> 缺口：讲义只述不证：§2.13 陈述该 Claim 并说明其机制与通常 Springer 层相同，未给出证明；§2.14 的投影公式计算以它为前提。

*出处*：Claim 2.13.1 / 原书 p.18


## 易错点

- $\operatorname{Spr}_i$ 用 $\varphi_!$（真前推）而非 $\varphi_*$；$\varphi$ 是真态射这一点是前提。
- 交错直和项的同构只在限制到 $\operatorname{Hecke}_n^i$ 后成立，不能在整个 $\operatorname{Mod}_n^{-i}$ 上断言它是常数层。
- $d_i=i(n-i)$ 与 Tate 扭转 $(d_i/2)$ 成对出现；只写移位 $[d_i]$ 会把归一化弄错。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§2.13 长度 i 修改的紧化叠，p.18（PDF p.18），`源码/chapters/ch02.tex:238-256（Claim 2.13.1）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Springer+correspondence — 该页只有参考文献列表（Kazhdan–Lusztig 1980、Springer 1978、Sauter arXiv:1307.0973），没有 Claim 2.13.1 中 Mod_n^{-i}、有序解消 φ、Spr_i = φ_! IC 及 Q_ℓ[d_i](d_i/2) 的逐条陈述。

## 关联

- `glc/concept/minuscule-hecke-reduction`
- `glc/concept/global-hecke-stack`
- `glc/concept/hecke-eigensheaf-general`
