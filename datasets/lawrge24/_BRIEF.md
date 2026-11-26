# lawrge24 施工简报（给并行写卡 agent）

## 0. 你在做什么

把 LAWRGE 2024 研讨会笔记 *Relative Langlands Duality*（73 页，15 讲）拆成中文资料卡。原文是 Ben-Zvi / Sakellaridis / Venkatesh 的参会者笔记，**大量结论只有陈述、没有证明**；卡片的价值是把「说什么、哪步是证明、哪步是期望」讲清楚，不是复述译文。

已存在的资产（先读，省得重新推导）：

- 工程级五件套：`08_source_code/SY02-15_相对朗兰兹对偶/资料卡/00-速览.md`、`01-结果清单.md`、`02-论证地图.md`、`03-条款索引.md`、`04-术语文献勘误.md`
- 原文分页文本：`08_source_code/SY02-15_相对朗兰兹对偶/工程文件/work/原文/chNN.txt`（`===== PDF PAGE N =====` 是**页末**标记，页 N 的正文在该标记之前）
- 中译源码：`08_source_code/SY02-15_相对朗兰兹对偶/源码/chunks/chNN.tex`（可对照术语，但**不要整段抄**）
- 术语表：`08_source_code/SY02-15_相对朗兰兹对偶/工程文件/work/glossary.tsv`
- 卡片规范：`datasets/lawrge24/SCHEMA.md`（必读）

## 1. 你要交付什么

只写分配给你的 `datasets/lawrge24/cards/concepts/<slug>.json` 与 `.../derivations/<slug>.json`。**不要**改 README、index、其他卡、统计文件。一卡一文件，UTF-8，2 空格缩进，字段按 SCHEMA。

写完后在仓库根目录跑：

```bash
python datasets/lawrge24/tools/lint_cards.py
```

你只负责让自己那几张卡 0 error；别的 agent 的卡可能暂时缺，`related` 指向未写的 id 时 lint 会报错——这是正常的，**不要**为了让 lint 通过而删掉 related，也不要改别人的卡。最终由 lead 统一收口。

## 2. 卡片主清单（id 固定，不得改名）

页码 = **原文 PDF 页**（1–73）。`§N` 对应 `chNN.txt`。

| id | track | 建议标题 | 节/页 |
|---|---|---|---|
| `lawrge/concept/relative-langlands-duality` | O | 相对朗兰兹对偶：主陈述 | §3 p.12–15；§13 p.60 |
| `lawrge/concept/a-and-b-theories` | O | 自守侧 $A_G$ 与谱侧 $B_{\check G}$ | §2 p.9–11；§7 p.31–33 |
| `lawrge/concept/proof-map` | O | 全书证明地图：从 TQFT 到 $L$-层 | 全书；p.12、p.63 |
| `lawrge/concept/tqft-axioms` | A | 拓扑量子场论的两条公理 | §1 p.4–6 |
| `lawrge/concept/bordism-category` | A | 配边范畴 $\mathsf{Bord}^n$ | §1 p.5–7 |
| `lawrge/concept/lagrangian-tqft` | A | 拉格朗日 TQFT 与场空间 | §1 p.6–8 |
| `lawrge/concept/arithmetic-topological-dictionary` | A | 算术–拓扑字典 | §2 p.9–11 |
| `lawrge/concept/langlands-as-4d-tqft` | A | Langlands 作为四维 TQFT | §2 p.10–11 |
| `lawrge/concept/boundary-conditions` | A | 边界条件作为理论的对象 | §3 p.12–14 |
| `lawrge/concept/raviolo-hecke` | B | raviolo 与 Hecke 算子 | §4 p.19–21；§7 p.31–33 |
| `lawrge/concept/hecke-category` | B | Hecke 范畴 $A_G(R)$ | §7 p.31–33 |
| `lawrge/concept/affine-grassmannian` | B | 仿射 Grassmann 流形 $\mathrm{Gr}$ | §7 p.34–35 |
| `lawrge/concept/geometric-satake` | B | 几何 Satake 等价 | §7 p.30–33 |
| `lawrge/concept/derived-satake` | B | 导出 Satake | §7 p.33–34 |
| `lawrge/concept/spectral-action` | B | 谱作用定理 | §7 p.34–35 |
| `lawrge/concept/koszul-duality` | B | Koszul 对偶与余伴随 | §7 p.33 |
| `lawrge/concept/e3-structure` | B | $E_3$ 结构与分歧点 | §7 p.29–31 |
| `lawrge/concept/spherical-variety` | C | 球簇 | §8 p.34–38 |
| `lawrge/concept/multiplicity-free` | C | 多重数自由定理 | §8 p.37–38 |
| `lawrge/concept/rank-one-freeness` | C | 秩 1 自由 | §8 p.36–37 |
| `lawrge/concept/dual-group` | C | 对偶群 $\check G$ | §8 p.37；§10 p.45–46 |
| `lawrge/concept/relative-cartan` | C | 相对 Cartan 子群 $A_X$ | §8 p.37 |
| `lawrge/concept/little-weyl-group` | C | 小 Weyl 群 $W_X$ | §10 p.44–46 |
| `lawrge/concept/hyperspherical-variety` | C | 超球簇 | §10 p.46–47 |
| `lawrge/concept/hyperspherical-structure` | C | 超球簇的结构定理 | §10 p.47 |
| `lawrge/concept/plancherel-density` | D | Plancherel 密度 | §8 p.34–36 |
| `lawrge/concept/local-plancherel` | D | 局部 Plancherel 公式 | §11 p.48–49 |
| `lawrge/concept/local-conjecture` | D | 局部范畴化猜想及其修正 | §11 p.49–50 |
| `lawrge/concept/shearing` | D | shearing 修正 | §11 p.50 |
| `lawrge/concept/trace-formula-hom` | D | 内积作为 Hom 上的迹 | §11 p.48–49 |
| `lawrge/concept/period-sheaf` | E | 周期层 $\mathcal P_X$ | §13 p.60–61 |
| `lawrge/concept/l-sheaf` | E | $L$-层 $L_{\check X}$ | §13 p.61–62 |
| `lawrge/concept/global-conjecture` | E | 整体几何猜想 | §13 p.62–63 |
| `lawrge/concept/beilinson-projection` | E | Beilinson 投影 | §13 p.62–63 |
| `lawrge/concept/l-function` | E | $L$-函数作为配对 | §12 p.56–58；§15 p.63 |
| `lawrge/concept/fixed-points` | E | 导出不动点与 $L$-层纤维 | §15 p.64–65 |
| `lawrge/concept/tate-example` | E | Tate 例：$\zeta$ 作为周期 | §5 p.22–25 |
| `lawrge/concept/eisenstein-example` | E | Eisenstein 级数与常项 | §14 p.66–67 |
| `lawrge/concept/whittaker-sheaf` | E | Whittaker 层 | §14 p.67–68 |
| `lawrge/concept/hitchin-gaiotto` | E | Hitchin 截面与 Gaiotto 拉格朗日 | §14 p.68–69 |
| `lawrge/concept/miraculous-duality` | E | 奇迹对偶 | §14 p.66–68 |
| `lawrge/deriv/tqft-1d-assignment` | A | 一维 TQFT 的赋值 | §1 p.4–5 |
| `lawrge/deriv/zeta-unfolding` | E | $\zeta$ 的 unfolding | §5 p.22–24 |
| `lawrge/deriv/rank-one-freeness-derivation` | C | 秩 1 自由：从因子化到生成元 | §8 p.36–37 |
| `lawrge/deriv/dual-group-assembly` | C | 组装 $\check G_X$：$A_X$、$W_X$ 与 $\mathfrak{sl}_2$ | §10 p.45–46 |
| `lawrge/deriv/inner-product-trace` | D | 从 Plancherel 内积到 Hom 上的迹 | §11 p.48–49 |
| `lawrge/deriv/l-sheaf-fiber` | E | $L$-层纤维 = 导出不动点 | §15 p.64–65 |

