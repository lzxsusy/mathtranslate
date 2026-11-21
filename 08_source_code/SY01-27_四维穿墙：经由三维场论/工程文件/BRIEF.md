# BRIEF —— GMN1《Four-dimensional wall-crossing via three-dimensional field theory》中译

- 原文：arXiv:0807.4723v3，66 页，LaTeX 源 `00_原文/GMN1_0807.4723/0807.4723v3_src/wcf-paper.tex`（4051 行）
- 作者：Davide Gaiotto, Gregory W. Moore, Andrew Neitzke（IAS / Rutgers, 2009）
- 译名：**《四维穿墙：经由三维场论》**
- 工程根：`C:\Users\admin\Desktop\GMN系列\01_翻译\GMN1_0807.4723\`

## 一、这篇文章在讲什么（给没读过原文的人）

**一句话**：用「把 4d N=2 理论放到 R³×S¹ 上」的办法，把 Kontsevich–Soibelman（KS）穿墙公式解释成一句物理上显然的话——三维低能有效理论（超凯勒靶空间上的 sigma 模型）的度量必须连续。

**逻辑链**（五步，任何一节译文都不能与它冲突）：

1. 4d N=2 的库仑分支 $\mathcal{B}$ 上有电荷格 $\Gamma$、中心荷 $Z_\gamma(u)$、BPS 简并度 $\Omega(\gamma;u)$；跨边缘稳定墙时 $\Omega$ 跳变，跳变规律由 KS 公式给出。
2. 该理论放到 $\mathbb{R}^3\times S^1$（半径 $R$）上，低能是 3d sigma 模型，靶空间 $(\mathcal{M},g)$ 超凯勒，$\mathcal{M}$ 拓扑上是 $\mathcal{B}$ 上的 Seiberg–Witten 环面丛。
3. $R\to\infty$ 时 $g\to g^{\rm sf}$（半平坦度量，由朴素量纲约化得到）；BPS 粒子绕 $S^1$ 缠绕形成「瞬子」，给 $g$ 带来 $e^{-2\pi R|Z|}$ 量级的修正。
4. 度量的连续性 ⇔ 单瞬子贡献的跳变恰被多瞬子贡献的跳变补偿 ⇔ KS 穿墙公式。
5. 反向：由「平坦的类 $tt^*$ 联络存在」这一超对称场论一般原理，反推出 $g$ 的性质，从而证明 WCF。

**技术内核**（第 3、5 节，全文最难）：
- 超凯勒流形对一整族复结构 $J^{(\zeta)}$（$\zeta\in\mathbb{CP}^1$）都是复辛的；研究 $g$ ⇔ 研究**全纯达布坐标** $X_\gamma(u,\theta;\zeta)$。
- $X_\gamma$ 关于 $\zeta$ **分段**全纯；不连续性出现在 $\zeta$ 平面中由 $\arg Z_\gamma$ 决定的射线上，跳变算子是 KS 辛同胚 $K_\gamma$。
- 用「$\zeta\to0,\infty$ 的渐近（由 $X^{\rm sf}_\gamma$ 定）+ 射线跳变」构成**无穷维黎曼–希尔伯特问题**；大 $R$ 下逐次逼近求解。
- 对 $U(1)$+单超多重态（第 4 节）有精确解（Ooguri–Seiberg 度量）可对照。

**读者定位**：懂 4d N=2 / Seiberg–Witten 的数学物理读者；中文数学界对「穿墙」一词已熟悉（数译全库 83 处）。

## 二、分块与页映射（PDF 页，按 0807.4723v3）

| 块 | 内容 | 页 | 原文行号（wcf-paper.tex） | 状态 |
|---|---|---|---|---|
| ch01 | §1 Introduction and Summary | 3–7 | 199–555 | ✅ 初稿（样板） |
| ch02 | §2 Preliminaries（2.1 规范理论 / 2.2 KS 公式 / 2.3 R³×S¹ 低能 / 2.4 半平坦几何） | 8–17 | 559–1164 | ✅ 已译（37 式） |
| ch03 | §3 A twistorial construction of hk metrics | 18–21 | 1165–1388 | ✅ 已译（19 式） |
| ch04 | §4 Mutually local corrections（4.1–4.7） | 22–34 | 1389–2128 | ✅ 已译（85 式含子编号） |
| ch05 | §5 Mutually non-local corrections（5.1–5.7，拆 ch05a/ch05b） | 35–46 | 2129–3001 | ✅ 已译（56 式） |
| ch06 | §6 Adding masses | 47–49 | 3002–3152 | ✅ 已译（13 式） |
| ch07 | §7 A proof of the wall-crossing formula | 50 | 3153–3222 | ✅ 已译（1 式） |
| — | 致谢 | 50 | 3223–3239 | ✅ 随 ch07 |
| appA | 附录 A Verifying the KS identity for some SU(2) theories | 51–55 | 3242–3394 | ✅ 已译（13 式） |
| appB | 附录 B Cauchy–Riemann equations on M | 56–57 | 3395–3528 | ✅ 已译（17 式） |
| appC | 附录 C Asymptotics of integral equations（拆 appC1/appC2） | 57–61 | 3529–3822 | ✅ 已译（28 式） |
| appD | 附录 D Asymptotics of differential equations | 61–62 | 3823–3899 | ✅ 已译（14 式） |
| appE | 附录 E A relation to the Thermodynamic Bethe Ansatz | 62–66 | 3900–4051 | ✅ 已译（11 式） |

**注意**：本文**没有任何 theorem/proposition 环境**（全文 grep 计数 0）。结果一律以编号公式和节内陈述出现。因此：
- 译文**不要**擅自给结论套「定理」环境；
- 资料卡的「结果清单」按「编号公式 + 所在节」组织，不按定理编号。

## 三、施工流程（每一块都照此走）

1. **通读原文**：读对应行号整段，不看译文先读懂；卡住的地方记进 `work/02_疑点清单.md`。
2. **对术语**：查 `04_共享/术语/glossary_master.tsv` 与本篇 `work/gmn1_glossary.tsv`；缺的补上（含依据）。
3. **落笔**：写到 `源码/chunks/chNN.tex`，公式逐字符回原文核对（尤其 $\pm$、上下标、$\zeta$ 与 $\bar\zeta$、$R$ 与 $R^{-1}$）。
4. **编译**：`build.ps1`（xelatex 三遍），要求 0 error、0 overfull > 3pt。
5. **自检**：段数对得上？公式编号连续？有没有漏译脚注/括号内短语？译注只在真有歧义处加。
6. **记账**：更新本文件页映射状态、`进度.md`、`04_共享/进度/GMN1_台账.md`。

## 四、质量标准（不可让步）

- **忠实**：不增删论点；原文的「we expect / it would be interesting / we do not understand」这类语气必须原样保留，不许升格为断言。
- **公式**：编号、符号、量纲全部与原文一致；引用公式时用原文编号（如 (2.18)）。
- **术语**：全库统一（见 STYLE_GUIDE 的硬性表）；新术语入表后才用。
- **中文**：可读的中文数学文风——长句拆开、少用「的的」、避免英式从句堆叠；专名保留原文。
- **译注**：只在「读者按字面会误解」处加，用 `yizhu` 环境或 `\zy{}`；不加读书心得。

## 五、交付物

- `成品/GMN1_四维穿墙_全文中译_v1.0.pdf`（合稿后）
- `资料卡/` 五件套（00-速览 / 01-结果清单 / 02-论证地图 / 03-条款索引 / 04-术语文献勘误）
- 本目录下的台账与施工记录

## 六、已知坑

- `\degen` 在原文里就是 $\Omega$（`\newcommand\degen{\Omega}`），别误当独立符号。
- 原文用 `\vm` 表示 4d 模空间 $\mathcal{B}$，用 `\CM` 表示 3d 模空间 $\mathcal{M}$——中文极易混，译文固定写「$\mathcal{B}$（4d 模空间）」「$\mathcal{M}$（3d 模空间）」首次出现时标注。
- §2.2 与附录 A 里 KS 公式的**符号约定**（$T$ vs $\tilde T$）是全文最容易译错的地方，原文自己也在 §1 末尾提醒读者可以「混为一谈」。
- 原文公式按节编号（(1.1)、(2.18)…），译文用 `\numberwithin{equation}{section}` 复现；跨节引用目前硬编码数字，合稿时统一换 `\eqref`。
