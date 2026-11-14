# EN48 — Cannizzo《亏格 2 曲线的同调镜像对称》中文译注本

**状态：已交付 v1.0（2026-11-12；成品 106 页；`check.py` PASS）**　｜　文献号 EN48　｜　主题域 01\_镜像对称与同调镜像对称
立项日期 2026-11-12　｜　样板块 c00、c01 已验收（Lead）

## 底本

| 项 | 内容 |
|---|---|
| 作者 | Catherine Kendall Asaro Cannizzo |
| 原题 | *Homological mirror symmetry for the genus 2 curve in an abelian variety and its generalized Strominger–Yau–Zaslow mirror* |
| 中译名 | 《亏格 2 曲线的同调镜像对称及其广义 Strominger–Yau–Zaslow 镜像》 |
| 类型 | 博士学位论文（T） |
| 学位/单位 | PhD in Mathematics, University of California, Berkeley, Spring 2019 |
| 导师/委员会 | Denis Auroux（主席）、David Nadler、Marjorie Shapiro |
| 来源 | eScholarship 开放获取 <https://escholarship.org/uc/item/88g945z7> |
| 本地底本 | `work/source/EN48_原文_Cannizzo2019_145p.pdf`（1,569,233 B / 145 页 / 文字层可抽取） |
| 语种 | 英文 → 中文 |
| 原书结构 | 正文页码 1–136；前置页罗马数字 i–v；6 章 + 参考文献；21 张图；无附录 |

**页映射：原书页 = PDF 页 − 9。** 例：PDF p.10 = 原书 p.1；PDF p.141 = 参考文献 p.132。
前置页：PDF p.5=i（献词）、p.6=ii（目录）、p.7–8=iii–iv（图目录）、p.9=v（致谢）；
PDF p.1–4 为 eScholarship 封面、扉页、版权页、摘要（摘要页未编页码）。
源码中每页起首以注释 `% ===== 原书 p.N =====` 标出。

**文字层文件名按「章」编号，不按块编号**：`work/en/ch01_en.txt`=第 1 章（c02、c03）、
`ch02_en.txt`=第 2 章（c04）、`ch03_en.txt`=第 3 章（c05）、`ch04_en.txt`=第 4 章（c06–c08）、
`ch05_en.txt`=第 5 章（c09）、`ch06_en.txt`=第 6 章（c10）、`ch07_bib_en.txt`=参考文献（c11）。

## 工程文档

- 施工总纲（**先读**）：`BRIEF.md`（块划分、每块工作流、LaTeX 规范、文风指标、报告模板、术语草案）
- 翻译纪律（必读全文）：`<本地路径>`
- 总纲（§1.4/§1.5/§5.3/§7.1/§7.2）：`<本地路径>`
- 编号登记表：`<本地路径>`（EN48 行已建，状态「在译」）

## 目录

```
BRIEF.md  README.md  build.ps1  check.py
src\        preamble.tex  main.tex  chunks\c00..c11.tex  figures\  tools\{compile_chunk.py,zoom.py}
work\       source\（底本 PDF） en\（全文/分章文字层） page_map.csv pages\（145 张 130dpi 页图） zoom\ tmp_cNN\ main_build\
deliverable\  成品（PDF + 七件套，交付时生成）
reports\      每块报告 cNN.md
review\       双校记录
```

## 进度表（Lead 统一维护；teammate 不要直接改本表）

| 块 | 原书页 | 内容 | 状态 | 报告 | 完成日期 |
|---|---|---|---|---|---|
| c00 | i–v | 摘要、献词、致谢 | 已完成 | `reports/c00.md` | 2026-11-12 |
| c01 | 1–12 + 13 上 | 1.1 结果陈述 + 1.2 B 侧流形（**样板块**） | 已完成 | `reports/c01.md` | 2026-11-12 |
| c02 | 13 中–23 上 | 1.3 环簇的背景 | 已完成 | `reports/c02.md` | 2026-11-12 |
| c03 | 23 中–43 | 1.4 A 侧流形 + 1.5 辛形式的定义 | 已完成 | `reports/c03.md` | 2026-11-12 |
| c04 | 44–69 | 第 2 章 辛形式 ω 的非退化性 | 已完成 | `reports/c04.md` | 2026-11-12 |
| c05 | 70–81 | 第 3 章 阿贝尔簇 V 与 V∨ 的 HMS | 已完成 | `reports/c05.md` | 2026-11-12 |
| c06 | 82–91 上 | 4.1 Fukaya–Seidel 范畴：引言 | 已完成 | `reports/c06.md` | 2026-11-12 |
| c07 | 91 中–110 上 | 4.2 背景 + 4.3 模空间 | 已完成 | `reports/c07.md` | 2026-11-12 |
| c08 | 110 下–113 | 4.4 定义与选择的无关性 | 已完成 | `reports/c08.md` | 2026-11-12 |
| c09 | 114–130 | 第 5 章 主定理 | 已完成 | `reports/c09.md` | 2026-11-12 |
| c10 | 131 | 第 6 章 记号 | 已完成 | `reports/c10.md` | 2026-11-12 |
| c11 | 132–136 | 参考文献 | 已完成 | `reports/c11.md` | 2026-11-12 |

