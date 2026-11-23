# kb 插件测试笔记（SY05-30 施工期间）

测试对象：本机 DSH 的 kb 插件，数据目录 `C:\Users\admin\.dsh\profiles\desktop\node_modules\dsh-kb\data`（包内自带数据：`data/cards` 3.2 MB、`data/src` 5.2 MB、`data/zh` 7.8 MB）。
只读接口：`kb_stats / kb_search / kb_brief / kb_card / kb_source / kb_zh`。
目的：验证它在「译一本全新的书」时能不能当检索工具用——具体地说，能不能在**动笔前**告诉我「本库有没有讲过这个话题、讲过什么、译名用过什么」。

## 测试记录

| # | 调用 | 输入 | 结果 | 判定 |
| --- | --- | --- | --- | --- |
| 1 | kb_stats | — | 2,897 卡 / 51 部；draft 1,947、checked 846、verified 104；带页码 1,327；原文层 7,644 段 / 33 工程；译文层 48,595 段 / 83 工程 | ✅ 一屏看清家底，比翻 51 个 jsonl 省事 |
| 2 | kb_brief | `Klein 曲面 实代数曲线 基本群 实结构`（4 词） | 「库里没有已核卡片覆盖这个主题」 | ❌ **误导性判断**：同一库的原文层明明 20+ 段命中（见 #3），`kb_brief` 只查卡片层且是严格 AND，于是把「卡不够」说成「没覆盖」 |
| 3 | kb_search | `Klein surface`（layer=all, limit=8） | 卡片层 8 条全是 Hirzebruch 曲面、面算符、分次曲面这类**边角命中**；译文层命中 SY05-08「不可定向曲面 / 克莱因瓶」；原文层命中 SY02-02 p.30 的 Klein 分类段落 | ❌ 卡片层**召回噪声**：多词查询像 OR，返回一堆只共享 surface 一词的卡；反而真正相关的层（原文/译文）要往下翻才见 |
| 4 | kb_search | `real structure 实结构` | 0 张已核卡，提示「译文层 7 段、原文层 20+ 段命中」 | ✅ 这次的提示语是对的（至少告诉了人去哪层看） |
| 5 | kb_search | `real algebraic curve fundamental group`（include_draft=true, limit=6） | 仍是「没有命中已核卡片」 | ❌ 见问题 2：`include_draft` 生效与否无法从输出判断，提示语也没跟着变 |
| 6 | kb_search | `Higgs 丛`（include_draft=false vs true） | 两次输出**逐字相同** | ❌ 见问题 2（后来用 #8 证明了 flag 本身是通的，但 #6 这个对照实验无法区分「flag 没生效」和「确实没有 draft 命中」） |
| 7 | kb_card | `SY02-22.term.higgs-丛` | 完整术语卡：`Higgs bundle → Higgs 丛（依据 A）`，复核记录 `{"drafter":"gen2","reviewer":"","blindtest":"pending","rounds":1}` | ✅ 术语卡格式干净，能直接拿来定译名 |
| 8 | kb_search | `晶体 六步`（先 false 后 true, limit=3） | false 时 3 条已核卡；true 时第 2 条变成 `sy29.concept.f-isocrystal`，标「未复核」 | ✅ 确认 include_draft 真的生效——但结果**顺序会变**，同一查询两次结果不同，引用时容易记错 |
| 9 | kb_source | `SY02-02, page=30, around=1` | 整页原文 + 前后各一段；命中内容正是 Klein 对实结构分类的 $(n,a)$ 不变量表述 | ✅ **本次最好用的一个**：底本原文整页调出，比翻 PDF 快；而且它证明本书 §2.1.2 的 $(g,k,a)$ 与另一本书的 $(n,a)$ 是同一分类 |
| 10 | kb_zh | `SY05-08, para=101, around=0` | 返回段 99–103（前后各 2 段）——`around=0` 没有生效 | ❌ 参数被忽略：`around` 传 0 仍给前后各 2 段，与「只读这一段」的预期不符 |

## 确认的问题

1. **`kb_brief` 只看卡片层，0 命中时把「卡不够」说成「库里没有」**（#2）。这是本次最影响工作流的一条：译前检索的第一步就是 `kb_brief`，它一摇头，人就会以为这本书在本库是空白，从而放弃查既有译法。建议：0 命中时按 `kb_search` 的做法回报「译文层 N 段 / 原文层 M 段命中」，或直接回退到 `layer="zh"` 给三条。
2. **`include_draft` 的效果无法从输出判断**（#5、#6）。#6 两次输出逐字相同，我无法区分「flag 没生效」和「确实没有 draft 命中」；直到 #8 才用一个已知存在于 draft 的词验证它是通的。建议：输出里固定打印「本次检索范围：已核 / 含未复核（N 张 draft 参与）」一行。
3. **卡片层多词查询的召回语义不清**（#3）：`Klein surface` 返回的几乎全是只共享 `surface` 的卡，像是 OR；而 #4 的 `real structure 实结构` 又像 AND（0 命中）。同一工具在不同查询下表现不一致，使用者无法预判。建议：统一为「AND 优先，不足时标注放宽」，并在输出里注明「以下为放宽后结果」。
4. **`around` 参数被忽略**（#10）。小事，但会让人误以为自己在读「只这一段」，实际读了五段。
5. **结果顺序不稳定**（#8）。同一查询开不开 draft，已核卡的顺序都会变；做引用记录时要连 id 一起记，不能只记「第 2 条」。

