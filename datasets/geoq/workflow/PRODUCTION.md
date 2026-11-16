# 几何量子化资料卡 · 生产工作流

这份文档记录 `datasets/geoq/` 是怎样从一本 PDF 书产出 48 张资料卡的。它既是施工记录，也是下次拆另一章时可以照抄的协议。

## 0. 总览

```text
源码定位 → 卡片总表 → Schema + lint → 示范卡 → 六路并行起草
        → 汇总修 lint → 人工抽检 → 渲染（index / md / map）
        → 入仓（README / CHANGELOG / MANIFEST）→ 推送
```

| 阶段 | 产物 | 质量门 |
|---|---|---|
| 0 勘察 | 章节结构、环境编号、页码映射 | 环境计数与源码对得上 |
| 1 总表 | `taxonomy.md` | 一卡一义；例子全部独立；每张卡有源码行段 |
| 2 规范 | `SCHEMA.md`、`tools/lint_geoq.py` | lint 能在空目录跑通 |
| 3 示范 | 1 张概念卡 + 1 张例子卡 | lint 0 error，人工通读一遍 |
| 4 起草 | 48 张 JSON | 每张卡 lint 通过；跨引用可解析 |
| 5 汇总 | 全量 lint、`index.jsonl` | 0 error；summary 长度、页码、证明步数全过 |
| 6 渲染 | `md/`、`map.svg`、`map.png` | 随机抽 5 张 md 与图对照无误 |
| 7 入仓 | 仓库 `datasets/geoq/` | 根 README、CHANGELOG、MANIFEST 同步 |

## 1. 勘察：先把书变成可定位的源码

1. 解压书稿包（本机无 `unzip`，用 Python `zipfile`）。
2. 找章节文件：本书第 5 章在 `chunks/ch05a.tex`（§5.1–§5.2）与 `chunks/ch05b.tex`（§5.3–§5.4）。
3. 用正则统计环境：`\begin{definition}`、`\begin{theorem}`、`\begin{proposition}`、`\begin{example}`、`\begin{remark}`，得到 20 / 2 / 16 / 20 / 1，共 59 个编号环境。
4. 抽出小节标题行号与 `% [原文 p.NNN]` 页码标记，建立「源码行号 ↔ 印刷页 ↔ PDF 页」三列对照表。
5. **先确认例子数**：20 个 `example` 环境正好是 20 张例子卡，不多不少；这一步决定后面派工规模。

> 经验：不要一上来就读整章。先做结构统计，再按卡片粒度精读；否则上下文会被 2700 行 TeX 吃掉。

## 2. 总表：一卡一义

`taxonomy.md` 是唯一的卡片清单，起草前必须定稿。规则：

- **一卡一义**：一个定义/定理/构造一张卡；不要把「预量子化 + 极化」塞进一张。
- **例子独立**：书中每个 `example` 环境一张卡，即使它只是某个命题的验证。
- **轨道**：A 辛几何 / B 半经典 / C 表示论 / D 量子化机器 / O 总览；轨道决定颜色、阅读顺序与地图位置。
- **每张卡三件事**：id、主源印刷页、源码行段。行段必须精确到能直接 `sed -n` 取出来。
- **跨引用先定 id**：`related` 和 `concept_refs` 只能指向总表里已有的 id；起草期间用 `lint --allow-missing` 放行，汇总时必须全部解析。

## 3. Schema 与 lint 先行

先写 `SCHEMA.md` 和 `tools/lint_geoq.py`，再写卡。Schema 的关键约束：

- 概念卡：`question` 必须是问句；`summary` ≤120 汉字；`key_points` 3–6 条；`formulas` 1–5 条；`theorems` 1–3 条；`pitfalls` 1–3 条；`related` ≥2。
- 例子卡：`setup → computation（≥2 步，每步 no/text/why）→ result → check`；`concept_refs` ≥1。
- 证明：`complete` 至少两步，每步 `text`（推导）与 `why`（为什么成立/为什么需要）都不能空；`sketch` 必须写 `gap_note`。
- 页码：`pages` 用印刷页，`pdf_pages = pages + 1`，两栏都写；`anchor` 形如 `ch05a.tex:1024-1111`。

lint 在起草期就要能跑，哪怕目录里只有两张卡。**规则前置，返工减半。**

## 4. 示范卡：把「好卡长什么样」固定下来

先由 lead 写两张：

1. 一张最核心的概念卡（本批是 `prequantization`，含 Q1–Q4 五步证明与存在性缺口）；
2. 一张计算型例子卡（本批是 `sp2-equals-sl2`，4 步计算 + Lie 代数维数复核）。

两张卡都跑 lint 0 error 后，连同 `SCHEMA.md`、`taxonomy.md` 一起发给所有起草 agent。示范卡的作用不是模板复制，而是让 agent 看到「证明的 why 写到什么程度、例子卡 check 长什么样」。

