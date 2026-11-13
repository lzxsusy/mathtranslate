N=2 超对称动力学入门
Yuji Tachikawa
对应原文：N=2 supersymmetric dynamics for pedestrians
arXiv:1312.2684v2，2014 年 5 月 22 日

文件结构
main.tex                主文档
preamble.tex            版式、字体、链接及编号设置
macros.tex              数学宏命令
sections/               正文第 0–13 节及附录 A、B
references.tex          参考文献
figures/                原文矢量插图
young-kugo.sty          Young 图宏命令
index.ist               双栏术语索引的点线样式
index-terms.json         术语及排序键
texglyphlist.txt         数学字形的 Unicode 映射文本
build.sh                编译脚本

编译
需要 XeLaTeX、makeindex 和源文件所用的 LaTeX 宏包，以及 Fandol、CMU Serif、Latin Modern 字体.
字体文件不包含在本压缩包内，须由本地 TeX 环境提供.

在本目录运行：
  xelatex -interaction=nonstopmode -halt-on-error main.tex
  makeindex -s index.ist main.idx
  xelatex -interaction=nonstopmode -halt-on-error main.tex
  xelatex -interaction=nonstopmode -halt-on-error main.tex

Linux 或 macOS 也可直接执行：
  bash build.sh

生成文件为 main.pdf. 修改正文导致分页变化后，应再次执行上述完整编译序列.
请在 main.tex 所在目录执行编译，保留 texglyphlist.txt，以供 XeLaTeX 的 PDF 输出程序读取数学字符映射.