## 好用的地方

- `kb_stats` 一屏给出可信度分布 + 三层规模，开工前判断「这本书在本库有没有底子」很快。
- `kb_card` 的术语卡（`term` 类）就是现成的译名表，`Higgs bundle → Higgs 丛` 这种直接可用；本次「克莱因曲面」「万有覆盖」「增广」都先查了库再定。
- `kb_source` 的整页原文 + 前后文，是核对底本句子的最快路径，本次用它交叉确认了 Klein 分类的 $(n,a)$ 与本书 $(g,k,a)$ 的对应。
- `kb_search(layer="all")` 一次给三层，且每条标作品编号与可信度——判断「这条能不能引」只需看可信度那一行。

## 待补测 / 本次没测到的

- 本工程的卡片入库后：新卡是否默认可检索、`related` 跨库链接是否生效、多词查询是否仍 0 命中（见下一节复测）。
- `kb_brief` 在只有 draft 卡时的行为（本次没有合适的查询对象）。
- 页码口径：卡片同时存 `pages`（印刷页）与 `pdf_pages`（底本 PDF 页）时，工具显示哪一个？（本次入库后观察。）

## 本次使用结论（一句话）

**能用，但只能当「线索机」不能当「断言机」**：`kb_source` / `kb_card` 的输出可以直接用；`kb_search` 的召回要人工筛；`kb_brief` 的否定结论不可信，必须用 `kb_search(layer="all")` 复核一次。

## 入库后复测（2026-11-24 00:50；库 2,907 卡 / 52 部；本卷 10 卡已入库）

| # | 工具 | 查询 | 结果 |
| --- | --- | --- | --- |
| 11 | kb_search | `Real 黎曼面 实结构` | 前 5 条全是本卷卡（real-riemann-surface / analytic-double / real-curve-topological-type / real-fundamental-group / klein-surface-dianalytic），均标「已核（引文可核）」 | 
| 12 | kb_card | `sy0530.concept.real-fundamental-group` | 正文字段出齐；页码写 `p.86–88`（卡内 `pages=[86,87,88]`）；术语行 `术语：[]` |
| 13 | kb_card | `sy0530.concept.gamma-model`（卡里补了 `terms` 之后） | 术语行变成 `术语：[{"en":"Gamma model","zh":"Γ 模型"},{"en":"homotopy class of paths","zh":"道路同伦类"}]` |
| 14 | kb_brief | `work=sy0530` | 10 张卡全出（按可信度排序）+ 「跨书线索」给 SY02-23.chain「实丛与手征代数」、SY02-21.chain D4/D6 —— **这是本次最好用的一个新用法**：`kb_brief(work=…)` 等于「这本书的入场券」 |
| 15 | kb_brief | `query="实曲线基本群 实覆盖 增广"`（不给 work） | 仍只查卡片层，返回与本卷无关的 chain 卡；**#2 的老问题没变**：`query` 模式不可信，`work` 模式可信 |
| 16 | kb_card / kb_search | 任意本卷卡 | 之前固定的「⚠ 页码由卡内文本启发式抽取」告警**消失**（仓库脚本 `kb/ingest.py` 已修：判断 `sources` 列表而非 `source` 字典） |

### 新发现的问题（接上节编号）

6. **离散页码被渲染成连续区间**（#12）。插件 `lib/index.js:152` 是 `p.${pages[0]}–${pages[pages.length-1]}`，本卷 `pages=[68,70,71]` 显示成 `p.68–71`，读者会以为 69 也在。建议改成按连续段合并：`p.68, 70–71`。
7. **`terms` 数组原样 `JSON.stringify`**（#13）。应是给人看的一行「Gamma model / Γ 模型」，现在是一坨 JSON。建议 `terms.map(t => [t.en, t.zh].filter(Boolean).join(" / ")).join("；")`。
8. **卡片正文里的 LaTeX 原样显示**（#12、#13、#14 都能看到 `$\Sigma$`、`\emph{双解析}`、`\Id`）。插件没有「纯文本渲染」字段，也不剥 LaTeX。两条路：卡内 `summary` / `definition.text` 改用 unicode 数学（$\Sigma\to$ Σ、$\pi^R_1\to$ π^R₁），LaTeX 只放 `formulas`；或插件侧做最小剥除（去 `$`、`\emph{}`→`{}`、已知宏映射）。
9. （工具侧，已修）`kb/ingest.py` 的 caveat 判断用 `d.get("source")`，而结构化卡用的是 `sources`，导致 `datasets/*/cards/**` 的卡**全部**被误标「页码由卡内文本启发式抽取」。已在仓库脚本里改成先认 `sources` 列表（#16 验证）。
10. （流程侧，已修）`kb/export_plugin_data.py` 的 `--out` 指错一层会 `rmtree` 掉插件 `data/` 下的 `zh`、`src` 层（本次实际踩到，见交付报告 §6）。已加防呆：`--out` 必须以 `cards` 结尾。

> 备注：#11–#16 的复测都在「数据已进插件」之后做，说明本卷的卡从 `datasets/` 到插件 UI 的通路是通的；卡的质量问题（LaTeX、页码）不是通路问题。
