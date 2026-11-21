# BRIEF · SY05-29 朗兰兹对偶 Hitchin 系统的增强镜像对称

## 一、任务

把 Tamás Hausel 的 ICM 2022 报告 *Enhanced mirror symmetry for Langlands dual Hitchin systems*（Proc. ICM 2022, Vol. 3, pp. 2228–2249，CC BY 4.0）译成中文，按《数学文献翻译纪律》v2.1 出 PDF，并配套一套可检索、可自测的资料卡。

## 二、为什么做这一篇

- 它是几何 Langlands 纲领在 Hitchin 系统上的"增强"版本：不只说两边的导出范畴等价，还要求 Wilson 算子与 Hecke 算子一起交换。这个问题在 2022 年是一个小综述，适合作为"从综述进入研究"的样板。
- 后半（§3）是作者尚未在他处完整发表的结果：在幂零锥上把镜像对称变成可以显式计算的**重数代数**，并把 Grassmannian / 仿射 Grassmannian 的上同调环卷进来。这一段最适合做成资料卡。
- 底本有 LaTeX 源码（arXiv:2112.09455v2），公式可逐字核对；又有正式印本（EMS，CC BY 4.0），页码、定理编号可双向对表。

## 三、交付物

| 交付物 | 位置 |
| --- | --- |
| 中译注本 PDF（28 页） | `成品/SY05-29_朗兰兹对偶Hitchin系统的增强镜像对称_中译注本.pdf` |
| 源码（1427 行） | `源码/`（`main.tex`、`preamble.tex`、`ch0_front.tex`、`ch1_intro.tex`、`ch2_background.tex`、`ch3_enhanced.tex`、`refs.tex`、`app_terms.tex`、`original/`） |
| 通读笔记 | `工程文件/reports/01_通读笔记.md` |
| 疑点清单（24 行） | `工程文件/reports/02_疑点清单.tsv` |
| 术语表（112 行） | `工程文件/reports/03_术语表.md`、PDF 附录 A |
| 交付核对 | `工程文件/reports/04_交付核对.md` |
| 资料卡（29 张） | `datasets/hausel22/` |

## 四、验收标准

1. 编译 0 error、0 Overfull、0 未定义引用、0 缺字。
2. 定理编号 3.1–3.20、公式编号 (1.1)(2.1)–(2.5)(3.1)–(3.14) 与印本逐条一致。
3. 印刷页 2228–2249 与译本页码的对照表可查（`ch0_front.tex` 的 longtable）。
4. 每条译注有来源或明确标"无外部依据"。
5. 原文笔误不擅改，加译注并登记进《疑点清单》（`未解` 须为 0）。
6. 资料卡 `lint_cards.py --strict` 0 error，`related` 全部可解析。

## 五、已知边界

- 原文 §3.4 的猜想 3.12、3.19 都是猜想，译本与资料卡都不写成"已证"。
- 原文式 (3.9)(3.10)(3.11) 的角标疑有笔误（$2\omega_1,2\omega_1,3\omega_1$ 与 $\mu=(d+1)\omega_k$ 不符），照录原文并加译注，资料卡按应有值表述并注明。
- 定理 3.10 的证明归给 [HH]，本文只有结论；资料卡把关键的"乘积分解无额外分量"标为 B 级并写进 `gaps`。
