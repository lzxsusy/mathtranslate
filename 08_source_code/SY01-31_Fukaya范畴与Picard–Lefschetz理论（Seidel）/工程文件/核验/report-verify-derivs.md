# Seidel 推导卡核验报告（8 张）

核验对象：`datasets/seidel/cards/derivations/` 的 8 张推导卡
（mu-d-grading、twisted-differential、mapping-cone、split-generation、
lefschetz-induction、theorem-b-construction、mutation、directed-dg）。

核验依据：原书英文文本层 `work/en/pages/pNNN.txt`（印刷页 p001–p314，用于定位与抄句）、
页面图像 `work/pages/`、译者注总表 `work/精选数据/译者注总表.tsv`、
规范 `datasets/seidel/SCHEMA.md`、结构检查 `tools/lint_cards.py --strict`。
日期：2026-11-19。

## 0. 结论摘要

- 8 张卡**全部**都有需要改正的错误：没有一张可以原样通过。
- 其中 4 张是**数学内容错**（不是排版或引注问题）：
  - `split-generation`：核心断言「TwA 已分裂闭、Cone(e) 实现幂等元的像」错误；
  - `mu-d-grading`：第 3 步的齐次性方程下标错位，按原式会解出 `deg μ^d = 1`；
  - `mapping-cone`：f 被说成次数 1，且 `δ^{1,0}` 的方向与 `X_0=Y, X_1=X` 矛盾；
  - `theorem-b-construction`：包含方向写反（TwB ⊂ F(X) 应为 F(X) 嵌入 TwB）。
- 其余 4 张主要是**定位页错误 + provenance 误标**：
  - `mutation`：三个 locator 全指 p.272 §17k，实为 §18；真正出处是 p.226 (16.7)、p.77 (5.24)、p.262 Cor 17.17、p.287 (18.29)；
  - `directed-dg`：locator 指 §18（p.287/290），实为 Cor 5.27（p.87）；且第 2 步的「twisting cochain 消去」不是原书论证；
  - `twisted-differential`：结论对，但 step 1/2 标 A 过强，且误引译者注 A05-09；
  - `lefschetz-induction`：落点漏了 split-闭包 Π，且 step 2 引 p.295 不支撑该步。
- 外部依据实际打开并抄句 3 张卡（twisted complex、exceptional collection、A∞-category），见 §3。
- 收尾 `lint_cards.py --strict`：**0 error，0 warn**（70 张卡：概念 32、推导 8、勘误 30）。

### 状态一览

| 卡 | status | 关键改动 | 依据 |
|---|---|---|---|
| mu-d-grading | corrected | 页 7→8；step 3 齐次性方程改正；provenance A→B | 原书 (1.1)(1.2) p.8 |
| twisted-differential | corrected | `d_T=d+δ` 标为 dg 特例（A→B）；误引 A05-09→A01-02 | 原书 p.44 + nLab twisted complex |
| mapping-cone | corrected | f 次数 1→0；矩阵块位置与方向改正；locator 35→48 | 原书 (3.28) + nLab twisted complex |
| split-generation | corrected | 删去「TwA 已分裂闭」，改为 Π(TwA) + Lemma 4.7 + Cor 4.9 | 原书 p.3、p.59–60 |
| lefschetz-induction | corrected | 落点补 Π；step 1 改 Prop 19.7；step 2 改 p.196 | 原书 p.298、p.302–303 |
| theorem-b-construction | corrected | 包含方向反转；构造改按 §19d | 原书 p.5、p.302–303 |
| mutation | corrected | locator p.272→(16.7)/(5.24)/Cor 17.17/(18.29) | 原书 p.226、p.77、p.262、p.287 + nLab exceptional collection |
| directed-dg | corrected | 删 twisting cochain；改 Yoneda 像路线；locator→p.87 | 原书 Cor 5.27 + nLab A∞-category |

## 1. 方法与改动原则

