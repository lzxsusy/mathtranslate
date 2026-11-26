# ARBITER BRIEF（glc 154 卡全量审计 · 第三独立仲裁）

你是本轮审计的**第三名独立仲裁员**。有一批卡在盲审中出现「一名审计员判 issue、另一名判 pass」的分歧。
你的任务：**独立**重新审这些卡，只凭卡片、本地中译源码、英文原文 PDF 自己判断——这些卡到底有没有错。

## 一、绝对禁止（违反即整批判定作废）

1. **不准读**任何人的结论：
   - `datasets/_audit/glc_full_2026-11-26/passA/`、`passB/`、`tiebreak/*.jsonl`、`compare*`、`issues.jsonl`、`fix_plan.json`、`fix_log.json`
   - `datasets/_audit/glc_full_2026-11-26/tmp/`（含 `lead_verdicts.md`、`notes/`、`packs/`、`mech.json`、`stats.json`）
   - `datasets/_audit/third_party_2026-11-26/passA|passB|confirmed|tiebreak/`
   - `11_card_audit/glc_full/`
2. **不准改任何卡**（只读）。唯一允许写的地方：`datasets/_audit/glc_full_2026-11-26/tiebreak/T1a.jsonl`（或 T1b）与 `datasets/_audit/glc_full_2026-11-26/tmp/notes/T1a/`（T1b 同理）。
3. **不准委派**给别人（不许再开 subagent）。
4. **不准用记忆/印象当证据**。外部资料只允许：`glc.pdf`、本地中译源码；nLab/Stacks 只能当强佐证。禁止 Wikipedia/博客/内容农场/模型记忆，禁止编造 URL、页码、引文。
5. **不要猜**。判 pass 就是 pass，别为凑数找问题；判 issue 必须能给出**逐字证据**。

## 二、材料位置（仓库根 `C:\Users\admin\Desktop\数译发布\gitee_shuyi`）

| 材料 | 路径 |
| --- | --- |
| 待仲裁卡清单 | `datasets/_audit/glc_full_2026-11-26/tiebreak/groups/T1a.txt`（T1b 同目录） |
| 卡片 | `datasets/glc/cards/concepts/<slug>.json` |
| 英文原文逐页文本 | `datasets/_audit/glc_full_2026-11-26/tmp/pages/pNNN.txt`（p001–p085；`p011.txt` = PDF 第 11 页） |
| 原文全文 | `datasets/_audit/glc_full_2026-11-26/tmp/glc.txt`（pdftotext -layout，4606 行） |
| 中译源码 | `08_source_code/SY02-33_几何Langlands理论导论（陈麟）_中文译注校订版/源码/chapters/ch01.tex … ch16.tex` |

- 读取大文件请用 `read` 工具；仓库内的文本用 `ops_inspect_local_file`。
- `python` 用 `C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe`；打印中文前 `export PYTHONIOENCODING=utf-8`。

## 三、页码口径（已实测，直接用，不要重新推导）

- **PDF 页 = 印刷页**（偏移 0）：PDF 第 11 页页眉印「11」。
- PDF 的 p.2–4 是目录；**p.5 起就是第 1 章正文**。
- 中译源码 `\srcpage{N}` 是分页标记：**标记行之后的文字属于印刷第 N 页**。但它会漂移，已实测：
  - `ch11.tex` 全文没有 `\srcpage{60}`（只有 57/58/59）；
  - `ch12.tex` 全文没有 `\srcpage{64}`（只有 60/61/62/63）；
  - `ch15.tex:65` 是 §15.4 标题，而 `\srcpage{74}` 在 `:77` → §15.4 实际在 **p.74**；
  - `ch16.tex:2` 的注释「原PDF第75页，第16章开始」**是错的**，但 `ch16.tex:12` 的 `\srcpage{76}` 正确 → 第 16 章起于 **p.76**；
  - `ch12.tex:110` 是 §12.6 标题、`\srcpage{63}` 落在 `:117` 的 note 句中 → §12.6 整节在 p.63。
- **PDF 自带目录对 §15.4 之后与第 16 章不可靠**（目录写 15.4→73、16→75，正文实测 74、76）。以**正文页眉/正文内容**为准。
- 判定页码对错只看一件事：**卡所引的那个定义/定理/公式/例句，实际印在哪一页**。若卡引的是某节标题或整段定义，看该标题/定义首句所在页。

## 四、逐卡怎么审（每卡 ≥3 条 checks）

三类都至少各一条：
1. **definition / theorem**：定义量词与适用范围、定理条件/方向/层级（定理有没有被说成猜想、方向有没有反、层级/编号对不对）、公式符号与归一化。
2. **sources**：`sources[].anchor` 指到的 TeX 行里是否真有卡所说的内容；`pages`/`pdf_pages` 是否覆盖该内容所在页；`theorems[].source` 的「原书 p.N」是否对；归因（作者/文献）是否对。
3. **internal**：卡内字段互相矛盾（summary vs definition vs key_points vs theorems vs pitfalls vs verification）、`related` 目标是否存在。

## 五、判定与输出

每卡一行 JSONL，写到 `datasets/_audit/glc_full_2026-11-26/tiebreak/T1a.jsonl`（T1b 写 T1b.jsonl）：

```json
{"n":1,"group":"T1a","reviewer":"arbiter-t1a","pass":"tiebreak","set":"glc",
 "id":"glc/concept/xxx","path":"datasets/glc/cards/concepts/xxx.json",
 "verdict":"issue|pass|unverifiable","confidence":"high|medium|low",
 "checks":[{"aspect":"definition|theorem|sources|internal|mathematical",
            "verdict":"ok|issue|na|concern","detail":"你查了什么、看到什么"}],
 "issues":[{"severity":"critical|major|minor","aspect":"...","field":"...",
            "card_says":"卡里的逐字原文","problem":"...","should_be":"...",
            "evidence":[{"kind":"pdf|tex|derivation","ref":"p012.txt L4 或 ch03.tex:68","quote":"逐字引文"}]}],
 "unverifiable_aspects":[],
 "notes":"一两句"}
```

- `verdict=issue` 当且仅当卡对 E1 来源有**错误断言**（页码/编号/引文/归属/定义/定理内容/自相矛盾）。`verdict=pass` 表示没找到错误。
- `severity`：critical=结论反了/定义恒真或恒假/核心公式符号错；major=定理条件/方向/关键因子错、出处无法定位、例子算错；minor=页码/节号笔误、术语、related 断链。
- **解释性措辞、风格、记号选择、等价改写不算错**；底本自身的问题（如 `\srcpage` 漂移、`ch16.tex:2` 注释错）不算卡错，**除非卡照抄了错页码/错话**。
- `card_says` 必须是卡 JSON 里的**逐字子串**（去掉空白后仍要是子串）。
- 你**不需要**猜另一名审计员说了什么；只记录你自己独立发现的问题。若你判 pass，就写 pass。
- 写完跑校验器，必须 0 error：
  `python datasets/_audit/glc_full_2026-11-26/tools/check_audit.py --file datasets/_audit/glc_full_2026-11-26/tiebreak/T1a.jsonl --group T1a --list datasets/_audit/glc_full_2026-11-26/tiebreak/groups/T1a.txt --reviewer arbiter-t1a`
- 每审完 2 张就把已完成的写入 JSONL（防丢），顺序严格按清单行序，`n` 从 1 连续。
- 结束时回一条消息：`完成 N/M；issue X；pass Y；unverifiable Z；校验器 0 error` + 逐行 `卡id — field — severity — 一句话`。
