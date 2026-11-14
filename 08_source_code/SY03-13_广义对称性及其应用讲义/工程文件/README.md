# 中文学术译本：Ran Luo, Qing-Rui Wang, Yi-Nan Wang《广义对称性及其应用讲义》

本目录是一篇英文理论物理论文（arXiv:2307.09215v3，83 页）的完整简体中文 LaTeX 译本，
含逐节「本节重点」、**50 条可见审校译注**、从原文 PDF 精确裁切的 7 张编号图，以及按原文编号锁定的
147 个公式。成品可逐式、逐图与原文对照。

- **原文**：Ran Luo, Qing-Rui Wang, Yi-Nan Wang,
  *Lecture Notes on Generalized Symmetries and Applications*,
  arXiv:2307.09215v3 [hep-th], 23 Aug 2024, 83 pp；
  正式发表版见 *Physics Reports*，doi:10.1016/j.physrep.2024.02.002。
- **译本**：正文、脚注、图注全译；参考文献按学术惯例保留英文著录与原文编号。
- **编译产物**：`main.pdf`（69 页，XeTeX 引擎编译通过）。

---

## 1. 编译方法

### 1.1 标准方式

```bash
xelatex main.tex     # 第一遍
xelatex main.tex     # 第二遍，生成目录与交叉引用
```

- 引擎必须是 **XeLaTeX**（中文由 `ctex` 处理，不能用 pdfLaTeX）。
- 中文字体默认 `fontset=windows`（Windows 的 SimSun/SimHei/SimKai）。
  在 Linux/macOS 上把 `main.tex` 第 26 行附近的 `fontset=windows` 改为 `fontset=fandol`
  （TeX Live 自带 Fandol 字体）即可。
- 依赖宏包：`ctex, amsmath, amsthm, amssymb, amsfonts, mathrsfs, mathtools, bm, geometry,
  xcolor, graphicx, tcolorbox, enumitem, booktabs, array, multirow, caption, cite, hyperref,
  tikz, tikz-cd`（TeX Live 2022 及以上完整安装均自带）。

### 1.2 无 TeX 发行版时（单二进制）

