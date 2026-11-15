# 《量子力学与几何》中文译注

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：全库统一 CC BY 4.0，明确欢迎用于训练、蒸馏与商用（署名即可）。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

清华大学丘成桐数学科学中心（YMSC）李思（Si Li）教授讲义
***Quantum Mechanics and Geometry*** 的中文译注本 LaTeX 工程。

- **底本**：Si Li, *Quantum Mechanics and Geometry*, preliminary draft updated December 2025
  （作者主页 <https://sili-math.github.io/> 上 2025 年 11 月版 PDF，共 338 页）。
- **译文**：现代汉语，术语统一，公式逐符号回原书页图核对；陈述编号照抄原文；图按原图裁切或重绘。
- **体例**：见 `译者手册.md`（体例的唯一依据）与 `术语对照表.tsv`（术语的唯一依据）。

> 本译注本仅供学习交流使用，一切以原书为准。原文版权归作者所有。

---

## 目录结构

```
李思_量子力学与几何_中文译注/
├── 00_原文/
│   └── QM_Geometry_SiLi_2025-11.pdf     # 底本 PDF（338 页）
├── src/                                 # LaTeX 源码
│   ├── main.tex                         # 整书主文件（三部分 + 书末）
│   ├── preamble.tex                     # 导言区：版式、环境、记号宏
│   ├── frontmatter/                     # 书名页、联系页、前言、译注说明
│   ├── chunks/                          # 正文按块切分的译文（ch01a…ch06b、ch99_back）
│   ├── appendix/terms.tex               # 英汉术语对照（由工具生成）
│   ├── figures/                         # 从原书裁切的插图
│   └── build.ps1                        # 编译脚本
├── work/
│   ├── en/                              # 原文抽取的纯文本（按块）
│   ├── pages/                           # 原书逐页渲染的 PNG（公式核对的依据）
│   ├── review/                          # 人工核对的裁图与预览
│   └── preview/                         # 编译结果的页面预览
├── tools/                               # 抽取、渲染、裁图、检查、汇总工具
├── reports/                             # 各块的译校报告
├── deliverable/                         # 交付物（PDF、指南、总结等）
├── 术语对照表.tsv                        # 英→中术语冻结表
└── 译者手册.md                           # 翻译体例与工程纪律
```

## 编译

需要 MiKTeX（xelatex + ctex + tikz），中文路径可直接编译。

```powershell
# 整书（三遍 xelatex）
powershell -ExecutionPolicy Bypass -File src\build.ps1

# 只编某一块（快速自检，输出 work\tmp_<块名>.pdf）
powershell -ExecutionPolicy Bypass -File src\build.ps1 -Chunk ch02b
```

`build.ps1` 会解析日志并打印
`LOG file:line=? fatal=? missingchar=? overfull=? undefref=?`，
六项全为 0 时打印 `BUILD OK`。

> 注意：在本机 pwsh 里脚本最后可能显示 `[exit code: 1]`，那是 MiKTeX 的
> “未检查更新”提示走 stderr 被 PowerShell 当成错误记录，**不是编译失败**；
> 以 LOG 行为准。

## 工具

| 工具 | 用途 |
|---|---|
| `tools/extract_text.py` | 从原 PDF 抽取文本，按块写入 `work/en/`，带页标记 |
| `tools/render_pages.py` | 把原书逐页渲染成 `work/pages/pNNN.png`（公式核对用） |
| `tools/figtool.py` | 自动/手动裁切原书插图到 `src/figures/` |
| `tools/lint.py` | 体例自检：页标、takeaway、陈述编号、禁用译法、翻译腔、UTF-8 |
| `tools/crosscheck.py` | 对核：原文陈述编号 vs 译文环境编号、节数、页标记、疑似未译 |
| `tools/release_check.py` | 交付前总检（页标记覆盖 + lint + crosscheck + 图片引用） |
| `tools/make_terms_appendix.py` | 由术语表生成书末《英汉术语对照》 |
| `tools/collect_notes.py` | 汇总各块译者批注，生成 `deliverable/译注汇总.md` |

## 进度

**已完成**（17 块全部译完，且每块都经他人交叉审校）。终稿三过编译：

```
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
PDF ok  size=4 536 131 bytes
BUILD OK
```

全书 **379 页**（正文 366 页＋参考文献 4 页＋术语附录 9 页），译注汉字 **62 893**，
41 节 / 142 小节，带编号陈述 353 条，行间公式 2 602 个，图 110 处裁切位图＋29 处 TikZ 重绘，
译者批注 16 条，页标 325 条。详见 `deliverable/工程总结.md`；
分块与页段的对应关系写在 `译者手册.md` §1。

## 交付物（`deliverable/`）

| 文件 | 内容 |
|---|---|
| `量子力学与几何_李思_中文译注本.pdf` | 全书印刷稿（379 页，含目录、参考文献、术语附录） |
| `阅读参考指南.md` | 全书地图、三条阅读路线、逐章提要、易卡住处、配套资源 |
| `术语对照表.tsv` | 英→中术语冻结表（723 条，9 组） |
| `译注汇总.md` | 全书 16 条译者批注，按章分组并标原书页号 |
| `校订记录.md` | 审校组织、问题清点、术语裁定、照原文不改的清单 |
| `工程总结.md` | 工程概况、技术决策、质量保障与终稿数据 |
| `源码_LaTeX.zip` | LaTeX 源码、裁切插图、`build.ps1`、`译者手册.md` |

## 免责与致谢

本译注本为学习交流之用，原文版权归作者李思教授所有。原文讲义由作者在清华大学
开设课程形成，初稿由杨鹏录入（作者在前言中致谢）。中文译文与译注内容由本工程完成，
译文或体例问题欢迎指出。
