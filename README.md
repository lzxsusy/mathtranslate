# 数译 · 中文数学译注文献库（数据集与语料）

> 让散落的数学资料得以保存，让数学术语形成共识。

> **施工标准（硬性）**：本库全部译注工程一律按 [`04_playbook/01_数学文献翻译纪律.md`](04_playbook/01_数学文献翻译纪律.md) **v2.1** 执行——
> 先通读后落笔（§1.0）、译注必须有来源并可追溯（§2.5）、来源黑名单与语料卫生（§2.5.9）。
> **每次开工前、每次接手别人的稿、每次交付前都要重读对应章节**；文件库总入口见 [`04_playbook/README.md`](04_playbook/README.md)。

本仓库是「数译」工程的**数据与语料发布仓**：把一批中文数学译注本、工程原件、术语资产、
AI 辅助翻译的过程轨迹、以及威腾文章研讨班的组织资料整理成**可以被别人直接拿去用**的数据。

- 译者/整理者：超对称梦想家（chaoduicheng）
- 用途：学术研究、教学；自产层可用于模型训练与蒸馏，译文层仅限非商业研读（见「使用许可」）

<!-- STATS:BEGIN -->

| 指标 | 数值 |
|---|---|
| 译注工程 | **96** 部（其中 **82** 部带完整 LaTeX 源码） |
| 仓库文件 | 6764 个 / **321.2 MB** |
| LaTeX 源文件 / 插图 | 1581 个 `.tex` / 2118 张图 |
| 成品 PDF（预印本类） | 41 部 / **50.8 MB**（Release 附件） |
| 中文段落语料 | **49038** 段（唯一 47471），其中 **42153** 段含公式（86%）；汉字 4,035,712 字 |
| 语料覆盖 | **81** 个工程有段落入库（其余为仅成品 PDF / 无正文的工程） |
| 近重复标注 | 1418 段（保留，标 `near_dup_of`） |
| 术语基 | 1627 条 |
| 精选轨迹 | 402 条 |
| 原始会话分片 | 4 片 / **144.6 MB**（Release 附件） |

<!-- STATS:END -->

## 这是一个有明确倾向的文献库（不是泛泛的数学资料堆）

**一句话**：本库集中在 **「镜像对称 — 辛几何 / 拓扑弦 — 量子场论与规范理论 — 几何朗兰兹 / 电磁对偶」**
这一条几何与数学物理的交叉带上，只收那些**能把这条主线某一段讲清楚**的材料，把它们译成中文，
并把工程、术语与语料一起放出来。

收起这些材料是**强烈个人取向**的结果：主线之外的经典教材基本不收，所以本库看起来"偏"是故意的。

### 收什么（按优先级）

1. **主线奠基性论文与系统讲义**：Fukaya 范畴与同调镜像对称、Gromov–Witten 不变量与量子上同调、SYZ 猜想、
   Batyrev–Borisov 环面构造、Kontsevich / Givental 的镜像对称公式、Floer 同调与 Hofer 几何。
2. **数学物理交叉的综述与讲义**：N=(2,2) 超共形场论、拓扑弦、CY 三维流形紧致化、
   Kapustin–Witten 对偶与几何朗兰兹、AGT 对应、Seiberg–Witten 理论、瞬子与单极子。
3. **三语学派文献**（本库的一个特色）：
   - **日本学派**：京都大学 RIMS 講究録、京大 / 阪大 / 东大的镜像对称与辛几何讲义
     （深谷賢治、植田一石、高橋篤史、梶浦宏成、入谷寛、秦泉寺雅夫、野原雄一）；
   - **法国学派**：Bourbaki 报告（946 / 981 / 884 / 801）、Astérisque、Claire Voisin 的 K3 与镜像；
   - **俄罗斯学派**：Batyrev–Borisov 组合镜像对称、Orlov 的导出范畴与镜像。
