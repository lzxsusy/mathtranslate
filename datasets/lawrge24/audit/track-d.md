# LAWRGE 2024 notes — track D 外部来源核验

范围：`cards/concepts/{plancherel-density, local-plancherel, local-conjecture, shearing, trace-formula-hom}.json` + `cards/derivations/inner-product-trace.json`（6 张卡）。
逐条结果见同目录 [`track-d.jsonl`](./track-d.jsonl)（17 行，一行一条断言）。

## 0. 结论摘要

| 指标 | 值 |
| --- | --- |
| 卡数 | 6 |
| 断言数 | 17（每卡 2–3 条） |
| 来源条目 | 37（4 篇论文 + 2 个 nLab 页，共 6 个不同 URL） |
| supported | 10 |
| partially-supported | 5 |
| unverifiable | 1 |
| conflict | 1 |
| severity critical / major / minor | 0 / 8 / 9 |

无 critical。底本自述"不完整、未校订"，核验中确实看到两类问题：**编号/术语是笔记自铸**（`q-char`、`IndCoh(·)^♮`），以及**一处修正版与已发表版本冲突**（shearing 卡 (11.19)）。

最需人工处理的 3 条：

1. `shearing` (11.19) 写成 `Sh_c(X_{F/O}) ≅ IndCoh(M̌/Ǧ)^♮`。BZSV 已发表的修正是 `SHV(X_F/G_O) ≃ QC^{fatslash}(M̌/Ǧ)`（sheared quasicoherent），`IndCoh`/`QC^!` 只出现在 de Rham 局部谱 2-范畴的类比里，`(-)^♮` 全文未出现。**verdict = conflict, major**。
2. `local-conjecture` 的例 11.17/11.18（`C[ξ²]` vs `C[xy]`、`C[det]`）在 BZSV/Sak13/SV17 中找不到逐字对应，只能核到 A¹ 例的不变量 `C[xξ]`（次数 `a+b`）。**verdict = unverifiable, major**。
3. `local-plancherel` (11.2) 把内积写成 `∫_{Ǧ_c} ⟨f̂,ĝ⟩ · q-char(Ǧ×G_gr, M̌) dμ_H`，并称 (11.1) 是保内积同构。BZSV (9.1) 只对 Hecke 平移 `T_V e` 陈述内积，(9.2) 再等于 `Hom` 的对偶的 Frobenius 迹；"对任意 `f,g` 保内积"是笔记的加强版。**verdict = partially-supported, major**。

## 1. 方法与底本对应

- 底本：LAWRGE 2024 NOTES（73 页工作坊笔记，Ben-Zvi / Sakellaridis / Venkatesh 主讲，无 arXiv）。卡内编号是 notes 的 §8、§11。
- 主外部源：**BZSV, _Relative Langlands Duality_, arXiv:2409.04677v1**（只有 v1；v2 返回 404）。notes 的内容与 BZSV §7–§9 同源，编号映射为：
  - notes (11.1)(11.2) ≈ BZSV Conjecture 7.5.1 + §9.2 的 (9.1)/(9.2)/(9.5)；
  - notes (11.12) ≈ BZSV 的未加 shearing 版本（§7.0.2 方框里已带 `(-)^{fatslash}`）；
  - notes (11.15)(11.16) ≈ BZSV (7.15)（原文就带 `?`）；
  - notes (11.4)–(11.11) ≈ BZSV Lemma 2.6.1 + Prop 9.2.1 的推导；
  - notes 例 11.3 ≈ BZSV Example 7.6.1（`X = A¹`, `G = G_m`）/ 7.6.2（群情形）。
- 每条断言先在 BZSV 取**逐字句**（从 arXiv HTML 转出的纯文本切出），再尽量补一个不同来源（Sak13 / SV17 / BF08 / nLab）；补不到时如实记为"同一文档的另一处"，不硬凑第二源。
- 引文一律从抓取的 HTML/ar5iv 文本原样切出，未做转述；URL 全部 `curl` 实测过状态码。

## 2. 来源清单（均已实测可打开）

