# Seidel《Fukaya categories and Picard–Lefschetz theory》A 轨概念卡核验报告

- 核验范围：6 张 A 轨概念卡（`cards/concepts/` 下 a-infinity-algebra、a-infinity-category、twisted-complex、karoubi-envelope、split-generation、exact-triangle）
- 权威底本：原书英文文本层 `work/en/pages/pNNN.txt` + 页面图像 `work/pages/pNNN.png`（p.8 的 A∞ 关系已用 `p008.png` 逐符号核对，文本层多处符号错序，只用于定位）
- 外部依据：nLab 对应条目，均为本机 `web_fetch` 实际打开（HTTP 200），引文见 `verification-concepts-a.jsonl`，accessed 2026-11-19
- 记录文件：`work/review/verification-concepts-a.jsonl`（6 行）；改动前原件备份在 `work/review/orig-backup/`
- lint：`tools/lint_cards.py --strict` → **0 error，0 warn**

## 总览

| 卡 | status | 改动数 | 主要问题 |
| --- | --- | --- | --- |
| a-infinity-algebra | corrected | 7 | A∞ 关系用了别家的 `(-1)^{r+st}`；Leibniz 规则符号与本书 bar-convention 不符；符号出处误记为 p.11 |
| a-infinity-category | corrected | 6 | 把「非含幺」写成「只要求同伦含幺」；复合顺序说反；opp 符号名 `†` 应为 `✻_d` |
| twisted-complex | corrected | 10 | MC 方程下标 `Tw A` 应为 `†A`；映射锥特例的 `δ^{ji}` 指标与滤过层号错位 |
| karoubi-envelope | corrected | 3 | 定理陈述从「有核（像）」改为「幂等分裂」；anchor 与 pages 不一致 |
| split-generation | corrected | 10 | 定理把推论 5.7/5.8 的前提结论整体写错（「逐次扭转最终为零 ⇒ 分裂生成」），且 source 页码 p.60 应为 p.70 |
| exact-triangle | corrected | 9 | 公式里用了抽象三角范畴没有的 `H^i`；TR1 缺恒等三角；长正合列定理的证明跳步却标 complete |

---

## 1. a-infinity-algebra（`seidel/concept/a-infinity-algebra`）

**核了什么**：原书 p.8 (1.1)(1.2)(1.3) 的定义与符号；`p008.png` 页面图像确认 (1.2) 写作 `∑_{m,n} (-1)^{✻_n} μ_A^{d-m+1}(…, μ_A^m(…), …)=0`，`✻_n=|a_1|+…+|a_n|-n`，`n` 是内层运算**右侧**的元素个数；p.9 Remark 1.1(iv) 与 (1.6) 再次确认这套 bar-convention。

**结论**：定义骨架、次数 `2-d`、`μ^{≥3}` 度量结合律失效的说法都对；错的是符号。

**改了哪里**：
- `definition.text`、`formulas[0]`：`(-1)^{r+st}` → `(-1)^{⋆_r}`，`⋆_r=|a_1|+⋯+|a_r|-r`，并在 `definition.notation` 补 `⋆_r` 的定义（原文缺）。
- `formulas[1]`：`μ¹μ²=μ²(μ¹⊗id)+(-1)^{|a|}μ²(id⊗μ¹)` → `μ¹μ²(a_2,a_1)=(-1)^{|a_1|}μ²(μ¹a_2,a_1)-μ²(a_2,μ¹a_1)`。已用 p.8 的 dg 特例 `∂a=(-1)^{|a|}μ¹_A(a)`、`a_2a_1=(-1)^{|a_1|}μ²_A(a_2,a_1)` 双向验算一致。
- `theorems[0].proof.steps[2].why`：同步改成用 `⋆_r` 定符号。
- `pitfalls[1]`：`本书用 † 记账（原书 p.11）` → bar-convention，出处改为 p.9 注 (iv)（p.11 讲的是自然变换，与符号无关）。
- `pitfalls[2]`：补 Remark 1.1(i) 原话「non-unital 应读作 not necessarily unital」。

**仍存疑**：无实质存疑。唯一可选扩充是补一句「本卡是代数版，不含对象」，未加，属可选项而非错误。

## 2. a-infinity-category（`seidel/concept/a-infinity-category`）

