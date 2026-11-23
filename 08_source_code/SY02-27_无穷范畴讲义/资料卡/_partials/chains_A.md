# SY02-27《无穷范畴讲义》论证链（A 组，第 1–9 讲）

三条链都从"口号"落到"可算的定义"，并各自标出**缺了哪一步会断**。页码为原书页（每讲重新计页）。

---

## 链一：同伦假设如何变成一个可检验的模型

**问题.** 口号说"∞-群胚的理论 = 同伦论"（SY02-27.stmt.1.3.9，第 1 讲 p3）。但"∞-群胚"若只是一个待定义的名词，这句话就没有内容。要把口号变成数学，必须给出一个组合对象，使"可逆态射"成为可判定的局部条件。

**起点.** SY02-27.concept.homotopy-hypothesis（第 1 讲 p3）给出方向：同伦型由 ∞-群胚承载；SY02-27.concept.infinity-groupoid（第 1 讲 p4）给出内容：一个 ∞-范畴，其 $k$-态射（$k\ge 1$）全部可逆。此时"可逆"仍是待解释的——起点只是把问题挪到了"可逆"上。

**步骤.**

1. **换成单纯集。** 取 SY02-27.concept.simplicial-set（第 3 讲 p1，$\Set_\Delta := \Fun(\Delta^{\mathrm{op}},\Set)$），并用 SY02-27.concept.nerve（第 3 讲 p2，$N_\bullet(\cC) := \Hom_{\Cat}(-,\cC)$）把普通范畴嵌入其中。
   *warrant*：SY02-27.stmt.3.1.4（第 3 讲 p1）断言 $N_\bullet$ 全忠实，故"范畴的数据"在单纯集里没有丢失；这一步让后续的填充条件有载体。

2. **用角填充刻画 Kan 复形。** 引入 SY02-27.concept.horn（第 3 讲 p4，第 $i$ 个角 $\Lambda^n_i$）与 SY02-27.concept.kan-complex（第 3 讲 p6，对全部角包含有右提升性质的单纯集）。
   *warrant*：SY02-27.stmt.3.6.2（第 3 讲 p6，Kan–Quillen 模型结构）把"纤维对象 = Kan 复形"钉死；而角包含同时含内角与外角，正是"所有态射可逆"的局部编码。这一步是整条链的枢纽。

3. **放宽到拟范畴。** 只保留内角条件，得 SY02-27.concept.quasi-category（第 4 讲 p2，Def 1.7：每个内角 $\Lambda^n_i\to X$，$0<i<n$，都可填充）。
   *warrant*：SY02-27.stmt.4.1.7（第 4 讲 p2）给出定义本身；SY02-27.stmt.4.5.3（第 4 讲 p4）证明拟范畴是 Kan 复形 $\iff$ 其所有态射可逆——即 Kan 复形恰是"群胚性"的那一支。于是 ∞-群胚与 ∞-范畴落在同一个组合框架里，只差可逆性。

4. **映回经典同伦论。** 取 SY02-27.concept.homotopy-category-of-quasi-category（第 4 讲 p4，$\mathrm{h}\cC$：对象为顶点、态射为同伦类），并与 SY02-27.concept.fundamental-groupoid（第 1 讲 p5）和 SY02-27.concept.homotopy-type（第 1 讲 p5，$\mathrm{hTop}$ 的对象）对接。
   *warrant*：只有把组合对象送进 $\mathrm{hTop}$，口号才获得可比较的右手边；这一步是"验证"，不是"定义"。

**收口.** 口号 3.9 在模型层面被实例化：Kan 复形 $\leftrightarrow$ ∞-群胚，拟范畴 $\leftrightarrow$ ∞-范畴，二者由"内角 vs 全角"分开（第 3 讲 p6、第 4 讲 p2–p4）。口号 4.20（SY02-27.stmt.1.4.20，第 1 讲 p6，"$n$-groupoids = homotopy $n$-types"）由此获得逐层的对应物。

**反事实.** 缺步骤 2 会断：没有"角填充 $\iff$ 可逆"这一局部刻画，"∞-群胚"就只能停在"所有态射可逆"的循环解释上，步骤 3 的"放宽一个角条件"也无从谈起——链在起点与拟范畴之间断成两截。

---

## 链二：极限的四层刻画（定义—判据—算法—模型）

