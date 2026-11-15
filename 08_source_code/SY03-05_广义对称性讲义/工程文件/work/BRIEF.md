# BRIEF —— 分工与接续点（Lead 维护；开工前必读）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，保留权利，仅限非商业学术研读，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

## 项目
把 *Lectures on Generalized Symmetries*（arXiv:2307.07547v2，150 页；正文 pp.1–138）译成中文 LaTeX 译注本，
公式无损（745 条编号公式）、结构化、带学术批注，由 Lead 合成单文件 PDF。
pp.139–150 的致谢 + 221 条参考文献不译（Lead 另行处理，参考文献保留英文）。

## 硬性流程（每位译者）
1. 读 `work/STYLE_GUIDE.md`（全文，必须）→ `work/glossary.tsv` → 本 BRIEF 中你的一段。
2. 读你的 `work/split/pNNN.txt` 把握论证结构与段落（**文字层只用来定位**）。
3. **逐页看 `work/pages/pNNN.png`**（`read_image`），公式逐符号抄成 LaTeX；看不清用 `work/tools/crop.py` 裁局部放大。
4. 写 `work/src/chunks/trNN{a,b,c}.tex`（UTF-8 无 BOM、LF；a→b→c 顺序拼接；每片约 5–6 页）。
5. 逐项过 STYLE_GUIDE §12 自检 → `send_message` 给 lead 回执（5 项格式）。