## 5. 六路并行起草

按轨道与工作量分簇，每簇 6–10 张卡：

| agent | 负责 | 卡数 |
|---|---|---|
| geo-a1 | A1–A5 概念 + 5 个线性辛几何例子 | 10 |
| geo-a2 | A6–A10 概念 + 4 个辛流形例子 | 9 |
| geo-b | B1–B5 概念 + 2 个半经典例子 | 7 |
| geo-c | C1–C5 概念 | 5 |
| geo-d1 | D1/D2/D4 概念 + 6 个极化例子 | 9 |
| geo-d2 | D5–D7 概念 + 2 个算子例子 | 5 |

每个 agent 的提示词必须包含：

1. 工作目录与**只准改自己负责的 JSON**；
2. `SCHEMA.md`、`taxonomy.md`、两张示范卡的路径；
3. 自己那几张卡的源码行段（不要给全书，也不要让它自己找）；
4. 三条硬约束：不复制原文、每步写 `why`、页码写印刷页且 `pdf_pages=pages+1`；
5. 完成前必须跑 `python tools/lint_geoq.py --allow-missing`，最后 5 行回报「写了哪些 / lint 结果 / 不确定的点」。

> 经验：给 agent 的源码行段要连带前后 30 行上下文；只给定义行，它会漏掉书里的约定与反例。

## 6. 汇总与修 lint

所有 agent 完成后：

1. 全量跑 `python tools/lint_geoq.py`（去掉 `--allow-missing`），按 error 逐条修；
2. 重点人工抽检四类：**证明的 why 是否真的解释、例子 check 是否可执行、页码是否偏移、pitfalls 是否是真正的坑**；
3. 检查同一概念在不同卡里的记号是否一致（$\hbar$、$2\pi$、$\Theta^{1/4}$、$E_n$）；
4. 用 `build_index.py` 生成 `index.jsonl`，确认 48 行、id 无重复。

## 7. 渲染

- `render_md.py`：JSON → `md/concepts/*.md`、`md/examples/*.md`、`md/index.md`；每张卡含「先自测」、定义、要点、公式、证明（每步 why）、易错点、相关卡、出处。
- `render_map.py`：手绘 SVG + PNG。本机没有 graphviz / mmdc，所以用 Pillow 按固定坐标画；SVG 与 PNG 共用一套布局常量，改图只改脚本。
- 地图的字体坑：微软雅黑缺 `ℏ ⊗ ∇ ⟺` 等符号，PNG 会出豆腐块；`render_map.py` 逐字符回退到 Cambria Math。SVG 交给浏览器回退，不需要处理。

## 8. 入仓与发布

1. 复制到仓库 `datasets/geoq/`；
2. 在 `datasets/README.md` 增加 geoq 条目（规模、目录、与 encyclopedia 的区别）；
3. 根 `README.md` 的 datasets 章节加一行入口；
4. `CHANGELOG.md` 增加版本条目；
5. 跑 `build_manifest.py` 更新 `MANIFEST.json`；
6. 提交并推送：`git push atomgit master:main`、`git push origin master:main`。

## 9. 复盘：这次踩过的坑

| 坑 | 现象 | 处理 |
|---|---|---|
| 页码双轨 | 卡片写 PDF 页，读者按印刷页找不到 | Schema 强制 `pages` + `pdf_pages`，lint 校验差 1 |
| 数学符号缺字 | 地图上 `ℏ ⊗ ∇` 变豆腐块 | PNG 逐字符回退 Cambria Math；SVG 靠浏览器 |
| JSON 转义 | LaTeX 反斜杠写成单杠导致解析失败 | 所有 `\` 写成 `\\`；lint 先 `json.loads` |
| 并行 id 冲突 | 两个 agent 各自发明 `geoq/concept/xxx` | 总表先定 id；agent 只准写自己那几行 |
| 证明只有结论 | `steps` 写成「由定理可得」 | Schema 要求每步 `why`；人工抽检专门看这个 |
| 例子卡没有复核 | `check` 写「显然成立」 | 要求可执行：代回、量纲、特例、数值 |
| 上下文爆炸 | 一次读整章 2700 行 | 按卡片行段精读；结构统计先行 |

## 10. 复用清单

下次拆另一本书/另一章，按这个顺序改：

1. `taxonomy.md` 的 id、标题、页码、行段；
2. `SCHEMA.md` 的 `sources.book` 与页码范围；
3. `tools/lint_geoq.py` 里的页码上下界与 anchor 文件名正则；
4. `render_map.py` 的 `NODES` / `PANELS` / `EDGES`；
5. 示范卡换成新章节的核心定义与最小例子；
6. 起草 agent 的提示词只换「轨道 + 行段」。
