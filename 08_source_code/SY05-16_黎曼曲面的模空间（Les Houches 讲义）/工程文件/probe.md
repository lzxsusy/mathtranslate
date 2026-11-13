# probe.md — 能力探测 + 底本尽职调查报告

> 生成时间：2026-11-03 | 探测人：Lead | 全部为**实测**结果，无推断。

## A. 环境能力（实测）

| 项目 | 结论 | 证据 |
|---|---|---|
| TeX 工具链 | **有**，TeX Live 2026 | `G:\texlive\2026\bin\windows\xelatex.exe`，`--version` → XeTeX 3.141592653-2.6-0.999998 (TeX Live 2026)，kpathsea 6.4.2 |
| PATH 里有没有 | **没有** | `where.exe xelatex` → INFO: Could not find。**必须用绝对路径 G:\texlive\2026\bin\windows\xelatex.exe** |
| 冒烟测试 1（英文+公式出 PDF） | **通过** | smoke/t1.pdf 30 605 字节，1 页 |
| 冒烟测试 2（ctexart 中文排版） | **通过** | 同上，simsun.ttc 正常，无缺字报错 |
| 中文字体 | 可用（Path 显式指定） | C:/Windows/Fonts/simsun.ttc + simhei.ttf + simkai.ttf，**不用 fontconfig** |
| TMP | 已设为 workspace\tmp，正常 | 无 `-1073740777` 事故 |
| Python | 有，**不是** WindowsApps 那份 | `<本地路径>`（3.12.14）。PATH 上的 `python.exe` 是 0 字节 App Execution Alias，**不可用** |
| PDF 库 | PyMuPDF 2.0 | `import pymupdf` OK；`fitz` 已弃用 |
| 写权限 | 全开（danger-full-access） | workspace = `<本地路径>` |
| 控制台编码 | GBK | 打印中文/数学符号会 `UnicodeEncodeError` → **一律设 `$env:PYTHONIOENCODING='utf-8'`，或只写文件不 print** |

## B. 底本尽职调查（Deck Check，实测）

| 检查项 | 实测值 |
|---|---|
| 文件 | `<本地路径>`，1 848 139 B，PDF 1.7 |
| 真实标题 | **Les Houches lecture notes on moduli spaces of Riemann surfaces** |
| 真实作者 | **Alessandro Giacchetto; Danilo Lewański** |
| 标识 | arXiv:2410.13273v2 [math.AG], 27 Feb 2026 |
| 总页数 | **46**（PDF p.1–46） |
| PDF 页号 vs 印刷页码 | **偏移 = 0**（PDF p.N = 印刷页 N；封面即第 1 页，页脚印 1）。已用 PDF p.2 = "1. Introduction" 与目录 p.2 交叉验证 |
| 位图数量 | **1**（仅 p.7，一张图）|
| 矢量绘图 | 1530 条（绝大多数是分式横线；真实插图 15 幅，见下） |
| 图 | **15 幅**：Fig 1 p2 / Fig 2 p4 / Fig 3 p6 / Fig 4 p7 / Fig 5 p9 / Fig 6 p9 / Fig 7 p11 / Fig 8 p11 / Fig 9 p12 / Fig 10 p13 / Fig 11 p13 / Fig 12 p18 / Fig 13 p24 / Fig 14 p25 / Fig 15 p39 |
| 表 | **3 张**：Table 1 p23（ψ 类相交数）/ Table 2 p37（CohFT ↔ 拓扑递归对应）/ Table 3 p41（Weil–Petersson 多项式 VWP） |
| 附录 | **无** |
| 参考文献 | p.43–46（`\section*{References}`）|
| 致谢 | p.3（Acknowledgements + Funding information）|
| 编号公式 | **155 条唯一编号**（原始 `(x.y)` 文本命中 176 次，多出的 21 次是正文里的交叉引用） |
| 公式编号分布 | §1: 2（1.1–1.2）／§2: 79（2.1–2.79）／§3: 60（3.1–3.60）／§4: 14（4.1–4.14） |
| 编号环境 | **35 处**：Definition 2.1,2.3,3.1,3.3,3.5 ／ Theorem 2.2,2.4,2.6,3.7,3.8,3.9,4.1,4.2,4.3 ／ Proposition 3.4,3.6 ／ Example 3.2 ／ Exercise 2.1–2.11, 3.1–3.5, 4.1 |
| 链接 | 40 页有内部/外部链接（目录、参考文献 arXiv/doi 链接）|
| 脚注 | 无独立脚注文本（原文用方括号内联注）|
| 章节结构 | 1 Introduction(p2)｜2 Moduli spaces(p4): 2.1 p4, 2.2 p10, 2.3 p16｜3 CohFT(p27): 3.1 p27, 3.2 p31, 3.3 p35｜4 Further directions(p38): 4.1 p38, 4.2 p41｜References p43 |
| 文字层可靠度 | 正文英文单词/段落可信；**数学完全不可信**（矩阵被拆成单字符行、分式上下颠倒、`\mathcal` 丢失、`\overline` 丢失）。例：p16 的 (2.37) 文字层把映射链打散成 6 行。**公式一律以 200 dpi 页面图为准** |

## C. 结论与路线

1. 直接用 `G:\texlive\2026\bin\windows\xelatex.exe`，**不安装任何东西**，不改 PATH。
2. 46 页 / 155 公式 / 15 图 / 3 表 → 9 个块（Lead + 8 队友）。
3. 图**不重画**（原文为 TikZ/矢量插图，重画即伪造）；图注照译并以"〔原文图 N 从略：…〕"标记；表**照抄重排**（表中原有数据，属翻译不属造表）。
4. 验收三重：check.py（静态 7 项）→ build2.py（真编译 4 项）→ verify_pdf.py（成品回读：155/155 公式编号 + 35 处环境编号序列 + 字体嵌入 + 抽页目视）。
