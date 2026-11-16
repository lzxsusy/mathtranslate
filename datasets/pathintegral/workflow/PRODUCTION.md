# 路径积分资料卡 · 生产工作流

这份文档记录 `datasets/pathintegral/` 怎样从一本 PDF 书产出 50 张资料卡。它既是施工记录，也是下次拆另一章时可以照抄的协议。

## 0. 总览

```text
源码定位 → 卡片总表 → Schema + lint → 示范卡 → 七路并行起草
        → 汇总 lint → 页码/重合审计 → 两轮审校 → 渲染（index / md / map）
        → 入仓（README / CHANGELOG / MANIFEST）→ 推送
```

| 阶段 | 产物 | 质量门 |
|---|---|---|
| 0 勘察 | 章节结构、环境编号、页码映射 | 环境计数与源码对得上 |
| 1 总表 | `taxonomy.md` | 一卡一义；20 个例子全部独立；每张卡有源码行段 |
| 2 规范 | `SCHEMA.md`、`tools/lint_pi.py` | lint 能在空目录跑通 |
| 3 示范 | 1 张概念卡 + 1 张例子卡 + 1 张总览 | lint 0 error，人工通读一遍 |
| 4 起草 | 50 张 JSON | 每张卡 lint 通过；跨引用可解析 |
| 5 汇总 | 全量 lint、`index.jsonl` | 0 error；summary 长度、页码、证明步数全过 |
| 6 审计 | `audit_pages.py`、`check_overlap.py` | 页码 0 问题；无 ≥20 字连续重合 |
| 7 审校 | 两份只读审校报告 | 数学错误全部修完，存疑写入 pitfalls |
| 8 渲染 | `md/`、`map.svg`、`map.png` | 抽 5 张 md 与图对照无误 |
| 9 入仓 | 仓库 `datasets/pathintegral/` | 根 README、CHANGELOG、MANIFEST 同步 |

## 1. 勘察：先把书变成可定位的源码

1. 解压书稿包（本机无 `unzip`，用 Python `zipfile`）。
2. 找章节文件：第 2 章在 `chunks/ch02a.tex`（§2.1–§2.5）、`ch02b.tex`（§2.6–§2.7）、`ch02c.tex`（§2.8），共 4378 行。
3. 用正则统计环境：20 个 `example`、4 个 `definition`、3 个 `proposition`、1 个 `theorem`、7 个 `remark`。**先确认例子数**：20 个 example 正好 20 张例子卡，不多不少；这决定派工规模。
4. 抽出小节标题行号与 `% [原文 p.N]` 页码标记，建立「源码行号 ↔ 印刷页 ↔ PDF 页」三列对照表。印刷页 80–160，PDF 页 = 印刷页 + 1。
5. 只精读与卡片粒度对应的段落；不要把 4378 行 TeX 一次性读进上下文。

## 2. 总表：一卡一义

`taxonomy.md` 是唯一的卡片清单，起草前必须定稿。规则：

- **一卡一义**：一个定义/定理/方法/构造一张卡；不要把「半经典核 + 雅可比场」塞进一张。
- **例子独立**：书中每个 `example` 环境一张卡，即使它只是某个命题的验证。
- **轨道**：A 定义与时间切片 / B 高斯与谐振子 / C 渐近与半经典 / D 格林函数与 WKB / E 微扰与代数 / O 总览；轨道决定颜色、阅读顺序与地图位置。
- **每张卡三件事**：id、主源印刷页、源码行段。行段必须精确到能直接 `sed -n` 取出来。
- **跨引用先定 id**：`related` 和 `concept_refs` 只能指向总表里已有的 id；起草期用 `lint --allow-missing` 放行，汇总时必须全部解析。

## 3. Schema 与 lint 先行

先写 `SCHEMA.md` 和 `tools/lint_pi.py`，再写卡。关键约束：

- 概念卡：`question` 必须是问句；`summary` ≤120 汉字；`key_points` 3–6 条；`formulas` 1–5 条；`theorems` 1–3 条；`pitfalls` 1–3 条；`related` ≥2。
- 例子卡：`setup → computation（≥2 步，每步 no/text/why）→ result → check`；`concept_refs` ≥1。
- 证明：`complete` 至少两步，每步 `text`（推导）与 `why`（为什么成立/为什么需要）都不能空；`sketch` 必须写 `gap_note`。
- 页码：`pages` 用印刷页，`pdf_pages = pages + 1`，两栏都写；`anchor` 形如 `ch02b.tex:31-88`。
- 数学：只用 MathJax 标准宏（`\mathbb`、`\operatorname`、`\partial`、`\hbar`），不要用书内自定义宏。

lint 在起草期就要能跑，哪怕目录里只有两张卡。**规则前置，返工减半。**

## 4. 示范卡：把「好卡长什么样」固定下来

先由 lead 写三张：

