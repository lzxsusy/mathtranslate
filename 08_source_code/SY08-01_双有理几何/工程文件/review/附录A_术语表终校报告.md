# 附录 A 术语对照表终校报告

终校人：t02　　日期：2026-11-09
对象：`work/glossary.tsv`（428 条数据行）、附录 A（`src/chunks/appendix_glossary.tex`）、生成器 `work/tools/gen_glossary.py`

## 〇、结果总览

| 项目 | 终校前 | 终校后 |
|---|---|---|
| `work/glossary.tsv` 数据行 | 438 | **428** |
| 附录 A 条目 | 456 | **444** |
| 重复行（英文键＋日文键联合判重） | 10 行冗余 | **0** |
| 备注中「术语表未收」陈旧说明 | 14 条 | 0 |
| 备注中 `$…$` 被转义成字面 LaTeX | 6 条 | 0 |
| 附录中的生成器泄漏行（proposals 表头、`文件:行号`） | 3 行 | 0 |
| 排序违例 | 4 处 | 0 |
| `build.ps1 -Chunk appendix_glossary` | — | file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0 |

三档统计：**已修 47 条 / 建议修（正文侧）6 项（12 处）/ 待定 8 条**。

## 一、已修（47 条）

### 1. 日文栏改正（4 条）

| 英文键 | 原日文栏 | 改正 | 依据 |
|---|---|---|---|
| 1-complement | 1-补足 | 1-補足 | 日文用「補足」，原栏误作简体 |
| extremal contraction | 极收缩 | 端射線収縮 | 原栏整条为中文；备注本身已写「日文 端射線収縮」 |
| log resolution | 对数奇点解消 | 対数特異点解消 | 「対数」「特異点」，原栏为简体混写 |
| general point | 生成点（general point） | 一般点 | 原文「一般点」；generic point 才是「生成点＝泛点」，原栏把英文注塞进日文栏 |

### 2. 中译栏改正（6 条）

| 英文键 | 原中译 | 改正 | 说明 |
|---|---|---|---|
| dlt | 因子对数终端 | 除子对数终端 | 全书 divisor＝除子、factor＝因子；全称作「除子对数终端」（divisional log terminal） |
| Nakai--Moishezon criterion | 中井--Moishezon 判别法 | 中井–Moishezon 判别法 | 人名与拉丁名之间用连接号，不用双连字符 |
| general intersection theory | 一般交叉理论 | 一般相交理论 | 表内「交差＝相交」已冻结，此处未跟随 |
| deformation space with base condition | 附带基点条件的形变空间 | 附带底条件的形变空间 | 底条件（base condition）≠ 基点（base point） |
| pushforward | 推出 | 顺像 | pushforward 与「直接像／顺像」同义；「推出」在正文均作动词「derive」，易混 |
| dlt / divisional log terminal | （英文键混入全称） | dlt | 英文键只保留缩写，全称移入备注 |

### 3. 备注栏清理（20 条）

- 「术语表未收，正文 N 处」14 条：该语已入表，删去「术语表未收」「建议入表」等提案语气，只留出现次数与章节出处（spectral sequence、nef、homology、general fibre、threefold、indeterminacy point、surjective、injective、simple normal crossing、dualizing sheaf、contraction morphism、big、trace map、neighbourhood）。
- 备注含 `$…$` 6 条（put / set、over a field、Kodaira dimension、cone of curves、linearly equivalent、weight）：生成器会转义 `$`，正文显示成 `\$…\$` 与 `\textbackslash{}`，一律改为纯文本（`記号 κ`、`記号 NE(X)`、`記号 ≡ 或 ∼`、`A^n 的权 w` 等）。
- 备注中残留日文语句 4 条（stack、f-free、analytic family、subring）：改写成中文说明，原文引语保留引号。
- 冲突备注 3 条：`big` 旧备注前半仍写「下文单用『巨大』」，与新裁定 big＝大 矛盾，改为「术语作『大』；nef and big＝nef 且大；不用『巨大』」；`Step` 备注末尾重复「原书『段階』」删去；`dlt` 备注改为按 divisor＝除子 记录原書「因子ログ端末的」。