1. **逐步检查**：每一步的 `why` 是否真的推出下一步；`locator` 所指页面是否真有该式；
   `provenance` 是否为「原文明写 = A / 由原文推出 = B / 我们的判断 = C」的正确标注。
2. **公式逐符号**核对：A∞ 关系 (1.2)、Koszul 符号、`deg μ^d = 2−d`、MC 方程 (3.19)、
   映射锥微分矩阵 (3.28)、Lefschetz 归纳的维数、定理 B 的 directed 性与有限性、变异的三角。
3. **改动最小化**：只改错误字段；`id` 一律未动；`steps[].no` 的编号与顺序一律未动
   （仍为 1..4，未增删步骤）；概念卡与校订卡未触碰；未动 git。

## 2. 逐卡核验

### 2.1 `seidel/deriv/mu-d-grading` — corrected

- **原断言**：由 μ¹ 是微分出发归纳，第 3 步写「为使关系齐次，`deg μ^s + deg μ^{d+1−s} = 2` 对任意 s 成立」，
  第 4 步据此解出 `2−d`；四步全标 A，locator 全为「原书 p.7 §1」。
- **问题**：
  1. `(1.1)` 在 **p.8**，不在 p.7（p.7 只是第一章导言，无 (1.1)）；
  2. 第 3 步的方程本身错：`(1.2)` 中第 d 个关系的项是 `μ^{d−m+1}(…, μ^m(…), …)`，
     复合次数为 `c_{d−m+1} + c_m`，齐次性要求它不依赖 m。取 `m=1` 与 `m=d−1` 得
     `c_d + c_1 = c_2 + c_{d−1}`，即 `c_d = c_{d−1} + c_2 − c_1`；
     而原卡写的 `c_s + c_{d+1−s} = 2` 在 `s=1` 时给出 `c_d = 1`，与 d≥2 矛盾。
  3. `(1.1)` 本身已把目标移位 `[2−d]` 写进定义，因此「归纳证明」实为**自洽性验证**，
     全标 A 属过度声称。
- **改动**：
  - locator 全部 `p.7 §1` → `p.8 §1`；
  - step 1 改述为 (1.1) 的目标移位（保留 A）；step 2–4 转为齐次性归纳（改 B）；
  - step 3 公式改为 `c_d + c_1 = c_2 + c_{d−1}`；step 4 改为 `c_1=1, c_2=0 ⇒ c_d=c_{d−1}−1=2−d`；
  - result 删去 `s^{2−d}μ^d` 的错误指数（suspended 下应为 `s^{d−1}μ^d`），改为「同时成为次数 1 的映射」；
  - gaps 增加「`c_2=0` 须单独取定，归纳只确定到相差常数」；
  - sources `pages [7,8] → [8,9]`，anchor → `原书 p.8 §1`；provenance_note 引 A01-01、A05-08。

### 2.2 `seidel/deriv/twisted-differential` — corrected

- **原断言**：`d_T = d + δ`，平方零 ⇔ δ 满足广义 MC；step 1/2/4 标 A、step 3 标 B。
- **问题**：
  1. `(3.19)`（`Σ_{r≥1} μ^r_{ΣA}(δ_X,…,δ_X)=0`）与 `(3.20)`（TwA 的复合公式）确在 **p.44**，locator 页正确；
  2. 但「把 `d_T = d+δ` 展开成 `d² + dδ + δd + δ²`」**不是原文写法**：
     原文是 `μ¹_{TwA}(a) = d a + Σ μ^{r+2}(δ,…,δ,a,…)`，dg 时才退化为 `d+[δ,·]`；标 A 过强；
  3. p.44 明言「(1.2) 在 TwA 中成立恰好等价于 (3.19)」，这才是该卡结论的原文出处；
  4. provenance_note 引的 **A05-09 是 p.127「上同调含幺的含义」**，与本卡无关（误引）。
- **改动**：step 1/2 改 B 并改述为 (3.20) 的展开；step 3 正文直引 (3.19) 与 p.44 那句等价性（保留 B）；
  step 4 保留 A；gaps 增加「`d_T=d+δ` 只在 μ^{≥3}=0 时成立」；provenance_note → A01-02。