状态取值：未开始 / 进行中 / 已完成 / 需返工。

## 块边界调整记录（页码是指导，小节完整性优先）

块的页码区间按「小节归属」微调，保证小节不被页边界切断、定理编号不跨块：

| 边界 | 调整 | 理由 |
|---|---|---|
| c01 / c02 | 原书 p.13 上半（§1.2 收尾：引理 1.2.24、断言 1.2.25、推论 1.2.26）归 **c01**；c02 从 p.13 中部 §1.3 起 | §1.2 不能断在三条结果中间；定理计数器按小节归零 |
| c02 / c03 | §1.3 延续到 p.23 上部（推论 1.3.29、注 1.3.30）归 **c02**；c03 从 p.23 中部 §1.4 起 | 同上 |
| c06 / c07 | §4.1 的 Claim 4.1.28 证明跨到 p.91 上部，收尾归 **c06**；c07 从 p.91 中部 §4.2 起 | 证明不能截断 |

## 术语冻结

- 版本：**v1（已冻结）**，2026-11-12，`work/glossary.tsv`，**241 条**（242 行含表头），无「待定」项。
  - 术语勘误一处：`Landau–Ginzburg model` 由 v0 的「朗道–金兹堡模型」改为「Landau–Ginzburg 模型」（保留英文），与 c01 正文一致；c04 同步修改。
  - 其余以「v1 追加（只增不改）」补入 c02（35 条）、c03（16 条）、c04（2 条）、c05（25 条）、c06（19 条）、c07（20 条）、c08（9 条）、c09（12 条）的表外术语；已冻结译名一律未动。
  - 主体 104 条为 c00/c01 冻结版；其后以「v1 追加（只增不改）」方式补入 c02（35 条）、c03（16 条）、c05（25 条）、c07（20 条）、c08（9 条）、c09（12 条）的表外术语（环簇术语；广义 SYZ 镜像/凯勒势/富比尼–施图迪形式/对数坐标/热带极限；族 Floer 理论/双边形/厚包络/Serre 对偶；香蕉流形/类截面映射/伪闭链/虚拟维数；拟等价/有向范畴/局部化/TQFT/虚拟基本链；球泡/点层/开闭 Gromov–Witten/Kuranishi 结构等），已冻结译名一律未动。
- v0 → v1 变更摘要：
  - 落定 v0 待定 5 条：`strip-like end`→条状端；`bounding cochain`→保留英文（中文无稳定译名）；`monodromy`→**单值性**（v0 误作「单值化」，那是 uniformization）；`tilings / tile`→瓦片；`hermitian`→Hermite。
  - 新增（c00/c01）：自守因子（factor of automorphy，不用「自同构因子」）、乘子、Hermite 形式/矩阵、半正交分解、正规交叉、例外除子、真变换、收缩映射、酉平坦联络、平坦联络、过渡函数、万有覆盖、覆盖、Picard 群、Cartier 除子、主除子、Čech 上同调、指数正合列、第一 Chern 类、反对称、双线性形式、格、Morse–Bott 纤维丛、可容、热带化、计数意义、凯勒参数、镜像映射、纤维、底空间、次数、零纤维、上同调深谷范畴、上同调 Fukaya–Seidel 范畴。
- 冻结后：**禁止跨块改译名**；确需修改须全局替换 + 三同步（正文/术语表/README 变更日志），并在报告里写明。teammate 遇表外术语按「中文（English）」首现括注，写进报告与给 Lead 的消息，由 Lead 决定是否入表。

## 并行施工约定（2026-11-12 起）

