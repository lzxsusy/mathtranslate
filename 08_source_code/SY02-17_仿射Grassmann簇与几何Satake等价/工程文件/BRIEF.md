# BRIEF · SY02-17《仿射 Grassmann 簇与几何 Satake 等价》

## 原文

| 项 | 内容 |
| --- | --- |
| 原题 | An introduction to affine Grassmannians and the geometric Satake equivalence |
| 作者 | Xinwen Zhu（朱歆文） |
| 性质 | 2015 年 PCMI 暑期学校（Park City，专题「几何朗兰兹纲领与自守形式」）五次讲座的讲义，后经扩充收入 *IAS/Park City Mathematics Series* 第 24 卷（2017），pp. 59–154 |
| 底本 | arXiv:1603.05593（2016），95 页 |
| 版本 | 扩充版；源文件 `工程文件/work/原文/main.tex`（4870 行，含 `pcmi.cls` 等 9 个附属文件） |
| 结构 | 引言（§0）＋第一至第五讲（§1–§5）＋附录 A（层论补充，A.1 等变反常层、A.2 ULA） |

**原文性质。** 这是讲义体，不是综述：每条定义、每个定理都给出（或勾勒）证明，且大量构造（归纳概形、BD Grassmann 簇、Ran 空间、半无限轨道）在后续文献中被直接引用。原文把定理类与公式挂在同一个计数器上，按节编号（PCMI 体例），故出现「Definition 1.1.1、Theorem 1.1.3、公式 (1.1.4)、Lemma 1.1.5」这样的混排。译文必须复现这一体制。

## 一句话主旨

把「仿射 Grassmann 簇上的反常层」这一几何对象，做成与 Langlands 对偶群的表示范畴等价（几何 Satake 等价），并为整个几何朗兰兹纲领提供局部基石。

## 五步逻辑链

1. **造空间**：仿射 Grassmann 簇 $\Gr_G=LG/L^+G$ 是归纳概形，$G=\GL_n$ 时可用格给出模解释（§1）。
2. **造几何**：Schubert 簇、对偶 Schubert 簇、横截片、Picard 群、中心扩张与仿射 Kac–Moody 代数（§2）。
3. **造族**：Beilinson–Drinfeld Grassmann 簇把 $\Gr$ 的参数化到曲线 $X$ 上，获得分解结构，从而把卷积积解释为融合积（§3、§5.4）。
4. **造应用**：单点单值化、线丛与共形块、adèle 单值化（§4）。
5. **造等价**：$\Sat_G=(\on{P}_{L^+G}(\Gr),\star)$ 是中性 Tannaka 范畴，其 Tannaka 群就是 $\hat G$（MV 理论 + 半无限轨道），于是 $\Sat_G\simeq\on{Rep}(\hat G)$；再自举到 ${}^LG$ 与多重点版本（§5）。

## 分块表

