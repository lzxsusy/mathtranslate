# BRIEF · SY01-30《三维镜像对称》中译注本

## 1. 书目信息

| 项 | 内容 |
|---|---|
| 原文标题 | 3-dimensional mirror symmetry |
| 作者 | Ben Webster（University of Waterloo / Perimeter Institute）、Philsang Yoo（Seoul National University） |
| 出处 | Notices of the AMS（本译本据 arXiv 版） |
| 底本 | arXiv:2308.06191v1 [math.RT]，2023-08-11，23 页（第 1 页标题页，第 2 页为原文 `\listoffixmes` 批注页，正文自第 3 页起） |
| 底本 LaTeX 源 | arXiv e-print 包内 `Webster-Yoo.tex`（911 行）+ `Webster-Yoo.bbl`（30 条文献，biblatex bbl format 3.2） |
| 文献表 | 原包不带 `.bib`，且 3.2 格式的 bbl 与 2026 年的 biblatex（3.3）不兼容（实测：空文献表 + `wrong format version` 警告）。故由 bbl 反推 `源码/main.bib`（30 条，脚本 `work/sy0130/bbl2bib.py`），改用 biber；`.bbl` 不入库（.gitignore） |
| 语言 | 英 → 中（简体） |
| 体例 | 中文译注本：译文 + 译注框 + 术语表；保留原文全部公式、定理编号与插图 |
| 编译 | `xelatex main.tex` → `biber main` → `xelatex main.tex` ×2（ctex + fandol；2026-11-22 实测 30 页（印刷页 29）、0 error、0 overfull） |
| 成品 | `工程文件/deliverable/Webster-Yoo_三维镜像对称_中文译注本.pdf` |
| 工程编号 | SY01-30（镜像对称组，接 SY01-29 之后） |

## 2. 文章结构与页码（PDF 页，据原编译版实测）

| 节 | 原文标题（照录） | 页 |
|---|---|---|
| — | 标题、作者、摘要 | 1 |
| — | 原文 `\listoffixmes` 批注页（原稿遗留，见译注） | 2 |
| §1 | Introduction（1.1 The House of Symplectic Singularities；1.2 Plan of the paper） | 3–6 |
| — | Acknowledgements | 6 |
| §2 | Physical Origin（2.1 QFT；2.2 TQFT；2.3 From QFT to TQFT） | 7–11 |
| §2.4 | Mirror Symmetry | 11–12 |
| §2.5 | Future Direction（**原文未印出**：整节包在 `\maybelater` 里） | — |
| §3 | Higgs and Coulomb branches（3.1 Higgs branches） | 12–15 |
| §3.2 | Coulomb branches | 15–19 |
| §4 | Advanced directions（4.1 Stable envelopes；4.2 Koszul duality of category O's；4.3 Line operators；4.4 Connections to 4d field theory and the Langlands program；4.5 Betti 3d mirror symmetry） | 19–22 |
| §5 | Future directions（**原文未印出**：整节包在 `\maybelater` 里，且 `enumerate` 首项为空） | — |
| — | References | 23 |

> 原文第 2 页的 `\listoffixmes` 是作者用 `fixme` 包留下的 8 条写作批注（其中数条已过时）。**本译本不排印这一页**，只在「译者说明」里交代；其余页序与原 PDF 一致。
>
> **两处「未印出的原文」**：原文把 2.5 节与第 5 节整段包在 `\newcommand{\maybelater}[1]{}` 里——宏体为空，所以这两节**在原文 PDF 里根本不出现**（与原文 23 页、译本 30 页的实测一致）。译本按「照原文印出的内容译」处理：不译入正文，把两节的起止与主旨登记在 `资料卡/04-术语文献勘误.md`，需要时可回头补。

## 3. 翻译决定（立项时定下，不再改动）

