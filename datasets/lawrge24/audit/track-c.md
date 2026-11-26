# Track C 外部来源交叉核验

范围：`datasets/lawrge24/cards/concepts` 中 track C 的 8 张卡 + `cards/derivations` 的 2 张卡，共 10 张。每张卡取 3 条实质断言，共 **30 条**。

底本：LAWRGE 2024 NOTES（73 页工作坊笔记，Ben-Zvi/Sakellaridis/Venkatesh 主讲，自述不完整、未校订），`08_source_code/SY02-15_相对朗兰兹对偶/工程文件/work/原文/ch08.txt`、`ch10.txt`。

## 判定汇总

| verdict | 条数 |
|---|---|
| supported | 13 |
| partially-supported | 12 |
| unverifiable | 3 |
| conflict | 2 |
| **合计** | **30** |

| severity | 条数 |
|---|---|
| critical | 1 |
| major | 10 |
| minor | 19 |

## 逐卡结果

| card | 断言数 | supported | partial | unverifiable | conflict | 要点 |
|---|---|---|---|---|---|---|
| concept/spherical-variety | 3 | 2 | 1 | 0 | 0 | 定义与 A_X/V 有 Brion、Bourbaki、BZSV 支持；Thm 8.19 的一般拟仿射情形只有仿射/齐性版本 |
| concept/multiplicity-free | 3 | 1 | 0 | 2 | 0 | 多重自由定义成立；(8.16) 局部有限判据与 X=G 反例均无外部对应 |
| concept/rank-one-freeness | 3 | 0 | 3 | 0 | 0 | 自由秩一是期望；BZSV 给的是类函数 C[Ǧ_X]^{Ǧ_X}，不是 C[Rep Ǧ_X] |
| concept/dual-group | 3 | 2 | 1 | 0 | 0 | 由 based root datum 对偶成立；Ǎ_X→Ǎ 的 “iff kernel connected” 仅部分来源；群情形有约定差异 |
| concept/relative-cartan | 3 | 3 | 0 | 0 | 0 | A_X 最大忠实商、精确列、Ǎ_X 为极大环面三源一致 |
| concept/little-weyl-group | 3 | 2 | 1 | 0 | 0 | V 基本域、T*X//G 同构成立；“三等价定义”的 Knop B-轨道作用未逐条核 |
| concept/hyperspherical-variety | 3 | 1 | 1 | 0 | 1 | 五条件内容成立；但“任意球簇的 T*X 都超球”与 Bourbaki 的 no Type N 条件冲突 |
| concept/hyperspherical-structure | 3 | 1 | 1 | 0 | 1 | **S 应为 H-表示，不是 G-表示**；V_X 公式多出 ǧ_1 |
| deriv/rank-one-freeness-derivation | 3 | 0 | 2 | 1 | 0 | 六步中“无关系”一步无证明，外部也无 |
| deriv/dual-group-assembly | 3 | 1 | 2 | 0 | 0 | 组装原则成立；(10.2) 与 BZSV 的类函数表述不一致 |

## 需要改卡的清单（按优先级）

1. **`concept/hyperspherical-structure`（critical，conflict）**
   卡片定义与定理都写“S 是 G 的辛表示”，底本 p.52 也写 “S a symplectic representation of G”。但外部五源一致为 **H-表示**：
   - BZSV Thm 3.6.1：`a symplectic H-vector space S`（arXiv:2409.04677, §3.6.1, p.62）
   - Bourbaki Thm 4.20：`a symplectic H-vector space S`（Exp. 1238, p.30）
   - Dai Thm 3.17：`a symplectic H-vector space S`
   - Gan slides：`S a (graded) symplectic (finite dim) representation of H`
   - Mao–Wan–Zhang：`ρ_H is a symplectic representation of H`
   这不是记号问题：结构定理的数据是 (G, H, ι, S)，S 是 H 的辛表示，Whittaker induction 沿 H×SL₂→G。建议改定义、定理陈述、summary 三处。

2. **`concept/hyperspherical-variety`（major，conflict）**
   卡片把“球簇的余切 T*X”当作无条件基本例子（关键点还写“T*X（X 球）是连接两者的桥”）。Bourbaki §4.6(i) 明确要求 **X 仿射光滑且没有 Type N 根**；BZSV §1.2 也说还需 moment map 与 generic stabilizer 的 mild conditions。建议加条件，或在定义后注明“并非任意球簇都成立”。

3. **`concept/rank-one-freeness` + `deriv/rank-one-freeness-derivation` + `deriv/dual-group-assembly`（major，partially-supported）**
   “S(X(F))^{G(O)} 在 H_X^G=C[Rep Ǧ_X] 上自由秩一”是底本的 **expectation**（p.41 “We expect”），卡片基本按定理口吻写。BZSV §9.4 给的是
   `Cc∞(X_f/G_O) ≅ C[Ǧ_X]^{Ǧ_X}`（类函数环），并带 distinguished vector 与内积；全文没有 “free of rank one”，也不是在 C[Rep Ǧ_X] 上。`(10.2)` 同样把右边写成 C[Rep Ǧ_X]，与 BZSV 的类函数表述不一致。建议把“自由秩一”标为猜想/期望，并把 (10.2) 改为 BZSV 的类函数版本（或注明底本自己的形式）。

4. **`concept/hyperspherical-structure` 的 V_X 公式（major，partially-supported）**
   底本 p.53 与卡片写 `V_X = ǢS ⊕ (ǧ/ǧ_X)_e + ǧ_1`；BZSV (4.16) 写 `V_X = S_X ⊕ [g_X^⊥ ∩ g^e]`。在 e∈g_X 时前两项可对应，但底本多出 `ǧ_1`，BZSV 无此 summand。需人工核对底本是否用了不同分级约定。

