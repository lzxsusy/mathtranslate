# Mark Gross《Tropical Geometry and Mirror Symmetry》中文译注工程

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 为准：语料 / 轨迹 / 会话 CC BY 4.0，明确欢迎用于训练与蒸馏（译文与工程文档 CC BY-NC-SA 4.0）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

> 底本：Mark Gross, *Tropical Geometry and Mirror Symmetry*, AMS CBMS Regional Conference Series in Mathematics **114**, American Mathematical Society, 2011（NSF-CBMS 2008 Kansas State 十讲）。原书 332 页，本工程翻译前言/引论 + 正文第 1–6 章（印刷 pp.1–306）；参考文献保留英文原貌，索引从略。

## 目录结构

```
TropicalGeometry_中文译注/
├─ src/
│  ├─ main.tex            汇总（Lead 独占）
│  ├─ preamble.tex        导言区（Lead 独占；定理环境按章自动编号）
│  ├─ chunks/c00 … c06d  各翻译块（译者交付）
│  ├─ Gross_TropicalGeometryAndMirrorSymmetry.pdf   底本
│  └─ main.pdf            编译产物（当前进度）
├─ work/
│  ├─ pages/pNNN.png      逐页 150 dpi 渲染（公式唯一真值）
│  ├─ split/pNNN.txt      逐页文字层（只用于定位，数学不可信）
│  ├─ full.txt            整本文字层
│  ├─ tags.txt            128 条编号公式清单（tag → 印刷页 → PDF 页）
│  ├─ tags_bypage.txt     页 → tags
│  ├─ figs.tsv            图标题检测结果（可能不全）
│  ├─ figures/f<章>_<图号>.png  译者裁出的原图
│  ├─ tools/              裁图（crop.py）、静态检查（check_project.py）、素材脚本
│  ├─ STYLE_GUIDE.md      翻译规范（术语、公式、图、批注、自检）
│  ├─ BRIEF.md            分工与接续点
│  ├─ TIMELINE.md         裁决与进度记录
│  ├─ glossary.tsv        术语冻结表（英→中）
│  ├─ probe.md            底本尽调（实测页数/页码偏移/公式数/图数/定理数）
│  └─ tmp/                临时放大图、编译日志
├─ build.ps1              编译脚本（镜像到 ASCII 目录后用 TeX Live 2026 LuaLaTeX 编译三遍）
└─ deliverable/           最终交付包（PDF + src + 日志 + 译注汇总 + README）
```

## 编译

```powershell
powershell -ExecutionPolicy Bypass -File .\build.ps1
```
- 本机硬约束：LuaLaTeX 在中文路径下无法写 `.log`，且子进程不能写 Desktop，因此脚本把 `src/` 与 `work/figures/` 镜像到
  `<本地路径>` 再编译，成功后把 `main.pdf` 拷回 `src/main.pdf`。
- 编译三遍（交叉引用/目录）。

## 关键约定（详见 work/STYLE_GUIDE.md）

- **页码**：PDF 页（1-based）= 印刷页 + 15；前言/引论为罗马页码（i–xvi）。
- **公式编号**：一律 `\tag{…}` 手工对应原文 128 条编号公式（`work/tags.txt` 为验收依据）；无编号公式不得自造编号。
- **定理类环境**：全书共用一个章节内计数器（Definition 1.1 / Examples 1.2 / Lemma 1.13 / Proposition 1.15 …），
  由 preamble 自动编号；与原文编号冲突时照原文语义 + 批注说明。
- **图**：原文按章内连续编号（每章从 Figure 1 开始）；译者从页图裁出 400–600 dpi PNG，图注照译。
- **批注**：形如 `% [Tutor Note: …]`，编译不显示；汇总见 `work/译注汇总.md`。
- **引用**：正文引用公式/节/图/文献全部用纯文本（如“式 (2.37)”“§2.3”“图 5”“[80]”），不用 `\ref`/`\cite`。

## 当前状态（2026-11-05 完成第一版）

- **全书译完并编译通过**：`src/main.pdf` 共 **297 页**（原书 332 页；A4/11pt 中文排版）。
- 范围：书名页/译者说明/前言/引论 + 正文第 1–6 章（印刷 pp.1–306）+ 参考文献（保留英文原貌，暂以原页图像排版）。
- **129/129 条编号公式**与原文一一对应（`work/tags.txt` 校验：无缺、无重、无自造；含文字层漏检、从页图补出的 (4.7)）。
- 定理类环境共用一个章节内计数器，自动编号与原文一致（Definition 0.1、1.1–1.33、2.1–2.45、3.1–3.44、4.1–4.27、5.1–5.60、6.1–6.49）。
- 图：第 1–6 章共 60+ 张图从页图裁出并插入；无图注的按原文只印编号。
- 译者批注 **208 条**（`work/译注汇总.md`），每 2–3 页 ≥1 条。
- 逐块分工与交接记录见 `work/TIMELINE.md`；规范见 `work/STYLE_GUIDE.md`。
- 已知限制：① 参考文献尚未转成校对后的文字（现为原页图像）；② 各块由多人并行翻译，术语与文风已统一主要术语（glossary），但**尚未做全稿交叉校对（Gate 4）**；③ 图由页图裁切，个别图留有少量白边。

## 版权

底本版权归 Mark Gross 与 American Mathematical Society 所有。本译注本仅供个人学习研究使用，不用于商业传播。