1. 一张最核心的概念卡（本批是 `feynman-kernel`，定义 + 复合律 3 步证明 + 4 个坑）；
2. 一张计算型例子卡（本批是 `gamma-asymptotics`，拉普拉斯方法 5 步 + 数值复核）；
3. 一张总览卡（`overview-path-integral`，三层计算引擎 + 两个定理 + 5 个坑）。

示范卡必须同时展示：`question` 的写法、`why` 的写法、`check` 的可复核性、`sources` 的页码格式。之后所有 agent 照抄结构，不照抄内容。

## 5. 七路并行：按轨道与例子负载切

| agent | 负责 | 卡数 |
|---|---|---|
| pi-a | A 轨基础 5 张 | 5 |
| pi-b | B 轨高斯与谐振子 4 张 | 4 |
| pi-c1 | C 轨渐近方法 4 张 + 3 个例子 | 7 |
| pi-c2 | C 轨半经典 4 张 + 2 个例子 | 6 |
| pi-d | D 轨格林函数/WKB 5 张 + 4 个例子 | 9 |
| pi-e1 | E 轨威克/费曼图/外尔 3 张 + 4 个例子 | 7 |
| pi-e2 | E 轨 S¹/Hochschild/HKR 3 张 + 6 个例子 | 9 |

派工时必须写清：

- 先读 `SCHEMA.md`、`taxonomy.md`、三张示范卡；
- 只写分配的文件，不碰别人的卡、总表与工具；
- 每张卡写完跑 `lint_pi.py cards --allow-missing` 与 `check_overlap.py`；
- 最后 5 行回报：卡片列表、lint 结果、最长重合、书中疑点、未解决项。

## 6. 汇总与审计

1. 全量 `lint_pi.py cards` 必须 0 error；`--allow-missing` 只用于起草期。
2. `audit_pages.py --src ...`：按页首标记核对每张卡的 `pages` 是否等于 anchor 覆盖页。常见错因是 anchor 从标题行起算、而 `pages` 从正文首行起算。
3. `check_overlap.py --src ...`：扫描卡片散文与底本的最长连续汉字串，阈值 20。**超标集中在 `definition.text` 开头与术语括号注**；改写这些句子，不要改公式。
4. `build_index.py`、`render_md.py` 重建索引与 Markdown；检查卡片内链接用 `../concepts/`、`../examples/`。

## 7. 两轮审校

- **数学审校**：逐条核对定义的条件、证明的每一步、例子的符号/因子/$2\pi$/$i$；重点查 Maslov 相位、$+i\epsilon$、半经典行列式、S¹ 零模、HKR 的映射方向。
- **合规审校**：中文散文与底本连续重合 <20 字；公式可以照录，但定义句式不能照抄。
- 审校 agent 只读，输出「卡 id — 字段/步骤 — 错在哪 — 建议改法」；由 lead 统一应用，避免多人同时写同一文件。

## 8. 入仓

- 只复制成稿：`README.md`、`MAP.md`、`map.svg/png`、`SCHEMA.md`、`taxonomy.md`、`index.jsonl`、`cards/`、`md/`、`tools/`、`workflow/`。
- 不复制：底本 `src/`、生成脚本、备份 JSON、临时裁图。
- 更新 `datasets/README.md`、根 `README.md`、`CHANGELOG.md`；提交后跑 `build_manifest.py`，再提交一次 MANIFEST。
- 推送：AtomGit `git push atomgit master:main`，Gitee `git push origin master`。

## 9. 踩坑复盘

1. **例子数先数清**：20 个 example 是硬约束；漏一个，后面例子卡与概念卡的比例就乱了。
2. **页码语义先确认**：`% [原文 p.N]` 标在页首；anchor 覆盖页要从标记行起算，不要从环境首行猜。
3. **不要用书内宏**：`\R`、`\C`、`\pa`、`\hs` 在 MathJax 下全是未定义；统一成标准宏后再渲染。
4. **目录单复数**：agent 容易写 `cards/concept/`；派工时明确 `cards/concepts/`，汇总时先 `find` 一遍。
5. **半经典符号**：$K_{sc}$ 的 Maslov 因子是 $e^{-i\pi\nu/2}$；$\nu$ 每穿一次焦散加 1，别把方向弄反。
6. **格林函数边界**：$+i\epsilon$ 决定出射波；漏掉会得到驻波而不是散射态。
7. **S¹ 零模**：周期传播子要除掉零模行列式，否则配分函数发散。
8. **HKR 只陈述**：定理 2.8.16 书中没有完整证明；卡里必须标 `sketch` 并写 `gap_note`，不能伪装成 complete。
9. **重合扫描要跑两遍**：改写后再跑一次；只改一两个字往往仍超 20 字。

## 10. 复用清单

- 复制 `_cards_pi/tools/` 到新章节目录，改 `lint` 里的页码范围、`audit_pages.py` 的文件名正则、`render_map.py` 的节点布局。
- 复制 `workflow/prompts/drafter.md` 与 `reviewer.md`，把轨道与页码换掉。
- 保留 `taxonomy.md` 的「id / 标题 / 印刷页 / 源码行 / 写作抓手 / agent」六列，这是派工与验收的共同语言。