4. **威腾（Witten）系列**：拓扑弦与量子上同调、Gauge Theory and Geometric Langlands、Kapustin–Witten 对偶、
   Jones 多项式与 Chern–Simons。本库目前收 9 篇，另有独立的威腾研讨班工程 `papers/`。
5. **有工程价值的博士论文与专题论文集**：能补上主线某个技术缺口的（例如正特征几何朗兰兹、驯顺分歧、
   Hitchin 系统的自对偶解）。

### 不收什么（避免摊大饼）

- **传统数论方向的 Langlands 纲领**（自守表示、迹公式、L-函数那一支）——与本库的几何侧是两条路，
  已有成熟中译的不重复造；
- **通用教科书**（微积分、线性代数、微分几何导论、代数几何入门等"谁都能买到"的）；
- 与数学物理无关的纯组合、纯分析题目；
- **无法溯源底本**、或只有二手转述的材料（施工纪律要求每条译注可追溯到原文页码）。

### 按主题的分布（83 部译注工程 / 10,303 页）

| 主线 | 编号 | 部数 | 页数 | 内容举例 |
|---|---|---|---|---|
| 辛几何 · 拓扑 · 纽结 · 指标定理 | `SY05` | 22 | 2,913 | Hofer 几何、Floer 同调、K-理论、指数定理、Jost 黎曼几何 |
| 量子场论与规范理论 | `SY03` | 21 | 2,266 | 超对称、AGT、共形场论、瞬子、Seiberg–Witten |
| 镜像对称与同调镜像对称 | `SY01` | 19 | 1,738 | SYZ、深谷范畴、Kontsevich 对偶、Batyrev 构造、植田一石讲义 |
| 弦论与紧致化 | `SY04` | 3 | 198 | 拓扑弦、CY 紧致化、D-膜 |
| 几何朗兰兹与电磁对偶 | `SY02` | 8 | 1,005 | Hecke 本征层、Hitchin 系统、Kapustin–Witten、Frenkel 圈群讲义 |
| 其他几何（热带 / 范畴 / 量子力学与几何） | `SY07` | 7 | 1,717 | 热带几何、导出范畴、几何量子化 |
| 拓扑学与专题 | `SY99` | 3 | 466 | Novikov 拓扑学、TQFT 博士论文、讨论班讲义 |

## 关键词（供检索与打标签）

下面这些词就是本库的"检索面"：找得到本库的中英文说法、以及日文原题里的对应写法。
（下游做检索增强、做术语对齐、或给别人写推荐语时可以直接用。）

**镜像对称 / Mirror Symmetry / ミラー対称性**
镜像对称、同调镜像对称、SYZ 猜想、Lagrange 环面纤维化、Fukaya 范畴、深谷范畴、Gromov–Witten 不变量、
量子上同调、Kontsevich 镜像公式、Givental 公式、Batyrev–Borisov 环面构造、环面几何、Landau–Ginzburg 模型、
B 模型 / A 模型、开闭弦镜像、ホモロジー的ミラー対称性、深谷圏

**辛几何与拓扑 / Symplectic Geometry & Topology / シンプレクティック幾何**
辛流形、辛容量、Arnold 猜想、Floer 同调、Hamilton 微分同胚、Hofer 几何、Gromov 宽度、扭量、
辛约化、接触几何、Kontsevich 形式性、K-理论、指数定理、Atiyah–Patodi–Singer、Dirac 算子、
Jones 多项式、Chern–Simons、纽结不变量、量子不变量、J-全纯曲线

**量子场论与规范理论 / QFT & Gauge Theory / 場の量子論**
超对称、超共形场论、N=(2,2) SCFT、N=4 超杨–米尔斯、瞬子、单极子、Seiberg–Witten 理论、
Seiberg 对偶、AGT 对应、共形场论、顶点算子代数、仿射 Kac–Moody、W-代数、可积系统、
Donaldson–Thomas 不变量、BPS 态、D-膜、AdS/CFT