1. **标题**：`3-dimensional mirror symmetry` →「三维镜像对称」。原文用 `3-dimensional`/`3d` 两种写法，中文统一「三维」。
2. **核心术语**（详见 `工程文件/work/glossary.tsv`）：
   - symplectic resolution / singularity → **辛消解 / 辛奇点**（不用「辛解消」「辛奇异性」）
   - Higgs branch / Coulomb branch → **希格斯分支 / 库仑分支**
   - symplectic duality → **辛对偶**；3-dimensional mirror symmetry → **三维镜像对称**
   - topological twist → **拓扑扭转**；TQFT → **拓扑量子场论**
   - hypertoric variety → **超环面簇**；quiver variety → **箭图簇**；BFN space → **BFN 空间**
   - stable envelope → **稳定包络**；category O → **范畴 O**；Koszul dual → **Koszul 对偶**
   - line operator → **线算子**；chiral algebra → **手征代数**
3. **人名不译**：Springer、Koszul、Slodowy、Nakajima、Hilbert、Fukaya、Langlands、Betti、de Rham、Kähler、Hitchin、Verma、Weyl、Dynkin、Cartan、Jordan 等。
4. **保留原文比喻**：dark mansion / secret passage / treasure hunt / x-ray specs / bon mot 全部照译，这是本文的文体特征，不「学术化」掉。
5. **不译第 2 页 fixme 页**：那是 2023 年投稿时的内部批注（如「add a reference to …」），不是正文；在译注中说明即可。
6. **编号照抄**：原文定理/定义/例每节内共享一个计数器（问题 1.1、例 2.1、定义 3.1 … 猜想 4.1），译本用同样的 `[section]` 计数，逐条对应，方便与原文对读（实测两版编号完全一致）。
7. **只译原文印出的内容**：`\maybelater{...}`（宏体为空）与 `\phil{...}`/`\ben{...}`（作者内部批注）都不进正文；前者在 04 号资料卡登记，后者不译。
8. **补回原文漏编的一条文献**：`\cite{dimofteMirrorSymmetry2020}` 在随文 `.bbl` 中缺失（作者生成文献表时漏编）。译文不伪造条目，改为在正文写明 Dimofte–Garner–Geracie–Hilburn《Mirror symmetry and line operators》(arXiv:1908.00013) 并加行内译者注。

## 4. 与仓库其他部分的关系

- **资料卡**：`资料卡/` 五件套（00 速览、01 结果清单、02 论证地图、03 条款索引、04 术语文献勘误）。
- **对齐卡（L2 陈述层）**：本文是**综述**，定理陈述少、定义与物理动机多；首批对齐卡只抽 3 条——定义 3.1（辛消解）、定理 3.7（希格斯/库仑分支的同构）、猜想 4.1（辛对偶的范畴化），其余登记为 gap G4（陈述歧义）。
- **术语表**：`工程文件/work/glossary.tsv` 的条目在完工后并入 `01_corpus_zh/termbase.jsonl`（`pkg=SY01-30`）。
- **数语规范**：服从 `01_corpus_zh/数语规范/STYLE_NL.md`；新术语一律登记，不改已冻结表。

## 5. 工程状态

- [x] 立项、取底本（arXiv e-print 源；bbl→main.bib 重建，biber 可跑）
- [x] BRIEF / STYLE_GUIDE / glossary（165 条）
- [x] 六块译文（ch01–ch06，六个子任务分译后统稿）
- [x] 合并编译（30 页 = 扉页 + 印刷页 29；0 error、0 overfull、0 未定义引用）
- [x] 术语复查（术语表 165 条；正文术语按表）、译注复查（11 条）
- [ ] 资料卡五件套（00/01/02/03/04）
- [ ] 成品 PDF 入 `工程文件/deliverable/`
- [ ] 入库登记（RELEASE_REGISTER 行、03_translations_meta 条目、datasets 索引）
- [ ] 对齐卡首批 3 条（定义 3.1 / 定理 3.7 / 猜想 4.1）

## 6. 许可与来源

原文版权归作者与 AMS；arXiv 版按 arXiv 许可发布（见 https://arxiv.org/abs/2308.06191 的 license 行）。本译本是**研究用中文译注本**，不代原作者授权、不另设限制；权利人通知即撤。自产的术语表、资料卡、工程文档按仓库 `COMPLIANCE.md` 与 `LICENSE` 处理。
