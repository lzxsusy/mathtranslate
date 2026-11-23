# 《迹公式与函子性——一个纲领的开端》中译注本

> 底本：Edward Frenkel、Robert Langlands、Ngô Bao Châu,
> *Formule des traces et fonctorialité : le début d'un programme*,
> arXiv:1003.4578v2 [math.RT]，2010-09-29，**法文 54 页**
> （导引 p.1–3；§1 p.3–12；§2 p.12–17；§3 p.17–38；§4 p.38–46；§5 p.46–52；文献 p.53–54）。
> 发布编号：**SY02-32**（`RELEASE_REGISTER.csv` 原至 SY02-31）。

## 这是什么

这是一篇**纲领性文章**，而不是一篇定稿的证明。三位作者——Frenkel、Langlands（1978 年 Fields 奖得主，函子性纲领的提出者）、Ngô Bao Châu（2010 年 Fields 奖得主，基本引理的证明者）——合写不到 54 页，交代一件事：

> 既然 Ngô 已经证出基本引理，稳定迹公式就不再是空话；那么能否**顺着 $L$ 函数的极点**——而不是沿着 Arthur 分类**自上而下**——把函子性「自下而上」搭起来？

文章的核心设想是：对自守表示 $\pi$，$L(s,\pi,\rho)$ 在临界线上的极点位置与阶，由某个更小的群 $H$ 的 Ramanujan 型表示决定；把这套对应逐层递归，就能既得到函子性，又得到 Ramanujan 猜想。为了把这件事变成可算的等式，作者做了三件事：

1. **§1** 用 $L$ 函数本身（而不只是它的对数导数）重写 Langlands 的 *Beyond endoscopy*（[L3]），把「极点的阶」换成迹公式里可以分离的项；
2. **§2** 在函数域情形把欧拉积展开成**几何和**：$\Bun_G$ 上的 Hecke 叠、几何 Satake、Grothendieck–Lefschetz 给出 $K_{\rho,d}$ 的同构（引理 2.6），这是全文唯一「已经严格算出来」的几何引理；
3. **§3–§5** 把稳定迹公式的椭圆正则项写成对 **Steinberg–Hitchin 基** $\mathbb A$ 的积分，再对 $\mathbb A$ 作**阿代尔化**（截断 + Poisson 求和），最后验证首项 $\hat\theta(0)$ 恰是主项，等于 $\int_{G(\mathbb A)}f$。

**这篇文章的价值不在结论，而在路线图。** 文中自认的缺口（Poisson 和的收敛、二重极限的次序、命题 3.29 只在 $\mathbb C$ 上证明）后来由 [FN]（arXiv:1004.5323）与 [L5] 继续；读这篇文章，是读一条**二十一世纪函子性纲领的施工图**。

## 目录

| 路径 | 内容 |
|---|---|
| `源码/` | LaTeX 源：`main.tex`、`preamble.tex`、`sections/s00`–`s99`、`build.bat` |
| `工程文件/BRIEF.md` | 施工手册（页映射、文件所有权、质量门） |
| `工程文件/SPEC.md` | 体例规范（章节文件、环境、页锚、编号对齐、译注格式） |
| `工程文件/work/通读笔记.md` | 三句话主旨、按节论证地图、体裁清单、阅读顺序 |
| `工程文件/work/疑点清单.tsv` | 15 行疑点（全部已解），八列：位置/原文/类型/猜测/查证动作/结论/依据/状态 |
| `工程文件/work/glossary.tsv` | 137 条术语冻结表（原文/中译/依据 A·B·I/首见页） |
| `工程文件/work/src/pNNN.txt` | 逐页法语原文（供引文核对；底本 PDF 不入仓） |
| `工程文件/reports/` | 分章报告与四路审校报告（`review-a`…`review-d`） |
| `资料卡/` | 00–04 叙述五件套 + `cards/` 31 张 JSON 卡（24 概念 + 7 推导） |
| `datasets/sy02-32/` | 卡片副本 + `SCHEMA.md` + `SOURCE.md` + 质检工具 |
| `成品/` | 全本 PDF（arXiv 底本，可随仓公开） |

