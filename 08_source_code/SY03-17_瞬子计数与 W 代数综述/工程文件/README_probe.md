# probe.md —— 环境与底本实测记录（2026-11-04，本机 Windows / DeepSeek Harness）

> 原则：以下每条都是**实测**，不是推测。未测的项目不写。

## 1. 工具链

| 项 | 实测值 |
|---|---|
| TeX 引擎 | `LuaHBTeX, Version 1.24.0 (TeX Live 2026)` |
| TeX bin | `<本地路径>`（`lualatex.exe` 存在，已实测） |
| TeX 发行版 | TeX Live 2026（`texmf-dist` 存在；本机 2026-11-03 已补装到 3481 包） |
| Python | `<本地路径>`（3.12） |
| PDF 库 | `pymupdf 2.0 / MuPDF 1.28.5`（`import pymupdf` 成功） |
| 冒烟编译 | **通过**：c00（中文标题页/摘要/译者说明/目录）+ c01（§1 中文正文 + 式 (1.1) + 图 1 + 表 1 测试）→ LuaLaTeX×3，`file:line=0 / !=0 / undefined=0 / missing-char=0`，`main.pdf` 201850 bytes |
| 中文字体 | LuaLaTeX + ctex 自动取系统字体，**未**加 fontset / 未手写 `\setCJKmainfont`，中文正常（已渲染目视确认） |
| 裁图脚本 | `work\tools\crop.py`（PDF 点坐标，默认 500 dpi，已指向本论文 PDF） |

## 2. 本机硬约束（沿用 v2.0 手册实测，本机复验一致）

- `lualatex` 在**非 ASCII 路径**下无法写 `.log`；**子进程不能写 Desktop**。
  → 本工程把 `work\src` + `work\figures` 镜像到 `<本地路径>` 再编译，PDF 拷回。
- `TMP`/`TEMP` 必须显式指向可写目录（build.ps1 已设到镜像目录下 `tmp\`）。
- 编译日志**绝不重定向到 `main.out`**（TeX 会当输入读）。
- 项目根 `<本地路径>` 为 ASCII 路径，可写。

## 3. 底本（Deck Check）

| 检查项 | 实测值 | 方法 |
|---|---|---|
| 文件 | `1412.7121v1.pdf`，1,105,669 bytes，`format=PDF 1.5`，`producer=pdfTeX-1.40.12` | `doc.metadata` |
| 作者 / 标题 | **Yuji Tachikawa** / *A review on instanton counting and W-algebras*（IPMU-14-0030, UT-14-6） | 首页文字层实测（metadata 的 title/author 均为空，不能按 metadata 猜） |
| 页数 | **43**，页面 595.276 × 841.890 pt（A4） | `len(doc)` |
| 页码偏移 | **PDF 页号 = 印刷页码 + 1**（PDF p.2 印页码 1；PDF p.5 印页码 4） | 逐页末行实测 |
| 位图 | **0 张** | `sum(len(p.get_images()))` |
| 矢量图 | 189 个 drawings（含 4 张图与公式横线） | `sum(len(p.get_drawings()))` |
| 图 | **4 张**：Figure 1 p.11、Figure 2 p.15、Figure 3 p.19、Figure 4 p.23 | 逐页正则 `(Figure|Table)\s*\d+\s*[:.]` + 页面图像目视 |
| 表 | **1 张**：Table 1 p.28 | 同上（逐页正则，未漏） |
| 目录（TOC） | 23 条（§1–§5 + 15 个 subsection），与正文起始页逐条比对一致 | `doc.get_toc()` |
| 编号公式 | **121 条**：1.1；2.1–2.11（11）；3.1–3.76（76）；4.1–4.12（12）；5.1–5.21（21） | 逐页 span 提取 + 分节单调过滤（`tools/prep2.py`），0 缺 0 重 |
| 参考文献 | **173 条** = 本卷内 [V:1]–[V:13] + 一般文献 [1]–[160]，0 缺号 0 重号 | `tools/gen_refs2.py` 从 pp.34–43 文字层解析 |
| 章节 | 1 Introduction；2 Gauge theory and the instanton moduli space；3 U(N) gauge group on R4；4 Other gauge groups；5 Other spaces + Acknowledgment | TOC + 正文 |
| 特殊结构 | 无 Part、无灰底要点框、无 Exercise；有 itemize 并列项与粗体行内小标题（Organization） | 逐页图像目视 |

**正文/文献分界**：PDF p.34 上半页为 Acknowledgment，p.34 下半页起为参考文献，至 p.43 结束。

## 4. 素材产出（已生成，位于 `work\`）

| 路径 | 内容 | 数量 |
|---|---|---|
| `pages/pNNN.png` | 200 dpi 逐页渲染 | 43 |
| `split/pNNN.txt` / `full.txt` | 逐页文字层 / 整本文字层 | 43 |
| `tags.txt` / `tags_bypage.txt` | tag → 页 / 页 → tags | 121 |
| `figures/fig1–4.png` | 450 dpi 裁图，`read_image` 复核：完整、无截断、无图注残影 | 4 |
| `figures/tab1.png` | 表 1 截图（仅供核对转录） | 1 |
| `glossary.tsv` | 术语冻结表 | 见文件 |

原始探测输出（未加工）保留在 `probe/probe_raw.md`；公式候选原始清单在 `probe/tags_raw.txt`。
