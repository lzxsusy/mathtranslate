# TIMELINE —— 边界裁决与工程事实（Lead 维护）

底本无页码，故边界以**源块号**裁定。裁决生效后 Lead 已同时通知上下游两人。

## 1. 分块边界裁决（2026-11-04，Lead）

| 边界 | 上游末块（含） | 下游首块（含） | 理由 | 已通知 |
|---|---|---|---|---|
| tr01a / tr01b | B023（段末 `Let $p\in\check X$…`） | B024（`**Lemma.** $\Hom^\ast(\cO_p,\cO_p)$…`） | 不把引理与证明拆开 | tr-01（单人口，本文件即通知） |
| tr01b / tr02a | B037（第 1 章末段） | B038（第 2 章开篇） | 章边界 | tr-01, tr-02 |
| tr02a / tr02b | B085（`**Corollary.** …integral affine structure.` 完整推论） | B086（小节 `Equivalences.`） | 小节边界，环境完整 | tr-02（单人口） |
| tr02b / tr03a | B104（第 2 章末段） | B105（第 3 章开篇） | 章边界 | tr-02, tr-03 |
| tr03a / tr03b | B115（`**Definition/Proposition(Batyrev).**` 完整环境） | B116（小节 `Homological Mirror Symmetry.`） | 小节边界 | tr-03（单人口） |
| tr03b / tr04a | B131（小节末段） | B132（小节 `SYZ mirror construction for toric Fano varieties.`） | 小节边界 | tr-03, tr-04 |
| tr04a / tr04b | B139（段末 `In particular, the numbers $\mu_i$…`） | B140（`**Lemma.** The summation…`） | 不拆引理 | tr-04（单人口） |
| tr04b / tr05a | B154（第 3 章末段） | B155（第 4 章开篇） | 章边界 | tr-04, tr-05 |
| tr05a / tr05b | B174（`**Theorem[[Sym03]].**…` 完整定理） | B175（小节 `Monodromy.`） | 小节边界 | tr-05（单人口） |
| tr05b / tr06a | B188（表 3，第 4 章末） | B189（第 5 章开篇） | 章边界 | tr-05, tr-06 |
| tr06a / c-refs | B214（第 5 章末段） | 参考文献（脚本生成） | 章边界 | tr-06 |

**规则**：跨块句子「开始者写完」；环境不许跨文件；上游末块若为 `env`，写成完整环境。

## 2. 工程事实（实测，2026-11-04）

| 项 | 值 |
|---|---|
| 底本 | `https://diewildkatze.com/SYZ.html`，HTML 106,386 B，抓取于 2026-11-04 |
| 章节 | 6 章正文（Overview 无章号；Introduction…Toric Varieties, Continued = 第 1–5 章）+ References |
| 源块 | 246（`work/source/blockmap.tsv`） |
| 独立公式 | 38（全部无编号；**`\tag` 数为 0**） |
| 定理类环境 | 62（Definition/Theorem/Lemma/Proposition/Corollary/Remark/Example/Exercise/Statement） |
| 证明 | 12；表格 3；交换图 3；插图 0 |
| 参考文献 | 32 条（英文原貌转录） |
| 编译 | LuaLaTeX ×3，镜像目录 `default-workspace\syzbuild`（ASCII 可写），0 error 为验收线 |

## 3. 术语裁决（跨块漂移风险点）

- `toric variety` = 环簇；`toric manifold` = 环簇流形；`toric` 形容词按语境（环面的/环簇的）。
- `fan` = 扇（不译「扇形」）；`cone` = 锥；`ray` = 射线；`primitive collection` = 原语集。
- `monodromy` = 单值化（不译「单值性」）；`wall-crossing` = 墙穿越。
- `focus-focus` = 焦点-焦点（连字符保留，不译「聚焦」）。
- `one-pinched torus` = 单收缩环面；`almost toric` = 近环面。
- `bounding cochain` = 约束上链；`unobstructed` = 无障碍的。
- `matrix factorization` = 矩阵分解；`skyscraper sheaf` = 摩天楼层。
- 人名/缩写保留：SYZ、HMS、FKTZ（Fang–Liu–Treumann–Zaslow）、HMF、AGT、Morse–Bott、Floer、Fukaya、Maslov。