| 来源 | URL | 用到的位置 |
| --- | --- | --- |
| BZSV, Relative Langlands Duality | https://arxiv.org/html/2409.04677v1 | §2.5.7/§2.5.8（shearing、半 Tate twist）、§2.6 Lemma 2.6.1、§6.1+Remark 6.1.1、§7.0.2、§7.5.2 pointings、§7.5 (7.15)(7.16)、§7.6 Example 7.6.1/7.6.2、§8 (8.1)、§9.2 (9.1)(9.2)(9.5)+Prop 9.2.1、§9.3 (9.7) |
| Sakellaridis, Spherical functions on spherical varieties | https://arxiv.org/abs/0905.4244 | §9 Theorem 9.0.1, (9.2)/(9.3)：未分歧 Plancherel 测度与密度 `L_X(χ)` |
| Sakellaridis–Venkatesh, Periods and harmonic analysis on spherical varieties | https://arxiv.org/abs/1203.0039 | §0.6.3 Théorème 0.6.3.4：`⟨Φ₁,Φ₂⟩ = ∫_{Ǧ} θ^Λ_π(Φ₁⊗Φ̄₂) μ_G(π)` |
| Bezrukavnikov–Finkelberg, Equivariant Satake category and Kostant–Whittaker reduction | https://arxiv.org/abs/0707.3799 | Abstract：等变 Satake ↔ 对偶 Lie 代数上的凝聚层 |
| nLab, Tate twist | https://ncatlab.org/nlab/show/Tate+twist | 末段："rational Tate twists … are used for instance in geometric representation theory" |
| nLab, Lefschetz trace formula | https://ncatlab.org/nlab/show/Lefschetz+trace+formula | "The Lefschetz formula holds more generally in Weil cohomology theories…" |

打不开或找不到的：

- `https://ncatlab.org/nlab/show/Chevalley-Shephard-Todd+theorem` → **404**（该站无此条目；未找到可替代页，因此群情形 `C[ȟ*]^W ≅ H*(BG)` 的经典依据没有独立来源，相关断言改由 BF08 支持"归属"而不支持"指数"）。
- `https://arxiv.org/abs/2409.04677v2` → **404**，只能引 v1。
- 例 11.17/11.18 的 `C[ξ²]`、`C[det]`：在 BZSV §7.6/§8、Sak13 §9、SV17 §0.6 内检索无逐字对应（见 `track-d.jsonl` 中该条 `note` 列的尝试 URL）。

## 3. 逐卡结果

| 卡 | 断言 | verdict / severity | 一句话依据 |
| --- | --- | --- | --- |
| plancherel-density | 密度 `= L(z,M̌)d^×z`，`L` 是 `O(M̌)` 对 `Ǧ×G_gr` 的分次特征标 | partial / major | BZSV (9.7) 的密度是 `det(I-t|ǧ_X/ǎ_X)/det(I-(t,q^{-1/2})|V_X')`——**行列式商**，且需 `Ǎ_X`-限制；BZSV 全文无 "q-character" 一词 |
| | 例：`X=A¹, G=G_m` 核为 `d^×z/((1-q^{-1/2}z)(1-q^{-1/2}z^{-1}))` | supported / minor | BZSV Ex 7.6.1：`λ·x=λ^{-1}x, λ·ξ=λξ`，两个坐标同处 degree 1，代入 (9.7) 即此核 |
| | 群情形指数 `q^{-1}`，因 `G_gr` 在 `ȟ` 上权 2 | supported / minor | BZSV Ex 7.6.2 说 `V_X=(ȟ^∨)*` 放在权 2，并称"即 [BF08] 的 derived Satake"；`q^{-1}=q^{-2/2}` 需用同文 Prop 9.2.1 |
| local-plancherel | `C_c(X(F))^{G(O)} ≅ C[Rep Ǧ_X]` 为 `H_G`-模等价 | partial / major | 等价由 Conjecture 7.5.1 支持，但已发表形式的光谱侧是 `QC^{fatslash}(M̌/Ǧ)`，不是 `C[Rep Ǧ_X]`（省略 shearing） |
| | 内积公式带 `q-char(Ǧ×G_gr,M̌)dμ_H` | partial / major | BZSV (9.1) 只对 `T_V e, T_W e` 陈述；"对任意 `f,g` 保内积"是加强 |
| | `1_{X(O)}` ↦ 平凡表示（pointing） | supported / minor | §7.5.2：`L_X(δ_X) ≃ O^{fatslash}`；"平凡表示"应读作 Hecke 单位对象/结构层 `O` |
| local-conjecture | (11.12) 未 shearing 的 `Sh_c ≅ QCoh(M̌/Ǧ)` 不成立（原文自标） | supported / major | 正确形式带 `(-)^{fatslash}`；底本的自标被外部印证 |
| | 检验归结为 `H*_G(X(C)) ≅ C[M̌]^{Ǧ}` | supported / major | BZSV (7.15) 同样带 `?`，脚注 60 称"可手工验证"，属期望非定理 |
| | 两例代数同构但分次不同（`C[ξ²]` / `C[det]`） | unverifiable / major | 只核到 A¹ 例不变量 `C[xξ]`（次数 `a+b`），两例无逐字对应 |
| shearing | 按 `G_gr` 半整数分次重设 `G_m`-作用 | supported / minor | §2.5.7 定义 `N ↦ ⊕ N_i⟨i⟩ = ⊕ Π^i N_i[i](i/2)`；nLab 支持半 Tate twist |
| | 左侧 `Fr ↔ q^{1/2}` 与右侧整分次对齐 | supported / minor | §2.5.8 需选 `√q`；Prop 9.2.1 证明："degree n ↔ Frobenius 特征值 `q^{-n/2}`" |
| | 修正版 (11.19) `≅ IndCoh(M̌/Ǧ)^♮` | **conflict / major** | 已发表修正是 `QC^{fatslash}`；`IndCoh/QC^!` 只在 de Rham 2-范畴类比中；`(-)^♮` 未出现 |
| trace-formula-hom | (11.4) `∫_{Ǧ_c} χ_Aχ_B dμ_H = dim Hom(B,A)^{Ǧ}` | partial / major | 对应物是 (9.2)+(9.5)：内积 = Frobenius 迹于 `Hom^∨`；`dim` 形式与 `χ̄` 约定是笔记改写 |
| | (11.8)-(11.9) 张量–Hom 伴随到层范畴 Hom | supported / minor | (8.1) 与 (7.16) 逐字对应；但原卡自注的 `indcoherent?` 问号在外部无答案（BZSV 全篇用 QC） |
| | (11.10) `tr(Fr^{-1}|Hom(F,G)) = Σ_{z∈Z(F_q)} f(z)g(z)` | partial / minor | Lemma 2.6.1 的主体成立，但右端取 `Hom^∨`、左端用 `D𝒢` 的迹函数 `ǧ`；nLab 支持 `F=G=Q_ℓ` 退化为 Lefschetz |
| inner-product-trace | 七步链条 (11.7)=(11.9)=(11.11) 复述 BZSV 的迹公式推导 | supported / minor | 与 §2.6+§9.2 同构；属整理性复述，不引入新断言 |
| | 第 7 步 `Fr^{-1} ↔ q^{-1/2}` 对齐 | supported / minor | Prop 9.2.1 有显式陈述 → provenance 应从 B 改成 **A** |

