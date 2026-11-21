# WIT-2021-ATIYAH-LANG：Witten 2021 年 INI 演讲中文译注本

Witten 于 2021 年 9 月 23 日在剑桥 Isaac Newton Institute 所作的演讲
*Duality, the Langlands Correspondence, and the Influence of Michael Atiyah*
（54 张 beamer 幻灯片）的中文译注本。

一句话：**从 1977 年 Atiyah 的一句口头提醒出发，把“电磁对偶”与“几何 Langlands
对应”这两条各自发展了四十余年的线索，串成一条可以按顺序读的故事。**

---

## 五分钟上手

1. 直接读成品，两个版本任选：
   - **幻灯片版**（与 Witten 原片同版式的 16:9）：`deliverables/slides/WIT-2021-ATIYAH-LANG_幻灯片版_v1.0.pdf`（90 页）；
   - **纸质版**（连续叙事、带导读）：`deliverables/lecture/WIT-2021-ATIYAH-LANG_中文译注本_v1.0.pdf`（39 页）。
2. 先读 `导读：一条走了四十七年的暗线`（正文前，共三页）：三个问题、三条线索、一张年表。
3. 想核对译法：`工程文件/术语表.tsv`；想核对原文：`工程文件/底本对应表.tsv`
   （54 行，原页 → 章 → 该页英文首句）。

---

## 目录

```
WIT-2021-ATIYAH-LANG/
├── README.md              本文件
├── deliverables/
│   ├── slides/
│   │   └── WIT-2021-ATIYAH-LANG_幻灯片版_v1.0.pdf   90 页，593 KB（含 .sha256）
│   └── lecture/
│       └── WIT-2021-ATIYAH-LANG_中文译注本_v1.0.pdf   39 页，763 KB（含 .sha256）
├── 源码-slides/
│   ├── main.tex           幻灯片主控（ctexbeamer，16:9，xelatex ×2）
│   └── parts/p5.tex … p7.tex   第 5–9 部分（第 1–4 部分在 main.tex 内）
├── 源码/
│   ├── main.tex           主控（xelatex ×2）
│   ├── preamble.tex       版式、环境、宏
│   └── chapters/
│       ├── 00_title.tex   标题页
│       ├── 01_editorial.tex   出版说明
│       ├── 02_guide.tex       导读「一条走了四十七年的暗线」
│       ├── 10_ch1.tex … 18_ch9.tex   九章正文（对应原 p.2–54）
│       ├── 20_appA.tex    附录 A 术语与译名对照（63 条）
│       ├── 21_appB.tex    附录 B 人物小传（18 人）
│       ├── 22_appC.tex    附录 C 参考文献
│       └── 23_appD.tex    附录 D 从本演讲到 Kapustin–Witten：技术路线图
└── 工程文件/
    ├── 底本说明.md         底本元数据、sha256、为什么不入库
    ├── 通读笔记.md         翻译前对论证结构的判断、术语决断
    ├── 疑点清单.tsv        13 条疑点及处理结论（未解 = 0）
    ├── 底本对应表.tsv      54 张幻灯片 → 章 → 英文首句
    ├── 术语表.tsv          61 条英中对照
    └── 交付报告.md         交付清单、校验记录、已知限制
```

---

## 现状（2026-11-21，v1.0）

| 项 | 状态 |
|---|---|
| 译文 | **完成**：54 张幻灯片全部译出；纸质版 39 页、20,916 汉字；幻灯片版 90 页 |
| 编译 | **通过**：XeLaTeX（MiKTeX 26.5）两遍，0 error、0 overfull box |
| 逐页对应 | **完成**：正文每段起始处标〔原 p.n〕；`底本对应表.tsv` 覆盖 54 页 |
| 译注 | 5 条（术语、译法、原文语气） |
| 批注 | 纸质版 33 条；幻灯片版另加 30 余条边注（蓝框），并增补第 9 部分“物理上怎么理解几何 Langlands” |
| 附录 | A 术语表 63 条；B 人物小传 18 人；C 参考文献；D 技术路线图 3 页 |
| 底本 PDF | **不入库**（版权与体积），仅记 sha256 与页对应 |

---

## 体例

正文之下分四层，版式上彼此可辨：

| 层 | 颜色 | 内容 |
|---|---|---|
| 正文 | 黑色 | Witten 演讲的忠实翻译，保留口语与修辞（*wild*、*terra incognita*、*smoking gun*） |
| 译注 | 橙色框 | 术语选择、译法理由、原文歧义处的处理 |
| 批注 | 蓝灰框 | 技术性补充与史实考订，由译者负责，不属于原文 |
| 文献摘录 | 灰底框 | 底本中五页论文扫描图改排为英文摘要 + 中译（GNO / Montonen–Olive / Witten–Olive / Osborn / Sen） |

编号按章：正文 §1.1、式 (3.2)、图 5.1、表 8.1；译注 2.1；批注 5.3。

---

## 复现

```bash
# 纸质版（39 页）
cd 源码
xelatex main.tex
xelatex main.tex        # 第二遍生成目录与交叉引用

# 幻灯片版（90 页，16:9）
cd ../源码-slides
xelatex main.tex
xelatex main.tex
```

依赖：TeX Live / MiKTeX，`ctex`（fandol 字体）、`tcolorbox`、`tikz`、`beamer`、
`fancyhdr`、`longtable`、`booktabs`、`hyperref`。不需要底本 PDF，也不需要图片素材。

---

## 两个版本

| | 纸质版 | 幻灯片版 |
|---|---|---|
| 版式 | A4，连续叙事，九章 | 16:9，90 帧，与 Witten 原片同构 |
| 定位 | 通读、查证、当导论 | 对读、投屏、看清每一句的落点 |
| 补注 | 33 条批注 + 5 条译注 | 30 余条蓝框边注 |
| 额外 | 导读三页、附录 A–D | 第 9 部分“物理上怎么理解几何 Langlands”（Capustin–Witten 2006、Frenkel–Witten 2008） |

两版共用同一套术语与底本页码标记，可对照阅读：纸版第 n 章 ↔ 幻灯片第 n 部分。

---

## 许可与责任

- 原文版权属 Edward Witten；本仓库只收译文、译注、批注与重排的图示，不收原文 PDF。
- 译文与批注以 CC BY-NC-SA 4.0 发布，仅供学习与研究；引用原文之处均为学术评论。
- 译文错误由译者负责；批注中的公式与史实，凡有疑问均在文中标明，欢迎指正。
