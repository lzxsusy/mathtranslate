# STYLE_GUIDE —— SY02-43 一般线性群的局部 Langlands 对应

本文件管**怎么翻译这份底本**：文体、术语、公式、注与框。与 `BRIEF.md` 冲突时以 BRIEF 为准；与 `04_playbook/01_数学文献翻译纪律.md` v2.1 冲突时以 playbook 为准。

## 1. 文体

- **直译优先，句子可以短**：底本是讲义口吻、句子短、常有省略号与括号补充。译文保持同样的断句节奏，不合并、不「润色成论文体」。
- **第一人称照译**：「we will show」「we remark」译「我们将证明」「我们指出」，不改写成「可以证明」。
- **作者自述保留**：「rough notes」「to be added in second draft」「To be completed in second draft」一律译出并加「（留存二稿补写）」，不用我们的论证替代。
- **人名与书目保留原文**：Bernstein、Zelevinsky、Henniart、Bushnell、Kutzko、Paskunas、Tate、Grothendieck 等不音译；书名/篇名保留原文，必要时在括号里给中文。
- **脚注上标复现**：底本用上标脚注，译本用 `\en{n}` 复现上标，条文集于文末「原注」，标注原页码与截断处。

## 2. 术语（冻结表见 `work/glossary.tsv`）

硬约定逐条：

| 英文 | 译文 | 备注 |
| --- | --- | --- |
| Weil–Deligne representation | Weil–Deligne 表示 | 保留连字符；不写「韦伊–德利涅」 |
| Weil group | Weil 群 $W_K$ | 不写「韦伊群」 |
| inertia group / wild inertia | 惯性群 $I_K$ / 野惯性群 $P_K$ | 与香蕉空间「惯性子群」一致；「子」字按底本省略 |
| tame character | 驯特征标 | `unramified` = 非分歧；`tame` = 驯；`wild` = 野 |
| admissible | 容许的（容许表示） | 香蕉空间无专条，沿本库 SY02-18/24/41 |
| smooth | 光滑的 | |
| supercuspidal | 超尖点（超尖点表示） | **不用**「超尖」；香蕉空间无专条，沿本库 SY02-24/41 |
| cuspidal | 尖点的（尖点表示） | 香蕉空间有「尖点表示」用例 |
| parabolic induction | 抛物诱导 | |
| Jacquet functor | Jacquet 函子 | |
| modulus character | 模特征标 $δ_P$ | |
| spherical Hecke algebra | 球面 Hecke 代数 | |
| Satake isomorphism | Satake 同构 | 不写「佐竹」 |
| unramified / ramified | 非分歧 / 分歧的 | |
| essentially square-integrable | 本质平方可积 | `essentially $L^r$` 照录为「本质 $L^r$」 |
| tempered | 缓增 | 不写「温和」 |
| generic | 一般的（一般表示） | **不用**「泛型」「通用」 |
| Whittaker model | Whittaker 模型 | |
| Zelevinsky segment | Zelevinsky 段 $Δ(π,m)$ | 不写「区间」 |
| linked / precedes | 相连 / 先于 | 底本原词 linked、precedes，译文照意 |
| Bernstein component / center | Bernstein 分量 / Bernstein 中心 | `block` 在 BZ 语境译「块」 |
| inertial equivalence | 惯性等价 | |
| type / $K$-type / minimal $K$-type | 类型 / $K$-型 / 极小 $K$-型 | 底本明说与 Bushnell–Kutzko 的 type 不同 |
| conductor | 导子 $c(π)$ | Artin conductor 译「Artin 导子」 |
| depth | 深度 | |
| local Langlands correspondence (LLC) | 局部 Langlands 对应 | 香蕉空间有实际用例 |
| $\varphi$-semisimple | $\varphi$-半单（Frobenius 半单） | 首次出现给出全称 |
| contragredient | 反变对偶 | |

## 3. 公式与记号

- **公式不改实质**：底本公式一律照录；只做排版层面的拆分（超宽公式改 `multline*`/`psmallmatrix`），不改符号。
- **`\mathrm` 函数名**：$\Hom,\End,\Ind,\ind,\Res,\tr,\rk,\diag,\Spec,\Frob,\Art,\Gal,\ad,\St,\triv,\vol,\rec$ 一律直立。
- **$\Sp_m$ 与 $\St_m$**：$\Sp_m$ 是 $W_K\times\SL_2$ 的 Steinberg 表示（Galois–Deligne 侧），$\St_m$ 是 $\GL_m$ 的 Steinberg 表示（自守侧），两者不可混写；底本用 `Sp` 与 `St` 区分，译文照此。
- **记号冲突**：底本 §4 用 $K$ 兼指局部域与 $\GL_n(\mathcal O_K)$，译文后者改记 $\mathcal K$，并在首现处说明。
- **不编号公式**：底本无公式编号，译本亦不编号；引用一律写「（见 p.n）」。
- **底本笔误**：只进橙框译注，正文公式**不改**。已知 4 条见 `资料卡/04-术语文献勘误.md`。

## 4. 注与框

- **橙框 `yizhu`（译注）**：只放四类内容——(1) 底本笔误或记号冲突；(2) 底本跳步大到影响阅读（给出「可以怎么补」，不替作者写完整证明）；(3) 术语选词的取舍理由（尤其与香蕉空间不一致处）；(4) 底本与通行文献的差异（如 p.25 支撑条件 $j=1,\dots,m_i-1$ 应为 $j=0,\dots$）。全篇共 5 条。
- **蓝框 `keytakeaways`（本节重点）**：每节末 3–5 条，写「这节做了什么」「哪一步是枢纽」「哪里容易读错」，是导读而非摘要。全篇 5 个（§1、§2.3、§3、§4、§5）。
- **「底本此处未写」**：底本留白处一律用居中斜体 `底本此处未写`（作者原注：…），不代拟。
- **框不嵌套**：译注与本节重点不互相嵌套；框内不放大段公式（超过两行的公式移到框外）。

## 5. 排版

- 版式：`\documentclass[11pt,a4paper]{article}` + `geometry` 2.6cm + `ctex(fontset=windows)`。
- 定理环境：`theorem/lemma/corollary/proposition` 共用 `nbthm` 计数器，按节重排；`definition/example/remark` 星号版不编号；`proof` 中文名「证明」。
- 编译：`xelatex` 三遍（有目录与交叉引用），要求 `grep -c "^!" main.log` 为 0、无 overfull。
- 交付：成品 PDF 放 `成品/`，文件名 `SY02-43_一般线性群局部Langlands对应讲义_中译注本.pdf`。

## 6. 不做什么

- 不改底本的结构（不合并小节、不补 §3.4 与 §5–§6 的正文）。
- 不引入底本没有的定理或证明。
- 不在正文里加译者观点；所有判断进译注或资料卡。
- 不把术语表里的「未定」词直接写进正文。
