# 工程简报（BRIEF）——《朗兰兹纲领与共形场论讲义》中文译注本

## 一、这是什么

Edward Frenkel 2005 年讲义 *Lectures on the Langlands Program and Conformal Field Theory*
（arXiv:hep-th/0512172v1）的中文**译注本**，加上一本配套的**读书笔记**。

底本不是 PDF 重打，而是 arXiv 提供的原始 LaTeX 源码（`work\houches.tex`，9,222 行），
因此正文、公式、编号、脚注、参考文献与原文逐字对应。

## 二、目录结构

```
<本地路径>
├─ docs\
│   ├─ BRIEF.md        本文件
│   ├─ STYLE.md        翻译体例（译者必读，逐条执行）
│   └─ TERMS.md        术语译名对照表 262 条（译者必守）
├─ latex\
│   ├─ main.tex        主文件（结构、章节标题、\input 顺序）
│   ├─ main_smoke.tex  英文预编译版（查错用，勿改）
│   ├─ preamble.tex    导言区（中文排版配置，由 work\gen_preamble.py 生成，勿手改）
│   ├─ en\<id>.tex     英文原文块（17 块，只读）
│   ├─ ref\<id>.txt    旧中译对应文字（只读，措辞参考）
│   ├─ tex\<id>.tex    ★ 译者产出：中文译文块
│   ├─ tex\biblio.tex  参考文献（已生成）
│   └─ front\
│       ├─ matter.tex  译本说明 + 阅读指南（Lead 写）
│       └─ terms.tex   术语表（由 work\gen_front.py 生成）
├─ notes\
│   ├─ nlab\           nLab 概念条目摘编（研究线 1）
│   ├─ discussion.md   互联网讨论 / 后续发展（研究线 2）
│   ├─ part1.md        读书笔记·第一部分（写作线 1）
│   ├─ part2.md        读书笔记·第二部分（写作线 2）
│   └─ part3.md        读书笔记·第三部分 + 末章（写作线 3）
├─ reports\            各工序 QA 报告
├─ work\               脚本与中间产物（勿动）
└─ 成品\               最终 PDF
```

## 三、17 个译文块与内容

| id | 原文行 | 字符 | 内容 |
|---|---|---|---|
| e00 | 216–559 | 19.7K | 引言 |
| e01a | 577–1043 | 24.3K | §1.1–1.4 伽罗瓦群 / 阿贝尔类域论 / Frobenius |
| e01b | 1044–1657 | 31.1K | §1.5–1.7 非阿贝尔推广、GL₂ 自守表示、椭圆曲线 |
| e02 | 1659–2294 | 32.4K | §2 从数域到函数域 |
| e03a | 2318–2883 | 31.1K | §3.1–3.4 几何猜想、阿代尔与向量丛、层、反常层→D-模 |
| e03b | 2884–3432 | 28.2K | §3.5–3.8 D-模例子、Hecke 对应、Hecke 本征层与猜想 |
| e04 | 3434–3958 | 27.5K | §4 几何阿贝尔类域论（Deligne、Fourier–Mukai） |
| e05 | 3960–4543 | 31.3K | §5 从 GLₙ 到一般约化群、几何 Satake |
| e06 | 4545–5124 | 31.2K | §6 C 上的几何朗兰兹猜想、双参数形变、D-膜 |
| e07a | 5156–5625 | 25.4K | §7.1–7.3 共形块、共形块层 |
| e07b | 5626–6004 | 21.2K | §7.4–7.6 扭化 D-模、WZW D-模 |
| e08a | 6006–6559 | 26.0K | §8.1–8.3 临界水平手征代数、中心、oper |
| e08b | 6560–7083 | 26.1K | §8.4–8.6 回到中心、自由场实现、T-对偶 |
| e09a | 7085–7600 | 27.1K | §9.1–9.4 用共形块构造 Hecke 本征层 |
| e09b | 7601–8030 | 22.0K | §9.5 Hitchin 系统的量子化 |
| e09c | 8031–8195 | 8.7K | §9.6 向其他局部系统推广 |
| e09d | 8196–8747 | 26.0K | §9.7–9.8 分歧与抛物结构 |

## 四、编译

```powershell
$tex="<本地路径>"
$env:PATH="$tex;$env:PATH"
Set-Location "<本地路径>"
& latexmk -xelatex -interaction=nonstopmode main.tex
```

- **latexmk 结尾常报 `[exit code: 1]` 与 "you have not checked for MiKTeX updates"，这是 MiKTeX 的更新提醒，不是编译失败**；判断依据是 `Output written on main.pdf (N pages)` 与日志里有没有 `! ` 开头的错误。
- 索引由 `\makeindex` + `\printindex` + 正文的 `\index{}` 生成，latexmk 会自动跑 makeindex。
- 缺字/缺图/公式断行：先看 `main.log` 的 `! ` 与 `Overfull`。

## 五、工序与分工

1. **翻译（当前阶段）**：译者按 id 交付 `latex\tex\<id>.tex`。只译文字，数学原样，不写译注。
2. **nLab 概念条目**：研究员产出 `notes\nlab\*.md`，每条：概念名、一句话定义、来历（谁在什么语境下引入）、在本书哪一节出现、为什么原文没解释它。
3. **互联网讨论**：研究员产出 `notes\discussion.md`：对本文的评论、引用语境、后续综述（2006 年以后）。
4. **读书笔记**：三位作者分三部分写 `notes\part1.md` / `part2.md` / `part3.md`（Markdown，数学用 `$...$`）。
5. **译注插入**：以 nLab 条目为据，在译文里插 `\begin{zhunote}...\end{zhunote}`，每块 2–4 条。
6. **总装**：编译、页面对账、公式回图核对、成品 PDF 归档 `成品\`。

## 六、硬规矩（所有人）

- 不要用 PowerShell 读写源码文本（编码会把中文弄坏）；用 read/write/edit 工具。
- 不要改别人的文件；写作用域见各自任务卡。
- 不要动 `latex\en\`、`latex\ref\`、`work\houches.tex`、`preamble.tex`。
- 交付必须是 UTF-8、能被 xelatex 直接 `\input` 的文件。
- 拿不准的地方不要停：按最合理的判断做完，把疑问写进 `reports\<id>_questions.md`。