## 体例

- **页锚**：每页开头 `\srcpage{N}`（$N$ = 原书页 = PDF 页），页界落在句中时用 `\srcpageinl{N}`；边注显示 `p.N`。
- **编号**：公式沿用原文 `(1.1)`–`(5.13)`（72 处）；引理/命题用原文编号（Lemme 2.6、3.26，Prop 3.29，Lemme 4.1、4.2、5.4、5.8、5.10、5.13，Prop 5.6）。
- **译注**：`\yizhu{内容}{来源}` 排楷体脚注并附 `[来源：…]`；无外部依据的推断用 `\yizhuw`。共 12 条，只写三类（易错预警、含糊点拨、背景直觉）。
- **笔误**：一律照录，出注说明，登记进 `疑点清单.tsv` 与 `资料卡/04-术语文献勘误.md`（E1–E9），不静默改动。
- **术语**：先冻结再译（内窥、内形式、$L$-包、拟分裂、$z$-扩张、Steinberg–Hitchin 基、阿代尔化、极赋值集……），无通行译名者保留原文。

## 进度

| 阶段 | 内容 | 状态 |
|---|---|---|
| Phase 0 | 通读笔记 + 137 条术语冻结 + 疑点清单 15 行 | ✅ |
| Phase 1 | 导引与 §1–§5 全译（54 页逐页对照），文献 42 条原样保留 | ✅ |
| Phase 2 | 整书统稿：页锚 54/54、编号 72/72、术语三同步、编译 0 error | ✅ |
| Phase 3 | 四路分章审校（rev-a…rev-d），高/中问题修复 | ✅ |
| Phase 4 | 资料卡 31 张 + 叙述五件套 + `datasets/sy02-32` 入库 | ✅ |
| Phase 5 | 登记 `RELEASE_REGISTER.csv`、统计、manifest、发布 | 见交付记录 |

## 怎么编译

```bat
cd 源码
build.bat                 :: 整书两遍（有索引时 xelatex → makeindex → xelatex ×2）
build.bat check sections\s05-sec3b.tex c   :: 单章自检，产出 _check_c.pdf
```

单章自检时编号显示为 `1.x`；并入 `main.tex` 后由 `\setcounter{theorem}{…}` 恢复为原文编号。

## 质量记录

| 门 | 结果 |
|---|---|
| 整书编译 | `main.pdf` **39 页**，0 error，0 Overfull，0 undefined，0 缺字 |
| 页锚 | `main.pagemarks` 54 条、覆盖 p.1–p.54 全部，无缺页 |
| 编号 | 公式 72 处、编号断言 10 条，与原文逐条对齐；`\tag` 手工编号 |
| 译注 | 14 条，全部带 `[依据：原书 p.N]` 或 A/B/I 来源标记 |
| 语言 | 「被……所」「进行……的」「对于……而言」0 处；长句已按 70 字上限拆分 |
| 资料卡 | 31 张（概念 24 / 推导 7），`lint_cards.py` 0 错误；31 条 quote 全部逐字命中 |
| 入库 | `datasets/sy02-32/cards` → `kb/cards/sy32.jsonl` 31 条，`kb/build_kb.py` 重建通过 |

## 纪律

一切按 `工程文件/SPEC.md` 与 `工程文件/BRIEF.md` 执行；母本是 `04_playbook/01_数学文献翻译纪律.md` v2.1：
先通读后落笔、译注必须带来源、来源白名单 nLab/Stacks/ProofWiki、黑名单知乎等。
底本 PDF 不入仓，只保留逐页文本与页面图（本地）。

## 引用

```
Frenkel, E., Langlands, R. P., Ngô, B. C. Formule des traces et fonctorialité :
le début d'un programme. arXiv:1003.4578v2 [math.RT], 2010.
中译注本：数译 SY02-32（2026）。
```
