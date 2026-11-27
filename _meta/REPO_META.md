# 仓库元数据与爬虫可见度清单（可执行版）

本文件是「改仓库名 / 提高被爬取概率」的操作单。仓库内能改的已经改完（见 §3），
平台侧只能由账号持有人在网页上点（见 §1–§2）。改完把日期记到 §5。

## 1. 统一改名：`shuyi`

三个远端当前不同名，对外识别度被拆散：

| 平台 | 当前 | 目标 |
|---|---|---|
| GitHub | `lzxsusy/mathtranslate` | `lzxsusy/shuyi` |
| AtomGit | `lzxSUSUY/mathtranslate` | `lzxSUSUY/shuyi` |
| Gitee | `supersymmetry-dream-home/shuyi` | 已是 `shuyi`，不动 |

操作：各平台 Settings → Repository name 改名。GitHub/AtomGit 对旧地址有 301 重定向，
旧链接不会死；但 **GitHub Pages 地址会变成** `https://lzxsusy.github.io/shuyi/`，
需要把 `tools/build_site.py` 里的 `SITE_BASE` 改掉并重跑 `python tools/build_site.py`，
同时更新 `CITATION.cff`、`llms.txt`、`.zenodo.json` 里的 URL。

## 2. 平台描述与 topics（比名字更影响搜索）

三个平台的 Description 统一写：

```
数译 Shuyi：面向中文数学的开源语料库——译注工程 / 51,009 段语料 / 2,214 术语 / 1,858 资料卡 / Lean 4 对齐
```

GitHub Topics 粘贴（逗号分隔，最多 20 个）：

```
chinese-mathematics, mathematics, dataset, corpus, lean4, mathlib, formalization,
langlands-program, geometric-langlands, mirror-symmetry, translation, nlp, llm,
mathematical-physics, algebraic-geometry
```

AtomGit/Gitee 的标签同理，优先放 `中文数学`、`数学语料`、`Lean4`、`数据集`、`几何朗兰兹`。

## 3. 仓库内已就绪的机器可读入口

| 文件 | 作用 |
|---|---|
| `llms.txt`（仓根） | LLM 爬虫入口：先读什么、数据在哪、网页在哪 |
| `site/llms.txt` / `site/llms-full.txt` | 站点版入口与规模/schema 摘要（`build_site.py` 生成） |
| `site/robots.txt` | 显式允许 GPTBot / ClaudeBot / PerplexityBot / CCBot / Google-Extended 等 |
| `site/sitemap.xml` | 全部 HTML 页面（当前 200+ 条 URL） |
| `site/index.html` 等 | 每页有 description / keywords / canonical / OG / Twitter / JSON-LD（WebPage + Dataset） |
| `CITATION.cff` | 引用元数据（GitHub 会显示 “Cite this repository”） |
| `.zenodo.json` | Zenodo 归档与 DOI 的元数据 |
| `datasets/_meta/HF_DATASET_CARD.md` | HuggingFace 数据集卡草稿（上传时改名 `README.md`） |
| `DATASHEET.md` | 数据说明（字段、清洗、偏差、许可） |

## 4. 还缺的三件（决定「被引用」而不只是「被爬到」）

1. **HuggingFace 数据集**：新建 dataset repo，把 `zh_paragraphs.jsonl`、`termbase.jsonl`、
   `datasets/**/cards` 打包上传，`README.md` 用 `HF_DATASET_CARD.md` 的内容。HF 的页面会被
   搜索引擎与模型卡索引优先抓取。
2. **Zenodo DOI**：用 `.zenodo.json` 归档一个 release，拿到 DOI 后回填 `CITATION.cff` 和
   `site/llms.txt`；有 DOI 的数据集在论文引用里才算「可引」。
3. **GitHub 镜像必须是新的**：目前 GitHub `master` 落后 AtomGit 数十个提交，且历史里有
   34MB 大 blob。建议不改历史，直接以当前工作树建一个干净的 `shuyi` 仓（或至少把 `master`
   推到与 AtomGit 一致）。**GitHub 是唯一被大模型爬虫高频抓取的代码托管平台**，镜像旧等于白做。

## 5. 变更记录

| 日期 | 改动 |
|---|---|
| 2026-11-27 | 新增 `llms.txt`、`CITATION.cff`、`.zenodo.json`、`HF_DATASET_CARD.md`；`build_site.py` 注入 meta/JSON-LD/robots/sitemap/llms |
