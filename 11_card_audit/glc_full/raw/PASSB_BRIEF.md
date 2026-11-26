# Pass B 盲审说明书（glc 全量卡审计 2026-11-26）

你是独立盲审员。你**只拿到卡片路径清单**，不知道上一轮（Pass A）任何人说了什么、判了什么。
你的判断必须完全从**卡片本身 + 本地中译源码 + 英文讲义 PDF**重新做出来。不要试图推测「这里会不会有人已报过问题」。

## 一、硬约束（违反即作废）

1. **禁读**：`datasets/_audit/glc_full_2026-11-26/passA/`、`passB/`（除你自己的组文件与输出）、`tiebreak/`、`compare.*`、`issues.jsonl`、`fix_log.json`、`tmp/notes/A*/`；以及 `datasets/_audit/third_party_2026-11-26/` 下的 `passA|passB|confirmed|tiebreak` 目录。也不要读其他 B 组员的输出。
2. **不改卡**：仓库 `datasets/glc/cards/**` 只读。
3. **不伪造证据**：每条 issue 的 `evidence[].quote` 必须是你在 PDF 页文本或 TeX 源码里**逐字看到**的字符串（可以截断，但必须连续；不要自己重排公式、不要翻译）。`card_says` 必须是卡 JSON 里逐字存在的子串（去掉换行/空白后可比）。
4. **只做本组**：不许抽样、不许跳卡；按组文件顺序逐张来。
5. 仓库根 = `C:\Users\admin\Desktop\数译发布\gitee_shuyi`。所有相对路径从仓库根算。

## 二、必读材料

- 规范：`11_card_audit/WORKFLOW.md`（铁律、证据等级、severity）、`datasets/_audit/third_party_2026-11-26/AUDIT_HANDBOOK.md`（JSONL schema、判定口径）、`11_card_audit/casebook/SHOWCASE.md`（失效模式）。
- 集口径：`datasets/glc/README.md`（154 卡、16 章 119 节、页码偏移 0、2026-11-18 已修 9 处——**这 9 处若已改对不报**）。
- 卡片：清单里的 `datasets/glc/cards/concepts/*.json`。
- 中译源码：`08_source_code/SY02-33_几何Langlands理论导论（陈麟）_中文译注校订版/源码/chapters/chNN.tex`，以及 `源码/main.tex`（宏定义，如 `\Qell`）。
- 英文一手：`datasets/_audit/glc_full_2026-11-26/tmp/glc.pdf`（85 页，PDF 页 = 印刷页，偏移 0）；逐页纯文本 `tmp/pages/pNNN.txt`（pNNN 就是 PDF 第 N 页）；全文 `tmp/glc.txt`。
- 现成材料包：`tmp/packs/<slug>.md`（slug = card id 去掉 `glc/concept/`），内含卡片 JSON、anchor 指向的 TeX 切片（带行号）、`pages` 附近的英文页文本、related 目标核查。**材料包只是省翻页，不等于证据**；有怀疑就回原始文件逐字核对。

## 三、页码口径（E1 级结论，务必照此判）

- **PDF 页 = 印刷页**（已实测：PDF 第 11 页页眉印 11）。引用页码一律以 PDF **正文页眉/正文**为准。
- 中译源码的 `\srcpage{N}` 是编者插入的分页标记，**会漂移**：标记可能早一段或晚一段，也可能整页缺失（已在 ch11 缺 p.60、ch12 缺 p.64、ch15/ch16 的章节起点观察到）。**不要拿 `\srcpage` 当页码证据**；它只能当线索，最终以 PDF 正文为准。
- PDF 自带目录（p.2–4）对最后几章（§15.4 之后、第 16 章）与正文**不一致**，同样只作线索。
- 卡里 `sources[].pages` 与 `pdf_pages` 是列表；判定「页码错」的标准是：**卡自己的定义/记号/定理/公式/引文所在的那一页**不在列表里（背景性上下文落在别页不算；已覆盖主对象、只是没列全某段背景，按可接受处理并写进 note）。