| 块 | 节 | 原文行 | 译本页 | 目标文件 | 状态 |
| --- | --- | --- | --- | --- | --- |
| ch00 | 引言 §0 | 555–726 | 4–9 | `chunks/ch00.tex` | 完成 |
| ch01 | §1.1–§1.2 | 727–908 | 9–11 | `chunks/ch01.tex` | 完成 |
| ch02 | §1.3 | 909–1032 | 11–14 | `chunks/ch02.tex` | 完成 |
| ch03 | §1.4–§1.5 | 1033–1191 | 14–18 | `chunks/ch03.tex` | 完成 |
| ch04 | §1.6–§1.7 | 1192–1254 | 18–21 | `chunks/ch04.tex` | 完成 |
| ch05 | 第二讲 §2.1 | 1255–1466 | 22–28 | `chunks/ch05.tex` | 完成 |
| ch06 | §2.2–§2.3 | 1467–1651 | 28–32 | `chunks/ch06.tex` | 完成 |
| ch07 | §2.4–§2.5 | 1652–1765 | 32–35 | `chunks/ch07.tex` | 完成 |
| ch08 | 第三讲 §3.1 | 1766–2013 | 35–40 | `chunks/ch08.tex` | 完成 |
| ch09 | §3.2–§3.4 | 2014–2194 | 40–46 | `chunks/ch09.tex` | 完成 |
| ch10 | 第四讲 §4.1–§4.2 | 2195–2292 | 46–48 | `chunks/ch10.tex` | 完成 |
| ch11 | §4.3 | 2293–2457 | 48–53 | `chunks/ch11.tex` | 完成 |
| ch12 | 第五讲 §5.1–§5.2 | 2470–2643 | 53–57 | `chunks/ch12.tex` | 完成 |
| ch13 | §5.3 | 2644–2929 | 57–64 | `chunks/ch13.tex` | 完成 |
| ch14 | §5.4 | 2930–3074 | 64–68 | `chunks/ch14.tex` | 完成 |
| ch15 | §5.5 | 3075–3320 | 68–74 | `chunks/ch15.tex` | 完成 |
| ch16 | §5.6 | 3321–3402 | 74–76 | `chunks/ch16.tex` | 完成 |
| ch17 | 附录 A.1 | 3405–3537 | 76–78 | `chunks/ch17.tex` | 完成 |
| ch18 | 附录 A.2 | 3538–3700 | 78–79 | `chunks/ch18.tex` | 完成 |
| ch19–ch20 | 空（内容并入 ch18） | — | — | `chunks/ch19.tex`、`chunks/ch20.tex` | 占位 |
| ch21 | 参考文献 | 3700–4868（amsrefs 源） | 80–89 | `chunks/ch21.tex` | 完成（82 条） |

> **v1.1（2026-11-25）**：全文校订 + 17 条译注后共 **90 页**（v1.0 为 89 页）。上表「译本页」仍是 v1.0 页码，误差 ≤1 页；本轮未增删定理与公式（仍 212 个定理环境、220 条显示公式），故编号索引不变。校订明细见 `reports/校订报告_R2_2026-11-25.md`。

## 施工流程（每块）

1. 读原文该行段，逐句核符号；2. 译成中文，编号一律 `\ref`/`\eqref`，label 沿用原文；3. `cd 源码 && xelatex -interaction=nonstopmode main.tex` 跑两遍；4. 过滤 `^!`／`Missing character`／`Overfull`；5. `scripts/render.py` 渲染该块首页目视核对；6. 在 `工程文件/reports/` 记该块报告。

## 纪律与已知坑

- **编号体制必须复现**：`\numberwithin{equation}{subsection}` 且全部定理环境挂 `[equation]`（共用计数器），否则 Definition 1.1.1／Theorem 1.1.3／(1.1.4) 的混排会全错。
- 定理环境名是 `dfn`（不是 `defn`）、`conj`（不是 `conjecture`）。
- amscd 箭头标注里写中文会缺字，须 `@V{\text{拉回}}VV`；tikz-cd 不可留空格子，三角图改用 plain tikz。
- 本机 `pymupdf`/`pdftotext` 抽不出本译本 PDF 的中文（`Unknown font tag 'F7'`），PDF 端自动编号对账不可用；改用**标签集合对账**（见 `work/label_check.txt`）。
- 目录里 `参考文献` 需手工 `\clearpage\phantomsection\addcontentsline`。
- **译注机制**：`\zy{…}`（`manyfoot`，印作「译1、译2…」独立序列）与作者 `\footnote` 并行不冲突；每条译注必须带 `[来源：…]` 或 `[译者按`。现有 17 条，见 `资料卡/05-卡点与nLab批注.md`。
- **`\usepackage{xurl}` 不可删**（在 preamble 的 hyperref 之后）：译注里的 nLab 永久链接很长，缺了它会新增 Underfull/溢出风险。
- 原文笔误两类处理：实质错误（如 §1.3 的 $\pi_0(G)$）**加译注并登记疑点清单**，不静默改；纯记号漏字（如 §5.6 的 $(A_2)$）直接补正并登记 `work/typos.txt`。
