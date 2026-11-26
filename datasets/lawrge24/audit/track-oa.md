# track O/A 外部来源交叉核验汇总

- 数据集：`datasets/lawrge24`（LAWRGE 2024 NOTES *Relative Langlands Duality*，73 页，Ben-Zvi/Sakellaridis/Venkatesh 主讲，无 arXiv，自述「不完整、未校订」）
- 范围：track O 的 9 张概念卡 + track A 的 1 张推导卡 = **10 张卡**
- 断言：**27 条**（每卡 2–3 条：定理陈述、定义、关键公式、历史归属）
- 判定：`supported` **19** ｜ `partially-supported` **7** ｜ `unverifiable` **1** ｜ `conflict` **0**
- 严重度：`major` **1** ｜ `minor` **26** ｜ `critical` **0**
- 明细：`datasets/lawrge24/audit/track-oa.jsonl`（一行一断言）

> 方法：每条断言查 ≥1 个外部来源，尽量 2 个**独立**来源（nLab、arXiv 原文/权威讲义）。引文均为抓取页面上的原句（≤200 字符）；打不开的来源记入 `attempted`。未发现外部与底本正面矛盾者，故无 `conflict`——但这不等于底本全对：7 条 partial 中有 1 条（proof-map 的定理 8.19）是「把猜想/单向结果写成已证双向定理」的实质风险。

> 可复核性：jsonl 引用的 **21 个 URL 全部实际抓取成功（HTTP 200）**；50 条引文逐条回页面核对——其中 29 条是提取文本的精确子串，其余 21 条仅因 nLab instiki 在数学符号后重复排印 TeX 源码（如 `X X`、`B G \mathbf{B}G`）或 arXiv HTML 的 MathML 噪声（如 `3 3 -manifolds`）而不匹配，已逐条短语检索确认；核对过程中改正 1 条不精确引文（nLab DW 页原句是 `of a group G (internal to Set)`，不是 `of a finite group`），并把 1 条跨句引文改为连续片段（nLab local system 页）。

## 分卡统计

| 卡 | card_id | 断言 | 判定 |
|---|---|---|---|
| relative-langlands-duality | `lawrge/concept/relative-langlands-duality` | 3 | 2 supported, 1 partial |
| a-and-b-theories | `lawrge/concept/a-and-b-theories` | 2 | 2 supported |
| proof-map | `lawrge/concept/proof-map` | 3 | 2 supported, 1 partial (major) |
| tqft-axioms | `lawrge/concept/tqft-axioms` | 2 | 1 supported, 1 partial |
| bordism-category | `lawrge/concept/bordism-category` | 3 | 3 supported |
| lagrangian-tqft | `lawrge/concept/lagrangian-tqft` | 3 | 2 supported, 1 partial |
| arithmetic-topological-dictionary | `lawrge/concept/arithmetic-topological-dictionary` | 3 | 2 supported, 1 partial |
| langlands-as-4d-tqft | `lawrge/concept/langlands-as-4d-tqft` | 3 | 2 supported, 1 unverifiable |
| boundary-conditions | `lawrge/concept/boundary-conditions` | 3 | 2 supported, 1 partial |
| tqft-1d-assignment | `lawrge/deriv/tqft-1d-assignment` | 2 | 1 supported, 1 partial |

## 需改卡清单

按处理优先级排列；「建议依据」即卡内应补/应改的外部锚点。

1. **proof-map（major）** — 断言「定理 8.19：X 球簇 ⟺ F[X] 作 H_G-模多重数自由，已证」。
   问题：可访问外部来源只支持单向（球簇 ⟹ 无分歧谱由 `A_X^*/W_X` 描述，Sakellaridis arXiv:math/0606130 摘要），且该摘要只说无分歧商与「若干份 `A_X^*/W_X` 的拷贝」成 almost bijection（多重数可 >1，故「多重数自由」不能照字面成立）；BZSV 论文自己强调 `the multiplicity one property certainly does not hold for all X such that T*X is hyperspherical`，并把 M̌ 的多重数自由说成由局部猜想 + Poisson 结构 `forces` 出来的，而非一条已证双向定理。
   建议依据：核底本 8.19 原文；若只证单向，卡片改为单向 + 条件；把「已证定理」限定到实际证明的方向，并引 arXiv:math/0606130 与 arXiv:2409.04677 §1.2/Example 8.5.4。

2. **tqft-axioms（minor）** — 断言「公理可压成两条：对称幺半 + 族上局部常值」。
   问题：外部标准是 Atiyah 1989 的一组公理（含乘法性等），而「局部/族上」属 extended（Stolz–Teichner 型）版本的额外要求；nLab 把后者写作 `A local (“extended”, “multi-tiered”) refinement`，与 Atiyah 1-函子版是两层。
   建议依据：卡片注明「两条公理是底本（LAWRGE notes）的压缩表述，非 Atiyah 公理原文」；引 nLab `topological quantum field theory` 与 `functorial field theory`。

