# 路径积分资料卡

李思《量子力学与几何》第 2 章「路径积分形式」的**可检索、可自测、可打印**资料卡。  
一张卡只回答一个问题：概念卡回答“这是什么、为什么成立、哪里会错”，例子卡回答“这道例题具体怎么算”。

- 底本：李思《量子力学与几何》（中文译注本）第 2 章，原书印刷页 80–160。
- 规模：**50 张**——1 张总览、29 张概念卡、20 张例子卡。
- 权利：全部 `rights: "rewritten"`。文字是改写，公式照录，出处逐条标印刷页；不收录底本原文段落。
- 先看地图：[MAP.md](MAP.md) / [map.png](map.png)。

## 30 秒入口

| 想做什么 | 打开 |
|---|---|
| 看整章脉络 | [map.png](map.png)（或 [map.svg](map.svg)） |
| 按轨道浏览 | [md/index.md](md/index.md) |
| 按 id / 页码检索 | [index.jsonl](index.jsonl) |
| 看某张卡 | `md/concepts/<slug>.md`、`md/examples/<slug>.md` |
| 自己出题 | 每张卡的 `question` 字段 |

## 资料卡怎么用

### 概念卡：七步

1. **先自测**：遮住正文，只读卡片正面的 `question`，用 30 秒口述答案。
2. **读定义**：`definition.text` 是改写后的精确表述，`definition.notation` 固定记号；先确认每个符号指什么。
3. **过要点**：`key_points` 是 5 条左右的“必须记住的句子”，不是证明。
4. **推公式**：`formulas` 里的式子自己推一遍，尤其是符号、$2\pi$、$\hbar$、$i$ 的位置。
5. **读证明**：`theorems[].proof.steps` 每步都有 `why`；`sketch` 的卡在 `gap_note` 说明书中省了什么。
6. **看坑**：`pitfalls` 是改卷时真正会错的地方，优先于背结论。
7. **跳相关卡**：`related` 指向同一条轨道的前后卡；例子卡在 `concept_refs` 里反向指回。

### 例子卡：四步

1. 读 `setup`，自己先列已知量与目标量。
2. 遮住 `computation`，独立算一遍；再逐步对照，重点是每步的 `why`。
3. 用 `check` 复核（代回、特例、量纲、数值），不要只看结果。
4. 回到 `concept_refs` 指向的概念卡，把这道题挂回框架。

### 三种典型用法

- **系统学**：`A 定义 → B 精确模型 → C 渐近机器 → D 格林函数/WKB → E 微扰与代数`，每张概念卡配一张例子卡。
- **查公式**：从 `index.jsonl` 按 `pages` 或 `track` 过滤，直接跳到 `formulas`。
- **复习/刷题**：只读 `question` 与例子卡 `setup`，把答案写出来再对照。

### Anki / 打印

- 概念卡正面用 `question`，背面用 `summary + key_points`；证明卡另做一张“这一步为什么成立”。
- 例子卡正面用 `setup`，背面用 `result + check`。
- `md/` 下的 Markdown 可直接打印；每张卡末尾有出处页，方便回书核对。

## 目录结构

```
README.md              本文件
MAP.md / map.svg/png   框架地图
SCHEMA.md              卡片字段与写作规则
taxonomy.md            50 张卡总表（按轨道）
index.jsonl            机器可读索引
cards/concepts/*.json  29 张概念卡 + 1 张总览
cards/examples/*.json  20 张例子卡
md/concepts/*.md       渲染后的概念卡
md/examples/*.md       渲染后的例子卡
md/index.md            人读索引
tools/                 校验、索引、渲染、地图、页码审计
workflow/              生产协议与可复用提示词
```

## 页码约定

- `sources.pages` 用**原书印刷页**（80–160）。
- `sources.pdf_pages = pages + 1`（PDF 81–161），因为 PDF 封面多一页。
- `anchor` 形如 `ch02a.tex:13-85`，指底本源码行；底本 TeX 不随本目录发布。

## 质量检查

在本目录运行：

```bash
python tools/lint_pi.py cards
python tools/audit_pages.py --src /path/to/SY07-03/chunks
python tools/check_overlap.py --src /path/to/SY07-03/chunks
python tools/build_index.py
python tools/render_md.py
```

- `lint_pi.py`：字段、id、页码、证明/例子步数、交叉引用。
- `audit_pages.py`：按 `% [原文 p.N]` 页首标记核对 `pages` 是否覆盖 anchor 实际范围。
- `check_overlap.py`：扫描卡片散文与底本的最长连续汉字串，阈值 20 字。
- 没有底本源码时，后两个脚本会提示跳过；`lint_pi.py` 仍可独立运行。

## 版权边界

- 本目录只发布**改写卡**：定义、要点、证明、例题均为重新表述；公式与标准术语照录。
- 单处引文不超过 60 字，累计不超过底本的 10%；不复制原书图表。
- 每张卡都标了印刷页，引用时请连同页码一起引，便于读者回书核对。
