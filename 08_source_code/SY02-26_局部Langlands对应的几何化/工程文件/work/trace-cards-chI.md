# Chapter I 资料卡 · 决策记录（trace）

格式：判断点 / 依据 / 结论与理由 / 事后确认。★ = 真实走过的弯路（先做错，发现后改回）。

| # | 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- | --- |
| 1 ★ | `diamond` 卡第一条 `quote` 写 `that is a quotient of a perfectoid space by a pro-étale equivalence relation` | 自写校验报 `MISS ... 1 bad`；调试发现归一化后我的串是 `…byaprotale…`（`é` 被整字删除），OCR 原文是 `pro-´etale`（尖音符是独立字符，删除后剩 `proetale`） | 换成纯 ASCII 前缀 `that is a quotient of a perfectoid space`（43 字符，p014 逐字前缀）。理由：`quote` 必须能被 `norm` 命中，「看起来一样」不算 | 重跑校验 `[quote-check] 51 quotes, 0 bad`，exit 0 |
| 2 ★ | 想用 `工程文件/work/pagemap_chI.tsv` 证明「印刷页 = PDF 页」 | 打开该表：`原文页\t译本页`，第一行 `7\t1`、`18\t11`、`44\t36` | 它是「PDF 页 → **译本**页」的映射，不能拿来论证 PDF 页与印刷页的关系；`pages` 字段只认 `01_pages/pNNN.txt` 的编号（任务书规定本工程印刷页 = PDF 页）。报告里删掉了这条错误依据，改为直接说明字段取自源文件编号 | 卡内 `pages` 与源文件编号逐条对应（如 `ff-curve` 13/14/18），校验脚本按 `p{p1}..p{p2}.txt` 打开文件全部成功 |
| 3 ★ | `spherical-hecke` 要不要做概念卡 | 任务书把它列为 D 轨候选；先 grep `01_pages/p007–p044`：`spherical` 命中 **0** 次、`euler` 命中 **0** 次 | 不做。Ch I 里没有这个词，做卡只能注水；D 轨第二张换成 `hyperbolic-localization`（p.29 原文称其 "Critical to all of our arguments"，且 `CT⁻→CT⁺` 有明确陈述可引） | 报告 §1.2 写明替换理由与 grep 计数；D 轨仍是 2 张概念卡，未减配 |
| 4 | 概念卡做 10 张还是只做下限 8 张 | SCHEMA 要求每轨 2–3 张、总数下限 8；五轨各自都有 ≥2 个不可替代的承重件（曲线/BC、Bun_G/Hecke、diamond/v-层、Satake/双曲局部化、L-参数叠/谱作用） | 做满 10 张（每轨 2 张），不做第 11 张。理由：第 11 张只能从 `B(G)` 或 `Gr^I_G` 里选，而两者在本章都是附属于已有卡的分层/有限性材料，会与 `bun-g-stack`、`small-v-sheaf` 重复 | lint 报 `卡 13 张（概念 10 / 推导 3）`；报告 §4 说明「宁多勿滥」的边界 |
| 5 | `excursion-operator` 是概念卡还是推导卡 | p.34–36 原文没有给巡游算子独立定义，它只作为 Prop I.9.1 构造里的三步复合（`T_α`、`(γ_i)`、`T_β`）出现 | 降为推导卡 `fs21/deriv/excursion-operator-reads-phi`。若做概念卡，`definition.text` 只能自己编一个原文没有的定义，违反 rewritten 的可追溯性 | 该卡 7 个 step 全部带 `locator`（p.34/p.35），`provenance` 5A/1B/1C；报告 §1.2 记录此取舍 |
| 6 | `Thm I.2.6`（`B(G) ≅ Bun_G(Spa C)`）的 `proof.status` 怎么标 | p.15 原文：该定理的证明在 [Far20a]，并由 [Ans19] 补全；Ch I 只给陈述与两句解释 | 标 `sketch` + `gap_note`（「证明不在本文，见 [Far20a]/[Ans19]」），不标 `complete`。理由：卡片不能把别人的证明冒充成本文的三步推导 | lint 对 `sketch` 只要求 `gap_note` 非空，通过；报告 §1.3 说明为何不为它做推导卡 |
| 7 | `Bun_G` 卡里 `Thm I.4.1` 的 (iv)/(v) 按哪个编号写 | p.21 原文 (iv) 是 `Bun^b_G ≅ [*/G̃_b]`、(v) 是 `Bun^ss_G` 开；`疑点清单.tsv` 记：Ch III `Thm III.0.2` 把这两条编号互换（p.87） | 按 p.21 原文写 (iv)/(v)，不「顺手更正」。理由：卡片锚定 Ch I，跨章编号冲突应留给全书统一处理，卡内只在自己的 `sources` 页范围内自洽 | 卡内 `theorems` 的 `source` 写 `A p.21 Thm I.4.1`；报告 §5.3 把此冲突列为已知限制 |
| 8 | `small-v-sheaf` 的「小」在 Ch I 没有正式定义，还立不立卡 | p.26 只说 `Gr^I_G` 是 small v-sheaf、可写成紧合可表闭子层之递增并；「小」的正式定义在 [SW20] | 立卡，但把「小 = 有限性条件（递增并）」写成 `key_points` 的一条，`theorems` 标 `sketch` + `gap_note` 指向 [SW20]。理由：它是 C 轨不可绕过的有限性语言，缺它 `Bun_G` 的 ULA/对偶都讲不清 | lint 通过；报告 §4 与 §5.3 都点明这是「按用法陈述、非原文定义」 |
| 9 | `quote` 的字符集要不要设一条硬规则 | 由 #1 的失败反推：`é/è/Ė/Ĝ` 在 OCR 与我的输入里归一化结果不同（`pro-´etale` vs `pro-étale`；`Ĝ`→`bG`、`Ė`→`˘E`） | 规则：`quote` 里一律避免带音调字母与组合符，必须用 OCR 的原样写法（`bG`、`˘E`、`Div1`、`OXC(λ)`）；遇到 `pro-étale` 这类词就截到它前面 | 51 条 quote 全部命中；报告 §5.2 记下规则与失败样本 |
| 10 | `verify_pages.py` 跑不过，改脚本还是绕开 | 直接跑：`ValueError: invalid literal for int() with base 10: '资料卡'`（`verify_pages.py:54` 用 `int(pkg.name.split("_")[0])` 取包编号）；且它要 `资料卡/txt/01/`（`verify_pages.py:55`），本工程原文在 `01_pages/` | 不改工程脚本（不属我可改范围），在工程外临时目录写等价校验：同一套 `norm`（lower + 连字映射 + 删非 `[a-z0-9]`）在 `p{p1}..p{p2}.txt` 里搜子串，并复核长度与汉字 | `[quote-check] 51 quotes, 0 bad`，exit 0；报告 §5.2 原文引用该脚本的报错行号与替代方案 |
| 11 | `l-parameter-stack` 卡的定义要不要引入凝聚态 | p.32 原文自陈矛盾：「要代数叠、却要连续上闭链，似乎有错配」，解法是把 `Λ` 看作 `ℤ_ℓ` 上相对离散的凝聚代数，抽象 `ℤ_ℓ`-模经 `M↦M_disc⊗ℤ_ℓ` 全忠实嵌入 | 必须写凝聚态，否则 `Z¹(W_E,Ĝ)` 的可表性没有着落，定义不成立。卡里把这一步放在 `definition.text` 与 `key_points` 各一次，并列为 `pitfall`（「把连续上闭链直接当概形映射」） | lint 通过；报告 §1.1 把它列为 E 轨两张卡之一 |
| 12 | 巡游算子卡里「存在唯一连续半单 `φ_A`」标 A 还是 B | p.34 原文把 Prop I.9.1 归给 `[Laf18, Prop 11.7]`（"essentially due to"），Ch I 只给构造与陈述，唯一性/半单性的论证未展开 | 构造三步标 A（原文逐字给出 `T_α`、`(γ_i)`、`T_β`）；唯一性与半单性单独一步标 B，并在 `provenance_note` 写明「原文归 [Laf18]，Ch I 未证明」 | 该卡 `provenance` 5A/1B/1C，`provenance_note` 逐条对应；lint 对 B/C 不额外要求，但报告与 trace 都留痕 |
| 13 | 推导步的 A/B/C 划分标准 | 试写第一版时把「由两步原文拼接」也标了 A，导致 A 的比例虚高、无法区分「原文写了」与「我接的」 | 定标准：能指到原文**一句或一个公式**→A；由两处原文按显然方式拼接/换语言→B；我补的验证、兼容性检查、或原文只说「同样成立」的地方→C。每张推导卡的 `provenance_note` 按此口径复述 | 三张推导卡分别为 7 步（5A/1B/1C）、6 步（5A/1B）、6 步（5A/1B）；lint 的 `provenance` 枚举校验通过 |
| 14 | `ff-curve` 卡里曲线的记号用 `X_S` 还是 `X_{FF}` | `symbols.tsv` 明确禁止 `X_{FF}`（原文从不用），原文一律写 `X_S`（或 `X_{S,E}`） | 全卡只用 `X_S`；`aliases` 里也不放 `X_FF` 字样。理由：记号表是冻结约定，卡片是给译者看的，引入别名会污染检索 | grep 全卡无 `X_{FF}`；报告 §5.3 记录该约束 |
| 15 | `related` 与 `index.jsonl` 的 id 怎么保证不悬空 | lint 会检查 `related` 是否命中本批 ids，但不检查 `index.jsonl` | `index.jsonl` 由脚本从卡片的 `id/type/title/track/summary/question/related/pages/status` 直接生成（`track_name` 另加映射），不手抄，避免 id 或标题漂移 | 生成后校验：13 行、11 个字段、10 concept + 3 derivation，与卡片数一致 |
| 16 | `index.jsonl` 的 `pages` 用单页还是区间 | 每卡有 3–4 条 `sources`，页码从 p.12 到 p.41 不等（如 `diamond` 跨 14–41） | 用「所有 `sources` 的 `min(p1)`–`max(p2)`」区间，不取单页。理由：索引是给读者定位用，区间比单页更诚实；单页信息在卡片 `sources` 里仍有 | 13 行的 `pages` 与各卡 `sources` 逐一吻合（生成时取 min/max，无手改） |

## 备注

- 上述 16 条里 #1、#2、#3 是真实弯路：先做错（写错 quote、用错 pagemap、按候选列了 spherical），发现后改回，并在报告或 `provenance_note` 留痕。
- 与本批卡片相关的「未做」决定集中在报告 §4（untilt / shtuka 模空间 / Whittaker 层），此处不重复。
