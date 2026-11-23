# 知识库插件（dsh-kb）试用笔记 · SY02-32

试用时间：2026-11-24。目的：按任务要求，在译校与立卡过程中试用 `kb_search` / `kb_card` / `kb_stats` 等工具，并验证本工程 31 张卡能否被插件检索。

## 一、可用的操作

| 工具 | 用途 | 本工程实测 |
| --- | --- | --- |
| `kb_stats` | 全库卡片/语料规模 | 起始 2,907 卡 / 52 部；入库后（仓库侧 `kb/q.py stats`）2,938 卡 |
| `kb_search` | 卡片/译文/原文三层检索 | 加 `work="sy32"` + `include_draft=true` 可精确命中本工程 31 张卡 |
| `kb_card` | 按 id 读全文 | `sy32.concept.base-steinberg-hitchin` 正常返回 |
| `kb_brief` | 立卡前查同类线索 | 用于查「基/底」「Tamagawa 测度」等术语的历史卡 |

## 二、实测发现（按影响排序）

1. **默认只返回已核卡片**。本工程 31 张全为 `status=draft`，所以默认查询（不带 `include_draft`）一张也搜不到，提示语「没有命中已核卡片」容易被误读成「库里没有」。查新工程必须先加 `include_draft: true`。
2. **检索是多词 AND，且中文长查询几乎必然空手**。实测「Steinberg–Hitchin 基 稳定共轭类」无命中，而单用「迹公式」+`work=sy32` 命中 4 张。建议查询只给 1–2 个核心词，或直接用 `work` 限定工程。
3. **插件读的是包内数据副本，不是仓库 `kb/`**：`~/.dsh/profiles/desktop/node_modules/dsh-kb/data/cards/*.jsonl`。仓库 `kb/ingest.py json` 只写 `kb/cards/`，要让插件看到新卡，还需把 `kb/cards/sy32.jsonl` 拷进上述目录（缓存按文件数+mtime 失效，拷完即生效，无需重启）。
4. **卡片顶层 `pages` 由 ingest 从所有 `sources[].pages` 合并**。本工程 4 张卡残留 B 类来源（本库 lbook04 的 p.188–191，属该底本页码，不属本文），导致插件里显示成「p.1–191」。已删除这 4 条 B 类来源、把本库出处移到 `provenance_note`；重新 ingest 后显示「p.1–31」。
5. 卡片的「未复核 / 未核」标签来自 `status=draft`，与内容质量无关；`verification` 字段才是复核进度。

## 三、结论

- 作为**译中检索**工具可用：查术语先例、查同主题卡、查译文段落都成立，但必须知道「默认只查已核」和「多词 AND」两条脾气。
- 作为**发布通道**要额外一步同步（仓库 `kb/cards/` → 插件 `data/cards/`），否则网页/插件端看不到新卡。
- 建议上游改进：`kb_search` 在结果为空时区分「库中无此卡」与「有 draft 卡但被过滤」，并在多词查询无命中时自动降级为 OR 或提示放宽。
