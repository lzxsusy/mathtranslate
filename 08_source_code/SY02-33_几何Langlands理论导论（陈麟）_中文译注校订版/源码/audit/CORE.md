# 核心任务与恢复记录

当前状态：第二轮全书对照审校和修订已完成；98页逐页视觉复核、字体和链接检查通过，干净副本独立复编98页逐页渲染一致，全部验证完成。先前“正文结束于82页、无遗漏”的结论不准确：原83页References之前的16.10结尾及1幅图遗漏，本轮已完整补齐并复核。旧审校记录为历史记录，本轮以revision2-review.json、revision2-report.md为准。

原书：C:/Users/Administrator/Downloads/LinChenGLC2023.pdf，共85页。模板：C:/Users/Administrator/Desktop/ElegantBook-v4.7-source.zip。工程：C:/Users/Administrator/Documents/ChatGPT/正在做的/LinChenGLC2023_CN_ElegantBook。
正文从原PDF第5页Introduction开始，至第83页References标题之前。原书无独立前言，出版元信息不译。完整16章119节；参考文献原83–85页33条，保留原语言。首批为1–9章72节；续批10–16章47节，本轮补齐83页末尾，不能将83页全部当成参考文献。

主助手亲自逐段翻译并对照原文，没有使用翻译软件或翻译网站。英文人名保留，术语统一见audit/glossary.txt。本轮再次完整对照全部段落、公式、33条文献，并查看全部98页及48幅矢量图。审校报告、计划保存在audit，不插入译本正文。

使用用户原生elegantbook.cls、字体、封面和环境；正文11pt、数学New Computer Modern。定理等54个带编号对象的类型和实际编译编号与原书一致；笔记采用note环境和共享原号；原6个例子不编号但使用原生例题环境。习题为练习、问题为问题、证明与解答使用原生环境。原6个有号公式(2.1)、(16.1)–(16.5)保留编号及内部超链接。目录、书签为原书两级关系。

本轮关键修订：补译原83页7段、5个陈列式及1幅图；修复3.10虚线箭头曾显示成99K的Unicode兼容错误；恢复11.5直和；去除额外说明、重复副标题；统一归一化、推前、加性特征标、幺幂根基、环路群、整体Langlands等；恢复149处原段落分隔；恢复Spec k[[t]]原书圆盘约定；修正两处越界、单行短页、1.1跨页残句和6.6正文靠近页码的问题。已确定的原书实质性笔误直接修正，译本不增加纠错说明。

封面图由内置imagegen生成，校验1536×1024、3:2。原图48个PDF矢量裁切、49次使用，原图文字不译、不重绘、不栅格化，仅设宽度保持长宽比。图宽与页面宽之比保持原比例：origimageunit=(439.2/612)*paperwidth，各图参数=原图宽/439.2。新增p083-whittaker.pdf裁切[198,189,411,263]。

最新交付PDF：output/pdf/LinChenGLC2023_CN_full.pdf，98页。源码包：output/LinChenGLC2023_CN_full_tex-images.zip（已独立复编验证）。首批部分译本保留。
验证：16章119节54个有号对象、33条文献、137个两级书签、761个有效链接；全部字体嵌入，PDF阅读无需安装字体；0缺字、0未定义引用、0重复号、0越界框、0书签字符串警告。优化PDF逐页渲染与编译原件一致。中文索引、正文引用、文献回引均有页码锚点，无外部PDF依赖。

多文件工程使用本地已安装XeLaTeX/Biber/MakeIndex，build.ps1自动编译到build。内置单文件编译器不支持此工程附加类和图片文件。主文件main.tex、chapters/ch01.tex–ch16.tex、references/bibliography.tex。保留main.tex中数学别名、math=cm、mathtools先于unicode-math、pageanchor=true，否则会出现字体或索引问题。
本地Python：C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe。PyMuPDF在audit/python-deps；QA工具须设置PYTHONPATH，该依赖不属于源码编译依赖、不进入压缩包。字体与结构验证：audit/full-final-validation.json、full-structural-check.json、full-fonts.txt；裁图audit/crops.json；最新计划和报告revision2-plan.md、revision2-report.md。

独立源码复编98页全部逐像素一致；源码、图片hash一致。收尾：根工程和干净复编副本均已执行latexmk -c，辅助文件清理成功；最终压缩包排除全部构建及渲染缓存。全书无待译正文，本轮审校修订完成。本地审校渲染缓存先前自动审批拒绝删除，原因为blocked by policy，不能改用别的方式绕过。压缩包必须排除所有构建、渲染缓存和临时Python依赖。保留真实审校记录与旧版备份。