### 4. 重复条目合并（删 10 行）

按「英文键＋日文键联合判重」，同一日文底本术语只保留一条（以 glossary.tsv 为准，提案文件不覆盖）：

| 日文键 | 保留 | 删除 |
|---|---|---|
| 端錐面（3 行中文不一） | extremal face → **极锥面** | extremal cone face（极锥面）、`—`（极锥面） |
| 中山の補題 | Nakayama lemma | Nakayama's lemma |
| 主張 | claim | assertion |
| 双有理変換 | birational transformation | birational transform |
| フリップ収縮 | flipping contraction | flip contraction |
| 数値的同値 | numerical equivalence | numerically equivalent |
| 例外因子／例外曲線 | （合并进 exceptional divisor，备注记旧记法） | exceptional divisor / curve |
| 収縮（射） | contraction morphism（收缩态射） | contraction (morphism)（收缩（射）） |
| 自由（線形系） | basepoint-free（无基点） | basepoint free |

`端錐面` 依 t04 裁定与 ch03/ch06 正文统一作**「极锥面」**，「极面」不再用（正文侧尚存混用，见下）。

### 5. 生成器修复（`work/tools/gen_glossary.py`，3 处）

1. **过滤泄漏行**：proposals 文件的表头（`原文/中文/English/备注`、`现词/建议/位置/依据`）与校勘记录（`ch06a.tex:214（…）`）此前作为条目进入附录；现按「表头词、无拉丁字母、`文件:行号`」三种规则跳过。
2. **排序键去变音符**：`étale`、`écart` 等此前排到字母表末尾（Unicode 码位），现按 NFKD 去声调后排序，`étale` 归入 e 段。
3. **同日文键去重**：先 glossary.tsv 后 proposals，同一日文底本术语只取首次出现，杜绝提案文件重复立项、中文互相覆盖。

## 二、建议修（正文侧，共 6 项 12 处，未动正文）

| 术语 | 正文现状 | 建议 | 位置 |
|---|---|---|---|
| 收缩射 | 7 处（术语表定「收缩态射」） | 改「收缩态射」 | ch01c.tex 5、ch02a.tex 1、appendix_digest.tex 1 |
| 同型射 | 2 处 | 改「同构态射」 | ch07c.tex 1、appendix_index.tex 1 |
| 终端补题 | 2 处（应作「终端引理」） | 改「终端引理」 | ch05b.tex 1、ch05c.tex 1 |
| 极面／极锥面 | 极面 16 处、极锥面 13 处，混用 | 统一「极锥面」 | ch01b/c、ch02b、ch03a/b/c/d、index/notes |
| 一般纤维 | 27 处，兼表 general fibre 与 generic fiber | generic fiber 单独作「泛纤维」，其余保留「一般纤维」 | ch01b、ch03b/c、ch06c、ch07a–d 等 |
| 补题 | 3 处（残） | 改「引理」 | 见上「终端补题」及 1 处备注 |

核查结论：`推出` 28 处均作动词「derive／推出结论」，与 pushforward（已改「顺像」）无冲突；`坍缩` 0 处；`支撑` 10 处均为 supporting（支撑函数），与「支集＝support」不冲突；`系` 304 处均为「线性系／局部系／谱序列」等复合词，无「系 2.31」式孤立用法；`因子` 45 处除 appendix_digest 两处因子（factor）外均为「因子」旧称，正文正文（ch0x）已无「因子＝divisor」用法。

## 三、待定（8 条）

1. **假设**：`assume` 与 `assumption` 两行同译「假设」，词性可区分（假设／假定），暂留。
2. **约化**：`reduced`（被約→约化）与 `reduction`（還元→约化）同形，靠上下文区分，暂留。
3. **奇点消解**：`desingularization` 与 `resolution of singularities` 两英文键同译，属同义词分立，暂留。
4. **顺像**：`direct image` 与 `pushforward` 同译「顺像」（前者为层、后者为映射），拟在备注区分，待 lead 定。
5. **分岐点＝fork**：日文「分岐点」通常作 ramification point／分歧点，备注却写「不用分歧点」；原书 定義 4.6 的 fork 语境存疑，未改。
6. **固定点集合＝base locus**：日文栏作「固定点集合」而中译作「基点集」，疑原书应为「基点集合」；未见页图，未改。
7. **一般元＝general member**：中文「一般元」易与「一般点」混，暂留。
8. **极小模型的运行＝running the MMP**：拟作「极小模型纲领的実行／运行」，待 lead 定中文习惯。