**核了什么**：p.8 (1.1) 的 `hom_A(X_{d-1},X_d)⊗⋯⊗hom_A(X_0,X_1)→hom_A(X_0,X_d)[2-d]` 与 `a_1…a_d` 的编号方向；p.8 opp 公式 `μ^d_{A^opp}(a_d,…,a_1)=(-1)^{✻_d}μ^d_A(a_1,…,a_d)`；p.23 §2 的三层含幺（严格 / 同伦 / c-unital）与其传递关系；p.9 的 `H(A)` 构造。

**结论**：主体正确；三处口径错误（非含幺的含义、复合顺序、符号名），另有一处 gap_note 的数学判断错误。

**改了哪里**：
- `definition.text` 末句：原写「恒等态射不列为数据，只要求它在同伦意义下充当单位元」——把「非含幺」与「同伦含幺」混为一谈。改为「定义不要求恒等态射；原书的非含幺即不必含幺（p.8 Remark 1.1(i)），§2 另分严格/同伦/上同调含幺三个层次」。
- `summary`：同步去掉「恒等态射只在同伦意义下存在」。
- `pitfalls[0]`：`μ² 的第一个变量是靠近源点的态射` 与本书 (1.1) 相反（`a_1` 靠源点、`a_d` 靠终点），已改。
- `pitfalls[1]`：反范畴的 Koszul 符号 `(-1)^{†}` → `(-1)^{⋆_d}`，`⋆_d=|a_1|+⋯+|a_d|-d`（与 p.8 的 `✻_d` 同义）。
- `theorems[0].proof.steps[2].why`、`gap_note`：原 gap_note 说「第 3 步只说明同伦结合；严格结合需要更强假设」——这是错的，`H⁰` 上的复合本就严格结合（`0` 次类符号为 `+1`），缺的只是把带 `μ¹` 的项逐项写成边界的细节。已改为「只引 d=3 关系，逐项化边界从略」。

**仍存疑**：nLab 的 `m_n` 次数写作 `n−2`（下指标/homological 约定），本书用上指标 `2−d`，两者等价，不构成矛盾，但若日后统一索引约定需全库一起动，本卡未改。

## 3. twisted-complex（`seidel/concept/twisted-complex`）

**核了什么**：p.43–44 §3l 的预扭曲复形 `(X,δ_X)`、`δ^{ji}_X=Σφ^{ji}_k⊗x^{ji}_k`、`|φ|+|x|=1`；p.44 (3.19) 的广义 MC 方程；p.45 §3m 关于「严格下三角 = 连接相对滤过的性质」的原话；p.43 (3.16)(3.17) 的 `†A` hom 公式；dg 特例 `d_T=d+q`。

**结论**：构造描述、`q_{ji}` 内部次数 `i-j+1`、`Tw A` 与 `†A` 的分工大体正确；但 MC 方程的下标、以及映射锥特例的 `δ` 指标写错，且证明第 2 步的滤过层号写错。

**改了哪里**：
- `definition.text`、`formulas[0]`：MC 方程下标 `μ^r_{\Tw A}` → `μ^r_{†A}`（p.44 (3.19) 确实是 `†A`），`δ_X∈hom¹_{\Tw A}(X,X)` → `hom¹_{†A}(X,X)`。
- `theorems[0].statement`：`δ^{1,0}=f` → `δ^{0,1}=f`。因为 `δ^{ji}` 由 `X_i` 指向 `X_j`，而 `f:X=X_1→Y=X_0`，正确位置是 `δ^{0,1}`；这样与第 4 步矩阵 `[[d_Y,f],[0,d_X]]`（按 `Y⊕X` 分块）自洽。
- 证明第 1 步：`V⁰→V¹ 的张量因子取次数 0` → `φ^{0,1}:K→K 取次数 0`。
- 证明第 2 步：滤过 `F⁰=X、F¹=V¹⊗X` → `F⁰=V⁰⊗X_0⊕V¹⊗X_1、F¹=V⁰⊗X_0`（原写法层号与 `δ^{ji}` 方向相反，`δ` 并不把 `F⁰` 送入 `F¹`）。
- 证明第 3 步：`dδ=0（f 闭）` → `d_Yf+fd_X=0`（即 `μ¹_{†A}(δ)=0`）；`why` 里「低次项是 dδ+δ²」改为「r=1 给 dδ+δd=0，r=2 给 δ²=0」。
- `key_points[0]`、`pitfalls[2]`：δ 是连接、`d_i=μ¹_{X_i}` 只出现在 `μ¹_{†A}(δ)` 里，总微分是 `d+δ`（原来说「d_i 只是 δ 中 V^i 为一维时的特例」不准确）。

