# 第二轮独立复核（2026-11-27）

> **目的**：不信任首轮判定与 13:07 的修卡结果，把 20 张样本逐张回到一手 PDF 重核：
> 逐条验证 25 处 after 值、抽验首轮判 pass 的 7 张卡、寻找首轮漏判。
> **执行**：lead，13:10–13:22（Asia/Shanghai）。**结论**：新增 1 条 minor（sy0238）、1 处定位补强（ggl09），无新增 major/critical。

## 1. 复核口径

- **页码**：siebert/ggl08/benzvi_glc/glc/ggl09 的 PDF 页 = 印刷页；kw06/gw06 PDF = 印刷 + 1；gtgl15 PDF = 印刷 + 2；lbook04 ch9 +3、ch3 +7。
- **证据**：不拿 `fix_log.json` 的 `why` 当证据；每条引文都从一手 PDF 抽文本（`%TEMP%/cardverify/<set>.txt`，按 `\f` 分页；lbook04 用原书 PDF）或源码批注重新取，再与卡上字段逐字比对。
- **判定**：`fix-confirmed`（原 issue 的 after 值正确）/ `pass`（首轮 pass 复核后维持）/ `issue`（新发现或改判）/ `unverifiable`（仍缺一手源）。

## 2. 20 张逐卡矩阵

| n | 卡片 | 首轮 | 复审 | 复核点（一手证据） | 处理 |
|---|---|---|---|---|---|
| 1 | `siebert/correction/prop-3-12-lci` | issue | fix-confirmed | p.50 有 `Definition 3.4.` 与 `(3.58) ι![V] := s∗0[C_W/V]`；p.51 有 `(3.64)`；p.58 有 `Proposition 3.12. If S is lci, …` | 保留 after `p.50–51` |
| 2 | `ggl08/deriv/anomaly-inflow-on-the-fixed-surface` | pass | pass | p.15 (5.2)、p.16 (5.3)、p.17 (5.4) `df=2πδ_W` 与 (5.5) `ΔI→ΔI−i∫_W X2` 逐字命中 | 无 |
| 3 | `gtgl15/concept/eigenbranes` | issue | fix-confirmed | PDF 39（页眉 37）`LB = B ⊗ V (4.3) for some vector space V`、`that appears in this definition`；Eq (4.3) 是定义，不是定理 | 保留 `theorems: []` |
| 4 | `kw/concept/n4-sym-theory` | issue | fix-confirmed | PDF 11 页脚 `10`，`(2.14) (2,1,4) ⊕ (1,2,4)` 在该页；PDF 12 页脚 `11` 为 `(2.15)` | 保留 `B p.7–10` |
| 5 | `functoriality/concept/strip-shrinking` | issue | fix-confirmed | p.27 页脚 27：`(62) HF*(L0;L01;L12;L2) ≃ HF*(L0;L01∘L12;L2)`；p.28：`[WW15, Theorem 5.1] … shrinking a strip or annulus … invariants coincide` | 保留 `p.27` / `p.28` |
| 6 | `ggl09/deriv/descent-to-xi` | issue | fix-confirmed + 定位补强 | p.16–17：右边界（Dirichlet）`xi(S) vanishes`；左边界（Neumann）`no reason for xi(S) to vanish`；`difference between the left and right boundaries … is homologous to a small two-sphere` | text 已改；locator 扩为 `A p.16–17` |
| 7 | `dmod/concept/holonomic-defect` | pass | pass | PDF 125（页眉 119）`holdef_x(V)=dim_{p_X^{-1}(x)}Ch(V)−dim_x X`、`6.9. Corollary`；PDF 57（页眉 51）`12.6. Theorem (Kashiwara)`、`13. Preservation of holonomicity` | 无 |
| 8 | `sy38/concept/tamagawa-number` | pass | **issue（改判）** | 卡把 Weil 猜想的完成者写成不存在的「Lai–Künnemann」；一手 Anschütz p.7 只给 τ 定义与 τ(SL_n)=1，史实为 Langlands（分裂）→ Rapoport/Lai（拟分裂）→ Kottwitz 1988（数域一般） | 已改 `key_points[1]`，minor |
| 9 | `functoriality/concept/mww-functor` | pass | pass | p.21 `A∞-functor` (49)、`Theorem 3.7 … homotopy of A∞-functors` (50) | 无 |
| 10 | `kshms/remark/rmk-21-truncated-theta` | pass | pass | PDF 59 顶部 `Remark 21 If we endow the torus Y = Rn/Zn …` 逐字；§9 标题紧随其后 | 无 |
| 11 | `dmod/concept/deligne-regular-singular` | pass | pass（源码级） | PDF 146（页眉 140）为 §4 末，正文无 `regular singular`；卡所引是 `chap5.tex:274-276` 的 `annote`（Deligne 正则奇点必有解）与 `chap1.tex:1894-1896`，卡已说明「讲义只以批注陈述、未给证明」 | 无 |
| 12 | `siebert/concept/gromov-witten-invariant` | issue | fix-confirmed | p.58 `Proposition 3.12. If S is lci, then for all s, s′ …`；不是「连通基底」 | 保留 `lci` |
| 13 | `lbook04/concept/ch9-langlands-spectral` | issue | fix-confirmed | 原书 PDF 225（页眉 222）`Theorem 4.2 … at most simple poles … at s = -iσ and s = 1 - iσ`；两条 observation 是未扭 `L(s, π×π̃)` | 保留 `s=−iσ / s=1−iσ` |
| 14 | `lbook04/concept/ch3-three-motives` | issue | fix-confirmed | PDF 46（页眉 39）为 §2 起；PDF 49（页眉 42）`Example 2.1. The Weierstrass p-function`；PDF 50（页眉 43）`Gk(Λ)` 与 §3 | 保留 `pages [39,43]` / `pdf_pages [46,50]` |
| 15 | `seidel/concept/exact-lagrangian` | unverifiable | unverifiable | 仍缺 Seidel《Fukaya Categories and Picard–Lefschetz Theory》原书 PDF；卡内 Stokes 论证自洽 | 维持 |
| 16 | `kshms/concept/prp-10-analytic-hms` | pass | pass | PDF 52 `Proposition 10 The category C(Y) is A∞-equivalent to D^b_{A∞}(Y) …`；§8 起于 p.52 | 无 |
| 17 | `bzg/concept/categorical-fourier` | issue | fix-confirmed | PDF 6（§1.3）`This fits in a general theme of categorical Fourier transforms`；PDF 8（§2.1）是 `categories as analogues of Hilbert spaces`，全文无 `FM_K(F)=p_{Y!}(p_X^*F⊗K)` | 保留 §1.3 / p.6 |
| 18 | `kw/concept/cohomology` | pass | pass | PDF 19（页脚 18）`the interesting operators or states lie in suitable cohomology groups of Q`；PDF 28（页脚 27）`cohomological field theories [59] …` | 无 |
| 19 | `gw06/concept/two-dimensional-defect` | issue | fix-confirmed | PDF 32（印刷 31）`The finite groups Z(G) and Hom(π1(G), U(1)) are exchanged by duality … discrete versions of α and η are exchanged` | 保留 `pages [29,31]` |
| 20 | `glc/concept/fundamental-local-equivalence` | issue | fix-confirmed | p.72 `Localization should enhance to a relative construction`、`Op_Ǧ(X \ {x})^unr := …` | 保留 `pages [71,72]` |