**问题.** ∞-范畴里的（余）极限要同时满足三件事：有定义、能算、且在模型范畴里算出来的同伦极限与它一致。三者不打通，极限就只是又一个待解释的名词。

**起点.** SY02-27.concept.limit-diagram（第 6 讲 p7，Def 6.1）与 SY02-27.concept.final-object（第 6 讲 p1，Def 2.2：$\Maps_\cC(y,x)$ 可缩）。经典情形下的刻画是"极限图 $\iff$ 切片范畴中的终对象"，本链就是把这句话逐层搬进 ∞-世界。

**步骤.**

1. **切片判据。** 用 SY02-27.concept.slice-infinity-category（第 6 讲 p2，Def 3.3）与 SY02-27.concept.slice-forgetful-functor（第 6 讲 p3）。
   *warrant*：SY02-27.stmt.6.3.11（第 6 讲 p3）断言遗忘函子 $\cC_{/u}\to\cC$ 是等价 $\iff$ $u$ 是极限图。这把"极限"归约成"终对象"，定义问题被消掉一半。

2. **终结性的可计算判据。** 引入 SY02-27.concept.initial-morphism / SY02-27.concept.final-morphism（第 7 讲 p3，Def 3.2）与 SY02-27.concept.conservative-functor（第 6 讲 p3）。
   *warrant*：SY02-27.stmt.7.4.1（第 7 讲 p6，Quillen 定理 A）把终结性化归为 $K'\times_K K_{/x}$ 的弱可缩性；SY02-27.stmt.6.3.15（第 6 讲 p4）保证切片只依赖图的等价类（$u_0\to u_1$ 为同构时 $\cC_{/u_0}\to\cC_{/u_1}$ 是等价），故判据可在同伦论的语言下逐点检验。

3. **逐点算法。** 用 SY02-27.concept.pointwise-limit（第 7 讲 p2）。
   *warrant*：SY02-27.stmt.7.2.14（第 7 讲 p2）断言 $\Fun(B,\cC)$ 中的（余）极限逐点计算；SY02-27.stmt.7.2.11（第 7 讲 p2）保证可表现函子保持并检测所有极限。二者合起来，把任意图上的极限归约到切片上的终对象判定。

4. **模型范畴侧的同伦极限。** 取 SY02-27.concept.homotopy-limit（第 8 讲 p1）与 SY02-27.concept.combinatorial-model-category（第 8 讲 p4）。
   *warrant*：SY02-27.stmt.8.1.2（第 8 讲 p1，HTT.4.2.4.1）断言 $\holim u := \R\lim(u)$ 与 $\mathfrak{N}_\bullet(\cC^\circ)$ 中的极限图一致；SY02-27.stmt.8.2.14（第 8 讲 p5）把 $\holim$ 定义为同伦右 Kan 扩张函子在 $\cJ'=[0]$ 的特例。这一步是从"∞-范畴内"跳到"模型范畴内"的桥：桥两头算的是同一个东西。

5. **Kan 扩张统一。** 用 SY02-27.concept.kan-extension（第 9 讲 p1，Def 1.2）与 SY02-27.concept.pointwise-right-kan-extension（第 9 讲 p3）。
   *warrant*：SY02-27.stmt.9.1.8（第 9 讲 p2，式 (1.3)）给出右 Kan 扩张的逐点公式 $\lim_{K_0\times_K K_{x/}}$；极限即沿 $K_0\to K$ 的右 Kan 扩张在单点处的值。于是步骤 1–4 的四种说法被同一个公式收拢。

**收口.** 定义（切片终对象，第 6 讲 p2–p3）、判据（Quillen 定理 A，第 7 讲 p6）、算法（逐点，第 7 讲 p2）、模型（同伦极限，第 8 讲 p1）与统一（Kan 扩张，第 9 讲 p2）五层闭环，且每层都能回指上一层。

**反事实.** 缺步骤 3 会断：没有逐点公式，步骤 4 的 $\R\lim$ 只能在模型范畴内部自说自话，无法与步骤 1 的切片判据比较——"同伦极限 = ∞-范畴极限"就失去了可验证的接口，链在步骤 2 与 4 之间断裂。

---

## 链三：把 ∞-范畴本身做成一个 ∞-范畴

**问题.** 第 7 讲起大量使用"函子范畴 $\Fun(K,\cC)$ 中的逐点极限"，这要求 $\mathcal{Q}\mathrm{Cat}$ 本身是一个 ∞-范畴，否则"函子性"无家可归。本链说明 $\mathcal{Q}\mathrm{Cat}$ 如何被造出来。