**仍存疑**：卡里把映射锥的 `f` 取成次数 1 的闭态射（而不是 0 次 + 平移），这是原卡自设的特例；数学上仍是合法的扭曲复形（相当于 `S^{-1}Cone(f)`），为保持改动最小未动，但若要与原书 p.35 的抽象映射锥完全对齐，应改写成 0 次 `f` 配 `V²` 的平移。

## 4. karoubi-envelope（`seidel/concept/karoubi-envelope`）

**核了什么**：p.55 §4a 的对象 `(Y,p)` 与 `Hom_{PA}((Y_0,p_0),(Y_1,p_1))=p_1Hom_A(Y_0,Y_1)p_0`（与卡里 `e'fe=f` 等价）；p.56 的「a triangulated structure on A induces one on PA」与 Lemma 4.1；nLab 的 Karoubi envelope 定义。

**结论**：定义与证明的代数部分正确（`q∘i=f²=f=id_{(X,f)}`、`i∘q=f`），不需要改数学内容；改的是陈述口径与页码一致性。

**改了哪里**：
- `summary`：原写「三角范畴的幂等完备化仍是三角范畴，且函子保持三角结构」——书里只说 induces，没有逐字断言函子是 3 函子，措辞收敛为「完备化函子保持三角结构（原书 p.56）」。
- `theorems[0].statement`：`都有核（像）` → `都分裂：q∘i=id_{(Y,p)}、i∘q=f`（与证明里实际算的东西一致）。
- `sources[0].anchor`：`原书 p.3、p.41–56 §4` → `原书 p.3、p.55–56 §4`（与 `pages: [3,56]` 对齐）。

**仍存疑**：完备化函子严格保持殊三角这一点，p.56 只有「induces」一句 + 引 [18]，未逐字写出；卡里已按「保持三角结构」的弱表述处理。

## 5. split-generation（`seidel/concept/split-generation`）

**核了什么**：p.60 §4c 分裂生成的定义原文（最小含 A、对 `H⁰` 中同构封闭、三角且分裂闭的子范畴；「Concretely … forming mapping cones and shifts … finally taking images under all idempotent endomorphisms」）；p.70 §5e 推论 5.7、5.8 的前提与结论；证明用到的 (5.12) 殊三角与 (5.13) 分裂。

**结论**：定义对；**定理整段错**——原卡把「固定的复合 `T_{Y1}…T_{Ym}` 把所有对象送到零 ⇒ 生成且范畴分裂闭」写成了「逐次扭转 `T_S^k(X)` 最终为零 ⇒ 分裂生成」，既漏了 c-有限前提与 `A` 已分裂闭的条件，也把「生成」与「分裂生成」搞混；source 页码 `p.60` 也应为 `p.70`。

**改了哪里**（定理名、陈述、三步证明、gap_note、source，以及 key_points/sources/provenance）：
- `theorems[0].statement`：按 p.70 重写为两级结论（`≅0 ⇒ 生成且 A 分裂闭`；`≅S^δX, δ≠0, A 已分裂闭 ⇒ 分裂生成`）。
- 证明三步改用 (5.12)/(5.13)：殊三角 `X→T_{Y1}…T_{Ym}X→Y→`；复合为零时三角分裂 `X⊕T…X[-1]≅Y`，故 `X` 是直和项；推论 5.8 由重复 `m` 次使 `X→S^{sδ}X` 消失。
- `theorems[0].source`：`原书 p.60、§5` → `原书 p.70 §5e 推论 5.7、5.8（(5.12)–(5.14)）`；`sources[0].pages` `[55,74]` → `[60,70]`；anchor → `原书 p.60 §4c、p.70 §5e`；`key_points[2]` 同步。

**仍存疑**：证明仍是 sketch——原书用八面体公理把 `m` 个锥合并成一个殊三角的细节没有复述；另外「推论 5.7 的结论包含 `A` 分裂闭」这一点书中陈述如此，但卡里只作为并列结论写出，未给出独立论证。

## 6. exact-triangle（`seidel/concept/exact-triangle`）