**几何朗兰兹与电磁对偶 / Geometric Langlands & Electric–Magnetic Duality / 幾何学的ラングランズ**
几何朗兰兹纲领、Hecke 本征层、Hitchin 系统、Hitchin 纤维化、Beilinson–Drinfeld、Gaitsgory、
Frenkel 圈群、电磁对偶、S-对偶、Montonen–Olive 对偶、Kapustin–Witten 方程、Langlands 参数、
分歧（ramification）、驯顺分歧、正特征几何朗兰兹

**弦论 / String Theory / 弦理論**
拓扑弦、弦对偶、CY 三维流形、紧致化、镜像流形、Gopakumar–Vafa 不变量、BPS 计数、
I 型 / II 型弦、杂化弦、F-理论、M-理论

**学科与方法 / 术语**
译注本、术语对照、日汉对照、法汉对照、俄汉对照、原文页码锚点、公式逐符号核对、LaTeX 工程

**文献类型**
讲义（lecture notes）、综述（review）、博士论文（PhD thesis）、講究録（RIMS Kôkyûroku）、
Bourbaki 报告、Astérisque 专辑、arXiv 预印本、论文集（proceedings）

## 内容结构

| 目录 | 内容 |
|---|---|
| `00_README.md` | 资产说明、脱敏说明、使用许可 |
| `MANIFEST.json` | 全部文件的路径 / 字节数 / sha256 前 16 位（提交后重算，见「校验」） |
| `01_corpus_zh/` | **中文段落语料**（保真保留 LaTeX 公式）+ 术语基 `termbase.jsonl` + 去重报告 |
| `02_trajectories/` | AI 辅助工作的精选工具调用轨迹（意图→动作→证据→结论，含评分） |
| `03_translations_meta/` | 每部书的元数据、投稿信息、术语表；41 部预印本类的**成品 PDF** 已移到 Release `v1.0.1` 附件（清单见 `_PDF清单.tsv`） |
| `04_playbook/` | 翻译总纲、施工纪律（v2.0）、文献引进标准、待完成清单、环境备忘 |
| `05_seminar_witten/` | 威腾（Witten）文章研讨班的索引、阅读路线、经验教训 |
| `06_sessions_raw/` | 原始对话事件流（已脱敏、zstd 压缩）；145 MB 分片已移到 Release `v1.0.1` 附件，仓库只留抽取脚本与分片说明 |
| `papers/WIT-1989-JONES/` | **威腾 1989 CS/Jones 论文研讨班**（第二轮解经试点）：六场研讨记录、claims/questions 数据、教材核查；交付两版讲义——**49 页连续叙事讲义**（`deliverables/lecture/`，可作课程主文本）与 **97 页逐句注疏版**（`deliverables/reading_note/`），均含 LaTeX 源码、一键构建工程、协作流程记录，并有打包下载 `WIT-1989-JONES-v1.0.zip` |
| `08_source_code/` | **每部译本的完整工程**：`工程文件/`（BRIEF、构建脚本、交付清单、术语表、校对记录、逐章报告）+ `源码/`（LaTeX 源与插图） |
| `07_refs_nlab/` | **nLab 参考资料库**（几何 Langlands 线专用）：120 条 nLab 条目摘要（含 `last_revised`，可直接写进译注来源行）+ 37 份替代来源卡（nLab 只有存根时改引 A 级教材 / MathWorld / Stacks）+ 110 条来源真实性抽查记录 |
| `site/` | 静态站点（`site/index.html` 双击即开，无需服务器） |

## `01_corpus_zh/`：语料的形态

`zh_paragraphs.jsonl` 每行一段，字段：

