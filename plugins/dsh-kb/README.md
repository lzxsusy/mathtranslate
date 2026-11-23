# dsh-kb — 数译知识库插件

把一座「带页码、带来源、带可信度」的数学文献资料卡库，接成 DSH 里 **任何 agent 都能直接调用**的检索工具。

它不是一个通用 RAG：检索单位是**一张结构化的卡**（谁、在什么书、第几页、什么等级的来源、
核对到哪一步），而不是切碎的文本块。所以每条结果都能回源核对，而不是给出一个无法追责的答案。

**装好即用，自带三层数据**：

- **资料卡层** `data/cards/*.jsonl`：**2,782 张卡 / 46 部作品**（几何朗兰兹、镜像对称、D-模、辛几何、GGL 研讨班等）；
- **译文层** `data/zh/zh_paragraphs.jsonl.gz`：**47,802 段中文译文 / 82 个工程 / 389.8 万汉字**，覆盖最全——
  卡片还没做到的地方，这里多半有；
- **原文层** `data/src/src_paragraphs.jsonl.gz`：**7,644 段底本原文抽文 / 33 个工程 / 5.2M 字符**（英/日为主），
  想直接读作者原话、核对译法时用它。

纯 JS 检索：不依赖 Python、不依赖 SQLite、零配置。

## 安装

```powershell
# 一条命令（从数译仓库直接装）
dsh plugin --profile desktop add https://atomgit.com/api/v5/repos/lzxSUSUY/mathtranslate/raw/plugins/dsh-kb-0.3.2.tgz
```

或在 DSH 会话里：

```
plugin_manager({ action: "install_bundle",
                 target: "https://atomgit.com/api/v5/repos/lzxSUSUY/mathtranslate/raw/plugins/dsh-kb-0.3.2.tgz" })
```

本地 tarball：`install_bundle({ target: "file:C:/…/dsh-kb-0.3.2.tgz" })`。
装完重启 DSH 桌面端，工具出现在会话里。

## 五个工具

| 工具 | 用途 | 典型问法 |
|---|---|---|
| `kb_search` | 检索，`layer` 选层：`cards`（默认）/ `zh` / `source` / `both` / `all` | 「Hecke 特征层 的定义在哪本书第几页？」「原文里怎么写的？」 |
| `kb_source` | 读底本原文整页（默认前后各 2 段） | 「把 SY02-15 p.30 原文调出来」 |
| `kb_zh` | 读中文译文某段及前后文（默认前后各 2 段） | 「SY01-07 第 47 段前后怎么译的？」 |
| `kb_card` | 读单卡全文（依赖/来源/证据引文） | 「展开 glc.concept.hecke-eigensheaf-oper」 |
| `kb_brief` | 阅读前置包：动笔前的“已知内容地图” | 「我要译顶点代数，先给我相关卡」 |
| `kb_stats` | 库现状 + 三层覆盖度 | 「哪些书的卡最全、哪些还是 draft、哪些有译文/原文？」 |

检索是中文 bigram + 拉丁词表：`顶点`（两个字）能查，`Gromov-Witten` 写连字符也能命中 `Gromov – Witten`。

**读者自选读哪一层**——这是三层并存的理由：卡片是「我们读出来的结论」（省事，但 1,250 张卡不可能覆盖
全部译文），译文是「我们自己译的中文」（覆盖 82 个工程，最全），原文是「作者自己说的话」（33 个工程）。
同一句话可以只查卡片：

```
kb_search({ query: "Hecke eigensheaf", layer: "cards" })
```

也可以几层一起看，卡片先给结论、译文给中文说法、原文给证据：

```
kb_search({ query: "affine Grassmannian", layer: "all" })    # 三层都查
kb_search({ query: "几何内窥", layer: "zh" })                 # 只在中文译文里找
kb_zh({ pkg: "SY01-07", para: 47 })                          # 读某段译文的前后文
kb_source({ pkg: "SY02-15", page: 30 })        # 把那一页原文整页读出来
kb_source({ pkg: "SY01-13", query: "ミラー対称性" })  # 只给工程+关键词，自动选最相关页
```

原文层按 `pkg`（工程编号）+ `page`（底本 PDF 页）组织，段落里的页标记已在建库时剥掉，页码单独存字段。
译文层按 `pkg` + `para`（段号）+ `page_orig`（有锚点的工程才有原书页）组织，重复段落已按文本去重。

## 行为契约（写在工具描述里，模型可见）

1. 结果必带 `status`（verified/checked/disputed/draft）、`pages`、`sources`、`caveat`。
2. 默认不返回 `draft`（未复核）；显式 `include_draft` 才返回，且标注“未复核”。
3. 命中只代表「某部作品可能讲过」，**不构成结论**；引用前用页码回原文核对。
4. 书级条目（`kind=work`）只是指针，排序上被压到后面。

## 配置（可选）

```yaml
- id: dsh-kb
  name: dsh-kb
  config:
    repo: ""              # 留空=用包内数据；填仓库根=用外部更新的 kb/cards
    pageRoots:            # 可选：work → 页图目录，用于回源
      glc: "C:\\…\\pages"
```

## 数据与许可

- 卡片数据 `data/cards/*.jsonl`、原文层 `data/src/*`：CC BY 4.0 —— 欢迎研究、教学、检索、**模型预训练/微调/蒸馏**。
- 插件代码：CC BY 4.0。
- 卡片内引文来自各作品原文，仅作学术引用与核对线索；上游译文另按 CC BY-NC-SA 4.0 发布。

## 数据从哪来

上游仓库 `mathtranslate` 的 `kb/` 目录：`ingest.py`（三种卡源 → 统一 schema）→ `build_kb.py`
（JSONL + 索引）→ 卡数据同时打进插件包。

原文层来自 `tools/build_src_corpus.py`：扫仓库里**已公开**的原文文本
（`08_source_code/*/工程文件/work/full.txt`、`work/split/pNNN.txt`、`05_seminar_witten/**/source/text/pNNN.txt`），
按页标记切页、按空行切段、去页眉页脚与页码行，输出 `01_corpus_src/src_paragraphs.jsonl`，
并同时写一份 gz 进 `plugins/dsh-kb/data/src/`。上游更新后重跑脚本 → 重新打包即可发新版本。

## 与市场的关系

已准备好上架条目（`MARKET-SUBMIT.md`）。插件市场（dshmarket）的收录清单由
[awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) 维护，
条目需要 GitHub 仓库 + 图床图片；当前只能在 AtomGit 分发——不影响使用，一条命令就能装。
