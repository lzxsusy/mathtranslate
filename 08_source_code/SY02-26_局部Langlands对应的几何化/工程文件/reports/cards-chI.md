# Chapter I（导论，PDF p.7–p.44）资料卡报告

本批为 `datasets/fs21` 的首批卡片：概念卡 10 张、推导卡 3 张，全部落在 Chapter I 的导论层，不展开 Ch II 及以后的材料。所有卡片 `rights="rewritten"`、`status="draft"`，每张 3–4 条 `sources`（全部 `text="A"`，逐条带 `quote`、`pages`、`anchor`），`quote` 共 51 条。

## 1. 为什么是这 13 个

### 1.1 选卡原则

只选**承重件**：在导论里承担「定义某个对象 / 证明某个定理 / 装配某条构造」三类职能之一，并且能在一页内指到原文的定理、定义或公式。按这个标准，五条轨道各取 2 张概念卡，推导卡只取三处真正「从 A 造出 B」的构造。

- **A 轨（FF 曲线）**：`ff-curve` + `banach-colmez-space`。曲线本身是 A 轨的入口；但导论关于曲线的三个定理（I.3.1–I.3.3）只是陈述，真正被后文反复使用的是它的**截面函子**（BC 空间），没有 BC 就没有 §I.4 局部图卡的紧合性与上同调光滑性论证。只做曲线不做 BC，会让 A 轨变成「有对象、没工具」。
- **B 轨（Bun_G / shtuka）**：`bun-g-stack` + `hecke-stack`。前者是整个层范畴的承载者（`D(Bun_G,Λ)`、谱作用、主猜想的左边），后者是「修改」的模空间（`T_V` 的定义域）。二者一静一动，缺一则 §I.7 的 Hecke 算子无法落地。
- **C 轨（diamond / v-层）**：`diamond` + `small-v-sheaf`。前者提供几何对象（`X_S`、`Div¹`、`Gr^I_G` 都在其中取值），后者提供有限性（「小」= 可写成紧合、可表为空间菱形的闭子层之递增并），二者共同支撑「在没有绝对曲线的世界里谈紧合与维数」。
- **D 轨（几何 Satake）**：`geometric-satake` + `hyperbolic-localization`。前者是 `Ĝ` 出现的源头（`Sat^I_G(Λ) ≃ Rep((Ĝ⋊W_E)^I)`），后者是它证明的技术核心。原文 p.29 明确说双曲局部化 "Critical to all of our arguments"，且它对每个 Levi 造 `Sat_G → Sat_M`，是整系数版本与 pinning 的唯一通道。
- **E 轨（L-参数 / 谱作用）**：`l-parameter-stack` + `spectral-action`。前者是靶（`Z¹(W_E,Ĝ)/Ĝ`），后者是作用（`Perf(Z¹/Ĝ)` 作用在 `D_lis(Bun_G)` 上）；`Thm I.10.1` 把「表示论侧的幺半函子族」与「几何侧的作用」判等，是全篇的收束点。

### 1.2 与任务书候选的偏离

任务书列的候选是方向而非硬指定，我改了四处，理由都可核：

| 候选 | 处理 | 理由 |
| --- | --- | --- |
| `spherical-hecke` | 换成 `hyperbolic-localization` | Ch I 全篇 `spherical` 出现 **0 次**（grep `01_pages/p007–p044`）——它是 Ch II 之后的语言，在本章做卡只能注水。 |
| `euler-product` | 不做 | 同上，`Euler` 在本章出现 0 次。 |
| `excursion-operator` | 从概念卡降为推导卡（`fs21/deriv/excursion-operator-reads-phi`） | Ch I 没有给游走算子独立定义（它只在 Prop I.9.1 的构造里出现），做成概念卡会逼我编一个原文没有的「定义」；它的内容恰好是三步构造，正是推导卡。 |
| `whittaker-sheaf` | 不做，列入 §4 | p.38 只有一句定义，真正的使用要等 Ch IV，证据不足。 |
| `p-adic hodge` 相关 | 不做 | 导论只在 untilt / 等晶体的语境里点到，展开就会侵入 Ch II–III；已作为 `ff-curve` 的一条 pitfall 处理。 |

