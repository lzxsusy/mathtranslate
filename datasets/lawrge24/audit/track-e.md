# E 轨外部核验（周期层 / L-层 / 整体猜想 / 例子）

审计对象：`datasets/lawrge24/cards/concepts/` 中 E 轨 13 张卡。逐卡挑 1–3 条实质断言，找外部来源逐字核对。**未修改任何卡片，未碰 git，未写 `verification.jsonl`。**

## 0. 结论摘要

| 指标 | 数值 |
| --- | --- |
| 卡数 | 13 |
| 断言数 | 28 |
| supported | 18 |
| partially-supported | 7 |
| unverifiable | 3 |
| conflict | 0 |
| severity critical / major / minor | 0 / 1 / 27 |

一句话：E 轨的公式与定义与 BZSV 正式论文（arXiv:2409.04677v1）高度一致，**未发现与外部文献正面冲突的断言**。主要问题不是「错」，而是三类：① 底本静默加强了 BZSV 的假设（固定点从单个推广到多个）；② 少数「更强」措辞（Whittaker 层是 Hitchin 截面上的常值层、ω≅O）在 BZSV 中只有弱形式；③ `trace-formula-hom` 属 D 轨已审内容，本轨无法独立复核。另有 3 条在时间盒内找不到外部来源，判 unverifiable（不代表为假）。

## 1. 方法与底本对照

1. 从 13 张卡的 `summary` / `key_points` / `formulas` 中提取断言，逐条回读底本：`ch05.txt`（Tate 例，p.24–26）、`ch12.txt`（L-函数，p.57–60）、`ch13.txt`（周期层/L-层/猜想，p.60–66）、`ch14.txt`（例子，p.66–70）、`ch15.txt`（不动点/纤维，p.71–73）。
2. 外部来源优先用 BZSV 正式论文 v1 的 PDF 与 HTML（本地 `bzsv.pdf` / `bzsv_pdf.txt`，页码即印刷页），再用 Gaitsgory 2017、Braverman–Gaitsgory 2002、Ginzburg–Rozenblyum 2018、nLab 交叉核对。
3. `quote` 全部取自实际抓到的文本（pdftotext / HTML 去标签 / nLab 页面），保留 LaTeXML 与 pdftotext 的原始转写痕迹（如 `BunX G Ñ BunG`、`Hompδρ , LX̌ q`），未做美化。`tier`：E1 = arXiv/期刊论文，E2 = nLab 等百科式来源。
4. **重要限定**：BZSV 是本底本（LAWRGE 2024 notes）的正式论文版，二者同源。因此「笔记与 BZSV 一致」只能算同源核对，不能算独立验证；各条 notes 已注明是否只有 BZSV 一个来源。

## 2. 来源清单（均为本次实测可访问）

| 来源 | URL | 用途 | 访问情况 |
| --- | --- | --- | --- |
| BZSV, Relative Langlands Duality (v1) | https://arxiv.org/abs/2409.04677 ；PDF https://arxiv.org/pdf/2409.04677v1 | 主源：§10.3/§10.6、§11.4/§11.8、§12.1–12.4、§13.0.2、§18 | 200，PDF 4.72 MB，1.47 M 字符 |
| D. Gaitsgory, A "strange" functional equation ... (Ann. ENS 50, 2017) | https://doi.org/10.24033/asens.2341 （DASH PDF 实测） | 奇迹对偶 ↔ Serre 对偶；Bun_G 非拟紧 | 200 |
| Braverman–Gaitsgory, Geometric Eisenstein series | https://arxiv.org/abs/math/9912097 | Eis 与 Verdier 对偶相容 | 200 |
| Ginzburg–Rozenblyum, Gaiotto's Lagrangian subvarieties ... | https://arxiv.org/abs/1703.08578 | T*Bun_G=Higgs、Gaiotto Lagrangian | 200 |
| nLab, L-function | https://ncatlab.org/nlab/show/L-function | L-函数三性质定义 | 200 |
| nLab, Riemann zeta function | https://ncatlab.org/nlab/show/Riemann+zeta+function | completed ζ 的定义 | 200 |
| nLab, Hitchin fibration | https://ncatlab.org/nlab/show/Hitchin+fibration | T*Bun 的 Hitchin 基 | 200 |

## 3. 逐卡结果

| 卡 | 断言数 | verdict | severity | 外部依据（要点） |
| --- | --- | --- | --- | --- |
| tate-example | 2 | partial ×2 | minor ×2 | BZSV p.207（θ 级数=周期函数）、p.214/§10.6.2（Iwasawa–Tate）；nLab completed ζ |
| l-function | 3 | supported ×2, partial ×1 | minor ×3 | nLab L-function（三性质）；BZSV p.156（X=GL_n×A^n）、p.96（GJ X=Mat_n） |
| period-sheaf | 2 | supported ×2 | minor ×2 | BZSV p.207（unnormalized period sheaf）、p.214；Gaitsgory §0.1.4（Bun_G 非拟紧） |
| beilinson-projection | 3 | supported ×2, unverifiable ×1 | minor ×3 | BZSV p.257（局部常值条件、Betti 左/étale 右伴随）、p.258 |
| global-conjecture | 2 | supported ×2 | minor ×2 | BZSV p.257–258（Conj 12.1.1、P^norm/L^norm、dualizing twist、de Rham 例外） |
| trace-formula-hom | 1 | unverifiable | major | 无（D 轨已审；本轨未找到可逐字引用源） |
| eisenstein-example | 2 | supported ×2 | minor ×2 | BZSV p.264 (12.7)、p.265（Eis! 与 P^Eis 积分变换）；BG02 Cor 2.1.3 |
| whittaker-sheaf | 2 | supported ×1, partial ×1 | minor ×2 | BZSV p.260（Whittaker ↔ dualizing，差 shift）；p.266（仅「对应 Hitchin 截面」） |
| raviolo-hecke | 2 | supported ×2 | minor ×2 | BZSV p.280（raviolo 定义、equivariant affine Grassmannian、Hecke 范畴） |
| hitchin-gaiotto | 2 | supported ×1, unverifiable ×1 | minor ×2 | GR18（Higgs=T*Bun、moment map 的 Lagrangian）；BZSV p.355 (18.1) |
| miraculous-duality | 2 | supported ×2 | minor ×2 | BZSV p.261–262（Δ_!k/Δ_!ω、Chevalley twist）；Gaitsgory Thm 0.1.6 + Conj 0.2.3 |
| fixed-points | 2 | supported ×1, partial ×1 | minor ×2 | BZSV p.244（∧*H¹）、p.241（假设唯一不动点 x0）、(11.33) |
| l-sheaf | 3 | supported ×1, partial ×2 | minor ×3 | BZSV p.233 (11.16)、p.244 (11.37) |