## 四、交叉核对（抽 60 条，摘录关键 24 条）

逐条 `grep src/chunks/*.tex` 核对正文与表内一致（附录文件本身除外）：

| 术语 | 表内 | 正文计数 | 判定 |
|---|---|---|---|
| 除子 divisor | 除子 | 901 | 一致（`因子` 45 处为 factor 或旧称） |
| 态射 morphism | 态射 | 382 | 一致；`收缩射` 7 处例外 |
| 推论 corollary | 推论 | 285 | 一致；无「系 N」孤立用法 |
| 引理 lemma | 引理 | 402 | 一致；`补题` 3 处例外 |
| 支集 support | 支集 | 15 | 一致；`支撑` 仅 supporting |
| 泛点 generic point | 泛点 | 18 | 一致；`生成点` 0 |
| 翻模 flop | 翻模 | 195 | 一致 |
| 翻转 flip | 翻转 | 388 | 一致（含翻转收缩） |
| 终端 terminal | 终端 | 321 | 一致 |
| 标准 canonical | 标准 | 415 | 一致 |
| 丰度 abundance | 丰度 | 27 | 一致 |
| 丰富 ample | 丰富 | 324 | 一致 |
| 收缩 contraction | 收缩 | 376 | 一致；`坍缩` 0 |
| 极锥面 extremal face | 极锥面 | 13 | 与 `极面` 16 混用，见第二节 |
| 极射线 extremal ray | 极射线 | 141 | 一致 |
| 小收缩 small contraction | 小收缩 | 25 | 一致 |
| 标准奇点 | 标准奇点 | 79 | 一致 |
| 终端奇点 | 终端奇点 | 93 | 一致 |
| 极小模型 | 极小模型 | 201 | 一致 |
| nef | nef | 229 | 一致（保留拉丁） |
| 基点集 base locus | 基点集 | 16 | 一致；`固定点` 10 处为群作用固定点 |
| 大 big | 大 | 大除子 2 | 一致；旧「巨大」正文已清 |
| Cartier/Weil | 卡蒂埃？ | — | 表作「Cartier 除子」「Weil 除子」，正文一致 |
| 顺像 direct image | 顺像 | 4 | 一致；pushforward 亦作顺像 |

## 五、排序与体例

- **排序**：按英文键、忽略变音符号的字母序；`1-complement` 起、`Weil divisor` 止，无违例。
- **判重**：445 行数据中英文键唯一（联合日文键去重后 0 重复）；附录 444 条无重复英文键。
- **列宽**：longtable 四列 0.27 + 0.22 + 0.17 + 0.22 textwidth（合计 0.88），`overfull=0`，最长条目「a cyclic group acting freely in codimension 1」「minimal model program (MMP)」均正常换行。
- **编号与页眉**：`\chapter*` 不编号、加入目录；附录 A 共 22 页，表末「共收录 444 条」与实际行数一致。
- **编译**：`build.ps1 -Chunk appendix_glossary` 可直接编单块（不走整书），pass1/2 exit=0，LOG 五项全 0。

## 六、文件改动清单

- `work/glossary.tsv`：428 数据行（原 438）；47 条行级修改、删 10 行冗余。
- `src/chunks/appendix_glossary.tex`：重新生成，444 条。
- `work/tools/gen_glossary.py`：过滤泄漏行、去变音符排序、同日文键去重。
- 未改任何正文 chunk（正文侧问题列在第二节，交 lead 分派）。


## 七、待定 8 条的最终裁定（术语定版记录）

