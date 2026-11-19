# Witten 2015（gtgl15）资料卡 · 骨架图

这张图是 Witten 2015（arXiv:1506.04293v3）的逻辑骨架：从 4d $\mathcal N=4$ 出发，紧致化到 Hitchin 系统，用谱曲线把几何展开，再把膜/线算符/本征膜的物理翻译成几何命题，最后用行列式线丛在 §7 算出赫克本征值。箭头上的数字是原文**印刷页**；概念卡是节点，推导卡是把节点连起来的边。

```text
§1  p.1–3     [O] n4-sym-partial-tqft ───deriv──▶ compactify-to-sigma
                    │  (4d N=4 的场内容与“部分拓扑”论证)
                    ▼
§2  p.2–22    [C] sigma-model-mh ──▶ branes-ab
                    │  靶空间 = MH（2+2=4）
                    ▼
§2.2 p.4–7    [A] higgs-bundle ─▶ hitchin-equations ─▶ hyperkahler-quotient
                    │   Hitchin 方程 = 超凯勒矩映射零点
                    ▼
§2.3–2.5 p.7–10  [A] hitchin-moduli ──┬──▶ stable-locus（T*M 开嵌入）
                    │                 ├──▶ hitchin-fibration（π: MH → V）
                    │                 └──▶ integrable-system（½ dim 对易 H）
                    ▼
§2.6 p.10–20  [A] spectral-curve ─▶ spectral-cover ─▶ kernel-cokernel
                    │   谱曲线/判别式/核与余核线丛 N(R) ≅ N⊗ψ*K^{N-1}
                    ├──▶ abelianization-prym（纤维 ≅ Prym(D/C) 的 torsor）
                    └──▶ distinguished-section（每个纤维挑一个标准点）
                    ▼
§2.6.6 p.18   [B] thooft-flux-psu（PSU(N) 分量 ← 't Hooft flux ξ ∈ H²(C,Z_N)）
§3   p.22–34  [B] dual-torus-fibration（S-对偶 = 纤维 T-对偶）
                    ├──▶ symplectic-form（Ω_I、耦合 τ、周期）
                    └──deriv──▶ symplectic-period-matching
                    ▼
§4.1–4.2 p.34–39  [C] line-operators ─▶ eigenbranes ─┬─▶ electric-eigenbranes
                    │                               │      ├─▶ universal-bundles
                    │                               │      └─▶ skyscraper-zero-brane
                    │                               └─▶ magnetic-eigenbranes ─▶ type-f-brane
                    ▼
§4.3–4.5 p.39–54  [D] thooft-operator ◀──deriv──▶ hecke-modification
                    │   't Hooft 算符 ↔ p 处赫克修正（U(1) 单极子 → Hecke）
                    ▼
§5   p.54–59  [C] magnetic-eigenbranes（= F 型膜） + type-f-brane
                    │   Hecke 保特征多项式 ⟹ 作用在 Hitchin 纤维内
                    ▼
§6   p.59–68  [E] determinant-line-pairing ─▶ gerbe-bfield
                    └──▶ pfaffian-theta（K^{1/2} 与 Z_2 gerbe 的 B 级补全）
                    ▼
§7   p.68–75  [E] magnetic-hecke-eigenvalue
                    ∏T^{(d_i)}B̂ = B̂ ⊗ (⊗_i L_p^{d_i})  （与电侧同一形式）
```

## 怎么用这张图

1. **第一次读**：从最上面 `n4-sym-partial-tqft` 出发，沿左侧主链（O → C → A → B → C → D → E）走一遍；每一段先看概念卡，再看对应推导卡。
2. **想补细节**：在 A 轨停下来读谱曲线三件套（`spectral-curve`/`spectral-cover`/`kernel-cokernel`）与五张 A 推导卡，这是全篇技术地基。
3. **想自测**：每张概念卡的 `question` 就是自测题；`md/` 下渲染版开头也印了这道题。

