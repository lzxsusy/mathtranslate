# 网站 MVP：研读档案站

**目标**：用 3–5 天做出一个能公开展示的单篇研讨班页面，验证“研读档案”作为网站产品的可行性。
**范围**：只做 **SEM-JP11** 一篇；不做用户系统、不做全文阅读、不做付费墙。
**前提**：计划书第 10 章的版权三层模型（L0 公开 / L1 私有 / L2 本地）。

---

## 1. 为什么先做单篇，不先搭平台

- 平台是抽象，单篇是证据。没有一篇完整内容，做出来的只是空壳；
- 版权边界只有在真实内容上才能验证；
- 单篇能暴露数据模型的问题（章节、锚点、claims、图），比先写 20 个页面更省时间；
- 3–5 天能上线，能给你一个“可给别人看的东西”，再决定是否扩张。

---

## 2. 技术选型

| 层 | 选择 | 理由 |
|---|---|---|
| 框架 | Astro + Content Collections | 静态优先、Markdown/YAML 友好、构建快 |
| 样式 | Tailwind CSS | 快速做干净学术排版 |
| 数学 | KaTeX | 静态渲染、速度快 |
| 搜索 | Pagefind（第二版） | 纯静态、无需后端 |
| 图 | 静态 SVG（第一版）；Cytoscape（第二版） | 论证图先静态，够用 |
| 内容 | Git + Markdown/YAML/JSON | 可审阅、可 diff、可回滚 |
| 部署 | Cloudflare Pages | 免费、CDN、预览部署 |

---

## 3. 内容契约（L0）

每个研讨班导出为一个 JSON + 若干 Markdown：

```json
{
  "id": "SEM-JP11",
  "title_zh": "镜像对称与 K3 曲面",
  "title_original": "ミラー対称性と K3 曲面",
  "authors": ["植田一石"],
  "year": 2014,
  "venue": "数理解析研究所講究録 第1918巻",
  "topic": "01_镜像对称与同调镜像对称",
  "language": "ja",
  "stats": {"source_pages": 25, "translation_pages": 22, "equations": 99, "figures": 9, "claims": 0, "questions": 0},
  "license_layer": "L0",
  "one_pager": "one_pager.md",
  "map": [
    {"id": "1", "title": "镜像对称", "pages": "1", "core_question": "四种镜像对称各自主张什么？"},
    {"id": "2", "title": "K3 曲面上的镜像对称", "pages": "2", "core_question": "..."}
  ],
  "claims": [],
  "questions": [],
  "errata": [],
  "graph": null,
  "updated_at": "2026-11-09"
}
```

**L0 允许**：
- 元数据、作者、出处、页数；
- 自写摘要/一页纸；
- 章节地图与核心问题；
- 论证图（自绘）；
- 问题集（自写）；
- 术语表（自建）；
- 短引用（每段 ≤200 字，每节 ≤3 段，注明页码）。

**L0 禁止**：
- 整节/整页译文；
- 原文 PDF 下载；
- 页图；
- 超过阈值的连续引用；
- 未授权的封面/图表。

---

## 4. 页面规格

### 4.1 首页 `/`

- 一句话项目定位；
- 3 个统计：1 篇研讨班 / 25 页原文 / 99 条编号公式；
- JP11 卡片：标题、作者、主题、状态、进入；
- “方法”入口：三步说明（读原文→建账本→质询综合）；
- 页脚：版权说明、联系、下架。

### 4.2 研讨班详情 `/seminars/SEM-JP11`

- 头部：标题（中/原）、作者/年/出处、标签（主题/语言/难度）、状态；
- 一页纸：一句话、三件事、怎么做的、一个例子、三个疑点、与谁相关、可信度；
- 章节地图：8 节 + 4 小节，点击展开核心问题与页码范围；
- 论证图：静态 SVG，节点可 hover 显示锚点；
- 3 条 claims（示例）+ 3 条 questions（示例）+ 2 条 errata；
- 下载/引用：BibTeX、纯文本一页纸；
- 版权提示：本页仅含自写研读内容，不含译文全文。

### 4.3 章节笔记 `/seminars/SEM-JP11/notes/1`

- 第一节的样例研读笔记（五段式）；
- 每条断言旁标注锚点；
- 底部“问题”列表；
- 上一篇/下一篇。

### 4.4 方法 `/method`

- 为什么不是“分章写笔记”；
- S0–S8 流程图；
- G0–G7 质量闸门；
- 角色说明；
- 评分表摘要。

### 4.5 关于 `/about`

- 项目目的；
- 版权与许可；
- 下架联系方式；
- 致谢（原文作者/出版社/arXiv）。

---

## 5. 数据流

```
seminars/SEM-JP11/
  seminar.yaml ─┐
  map.yaml     ├─→ tools/export_site.py ─→ site/src/content/seminars/SEM-JP11.json
  one_pager.md │                          └→ site/src/content/notes/SEM-JP11/1.md
  claims.jsonl │
  questions.jsonl
  argument_graph.json
        │
        └─→ copyright_scan.py（L0 阈值检查）──→ PASS 才构建
```

构建命令（示意）：

```bash
cd 04_网站MVP/site
pnpm install
pnpm run export
pnpm run build
pnpm run preview
```

部署：

```bash
# Cloudflare Pages：连接 Git 仓库，build command = pnpm run build，output = dist
# 或：
npx wrangler pages deploy dist --project-name=ai-seminar
```

---

## 6. 三天任务拆解

### Day 1：骨架 + 内容导出
- [ ] `pnpm create astro`，装 Tailwind/KaTeX；
- [ ] 定 `seminar.json` 契约；
- [ ] 写 `export_site.py`，从 JP11 的 `seminar.yaml`/`map.yaml` 导出 L0 JSON；
- [ ] 首页 + 详情页静态骨架。

### Day 2：内容 + 视觉
- [ ] 一页纸排版；
- [ ] 章节地图组件；
- [ ] claims/questions 列表组件；
- [ ] 方法页；
- [ ] 移动端检查。

### Day 3：版权 + 构建 + 部署
- [ ] `copyright_scan.py`；
- [ ] `/about` 版权说明；
- [ ] Pagefind 搜索（可选）；
- [ ] 部署 preview；
- [ ] 用手机/桌面各走一遍；
- [ ] 记录 Lighthouse 分数。

---

## 7. 验收标准

- [ ] 首页、详情、笔记、方法、关于 5 个页面可访问；
- [ ] 手机/桌面均可读，无横向滚动；
- [ ] 一页纸在首屏可读；
- [ ] 每条 claim 有锚点，点击可跳到对应章节说明；
- [ ] 版权扫描零超阈值；
- [ ] Lighthouse 性能 ≥90，可访问性 ≥90；
- [ ] 部署 URL 可分享；
- [ ] 页面明确写“不含译文全文”。

---

## 8. 成本与运维

| 项目 | 费用 |
|---|---:|
| 域名 | ¥70–100/年 |
| Cloudflare Pages | 免费 |
| 构建 | 本地/CI 免费 |
| 总计 | **<¥200/年** |

运维：
- `main` 自动部署；
- 每月检查链接；
- 内容更新走 PR；
- 下架流程写在 `/about`；
- 不做用户追踪，最多用隐私友好的访问统计。

---

## 9. 第二版再做什么

- Pagefind 全文搜索；
- Cytoscape 交互论证图；
- claims/questions 筛选与 permalink；
- 多篇研讨班列表与主题聚合；
- 术语总表跨文献检索；
- RSS/更新日志。

**第一版不做**：用户系统、评论、付费、全文阅读、AI 问答。
