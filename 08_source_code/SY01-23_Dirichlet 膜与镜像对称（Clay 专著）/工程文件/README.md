# 工程文件 · SY01-23《Dirichlet 膜与镜像对称》校订工程

本目录是 2026-11-14 那次「对照 Clay 官方原文逐段校订」的全部过程材料。**源码在 `../源码/`**，本目录不重复放代码。

## 先看哪几个

| 想看什么 | 打开 |
|---|---|
| 这次到底改了什么、为什么 | `deliverable/校订报告.md` |
| 一句一条的改动清单（原文—原译—改为—理由） | `reports/log_<章节>.md`（11 份） |
| 改动是否真落地到 tex | `reports/verify_landed.md`（201/201 命中） |
| LaTeX 结构/编码/引用有没有被改坏 | `reports/integrity_audit.md`（通过） |
| 术语与记号统一清单 | `reports/term_audit.md` + `deliverable/术语表_术语对照.csv` |
| 校对口径（什么该改、什么不许动） | `校对标准与方法.md` |
| 工程怎么搭、流水线怎么跑 | `BRIEF.md` |
| 怎么编译 | `编译说明.md` / `build.ps1` |

## 目录

```
BRIEF.md                 工程说明书：底本、结构、流水线、判据、结果、已知限制
README.md                本文件
编译说明.md               环境、命令、已知坑（biber 路径、python3）
build.ps1                一键编译（xelatex+biber，3 遍）
校对标准与方法.md          校对员手册（P1/P2 判据、LaTeX 安全规则、日志格式）
deliverable/
  ├ 校订报告.md            交付级总结（七节）
  └ 术语表_术语对照.csv     762 条术语（id,english,chinese,context）
reports/
  ├ log_preface_ch01.md … log_bib.md   11 份分章日志
  ├ term_audit.md          全书术语/记号一致性审计
  ├ verify_landed.md       201 条改动落地回查
  └ integrity_audit.md     LaTeX 完整性审计
src/tools/                14 个流水线脚本（见下表）
```

## 流水线脚本（`src/tools/`）

| 脚本 | 作用 |
|---|---|
| `make_align.py` | 按 `\SourceParagraph` 把原书每页英文与该页中文段落对齐，产 `review/<chap>_align.txt` |
| `make_chunks.py` | 每 10 页切一块，产 `review/chunks/<chap>/pNNN-NNN.txt`（全书 72 块） |
| `split_chapters.py` | 在 section 边界把 ch03/ch05 拆 a/b 两文件，免两人同改一个文件 |
| `estimate_tokens.py` | 估算每块 token，用于分派 |
| `figcap2.py` | 图题审计：原书 "Figure N." 题注 vs 译文 `\caption`（222 图逐幅比） |
| `refnum.py` | `\BookRef` 显示编号 vs label 编号一致性（1740 处） |
| `refcheck.py` | 解析 aux 的 `\newlabel`，核对 1101 个编号标签的打印值 |
| `eqnum.py` | 各章最大公式号 vs 工程 `\label{eq:CH.N}` |
| `stmtnum.py` | 定理/定义/例… 各类型计数 vs 原书 |
| `pagecover.py` | 原书每页是否都有 `\SourceParagraph` 覆盖 |
| `fix_terms.py` | 术语批量替换（逐规则断言命中数，不符即退出） |
| `merge_back.py` | ch03a+b / ch05a+b 合回单文件，恢复 main.tex |
| `assemble.py` | 装配桌面交付目录（PDF+源码+原文+校对记录） |
| `crop.py` / `pagecover.py` | 按 `pdftotext -bbox` 定位并裁切 PDF 片段，用于核对原书页面 |

脚本里的路径写的是当时的工作目录（`C:\Users\admin\Downloads\DBMS_work`），复用时改 `PROJ`/`REVIEW` 两个常量即可。

## 复现校订结论的最小步骤

```powershell
cd ..\源码
latexmk -xelatex main.tex           # → build/main.pdf，530 页
pdftotext -layout build/main.pdf out.txt   # 与原书 full.txt 按 \SourceParagraph 页号对照
```

校订本身依赖 Clay 官方 PDF（`原文/` 目录，或 <https://www.claymath.org/library/monographs/cmim04.pdf>，SHA256 `84230A5C…F5F4`）。
