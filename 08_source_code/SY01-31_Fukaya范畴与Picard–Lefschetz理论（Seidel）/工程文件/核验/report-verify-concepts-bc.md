# B/C 轨概念卡核验报告

对象：`datasets/seidel/cards/concepts/` 下 10 张概念卡（B 轨 6 张、C 轨 4 张）。
底本：Seidel, *Fukaya categories and Picard–Lefschetz theory*，页码为原书印刷页。
外部依据：Auroux arXiv:1301.7056、Harris arXiv:1102.0517、Maydanskiy arXiv:0906.2224（均经 ar5iv 打开）与 nLab 相应条目；仅引用实际读到的句子。
日期：2026-11-19。

## seidel/concept/exact-lagrangian

- **status**: `corrected`；改动 7 处。
- **核验**: 定义：正合辛流形与 λ|_L=da（p.96 §7a）；定理：正合 L 上无非常值全纯盘（p.99 (7.5)、p.112 §8l）；公式：能量恒等式。
- **外部依据**: <https://ar5iv.labs.arxiv.org/html/1301.7056>；<https://ar5iv.labs.arxiv.org/html/1301.7056>。

核验 p.96 §7a 与 p.99 (7.5)、p.112 §8l。原稿把「Liouville 向量场完备」写进定义（原书只要求紧致带角、负 Liouville 场沿边界严格向内），又声称正合性「让 L 获得分次」（分次需膜结构，见 maslov/brane 卡），并把无盘定理的出处写成 §7。已按原书改写定义、修正 key_point 的逻辑（面积为零排除非平凡盘），定理出处改为 p.99 (7.5) 与 p.112 §8l，并补 §8l 的 sources。带边一句改为「原书默认 L 无边」的说明。

- **存疑/备注**: 原书 §7a 只假设 M 紧致带角、负 Liouville 场沿边界向内，L 闭且不交 ∂M；卡中删去了原稿「Liouville 向量场完备」与「带边 L 需 a|∂L 常数」两处无来源内容。无盘定理由 (7.5) 直接推出，§8l 是书中显式落点。

## seidel/concept/floer-complex

- **status**: `corrected`；改动 9 处。
- **核验**: 定义：CF*、μ1 与定向线（p.181 (12.16)–(12.18)）；定理：μ1∘μ1=0（p.182）；符号与 char K 约定（§8 与 §12 的区别）。
- **外部依据**: <https://ncatlab.org/nlab/show/Fukaya+category>；<https://ar5iv.labs.arxiv.org/html/1301.7056>。

核验 p.181 (12.16)–(12.18) 与 p.179–182 §12e–f。原稿对象只写「紧致 Lagrangian、横截」，却使用膜结构给出的定向线 o_x，并把 μ1 的计数条件写成「μ(x)=1」（应为 Maslov 指标差 1）；定理出处停在 §8，而 §8 是 char 2 无符号版。已把对象改为紧致正合 Lagrangian 膜、计数条件改为指标差 1、定理与符号约定改引 §12e–f，并补充 §12 sources。

- **存疑/备注**: 原书 §8 是 char K=2 的简化版（无符号、无分次）；带符号的 μ1 与定向线在 §12e–12f，卡按 §12 表述并补出处。μ1=(−1)^{|a|}∂ 的符号约定（§12g）未展开。

## seidel/concept/maslov-index

- **status**: `corrected`；改动 17 处。
- **核验**: 定义：Maslov 指标与平方相位分次（p.157 §11e、p.169 §11j）；定理：分次存在当且仅当 μ_L=0；n=1 与 n=2 的 π1/π2 情形（p.157 (11.23)）。
- **外部依据**: <https://ncatlab.org/nlab/show/Maslov+index>。

核验 p.157 §11e、p.169 §11j 与 p.171。原稿有三类问题：定理证明的 why 字段混入 BEL 控制字符；分次定义用未归一化的 det²；定理写成「存在分次 iff [dα]=0」，用被定义对象定义自身。已清除控制字符、改用 α_V=ϑ²/|ϑ|² 的平方相位、把障碍改为 Maslov 类 μ_L∈H¹(L;Z)，并修正 n=1 的错误断言（n=1 时 Gr(V)≅S¹，π1 仍由 Maslov 指标给出）。

- **存疑/备注**: 原稿两处 why 字段含 BEL 控制字符（\u0007lpha），已清除。分次定义改用 (11.34) 的归一化平方相位；障碍陈述改为 μ_L=0，不再循环地用 [dα]=0 定义自身。n=1 时 Maslov 仍给出 π1≅Z，原稿「n=1 时 Maslov 指标退化、定理 A 排除 n=1」不成立（Theorem A 前提为 d≠2, n≥1, char K≠2）。交叉形式 σ_t 的显式定义 (11.5) 未在卡中展开。

## seidel/concept/determinant-line

