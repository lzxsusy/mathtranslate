# lbook04 ·《朗兰兹纲领导论》概念资料卡

Bernstein–Gelbart 编 *An Introduction to the Langlands Program*（Birkhäuser 2004）中译注本（工程 `SY02-24`）的概念卡片，覆盖第 1–11 章；第 12 章（Gaitsgory《几何朗兰兹的非正式导论》）的深度卡片见 [`../gaits04/`](../gaits04/README.md)（23 张，含层化与几何 Langlands 猜想）。

## 规模

| 轨 | 主题 | 章 |
|---|---|---|
| O | 总览 | 全书 |
| L | L 函数 | 1、2、4、5 |
| M | 模形式与自守表示 | 3、7 |
| T | Tate 与迹公式 | 6、8 |
| G | GL_n 的 Langlands 纲领 | 9、10、11 |

每条卡都带 `annotations`（批注：易错预警 / 含糊点拨 / 背景直觉）、`sources`（原书印刷页 + 中译本源文件行号锚点）与 `verification`（当前均为 `source-only`）。

## 用法

```bash
cd tools
python build.py --check    # 只校验
python build.py            # 生成 cards/concepts/*.json、index.jsonl、verification.jsonl、md/、taxonomy.md、MAP.md
```

## 权利

卡片为改写（`rights: rewritten`），不含原文长段引文；单条摘要不超过 120 汉字。底本为在版图书，原文不入库。

## 出处

- 底本：J. Bernstein, S. Gelbart (eds.), *An Introduction to the Langlands Program*, Birkhäuser, 2004。
- 中译注本：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/`（234 页，154 条译注）。