**核了什么**：p.39 (3h) 三角 `A∞` 范畴的定义（每个态射可补全、每个对象有平移）；p.40 Cor 3.15（前后两个态射复合成零 + 取 `Hom` 得长正合列）；p.41 的分公理归属原话「Corollary 3.17 corresponds to (TR2) … Corollary 3.19 is an incomplete version of the octahedral axiom (TR4)」，并明言公理列表见 [61, Chapter 5]；p.36 (3.8)(3.9) 第三态射 `Z→SY_0` 次数为 1；p.35 (3.6) 抽象映射锥。

**结论**：定义的 TR 编号与 Seidel 口径一致（TR2=旋转、TR3=方块补全、TR4=八面体），不必改；但公式里出现了抽象三角范畴没有的 `H^i`，TR1 漏了恒等三角，且长正合列定理的证明跳步却标 complete。

**改了哪里**：
- `definition.text`：TR1 补「恒等三角 `X→X→0→TX` 是殊三角」。
- `formulas[1]`：无意义的 `⋯→H^i(X)→H^i(Y)→H^i(Z)→H^{i+1}(X)→⋯` → 旋转公式 `(f,g,h) 殊 ⟺ (g,h,−Tf) 殊`。
- `theorems[0].statement`：改为协变/反变两条 `Hom` 长正合列（原只写一条 `H^i` 序列，且抽象范畴里没有上同调对象）。
- `theorems[0].proof.status`：`complete` → `sketch`；第 1 步补「恒等三角 + TR3 补全读中间方块得 `gf=0`」；第 2 步补出反变情形真正的补全方块（`(0,ψ)` 作三角态射、补出 `γ∘g=ψ`）；第 3 步说明协变情形由 TR2 旋转重复得到；`gap_note` 说明未逐项展开完整长链。
- `theorems[0].source`：`原书 p.34–40 §3` → `原书 p.40 Cor 3.15、p.41 §3i`。

**仍存疑**：协变情形只给出「旋转后重复反变论证」的路线，两条长正合列的完整链（含 `T^{±1}` 平移）没有逐项写出，故 proof 降为 sketch——这是六卡中唯一因证明不完整而降级的一处。另：卡里的 TR1–TR4 编号沿用 Seidel 口径，与 nLab 的 TR1–TR5 编号（TR1 恒等三角、TR2 补全、TR3 旋转、TR4 方块、TR5 八面体）不同，为不与 p.41 冲突未改编号，仅在报告里注明。

---

## 外部依据（均为本机 `web_fetch` 实际打开，HTTP 200）

| 卡 | URL | 支撑点 |
| --- | --- | --- |
| a-infinity-algebra | https://ncatlab.org/nlab/show/A-infinity-algebra | A∞ 代数的定义；`D_3` 度量 `D_2` 结合律的失效 |
| a-infinity-category | https://ncatlab.org/nlab/show/A-infinity-category | dg 范畴是 `μ^{≥3}=0` 的特例；`m_n` 的次数约定 |
| twisted-complex | https://ncatlab.org/nlab/show/twisted+complex | `deg(q_ij)=i−j+1` 与 MC 方程 `dq_ij+∑q_kj q_ik=0`；Tw 是预三角化的一步 |
| karoubi-envelope | https://ncatlab.org/nlab/show/Karoubi+envelope | 对象是 `(c,e)`、态射条件 `f∘φ=φ=φ∘e` |
| split-generation | https://ncatlab.org/nlab/show/thick+subcategory | 分裂闭 = 对直和项封闭 |
| exact-triangle | https://ncatlab.org/nlab/show/triangulated+category | `(f,g,−h)` 一般不殊但仍「exact」；TR1 恒等三角 |

## 引文核对

nLab 页面把公式同时输出 LaTeX 与纯文本回退，故 `jsonl` 里的 `quote` 是该句的纯文本写法。落盘后另跑了一次复核（`work/review/check_quotes.py`）：逐条回抓 6 个页面并检索特征子串，12/13 直接命中；唯一不命中的是含 `A∞` 记号的那句（页面写作 `A ∞ A_\infty`，属 MathJax 标记而非文字差异），已换成另一句同样被页面支持、且不含歧义记号的原句。

## 未做的事（遵守最小改动）

- 未改任何 `id`、`related`（全部指向 `index.jsonl` 中存在的卡，lint 已校验）。
- 未动其他 64 张卡、未动 git、未改 `index.jsonl`。
- 未把「仍存疑」的两处（exact-triangle 的协变长正合列、karoubi 的 3 函子性）当作已解决；相应措辞已保守化。