按 lead 定下的原则（数学正确第一、通行译法第二；同词异域以备注限定；无法一条定名者取主译＋异译）逐条裁定，均已在 `work/glossary.tsv` 落实：

| # | 待定项 | 最终裁定 | 备注栏写法 |
|---|---|---|---|
| 1 | fork＝分叉点 | 分叉点 | 定義 4.6；对偶图的树中连接至少 3 条边的顶点；与「分岐（ramification，分歧）」无关，故不用「分歧点」 |
| 2 | base locus | 基点集 | 原書作「固定点集合」；英文 base locus；亦作「基点集合」 |
| 3 | pushforward / direct image | 顺像 | 两条互注；层论作「顺像层」；不用「推出」（正文「推出」均作动词 derive） |
| 4 | reduced / reduction | 约化 | reduced 记除子/纤维/概形三例；reduction 问题化简语境作「归约」 |
| 5 | desingularization / resolution of singularities | 奇点消解 | 两条互注同义，正文统一「奇点消解」 |
| 6 | assume / assumption | 假设 | 按词性在备注区分，不另造译名 |
| 7 | general member | 一般元 | member＝元；区别于 general point（一般点／泛点） |
| 8 | running the MMP | 极小模型的运行 | 原書「実行」；亦作「实施」 |

另核定：`general fibre` 与 `generic fiber` 均作「一般纤维」（与正文 sweep 规则一致）。

## 八、端錐面 最终定名（定版：极锥面）

- 定名：**端錐面 → 极锥面**（英文 extremal face；英文底本亦作 extremal cone face）。依据：t01 核页图确认定義 1.15 作「端錐面(extremal face)」，与「端射線＝极射线」配套；字面可溯源（端＝极、錐面＝锥面），一术语一译名。
- `work/glossary.tsv` 该行中译定为「极锥面」，备注：「英文 extremal face；原书「錐面」指凸锥的面、「端錐面」指由负极射线张成的极面（extremal cone face）；本书统一作极锥面，配套 端射線＝极射线」。
- 已核：`錐面＝锥面（face of a cone）` 在位；`端射線＝极射线（extremal ray）`、`端的＝极端的（extremal）` 在位；glossary 内无独立「极面／極面」行；附录中译栏无「极面」，「极面」只出现在该条备注的释义句中；0 重复英文键。
- 历史：中途曾按「极面」定过一次（当时 t04 已按此改第 3 章正文），现撤回；正文的「极面」由 lead 统一 sweep 回「极锥面」，本报告以本节为最终记录。

## 九、附录 A 归一化去重（gen_glossary.py 别名表）

- 新增 `ALIASES` 别名映射与归一化去重键（英文键去括号、连字符、撇号-s 后比较；同义键并入 glossary 已有主条，别名追加进备注或在附录中合并为一行）。归并后附录 A **443 条**（此前 446 条，另含提案文件 272 次英文重键合并）。
- 实际归并清单（9 条）：

| 别名键（并入者） | 主条 | 处理 |
|---|---|---|
| base point free | basepoint-free | 合并为一行（同词异写） |
| exceptional divisor / curve | exceptional divisor | 并入，备注记「亦作 exceptional divisor / curve」 |
| contraction (morphism) | contraction morphism | 合并为一行（同词异写） |
| Nakayama's lemma | Nakayama lemma | 合并为一行（同词异写；备注已记亦作） |
| extremal cone face | extremal face | 合并为一行（备注已含英文底本写法） |
| flip contraction | flipping contraction | 同日文键优先拦下，映射表记录 |
| birational transform | birational transformation | 同上 |
| assertion | claim | 同上 |
| numerically equivalent | numerical equivalence | 同上 |

- **附录 A 定版状态**：443 条；`work/glossary.tsv` 428 数据行；0 重复英文键、0 重复日文键；`build.ps1 -Chunk appendix_glossary` pass1/2 exit=0，LOG file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0。
- 说明：〇节总览的「444 条」是首次定版数；其后其他译者更新 `work/proposals/`（t04 于 23:11、新增 t01_check 于 23:19）使条数一度为 446，再经本节归并后定版为 443 条。
