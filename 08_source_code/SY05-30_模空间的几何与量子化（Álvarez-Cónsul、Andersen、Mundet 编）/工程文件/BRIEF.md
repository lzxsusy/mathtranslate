# BRIEF — SY05-30《模空间的几何与量子化》

| 项 | 内容 |
| --- | --- |
| 编号 | SY05-30 |
| 中文题名 | 模空间的几何与量子化 |
| 原文题名 | *Geometry and Quantization of Moduli Spaces* |
| 编者 | Luis Álvarez-Cónsul、Jørgen Ellegaard Andersen、Ignasi Mundet i Riera |
| 作者 | Vladimir Fock、Andrey Marshakov、Florent Schaffhauser、Constantin Teleman、Richard A. Wentworth |
| 出版 | Birkhäuser（Springer），Advanced Courses in Mathematics – CRM Barcelona，2016 |
| ISBN / DOI | 978-3-319-33577-3 / 10.1007/978-3-319-33578-0 |
| 底本页数 | 230 PDF 页；正文印刷页 1–216（四章）＋前置罗马页 i–x |
| 底本类型 | 已出版专著（Springer 版权）；**只入库自产译文与元数据，出版社 PDF 不入仓** |
| 本卷范围 | 前言（Foreword）＋第 2 章（Schaffhauser，印刷页 67–108）全译；第 1、3、4 章建骨架与任务书 |
| 译稿 | `源码/main.tex` + `源码/chapters/*.tex`（xelatex 独立可编译） |
| 参考卷 | 版式与工序参照 `SY07-11`（Miličić）；资料卡与插件测试参照 `SY07-11` 的 `work/kb插件测试笔记.md` |

## 为什么选第 2 章做样板章

1. **自含**：不依赖第 1/3/4 章的 cluster、TQFT、Higgs 丛语言，读者拿这一章就能读。
2. **prose 密度高、公式密度低**：42 页里 26 个编号公式、30 余个定理类环境、0 张插图，适合把「通读 → 术语 → 翻译 → 编译 → 资料卡 → 插件反馈」整条管线一次跑通，而不被图与长公式拖住。
3. **术语可复用**：克莱因曲面、实结构、万有覆盖、增广同态、酉表示簇这一组词，后面第 4 章（Higgs 丛 ↔ 局部系统）还要用；先把术语冻住，第 4 章能直接受益。
4. **试点公平**：它是全书四章中页码最少的一章（42 PDF 页）；用最小成本验证工程标准，再谈扩产。

## 成功标准（本卷）

- [x] `源码/main.tex` 三遍编译 0 error、0 Overfull、可独立出 41 页 PDF；
- [x] 定理/公式编号与原文逐一对得上（定义 2.1.1 … 定理 2.3.4、式 (2.1)–(2.26)、习题 2.1.17–2.3.10）；
- [x] 原文笔误照译并出译注（Q005、Q006 两条），不静默改正；
- [x] 术语表冻结在前、正文一致（`work/术语表.tsv` → `成品/术语对照表.md`）；
- [x] 通读笔记、疑点清单、校订日志、插件测试笔记、工程反馈、工作流记录齐备；
- [x] 资料卡入库并在 kb 插件里可检索（`datasets/sy0530`）；
- [x] `RELEASE_REGISTER.csv` 一行 + `03_translations_meta/SY05-30/` 元数据。

## 不做的事

- 不重排原书的四章次序，不为四章写统一导言（编者前言已译，导读另置《全书导读》，标明「据前言与各章导言写成，非译文」）。
- 不补图、不改公式编号、不把「Real」译成「实」（Atiyah 的 Real 是专名，保留大写，见术语表）。
- 第 1/3/4 章本卷不出译文；只在 `work/notes/` 留任务书，避免后来者重复勘察。
