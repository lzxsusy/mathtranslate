# BRIEF —— 校对分工、页段与接续（v1.0，Lead 独占）

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

底本：Yuji Tachikawa, *N=2 supersymmetric dynamics for pedestrians*, arXiv:1312.2684v2（**194 页**）。
待校对稿：本目录（草稿 PDF 重建后 153 页左右；正文页另有浮动，以文件为准）。
原文英文源码：`work/ref/<块>-en.tex`（由 `dummies.tex` 按节切分，与 `sections/<块>.tex` 一一对应）。

## 一、分工表（Lead + 7 校对 + 1 工程）

| 块 | 拟校文件 | 原文页 | 原文章节 | 实测规模（原文标签/公式/图/脚注） |
|---|---|---|---|---|
| Lead | `00-introduction.tex` + `01-electromagnetic.tex` | pp.5–18 | Introduction；Prerequisites/致谢；Electromagnetic duality and monopoles | 标签 1+25；公式 0+51；图 0+1；脚注 1+2 |
| tr-01 | `02-multiplets.tex` + `03-renormalization.tex` | pp.18–35 | N=2 multiplets and Lagrangians；Renormalization and anomaly | 24+15；62+48；图 0；脚注 1+2 |
| tr-02 | `04-pure-su2.tex` | pp.35–50 | Seiberg-Witten solution to pure SU(2) theory | 32 标签；70 公式；11 图；3 脚注 |
| tr-03 | `05-one-flavor.tex` + `06-six-dimensions.tex` | pp.50–72 | SU(2) with one flavor；Curves and 6d N=(2,0) theory | 22+25；33+40；图 11+13；脚注 0+1 |
| tr-04 | `07-higgs.tex` + `08-two-three-flavors.tex` | pp.72–90 | Higgs branches；SU(2) with 2 and 3 flavors | 21+27；40+39；图 2+12；脚注 0+1 |
| tr-05 | `09-gaiotto.tex` + `13-conclusions.tex` | pp.90–110,170–173 | SU(2) with 4 flavors / Gaiotto duality；Conclusions | 43+1；75+0；图 18；脚注 2+1 |
| tr-06 | `10-argyres-douglas.tex` + `11-other-groups.tex` | pp.110–142 | Argyres-Douglas CFTs；Theories with other simple gauge groups | 30+30；48+96；图 10+9；脚注 1+1 |
| tr-07 | `12-su-n-duality.tex` | pp.142–170 | Argyres-Seiberg-Gaiotto duality for SU(N) | 64 标签；76 公式；33 图；1 脚注 |
| tr-qa | `A-instantons.tex` + `B-theory-zoo.tex` + 参考文献/索引/工程 | pp.173–194 | 附录 A、B；参考文献；索引 | 19+12；35+18；图 2；脚注 0+1 |

> 每块还附：① `work/ref/<块>-en.tex` 英文对照；② `work/probe/structdiff.md` 中该块的「缺失标签 / 低相似度公式」；
> ③ `work/page/<原文章节>.pdf`（如需要，可按 page 抽原文 PDF 页看排版）。

## 二、结构核查结论（2026-11-05 09:55 更正：**无缺口，不要补内容**）

> 早先 BRIEF 列出的「缺失公式/图/标签/小节」是**计数假象**：那些计数没有剥掉 `%` 注释行与 `\if0 … \fi` 恒假块。
> tr-qa 已按「剥注释 + 删 \if0」重算，并与 PDF 层交叉验证：**草稿与 v2 原文逐块完全一致，不要补任何东西**。

实测（v2 真计数 = 草稿计数）：section 16/16、subsection 57/57、equation 725/725、align 24/24、multline 8/8、
figure 122/122、table 3/3、footnote 18/18、`\cite` 命令 142/142、label 缺失 0/多余 0；
PDF 层公式编号去重 **793 vs 793** 且逐节相同（1:58, 2:65, 3:54, 4:74, 5:37, 6:40, 7:47, 8:41, 9:82, 10:48,
11:109, 12:79, A:43, B:16），图 122/122、表 3/3、参考文献 123/123。

具体「假缺口」的来源（**均不要补**）：
- `12-su-n-duality` 的 `fig:f-term-relation`：v2 源码里整段被注释掉，v2 PDF 也没有这张图；
- `09-gaiotto` 的 `\label{++++}`：v2 源码里不存在；
- `B-theory-zoo` 的「少 2 条 equation」：来自 v2 的 `\if0 … \fi` 块（恒假、不排版）；
- 「少 1 个 subsection」：v2 里该 subsection 被注释掉；
- 「`\cite` 少 7 处」「equation 少 6 条」「multline 少 1 条」：同样全部来自注释行或 `\if0`。

**若你已为这些"缺口"补过公式/图/label/小节，请立刻撤回到 v2 原样。** 结构已经对齐，精力全部放在内容校对。

## 三、边界与接续

- 各块是**独立文件**，不存在行内接缝问题；但**跨文件延续的编号**（公式/图/表/节）是全书的，校对时注意：
  1. `\numberwithin{equation}{subsection}`：同小节内公式编号连续，若补/删公式，必须与原文完全一致；
  2. 图/表编号 `\numberwithin{figure}{section}`：某节少一张图会导致全节图号错位——**每节图数必须与原文一致**；
  3. `\ref/\eqref` 引用目标必须存在（编译后 0 undefined reference）。
- **改哪个文件只动哪个文件**；发现别块的问题，写进回执，不代改。

## 四、开工必读（按顺序）

1. `work\STYLE_GUIDE.md`（硬规范）
2. 本文件 `work\BRIEF.md`
3. `work\glossary.tsv`（术语冻结表）
4. `work\TIMELINE.md`（边界与裁决记录）
5. `work\ref\<块>-en.tex`（你的英文对照）
6. `work\probe\structdiff.md`（自动对照：缺标签、低相似度公式、图表计数）

## 五、当前工程状态（Lead 已做，供你判断）

- 字体依赖已修（本机补装 cm-unicode，`preamble.tex` 不用改）；`build.ps1` 可一键编译（XeLaTeX+makeindex×3 遍）。
- 已把正文里作汉语句号用的半角「.」统一改成「。」（2574 处），数学环境内句点保持英文「.」；
  若你发现残留的半角句号（中文语境）→ 顺手改「。」。
- 参考文献 `references.tex` 与索引 `index.ist/index-terms.json` 由 tr-qa 负责核对，正文作者不要动。

## 六、回执

按 `STYLE_GUIDE.md` §8 六项，send_message 给 lead；并 complete 你的 task。