### 2.3 `seidel/deriv/mapping-cone` — corrected

- **原断言**：`f:X→Y` 是「次数 1 的闭态射」，`δ^{1,0}=f`，`X_0=Y, X_1=X`，
  滤过 `F^0=Y⊕X, F^1=X`，矩阵 `[[d_Y,f],[0,d_X]]`；四步全 A，locator p.35 §3e。
- **问题**：
  1. 次数错：`(3e)`（p.35）与 `(3p)`（p.48）都要求 c 是 **degree zero cocycle**；
     次数 1 的是它的移位 `S(c) ∈ hom¹(SY_0, Y_1)`；
  2. 方向错：`δ^{1,0}: X_0 → X_1` 而 `X_0=Y, X_1=X`，于是 δ^{1,0} 是 `Y→X`，与 `f:X→Y` 矛盾；
  3. 矩阵块位置错：`(3.28)` 为 `C = SY_0 ⊕ Y_1`、`δ_C = [[S(δ_{Y_0}), 0], [S(c), δ_{Y_1}]]`，
     非零块在**左下**；原卡按 `(Y,X)` 顺序写 `[[d_Y,f],[0,d_X]]`，与原文分块顺序不符；
  4. locator 指 `(3e)`（抽象锥作为 A∞-模），而「映射锥写成扭曲复形」是 `(3p)`（p.48）；
  5. provenance_note 里「译者注 A05-xx」是**未填的占位符**。
- **改动**：f 改为次数 0；对象改 `X_0=X, X_1=Y, C=SX⊕Y`；`δ^{1,0}=S(f)`，
  矩阵 `[[S(d_X),0],[S(f),d_Y]]`；滤过 `F^0=C, F^1=Y, F^2=0`；step 4 给未移位写法 `[[d_X,0],[f,d_Y]]`；
  locator 全部 → p.48 §3p；sources §3p、pages [48,49]；provenance_note → A02-08、A03-09。

### 2.4 `seidel/deriv/split-generation` — corrected（核心断言错误）

- **原断言**：`TwA` 已经分裂闭；幂等 e 的像 = `Cone(e) = (X⊕X, δ)`，存在 `p∘i=id`、`i∘p=e`；
  result 写「TwA 是分裂闭的；Π(TwA) 与 TwA 在 H⁰ 一致」；locator 全 p.68 §4。
- **问题**（性质错误，不是措辞）：
  1. 若 TwA 已分裂闭，则 `Π` 与 Lemma 4.7（分裂闭包的存在唯一）都失去意义；
  2. p.3 明说分裂闭包是**继扭曲复形之后的第二步**，「introduces formal direct summands of all idempotent endomorphisms」；
  3. p.5 说 `TwB is already split-closed` 是 **B directed** 的特例（定理 B 的构造），不是 Tw 的一般性质；
  4. `Cone(e)` 只在分裂闭包中才是 e 的像；TwA 缺形式直和项，`p∘i=id`、`i∘p=e` 在 TwA 内一般不存在；
  5. p.68–70 属 **§5 Twisting**，不是 §4 Idempotents（§4 在 p.55–63）。
- **改动**：整卡改写为正确陈述：
  - step 1：TwA 三角但不分裂闭，分裂闭包要再取一步（p.3）；
  - step 2：分裂闭定义 (4c) 与「A 分裂闭 ⇔ H⁰(A) 分裂闭」（p.59）；
  - step 3：Lemma 4.7 + `B=Π(TwA)`、`H⁰(B)=D^π(A)`（p.59–60）；
  - step 4：Cor 4.9 的 split-生成判别法（p.60）；
  - result：TwA 一般非分裂闭；Π(TwA) 才是闭包；TwB 分裂闭需 B directed（p.5）；
  - gaps/pitfalls 重写；locator 改 p.3 / p.59 §4c / p.60 §4c；sources §4c、pages [59,60]。