**起点.** SY02-27.concept.nerve（第 3 讲 p2）与 SY02-27.concept.simplicial-model-category（第 8 讲 p4）。$\mathcal{Q}\mathrm{Cat}$ 要同时是"单纯充实范畴"和"拟范畴"，起点因此必须是两套语言的翻译器。

**步骤.**

1. **$\mathfrak{C}\dashv\mathfrak{N}_\bullet$。** 取 SY02-27.concept.c-of-simplex（第 5 讲 p7）。
   *warrant*：SY02-27.stmt.5.6.8（第 5 讲 p7，HTT.2.2.5.1/5.8）断言 $\mathfrak{C}:\Set_\Delta\rightleftarrows\Cat_\Delta:\mathfrak{N}_\bullet$ 是 Quillen 等价。这一步让"单纯范畴"与"单纯集"互为翻译，$\mathcal{Q}\mathrm{Cat}$ 的两种身份有了统一的语言。

2. **Joyal 模型结构。** 用 SY02-27.concept.joyal-model-structure（第 5 讲 p4）。
   *warrant*：SY02-27.stmt.5.4.10（第 5 讲 p4，Joy08 Thm 6.12）存在该模型结构；SY02-27.stmt.5.4.6（第 5 讲 p4，Joy08 Cor 2.29）断言任一内角包含 $\Lambda^n_i\hookrightarrow\Delta^n$ 是范畴等价（即弱等价加余纤维化）。于是"纤维对象 = 拟范畴、弱等价 = 范畴等价"成立。

3. **$\mathcal{Q}\mathrm{Cat}$ 的单纯充实。** 取 SY02-27.concept.homotopy-category-of-qcat（第 5 讲 p2）与 SY02-27.concept.equivalence-of-quasi-categories（第 5 讲 p2）。
   *warrant*：SY02-27.stmt.5.2.3（第 5 讲 p1，可逆 $\iff$ 逐对象为同构）与 SY02-27.stmt.5.3.4（第 5 讲 p2，等价 $\iff$ 全忠实 + 本质满）把"同构/等价"降到对象层可检验；于是可取 $\Hom_{\mathcal{Q}\mathrm{Cat}}(\cC,\cD) := \Fun(\cC,\cD)^{\simeq}$（核心 Kan 复形），得到单纯充实范畴 $\mathcal{Q}\mathrm{Cat}$，其 $\pi_0$ 与模型范畴的同伦范畴一致（对照 SY02-27.stmt.2.2.19，第 2 讲 p5）。

4. **$\mathcal{Q}\mathrm{Cat}$ 是拟范畴。** 用 SY02-27.concept.homotopy-coherent-commutative-diagram（第 5 讲 p8）与 SY02-27.concept.quasi-categorical-localization（第 5 讲 p9）。
   *warrant*：SY02-27.stmt.5.6.11（第 5 讲 p8，Ker.01LE）给出纤维单纯范畴与拟范畴的对应；SY02-27.stmt.5.9.3（第 5 讲 p9）给出沿 $W$ 的局部化；附 A 的 Thm A.3（第 5 讲 p10）收口为 $\mathfrak{N}_\bullet(\mathcal{Q}\mathrm{Cat})\to\mathcal{Q}\mathrm{Cat}$ 展示 $\mathcal{Q}\mathrm{Cat}$ 为拟范畴。

**收口.** $\mathcal{Q}\mathrm{Cat}$ 自指成立（第 5 讲 p10，Thm A.3），于是第 7 讲"函子范畴中逐点算极限"（SY02-27.stmt.7.2.14，第 7 讲 p2）与第 9 讲的 Kan 扩张公式（SY02-27.stmt.9.1.8，第 9 讲 p2）都有了严格的落脚点：它们说的都是 $\mathcal{Q}\mathrm{Cat}$ 内部的（余）极限。

**反事实.** 缺步骤 2 会断：没有 Joyal 模型结构，"纤维对象 = 拟范畴"无定义，步骤 3 的 $\Hom$ 空间无从取（$\Fun(\cC,\cD)^\simeq$ 的核心依赖于 $\Fun$ 是拟范畴），步骤 4 的局部化也失去模型范畴基础——$\mathcal{Q}\mathrm{Cat}$ 只能退化为普通范畴，链在步骤 1 与 3 之间断裂。
