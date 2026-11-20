# BRIEF — SY05-28《曲线的镜像及其 Fukaya 范畴》中译注本

本文件是交给新会话（翻译执行者）的完整任务书。**先读本文件，再读仓库条例，然后动手。**

## 0. 一句话任务

把 Denis Auroux 的两份公开讲义译成中文、排版成一本可编译的 LaTeX 书并出 PDF，保留全部源码与过程记录。

- 底本一：《Mirrors of curves and their Fukaya categories》—— 2020 年 1 月迈阿密「Conference on Homological Mirror Symmetry」三场报告的手写笔记（Talk 1–3），共 17 页，无文字层，是扫描手写稿。
- 底本二：《An invitation to homological mirror symmetry》—— 2019 年 9 月 IMSA 成立大会报告（14 页 beamer 幻灯片，有文字层）。

两者合为一册：底本一为正文（第一至三讲），底本二作附录（「同调镜像对称引论」）。

## 1. 必须先读的仓库文件（按顺序）

1. `C:\Users\admin\Desktop\数译发布\gitee_shuyi\04_playbook\01_数学文献翻译纪律.md`（v2.1，606 行）——**这是硬约束**。五公理、第 0 定律（先通读后落笔）、§1 通读笔记与疑点清单、§2 术语与来源分级、§3 数学纪律、§4 十三条铁律、§5 语言、§6 LaTeX、§9 交付清单。
2. `C:\Users\admin\Desktop\数译发布\gitee_shuyi\04_playbook\00_学术翻译总纲.md`
3. `C:\Users\admin\Desktop\数译发布\gitee_shuyi\04_playbook\02_文献引进标准.md`
4. 模板目录 `C:\Users\admin\Desktop\数译发布\gitee_shuyi\04_playbook\templates\`（通读笔记、疑点清单表头、译前契约）
5. **同一位作者、同一路线的上一本成品**（强烈建议照抄其工程组织与文风）：
   `C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY05-27_三价图的拉格朗日 Floer 理论与曲线的同调镜像对称\`
   - `源码\main.tex`、`preamble.tex`（ctexart + fontset=windows + 定理环境 + TikZ）、`ch0_front.tex`（封面/译者说明/目录）、`refs.tex`、`app_terms.tex`
   - `工程文件\README.md`、`工程文件\reports\01_通读笔记.md`、`02_疑点清单.tsv`、`03_术语表.md`

## 2. 底本与素材（已就位，不要重新下载）

工程根目录：`C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY05-28_曲线的镜像及其Fukaya范畴\`

- `源码\original\notes-miami2020-1.pdf`（Talk 1，4 页）
- `源码\original\notes-miami2020-2.pdf`（Talk 2，6 页）
- `源码\original\notes-miami2020-3.pdf`（Talk 3，7 页）
- `源码\original\slides-hmsdim1-miami2019-trans.pdf`（附录幻灯片，14 页，有文字层）
- `源码\original\pages\`：上述 31 页的 300 dpi PNG，命名 `t1-01.png … t3-07.png`、`inv-01.png … inv-14.png`。
  **手写笔记必须逐页读图翻译**（read_image 工具直接看 PNG）。幻灯片可用 `pymupdf`（Python 3.12，`C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe`，已装 pymupdf）导出文字作辅助，但公式与图仍以页面图像为准。
- 出处：https://people.math.harvard.edu/~auroux/papers/ （作者个人主页 papers 目录）。元数据：Auroux, Harvard University；Miami, Jan 27–29 2020；IMSA Inaugural Conference, Miami, Sept 6 2019。

## 3. 硬性流程（条例要求，不得跳步）

1. **先通读**全部 31 页图像，产出 `工程文件\reports\01_通读笔记.md`（含每页要点、整体论证线、与 SY05-27 论文的呼应处）与 `工程文件\reports\02_疑点清单.tsv`（手写难辨处、原文笔误、跳步；**未解项必须清零或逐条注明处理方式**）。
2. 冻结术语表 `工程文件\reports\03_术语表.md`（英文/中文/依据；依据写法见条例 §2.5.6，可用 `本库:SY05-27 术语表` 作内部依据）。与 SY05-27 已冻结的译名保持一致（Fukaya 范畴、拉格朗日、同调镜像对称、广义 Tate 曲线、传播圆盘、热带化、Novikov 域等）。
3. 建 LaTeX 工程并搭建骨架，先做一章样板（建议 Talk 1），编译通过后再推进。
4. 逐讲翻译 → 每 2–3 章编译一次 → 全部完成后整书三遍 `xelatex`。
5. 写 README/BRIEF/交付核对，落 `成品\` PDF。

## 4. 交付物清单（缺一不可）

工程根 `C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY05-28_曲线的镜像及其Fukaya范畴\`：

- `源码\`：`main.tex`、`preamble.tex`、`ch0_front.tex`、`ch1_talk1.tex`、`ch2_talk2.tex`、`ch3_talk3.tex`、`app_invitation.tex`、`refs.tex`、`app_terms.tex`（术语附录）、`original\`（底本 PDF + pages）、构建脚本可选。
- `成品\SY05-28_曲线的镜像及其Fukaya范畴_中译注本.pdf`
- `工程文件\BRIEF.md`（本文件，可补充）、`工程文件\README.md`（编译方法、实测记录、翻译与校订说明、已知取舍）、`工程文件\reports\01_通读笔记.md`、`02_疑点清单.tsv`、`03_术语表.md`、`04_交付核对.md`
- `工程文件\精选片段.md`（3–5 段中英对照）
- 项目根 `投稿信息.md`（含 `<!-- TRANSLATION-STANDARD:v2.1 -->` 标记块；照 SY05-27 的写）
- `C:\Users\admin\Desktop\数译发布\gitee_shuyi\03_translations_meta\SY05-28\投稿信息.md`（meta 目录只放这一个文件）

## 5. 排版与质量要求

- `ctexart`，`fontset=windows`，A4，geometry 2.6cm 左右；XeLaTeX 编译（MiKTeX 在 `C:\Users\admin\AppData\Local\Programs\MiKTeX\miktex\bin\x64\`，需先 `export PATH=".../x64:$PATH"`）。
- 版式照 SY05-27：封面 → 译者说明（翻译原则、符号约定、批注说明）→ 目录 → 正文 → 参考文献 → 附录（术语对照表）。
- 原文的图用 TikZ 重绘（手写稿的示意图按几何内容重画，图注注明「原稿第 N 页」）。幻灯片里的图同样重绘。
- 定理/定义/引理环境与原文编号一致（原文无编号则按节编号），`\label`/`\ref` 自洽。
- 批注：`% [Tutor Note: 易错|点拨|直觉] …`，每条必须有来源（nLab/教材/原始论文/本库），批注内不写 `%`；数量 8–15 条，分布均匀。
- 语言：条例 §5（数学工作者的中文、禁「被……所」「进行……的」、一句 ≤60–70 汉字、全角标点、英文术语两侧半角空格）。
- **验收线**：三遍编译 exit=0；`Overfull`=0；`Undefined control sequence`=0；`undefined reference/citation`=0；`Missing character`=0；目录条目数与节数相符；无「待译」占位。
- 手写稿辨认不确定的公式：**不得臆造**，按条例保留原样并进疑点清单，或在批注里说明。

## 6. 边界

- 只改本工程目录内的文件；不要动 `03_translations_meta` 下别人的目录，也不要改其他 SY 工程。
- 不做 `git push`；完成后 `git add` + `git commit`（提交信息写清 SY05-28 内容），把 commit hash 写进报告，推送由主会话复核后执行。
- 不新增依赖、不联网取新素材（底本已全）。

## 7. 完成时的回报格式

1) 成品 PDF 绝对路径与页数；2) 编译统计（error/overfull/undefined/missing 各几）；3) 批注条数、术语条数、文献条数；4) 疑点清单未解数；5) commit hash；6) 已知取舍与建议。