1. **写作用域互不重叠**：每个 teammate 只写自己负责的 `src/chunks/cNN.tex`、自己的 `src/figures/` 图、自己的 `reports/cNN.md`。不得改 `preamble.tex`、`main.tex`、`README.md`、`work/glossary.tsv`、其他块、`check.py`、`build.ps1`、`04_编号登记表.csv`。
2. **README 只由 Lead 更新**（并行编辑会冲突）；teammate 完成后用 `send_message` 向 Lead 汇报，由 Lead 回填进度表。
3. **块内只 `\ref` 本块定义的 label**：单块 `compile_chunk.py` 要求 `undefined=0`，跨块引用一律用文字（如「§1.2」「第 1 章主定理」）。
4. 工具链：`compile_chunk.py` 每块必须 `errors=0 overfull=0 undefined=0 missing_char=0`（underfull 不计）；`zoom.py` 参数为 PDF 点（PDF点 = 130dpi 像素 × 72/130）；图从 PDF 页 600dpi 裁切。
5. Lead 最后统一跑 `build.ps1` 与 `check.py`，跑完按 BRIEF §12 出七件套并更新登记表。

## 已就绪的骨架

- `src/preamble.tex`：章节样式（第 N 章 / 1.1）、**共享定理计数器**（原文各环境共用
  章.节.序号编号，如 注 1.2.1 → 定义 1.2.2 → 断言 1.2.4）、公式/图/表按章编号、
  `\transnote`、记号宏、`\Vdual`、`\DBCoh` 等。
- `src/main.tex`：扉页、译本说明（含页映射）、内容提要、目录、12 个 `\input`。
- `src/chunks/c00..c11.tex`：块骨架，**标题行已给、正文待译**，首行注释含页码与内容说明。
- 已验证：`compile_chunk.py` 对 c00、c01 均四项全 0；`check.py` 在 c00+c01 阶段 VERDICT: PASS。

## 编译

```powershell
# 单块自检（必须全 0）
python src\tools\compile_chunk.py c01
# 整书三遍 + 质量统计，成品复制到 deliverable\
pwsh -File build.ps1
# 交付前审计（句式/连字/手工编号/整书指标），末行 VERDICT: PASS
python check.py
# 公式/插图局部放大（参数：PDF 页 dpi x0 y0 x1 y1，单位 PDF 点）
python src\tools\zoom.py 23 300 100 100 500 400
```

## 变更日志