### 2.5 `seidel/deriv/lefschetz-induction` — corrected

- **原断言**：step 1（locator p.303）「X¹ 的 Fukaya 范畴由消失圈生成」；step 2（p.295）
  「V_i 的自同态与相互态射由 PL 数据给出」；step 3「TwB ≃ TwF(X¹)」；四步全 B。
- **问题**：
  1. step 1 的正确出处是 **Prop 19.7（p.298）**，且结论是**消失圈 split-生成 `Π(TwF(M))`**，需 `d≠2`；
  2. step 2 引 p.295 只讲 Lefschetz 铅笔的构造 (19.1)(19.2)，不含「态射由 PL 数据给出」；
     该内容在 §13 (13b)（p.196，多边形计数）与 §19c（PL 数据）；
  3. step 3 的落点漏了 split-闭包：p.303 原文是 `ΠTwF(X¹) ≃ ΠTwA_1 ≃ ΠTwB_1`；
  4. p.303 的 Theorem A 证明只有三句话（Prop 19.7 + Cor 4.9 + Lemma 4.7），原卡把一个步骤拆得过细。
- **改动**：step 1 → Prop 19.7（p.298）+ split-生成 + `d≠2`；step 2 → p.196 §13b；
  step 3 → (19.6) 与 `B_k ⊂ TwB_{k+1,!}`（p.302）；step 4 → `ΠTwA_1 ≃ ΠTwB_1`（p.303）、改 A；
  gaps 增加「Prop 19.7 是硬定理、d=2 失败、n=0 需 (19.7)」；sources pages [298,303]。

### 2.6 `seidel/deriv/theorem-b-construction` — corrected（方向反了）

- **原断言**：`TwB ⊂ F(X)` 是拟等价的全子范畴；step 1–4 locator 全「原书 p.5」；
  step 3「B directed：i>j 时 hom(V_i,V_j)=0」。
- **问题**：
  1. p.5 原文：「one can construct an A∞-category which **contains** a full subcategory quasi-equivalent to F(X)」，
     且「TwB is already split-closed, so it will contain not only F(X), but the whole of Π(TwF(X))」——
     **TwB 是更大的那一边**，原卡方向写反；
  2. 构造在 §19d（p.302）：`A_k=F(V^{k,#})`、`A_{k,!}=F^!(V^{k,#})`、`B_k ⊂ TwB_{k+1,!}`、`B_k ≃ A_k`，
     最后一步用 (19.6) 得 `F(X)` 拟等价于 `TwB_{1,!}` 的某个全子范畴；
  3. p.5 只是定理陈述，不足以支撑四个技术步骤（尤其 directed 性与有限性）。
- **改动**：summary/goal/pitfalls 纠正方向；四步按 §19d 重写（p.302、p.196 §13b、p.287 定理 18.24、p.302）；
  sources §19d、pages [302,303]；保留「B 有限、directed」的结论，但改由 (5n) directed 子范畴 + 临界值排序支撑。

### 2.7 `seidel/deriv/mutation` — corrected（locator 全错）

- **原断言**：四步全 B、locator 全「原书 p.272 §17k」；sources §17k、pages [272,273]。
- **问题**：
  1. **p.272 属 §18**（页眉「18 The Fukaya category of a Lefschetz fibration」），讲 Lemma 18.3/18.4 与
     Dehn twist / 消失圈，没有变异公式；
  2. §17k（The equivariant case）实际从 **p.263** 开始；
  3. 正确出处：Hurwitz 移动 (16.7) 在 **p.226**（§16d）、变异 (5.24) 在 **p.77**（§5j）、
     `Cor 17.17`（Hurwitz 移动 ↔ 变异）在 **p.262**、`(18.29) QΣ^#_{L_kα} ≅ L_k QΣ^#_α` 在 **p.287**；
  4. 原 gaps「变异依赖例外对象的选择」不具体。