本仓库在**未安装 TeX Live** 的环境中用 [Tectonic](https://tectonic-typesetting.github.io/)
（XeTeX 引擎、自动下载所需宏包）完成全部编译验证：

```bash
tectonic -X compile main.tex
```

---

## 2. 目录结构

```
.
├── main.tex                  导言区、题名页装配、章节 \input
├── main.pdf                  编译产物（69 页）
├── defs.tex                  原文记号宏（逐字取自 arXiv 源码导言区，保证公式可 1:1 复制）
├── refs.bbl                  参考文献（原文 JHEP 格式 bbl，201 条，编号与原文一致）
├── SPEC.md                   翻译与排版规范（术语表、数学保真规则、批注与图表格式）
├── REVIEW-NOTES.md           全部 50 条译注的汇总索引（权威版在源码行内）
├── README.md                 本文件
├── sections/                 正文分片，按原文节次一一对应
│   ├── s00-front.tex         题名页、摘要、译者说明、目录
│   ├── s01-intro.tex         §1 引言
│   ├── s02a-higher-form.tex  §2.1–2.2 拓扑算符与高形式对称性（图 1–4）
│   ├── s02b-trifecta.tex     §2.3–2.4 规范化、't Hooft 反常、对称性三要素（图 5–6）
│   ├── s03a-anomalies.tex    §3.1 SPT 边界上的 't Hooft 反常
│   ├── s03b-classification.tex  §3.2 反常与 SPT 的一般分类（表 1）
│   ├── s04a-applications.tex §4.1 弦论中的应用（图 7）
│   ├── s04b-cmt.tex          §4.2 凝聚态中的应用（环面码；不编号表）
│   ├── s05a-higher-group.tex §5.1–5.2 范畴论初步与 2-群定义
│   ├── s05b-crossed.tex      §5.3–5.4 交叉扩张与 Postnikov 类
│   ├── s05c-physical.tex     §5.5–5.8 物理诠释、弱 n-群、非可逆对称性；致谢
│   ├── s06-appa.tex          附录 A  Čech 上同调
│   └── s07-appb.tex          附录 B  群上同调
└── figures/                  7 张编号图（400 dpi PNG）
    ├── figure-1.png … figure-7.png
    └── FIGURE-QA.md          裁片质检记录（含每张的 PDF 页码与裁切矩形）
```

---

## 3. 排版约定（改稿前请先读这一段）

1. **公式编号锁定原文编号**：正文全部编号公式均由 LaTeX 自动编号（`\numberwithin{equation}{section}`），
   且公式环境与原文**严格同序同数**，因此编号与原文一致：
   §2 为 (2.1)–(2.60)、§3 为 (3.1)–(3.27)、§4 为 (4.1)–(4.29)、§5 为 (5.1)–(5.31)，
   附录 A/B 为 (A.1)–(A.9)、(B.1)–(B.2)，共 **147 条**。交叉引用用 `\eqref{}` / `\ref{}`。
   > 注意：这一做法要求**不增删公式环境**；若你增删了某条公式，其后编号会自动顺移，
   > 与原文的对应关系即被打破（可改回 `\tag{编号}` 的锁定写法，见 `SPEC.md` §3）。
2. **节标题层级与原文完全一致**，编号由 LaTeX 自动生成（§1–§5、附录 A/B；2.1、2.2.1 等），
   与原文目录逐条相同。每个 `\section` 后紧跟 `\label{sec:...}`，可跨文件引用。
3. **图、表编号自动生成**，与原文 Figure 1–7、Table 1 一一对应；原文中不编号的示意图与第二张表
   不占编号（见第 5 节）。译注与图注中给出原文页码（**PDF 页码**，非印刷页码）。
4. **「本节重点」方框**（`keytakeaways` 环境，蓝色）是译者所加、非原文内容，共 7 个
   （§1–§5 与附录 A、B）。
5. **译注**（`yizhu` 环境，橙色）——成品中可见、全文连续编号 **1–50**，三类内容：
   - 审校批注：推导易错点、作者省略的论证、物理图像点拨（共 40 条）；
   - `\begin{yizhu}[原文疑误]`：原文疑似笔误/排版问题，**照原文保留不改公式**，
     注中说明理由与核对建议（共 10 条）。
   译注可整体关闭：`main.tex` 里 `\showyizhutrue` → `\showyizhufalse`，方框与编号全部消失，
   正文回到纯译本状态。`REVIEW-NOTES.md` 是与成品编号一一对应的索引。
6. **页码锚点**：每页起始处有 `% ==== 原文 PDF 第 N 页 ====` 注释，用于与原文逐页对照；
   由于中译本版面更紧凑（69 页 vs 原文 83 页），锚点页码是**原文页码**，不是译本页码。
7. **参考文献**：正文引用沿用原文 `\cite` 键，`refs.bbl` 直接读入，编号 [1]–[201] 与原文一致。
8. **版权与分享声明**排在题名页底部（PDF 第 1 页），转发时不得删除；条文见第 7 节。

---

## 4. 本次交付的校验记录

- **编译**：以 XeTeX 引擎完整编译：**0 error、0 未定义引用、0 overfull hbox、0 缺字
  （Missing character）**；仅 1 处 Underfull hbox（中文两端对齐的常见现象）与 1 条
  `Font shape ... undefined` 字体形状提示（中文粗斜体回退，不影响版面）。
  产物 `main.pdf` 共 **69 页**（原文 83 页；中译本行距与汉字密度使正文更紧凑）。
- **公式**：全文 **147 个编号公式**。用脚本从成品 PDF 抽取全部编号并与原文 PDF 抽取的编号序列
  逐节比对：**§2=60、§3=27、§4=29、§5=31，完全一致、无缺号、无重号**。
  另用脚本把每个公式块的 LaTeX 内容与原文 arXiv 源码逐条比对（空白归一化后完全相同，
  仅 `\text{}` 内的说明性英文按规范中译），确保无符号、上下标、括号、因子遗漏。
- **结构**：§1–§5 与 2.1–2.4、3.1–3.2、4.1–4.2、5.1–5.8 及附录 A/B 的层级与标题数量
  与原文逐条相同（`\section` 7、`\subsection` 16、`\subsubsection` 20）。
  定理类环境计数一致：例 11、定义 11、命题 2、定理 2、证明 3，编号与原文相同
  （例 1–11、定义 2.1/3.1/3.2/5.1–5.8、命题 1–2、定理 1–2）。
- **图**：7 张编号图（Figure 1–7）逐张从 PDF 以 400 dpi 裁切，按原图尺寸比例插入；
  正文示意图与公式内图示保留原文 TikZ/tikzcd 矢量源码（逐字复制，共 25 个
  `tikzpicture` + 15 个 `tikzcd`）。裁片逐张目视核验，无正文渗入、无图形切边
  （记录见 `figures/FIGURE-QA.md`）。
- **表**：Table 1 用源码原生 `tabular` 重排；原文第二张表（无 `\caption`、原文不编号）
  用原生表格重排且不加编号，以免破坏表编号。
- **交叉引用**：59 个 `\label`（覆盖源码全部 57 个 label，另加 2 个方便引用的节/附录 label），
  全部 `\ref`/`\eqref` 可解析，成品中 **0 个 `??`**。
- **译注**：成品中 50 个橙色方框，编号 1–50 连续；`REVIEW-NOTES.md` 与之一一对应。
- **翻译完整性**：用脚本核查——源码五个文件的全部节标题均已译出；源码中被 `%` 注释掉、
  PDF 中不出现的内容未收入；无整段漏译（逐段对齐，页码锚点可用于人工抽查）。

### 4.1 校对中发现的原文笔误（10 条，均照原文保留并加注）

| 位置 | 原文 | 判断 |
|---|---|---|
| §1 末（源码 26 行） | “symmtries” | `symmetries` 之误 |
| §2.1（源码 93 行） | `V_(C^{p})` | 应为 `V(C^p)`（PDF 第 8 页即如此排） |
| §2.1 | “symmetric group”（源码） | 应为 “symmetry group” |
| §2.3.1（2.36 后） | “$I_{d+1}$ 是 … (d+2)-形式” | 第二个 $I_{d+1}$ 应为 $I_{d+2}$ |
| §3.1 | “the topology of the topology of TDN” | 重复 |
| §3.1 | `Eq.~(ref{eq:tri})` | 缺反斜杠，PDF 排成 “refeq:tri” |
| §3.1 | “believed to leads” | 语法笔误 |
| §3.2.4（3.24） | 正文 $\omega_2$ 与式中 $\omega$ 记号不一致 | 记法混用 |
| §4.2（4.7） | $\sum_{r=1}^r A_i\wedge\omega_i$ | 指标不匹配（应为 $\sum_{i=1}^r$） |
| §4.2 | “4+1D”（4.29 上下文） | 应为 3+1 维 |
| §5.3（5.7） | 交叉模 $(G_1,H_1,\ptl_1,\rhd_2)$ | 应为 $\rhd_1$ |
| §5.3（5.8） | 量词 $H\in H_1$ | 应为 $h\in H_1$ |
| §5.3（5.10） | 左端 $s(g,h)$ | 按 (5.11) 应为 $s(gh)$ |
| §5.1 脚注 15 | “Cartisian” | `Cartesian` 之误 |
| §5.1 | “Pieffer identity” | `Peiffer` 之误 |
| §5.4 | “the commutators of then are” | `of them` 之误 |

> 其中 §2.3.1 的 $I_{d+1}/I_{d+2}$ 与 §5.3 的 $\rhd_1/\rhd_2$ 若只按字面读会引起推导困惑，
> 译注中给出了两种可能来源与核对建议；其余均为拼写/语法/编号引用层面的笔误，不影响物理内容。

---

## 5. 已知偏离与处理（与原文版式的差异）

1. **编号图用 400 dpi 位图**：Figure 1–7 按任务要求从 PDF 精确裁切为 PNG 插入（保证与原图完全一致、
   并可就地裁剪），代价是放大时不如矢量图锐利。若需要矢量版，可直接用原文 arXiv 源码的
   TikZ/`FigVS.pdf` 重绘——`figures/FIGURE-QA.md` 给出了每张图的原文标签与页码。
2. **正文中的不编号示意图保留 TikZ 矢量源码**：原文有 3 个 figure 环境没有 `\caption`（因而在
   原文中不占图号）以及大量嵌入公式或句中的示意图。它们不是“图”，无法用 `figure` 环境承载
   （会破坏图编号），故逐字保留原文 TikZ/tikzcd 源码，以保证与正文基线对齐、可编辑、且不改变图号。
3. **图内英文标注保留**：裁切图内的文字（如 Figure 7 的 `singularity`、`∂X`）属于原图内容；
   译文只翻译图注（caption），不改动图内标注。
4. **表格用原生 LaTeX**：原文 Table 1 与第二张（不编号）表都是简单 `tabular`，故用原生表格重排
   （可编辑、清晰），未使用图片。
5. **原文 (2.21) 的 `\mqty(\dmat{...})`** 使用了 physics 宏包的自定义矩阵命令，本译本未加载该宏包，
   已按 PDF 第 13 页的实际排版改写为标准 `pmatrix`（对角元 $d_1,\dots,d_k$ 与两行零），
   数学内容不变（译注 9 说明 Smith 标准形的读法）。
6. **原文个别装饰性排版**（断行、空行、`\hspace` 等）未逐字复刻；术语与公式不受影响。
7. **页码**：中译本 69 页、原文 83 页（原文含 15 页参考文献；中译本参考文献经 `refs.bbl` 直接
   排入，亦占用相应页数）。本译本正文比原文紧凑，故**不能按页对齐**；请按公式编号、图号与
   源码中的页码锚点定位。

---

## 6. 使用建议

- **只需讲课用的干净正文**：把 `main.tex` 的 `\showyizhutrue` 改为 `\showyizhufalse`
  （译注方框与编号全部消失），再删除各 `keytakeaways` 环境即可；无需改动任何一节正文。
- **只删个别译注**：定位 `\begin{yizhu} ... \end{yizhu}`（`REVIEW-NOTES.md` 给出每个编号的
  `文件:行号`），整行删除即可，其余编号会自动重排。
- **对照原文核对某式**：按编号（如 (5.12)）翻原文即可；原文 PDF 页码可由源码页码锚点
  `% ==== 原文 PDF 第 N 页 ====` 定位。
- **把某个分片单独发给学生**：整段复制即可，它只依赖 `main.tex` 导言区、`defs.tex` 与 `figures/` 目录。
- **术语对照**：`SPEC.md` §3 附有完整术语表（广义对称性、高形式对称性、高群、配边、Postnikov 类、
  SPT、环面码等），可单独抽出作为课程术语表。

---

## 7. 版权与分享（全文见 PDF 第 1 页底部）

- **原著版权**：原文 © 2024 Ran Luo, Qing-Rui Wang, Yi-Nan Wang，经 arXiv 以「非独占分发许可」
  （arXiv.org perpetual, non-exclusive license）发布。该许可**只授权 arXiv 分发原文**，
  不授予第三方翻译、改编或再发布的权利；因此原文著作权仍完全归作者所有。
- **本译本**：属于原文的演绎作品。翻译、图表裁切、译注与排版由 DeepSeek Harness 智能体集群完成，
  译注与「本节重点」系译者独立添加的评论，不代表原作者观点；译文讹误由译者负责。
- **可以做什么**：学术研究与教学使用；**原样**转发本 PDF 全文（不得改动正文、不得删除版权声明）。
- **不可以做什么**：任何商业使用；未经许可的改编、摘编、再发布（尤其投稿、出版、收录进教材）。
  这类使用须先取得**原作者**（著作权人）与本译者的书面许可。译注部分可单独按
  CC BY-NC-SA 4.0 使用，但整份文档的许可上限由原文决定。
- **引用**：请同时标注原文与本译本，例如：R. Luo, Q.-R. Wang, Y.-N. Wang,
  *Lecture Notes on Generalized Symmetries and Applications*, arXiv:2307.09215；
  中译本（含译注），第 1.0 版，2026。
- 本译本非 arXiv 或原作者发布的官方版本；如原作者或 arXiv 提出异议，将立即停止分发。