## 4. 需改卡清单（按优先级）

1. **`cards/concepts/shearing.json`（必须改）**：(11.19) 与 BZSV 已发表版本冲突。建议在卡内注明"底本给出的修正形式与已发表版本不同：BZSV 的修正是 `Shv(X_F/G_O) ≃ QC^{fatslash}(M̌/Ǧ)`；`IndCoh(M̌/Ǧ)^♮` 未见于 BZSV，`IndCoh/QC^!` 只作 de Rham 局部谱 2-范畴的类比"。保留底本原样可以，但必须标 conflict，否则下引用者会当成定理。
2. **`cards/concepts/local-conjecture.json`（应改）**：例 11.17/11.18 标 unverifiable，或说明"笔记自算，未在 BZSV/Sak13/SV17 找到"。
3. **`cards/concepts/local-plancherel.json`（建议改）**：(11.1)(11.2) 加限定"未 shearing 形式"，与 local-conjecture/shearing 卡的自我修正衔接；"保内积"改成"在 Hecke 平移上保内积（BZSV 9.1）"。
4. **`cards/concepts/plancherel-density.json`（建议改）**：`L(z,M̌)` 的描述改为"`O(M̌)` 作为 `Ǧ×G_gr`-模的分次特征标（等价地，(9.7) 的行列式商）"，并注明 `q-char` 是笔记术语（BZSV 无此词）。
5. **`cards/concepts/trace-formula-hom.json`（建议改）**：(11.4) 注明显式对应 `⟨T_V e, T_W e⟩ = [Hom(·,·)^∨]`（BZSV 9.1–9.2），并说明 `χ_Aχ_B` 与 `χ_V \overline{χ_W}` 的复共轭约定差。
6. **`cards/derivations/inner-product-trace.json`（应改）**：第 7 步 provenance 由 B 改为 A（BZSV Prop 9.2.1 证明中显式写出）。
7. **术语统一**："平凡表示"→"Hecke 单位对象（几何 Satake 下为结构层 `O`）"；`q-char` 首次出现处标注"笔记自铸，非文献术语"。

## 5. 局限

- **来源独立性有限**：17 条中 9 条只用到 BZSV 的两处不同位置（同一文档，冠以两个"来源条目"），8 条另有非 BZSV 来源——其中 5 条是 Sak13/SV17（与 BZSV 共享作者 Sakellaridis、Venkatesh），2 条 nLab，1 条 BF08。因此本报告的 `supported` 应读作"与已发表文献一致"，不等于"多学派独立确认"；各条 `note` 已注明是否同源。
- **shearing 是单源构造**：作为命名概念的 `shearing` 只在 BZSV §2.5/§6 有系统表述，nLab 仅支持其中的"半 Tate twist / 有理 Tate twist"约定。因此 shearing 卡的两条 supported 实为"单源 + 一条独立约定"。
- 底本自述不完整、未校订，本报告不替它补证明；凡外部与底本不一致处均记为 conflict，未做调和。
- 未修改卡片、`README`、`index.jsonl`、`taxonomy.md`、`verification.jsonl`，未运行 `git`。
