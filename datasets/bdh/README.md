# bdh · Beilinson–Drinfeld《Hitchin 可积系统的量子化与 Hecke 特征层》资料卡

本书是 A. Beilinson 与 V. Drinfeld 的长篇专著（386 页，无正式出版本）中译校订本的**单章资料卡**试点：
一段原文、一段译文、一条「为什么这么译」才算数据；这里进一步做成可校验的概念卡与勘误卡。

- 底本：A. Beilinson, V. Drinfeld, *Quantization of Hitchin's Integrable System and Hecke Eigensheaves*（pdfTeX 2020 重排版，386 页）。
- 译本：`08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/`（章文件 `chapters/chNN.tex`，翻译单元 `units/chNN_uMM.tex`）。
- 卡片一律**锚到中译源码的确切行号**（`anchor`），不锚 PDF 页码；`pages` 与 `pdf_pages` 相同（本书 PDF 页 = 印刷页）。
- 权利：`rewritten`（改写，不复制原文；英文短引 ≤120 字符）。
- 核验：全部 `source-only`——只对照原书页面图像与译文，不引外部文献背书。

## 目录

| 路径 | 内容 |
| --- | --- |
| `cards/concepts/*.json` | 概念卡：定义、记号、关键点、公式、常见错误 + 批注 |
| `cards/corrections/*.json` | 勘误卡：原书笔误判定、译本改译、术语统一 |
| `tools/make_cards.py` | 唯一生成入口：校验并写出 `index.jsonl`、`verification.jsonl`、`md/`、`MAP.md`、`taxonomy.md` |
| `md/` | 每卡一页 Markdown（生成物，勿手改） |
| `MAP.md` | 卡片地图（按位置/类型/锚点） |
| `taxonomy.md` | 按章分类 |

## 生成与校验

```bash
python tools/make_cards.py --check     # 只校验，0 = 通过
python tools/make_cards.py             # 校验 + 重写生成物
python tools/make_cards.py --strict    # WARN 也当失败
```

## 写作纪律

- 断言必须有锚点：`sources[].anchor` 指向 `源码/...:a-b`，行号必须真实存在。
- 不复制原文；英文短引不超过 120 字符。
- 不写本机路径。
- 诚实标注核验状态：`verification.status` 只用 `source-only`。
- 批注只写三类：**易错预警**、**含糊点拨**、**背景直觉**，每条 ≥40 汉字。
