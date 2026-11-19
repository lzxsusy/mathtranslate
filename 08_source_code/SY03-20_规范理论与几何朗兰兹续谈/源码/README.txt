《规范理论与几何朗兰兹续谈》中文译文 LaTeX 源文件
==================================================

原作者：Edward Witten
原文题名：More On Gauge Theory And Geometric Langlands
版本：arXiv:1506.04293v3，2017 年 7 月 28 日

本目录包含完整中文正文、原文参考文献、术语索引、两张矢量图、规定字体、
编译入口及 PDF Unicode 映射补全工具. 所有项目资源均通过相对路径引用，
无需原工作区，也无需在系统中安装本包提供的 OpenType 字体.

一、环境要求
------------

1. 完整 TeX Live，或具备以下包的其他 XeLaTeX 发行版.
   本稿已使用 TeX Live 2023 的 XeTeX 0.999995 编译核验.
   XeLaTeX、makeindex 与原生 PDF 后端 xdvipdfmx 须可从命令行直接调用.

   直接依赖的常用包：geometry、fontspec、xeCJK、amsmath、amssymb、
   amsthm、mathtools、bm、upgreek、slashed、url、graphicx、amsfonts、
   xr、eucal、titlesec、tocbibind、imakeidx、hyperref、bookmark、cleveref.
   请使用这些包相互兼容的发行版本. 原 Computer Modern / AMS / Euler
   数学字体及其 TeX 字体映射由 TeX 发行版提供.

2. Python 3.10 或更新版本.

3. PDF Unicode 补全所需的 Python 包：PyMuPDF、pypdf、fonttools.
   已验证的具体版本记录在 unicode_tools/requirements.txt.
   在本目录中运行：

   python -m pip install -r unicode_tools/requirements.txt

   构建脚本不会自动安装软件、联网下载资源或启用 shell-escape.

二、编译
--------

Linux / macOS：

   bash build.sh --verify-render

Windows，或直接使用 Python：

   python compile.py --verify-render

脚本从自身所在目录定位全部资源，即使从其他目录调用也可使用.
它将先检查字体文件，再循环运行 XeLaTeX 和 makeindex，直到目录、
交叉引用、参考文献回链与索引页码稳定. 各轮 XeLaTeX 使用 -no-pdf
输出原生 XDV，收敛后显式调用 xdvipdfmx 一次，并检查其退出码、PDF
结束标记、非空页数与文件稳定性，再以完整文件替换 main.pdf，最后
补全 PDF 的 Unicode 映射. 全程使用 XeLaTeX 的原生排版及 PDF 后端.

完成后，主要文件为：

   Witten_Geometric_Langlands_ZH.pdf
       补全 Unicode 映射的成品 PDF，可用于阅读、复制与分发.

   main.pdf
       XeLaTeX 直接输出，保留用于与 Unicode 补全版本核验.

   Witten_Geometric_Langlands_ZH.unicode-audit.json
       字体嵌入、正文流、链接、书签与可选逐页像素比较的核验结果.

所有 LaTeX 中间文件、索引文件及编译日志保存在本目录中.
如只需 XeLaTeX 原始输出，可使用：

   python compile.py --tex-only

此选项仍需要 PyMuPDF 以核验输出 PDF 的完整性.

省略 --verify-render 时，仍核验字体程序、页面内容、链接、书签和元数据
不变，仅跳过逐页渲染像素比较. 若首次编译缺包或引用未收敛，请查看
main.log 及 main-build-*.txt.

三、文件结构
------------

   main.tex                 文档入口、标题、摘要及正文组合
   preamble.tex             字体、版式、数学宏、链接、索引配置
   part1_zh.tex             第 1 节至第 2.6.3 小节
   part2_zh.tex             第 2.6.4 小节至第 3 节
   part3_zh.tex             第 4、5 节
   part4_zh.tex             第 6、7 节及原文致谢
   bibliography.tex         原文参考文献与引用页回链
   index.ist                术语索引点线引导与链接格式
   gla8-1.pdf, gla8-2.pdf    保留矢量文字与嵌入字体的原图
   appendix_notes.tex       附录 A 译注汇总（由 工程文件/tools/gen_appendix.py 生成）
   appendix_glossary.tex    附录 B 中英术语对照表（同上，机械生成）
   compile.py, build.sh     可移植构建入口
   unicode_tools/           Unicode 补全工具、数据与 Python 依赖版本

四、字体与版式
--------------

中文正文使用 FandolSong，粗体使用相应真实粗体；标题使用 FandolHei.
FandolKai 用于指定楷体命令. 中文处于斜体环境时保持对应直立字形，
不生成伪斜体. 西文正文使用 CMU Serif，西文标题使用 Latin Modern Sans，
URL 等等宽文字使用 Latin Modern Mono.

【2026-11 校订译注版改动】本包不再随附字体：原先 fonts/ 下 15 个
OpenType 字体（29 MB）已移除，preamble.tex 改由 kpathsea 从 TeX 发行版
解析（TeX Live / MiKTeX 的 fandol、cm-unicode、lm 包；实测 MiKTeX 26.5
可编译）。同时新增 booktabs / longtable / enumitem / xurl 四个宏包，
\transnote{} 译为脚注「译注｜」，附录 A/B 由各 part 文件机械生成，
正文末尾为中文概念索引.

数学公式保留原文 Computer Modern / AMS / Euler 字体与原数学宏.
文档使用 article、letterpaper、reqno、11pt、四边 1 英寸页边距与
1ex 段间距，公式按原文章节编号. 页码位于页脚中央，目录、交叉引用、
参考文献回链与双栏术语索引均可点击，链接无可见边框.

字体的版权和再分发条件以 licenses/ 中的原始文件为准.

五、Unicode 补全工具
-------------------

也可对本项目编译得到的 PDF 单独运行：

   python unicode_tools/add_unicode_maps.py main.pdf result.pdf --verify-render

输入与输出须为不同文件. 工具以增量方式添加 ToUnicode 映射，保留输入
PDF 的全部原始字节前缀、页面内容流、嵌入字体程序、链接、书签和元数据.
若遇到无法确定的字符映射，它将报错而不会猜测字符.

工具所需的数据已包含在 unicode_tools/resources/：

   cmaps/Adobe-GB1-UCS2
   glyphlist/glyphlist.txt
   glyphlist/pdfglyphlist.txt
   glyphlist/texglyphlist.txt

各资源保持其原始内容与版权声明，附加许可文件位于 unicode_tools/licenses/.
字体嵌入使最终 PDF 的显示无需依赖接收设备的本地字体. 数学公式的视觉
排版完整保留；复制复杂数学排版时仍由阅读器决定其线性文字顺序.