| 日期 | 变更 |
|---|---|
| 2026-11-12 | 立项：建目录、复制底本、抽取全文（272,433 字符）、渲染 145 张 130dpi 页图、分块文字层、页映射表；写 preamble/main/12 块骨架/编译自检工具；登记表 EN48 置「在译」；glossary v0 草案；c00/c01 骨架编译验证通过。 |
| 2026-11-12 | **c00 完成**（摘要/献词/致谢；8 条译者注；compile 四项全 0），报告 `reports/c00.md`。 |
| 2026-11-12 | **c01 完成**（§1.1–1.2 + p.13 上半；31 定理环境、9 编号公式、13 译者注、图 1.1、tikz-cd 交换图；compile 四项全 0），报告 `reports/c01.md`，双校记录 `review/ch01_c00-c01.md`；`check.py` VERDICT: PASS。 |
| 2026-11-12 | **术语 v1 冻结**（104 条，无待定），落定 5 条待定、改正 monodromy、新增 35 条（详见「术语冻结」）。 |
| 2026-11-12 | 块边界三处调整（c01/c02、c02/c03、c06/c07，详见「块边界调整记录」）。 |
| 2026-11-12 | 启动 6 个 teammate 并行施工 c02–c11（t-c02、t-c03、t-c04、t-c05c06、t-c07c08、t-c09c10c11）；README 改为 Lead 统一维护。 |
| 2026-11-12 | **c05 完成**（第 3 章；22 定理环境 3.0.1–3.0.22、1 编号公式 (3.1)、图 3.1、11 译者注；compile 四项全 0），报告 `reports/c05.md`；c05 中 6 处字面编号（含注释）已由 Lead 改为「原书 X.Y.Z」式引用；术语 v1 追加 25 条。 |
| 2026-11-12 | **c02 完成**（§1.3；30 定理环境 1.3.1–1.3.30、无编号公式、2 张无编号插图、12 译者注；compile 四项全 0），页范围定为「p.13 中部–p.23 上部」，报告 `reports/c02.md`；术语 v1 追加 35 条环簇术语。 |
| 2026-11-12 | **c07 完成**（§4.2–4.3 + p.110 上部；32 定理环境 4.2.1–4.3.22、3 图、11 译者注；compile 四项全 0），报告 `reports/c07.md`；术语 v1 追加 20 条。 |
| 2026-11-12 | **c09/c10/c11 完成**（第 5 章 24 定理环境 5.1.1–5.1.24、3 图 + tikz 流程图 + 2 交换图、12 译者注；第 6 章记号 3 译者注；参考文献 53 条不译、1 译者注；compile 四项全 0，underfull 各 1 不计），报告 `reports/c09.md`、`reports/c10.md`、`reports/c11.md`；术语 v1 追加 12 条。 |
| 2026-11-12 | **c03 完成**（§1.4–1.5；27 定理环境 1.4.1–1.5.3、13 编号公式 (1.10)–(1.22)、10 图 1.2–1.11、13 译者注；compile 四项全 0），页范围「p.23 中部–43」，报告 `reports/c03.md`；术语 v1 追加 16 条。 |
| 2026-11-12 | **c08 完成**（§4.4；9 定理环境 4.4.1–4.4.9、1 图、10 译者注；compile 四项全 0），页范围「p.110 下部–113」，报告 `reports/c08.md`；术语 v1 追加 9 条。c07 报告中「p.110 上 6 条 bullet」更正为 5 条。 |
| 2026-11-12 | **c04 完成**（第 2 章；4 定理环境 2.0.1–2.1.2、无编号公式、3 图、11 译者注；compile 四项全 0，underfull 1 不计），报告 `reports/c04.md`；术语 v1 追加 2 条；`Landau–Ginzburg model` 术语勘误已同步到 c04。 |
| 2026-11-12 | **c07 交叉双校完成**（t-c09c10c11，`review/ch04_c07.md`）：抽检 14 条公式/定理 + 5 条译注，发现 9 处问题（3 处译注事实错误、2 处错字、3 处增义、1 处建议补注），数学与编号 0 错误；问题已交 t-c07c08 修正。 |
| 2026-11-12 | **c06 完成**（§4.1 + p.91 上部；28 定理环境 4.1.1–4.1.28、4 编号公式 (4.1)–(4.4)、1 图、12 译者注；compile 四项全 0），页范围「p.82–91 上部」，报告 `reports/c06.md`；术语 v1 追加 19 条。**至此 12 块初译全部完成**。 |
| 2026-11-12 | **c07 双校修正 7 处**（宽度 1→π、上半圆盘→下半圆环、条状端极限方向、「算盘计数」→「圆盘计数」、删两处增义、补上划线说明）；c07 重编译四项全 0；`reports/c07.md` 新增「双校修正记录」。 |
| 2026-11-12 | **整书编译**：`build.ps1` 三遍 → `pages=106 errors=0 overfull=0 underfull=4 undefined=0 missing_char=0`，成品 `deliverable/EN48_Cannizzo_亏格2曲线HMS_中文译注本.pdf`。 |
| 2026-11-12 | **交付审计**：`python check.py` →**VERDICT: PASS**（12 块齐、病灶句式 0、连字 0、手工编号 0、汉字间半角标点 0；transnote 合计 117 条；label 244、ref 66，无重名）。 |
| 2026-11-12 | **v1.0 交付**：七件套入 `deliverable/`（成品 PDF 106 页、README、译注汇总 117 条、阅读参考指南、工程总结、术语对照表 241 条、源码 zip）；`04_编号登记表.csv` 的 EN48 行改为「已交付 / 106 页 / 2026-11-12 / deliverable 路径」。 |

## 当前队列与收尾步骤

**已完成**：12 块初译、整书编译、`check.py` PASS、七件套交付、登记表更新。

**v1.0 交付记录**（2026-11-12）：

- 成品 PDF：`deliverable/EN48_Cannizzo_亏格2曲线HMS_中文译注本.pdf`，**106 页**
- 编译指标：errors=0 overfull=0 undefined=0 missing_char=0（underfull 4，不计）
- 审计：`python check.py` → `VERDICT: PASS`
- 规模：207 定理环境、27 编号公式、22 编号图 + 3 无编号插图、117 译者注、241 条冻结术语、源文件 5 990 行
- 登记表：EN48 → 已交付（页数 106，路径指向成品 PDF）

**后续可选**：做「已校订」版时优先通读 c04（计算最密）、复核 c03 的 10 张图注页码、逐条核对 117 条译注的数学陈述（详见 `deliverable/工程总结.md` 第四节）。