| 字段 | 含义 |
|---|---|
| `pkg` / `file` / `para` | 所属工程、源文件、段序 |
| `para_id` | 内容哈希（sha1 前 16 位），全库唯一稳定标识，便于下游去重 / 增量更新 / 引用 |
| `page_orig` | 原书页码（解析 TeX 里的 `% ===== PDF p.NNN (原书 p.N) =====` 标记；仅 92 个工程带此标记） |
| `env` | 段落所在环境：`text` / `theorem` / `definition` / `proof` / `remark` / `example` |
| `tier` | 该工程的评级 A/B/C（来自工程元数据） |
| `text` | **保真文本**：行内/行间公式原样保留 `$...$`、`\begin{equation}...\end{equation}`，不再被洗成 ASCII 骨架 |
| `dup_of` / `dup_pkg` | 若与前面某段文本完全相同，指向首个出现位置；重复段**不删除**，便于按需过滤 |

去重统计与理由见 `01_corpus_zh/DEDUP_REPORT.md`；术语基 `termbase.jsonl` 字段为
`foreign / lang(en|ja|other) / zh / status / pkg / src_format`，SY02-09 的 215 行另有
`level`（A/B/I）/ `source`（依据）/ `lecture`（首次出现讲次）三字段，`status=confirmed`。

**术语定案表**：[`01_corpus_zh/terms_frozen_SY02-09.tsv`](01_corpus_zh/terms_frozen_SY02-09.tsv)（223 条，
列：英文 / 中文 / 等级 / 依据 / 首次出现 / 本轮校订备注）。这是《Langlands 纲领导论》逐页校订后的
冻结术语表——`B` 级条目都能在 `07_refs_nlab/pages/` 找到对应 nLab 页，`A` 级条目指向本讲参考文献的
具体章节。以后翻译几何 Langlands 的文献先查这张表，避免同词异译。

## `08_source_code/`：工程源码

- 放的是**翻译工程本身**：`工程文件/` + `源码/`（LaTeX + figures）。
- 装 TeX Live / MiKTeX 后进 `源码/` 跑 `xelatex main.tex` 即可重建中文译注本；
  少数工程的根文件叫 `main.tex` 之外的名称，见该工程 `工程文件/编译说明.md`。
- **14 部当初只留了成品 PDF、没有 LaTeX 工程**（`SY01-18 / 01-19 / 02-08 / 03-02 / 03-16 / 03-17 / 03-18 / 03-20 / 03-21 / 05-10 / 05-19 / 05-20 / 05-21 / 05-22`），
  这些目录只有 `投稿信息.md`；其余 **72 部**有完整可编译源码。
- **`工程文件/` 覆盖 81 部**（2026-11-14 从投稿包回填了 38 部缺失的 `工程文件/`，共 223 文件 / 2.8 MB）；
  其余 9 部（`SY01-18 / 01-19 / 02-08 / 03-16 / 03-18 / 03-20 / 05-20 / 05-21 / 05-22`）的原始投稿包本身就没有工程文档，只有 `源码/` 或仅成品。
- **自 2026-11-14 起，`03_translations_meta/<编号>/` 不再重复保存 `源码/` 与 `工程文件/`**：
  它们此前与 `08_source_code/<编号>_<中文名>/` 下的同名目录逐字节相同（约 45 MB 重复）。
  源码、工程文档与术语表统一以 `08_source_code/` 为唯一来源。
- 用途：学习、研究、复用翻译流水线。

## 成品 PDF 与原文（合规说明）

> 本库**不在仓库里保存任何成品 PDF，也不保存原文**。这一节说明去哪拿、为什么。

