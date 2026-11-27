# 每日核验 2026-11-27

- 采样：20 张（`sample_daily.py --n 20`，seed=2026-11-27；确定性抽样，未手工换卡）；集分布：siebert 2、ggl08 1、gtgl15 1、kw06 2、functoriality 2、ggl09 1、dmod 2、sy0238 1、kshms 2、lbook04 2、seidel 1、benzvi_glc 1、gw06 1、glc 1。
- 首轮结果（12:50）：pass 8 / issue 11（critical 0、major 3、minor 9；共 12 条 issue）/ unverifiable 1。
- **复审后最终（13:22）**：pass 7 / issue 12（critical 0、major 3、minor 10；共 13 条 issue）/ unverifiable 1。
- ⛔ 立即处理：无 critical。
- 页码口径：siebert/ggl08/benzvi_glc/glc/ggl09 PDF=印刷页；kw06/gw06 PDF=印刷+1；gtgl15 实测 PDF=印刷+2（README 写 +1，已在卡 3 记下，数据集未改）；lbook04 ch9 +3、ch3 +7。详见 `notes/METHOD.md`。
- 校验：`check_daily.py` 0 error、0 warning；12 条 issue 的 `card_says` 与 `quote` 均经 `notes/verify_quotes.py` 逐字复核（BAD=0）。

## issue 清单

| # | 卡 | 字段 | severity | 一句话 | 证据 |
|---|---|---|---|---|---|
| 1 | siebert/correction/prop-3-12-lci | pitfalls[1] | minor | Gysin 拉回的统一定义 (3.58)（Def 3.4）在 p.50，卡写「p.51 起」 | siebert.pdf p.50 Definition 3.4，ι![V]:=s_0^*[C_{W/V}] |
| 2 | gtgl15/concept/eigenbranes | theorems[0] | minor | 把定义（本征值取值为向量空间）登记为 theorem 且 `proof.status=gap` | 卡自身 gap_note：「原文 §4.1 直接以定义形式给出 eq (4.3)」 |
| 3 | kw/concept/n4-sym-theory | theorems[0].source | minor | eq (2.14) 在印刷 p.10（PDF 11，页脚「10」），卡写 p.11 | kw06.pdf PDF 11 页脚 10；`(2, 1, 4) ⊕ (1, 2, 4). (2.14)` |
| 4 | functoriality/concept/strip-shrinking | theorems[0].source | minor | Thm 1（eq (62)）在 p.27（§3.5.2），卡写 p.25 | functoriality.pdf p.27「(62) HF*(L0; L01; L12; L2) ≃ HF*(L0; L01 ∘ L12; L2)」 |
| 5 | functoriality/concept/strip-shrinking | theorems[1].source | minor | WW15 Thm 5.1（收缩带/环域的推广）在 p.28，卡写 p.26 | functoriality.pdf p.28「[WW15, Theorem 5.1] … shrinking a strip or annulus」 |
| 6 | ggl09/deriv/descent-to-xi | steps[4].text、locator | **major** | 第 5 步把「左(Neumann)与右(Dirichlet)边界之差」写成「Neumann 与小 S² 之差」，该差其实是 x_i=0 的右边界，逻辑反向 | ggl09.pdf p.16–17：「difference between the left and right boundaries … is homologous to a small two-sphere」；右边界 x_i 消失 |
| 7 | siebert/concept/gromov-witten-invariant | pitfalls[4] | **major** | Prop 3.12 的假设是「S is lci」；卡删掉 lci、改成「连通基底」，与卡 1 的勘误直接冲突 | siebert.pdf p.58「If S is lci, then for all s, s′ …」 |
| 8 | lbook04/concept/ch9-langlands-spectral | key_points[2] | minor | 带 \|det\|^{iσ} 扭时极点在 s=−iσ、s=1−iσ，只有 σ=0 才是 s=1；「反过来保证 s=1 有极点」只对未扭情形 | 原书 p.222（PDF 225）「then at s = -iσ and s = 1 - iσ」；两条 observation 是 π×π̃ |
| 9 | lbook04/concept/ch3-three-motives | sources[0].pages | minor | 定义正文含 §2.3（τ'=γτ、Example 2.1 ℘ 函数，印刷 42），pages 只到 40 | 原书 p.42 = PDF 49 |
| 10 | bzg/concept/categorical-fourier | sources[0].section | **major** | FM_𝒦(F)=p_{Y!}(p_X^*F⊗𝒦) 归于 §2.1，但 §2.1 是「范畴/Hilbert 空间类比」，全文无此核公式；FM 只在 §1.3 p.6 作 general theme 提及 | benzvi.pdf p.6「general theme of categorical Fourier」；p.8 为 §2.1 |
| 11 | gw06/concept/two-dimensional-defect | sources[0].page_note | minor | α∈𝒵(G) 与 η∈Hom(π1(G),U(1)) 在对偶下互换在印刷 31（PDF 32），pages 只到 30 | gw06.pdf PDF 32「are exchanged by」 |
| 12 | glc/concept/fundamental-local-equivalence | sources[0].pages | minor | 相对构造与 Op(X\{x})^unr 定义在印刷 72，pages 只有 [71] | glc.pdf p.72「Localization should enhance to a relative construction」 |
| 13 | sy38/concept/tamagawa-number | key_points[1] | minor | 把 Weil 猜想的完成者写成不存在的「Lai–Künnemann」；标准链为 Langlands（分裂）→ Rapoport/Lai（拟分裂）→ Kottwitz 1988（数域一般） | Lurie AWS 大纲「proven by Kottwitz (building on earlier work of Langlands and Lai)」；Pacific J. Math. 338 (2025) 综述 |

