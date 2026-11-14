Dirichlet 膜与镜像对称 — 完整中文译本源工程（2026-11-14 校订版）

内容：前言、全部 8 章正文、脚注、图注、原书 476 条参考文献及中文索引。
排版：ElegantBook 4.7；A4；正文 11pt；模板原生默认中英文字体与 Computer Modern 数学字体（math=cm）。封面沿用原生布局，图片为 1281×1024。
图件：figures/ 内 222 幅原书 PDF 矢量裁剪图，保持原纵横比及相对于整页的面积比例。
导航：目录收录章与节，书签保留正文实际层次；数学陈述、图、公式、引文及索引使用交叉引用。索引页码通过段落锚点重新生成，并链接到对应内容。

编译环境：TeX Live 2023 及以上，或 MiKTeX（需 xelatex、latexmk、biber）。本工程不需要 Python。
请在本目录运行：

    latexmk -xelatex main.tex

.latexmkrc 已配置：$pdf_mode=5（XeLaTeX）、$out_dir='build'、biber 以 `--input-directory=. --output-directory=build` 从工程根目录调用，确保读取本工程的 references.bib，而不是 TeX 发行版里自带的同名 bib（否则 .bbl 会缺失大部分条目）。输出 build/main.pdf。
若系统终端找不到程序，先将 TeX 安装目录加入 PATH；macOS 通常为 /Library/TeX/texbin。
中文字体由 ElegantBook 的 ctexfont 原生设置按操作系统选择；不要另行覆盖。正式 PDF 已嵌入全部字体，阅读端无需安装这些字体。
所有源文件为 UTF-8。公式、引文和索引页码依赖辅助文件，请等待 latexmk 完成，不能以第一轮编译的页码为最终页码。
index-zh.tex 已包含完整中文词项及段落引用，重编译会自动更新译文页码，不需要原书 PDF 或外部索引数据。
源文件包不包含编译缓存，首次编译自动创建 build/。

源文件结构：
main.tex 为入口；book-adapt.sty 为模板适配；figure-dimensions.tex 保存图件比例；chapters/ 为正文（第 8 章按节拆分）；references.bib 保留原文参考文献顺序；index-zh.tex 为中文索引；glossary.csv 为统一术语表；assets/cover.png 为封面图。
elegantbook.cls 及 ELEGANTBOOK-LICENSE 随包提供。

校订记录（2026-11-14）：
全书对照 Clay Mathematics Monographs Vol. 4 原书 PDF 逐段修订，共 195 处正文 + 18 条参考文献，详见随包的《校订报告.md》与《校对记录/log_*.md》。本轮只改误译、漏译、术语与数学错误，不重写文风；译者对原书笔误的正确修正一律保留，并在日志中标注"原文疑误/译者补正"。
对照原文时请注意：译本页码与原书页码不可互推；源码中每个段落前有 `\SourceParagraph{id}{原书PDF页号}`，原书印刷页码 = PDF 页号 − 10。

工作流程：译文由模型直接阅读原 PDF 并逐段译录，未使用翻译软件、网站或翻译服务。第 8 章部分节及索引采用分工译录，由主代理统一术语与构建。

可选技术验证：安装 pypdf 并提供 pdffonts/pdftotext 后，可运行 tools/verify_final_pdf.py；普通编译不需要这些验证依赖。
