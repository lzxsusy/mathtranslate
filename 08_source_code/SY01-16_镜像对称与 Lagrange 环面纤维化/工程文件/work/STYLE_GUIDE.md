# JP03 中文译注本体例要点

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，保留权利，仅限非商业学术研读，权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

- chunks 只写片段：禁 `\documentclass`、`\usepackage`、`\begin{document}`、`\newcommand`、`\title`、`\tableofcontents`。
- `\section{…}` 对应原文「N 标题」，只在节起始页写一次；参考文献写 `\section*{参考文献}`。
- 编号公式逐条 `\begin{equation}…\tag{N}\end{equation}`；无编号公式用 `\[…\]`，绝不加号。
- 正文引用式号写「式 (5)」纯文本，不用 `\ref`；文献写 `[AAK]`、`[CPUa, Theorem 1.1]`，不用 `\cite`。
- 定理：`\begin{theorem}[{[CPUa, Theorem 1.1]}]`；原文「定理 5.1 ([CPUa, Theorem 1.2]).」译作定理环境 + 题注。
- 每页开头 `% ===== 原书 p.N =====`；chunk 末 `% CHUNK cNN DONE pages pXXX–pYYY`。
- 原文笔误照录，另起一行写 `% [Tutor Note: …]`（注释内不得再出现 `%`）。
- UTF-8 无 BOM、LF；全角中文标点；英文术语与数字两侧半角空格。
- 消灭「被……所」「进行……的」「对于……而言」；不用「我們」。
- 批注只有三类：易错预警、含糊点拨、背景直觉；每条给具体信息，禁空话。