## 4. 最需人工处理的 3 条

1. **`trace-formula-hom`（unverifiable / major，且卡内 `track` 实为 D）**  
   该卡 11.4、11.8–11.9、11.10 已被 `track-d.md` 审过（partial/major、supported/minor、partial/minor）。本轨未能找到可逐字引用的独立外部文献；BZSV 对应段落也不含这些编号。建议**以 D 轨结论为准，E 轨不重复计分**，并在 merge 时去重。

2. **`fixed-points` 的纤维直和（partial / minor）**  
   底本 p.73 写 `fiber of L-sheaf = ⊕_{x∈X̌^fix} ∧*H¹(T_x)`；BZSV §11.8.1 明确假设 **唯一**不动点 `x0`（`The classical fixed point locus ... is a singleton x0`），(11.33) 算的是 `Hom(δ_ρ, L_Ẋ)` 而非多不动点直和。底本 Remark 15.5 把读者指向 §11.8，属**静默加强**。建议在卡上补「需假设不动点有限/孤立，多不动点按直和延拓」或降格为 conjecture/remark。

3. **`l-sheaf` 的 `ω≅O` 与 `whittaker-sheaf` 的「Hitchin 截面上的常值层」（partial / minor）**  
   BZSV (11.37) 只给 `Hom(δ_ρ,L_Ẋ)=π_ρ^* ω`，未说 `ω` 平凡化；后者是底本 Ex 13.23 用 Loc_Ǧ 的辛结构补的。Whittaker 一侧，BZSV p.266 只说 `the Whittaker period sheaf corresponds to a section of the Hitchin fibration`，没有「常值层」的强度。两处都建议把底本的强断言标注为「在额外平凡化/归一化下」。

> 次一级候选：`tate-example` (5.1) 的 `∫₀^∞ x^s Σ_{n∈ℤ}` 含 n=0 项、字面积分发散，标准形式应用 `θ−1`（partial/minor）；`l-function` 的「Hecke 1936 是最早实例」若不加限定则不成立（Riemann/Dirichlet 更早）。

## 5. 失败 / 受限检索记录

| 检索 | 结果 |
| --- | --- |
| `en.wikipedia.org`（Riemann zeta、Theta、L-function、Hecke L-function、Rankin–Selberg、Higgs bundle、Lefschetz trace 等） | **连接超时 25 s（HTTP 000）**，全部失败；故本轮缺 E2 级经典文献，只能改用 nLab |
| `mathoverflow.net` | **403**（被拒），未使用 |
| nLab `Beilinson projector`、`Whittaker sheaf` | **404**（nLab 无此条目） |
| BZSV v2 | **404**，只有 v1（D 轨已记录） |
| arXiv:1502.03068 | 实际是控制论论文 *Multi-Sensor Scheduling...*，与奇迹对偶无关；正确的 Gaitsgory 文献是 Ann. ENS 2017（改从 DASH/SMF 取） |
| arXiv:math/9912105 | 实际是 Berenstein–Kazhdan *Geometric and unipotent crystals*；Braverman–Gaitsgory 的正确编号是 **math/9912097** |
| arXiv:1106.4789（Gaiotto–Witten） | *Knot Invariants from Four-Dimensional Gauge Theory*，与 Hitchin/Gaiotto Lagrangian 无直接关系；改用 GR18 (1703.08578) |
| Kostant 截面 `κ=f+Z_g(e)`、Hitchin 截面与整体幂零锥横截 | 时间盒内未定位到逐字外部文本；判 unverifiable |
| Sakellaridis–Venkatesh 1203.0039、Sakellaridis 0905.4244 | PDF 已下载（2.39 MB / 0.89 MB），时间盒内未及逐条提取；后续可补「period/L-函数」侧的独立第二源 |
| `(P_G)_spec = j_! k_C`（例 13.28） | BZSV/nLab 未找到对应陈述；未查 Stacks Project，判 unverifiable |

## 6. 局限

- BZSV 与底本同源，凡「仅 BZSV 支持」的条目（period-sheaf、global-conjecture、l-sheaf 定义等）严格说只有**一个**来源；已在各条 notes 标明。
- 引文保留了 pdftotext/LaTeXML 的转写痕迹（`Ñ`、`˚`、`ρ` 等），以保证逐字；阅读时按原论文排版理解。
- 本轨只做「外部文献是否支持」，不判断底本内部推导是否完整；`conflict` 为 0 是本轮检索范围内的事实，不等于不存在冲突。
