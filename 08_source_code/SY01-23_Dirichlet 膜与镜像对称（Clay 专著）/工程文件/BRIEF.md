# BRIEF · SY01-23《Dirichlet 膜与镜像对称》中文译本校订工程

## 0. 一句话

把已完成的《Dirichlet Branes and Mirror Symmetry》（Clay 数学专著第 4 卷）中文译本，**逐段对照 Clay 官方 PDF 原文重新校订一遍**，修掉误译/漏译/增译/数学符号错误与术语不一致，修好工程里妨碍复现的构建缺陷，交付「成品 PDF + 可编译源码 + 原文 + 校订记录」四件套。

## 1. 底本与产物

| 项 | 内容 |
|---|---|
| 底本 | *Dirichlet Branes and Mirror Symmetry*, Clay Mathematics Monographs 4, AMS/CMI 2008；697 页 Letter PDF，有文字层 |
| 底本获取 | <https://www.claymath.org/library/monographs/cmim04.pdf>（5,020,938 B，SHA256 `84230A5C…F5F4`） |
| 原文抽取 | `pdftotext -layout` 全本 1,891,233 字符，按 `\f` 分页 698 段（第 N 段 = PDF 第 N 页） |
| 页码关系 | **原书印刷页 = PDF 页 − 10**；译本 530 页与原书页码不可互推 |
| 译本工程 | ElegantBook（`lang=cn,11pt,math=cm,usesamecnt,mode=fancy,citestyle=numeric`），A4，222 幅矢量插图，1521 个 label |
| 段落锚点 | 全书 2 929 个 `\SourceParagraph{id}{原书PDF页号}`，逐段可回溯到原文页 |
| 成品 | 530 页 / 24,434,480 B；`xelatex` 3 遍 + `biber`，0 error、0 undefined reference |

## 2. 工程结构

```
源码/
├─ main.tex                # 26 行：elegantbook + book-adapt，ch01–ch08 + 参考文献 + 索引
├─ book-adapt.sty          # \BookImage / \BookRef / \BookEqRef / \BookIndexPage / \SourceParagraph
├─ chapters/               # preface + ch01–ch08（ch08 拆 6 个文件）
├─ figures/                # 222 个从底本 PDF 裁剪的矢量图
├─ assets/cover.png        # 封面
├─ figure-dimensions.tex   # 每图定宽表（\BookFigureWidth:<路径>）
├─ references.bib          # 476 条
├─ glossary.csv            # 762 条术语（id,english,chinese,context）
├─ index-zh.tex            # 430 行索引，由 tools/build_chinese_index.py 生成（勿手改）
└─ tools/build_chinese_index.py
工程文件/
├─ BRIEF.md  README.md  编译说明.md  build.ps1
├─ 校对标准与方法.md        # 本次校订的口径（只改 P1/P2 类，不重写文风）
├─ deliverable/校订报告.md  deliverable/术语表_术语对照.csv
├─ reports/log_*.md        # 11 份分章日志（逐条「原文—原译—改为—理由」）
├─ reports/{term_audit,verify_landed,integrity_audit}.md
└─ src/tools/              # 14 个流水线脚本（对齐、切块、拆分、审计、修复、合并、装配）
```

## 3. 校订流水线（本次做法，可复用）

1. **建对齐材料**：`make_align.py` 按 `\SourceParagraph{id}{page}` 把每个原书 PDF 页的英文 `pdftotext` 文本与该页对应的中文段落对齐，输出 `review/<chap>_align.txt`（带 tex 行号区间）。
2. **切块**：`make_chunks.py` 每 10 页一块 → `review/chunks/<chap>/pNNN-NNN.txt`（全书 72 块），按章分派给校对员。
3. **大章拆分**（避免两人改同一文件）：`split_chapters.py` 在 section/段落边界把 ch03、ch05 各切成 a/b 两个物理文件，`main.tex` 改用 `\InputIfFileExists` 分别引入；记 `review/_split_map.txt` 行号偏移。
4. **逐块校对**：每人只改自己章节的 `.tex` + 自己那份 `log_<chap>.md`；只动「真正的错译/漏译/增译/数学符号/术语」，不重写文风；每条记录「原文—原译—改为—理由」。
5. **术语与记号统一（第二轮）**：`term_audit` 只读审计全书，产出一致性清单；再用 `fix_terms.py` 按规则批量替换（**逐条断言命中数，不符即整体退出**），避免脚本改过头。
6. **落地核验**：日志条目 ↔ tex 实际内容逐条回查（行号命中 + 全文检索），产出 `verify_landed.md`；本次 201/201。
7. **完整性审计**：花括号/`$`/环境栈/`\left-\right`/`\[ \]` 平衡、纯 LF、无 BOM、`\label` 唯一、`\BookCite` 与 `\BookRef` 全可解析、hunk ≤ 2 行（改动局部性）——`integrity_audit.md`。
8. **合并回单文件并重建**：`merge_back.py` 把 ch03a+b、ch05a+b 拼回 ch03.tex / ch05.tex（备份原分割件），恢复 `main.tex` 单文件引入，删构建产物，重跑 `latexmk`。
9. **装配交付**：`assemble.py` 生成 `Dirichlet膜与镜像对称_校订版/`（PDF + 源码 + 原文 + 校对记录 + 校订报告）。

工具见 `工程文件/src/tools/`；流水线的判据与踩坑记录见发布仓 `04_playbook/07_整书对照校订流水线.md`。

## 4. 判据（什么是「必须改」）

- **P1**：改变数学含义——译反、丢 only/never/any/equivalent、蕴含关系变并列、公式符号/指标错、定义对象错位、整句漏译、原文所无的整句增译。
- **P2**：术语不一致（同构/等价、内射/单射消解、幺模/非退化、quintic threefold 译名）、交叉引用编号错。
- **不动**：文风、断句、译注风格；**译者对原书笔误的数学修正一律保留**（如原书 `(−1)^{deg φ}` 应为 `q^{deg φ}`、原书 thm 4.78/4.88 缺前提），只在日志标注「原文疑误/译者补正」。

## 5. 本次结果

| 项 | 数值 |
|---|---|
| 正文修订 | 201 处（误译、漏译、增译、数学符号、病句/标点） |
| 术语/记号统一 | 90 处（quintic 译名 5、`\mathcal Hom` 15、`\mathbb Z` 括号 5、`\operatorname` 群名 7、图/定理号前空格 57 等） |
| 参考文献 | 18 条 / 19 处（页码区间、期号、连字符丢失、专名、`L2→$L^2$`） |
| 排版修复 | ① `.latexmkrc` 里 biber 被交给不存在的 `python3`；② biber 按 kpathsea 误读系统同名 bib（bbl 5.8 KB → 143 KB）；③ `references.bib` 的 Unicode 弯引号/连接号在 xeCJK 下加宽（PDF 显示 "Almgren’ s"） |
| 结构核验 | 1521 label 全部唯一；1101 个编号标签打印值 = 标签号；各章公式号最大式号逐章相等；定理类计数逐类相等；图 222/222 与图题逐幅一致；表 6 张；目录与原书 TOC 逐条对应 |

## 6. 已知限制

- 索引 6 页（原书 11 页）；条目内容一致，差异来自排版密度与条目合并策略。
- 原书自相矛盾处（(5.115)/(5.117)/(5.118)、`Fuk(X̌)` 与 `Fuk(X(B))` 混用等）照录原书用法，未强行统一，已在日志标注。
- 逐段对齐只到「页」粒度：同页内段落顺序偶有原文跨栏造成的错位，校对时以句意判断。