> 卡 1 与卡 12 曾互相矛盾：卡 1 的勘误明说「讲义原文也没有『同一连通分支』这一条」，卡 12 却在 pitfalls 里补上「连通基底」。本批已把卡 12 改回 lci（major），冲突解除。

> 复审补记（13:10–13:22）：首轮 8 张 pass 逐张回一手 PDF 抽验，7 张维持；`sy38/concept/tamagawa-number` 改判 minor（第 13 条）。
> `ggl09/deriv/descent-to-xi` 第 5 步另补 locator：`A p.16` → `A p.16–17`（边界论证在 p.17），计入该卡第 2 处改动。
> 20 卡逐卡矩阵与证据见 `round2/ROUND2.md`。

## unverifiable

- `seidel/concept/exact-lagrangian`：缺 Seidel《Fukaya Categories and Picard–Lefschetz Theory》（EMS 2008）原书 PDF；试过 `datasets/_audit/third_party_2026-11-26/tmp/sources/`、`08_source_code/SY01-31_Fukaya范畴与Picard–Lefschetz理论（Seidel）/工程文件/`（只有译稿与成品，无原书）、全盘 `*seidel*.pdf`。卡内数学自洽（Stokes 论证 E(u)=∫u*ω=∫∂D u*λ=0），但 §7 p.96–100、§8l p.112 的原文无法核；4 条 unverifiable_aspects 见 records。

## 本批可形式化提示

- `ggl09/deriv/descent-to-xi`：五步链条每步都带 locator，可直接形式化为「下降方程 (2.8) ⇒ x_i(S) 为 Q-闭且只依赖 [S]」；需补 Q 在形式次数/ghost number 上的分级约定（卡已给 2d_i−r）。
- `kw/concept/n4-sym-theory`：场内容与超代数可形式化为表示论陈述；需补 SU(4)_R ≅ Spin(6) 的嵌入约定及 (2,1,4)⊕(1,2,4) 的复共轭记号。
- `siebert/correction/prop-3-12-lci` 与 `siebert/concept/gromov-witten-invariant`：形式化时一律以源命题的 lci 假设为准，勿继承卡 12 的「连通」加强。

## 备注

- 本轮新增 ggl09 的 arXiv PDF 仅存 `%TEMP%/cardverify/`，未入库；核验轮本身对 `datasets/**` 零改动，随后的修卡见下节。
- 工作树在本轮开始前已有大量未提交改动（11-26 的其他工程），本轮 commit 只暂存 `11_card_audit/daily_verify/2026-11-27/` 与 `11_card_audit/daily_verify/ledger.jsonl`。
- 方法、页码表与复跑命令：`notes/METHOD.md`；复核脚本：`notes/verify_quotes.py`、`notes/assemble.py`。

## 修卡（2026-11-27，核验之后）

- 按用户要求把 13 条 issue 修入 `datasets/` 卡片：12 张卡、25 处字段级改动（含复审新增的 sy0238 与 ggl09 locator）；逐处 before/after 见 `fixes/fix_log.json`，逐卡七节案例见 `fixes/casebook/`（12 例），施工说明与验证记录见 `fixes/README.md`、`fixes/TRACE.md`。
- 派生文件同步：9 个 md 由卡片重生成后回拷，gw06 手工两行；`gw06/index.jsonl` 的 `pdf_pages` 同步；lbook04 与 benzvi 的生成器源码同步，重建结果与卡片逐字段相等。
- 验证：`verify_final.py` 全量 1859 张 `errors: 0`；`round2/check_round2.py` 复核 25 处 after 全对；`git diff --check` 干净；既有 32 例 casebook 未动。
- 需知：kw06 的 `theorems[0].source` 按页脚由 p.11 改为 p.10（11-26 批次此处 off-by-one），故 `verify_final.py` 对该条永久显示 1 个 STALE，属预期。
