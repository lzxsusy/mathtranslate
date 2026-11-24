几何 Langlands 理论导论——完整中文译本

原PDF：LinChenGLC2023.pdf，共85页。
全书范围：原PDF第5页正文Introduction开始，至第83页References标题之前的第16章末，完整第1–16章，共119节。出版及讲义元信息不译；原书无独立前言。全部33条参考文献按原语言以LaTeX保留；新增可点击中文索引。
本批续译：第53页第10章至第83页References标题之前；前一批第1–9章已合并。

主文件：main.tex；正文：chapters/ch01.tex–ch16.tex。
模板：用户提供的ElegantBook-v4.7-source.zip中的elegantbook.cls；保留原生封面、字体和环境。正文11pt；数学New Computer Modern。TeX和bib文件UTF-8。
图示：images中的48个PDF矢量裁切，正文共49次使用。没有翻译或重绘图中文字；宽度按原图相对于原PDF页面612bp宽度的比例配置，保持各图长宽比。第16章带编号图式用LaTeX生成编号，并提供超链接。
封面：images/cover.png，由内置imagegen生成，校验为1536×1024、3:2；images/logo-blue.png为原模板标志。

编译：需要XeLaTeX、Biber、MakeIndex，以及ElegantBook、unicode-math、New Computer Modern、imakeidx等宏包。
在工程目录依次运行：
  xelatex -interaction=nonstopmode -halt-on-error main.tex
  biber main
  makeindex main.idx
  xelatex -interaction=nonstopmode -halt-on-error main.tex
  makeindex main.idx
  xelatex -interaction=nonstopmode -halt-on-error main.tex
Windows可运行build.ps1，自动编译到build目录。正文或引用修改后，如LaTeX仍提示重新运行，应再次编译。
全部章节引用均为译本内部链接；索引页码和文献回引有有效的页码锚点。references/original.pdf随包提供，供原文对照，编译不需要它。
交付PDF的所有字体均已嵌入，在其他设备阅读时无需安装中文或数学字体。重新编译时，中文字体由原生ctex字体方案按操作系统选择。
可选的audit/full_finalize.py只用于PDF压缩与额外验证，需要Python、PyMuPDF、Pillow和pdffonts；普通LaTeX编译无需这些工具。

2026-11-18 校订版（在初版译本上完成的整书校订）
- 正文改动 55 处：数学错误（ch03 Tate 扭转符号、ch15 权/余权颠倒、ch14 直和写成乘积、ch08 α_d、ch09/10/13 的 temp 上标、ch04 χ^λ、ch02 P^0）、
  增译与漏译（ch05/08/12/13/16）、术语统一（stratum=分层、infinite level=无限级、restricted variant=受限变体、chart=图卡、generic=泛）、翻译腔。
- 新增 59 条译注（transnote 环境，定义在 main.tex）：含糊点拨 44、易错预警 9、背景直觉 6；
  每条末句带 [来源：nLab 或 Stacks Project ...] 或 [依据：原书 p.N ...] 或 [译者按（上下文推断，无外部依据）]。
  书末「译注一览」（chapters/notes-index.tex，由脚本生成）列出全部条目的标题、类型与页码；main.tex 另需 multicol 宏包。
- 术语表 audit/glossary.txt 末尾「2026-11-18 校订批注」记录本轮的术语决定。
- 校订后全书 110 页（初版 98 页），label 集合与初版一致（141 个）。
- 改动明细见交付目录的 校对记录/改动对照.md；逐章审读记录见 校对记录 下的 chNN_issues.md 与 chNN_notes.md。

第二轮全书复核：audit/revision2-plan.md、audit/revision2-report.md和audit/revision2-review.json；补齐旧版遗漏的原83页末尾正文及图示，重新核验54个实际编译编号、全部119节和33条参考文献。
审校：audit/review.json记录首批72节；audit/review-continuation.json记录续译47节。audit/full-structural-check.json、audit/full-final-validation.json记录全书结构、字体和链接检查。恢复信息与术语表分别在audit/CORE.md、audit/glossary.txt。
源码压缩包不含构建、渲染缓存或临时Python依赖。

封面生成的完整提示词：
Generate one elegant academic mathematics book cover banner image, exact image canvas 1536 by 1024 pixels, landscape 3:2. This is the replacement illustration inside the native ElegantBook cover, NOT a whole book cover design. Subject inspired by geometric Langlands: a refined abstract algebraic Riemann surface, two gently flowing geometric surfaces in correspondence, a few fine luminous connecting filaments suggesting duality. Quiet ivory background, muted deep teal and slate blue, very restrained warm gold accents, smooth precise forms, soft sophisticated lighting, balanced generous negative space, uncluttered, modern scholarly beauty. No letters, words, equations, symbols, numbers, title, logo, watermark, border or book mockup. Output exactly 1536×1024.
