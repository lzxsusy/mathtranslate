# BRIEF · SY02-19《几何朗兰兹的一个算术应用》

## 一、原文

| 项 | 内容 |
|---|---|
| 作者 | Sam Raskin（Yale University） |
| 标题 | *An arithmetic application of geometric Langlands* |
| 出处 | Proc. Sympos. Pure Math. **112.1** (2025)，42 页 |
| DOI | 10.1090/pspum/112.1/02062 |
| 底本 | 作者排版 PDF（TexpadTeX，2025-06-05）（工作副本不入库） |
| 体裁 | 研究论文（含完整证明；大量引用 AGKRRV 三篇预印本） |
| 主题 | 几何朗兰兹（AGKRRV 谱分解、受限变差局部系统、shtuka）在函数域算术朗兰兹上的应用；主结果是"平凡 Langlands 参数处无无分歧尖形式" |

## 二、一句话主旨

把 AGKRRV 的几何朗兰兹谱分解（`IndCoh_Nilp(LS^restr)` 与 `Shv_Nilp(Bun_G)` 的等价、Frobenius 迹）搬到函数域算术侧，通过谱 Eisenstein 级数与 `LS^arthm_Ĝ` 在平凡局部系统附近的 Grothendieck–Springer 型显式坐标，证明分裂半单群在平凡 Langlands 参数处的无分歧尖形式空间为零。

## 三、五步逻辑链

1. **翻译几何–算术**（§2）：`Shv_Nilp(Bun_G) ≃ IndCoh_Nilp(LS^restr_Ĝ)`（Conjecture 2.3.1，restricted GLC），取 Frobenius 迹得 `Aut^unr_{G,c} ≃ Γ(LS^arthm_Ĝ, ω)`（(3.8) 的算术猜想，[4] 主定理）。
2. **造谱侧 Eisenstein**（§3.1、§3.3）：自守侧 `Eis_!` 的迹对应伪 Eisenstein `ps-Eis`；谱侧用对应 `LS^restr_B → LS^restr_T`、`LS^restr_B → LS^restr_Ĝ` 定义 `Eisspec`。
3. **局部化与满射**（§3.5）：构造 `δ_Ĝ`，证明局部化后 `Eisspec` 在 degree 0 且满射（Theorem 3.5.2.1），由此 `ps-Eis` 的像包含 `Aut^unr_{G,c,[triv]}` 中所有尖形式。
4. **显式坐标**（§4.3）：`τ_H: H^ad/H → LS^arthm,∘_H` 在非共振开集上是同构（Theorem 4.3.3.1）；证明用形式 étale + e-点上 1-群胚同构，关键是非共振条件排除 `H°` 的非平凡性。
5. **L-值与玩具模型**（§4.5–4.7）：`δ` 由 `R_X`（Frobenius 在 H¹、H² 上的特征值）定义；用 `ζ*_X(1)^{dim H}`（Lemma 4.6.4.1）比较 `Eisspec` 与 `Eisspec,toy`，玩具模型由 Borel–Weil–Bott 与 Weyl 特征标公式给出满射，从而完成 Theorem 3.5.2.1 的证明，再回代 §3.6 得 Theorem A。

## 四、分块表（按 PDF 页 = 印刷页）

| 块 | 页 | 内容 | 主要编号 |
|---|---|---|---|
| ch00 | 1–4 | 标题、摘要、§1 引言（背景、主定理、动机、约定） | Theorem A, Conjecture 1.3.1 |
| ch02a | 5–9 | §2.1 算术 vs 几何朗兰兹；§2.2 受限变差局部系统 | (2.1)–(2.4), 2.2.6, 2.2.7 |
| ch02b | 9–12 | §2.2 续（Tannaka、一般结构）；§2.3 restricted GLC | Conjecture 2.3.1 |
| ch02c | 12–14 | §2.4 Frobenius 与迹；§2.5 Xue 定理、shtuka | (2.5)–(2.7) |
| ch02d | 14–16 | §2.5 续（Sht^tr、Sht^!） | 2.5.4–2.5.6 |
| ch03a | 16–19 | §3.1 自守 Eisenstein；§3.2 一般构造 | (3.1)–(3.4), Prop 3.1.1.1 |
| ch03b | 19–21 | §3.3 谱 Eisenstein；§3.4 谱 vs 函数论 | Def 3.3.1.1, (3.7), (3.8) |
| ch03c | 21–23 | §3.5 局部化；Theorem 3.5.2.1 | (3.9)–(3.12) |
| ch03d | 23–25 | §3.6 Theorem A 的证明；§3.7 玩具模型 | Lemma 3.7.1.1, Cor 3.7.2.1 |
| ch04a | 25–29 | §4.1 基点与 Weil 群；§4.2 伴随商；§4.3 非共振 | Theorem 4.3.3.1 |
| ch04b | 29–31 | §4.4 Theorem 4.3.3.1 的证明 | Lemma 4.4.1.1, (4.7) |
| ch04c | 31–37 | §4.5 证明 setup；§4.6 L-值与迹（含发散级数插叙） | (4.8)–(4.15), Lemma 4.6.4.1 |
| ch04d | 37–42 | §4.7 结论（Theorem 4.7.2.1）；参考文献 | (4.16)–(4.17) |

## 五、施工流程

1. `scripts/extract_source.py` 抽取 42 页文本与 170 dpi 位图；公式一律对位图核对，文本层只作行文参考。
2. 先写 `work/通读笔记.md`、`work/疑点清单.tsv`、`work/glossary.tsv`（术语冻结）。
3. 逐块翻译：每块先读原文页图，再落 LaTeX；新术语先入 glossary 再用。
4. 每块翻译后编译单块测试（`chunks/chXX.tex` + 临时主文件），0 error 再进下一块。
5. 全稿 xelatex ×3；检查 0 error / 0 Overfull / 0 缺字 / 0 undefined。
6. 双校：术语残留、译注来源、编号对账、公式抽查；写 `reports/ch*.md`。
7. 写 `资料卡/`（速览、结果清单、论证地图、条款索引、术语文献勘误）、`精选片段.md`、`投稿信息.md`。

## 六、纪律与坑

- **公式不可信文本层**：`raw.txt` 的数学上下标、分式、矩阵全被打散（如 `H1´etpX, eq`），必须看页面图。
- **编号**：定理类为"节.小节.子小节.序号"（如 4.3.3.1），用 `\newtheorem{thm}{定理}[subsubsection]`；公式按节编号（(4.7)），用 `\numberwithin{equation}{section}`。
- **术语**：restricted variation 译"受限变差"；restricted GLC 译"受限几何朗兰兹猜想"；unipotent 译"幂幺"；qLisse 保留 `qLisse`；shtuka 保留 `shtuka`；Bun、LS、IndCoh、QCoh、Shv 保留英文缩写。
- **原文笔误**：保留正文并加 `% [Tutor Note: ...]` 与疑点清单登记，不悄悄改。
- **译注来源**：解释性译注必须 `[来源：A/B/I…]`；无外部依据只能 `[译者按（上下文推断，无外部依据）]`。
- **AGKRRV 引用**：[2][3][4] 分别是 arXiv:2010.01906、2012.07665、2102.07906，译文中首次出现时给全称与编号，不展开其内容。
- **无参考文献节？** 原文 pp.38–42 有 References（32 条），但正文引用编号 [1]–[32] 与列表对应；译文照录并核对。