另有三张「本可以做但故意不做」：`B(G)`（Kottwitz 集）虽是重要记号，但它在导论里全部作为 `Bun_G` 的分层指标出现，单独立卡会与 `bun-g-stack` 重复；`untilt`、`shtuka` 模空间见 §4。

### 1.3 三张推导卡的取舍

导论里真正「从 A 造出 B」的构造只有三处，且每处都能把每个推导步定位到原文一句或一个公式：

1. `satake-to-hecke-operator`（D）：`Sat` 等价 → 层 `S_V` → 沿 Hecke 对应推拉 → `T_V`，并解释 `W_E^I`-等变性。
2. `excursion-operator-reads-phi`（E）：`α,β,γ_i` → 游走算子 → 标量 → 唯一半单 `φ_A`。
3. `spectral-action-compact-support`（E）：紧支撑作用 ↔ 幺半函子族，两个方向互造，收于 `Conj I.10.2`。

`Thm I.2.6`（`B(G) ≅ Bun_G(Spa C)/≅`）虽然同样重要，但它的证明外包给 [Far20a] 与 [Ans19]，本章只给陈述；硬拆成推导卡会得到一张「每步都标 C」的卡，违背「每个推导步必须能定位」的要求，故只在 `bun-g-stack` 里以 `proof.status="sketch"` + `gap_note` 处理。

## 2. 轨道分布

| 轨道 | 概念卡 | 推导卡 | 合计 |
| --- | --- | --- | --- |
| A · FF 曲线与向量丛 | `ff-curve`、`banach-colmez-space` | — | 2 |
| B · Bun_G 与 shtuka | `bun-g-stack`、`hecke-stack` | — | 2 |
| C · diamond 与 v-层 | `diamond`、`small-v-sheaf` | — | 2 |
| D · 几何 Satake 与 Hecke | `geometric-satake`、`hyperbolic-localization` | `satake-to-hecke-operator` | 3 |
| E · L-参数与谱作用 | `l-parameter-stack`、`spectral-action` | `excursion-operator-reads-phi`、`spectral-action-compact-support` | 4 |
| **合计** | **10** | **3** | **13** |

概念卡 A2/B2/C2/D2/E2；推导卡 D1/E2。D、E 两轨各多一张推导卡，因为导论的构造性内容集中在 §I.7 与 §I.9–I.10。

## 3. 每张卡一句话

