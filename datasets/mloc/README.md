# mloc · 局部化与约化李群的表示论（资料卡）

底本：Dragan Miličić, *Localization and Representation Theory of Reductive Lie Groups*（作者自排讲义，129 印刷页，6 章 28 节）。
卡片依据本仓中译本：`08_source_code/SY07-11_局部化与约化李群的表示论（Miličić）/`。

## 这是什么

一本书的「可检索知识点」：一张卡 = 一个能独立回答的问题（定义、定理、构造、可复算的例子）。
与 [`../dmod/`](../dmod/) 的关系：dmod 是作者前作《D-模的代数理论讲义》的卡（61 张），本书是它的续篇——
前作造语言，本书把语言用到旗簇与表示论。**通用 D-模概念只在 dmod 立卡**，本库只收本书特有的构造。

## 目录

```
mloc/
├── SCHEMA.md        卡片字段规范（必读）
├── taxonomy.md      轨道划分与粒度
├── cards/
│   ├── concepts/    概念卡 *.json
│   └── examples/    例子卡 *.json
├── verification.jsonl  核验记录（一行一卡）
├── index.jsonl         索引（build_index.py 生成）
├── md/                 卡片 Markdown 渲染（render_md.py 生成）
└── tools/
    ├── lint.py       结构与页码检查（0 error 才入库）
    ├── build_index.py
    ├── render_md.py
    └── build_verification.py
```

## 用法

```bash
cd datasets/mloc
python tools/lint.py                       # 0 error 才允许提交
python tools/build_index.py                # 重建 index.jsonl
python tools/render_md.py                  # 渲染 md/
python tools/build_verification.py         # 汇总 verification.jsonl
```

## 页码

本书底本 PDF 有 133 页，前 4 页是封面/空白/目录，**印刷页 = PDF 页 − 4**。
`SCHEMA.md` 要求每张卡的 `sources` 同时给 `pages`（印刷页）与 `pdf_pages`（PDF 页），`lint.py` 校验两者恒差 4。

## 核验

`verification.status` 三态：`external-confirmed`（nLab / Stacks Project / ProofWiki 等 B 级以上公开页面明确支持，逐条记录「哪句支持哪条断言」）、`source-only`（只有讲义依据）、`rejected`（与权威陈述冲突，禁止入库）。
来源黑名单：知乎、百度系、CSDN、简书、公众号、B 站、个人博客、AI 摘要。

## 与译本的对应

卡片的 `sources.anchor` 指向译本的 `.tex` 行号，形如
`源码/chapters/ch02a.tex:88-96（引理 1.2）`，便于从卡回到译文、再回到底本印刷页。
