# arXiv:2112.12756v2 中译与译校批注项目

**原文**：O. Chekeres, A. Losev, P. Mnev, D. R. Youmans,
*Two Field-Theoretic Viewpoints on the Fukaya–Morse $A_\infty$ Category*,
arXiv:2112.12756v2 [hep-th], 10 Jul 2022, 27 pp.

**说明**：用户提供的 PDF 虽在任务描述中被预设为 Witten 的文章，实际底本为上述四位作者的论文（文中引用了 Witten 1982 年的 Morse 理论论文 [17]，但作者不是 Witten）。译文与批注均以这份 PDF 为唯一底本。

## 1. 底本与页映射
- 底本：`2112.12756v2.pdf`，A4，595×842 pt，27 页。
- 页映射：**原书页 = PDF 页**（arXiv 版无前置页，正文页码 n 直接对应 PDF 第 n 页），批注中的“原书 p.N”即 PDF 页码。
- 文本提取：`work/full_text.txt`（PyMuPDF 2.0，按 `===== PDF PAGE n =====` 分页）；页面渲染：`work/pages/pNN.png`（140 dpi）。
- 公式一律回页面图像核对（提取文本会丢上下标层级）。

## 2. 目录结构
```
main.tex                     主文件：导言区 + 标题页 + 译校说明 + 目录 + \input
chapters/sec01.tex           第 1 节 引言、1.1 结果概述
chapters/sec02a.tex          第 2 节 开头、2.1 增强的 Fukaya–Morse A∞ 范畴（式 1–7、定理 1）
chapters/sec02b.tex          2.2 例子与图示、2.3 Morse 收缩（式 8–22、图 1–5）
chapters/sec02c.tex          2.4 用闭链形变 Morse 微分、2.5 相交公式与横截性、2.6 积分公式（式 23–31、图 6–7）
chapters/sec02d.tex          2.7 旁注、第 3 节 二次量子化（式 32–47、注 3.1/3.2、图 8–10）
chapters/sec04.tex           第 4 节 一次量子化（式 48–56、注 4.1、例 6/7、图 11–12）
chapters/sec05.tex           第 5 节 结语
chapters/sec06.tex           参考文献（[1]–[17]，条目序即原编号）+ 作者单位
chapters/appendix_notes.tex  附录 A 译校批注一览（由 work/gen_notes.py 自动生成，勿手改）
figures/fig01.png … fig12.png  原文 Figure 1–12（矢量图按 400 dpi 裁剪），对应表见 figures/README.md
work/                        术语表、体例、引用键表、提取文本、页面图、lint.py、gen_notes.py
reports/                     各章分章报告
```

## 3. 编译
```powershell
xelatex main.tex
xelatex main.tex          # 第二遍：目录与交叉引用
```
- 需要标准 TeX Live / MiKTeX（`ctex`、`amsmath`、`amssymb`、`amsthm`、`graphicx`、`geometry`、`hyperref`、`natbib`、`verbatim`、`xcolor`）。
- 导言区默认 `fontset=windows`（Windows 下调用系统宋体/黑体）；macOS/Linux 请改为 `fontset=mac` / `fontset=fandol`。
- 本次交付已附**编译好的 `main.pdf`（37 页）**，由 XeLaTeX 实测生成，可直接打开；`main.log` 为其编译日志。
- 一键构建脚本：`build.ps1`（本机若装有 TeX，双击/运行即可；脚本内含两遍 xelatex 与日志检查）。

## 4. 体例（详见 work/style.md）
- **编号一律照录原文**：式 (1)–(56) 用 `\tag{…}`；定理 1、假设 2.2、例 1–7、注 2.1/3.1/3.2/4.1 用 `thmenv` 环境手工落号；图 1–12 保持原序。读者可直接拿中译与原 PDF 对读。
- **本节重点**：每节/每小节开头 `takeaway`（物理图像 / 数学工具 / 主要结论），可用 `\showtakeawayfalse` 关闭。
- **批注**：源码内 `% [Tutor Note: …]`，三类（易错预警、含糊点拨、背景直觉），不进入排版结果；附录 A 按节汇总，可用 `\shownotesfalse` 隐藏。
- **术语**：`work/glossary.md` 冻结；保留英文者在首次出现处括注。

## 5. 质检（详见 reports/00_总报告.md 与各分章报告）
- **规模**：正文约 11 400 汉字、批注约 5 200 汉字（68 条）；编号式 56 条（原号 (1)–(56) 全保留）；图 13 幅（原书 Figure 1–12 + p.15 内嵌手绘树形图）；脚注 16 条；"本节重点" 17 处。
- **静态检查**：`python work/lint.py --all`（环境配对、花括号、`$` 配对、`\ref` 目标、翻译腔、英文残留、`\tag` 连续性）→ **0 FAIL**。
- **编译前仿真**：`python work/precompile.py`（文本模式未转义 `& _ ^ #`、`equation` 环境缺 `\tag`、`\tag` 误置于 `aligned/split` 内、`thmenv` 参数、`\cite` 键是否登记、图文件是否存在、`\verb` 配对）→ **0 problem**。
- **项目审计**：`python work/audit.py` → 式号覆盖 56/56、标签无重复且引用全部有定义、13 图全部引用。
- **批注一致性**：正文 `% [Tutor Note:` 68 条 = 附录 A 条目 68 条（`work/gen_notes.py` 自动生成，勿手改）。
- **公式核对**：56 条编号式逐条对照 `work/pages/pNN.png` 与临时 350–600 dpi 裁剪图。
- **实测编译（最终结果）**：已在本次环境装好 TeX Live 2026 并用 XeLaTeX 两遍**实际编译通过**：**37 页，0 error，0 缺字（Missing character = 0），0 未定义引用/引文，仅 1 处 1.23 pt 的 Overfull（肉眼不可见）**。成品 `main.pdf`（约 1.32 MB）随附，编译日志 `main.log` 保留备查。

## 6. 交付清单
- `main.tex` + `chapters/`（9 个文件）+ `figures/`（12 图 + 对应表）+ `work/`（术语表、体例、引用键、工具）+ `reports/`（分章报告）+ `README.md`。