- **改动**：四步 locator 改为 p.226 / p.77 / p.262 / p.287，provenance 保持 B→A（各处均原文）；
  step 2 写出 `U_k=T_{Y_k}Y_{k+1}, U_{k+1}=Y_k`；step 4 写出 (18.29)；
  gaps 改为「(18.29) 的严格同构需按 Prop 18.23 选分次；第三映射符号见 Remark 17.19」；
  sources pages [262,287]。

### 2.8 `seidel/deriv/directed-dg` — corrected

- **原断言**：step 1–3 locator p.287 §18、step 4 p.290 §18；step 2「用同伦变换（twisting cochain）
  把 μ^d 吸收到低阶」；result「directed + 有限 ⇒ 可 dg 化且 hom 有限维」。
- **问题**：
  1. Cor 5.27 在 **p.87**（§5p），不在 p.287/p.290（§18 讲 Lefschetz 纤维化，与该结论无关）；
  2. 「twisting cochain 逐对消去」**不是原书论证**：Cor 5.27 的证明是
     「`I(Y_k)` 构成 `P=mod(A^!)` 中的例外聚集，取 associated directed A∞-子范畴；
     P 严格含幺、hom 有限维；A∞-模的高阶复合恒为零」；
  3. p.87 紧接着强调：一般 A∞ 范畴也能换成 dg 范畴（Cor 2.14），
     但**只有 directed 情形能保住 hom 有限维**——这正是本卡的要点，原卡未点出。
- **改动**：四步按 Cor 5.27 的证明重写（p.82 §5n、p.87 §5p ×3）；删去 twisting cochain 说法；
  gaps 改为「dg 模型拟同构意义下唯一；一般情形失去有限维」；sources §5n,§5p、pages [82,87]；
  anchor → `原书 p.87 Corollary 5.27`。

## 3. 外部依据（实际 web_fetch，2026-11-19）

只列真正打开并抄下支持句的页面；nLab 的 `Lefschetz fibration`、`Lefschetz pencil`、`mutation`
三个条目均返回 **404**，故未引用。另抓到 `arxiv.org/abs/math/9909089` 经核实是
Buch《On a conjectured formula for quiver varieties》，与 Seidel 无关，**弃用**。

1. **nLab, "twisted complex"** — <https://ncatlab.org/nlab/show/twisted+complex>
   支持句：`deg(q_ij) = i−j+1`；`∀i,j: dq_ij + Σ_k q_kj∘q_ik = 0`；
   以及微分公式 `df = d_C f + Σ_m (q_jm∘f + (−1)^{l(i−m+1)} f∘q_mi)`。
   用于：`twisted-differential`（MC 方程的形状与 δ 的次数 1）、`mapping-cone`（两项复形的块与次数）。
   注意 nLab 用 `E_i → E_j`、`i−j+1` 的记法，与本书 `δ ∈ hom¹` 同型但符号约定需按 (3.20) 对齐。

2. **nLab, "A-infinity-category"** — <https://ncatlab.org/nlab/show/A-infinity-category>
   支持句：`Every A∞-category is A∞-equivalent to a dg-category.` /
   `This is a corollary of the A∞-categorical Yoneda lemma.`；
   另 `m_n` 为 `degree n−2 (homological grading convention is used)`。
   用于：`directed-dg`——印证「经 Yoneda 引理得到 dg 模型」这一路线确实成立（原书的额外内容是 directed 性保住 hom 有限维）。
   注意：nLab 用**同调**分次 `n−2`，本书用**上同调**分次 `2−d`，两者差一个整体符号，不可直接混抄。

3. **nLab, "exceptional collection"** — <https://ncatlab.org/nlab/show/exceptional+collection>
   支持句：`an exceptional collection of object is a set of objects such that the Ext-groups (hom-spaces)
   between them are concentrated in degree 0. It is a full exceptional collection if in addition it
   generates the category.`
   用于：`mutation`——确认「例外聚集 + 生成」是变异理论的框架；但该页**不含**变异公式，
   变异公式仍只能引原书 (5.24)。

