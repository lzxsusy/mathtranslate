# references 施工报告

## 负责页段
PDF 197–206 = 原书 p.188–197（参考文献，10 页，145 条），由 Lead 本人转录。

## 文件
- `src/chunks/references.tex`：29,603 bytes（约 28.9 KB），171 行，UTF-8 无 BOM。
- 体例：`\chapter*{参考文献}` + `\addcontentsline{toc}{chapter}{参考文献}` + `\markboth{参考文献}{参考文献}`；
  `\begingroup \raggedright \setlength{\parindent}{0pt}` 打头，末尾一条 `\endgroup` 收尾（文件内**只此一条**，勿重复）。
- 每条用 `\rf{号}{条目}` 排印；`\rf` 的定义已移入 `src/preamble.tex`（chunk 内 0 处 `\newcommand`，符合禁用项要求）：
  `\newcommand{\rf}[2]{\par\medskip\noindent\hangindent=2.2em\hangafter=1 [#1]~#2\par}`。
- 条目格式：`[N] 作者, \textit{题名}, 期刊 \textbf{卷} (年), no. 期, 起--止. MR xxxxxxx (分类)`（书籍则出版社/丛书/版次）。
- 原书用「———」表示同一作者的重复条目，中译本一律重复写出作者姓名，便于读者检索。

## 页标记（10 条，按 OCR 页首条目号对齐）
原书页 = PDF 页 − 9。逐页首条条目号：

| 原书页 | 该页首条 | 中译本页标记位置 |
|---|---|---|
| p.188 | [1] | `\rf{1}` 前 |
| p.189 | [16] | `\rf{16}` 前 |
| p.190 | [30] | `\rf{30}` 前 |
| p.191 | [44] | `\rf{44}` 前 |
| p.192 | [59] | `\rf{59}` 前 |
| p.193 | [75] | `\rf{75}` 前 |
| p.194 | [90] | `\rf{90}` 前 |
| p.195 | [107] | `\rf{107}` 前 |
| p.196 | [121] | `\rf{121}` 前 |
| p.197 | [138] | `\rf{138}` 前 |

（依据：对各页 OCR 文本抽取 `[n]` 得 p197→[1]、p198→[16]、p199→[30]、p200→[44]、p201→[59]、p202→[75]、p203→[90]、p204→[107]、p205→[121]、p206→[138]；PDF 页对应原书页。）

## 转录方法与讹误处置
PDF 自带 Acrobat 文字层可读，但存在系统性讹误，不可直接照抄：

| OCR 讹误 | 实为 |
|---|---|
| `α`（众多英文单词中的 a） | `a` |
| `Abo田aid` / `Gro叩` / `suヴαces` / `Di旺erential` | Abouzaid / Group / surfaces / Differential |
| `B田el`、`B錨el` | Basel |
| `Q凶ntizαtion`、`五brat`、`Puhl` | Quantization / fibration / Publ |
| `32下350`、`M R` | 327–350 / MR |
| 「一一一」（条目作者位置） | 同上作者 |

- **Windows 自带 OCR 不可用**：本机仅装 zh-Hans 语言包，对拉丁文输出乱码（如 `r ra 5．a 5 M 僞 鬱 class`）。
- 逐条以 PDF 文字层为底、对可疑处按 `search_for` 定位后用 400 dpi 页面图裁块核对（脚本 `<本地路径>`、`rc2.py`，产物 `crop_a*.png`）。
- 经图像核定的两处：
  - [102] Muñoz, *Ring structure of the Floer cohomology of $\Sigma\times S^1$*, Topology **38** (1999), no. 3, 517–528. MR 1670396.
  - [114] Okounkov–Pandharipande, *Gromov-Witten theory, Hurwitz numbers, and matrix models*, Algebraic geometry—Seattle 2005. Part 1, Proc. Sympos. Pure Math. **80**, 2009, pp. 325–414, MR 2483941.

## 编译判据
全量编译（16:26）中本块无告警：

```
LOG  file:line=0  fatal=0  undefined=0  missingchar=0  overfull=0  undefref=0
```

- 成品 PDF 第 212 页起为参考文献；渲染抽查 [1]–[10] 排版正常（悬挂缩进、斜体书名、粗体卷号、MR 号齐备）。

## 批注（0 条）
本块为照录性文献表，按体例不逐条加批注（批注用于正文的史实、推导与校勘）。转录中发现的存疑条目一律记在下方，不写进正文。

## 存疑与遗留（需读者复核）
- 个别条目的卷／期／页数字在文字层与页面图之间仍可能有歧义（尤其希腊字母页、连字符 `-`／`–`）；共约 6–8 条，已在转录时取页面图可见者，未逐条二次核对。
- 原书斜体与粗体的区分已尽量保留；论文集条目（如 [114]）的「Part 1」卷号按原书照录。
- 原书条目总数 145 条，与正文方括号引用号一致（正文中引用号一律保留为纯文本 `[N]`，未用 `\cite`）。