| # | 卡片 | 一句话 |
| --- | --- | --- |
| 1 | `fs21/concept/ff-curve` | 把完满的去心圆盘或形式圆盘按 `φ^ℤ` 取商得到的 adic 曲线族；只有 `S=Spa C` 时它才是真正的曲线，经典点由 untilt 参数化，向量丛按斜率 λ 唯一分解为 `⊕O_{X_S}(λ)`。 |
| 2 | `fs21/concept/banach-colmez-space` | 向量丛整体截面函子 `T↦H⁰(X_T,E)` 的几何化：正斜率给完满开圆盘，负斜率给「仿射线除以平移」，是局部图卡 `M_b` 与紧合性论证的原料。 |
| 3 | `fs21/concept/bun-g-stack` | `S↦{X_S 上 G-主丛}` 的 v-叠；曲线本身不良定义而它良定义，分层为 `[*/G̃_b]`、半稳定层开、`|Bun_G|≅B(G)`，全部 Hecke 与谱作用都长在它上面。 |
| 4 | `fs21/concept/hecke-stack` | 记录两 `G`-丛沿除子「修改」的叠；Schubert 分层使两投影紧合，从而 `T_V` 有定义，全局与局部版本由 `q` 相连。 |
| 5 | `fs21/concept/diamond` | 完满空间按 pro-étale 等价关系取商所得的几何对象；`Z^♢` 构造把 untilt 变成层，`Div¹` 只是菱形，空间菱形才承载紧合、维数与上同调光滑。 |
| 6 | `fs21/concept/small-v-sheaf` | `Perf` 上对 v-拓扑的层与叠；「小」是有限性条件（紧合、可表为空间菱形的闭子层之递增并），`Gr^I_G` 与 `Bun_G` 的有限性论证都靠它。 |
| 7 | `fs21/concept/geometric-satake` | `Sat^I_G(Λ) ≃ Rep((Ĝ⋊W_E)^I)`：把 `Ĝ` 的表示实现为 Hecke 叠上的反常层，是 `T_V` 与 `Ĝ` 出现的源头。 |
| 8 | `fs21/concept/hyperbolic-localization` | `CT⁻→CT⁺` 在等变对象上是等价（本文版 Braden 定理），是 Satake 变换、Levi 限制与相对反常 t-结构的共同技术核心。 |
| 9 | `fs21/concept/l-parameter-stack` | 以连续 1-上闭链 `φ:W_E→Ĝ(Λ)` 为 `Λ`-点的概形 `Z¹(W_E,Ĝ)` 及其商叠；用凝聚态解决「代数 vs 连续」的错配，是谱作用与 `Ψ_G` 的靶。 |
| 10 | `fs21/concept/spectral-action` | `Perf(Z¹(W_E,Ĝ)/Ĝ)` 在 `D_lis(Bun_G)` 上的紧支撑作用，与「对每个 `I` 给 `Rep(Ĝ⋊Q)^I` 的幺半作用」等价（Thm I.10.1）。 |
| 11 | `fs21/deriv/satake-to-hecke-operator` | 从 Satake 等价取层 `S_V`，沿 `Hck^I_G` 的对应推拉得 `T_V`，并用「`Div¹` 仍只是一个点」证明其 `W_E^I`-等变性。 |
| 12 | `fs21/deriv/excursion-operator-reads-phi` | 用 `α,β,γ_i` 把 `T_V(A)` 上的 `W_E^I`-作用压成 `A` 的自同构标量，这些标量唯一确定连续半单 `φ_A`。 |
| 13 | `fs21/deriv/spectral-action-compact-support` | 两个方向互造「紧支撑作用 ↔ 幺半函子族」，用 Thm I.8.2 的生成性证互逆；施于 Whittaker 层 `W_ψ` 得 `Conj I.10.2`。 |

## 4. 本章最重要但没做成卡的 3 个概念

1. **untilt（`S^♯`）**。它是 §I.2–I.3 的技术枢纽（`X_C` 的经典点 = `C` 的 untilt 模 Frobenius，`Div¹=(Spa Ė)^♢/φ^ℤ` 也靠它），但 Ch I 没有给它独立定义，只是反复使用「`S` 的 untilt」这一短语；单独做卡会得到一张「只有用法、没有定义」的卡。处理：已把它写进 `ff-curve` 的 `key_points` 与 `pitfalls`（并注明「没有绝对曲线、Frobenius 只在 `(Spa Ė)^♢` 上存在」），不另立卡。
2. **shtuka 模空间 `Sht_{(G,b,μ_•),K}`**。导论只在 §I.7 用它做 `Cor I.7.3` 的有限性推论（局部 Shimura 簇的 `RΓ` 紧性），定义与主定理都在 [SW20]；Ch I 层面做卡只能复述引用。处理：作为 `hecke-stack` 与 `satake-to-hecke-operator` 的一条 `related` 语境提及，不立卡；等 Ch IV 再补。
3. **Whittaker 层 `W_ψ`**。它是 `Conj I.10.2` 的主角，但 p.38 只给一句定义（集中在 `Bun¹_G`、对应 `c-Ind_{U(E)}^{G(E)}ψ`），其构造与性质要等 Ch IV；做卡会变成「一句原文 + 九句转述」。处理：写进 `spectral-action` 的 `theorems` 的 `gap_note` 与 `spectral-action-compact-support` 的 `setup`，不单独立卡。