## 4. 交叉发现（页码与引注层面的系统问题）

1. **p.68–70 不是 §4**：这三页属 §5 Twisting（(5.12)(5.13)、Cor 5.7 等）。§4 Idempotents 在 p.55–63。
2. **p.272 不是 §17k**：p.272 属 §18；§17k 从 p.263 开始。
3. **p.7 不是 §1**：§1 从 p.8 开始；(1.1)(1.2) 都在 p.8。
4. **译者注误引**：`twisted-differential` 原引 A05-09，实为 p.127「上同调含幺的含义」；
   `mapping-cone` 原引「A05-xx」是占位符（总表中不存在该 id）。
5. **定理 A/B 的落点**：定理 A 的结论是 `ΠTwF(X¹) ≃ ΠTwA_1 ≃ ΠTwB_1`（p.303），
   定理 B 的结论是 `F(X)` 嵌入 `TwB_{1,!}`（p.303、p.5）。两卡的 `Tw` 与 `Π` 都不能省。

## 5. lint 结果

```
cd C:\Users\admin\Desktop\数译发布\gitee_shuyi\datasets\seidel
C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe tools/lint_cards.py --strict
卡片 70 张（概念 32，推导 8，勘误 30）
OK：0 error，0 warn
```

（本次核验开始时为 65 张；期间有并行工作在补概念卡，故收尾时为 70 张。
8 张推导卡的检查结果与卡片总数无关：0 error、0 warn。）

8 个 JSON 均为 UTF-8、`indent=2`、`ensure_ascii=False`；LaTeX 反斜杠为单层（与数据集其余卡片一致）。

## 6. 仍存疑 / 未解决

1. **`mu-d-grading` 的 `c_2 = 0`**：本卡以「μ² 是次数 0 的乘法」取定，但 (1.2) 的 d=2 关系本身
   给不出这一条（两侧同式）。严格说 `2−d` 是 (1.1) 的定义而非定理；已在 gaps 明写这一点，
   若要求「纯从 (1.2) 推出」则本卡只能标 C。
2. **`twisted-differential` 的 `d_T = d+δ`**：这是 dg 特例的写法，一般情形 `d_T` 含 δ 的任意次插入。
   卡内已注明，但标题式表述（`d_T=d+δ`）仍有轻微误导，未改标题以免改动过大。
3. **`mapping-cone` 的未移位矩阵**：`[[d_X,0],[f,d_Y]]` 是把 `S` 吸收进分块的写法，
   严格说 `f` 应在 `hom¹(SX,Y)`；卡内两个写法并存并注明关系，但读者仍可能混淆。
4. **`split-generation`**：正确的「幂等元在 Π(TwA) 中分裂」的显式构造（用 Yoneda 模/抽象像）
   本卡未展开，只引 Lemma 4.7 的存在性；若需构造性证明，应另开一卡。
5. **`mutation` 的符号**：`Remark 17.19` 自认第三映射的符号未完全验证；(18.29) 的严格同构
   依赖 Prop 18.23 的分次选择。这两点无法从文本层消除，已在 gaps 保留。
6. **`directed-dg` 的 `B^!` 记号**：§5n 的 `A^! = A^!(Y)`（directed 子范畴）与 §5k 的 Koszul 对偶
   记号同形，原书未显式区分；本卡按 §5p「P = mod(A^!)」的上下文理解为前者，若按后者读则论证不成立。
7. **外部依据覆盖不足**：nLab 无 Lefschetz fibration / mutation 条目，故
   `lefschetz-induction`、`theorem-b-construction` 两卡只能靠原书自证（evidence 为空）。

## 7. 产出清单

- 卡片（8 个，已改）：`datasets/seidel/cards/derivations/{mu-d-grading,twisted-differential,mapping-cone,split-generation,lefschetz-induction,theorem-b-construction,mutation,directed-dg}.json`
- 逐卡记录（8 行）：`work/review/verification-derivs.jsonl`
- 本报告：`work/review/report-verify-derivs.md`