- **status**: `corrected`；改动 14 处。
- **核验**: 定义：det(D)=Λ^top(coker D)^∨⊗Λ^top(ker D)（p.149–150 §11a）；公式：det(D1⊕D2) 与 Koszul 符号（11.1–11.2）；定理：定向与带符号计数。
- **外部依据**: <https://ncatlab.org/nlab/show/determinant+line+bundle>。

核验 p.149–150 §11a 与 (11.2)。原稿定义把两个因子次序写成 ker⊗(coker)^∨，与原书 (coker D)^∨⊗ker D 差 Koszul 符号；定理 step 2 写「零维时 ker D=0」，漏掉正则性；pitfall 又称漏掉 coker 对偶会「使次数与定向都错」，与原书「dualizing the cokernel is redundant」相反。已按原书次序改写并说明交换只差 Koszul 符号，step 2 补「零维且正则」，pitfall 改为对偶冗余的说明，公式补 (11.2) 的符号。

- **存疑/备注**: nLab 把对偶放在 kernel 上，与 Seidel 的 (coker D)^∨⊗ker D 整体互为对偶，只作「行列式线由 kernel/coker 最高外幂构成」的结构旁证。原书 p.150 明说「dualizing the cokernel is redundant」，原稿「漏掉对偶会使次数与定向都错」与此相反，已改。零维点步骤补上「正则」前提（正则⇒coker=0，index=0⇒ker=0）。

## seidel/concept/brane-structure