- **成品 PDF（中文译注本）只对 arXiv / 开放许可底本开放**：41 部以 arXiv 预印本（含 arXiv 托管的学位论文与讲义）为底本的译本，成品 PDF 在 Release [`v1.0.1`](https://atomgit.com/lzxSUSUY/mathtranslate/releases/tag/v1.0.1) 的附件，点开即下载；逐部清单（页数、字节、arXiv 号、文件名、下载直链）见 [`03_translations_meta/_PDF清单.tsv`](03_translations_meta/_PDF清单.tsv)。
- **其余 55 部的成品不公开**：在版图书、非 arXiv 讲义、学位论文等，成品 PDF 不发布、不给直链；确需研读可按 [`COMPLIANCE.md`](COMPLIANCE.md) §4 申请，逐部登记在 [`RELEASE_REGISTER.csv`](RELEASE_REGISTER.csv)。
- **原文不发布、不给直链**：本库只发布译文、工程源码、元数据与自建语料；原文（无论 arXiv 版还是出版书）请按书目信息自行从 arXiv、出版社或图书馆获取。
- **2026-11-16 已撤下**：SY02-09 随仓的袁瑶课程讲义原本、SY07-08 随仓的扶磊《代数几何》成品，以及另外 4 部误入仓的成品 PDF。撤下记录见 `CHANGELOG.md` 与 `RELEASE_REGISTER.csv`。
- **为什么这样**：① 图书译文的再分发权在出版社，公开全文会累积下架与封仓风险；② 成品 PDF 是二进制大文件，留在 Git 历史里会让每次 clone 都下载全部版本。移出后检出体积约 280 MB。

## 校验（`MANIFEST.json`）

- `MANIFEST.json` 记录每个文件的 **路径 / 字节数 / sha256 前 16 位**，在**提交后**按仓库内容重算（`.gitattributes` 已固定 `eol=lf`，因此清单位节数 = 仓库内 blob 字节数，不会因换行归一化而集体失配）。
- 自查：`python tools/check_manifest.py`（仓库自带）会重算并报告不一致项。
- 已知例外：`MANIFEST.json` 自身与 `_build_summary.json` 不计入清单（它们是生成物）。

## 分片还原

`06_sessions_raw/` 的 145 MB 会话分片已移到 Release `v1.0.1` 附件（Git 仓库不再保存）。
下载、拼接与 sha256 校验命令写在 [`06_sessions_raw/_分片说明.md`](06_sessions_raw/_分片说明.md)，机器可读元数据见同目录 `_attachments.json`。

## 脱敏

已发布文本资产统一过一遍脱敏（脚本 `tools/scrub_publish.py`）：

- 邮箱 → `[邮箱隐去]`
- Windows 本机绝对路径 / UNC 路径 → `<本地路径>`
- `ghp_ / github_pat_ / sk- / AKIA / ssh-ed25519` 等凭据与密钥模式 → `[已脱敏]`
- 真实密码、账号名等由 `package_upload.py` 在打包阶段剔除

`06_sessions_raw/` 的 zstd 分片（现为 Release 附件）是用同一套规则（含新增两类模式）重新脱敏后压缩的。

## 使用许可

**分两层**，完整条款见 [`LICENSE`](./LICENSE) 与 [`COMPLIANCE.md`](./COMPLIANCE.md)。

- **自产层 → CC BY 4.0**：元数据、术语库、标注、工作流轨迹、方法文档、工程文档、脚本、站点，署名即可，**欢迎训练、蒸馏、评测与商用**。
- **译文层 → 保留权利**：译文、译注、语料正文、译文源码是第三方作品的**演绎作品**，本库无权再许可；只允许**非商业学术研读**，不得整本转载、不得用于训练商业模型、不得出版发行；需要其他用途请先取得底本权利人授权。
- **成品 PDF**：不随译文以 CC BY 发布。arXiv / 开放许可底本的成品走 Release 外链；图书底本的成品不公开，按 `COMPLIANCE.md` §4 申请。
- **原文版权**归原作者与出版方，本库不发布原文、不授予原文权利。权利人要求撤下时 48 小时内移除。
- **历史口径**：2026-11-15 曾把全库统一为 CC BY 4.0 并声明欢迎训练/商用；该口径对译文层越权，已于 2026-11-16 由 `LICENSE` v1.1 取代，旧表述一律作废。

## 相关

- 站点：`site/index.html`
- 术语表：`08_source_code/*/工程文件/deliverable/术语表_*.csv`，汇总见 `01_corpus_zh/termbase.jsonl`
- 统计与一致性：`make_stats.py`（生成上面的统计块）、`tools/check_manifest.py`
