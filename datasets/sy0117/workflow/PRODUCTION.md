# sy0117 生产流程

## 1. 输入

- 中译定稿：`08_source_code/SY01-17_同调镜像对称性浅入门/源码/chapters/ch01.tex`–`ch12.tex`
- 二轮报告：`工程文件/reports/ch01.md`–`ch12.md`、`工程文件/审校报告.md`
- 二轮改动台账：`work/review2/changes.md`（工作区，不随仓库发布）
- **没有**英文原书与页面图像。本机 `originals_pkg` 只有一张插图，不是原书。

## 2. 三道闸

1. **锚点闸**：每条 `sources[].anchor` 必须解析到源码文件，行号在文件内；`make_cards.py --check` 失败即不入库。
2. **批注闸**：每张概念卡至少 1 条批注，类型限 `易错预警` / `含糊点拨` / `背景直觉`；批注必须说明「错在哪/补什么/为什么重要」，不得写空泛的「注意」。
3. **诚实闸**：没有英文原文，不得写「原书作 X」；勘误卡 `why` 只引中译上下文与数学自洽；`verification.status` 一律 `source-only`，不得标 `published`。

## 3. 生产步骤

1. 从二轮报告与 `changes.md` 选代表条目：每章至少 1 张概念卡，勘误卡只收可独立成卡的硬错误。
2. 写卡：定义自足、公式用 LaTeX 源码、`related` 至少 2 条并交叉链接。
3. 回填锚点：用当前 `chNN.tex` 行号；不凭记忆。
4. 跑 `python tools/make_cards.py --check`，0 错后跑 `python tools/make_cards.py` 生成 JSON、Markdown、索引与地图。
5. 人工抽读 `md/` 三张卡，确认公式渲染与批注无空话。
6. 更新 `datasets/README.md` 计数与 `CHANGELOG.md`。

## 4. 复跑命令

```bash
cd datasets/sy0117/tools
python make_cards.py --check
python make_cards.py
```

## 5. 已知边界

- 12 张勘误卡只是 89 处改动中的代表，不是全量勘误表；全量见逐章报告。
- 概念卡是“读者入口”，不是教材替代；定义与定理的完整陈述仍以中译定稿为准。
- 若章节再改，锚点会漂移，必须重跑校验并更新 `anchor`。
