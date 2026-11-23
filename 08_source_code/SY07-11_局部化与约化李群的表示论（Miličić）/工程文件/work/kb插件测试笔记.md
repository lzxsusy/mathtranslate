# kb 插件测试笔记（SY07-11 施工期间）

测试对象：本机 DSH 的 kb 插件（`C:\Users\admin\.dsh\profiles\desktop\node_modules\dsh-kb\data`，只读接口 `kb_stats / kb_search / kb_brief / kb_card / kb_source / kb_zh`）。
目的：验证它能否在「翻译一本新书」的过程中当检索工具用；记录失效场景。

## 测试记录

| # | 调用 | 输入 | 结果 | 判定 |
| --- | --- | --- | --- | --- |
| 1 | kb_stats | — | 2,782 卡 / 46 部；draft 1,876、checked 802、verified 104；带页码 1,213；原文层 7,644 段 / 33 工程；译文层 47,802 段 / 82 工程 | ✅ 可用 |
| 2 | kb_search | `局部化 D-模 表示论 localization`（4 词） | 0 命中 | ❌ **多词查询是严格 AND，且无回退**：只要有一词不在同一张卡里就整条 0 结果，用户以为库是空的 |
| 3 | kb_search | `localization`（单词） | 1 命中（dmod 支集局部化） | ✅ |
| 4 | kb_search | `Verma` / `Harish-Chandra` / `旗簇` | 分别命中 bdh / SY02-21 / SY02-22 等 | ✅ 单词可靠 |
| 5 | kb_brief | `Verma 模`（2 词） | 4 条命中 | ✅ 词在卡内相邻出现时可行 |
| 6 | kb_brief | `局部化 旗簇 微分算子 表示论 localization D-module flag variety`（8 词） | 「库里没有已核卡片覆盖这个主题」 | ❌ 同 #2：长查询几乎必然空手，提示语把人引向「没有资料」而不是「查询过严」 |

## 确认的问题

1. **多词查询无回退**（#2、#6）。建议：分词后按命中词数排序、给部分命中，或至少在 0 结果时提示「是否放宽为单词检索」。当前行为对使用者是误导性的。
2. **页码启发式**（工具自己在每条结果里挂 `⚠ 页码由卡内文本启发式抽取，引用前请回源核对`）。所有卡片页码只能当线索；本项目资料卡因此同时存 `pages`（印刷页）与 `pdf_pages`，并在 `sources.anchor` 里存原文首句，便于回源。
3. **覆盖缺口**：`dmod`（Miličić 前作，61 卡）里没有「旗簇 / 局部化函子 / 交织函子」这类本可直接复用的卡；用 `kb_brief` 为本书做前置检索时，命中的全是 bdh / gw06 / SY02-21 的间接相关卡。建议本书资料卡建好后补进 `dmod` 的 `related`，形成跨书链。
4. **未复核卡默认不出现**（`status=draft` 的 1,876 张默认不检索）：合理，但 `kb_stats` 未在同一屏说明「默认只查已核」，容易被误读为「库里只有 906 张」。

## 好用的地方

- `kb_search` 一次能同时返回**卡片层 / 译文层 / 原文层**，且标注作品编号与可信度——查「某术语在本库既有译法」很快（本项目的 `translation`、`holonomic`、`direct image` 等译法都是先查库再定的）。
- `kb_source`（原文整页上下文）适合核对底本句子，比翻 PDF 快。
- `kb_zh` 能看既有中译段落，判断术语惯例。

## 待补测

- 入库本项目的译稿与资料卡后，验证：新卡片是否默认可检索、`related` 跨库链接是否生效、多词查询是否仍 0 命中。

## 入库后复测（2026-11-23 22:35，本项目 43 张卡 + 793 段语料入库后）

| # | 工具 | 查询 | 结果 |
|---|---|---|---|
| 7 | kb_search(layer="zh", work="SY07-11") | `localization` | ✅ 命中本书译文第 3 段（局部化函子定义） |
| 8 | kb_search(work="mloc", include_draft=true) | `localization functor` | ✅ 3 条 mloc 卡（`localization-functor-delta`、`duality-and-standard-modules`、`geometric-translation-functor`）——**两词在本项目卡片里能命中** |
| 9 | kb_stats | — | 卡 2,782 → **2,896**；译文层 47,802 段 → 重打包后 48,596 段；原文层不变（L4 禁入，不加本书原文） |

新发现的问题：

5. **「source-only」被读成「已核」**（#8）：本项目 43 张卡在 JSON 里是 `status: draft` + `verification.status: source-only`，插件显示为「**已核（引文可核）**」。`kb/ingest.py:172` 的 `VERIF_CHECKED = {"source-verified","source-only"}` 是这么设计的——它表示「与底本对齐过」，不是「外部独立核验过」。但这层意思界面上看不出来，容易被当成 external-confirmed 用。建议结果行改成「引文已对齐（未外部核验）」。
6. **`include_draft` 的提示数与实际不符**（#8）：同一批查询的尾注写「另有 10 张未复核卡，加 include_draft:true 可看」，而该作品 43 张卡全部是 checked；10 这个数像是全库或缓存口径。
7. **译文层更新要手工同步两份数据**：`tools/pack_zh_corpus.py` 只写仓库里的 `plugins/dsh-kb/data/zh/`，而插件实际读 `C:\Users\admin\.dsh\profiles\desktop\node_modules\dsh-kb\data\zh\`，两份互不同步（本次是手工 `cp` 过去的）。卡片层同理（`kb/export_plugin_data.py --out <安装目录>` 要显式指过去）。建议插件加载时对仓库路径做 fallback，或在 README 里把「拷到安装目录」写成入库的最后一步。

## 第二次复测（2026-11-23 22:45，44 张卡、页码全部改为底本印刷页之后）

| # | 工具 | 查询 | 结果 |
|---|---|---|---|
| 10 | kb_search(layer="cards", work="mloc") | `localization equivalence` | ✅ 4 条 mloc 卡（`hc-modules-and-hc-sheaves`、`localization-equivalence`、`localization-and-n-homology`、`localization-functor-delta`），页码显示为底本印刷页 `p.87–90` / `p.36–43` 等 |
| 11 | kb_search(work="mloc", include_draft=true) | `Kazhdan-Lusztig` | ✅ 命中新建的 `kazhdan-lusztig-algorithm` 卡 |

新发现的问题：

8. **结果与尾注自相矛盾**（#10）：查询 `localization equivalence` 明明返回 4 张专门讲局部化等价的卡，尾注却写「已核卡片里只有边角提及，还没有专门讲这个主题的卡」。尾注像是按某个内部阈值判的，与返回列表不一致；用户只看尾注会被劝退。
9. **「另有 N 张未复核卡」的 N 与作品无关**（#10 仍然出现「另有 4 张未复核卡」）：该作品 44 张卡全部是 `checked`，这个数更像是全库未复核卡计数或缓存残值；问题 6 未修。
10. **页码口径正确，但插件不校验**（#10）：`p.36–43` 这类是卡里的底本印刷页；插件只做启发式抽取、不校验 `pdf_pages = pages + 4`，所以「页码印错」与「页码正确」在结果里长得一样。建议插件在卡片层展示时带上 `pdf_pages`，或直接读取卡片的 `sources` 而不是从正文抽页码。
