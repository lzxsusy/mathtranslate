# STYLE GUIDE — SY02-44

本册译文遵循《数学文献翻译纪律》v2.1（`04_playbook/01_数学文献翻译纪律.md`），下面只记本工程的具体决定。

## 一、层与语气

- 目标读者：做代数几何/几何表示论的数学工作者，熟悉 D-模、叠、$\infty$-范畴的基本语言。
- 术语一律「中文（首次出现给英文）」：只译概念，不译记号。
- 保留英文原样的：Whittaker（人名/专名复合词「Whittaker 范畴」）、Eisenstein（「Eisenstein 级数」）、Borel、Plücker、Hecke、Ran、Artin-Schreier、Gap 定理（首次加「间隙定理」括注）、Drinfeld、Gaitsgory、Beilinson。
- 「Quasi-Theorem/Quasi-Proposition」译「拟定理/拟命题」，不作「准定理」。
- 原文用引号标出的临时说法（"space"、"category"、"closed embedding"）译作「空间」「范畴」「闭嵌入」并加引号，保留其「此处只是类比」的语气。

## 二、句法与标点

- 一句不超过 60–70 汉字；长句按逻辑切分，不靠逗号硬撑。
- 消灭「被……所……」「进行……的」「对于……而言」「起到了……的作用」。
- 全角标点；英文术语、数字与汉字之间加半角空格（如「DG 范畴」「17 页」「$G$-丛」）。
- 行内公式后的句号放在公式之后；公式内用半角逗号与句点。
- 破折号用「——」，不用「--」。

## 三、记号与字体

- 映射字母用 Fraktur：$\mathfrak p,\mathfrak q,\mathfrak i,\mathfrak j,\mathfrak r$，紧化加横线 $\bar{\mathfrak p},\bar{\mathfrak q}$。
- 遗忘/诱导/平均函子用粗直体：$\mathbf{oblv}$、$\mathbf{ind}$、$\mathbf{Av}$；$\mathrm{Av}$ 用直立体。
- 无衬线体留给 $\mathsf{QCoh}$、$\mathsf{IndCoh}$、$\mathsf{coeff}$、$\mathsf{Poinc}$。
- 直立体留给 $\mathrm{Eis}$、$\mathrm{CT}$、$\mathrm{Whit}$、$\mathrm{Rep}$、$\mathrm{LocSys}$、$\mathrm{Bun}$、$\mathrm{Hom}$、$\mathrm{Spec}$。
- 上下标一律放在正体宏之外：$D(\mathrm{Bun}_B^{rat})$、$\mathrm{Whit}(G)^{red,ext}_{glob}$、$\mathrm{Eis}^{spec,ref}$。
- 对偶群、对偶环面用 $\check G$、$\check T$、$\check B$。
- 张量积：一般用 $\otimes$；§2.3 的 $(H(X^\lambda,-)\boxtimes\mathrm{Id})$ 与原书同用 $\boxtimes$。
- 原书的单子记 $\widetilde\Omega$（Omega 上加波浪线），不用 $\Omega$。

## 四、编号

- 节号与原书一致（1–8），节下「编号段」用加粗 run-in（如 **1.2. 单子描述。**），编号由 `\ob` 宏显式给出。
- 定理类编号与原书一致（Lemma 2.2.1、Proposition 3.3.1、Quasi-Theorem 4.6.1……），由 `\othm` 宏给出。
- 公式只给原书编号的四条：(4.1)、(4.2)、(7.1)、(8.1)；其余公式不编号。
- 脚注 1–4 与原书对应（首页日期脚注另计）。

## 五、译注

- 体例：`\begin{annote} 正文 \par\vspace{0.15em}{\raggedleft 【来源：…】\par} \end{annote}`；左侧竖线、小字号、浅底。
- 只写三类：易错预警、含糊点拨、背景直觉。
- 每条必须带来源：A=原书/作者他文/经典教材/arXiv；B=nLab/Stacks Project/ProofWiki（须与 A 交叉）；I=本库已交付工程；无外部依据者写「译者按（上下文推断，无外部依据）」并在末尾注明「（A）」或「（I）」。
- 原书笔误的说明一律放在译注里，正文照原文译，不改写公式。

## 六、排版

- ctexbook，A4，11 pt，`openany`；正文不设 chapter，节号从 1 起。
- 字体 Noto Serif SC（正文）/ Noto Sans SC（标题、页眉）；AutoFakeBold 1.5、AutoFakeSlant 0.2（Noto Serif SC 无真粗体）。
- 页眉：偶数页书名，奇数页当前节标题；首页无页眉。
- 定理类环境用 amsthm，样式与原书一致（标题斜体、正文正体、右侧 $\square$ 结尾）。