## 绝对路径速查
- 项目根：`<本地路径>`
- 工作区：`...\work`（pages/ split/ figures/ tags.txt tags_bypage.txt glossary.tsv STYLE_GUIDE.md BRIEF.md TIMELINE.md）
- 输出目录：`...\work\src\chunks\`
- 原 PDF：`<本地路径>`
- Python（crop.py 用）：`<本地路径>`

## 九块分工（页码 = PDF 页 = 印刷页，偏移 0；tag 区间必须首尾接上邻居）

| 块 | 负责人 | 页段 | 负责内容（含你负责写的标题） | tag 区间 | 图/表 | 输出 |
|---|---|---|---|---|---|---|
| L | **lead** | 1–12 | 标题页/摘要/目录；**§1 引言**；**§2 标题**（p5）；**2.1 0-Form Symmetries**（p6）；**2.2 Higher-Form Symmetries + 2.2.1 General Properties**（p12 页末） | 2.1–2.37 | fig1(p7), fig2(p9), fig3(p11) | c00,c01 |
| 1 | **tr-01** | 13–28 | 2.1 续完；**2.2 Higher-Form Symmetries**、**2.2.1 General Properties**、**2.2.2 Action of p-Form Symmetries**、**2.3 Discrete (Higher-Form) Gauge Theories**；**§3 标题** + **3.1 Screening of Extended Operators**（p.26 页末，标题由你写，正文由 tr-02 续） | 2.38–3.6 | fig4(p15), fig5(p18), fig6(p19), fig7(p27), fig8(p28) | tr01a/b/c |
| 2 | **tr-02** | 29–44 | 3.1 续（无标题，直接续写）；**3.2 Abelian Gauge Theories** + **3.2.1–3.2.5**；**3.3 Non-Abelian Gauge Theories** + **3.3.1 Pure SU(2) Yang-Mills Theory**、**3.3.2 Pure SO(3) Yang-Mills Theory**（p.44 标题） | 3.7–3.107 | fig9(p30), fig10+fig11(p43) | tr02a/b/c |
| 3 | **tr-03** | 45–60 | 3.3.2 续；**3.3.3 Pure Yang-Mills Theory with General Gauge Group**、**3.3.4 Including Matter Fields**、**3.3.5 Multiple Gauge Group Factors**；**3.4 Discrete Theta Angle in 4d Gauge Theories** + **3.4.1**、**3.4.2**；**§4 标题** + **4.1 Background Fields**（p.60） | 3.108–4.2 | **Table 1 (p47)** | tr03a/b/c |
| 4 | **tr-04** | 61–76 | 4.1 续；**4.2 't Hooft Anomalies and SPT Phases** + **4.2.1 Basics of 't Hooft Anomalies**、**4.2.2 SPT Phases**（p.74） | 4.3–4.78 | fig12(p65), fig13(p69), fig14+fig15(p71), fig16(p73) | tr04a/b/c |
| 5 | **tr-05** | 77–92 | 4.2.2 续；**4.2.3 Anomaly Theory and Anomaly Polynomial**、**4.2.4 Mixed 't Hooft Anomaly for a Non-Abelian Gauge Theory**；**4.3 Gauging** + **4.3.1 Definition**、**4.3.2 Discrete Torsion**、**4.3.3 Dual Symmetries Obtained After Gauging**、**4.3.4 Gauging Exchanges Twisted and Charged Sectors** | 4.79–4.184 | fig17(p78), fig18(p91), fig19(p92) | tr05a/b/c |
| 6 | **tr-06** | 93–108 | 4.3.4 续；**4.3.5 Gauging Exchanges Mixed 't Hooft Anomalies and Group Extensions**；**4.4 Spontaneous Symmetry Breaking and Confinement** + **4.4.1 General Concepts**、**4.4.2 Example: 4d N=1 SYM Theories with su(2) Gauge Algebra**；**4.5 Symmetry TFTs**（p.108） | 4.185–4.255 | fig20(p98) | tr06a/b/c |
| 7 | **tr-07** | 109–124 | 4.5 续；**§5 Higher-Group Symmetries** + **5.1 Continuous Higher-Group Symmetries**、**5.2 Discrete Higher-Group Symmetries** + **5.2.1 Motivation: Group Extension**、**5.2.2 General Structure**、**5.2.3 Relationship to Mixed 't Hooft Anomalies**、**5.3 Mixed Continuous-Discrete 2-Group Symmetries** + **5.3.1 Global Form of 0-Form Symmetries** | 4.256–5.59 | fig21(p109), fig22(p110), fig23(p111), fig24(p112), fig25(p113), fig26(p118), fig27(p119) | tr07a/b/c |
| 8 | **tr-08** | 125–138 | 5.3.1 续；**5.3.2 Bockstein 2-Group Symmetries**；**§6 Higher-Form Symmetries and String Theory** + **6.1 Higher-Form Symmetries from Geometric Engineering**、**6.2 Generalised Symmetries in Holography** | 5.60–6.54 | fig28(p130) | tr08a/b/c |

> 字数/公式量提示：tr-02、tr-03、tr-05 的编号公式最多（100+ 条），要留足时间；tr-08 页数少但 §6 密度大。

## 边界接续（Lead 已裁决，详见 TIMELINE.md）
- **§ 标题归属**：谁负责该 § 的**起始页**，谁写 `\section{…}`（见上表加粗项）。块内出现的小节标题
  仅当上表写明时由你写；块开头若处于某小节中间，**不要**再写该小节标题，直接续写正文。
- **块首/块尾跨页句**：「开始者写完」——谁开始这句话，谁把它写完；下一块从下一句/下一段开始写。
- **公式编号连续性**：每块 tag 区间首尾相接（见上表）；块内出现的无编号公式照原文排成 `\[…\]`，不得加编号。
- **图/表归属**：按上表，只有列给你的 figure/table 由你写；**table 1** 由 tr-03 手工排版。
- **致谢/参考文献**：Lead 处理。tr-08 写到 p.138 正文结束即可。

## 常见误判提醒
1. 文字层里 `\int`、`\prod`、`\sum`、希腊字母、上下标几乎必然错；**只信图像**。
2. 原文大量公式**没有编号**；`tags_bypage.txt` 里同一 tag 在一页出现两次的多是行文引用，不是新公式。
3. 彩色方框要照译（见 STYLE_GUIDE §7）：蓝色 Statement、绿色 Definition、粉色带标题注释框、无标题框。
4. 原文的 "**[粗体小标题].**" 是行内小标题 → `\para{…}`。
5. 术语统一：先查 `glossary.tsv`；新词自己定译法后回报 Lead，由 Lead 汇总并回写。
6. 图注、公式号、小节号全部**照抄原文数字**；不要重排编号。