- **status**: `corrected`；改动 15 处。
- **核验**: 定义：膜结构 (α#,P#) 与平方相位（p.169–170 §11j、p.174 §12a）；抽象膜空间 Gr(V)^#→K(Z,1)×K(Z/2,2)（p.163 (11.22)）；定理：膜结构给出整数分次（p.179–182 §12e–f）。
- **外部依据**: <https://ncatlab.org/nlab/show/Pin+group>。

核验 p.163 (11.22)、p.166–169 §11i、p.169–171 §11j 与 p.174。原稿把 K(Z,1) 写成 K(Z/1)（分类空间记号错误），把「n≥3 时 2-连通」说成对所有 n，并把 Pin 结构与 char K 绑在一起；定义中还把膜结构写成与相位无关的 (α,P)。已改为 (α#,P#)（含 e^{2πiα#}=α_M(TL) 与 TL 的 Pin 结构）、K(Z,1)×K(Z/2,2)、n≥3 的限制，并删去 char K 与 Pin 的错误关联；另把 n=1（π1=Z/2、π2=0）与 n=2（π1=0、π2=Z）分开写清，并说明 char 2 只是符号消失、并不退回 §8 的无分次版本。

- **存疑/备注**: 原稿把抽象膜空间写成 K(Z/1)×K(Z/2,2)（应为 K(Z,1)），称 Gr(V)^# 一概 2-连通（仅 n≥3），又称 char K≠2 时 Pin 才保证定向（Pin 是 O_n 的 Z/2 中心扩张，与系数域特征无关）。已改 K(Z,1)、n≥3、Pin 与 char 无关；障碍写为 μ_L 与 w2(TL)。一般 n≤2 的 (11.23) 拓扑与 Pin 分类细节未展开。

## seidel/concept/fukaya-category

- **status**: `corrected`；改动 8 处。
- **核验**: 定义：对象与 μ^d（p.174 §12a、p.183–184 §12g）；定理：A∞ 关系（§9 初步版、§12g 完整版）；公式：μ^d 次数 2−d。
- **外部依据**: <https://ncatlab.org/nlab/show/Fukaya+category>。

核验 p.113–120 §9 与 p.183–185 §12g。原稿对象写「带膜结构的紧致 Lagrangian」，但未提正合性与 2c1(M)=0，而 §12 的对象是 exact Lagrangian branes；公式里张量因子次序与定义文字不一致；证明 step 1 把 Kontsevich 拼成「Konsevich」。已补 2c1(M)=0 与「正合」，统一 μ^d 的因子次序，改正拼写，并把定理出处补到 §12g。

- **存疑/备注**: §9 的 F(M)^pr 对象是 exact Lagrangian（无膜结构、char 2、ungraded）；卡按 §12 的完整版写，并补 2c1(M)=0。原稿证明 step 1 把 Kontsevich 拼成「Konsevich」，已改。

## seidel/concept/lefschetz-fibration

- **status**: `corrected`；改动 16 处。
- **核验**: 定义：exact Lefschetz fibration（p.216 §15d）；局部模型 Q(x)=x_1²+…+x_{n+1}²（p.217 (15.9)）；定理：临界纤维单节点；维数约定：dim_C E=n+1，纤维 2n。
- **外部依据**: <https://ar5iv.labs.arxiv.org/html/1102.0517>；<https://ar5iv.labs.arxiv.org/html/0906.2224>。

核验 p.216–217 §15d 与 (15.9)。原稿的维数约定自相矛盾：notation 说「n=dim X−1 是纤维维数」，局部模型却只写 n 个平方，pitfall 又说纤维实 2(n−1) 维。已统一为原书约定：总空间 E^{2n+2}、纤维复维数 n（实 2n）、局部模型 z_1²+…+z_{n+1}²；并在定义中补上「π 在临界点外是淹没」这一原书前提，定理补上「每条纤维至多一个临界点（仅为方便）」的前提，修正消失球面维数为 n。

- **存疑/备注**: 原稿同时写「n=dim X−1 是纤维维数」「局部模型 n 个平方」「纤维实 2(n−1) 维」，三者互相矛盾。按原书 §15d 统一为：E^{2n+2}→S，n 为纤维复维数，局部模型 n+1 个平方，纤维实维数 2n。

## seidel/concept/vanishing-cycle

- **status**: `corrected`；改动 15 处。
- **核验**: 定义：消失路径与消失圈（p.221 §16b）；定理：消失圈是 Lagrangian S^n 且自动正合（p.221–223）；公式：V_γ=∂Δ_γ 与 monodromy。
- **外部依据**: <https://ar5iv.labs.arxiv.org/html/1102.0517>。

核验 p.221–223 §16b。原稿把 vanishing path 说成「简单环路」（应为嵌入道路，γ⁻¹(Critv)={1}），球面维数写作 S^{n−1} 且 notation 用「n−1=dim_C X−1」，与 thimble 卡的 D^n/S^{n−1} 约定冲突；pitfall 还含繁体「兩」与混乱表述。已改为以 V_γ=∂Δ_γ 定义、平行移动极限作等价刻画，统一 n=dim_C E−1 与 S^n，并清理 pitfall。

- **存疑/备注**: 原书以 V_γ=∂Δ_γ 定义消失圈，(16.2) 的平行移动极限是等价刻画；原稿却把 γ 说成「简单环路」，并以极限作定义。维数按原书 n=dim_C E−1 统一为 S^n。

## seidel/concept/matching-cycle

- **status**: `corrected`；改动 25 处。
- **核验**: 定义：匹配路径与匹配圈（p.230 §16g）；定理：匹配圈是 E 中的 Lagrangian S^{n+1}；公式：Σ_γ=Δ^-_γ∪Δ^+_γ。
- **外部依据**: <https://ar5iv.labs.arxiv.org/html/1102.0517>。

核验 p.230–231 §16g。原稿把匹配圈定义为纤维中两个消失圈在交点粘合（M_γ=V_{γ1}∪V_{γ2}）、说它是 thimble 的边界、维数 n−1，并把出处写到 §16c–16d / p.224–228。按原书应为：γ:[−1,1]→int(S) 连接两个临界值，Σ_γ=Δ^-_γ∪Δ^+_γ⊂E 是两个 thimble 沿公共消失圈粘成的 Lagrangian S^{n+1}，匹配条件是 V± 作为 framed exact Lagrangian spheres 同痕。已重写定义、key_points、公式、定理、pitfalls 与出处。

- **存疑/备注**: 原稿核心错误：把匹配圈写成纤维中两个消失圈的并 M_γ=V_{γ1}∪V_{γ2}，并说它是 thimble 的边界。原书 p.230 的 Σ_γ=Δ^-_γ∪Δ^+_γ 是总空间 E 中两个 thimble 沿公共消失圈粘成的 Lagrangian 球面。一般情形 Σ_{γ,I} 依赖匹配同痕 I；Remark 16.11 只在高维用 Prop 18.21/18.13 说明与 I 无关。

## seidel/concept/thimble

- **status**: `corrected`；改动 17 处。
- **核验**: 定义：Lefschetz thimble（p.221 §16b）；定理：thimble 是 Lagrangian (n+1)-球；公式：∂Δ_γ=V_γ≅S^n。
- **外部依据**: <https://ar5iv.labs.arxiv.org/html/1102.0517>。

核验 p.221–223 §16b。原稿把 thimble 写成 D^n、边界 S^{n−1}（n=dim_C X），与消失圈卡的 S^{n−1} 约定一起偏离原书；source 又落在 §16f 的 p.229–231。已统一为 Δ_γ≅D^{n+1}、∂Δ_γ=V_γ≅S^n（n=dim_C E−1），定义改用「E 中唯一嵌入的 Lagrangian (n+1)-球，π(Δ_γ)=γ([0,1])、π(∂Δ_γ)={γ(0)}」，出处改 §16b，并把「匹配圈是两个消失圈的并」的错误 pitfall 改为两 thimble 粘合。

- **存疑/备注**: 原稿方向基本正确（T_γ 为全空间中的 Lagrangian 盘、∂T_γ=V_γ），但用 n=dim_C X 约定写成 D^n/S^{n−1}，且 source 落在 p.229–231（§16f grading issues），实际定义在 §16b pp.221–223。已统一为 (n+1)-球/S^n 并改出处；唯一性/存在性证明未展开。