3. **langlands-as-4d-tqft（minor, unverifiable）** — 断言 `A_G(Z)=Hom_{Rep G(Qp)}(A_G(Zp),A_G(Z[1/p]))`，黏合迫使 `A_G(Zp)=ind 1`。
   问题：BZSV 全文 HTML 检索无 `Z[1/p]`/该 Hom 式；nLab Hecke algebra 只到「Hecke 代数=置换表示的自同态」。外部无对应命题。
   建议依据：标注为「底本自述推导（未在外部文献中找到）」，或补一条底本页码 locator；不要以定理口吻呈现。

4. **relative-langlands-duality（minor）** — 「局部 Plancherel 由 M̌ 的 q-特征标给出」。
   问题：外部（arXiv:1203.0039 摘要）只说 Plancherel `should be related to` 对偶群的 Arthur 参数，且对偶群「closely related to」Gaitsgory–Nadler 的构造；「q-特征标」是 BZSV 自身表述。
   建议依据：降为「局部 Plancherel 与对偶群参数相关（猜想）；q-特征标形式见 BZSV」，引 arXiv:1203.0039、arXiv:0905.4244。

5. **tqft-1d-assignment（minor）** — 「Z(S¹)=dim V，映射环面↦tr」。
   问题：概念上成立（杯帽/迹图），但 nLab/Baez 未逐字陈述，严格只有 partial。
   建议依据：补教科书级来源（如 Kock, *Frobenius Algebras and 2D Topological Quantum Field Theories*）后升为 supported。

6. **lagrangian-tqft（minor）** — 「线性化按维数分：#X、C[X]、Vect[X]；2 维迹=除以 |G|」。
   问题：外部只支持「有限群模型按群胚基数计数」（nLab Dijkgraaf–Witten）与「2 维给圆上代数」（nLab 2d TQFT）；三档分类是底本自己的打包。
   建议依据：注明为底本组织方式；除法因子引 groupoid cardinality。

7. **arithmetic-topological-dictionary（minor）** — 「(2.1) 长正合列与 (2.2) Poincaré–Lefschetz 对偶逐项对应」。
   问题：nLab 只到 `This resembles Poincaré duality for 3-manifolds`（Artin–Verdier 配对），没有与具体序列的逐项对应。
   建议依据：把「逐项对应」限定为底本 §2 的表述；外部锚点用 nLab `arithmetic topology` 的 Artin–Verdier 段。

8. **boundary-conditions（minor）** — 「O_{G,X}(E_G)=#X^φ」。
   问题：外部只有群胚基数计数框架（nLab Dijkgraaf–Witten `groupoid cardinality of BG`），无该逐字公式。
   建议依据：注明「有限群模型的具体化，按群胚基数计数」。

9. **bordism-category / a-and-b-theories（不改卡，补来源即可）**：
   - bordism-category 三条均已判 supported，但「对称幺半」的引文只到 `monoidal` / `noncartesian monoidal`（未逐字出现 symmetric），2 维例 `C[G/G]` 与迹公式未在外部来源出现。建议补引 nLab `symmetric monoidal category`，并把 `C[G/G]` 例标注为底本自算。
   - a-and-b-theories 两条 supported 引文同页（nLab geometric Langlands），独立性弱；建议补 Beilinson–Drinfeld 或 Frenkel 讲义作第二来源。

## 外部来源清单（实际抓取成功）

nLab（11 页）：`relative Langlands program`、`geometric Langlands correspondence`、`topological quantum field theory`、`functorial field theory`、`cobordism category`、`2d TQFT`、`Frobenius algebra`、`Dijkgraaf-Witten theory`、`local system`、`arithmetic topology`、`dualizable object`。（另抓取 `Hecke algebra` 用于判断 K3，未直接引用。）

arXiv（9 篇 / 10 URL）：
- arXiv:2409.04677（BZSV 原文摘要 + 全文 HTML）、arXiv:2111.03004（Sakellaridis ICM 综述）
- arXiv:1203.0039（Sakellaridis–Venkatesh）、arXiv:0905.4244、arXiv:math/0606130、arXiv:math/0401222（Mirković–Vilonen）
- arXiv:2409.06303（S-dual 综述）、arXiv:hep-th/0604151（Kapustin–Witten）、arXiv:quant-ph/0404040（Baez）

## 未能取得 / 证伪的来源

- `https://ncatlab.org/nlab/show/geometric+Satake+correspondence` → 404（故 proof-map 的几何 Satake 只有 MV 原文一条来源）。
- `https://ncatlab.org/nlab/show/spherical+variety` → 404。
- `https://arxiv.org/abs/2401.06624` → 抓取失败（-1），未使用。
- 记忆候选被证伪：`arXiv:2409.11776` 是微游动机优化论文（非 BZSV）；`arXiv:1105.0165` 是 quantum counter automata；`arXiv:math/0204051` 是 Tolman–Weitsman 论文。均已弃用，未进入 jsonl。

## 说明

- 未修改任何卡片、README/index/统计；未运行 git。
- jsonl 的 `card_id` 取卡片自身的 `id` 字段（形如 `lawrge/concept/relative-langlands-duality`、`lawrge/deriv/tqft-1d-assignment`），与 `verification.jsonl` 的 `id` 一致；`sources[].bearing` 记录该来源支持/削弱/反对什么。
- 底本自述「不完整、未校订」：本核验只对照外部来源记录支持/削弱，不替底本补证明；外部与底本不一致处按 partial 记录并说明差异方向，未发现需记 `conflict` 的正面矛盾。
