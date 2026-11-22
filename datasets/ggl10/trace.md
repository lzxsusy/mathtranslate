# 决策记录（14 条，其中 4 条是真实走过的弯路）

每条四栏：判断点 / 依据 / 结论与理由 / 事后确认。

**1. 页码基准取 PDF 页序还是印刷页号**
- 判断点：卡片与 notes 的 `p.N` 用哪一个？
- 依据：任务书要求 PDF 页序；`verify_pages.py` 按 `txt/10/pNNN.txt` 回查；页脚实测 p008=7、p067=66。
- 结论与理由：全部用 PDF 页序；印刷页 = PDF−1，只在 notes §0 说明，不参与任何 locator。
- 事后确认：`verify_pages` 46 条 A 类 quote 全过，0 问题。

**2. 公式页的定位（这是弯路）**
- 判断点：读正文时我按「节起始页 + 目测」把 (5.61) 记在 p117、把 (5.61)–(5.68) 的若干条记在相邻页，随后按此写卡片。
- 依据：第一版卡片直接用了这些目测页；`verify_pages` 报出 5 条页码不符（knot-monodromy p76→p75、stokes-jumping p70→p71、wilson-loop p72→p73 与 p73→p74、singularity p112→p113）。
- 结论与理由：改用脚本把每个 `(n.m)` 在 `txt/10/p*.txt` 里全文检索、取首次**显示**该式的页；再按检索结果逐条改 `pages` 与 `anchor`。公式页与「正文提到该式」的页必须区分，不能凭阅读顺序猜。
- 事后确认：`verify_pages --strict` 0 问题；另写脚本核对 15 张卡的 `A p.N eq (x.y)`，修掉 3 处 anchor 与页不一致后 bad=0。

**3. p118 的 γ=k/n（这是弯路）**
- 判断点：p118 写「where as usual γ = k/n」，而 §5 开头写 γ=n/k；到底哪个是定义？
- 依据：初读时我一度按 p118 的字面把全节的 γ 当 k/n，甚至怀疑 p086 的 n/k 是笔误。
- 结论与理由：查 p086「fixed ratio γ = n/k」、p099「ln m=iπγ」与 p082 的 m=exp(iπ(n−1)/k)，三者只在 γ=n/k 下相容；p100 的 γ=±(1/6+p) 也是按 n/k 推出。故 p118 是笔误，记 E1（high），卡片按 n/k 写。
- 事后确认：下载 arXiv v1 比对，v1 同页也写 k/n，排除「v4 修版引入」；errata E1 的 impact 与两卡 corrections 对上。

**4. p119 的「just greater than 1/3」（这是弯路）**
- 判断点：p119 说「To continue past γ = 2/3」之后，紧接着写「The integration cycle for γ just greater than 1/3」；是否我把 2/3 读错？
- 依据：同段明确说 past 2/3，下段又说「with Re γ > 2/3, exponential growth comes from...」；且 (5.66) 是在 γ→2/3 下方取的 cycle。
- 结论与理由：p119 的 1/3 是笔误，应为 2/3，记 E2（high）；卡片按 2/3 写。
- 事后确认：v1 同误；E2 只影响 figure-eight-volume-cycle，已挂 corrections。

**5. 是否给「定理」编号**
- 判断点：全文没有编号定理，notes 的主命题清单与卡片怎么组织？
- 依据：grep「Theorem」只命中引 [16]/[23]/[49] 等外部文献处；本文只有公式号。
- 结论与理由：notes 自编 S1–S17 并注明「编号为笔记所加」；卡片只引公式号与 PDF 页，不引 S 编号，避免二次编号错位。
- 事后确认：lint/verify 不依赖 S 编号；卡片交叉引用稳定。

**6. 概念卡取 11 张还是 13 张**
- 判断点：§2–§6 可建卡的对象很多（Bessel 原型、指标、分组、§6 的 Hilbert 空间），取多少？
- 依据：任务要求 11±2；卡片要能迁移，不能是摘要。
- 结论与理由：取 11 张，覆盖「作用量—thimble—流方程—半稳定—纽结单值—彩色 Jones—A 多项式—Stokes—局部奇点—体积猜想—Wilson 圈 ρ 场」；放弃 Bessel 原型（§3.5）与指标细节（§4.1.1），只写进 notes 骨架；§6 的 Hilbert 空间不单独建卡，附在 notes S17。
- 事后确认：11 张都有 ≥3 条 A 类 quote 或 A+C；lint 0 error。

**7. 推导卡取哪 4 条**
- 判断点：可推的链条很多（Bessel 的 (3.66)–(3.73)、三叶结 Stokes 曲线、八字结 cycle），取哪 4 条？
- 依据：要求每步 text/why/locator/provenance 齐全，且是主线。
- 结论与理由：取「作用量与 k+h 移位」「流方程平方和 ⇒ φ_t=0」「三叶结 W 与 I」「八字结 cycle ⇒ 体积指数」；放弃 Bessel 原型（枝节）与三叶结 Stokes 曲线的完整推导（只作概念卡 S14 的要点）。
- 事后确认：4 张各 5 步，locator 全部落在含该式的页（脚本核过）。

