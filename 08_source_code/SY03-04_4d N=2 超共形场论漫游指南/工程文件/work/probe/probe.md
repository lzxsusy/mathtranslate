# probe.md —— 本机环境实测 + 底本尽调（2112.14764）

> 全部数据为本机实测（2026-11-05）。凡未实测的都标「未测」。

## 1. TeX 工具链

| 项目 | 实测值 |
|---|---|
| TeX bin | `<本地路径>` |
| 引擎 | `lualatex` = LuaHBTeX 1.24.0（TeX Live 2026） |
| 宏包 | 3481 个包（含 ctex / tcolorbox / tikz / booktabs / hyperref 等） |
| 冒烟编译 | **通过**：preamble + c00（中文标题页 + 目录 + hyperref + tcolorbox）LuaLaTeX ×3 = 0 error / 0 undefined / 0 missing char / 0 overfull |

## 2. 本机三条硬约束（实测，build.ps1 已按其实现）

1. `lualatex` 在**非 ASCII 路径**（中文目录）下无法写 `.log`（报 `I can't write on file main.log`）；
2. 子进程（`lualatex.exe`）**不能写 Desktop**；可写 `<本地路径>`；
3. `TMP`/`TEMP` 必须显式指向可写目录。
→ 结论：把 `work\src\*` 与 `work\figures\*.png` 镜像到 ASCII 目录
`<本地路径>` 再编译，最后把 PDF 拷回。

## 3. Python / PDF 库

| 项目 | 实测值 |
|---|---|
| Python | `<本地路径>`（3.12） |
| PyMuPDF | `pymupdf 2.0`（MuPDF 1.28.5）**可用** |
| Pillow | 可用（用于拼图核验） |

## 4. 底本尽调（Deck Check，实测）

| 检查项 | 实测值 |
|---|---|
| 文件 | `<本地路径>).pdf`（1,377,549 B） |
| 标题 | The Hitchhiker's Guide to 4d N=2 Superconformal Field Theories |
| 作者 | Mohammad Akhond, Guillermo Arias-Tamargo, Alessandro Mininno, Hao-Yu Sun, Zhengdi Sun, Yifan Wang, Fengjun Xu（首页作者行实测） |
| 编号 | arXiv:2112.14764v3 [hep-th]，2022-08-21（PDF metadata creationDate 2022-08-23） |
| 总页数 | **122**；页面尺寸 612×792 pt（US Letter） |
| 页码偏移 | **PDF 页 = 印刷页 + 1**（PDF p.3 = 印刷 p.2；PDF p.9 = 印刷 p.8 = §2 起点，已与目录核对） |
| 位图 | **0**（`get_images()` 全 0） |
| 矢量图 | **15 幅**（Figure 1–15，p8/19/27/29/38/42/54/58/62/63/64/65/66/72/74）→ 已按 450 dpi 裁为 `work\figures\fig1..15.png`，逐张目视复核 |
| 表 | **8 张**（Table 1–8，p14/30/47/70/75/89/92/94） |
| 编号公式 | **164 条**：§2 2.1–2.53；§3 3.1–3.42；§4 4.1–4.33；§5 5.1–5.36；§1/§6 无编号公式。提取核对：缺 0 / 重 0 |
| 定义/例/习题 | 定义 2.1–2.5；例 3.1、4.1–4.9、5.1–5.3；习题 2.1–2.4、3.1–3.2、4.1–4.3、5.1 |
| 附录 | 无 |
| 结构 | §1 p2｜§2 p8｜§3 p30｜§4 p47｜§5 p75｜§6 p92｜致谢 p96｜参考文献 p96–121（印刷页） |
| 目录可信度 | 与正文实际起始页一致（逐项核对 p2–3 目录） |
| 文献 | PDF p.97 起至 p.122（`[1]`–；自动转录，未逐条校对） |

## 5. 写盘与工作目录

| 路径 | 可写 | 用途 |
|---|---|---|
| `<本地路径>` | 是（文件工具可写；lualatex 不可直接写） | 项目根（源码、素材、交付） |
| `<本地路径>` | 是（lualatex 可写） | 镜像编译目录 |

## 6. 结论

环境与素材均就绪：冒烟编译通过（0 error），164/164 编号公式清单已冻结，15 图 8 表已普查并裁好。
→ 可以进入分工与并行翻译阶段。