## 三条推荐阅读路径

### 几何侧（先把 Hitchin 系统读懂，再回来读物理）

`higgs-bundle` → `hitchin-equations` → `hyperkahler-quotient` → `hitchin-moduli` → `hitchin-fibration` → `integrable-system` → `spectral-curve` → `spectral-cover` → `kernel-cokernel` → `abelianization-prym` → `dual-torus-fibration` → `symplectic-form`

配推导：`hitchin-as-moment-map` → `dimension-count` → `spectral-genus` → `kernel-cokernel-relation` → `prym-abelianization` → `symplectic-period-matching`

### 物理侧（从 4d 理论出发，关心膜与线算符）

`n4-sym-partial-tqft` → `sigma-model-mh` → `branes-ab` → `line-operators` → `eigenbranes` → `electric-eigenbranes` → `skyscraper-zero-brane` → `magnetic-eigenbranes` → `type-f-brane`

配推导：`compactify-to-sigma` → `electric-action-formula`

### 计算侧（直接看 §7 的赫克本征值怎么算出来）

`magnetic-eigenbranes` → `type-f-brane` → `thooft-operator` → `hecke-modification` → `determinant-line-pairing` → `gerbe-bfield` → `magnetic-hecke-eigenvalue`

配推导：`thooft-hecke-u1` → `magnetic-hecke-eigenvalue`；顺带读 `thooft-flux-psu` 理解离散电/磁荷。

## 图与卡、与原文的对应

| 图上节点 | 概念卡 | 原文页 |
| --- | --- | --- |
| 4d 理论 / 部分拓扑 | `n4-sym-partial-tqft` | §1 p.1–3（脚注 `partial`） |
| Hitchin 方程 | `hitchin-equations`、`hyperkahler-quotient` | §2.2 p.4–7 |
| Hitchin 模空间 | `hitchin-moduli`、`stable-locus` | §2.3 p.7 |
| 纤维化与可积 | `hitchin-fibration`、`integrable-system` | §2.4–2.5 p.7–10 |
| 谱曲线 | `spectral-curve`、`spectral-cover`、`kernel-cokernel` | §2.6.1 p.10–13 |
| 阿贝尔化 | `abelianization-prym`、`distinguished-section` | §2.6.2 p.13–14、§2.7 p.20 |
| PSU(N) 分量 | `thooft-flux-psu` | §2.6.6 p.18 |
| 对偶环面 | `dual-torus-fibration`、`symplectic-form` | §3 p.22–34 |
| 膜与线算符 | `branes-ab`、`line-operators`、`eigenbranes` | §4.1 p.34–37 |
| 电/磁本征膜 | `electric-eigenbranes`、`magnetic-eigenbranes`、`type-f-brane` | §4.2 p.37、§5 p.54–59 |
| 't Hooft / 赫克 | `thooft-operator`、`hecke-modification` | §4.3–4.5 p.39–54 |
| 行列式线丛 | `determinant-line-pairing`、`gerbe-bfield`、`pfaffian-theta` | §6 p.59–68 |
| 赫克本征值 | `magnetic-hecke-eigenvalue`（推导） | §7 p.68–75 |

## 三个最容易搭错的地方

1. **别把 $\sigma$-模型当成精确理论**：它只在 $\MH$ 的一般点有效，奇点处要回到 $C$ 上联络的无穷维空间（`sigma-model-mh` 卡）。
2. **别把本征值当数字**：本征值是向量空间（Chan–Paton 纤维），这正是电/磁本征膜对偶能成立的关键（`eigenbranes` 卡）。
3. **别把 $S$-对偶当 4d 对偶**：本文不用 $S$-对偶证明 §4；它用的是 Hitchin 系统几何（Hecke 保特征多项式），只在 §3 把“S-对偶 = 纤维 T-对偶”当结构陈述用（`magnetic-eigenbranes`、`dual-torus-fibration`）。