**8. term_index 撞名怎么处理（这是弯路）**
- 判断点：`stokes-jumping` 的别名 `Stokes phenomenon` 与 `pathintegral:pi/concept/stokes-phenomenon` 撞名，改标题还是改别名？
- 依据：任务要求「把新卡标题写专，不要改旧卡」；标题本身不撞，撞的是别名。
- 结论与理由：保留标题「Stokes 曲线与 thimble 系数的跳跃」，把别名改为 `Stokes jumping of Lefschetz thimbles` / `wall-crossing of thimble coefficients` / `jumping n_tau`；没有为通用概念重复造卡。
- 事后确认：`term_index.py check` 0 撞名。

**9. meridian/longitude 的中译（这是弯路）**
- 判断点：m̂（短、环绕数 1）与 l̂（长、环绕数 0）分别译什么？
- 依据：初稿把两者都写成「经线」，读起来分不清；查旧库与纽结理论惯例，meridian=子午线、longitude=经线。
- 结论与理由：m̂ 改「子午线」、l̂ 保留「经线」；A 多项式卡标题改成「子午线/经线本征值 l、m」，并在 terms.tsv 固定这两条。
- 事后确认：grep 全部卡片，只有 l 还叫经线、m 都叫子午线；terms.tsv 与卡片一致。

**10. m²+m⁻²+1>1 是否列 errata（这是弯路）**
- 判断点：p116 写「For m²+m⁻²+1>1」，而 §5.3.3 的 case (2) 用 >0；是否笔误？
- 依据：初看像漏了 0；但 p116 该段只讨论「一对 SL(2,C) 平坦联络被复共轭交换」的某个子区，>1 是更强的充分条件，不与后文等式冲突。
- 结论与理由：按 §9.2「只有一处冲突」的标准不足以判笔误，撤回候选，不列 errata；写进 notes 的「排除项」。
- 事后确认：errata 只留 E1/E2；notes 的排除项有记录，未把它说成笔误。

**11. (5.11)–(5.12) 的 C·C⁻¹ 是否列 errata**
- 判断点：符号计算给出 C⁻¹xC=diag(m,m⁻¹)、C⁻¹yC=(5.12)，而文中写 C·C⁻¹；是否为笔误？
- 依据：SymPy 直接算 CxC⁻¹=[[m,2],[0,m⁻¹]]；C⁻¹yC 与 (5.12) 逐元素相等。只影响记法，bc<0 判据与结论不变。
- 结论与理由：确实与印出的 C 不一致，但没有任何卡片引用 (5.11)–(5.12)，且这是「C 还是 C⁻¹」的记法问题；不列 errata，只在 notes「不懂」第 1 条记录。
- 事后确认：卡片 0 处引用该式；notes 有完整计算描述。

**12. 外部源选哪些**
- 判断点：任务要求每个公式至少两处独立出处；只靠 arXiv abs 不够。
- 依据：能拿到的：arXiv abs、INSPIRE API、arXiv v1 PDF、Murakami 0802.0039、Hikami–Murakami 0711.2836、nLab 两页、库内 csw/ggl13 卡。
- 结论与理由：选 Murakami 综述核三叶结/八字结的单值与 A 多项式，选 Hikami–Murakami 核 n^{1/2}/n^{2/3}，选 nLab 核体积猜想的 2π 因子与复群 CS 的定位；arXiv v1 只用于版本比对。所有下载物放 `external/`，卡片不写路径。
- 事后确认：notes 外部来源表 8 行；卡片 A+C 来源合计 53 条；`verify_pages` 跳过非 A 的 7 条，其余 46 条全过。

**13. 摘要「generalizing」与 arXiv 元数据「rotating」**
- 判断点：本地 v4 PDF 摘要与 arXiv abs 页摘要措辞不同，是否版本/笔误？
- 依据：本地 PDF 是 v4（页眉），arXiv abs 也标 v4；差异只在「generalizing the usual integration cycle」vs「rotating the integration cycle」。
- 结论与理由：这是摘要元数据与 PDF 正文的差异，不影响数学内容（正文两处都说 rotate/deform cycle）；不列 errata，只在 notes ① 项说明。
- 事后确认：未影响任何卡片或公式。

**14. 不跑 lead 的三条命令**
- 判断点：`package.py ship`、`build_train.py`、`thinking_card.py` 是否要跑？
- 依据：任务书明确「由 lead 统一做」，且 `package.py ship` 会写发布仓。
- 结论与理由：一律不跑；只跑 lint/verify/term_index 三条自检。外部 PDF 只落 `external/`。
- 事后确认：交付目录只有 notes/cards/terms/excerpts/errata/trace/workflow 与 external，没有 index.jsonl/README/MAP。