5. **`concept/spherical-variety` 的 Thm 8.19（minor，partially-supported）**
   底本说“拟仿射球簇 ⇔ F[X] 多重自由”，但只证 ⇒；外部 Brion Lemme 2.12 只覆盖 **仿射** X，Kimelfeld–Vinberg（Can 的 slides）只覆盖 **拟仿射齐性** X。一般拟仿射情形没有找到逐字定理。建议在卡上标“仿射/齐性已证，一般拟仿射为底本断言”。

6. **`concept/multiplicity-free` 的 (8.16)（major，unverifiable）**
   `dim Hom_{H_G}(Func(X(F)),C_χ)<∞ ⇔ X spherical` 在 BZSV、SV、Brion、Dai 中均未检索到；底本自称 Claim 且只证 ⇒。X=G 的 Peter–Weyl 反例也只是底本论证，未外部展开。建议标“底本内部 Claim，未外部核”。

7. **`concept/dual-group` 的 “iff kernel connected”（minor，partially-supported）**
   SV 只说 `A*_X → A*` 有 finite kernel，并给 PO2\PGL2 的 order 2 例子；没有“单 iff ker(A↠A_X) 连通”的逐字判别。这可作为底本补充，但不应标为已引用的定理。

8. **`concept/little-weyl-group`（minor）**
   (a) V 基本域、(b) T*X//G ≅ a*_X/W_X 有 Bourbaki/BZSV/Knop 支持；但 (c) Knop 用 PGL₂ 四类型对 B-轨道的作用没有逐条核；“T*X→g*→a*/W 经此分解”也没有找到逐字表述，故该条降为 partial。

9. **`concept/hyperspherical-variety` 的 Remark 10.20（minor，partially-supported）**
   “(2)+(3) 对偶于 (1) 只是实验”与 Dai Prop 3.6（拟仿射时 T*X 余迷向 ⇔ X 球）有张力；BZSV 对 T*X 的条件 (4) 有对偶 Cartan 解释，支持“自动”。建议不要把“实验”写成定论，也不要把 Dai 的定理误当反例。

## 来源与独立性说明

实际打开并抽取正文的来源：

- Brion, *Introduction to actions of algebraic groups*, Les cours du CIRM 1.1 (2010) 1–22 — http://www.numdam.org/item/10.5802/ccirm.3.pdf
- Knop, *Spherical roots of spherical varieties*, Ann. Inst. Fourier 64 (2014) 2503–2526 — https://aif.centre-mersenne.org/item/10.5802/aif.2919.pdf
- Ben-Zvi–Sakellaridis–Venkatesh, *Relative Langlands Duality*, arXiv:2409.04677 — https://arxiv.org/abs/2409.04677
- Gan, Bourbaki seminar Exp. 1238 — https://bourbaki.fr/TEXTES/Exp1238-Gan.pdf
- Sakellaridis–Venkatesh, *Periods and harmonic analysis on spherical varieties*, arXiv:1203.0039 — https://arxiv.org/abs/1203.0039
- Gaitsgory–Nadler, *Spherical varieties and Langlands duality*, arXiv:math/0611323 — https://arxiv.org/abs/math/0611323
- Can, *Spherical Schubert Varieties* (Okinawa slides, 2020-09-29) — https://groups.oist.jp/sites/default/files/imce/u111531/Okinawa_29%3A09%3A20_0.pdf
- Dai, *Hyperspherical Hamiltonian Varieties* (seminar notes) — https://dai-wenhan.github.io/blurbs/hamiltonian.pdf
- Gan, *Relative Langlands Duality* slides — https://www.majiajun.org/wp-content/uploads/2024/07/Wee-Teck-Gan-2.pdf
- Mao–Wan–Zhang, *Relative Langlands duality for some strongly tempered spherical varieties* — http://sites.rutgers.edu/chen-wan/wp-content/uploads/sites/518/2025/04/BZSV.pdf

独立性提醒：BZSV 是这些材料的共同上游；Bourbaki、Dai、Gan slides、MWZ 对结构定理的表述都依赖 BZSV，严格说不是独立证据。真正相对独立的是 Brion（定义/多重自由）、Knop（little Weyl）、SV（A_X 与对偶环面的技术细节）、GN（Tannakian 构造）、Can（Kimelfeld–Vinberg 的讲义陈述）。因此“五源一致”表示“五份不同文献一致”，不表示五个独立证明。

## 未能核验/打不开的记录

- 对 (8.16) 与“无关系”步骤，已在 BZSV、SV、Brion、Dai 全文检索，均无对应陈述；这不是页面打不开，而是来源中没有该断言。
- BZSV 全文没有 “free of rank one”；`C[Rep Ǧ_X]` 与 `C[Ǧ_X]^{Ǧ_X}` 的差别是本次核验最实质的发现之一。
- 早期尝试的 `arXiv:1203.3602` 是无关的 “Picture-Hanging Puzzles”，已弃用；正确 SV 编号为 `1203.0039`。
- 所有引文均来自上述 PDF 的文本层；PDF 抽取会在数学符号两侧插入空格，JSONL 中的引文做了空格归一化，未改动词句。

## 最需要人工处理的 3 条

1. **hyperspherical-structure 的 S 类型（critical）**：S 是 H-表示，不是 G-表示；底本 p.52 的 “of G” 是错误源头，卡片照抄。
2. **hyperspherical-variety 的“任意球簇 T*X” （major conflict）**：Bourbaki 要求 no Type N roots，BZSV 还要求 generic stabilizer 的 mild conditions。
3. **rank-one-freeness / (10.2) 的“自由秩一 over C[Rep Ǧ_X]”（major）**：这是底本的 “We expect”，BZSV 给的是 C[Ǧ_X]^{Ǧ_X} 类函数环，不是表示环。