`related` 只能从这张表里选；至少 2 条，不能指向自己。

## 3. 引文怎么取（最容易翻车）

1. 打开 `工程文件/work/原文/chNN.txt`，找 `===== PDF PAGE N+1 =====` 之前那一段 = 页 N。
2. 复制**一句连续的英文**（12–120 字符，ASCII，不含中文），不要跨行拼接、不要改标点。
3. `pages` 写 `[N, N]`，`pdf_pages` 同，`anchor` 写 `A p.N`。
4. 每个 `sources` 条目都必须是**该页原文真实存在的字符串**；lint 会用页文本逐字核对，多一个空格都算错（lint 会规范化连续空白）。

示例（§3 p.12）：

```json
"quote": "This third talk will be about relative Langlands as TQFTs."
```

示例（§13 p.60）：

```json
"quote": "the period sheaf should match the L-sheaf."
```

## 4. 写法

- **中文重写**，不是翻译。定义、机制、为什么重要；公式保留 LaTeX（`$...$`）。
- 一张概念卡 400–800 字为佳；`key_points` 3–5 条，每条一句完整判断；`pitfalls` 2–3 条，写**具体的误读**（例：「把 $\check G_X$ 当成 $\check G$ 的闭子群——原文的 $A_X$ 一般不是单射」）。
- 原文只给陈述的，`proof.status` 写 `sketch` 或 `gap`，`gap_note` 说清「原文只说『见 BZSV §4』/未给证明」。
- 编号要引原文编号：定理 7.4、定理 7.8、定理 7.10、定理 8.19、定理 10.22、猜想 13.17/13.21、(11.4)–(11.11)、(13.29)–(13.35) 等，写在 `theorems[].name` 或正文里。
- 不写「本文」「笔者认为」这类空话；不写「显然」。
- 术语按 `04-术语文献勘误.md` 与香蕉空间核对结果：球簇（不写球形簇）、超球簇、对偶群（caron $\check G$）、小 Weyl 群、周期层、$L$-层、多重数自由、无分歧/分歧；「几何 Satake 等价」用全称。

## 5. 自检

```bash
python datasets/lawrge24/tools/lint_cards.py 2>&1 | grep -E "<你的 slug>|cards=" 
```

重点看：quote 是否命中、summary 是否超 120 汉字、related 是否写错 id、derivation 是否 ≥4 步。把错误修到 0 再回报。