> 引文机械核验：ggl08 的 5 条 `sources[].quote`、ggl09 的 4 条、sy0238 的 2 条，去空白后均为所声称 PDF 页文本的子串（BAD=0）。其余卡的字段没有独立 `quote`，按上表逐条人工比对。

## 3. 复审发现

### 3.1 改判：sy0238 玉河数的历史归属（minor）

- **卡上原文**（`key_points[1]`）：「$\tau(\mathrm{SL}_n)=1$ 属于 Weil 猜想的一类情形（Langlands 证 $\mathrm{SL}_2$，一般情形后来由 Lai–Kunnemann 等完成）…」
- **问题**：公开文献中没有「Lai–Künnemann」这条完成链。Weil 猜想（单连通半单群的 Tamagawa 数 = 1）的标准史实是：Langlands（1966）证数域分裂情形，Rapoport（1976）与 Lai（1980）推广到拟分裂情形，Kottwitz（1988，Annals 127）用 Arthur 迹公式完成数域一般情形；函数域情形后由 Gaitsgory–Lurie（2019）解决。Künnemann 的公开著作目录以 Arakelov 几何为主，未见 Tamagawa 数工作。
- **证据**：Lurie, *Tamagawa Numbers via Nonabelian Poincaré Duality* 课程大纲「proven by Kottwitz (building on earlier work of Langlands and Lai)」；Pacific J. Math. 338 (2025) 综述「split … by Langlands [1966] … quasisplit … by Rapoport [1976] and Lai [1980] … Kottwitz [1988] proved Weil's conjecture over number fields」；Kottwitz, Ann. of Math. 127 (1988), 629–646。
- **定级**：minor。τ 的定义、体积公式与卡的主断言不受影响，错的是历史归属（且把两个人名拼成了不存在的合作者）。
- **首轮为何漏**：首轮 `notes` 已写「Lai–Künnemann 无法核实」，但把「本地一手源 p.7 不讲历史」当成 pass 的理由；本轮改用外部文献链交叉核对，才把「无法核实」升级为「可证伪」。
- **修复**：`key_points[1]` 改为「…Langlands 证分裂情形，Rapoport 与 Lai 推广到拟分裂情形，Kottwitz（1988）用 Arthur 迹公式完成数域一般情形…」。

### 3.2 补强：ggl09 第 5 步的 locator（同一 issue 的定位面）

- 首轮 issue 只记 `steps[4].text` 的方向错误；该步改写后覆盖 p.16–17 的边界论证，但 `locator` 仍写 `A p.16 eq (2.10)`。
- p.16 是 `x_i(S)` 的定义与固定时刻曲面，左/右边界与小 S² 的同调论证在 p.17；locator 与正文不匹配，本轮扩为 `A p.16–17 eq (2.10)`。
- 不改数学结论，计入同一张卡的第二处改动（案例 D27-05 §1.2）。

## 4. 结论

- 20 张样本：**12 张有 issue、7 张 pass、1 张 unverifiable**（首轮为 11 / 8 / 1）。
- issue 总数 **13 条**：critical 0、major 3、minor 10（新增 sy0238 minor）。
- 12 张卡共 **25 处字段级改动**；25 处 after 均已回到一手页码复核，`fix_log.json` 的 before 均已从当前卡片消失。
- 首轮 8 张 pass 中 7 张维持；sy0238 改判，ggl09 增补定位。没有发现新的 major/critical。
- `daily_verify/2026-11-27/ledger.jsonl` 保留首轮 20 行原判（历史记录）；本轮最终状态以 `round2/records_round2.jsonl` 与本文件为准，`SUMMARY.md` 已追加复审节。

## 5. 复跑

```bash
python 11_card_audit/daily_verify/2026-11-27/round2/check_round2.py --source index
# --source index：校验 git 暂存区（本次 commit 的内容），不受并行工作树改动影响
python datasets/_audit/third_party_2026-11-26/tools/verify_final.py
python 11_card_audit/tools/check_casebook.py
git diff --check
```