## 四、逐卡检查清单（每卡至少 3 条 checks，必须覆盖三类）

- `aspect: "definition"`（或 `"theorem"`）：定义量词/适用范围、定理条件/方向/层级（定理 vs 猜想 vs 定义）、公式符号/归一化（移位 `[dk]`、Tate 扭转 `(dk/2)`、系数域、对偶方向）、归因（谁证的、哪篇文献）。
- `aspect: "sources"`：`sources[].section/pages/pdf_pages/anchor` 与 PDF 正文、TeX 源码是否对得上；`theorems[].source` 的编号/页码；anchor 行号是否真的覆盖所述内容。
- `aspect: "internal"`：summary/definition/key_points/formulas/theorems/pitfalls/related 之间是否自洽（同一事实不能两种说法）；`related` 目标是否存在；`verification.checks` 里是否残留与正文冲突的旧结论（注意：`verification` **只能当线索**，不能当证据）。

每卡判定：`verdict` ∈ `pass | issue | unverifiable`；`confidence` ∈ `high | medium | low`。
check 的 `verdict` ∈ `ok | issue | na | concern`（`ok`=核对通过；`issue`=这条查出问题；`na`=该方面不适用；`concern`=可疑但证据不足）。

**不是错的东西（别报）**：解释性措辞与风格；等价改写；自洽的记号约定；底本自身的缺陷（例如讲义把 §15.4 编在目录 73 而正文 74）——除非卡歪曲了底本；`sketch` 证明没有细节（有 `gap_note` 就不算缺证明）；「讲义未编号」的诚实标注。

**算错的东西（要报）**：定义量词错/适用范围被放宽或收紧；定理条件缺失或方向反了；定理/猜想层级被改；核心公式系数、移位、扭转、对偶错；页码/编号/引文与一手原文不符；归因错误；术语张冠李戴；卡内字段互相矛盾；`pages` 漏掉卡自己引用的那一页。

severity：`critical`（结论反了/定义恒真恒假/核心公式符号错）、`major`（定理条件/方向/关键因子错，定理编号或出处无法定位，例子算错，适用范围被实质放宽/收紧）、`minor`（页码/节号/术语笔误、related 断链、措辞精度问题）。

## 五、输出

- 文件：`datasets/_audit/glc_full_2026-11-26/passB/B<n>.jsonl`（一行一卡，行序 = 组文件行序）。
- 每行字段（固定）：`n, group, reviewer, pass, set, id, path, verdict, confidence, checks[], issues[], unverifiable_aspects[], notes`。
  - `group` = `reviewer` = `B<n>`（如 `B1`），`pass` = `"B"`，`set` = `"glc"`，`id` = 卡 JSON 的 `id`，`path` = 组文件里的路径。
- `issues[]` 每项：`severity, aspect, field, card_says, problem, should_be, evidence[]`；
  `evidence[]` 每项：`kind`（`pdf` / `tex` / `card`）、`ref`（如 `glc.pdf PDF p.36`、`ch05.tex:114-123`）、`quote`（逐字）。
  `field` 用 `definition.text`、`theorems[0].source`、`sources[0].pages`、`key_points[2]` 这种路径写法。
- `notes` 一句话写这卡的核对范围与你没查清的地方。
- 自检：`python datasets/_audit/glc_full_2026-11-26/tools/check_audit.py --file datasets/_audit/glc_full_2026-11-26/passB/B<n>.jsonl --list datasets/_audit/glc_full_2026-11-26/passB/groups/B<n>.txt --reviewer B<n>`，必须 `0 errors`（warning 尽量也清零）。每写完 3–5 张就 append 落盘一次，不要攒到最后。

## 六、收尾消息格式

`完成 N/M；pass X；issue Y；unverifiable Z；校验器 0 error；最严重问题一句话`，然后逐行列出你判 issue 的卡：`id — field — severity — 一句话`。
