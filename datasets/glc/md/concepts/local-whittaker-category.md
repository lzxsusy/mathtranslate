---
id: glc/concept/local-whittaker-category
type: concept
track: H
---

# 局部 Whittaker 范畴与双 Whittaker 范畴

> 带 $G(\mathcal K)$ 作用的 DG 范畴对 $N(\mathcal K)$ 取 $\psi$-等变部分得 $\operatorname{Wh}$；双 Whittaker 范畴充当重构映射的基环。

**问题**：$\operatorname{Wh}(\mathcal C)$ 与 $\operatorname{BiWhit}(G)$ 各是什么，重构映射写成什么形状？

## 定义

令 $\mathcal K=\mathbb C((t))$、$\mathcal O=\mathbb C[[t]]$。若 DG 范畴 $\mathcal C$ 带有 $G(\mathcal K)$ 作用，则它的非退化 Whittaker 范畴为 $\operatorname{Wh}(\mathcal C):=\mathcal C^{N(\mathcal K),\psi}$。在 [Gai18]、[FR23] 的 Whittaker 形式体系中，局部几何 Langlands 的基本思想预言 $\operatorname{DMod}(G(\mathcal K))\text{-}\mathrm{Mod}^{\mathrm{temp}}\simeq\operatorname{ShvCat}(\operatorname{LocSys}_{\check G}(D^\circ))$，其中 $D^\circ=\operatorname{Spec}\mathcal K$。在这一图景下，双 Whittaker 范畴 $\operatorname{BiWhit}(G):=\operatorname{DMod}((N(\mathcal K),\psi)\backslash G(\mathcal K)/(N(\mathcal K),\psi))$ 应当识别为 $\operatorname{BiWhit}(G)\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check G}(D^\circ))$。对一个 $G(\mathcal K)$-范畴 $\mathcal C$，预期的重构映射是 $\operatorname{Wh}(\operatorname{DMod}(G(\mathcal K)))\otimes_{\operatorname{BiWhit}(G)}\operatorname{Wh}(\mathcal C)\longrightarrow\mathcal C$。

*记号*：$\mathcal K$ 为形式 Laurent 级数域、$\mathcal O$ 为形式幂级数环；$D^\circ=\operatorname{Spec}\mathcal K$；$\operatorname{ShvCat}$ 为谱叠上的范畴层；$\mathcal C^{N(\mathcal K),\psi}$ 为 $N(\mathcal K)$-等变、按特征标 $\psi$ 取的部分；$\psi$ 为 $N$ 上的非退化加性特征标。

## 要点

- $\operatorname{Wh}$ 把 $G(\mathcal K)$-范畴送到 $\operatorname{BiWhit}(G)$-模，张量 $\otimes_{\operatorname{BiWhit}(G)}$ 在 $\operatorname{Wh}$ 值上取。
- 重构映射全忠实，其像是由 $\operatorname{Wh}(\mathcal C)$ 生成的 $\operatorname{DMod}(G(\mathcal K))$-子模。
- 因此 $\mathcal C$ 温和，当且仅当这个像是整个 $\mathcal C$。
- 非分歧情形：$\operatorname{Sph}_{G,x}:=\operatorname{DMod}(G(\mathcal O)\backslash G(\mathcal K)/G(\mathcal O))$ 是 $x\in X$ 处的球面 Hecke 范畴；带强 $G(\mathcal O)$ 作用的 $\mathcal C$ 受其球面不变量 $\mathcal C^{G(\mathcal O)}$ 控制，后者是 $\operatorname{Sph}_{G,x}$-模。
- 对 $\operatorname{Bun}_G$，每个 $x\in X$ 通过 Hecke 修改给出 $\operatorname{Sph}_{G,x}$ 的作用；Færgeman–Raskin 证明 Arinkin–Gaitsgory 的 $\operatorname{DMod}(\operatorname{Bun}_G)^{\mathrm{temp}}$ 定义与 $x$ 无关。

## 关键公式

- $\operatorname{Wh}(\mathcal C):=\mathcal C^{N(\mathcal K),\psi}$
- $\operatorname{BiWhit}(G):=\operatorname{DMod}((N(\mathcal K),\psi)\backslash G(\mathcal K)/(N(\mathcal K),\psi))$，讲义预期它 $\simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check G}(D^\circ))$
- $\operatorname{Wh}(\operatorname{DMod}(G(\mathcal K)))\otimes_{\operatorname{BiWhit}(G)}\operatorname{Wh}(\mathcal C)\longrightarrow\mathcal C$
- $\operatorname{Sph}_{G,x}:=\operatorname{DMod}(G(\mathcal O)\backslash G(\mathcal K)/G(\mathcal O))$

## 定理与证明

### 重构映射的全忠实性（要点（有缺口））

重构映射 $\operatorname{Wh}(\operatorname{DMod}(G(\mathcal K)))\otimes_{\operatorname{BiWhit}(G)}\operatorname{Wh}(\mathcal C)\to\mathcal C$ 全忠实，其像是由 $\operatorname{Wh}(\mathcal C)$ 生成的 $\operatorname{DMod}(G(\mathcal K))$-子模；故 $\mathcal C$ 温和当且仅当该像是整个 $\mathcal C$。

1. 讲义在 §13.2 直接陈述全忠实性与像的描述，未给论证。  
   *为什么*：该结论属于所引的 Whittaker 形式体系。

> 缺口：讲义只述不证：原文只说重构映射全忠实到由 $\operatorname{Wh}(\mathcal C)$ 生成的 $\DMod(G(\mathcal K))$-子模上，于是温和性等价于该像充满 $\mathcal C$；讲义并未把它归为某条单独命名的定理。

*出处*：§13.2 局部 Whittaker 范畴与温和性 / 原书 p.65


## 易错点

- $\operatorname{BiWhit}(G)$ 是 DG 范畴而不是交换环，$\otimes_{\operatorname{BiWhit}(G)}$ 是范畴张量，不要按环上的模张量理解。
- 「应当识别为 $\operatorname{QCoh}(\operatorname{LocSys}_{\check G}(D^\circ))$」在讲义中是预期（局部几何 Langlands 的预言），不是已证定理，不能当定义用。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§13.2 局部 Whittaker 范畴与温和性，p.65（PDF p.65），`源码/chapters/ch13.tex:46-61（Wh、BiWhit 与重构映射）`

## 核验

状态：`source-only`（2026-11-18）
- Gai18：https://arxiv.org/abs/1811.02468 — 「Whit(C):=C^{L(N),χ}≃lim C^{N_α,χ}⊂C」——直接支持卡 Wh(C):=C^{N(K),ψ}
- Dhillon22：https://arxiv.org/abs/2205.14578 — 「D-mod(LN,ψ\LG/LN,ψ) ≃ QCoh(LocSys_Ǧ)」随即注明「This is a striking and essentially wide open conjecture」——支持卡「应当识别为」且属预期而非定理
- Dhillon22：https://arxiv.org/abs/2205.14578 — 「the tautological map D-mod(K/H)⊗_{D-mod(H\K/H)} C^K→C … is always a fully faithful embedding」（有限维 K）——仅是类比，未给出 G(K) 的重构映射
- Gai18：https://arxiv.org/abs/1811.02468 — grep「reconstruct」「temper」「QCoh」「LocSys」0 命中，§7.3 无重构映射、BiWhit 或局部温和等价——卡 gap_note 称其为「[Gai18] 的定理」在该文无据

## 关联

- `glc/concept/tempered-category`
- `glc/concept/whittaker-conservativity`
- `glc/concept/whittaker-coefficient`