补充一个「想做但证据不够」的：**Kottwitz 集 `B(G)` 的 `(ν,κ)` 不变量**。p.20 给了完整定义与偏序，材料其实够；但它在本章的作用完全是 `Bun_G` 的分层指标，独立成卡会与 `bun-g-stack` 的 `key_points` 大段重复，故按「宁多勿滥也别硬凑」的原则放弃。

## 5. 自检

### 5.1 lint

```
python 资料卡/tools/lint_cards.py 资料卡/cards --prefix fs21 --max-pages 356 --no-pkg --strict
```

输出最后一行（原文）：

```
[done] 卡 13 张（概念 10 / 推导 3），错误 0
```

`--strict` 下 exit 0。`--no-pkg` 是必须的：本工程没有 `notes.md` / `errata.tsv`，包级检查会误报。

### 5.2 quote 校验（替代 verify_pages.py）

`python 资料卡/tools/verify_pages.py 资料卡 --strict` 在本工程**必然失败**，原因不在卡片：

- 该脚本把第一个参数当「包目录」，要求目录名形如 `NN_xxx`，用 `int(pkg.name.split("_")[0])` 取编号（`verify_pages.py:54`）；
- 本工程的卡片直接放在 `资料卡/cards/` 下，`pkg.name` 是 `资料卡`，`int("资料卡")` 抛 `ValueError: invalid literal for int() with base 10: '资料卡'`，exit 1；
- 即使绕过这一步，它还会去找 `资料卡/txt/01/p*.txt`（`verify_pages.py:55`），本工程没有这个目录（原文在 `01_pages/`）。

因此改用自写校验（放在工程外临时目录，不污染工程）：读每张卡的全部 `sources`，按 `verify_pages.py` 同一套 `norm` 规则（转小写、`LIG` 连字映射、删去所有非 `[a-z0-9]`）在 `01_pages/p{p1}.txt … p{p2}.txt` 中搜索 `quote` 的归一化子串，同时检查 `12 ≤ len(quote.strip()) ≤ 120` 与「不含汉字」。结果：

```
[quote-check] 51 quotes, 0 bad, files=13
```

即 13 张卡、51 条 `quote` 全部能在声明的页码区间内逐字命中，exit 0。

### 5.3 其它一致性

- `pages` 一律用 PDF 页，即 `01_pages/pNNN.txt` 的文件编号（任务书规定本工程印刷页 = PDF 页）：`ff-curve` 的 12–14、13、18，`l-parameter-stack` 的 32、33，`spectral-action` 的 37、38 都直接对应该编号的源文件。注意 `工程文件/work/pagemap_chI.tsv` 记的是「原文页 → **译本**页」（p.7→1、p.18→11、p.44→36），与卡片 `pages` 字段无关，两者的编号体系没有混用。
- 译名与 `glossary.tsv`、`术语裁定.md` 完全一致：perfectoid=完满、diamond=菱形、excursion=游走、Hecke eigensheaf=Hecke 特征层、Langlands dual=朗兰兹对偶群、condensed=凝聚态、solid=固体；ULA/anima/shtuka/`Bun_G` 不译。
- 未引入 `X_{FF}`（`symbols.tsv` 明确禁止；原文一律用 `X_S`）；`B(G)` 一律写 `B(G)=B(E,G)`。
- 已知限制：Ch I 没有给「小 v-层」的正式定义，`small-v-sheaf` 卡按原文的使用方式陈述并在 `theorems` 里标 `proof.status="sketch"` + `gap_note`；`Thm I.4.1` 的 (iv)/(v) 与 Ch III `Thm III.0.2` 编号互换（见 `疑点清单.tsv`），卡内按 p.21 原文写，不擅自「更正」。
