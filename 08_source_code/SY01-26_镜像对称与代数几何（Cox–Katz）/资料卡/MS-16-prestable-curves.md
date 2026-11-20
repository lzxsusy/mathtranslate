---
id: MS-16
zh: 预稳定曲线与模空间
en: prestable curves and moduli
aliases: [预稳定曲线, 稳定曲线模空间, prestable curve, 稳定化]
layer: L0
prereqs: []
sources:
  - "Cox–Katz 1999, p.192–194（PDF p.192–194）：定义 7.1.1–7.1.2、定理 7.1.3–7.1.4、式 (7.6)–(7.7)"
  - "Cox–Katz 1999, p.202–203（PDF p.202–203）：预稳定曲线叠 $\\mathfrak M_{g,n}$、式 (7.17)、相对与绝对虚拟基本类"
  - "Cox–Katz 1999, p.221–222（PDF p.221–222）：$\\overline M_{0,4}\\simeq\\mathbb P^1$ 与三个边界点"
  - "B 级：Stacks Project『Moduli of Curves』章（叠/DM 性判据）；本书 §7.1 节内索引（预稳定曲线，p.202）"
status: draft
review:
  drafter: agent-221
  reviewer: lead
  blindtest: pending
glossary_refs: [glossary.tsv 行 62（prestable curve → 预稳定曲线）, 行 60（stack → 代数叠）, 行 57（node → 结点）]
symbols_refs: ["$\\mathfrak M_{g,n}$", "$\\overline M_{g,n}$", "$\\overline{\\mathcal M}_{g,n}(X,\\beta)$"]
updated: 2026-11-20
---

# MS-16 预稳定曲线与模空间

## 1. 一句话

带结点、允许不稳定分支的曲线及其模叠，为稳定映射的虚拟基本类提供靶空间。

## 2. 为什么需要它

1. **GW 类需要一个紧的靶空间。** 式 (7.3) 把 GW 类定义为 $\overline M_{g,n}$ 上的上同调类，式 (7.4) 把它积掉（p.191）。只取光滑曲线时映射空间不紧，退化极限必须允许结点曲线，这就是定义 7.1.1 的条件 (i)；而 $\overline M_{g,n}$ 只在 $n+2g\ge 3$ 时存在（p.192），所以还需要一个更大的对象兜住边界。
2. **虚拟基本类需要一个「忘掉映射、不作稳定化」的靶叠。** 式 (7.17) 的 $F:\overline{\mathcal M}_{g,n}(X,\beta)\to\mathfrak M_{g,n}$ 是全部相对构造的入口（p.202）；若把靶换成 $\overline M_{g,n}$，$F$ 没有定义，因为稳定映射的域曲线不必是稳定曲线（p.194）。相对虚拟基本类 $[\overline{\mathcal M}_{g,n}(X,\beta)/\mathfrak M_{g,n},R\pi_{n+1*}e_{n+1}^*\Theta_X]$ 只在这个更大的叠上才有意义（p.203）。
3. **稳定化是一切「忘标记」态射的技术前提。** p.194 用 Knudsen 的技术证明：$n+2g\ge 3$ 时依次收缩不稳定分支后，$\pi_2:\overline{\mathcal M}_{g,n}(X,\beta)\to\overline M_{g,n}$ 是态射；p.221–222 的 $\phi:\overline M_{0,3d}\to\overline M_{0,4}$ 与边界除子关系同样依赖它。

## 3. 定义（全假设）

### 3.1 预稳定曲线

基域 $k=\mathbb C$，$g,n\ge 0$。一条**预稳定曲线**是一个三元组 $(C;p_1,\dots,p_n)$：$C$ 是 $\mathbb C$ 上连通、射影、既约的曲线，算术亏格 $p_a(C)=g$；$p_1,\dots,p_n$ 是 $C$ 上互不相同的有序光滑点，并且

- **(i)** $C$ 的每个奇点都是普通二重点（结点）；
- **(ii)** $p_1,\dots,p_n$ 互不相同、有次序、且均为光滑点。

（(i) 已蕴含既约：结点处 $\widehat{\mathcal O}_{C,x}\cong\mathbb C[[x,y]]/(xy)$。**不假设**有限自同构，即不假设稳定；也不假设不可约。）

**模叠。** $\mathfrak M_{g,n}$ 是 $(\mathrm{Sch}/\mathbb C)$ 上的叠：对象为平坦、固有的族 $\pi:\mathcal C\to S$ 连同 $n$ 个互不相交的截面 $s_1,\dots,s_n$，使每个几何纤维是亏格 $g$ 的预稳定曲线；态射为纤维积方块。按 p.202 原文，它就是「满足定义 7.1.1 条件 (i)、(ii) 的带 $n$ 个标记的亏格 $g$ 曲线的叠」。

### 3.2 稳定曲线与 $\overline M_{g,n}$

在 3.1 之上加**稳定性**：对 $C$ 的每个不可约分支 $C_i$，若 $g_i$ 为其亏格、$n_i$ 为该分支上「标记点 + 结点」的总数，则

$$2g_i-2+n_i>0\qquad(\text{对所有 } i).$$

等价说法：$\mathrm{Aut}(C;p_1,\dots,p_n)$ 有限。$g_i=0$ 时退化为「每条 $\mathbb P^1$ 分支至少 3 个特殊点」，这正是定义 7.1.1 条件 (iii)（常值映射情形）的来源。$n+2g\ge 3$ 时稳定曲线模叠 $\overline M_{g,n}$ 存在，是维数 $3g-3+n$ 的轨形，粗空间为射影概形（p.192，[DM]）；$n+2g<3$ 时它不存在。

### 3.3 稳定化

设 $n+2g\ge 3$ 且 $(C;p_\bullet)$ 预稳定。若某分支满足 $2g_i-2+n_i\le 0$，则 $(g_i,n_i)\in\{(0,0),(0,1),(0,2)\}$，该分支必为 $\mathbb P^1$ 且带 0、1 或 2 个特殊点。反复收缩这类分支（每次把一个 $\mathbb P^1$ 压成一点），得稳定曲线 $\widetilde C$ 与态射 $C\to\widetilde C$，标记点与原标记点一一对应。p.194 的表述是「依次收缩 $C$ 的不稳定分支，就得到稳定曲线 $\widetilde C$」；收缩的唯一性是标准事实（B 级，[Knudsen]），本书未证。

### 3.4 稳定映射（定义 7.1.1，上下文）

$X$ 是 $\mathbb C$ 上射影簇，$\beta\in H_2(X;\mathbb Z)$。**稳定映射**是 $(C;p_1,\dots,p_n;f)$，其中 $f:C\to X$ 是态射、$f_*[C]=\beta$，$(C;p_\bullet)$ 满足 3.1 的 (i)(ii)，且

- **(iii)** 若 $C_i\cong\mathbb P^1$ 是 $C$ 的分支且 $f|_{C_i}$ 常值，则 $C_i$ 至少含 3 个特殊点；
- **(iv)** 若 $C$ 的算术亏格为 1 且 $n=0$，则 $f$ 非常值。

在 (i)(ii) 成立时，(iii)(iv) 等价于 $\mathrm{Aut}(C;p_\bullet;f)$ 有限（p.192）——这正是模空间存在所需的有限性，也解释了 (iii)(iv) 为何长成这样。

### 3.5 本书用法

p.202 只以「满足定义 7.1.1 条件 (i)(ii) 的带 $n$ 个标记的亏格 $g$ 曲线」界定预稳定曲线，未重述连通性与射影性（英文 OCR p.202 同此措辞，非译本笔误）；(iii)(iv) 是稳定映射的额外要求，不是预稳定的条件。记号上本书区分：$\mathfrak M_{g,n}$ = 预稳定曲线叠；$\overline{\mathcal M}_{g,n}(X,\beta)$ = 稳定映射叠；$\overline M_{g,n}$ = 稳定曲线粗模空间。与标准文献（[DM]、[FP]）无实质出入，只是本书不采用 stable reduction 的构造路线。

## 4. 最小例子

### 4.1 预稳定但非稳定的最小点：$(\mathbb P^1;0,\infty)\in\mathfrak M_{0,2}$

$C=\mathbb P^1$，$n=2$，$p_1=0$，$p_2=\infty$：(i) 空（$\mathbb P^1$ 光滑），(ii) 两点互异且光滑，故它是预稳定曲线。但

$$\mathrm{Aut}(\mathbb P^1;0,\infty)=\{z\mapsto az:a\in\mathbb C^*\}\cong\mathbb C^*,\qquad \dim=1,$$

无限群；且 $2g_i-2+n_i=0-2+2=0\not>0$，所以它不是稳定曲线。同时 $n+2g=2<3$，$\overline M_{0,2}$ 根本不存在（p.192）。可见 $\mathfrak M_{g,n}$ 比 $\overline M_{g,n}$ 大得多，多出来的正是被稳定化压掉的点。

### 4.2 $\overline M_{0,4}\cong\mathbb P^1$（queue 指定的可算例子）

1. **维数**：$3g-3+n=0-3+4=1$（p.192）。
2. **参数化**：$\mathrm{PGL}_2$ 在 $\mathbb P^1$ 上三传递，故任意 4 个互异有序点可唯一归一化为 $(0,1,\infty,\lambda)$，$\lambda\in\mathbb C\setminus\{0,1\}$。于是 $M_{0,4}\cong\mathbb P^1\setminus\{0,1,\infty\}$，$\lambda$ 即交比坐标（p.221–222）。
3. **紧化**：在 $\lambda=0,1,\infty$ 处补点。$\lambda\to0$ 时 $p_4\to p_1$，结点把曲线分成 $\{1,4\}|\{2,3\}$；$\lambda\to1$ 时 $p_4\to p_2$，分拆 $\{2,4\}|\{1,3\}$；$\lambda\to\infty$ 时 $p_4\to p_3$，分拆 $\{3,4\}|\{1,2\}$。边界点共 $\tfrac12\binom42=3$ 个（一般公式：$\overline M_{0,n}$ 的边界除子数为 $2^{n-1}-1-n$，$n=4$ 时 $8-1-4=3$），故 $\overline M_{0,4}\cong\mathbb P^1$。
4. **逐支核对稳定性**：每个边界曲线是 $\mathbb P^1\vee\mathbb P^1$，每支带 2 个标记点 + 1 个结点，共 3 个特殊点，$2g_i-2+n_i=0-2+3=1>0$，稳定；每支自同构平凡（3 个特殊点被固定）。
5. **模叠稳定化子**：$\mathrm{Aut}(C;p_1,\dots,p_4)=\{\varphi\in\mathrm{PGL}_2:\varphi(p_i)=p_i\ \forall i\}$。固定 3 个互异点即 $\varphi=\mathrm{id}$，故 4 个互异有序点的自同构群恒平凡，$\overline M_{0,4}$ 是细模空间（概形）、没有轨形点；这与 p.192 称它为「轨形」不矛盾，因为轨形允许平凡稳定化子。
6. **有限数字核对**：$S_4$ 作用在交比上给出 6 个值 $\{\lambda,\ 1/\lambda,\ 1-\lambda,\ 1/(1-\lambda),\ \lambda/(\lambda-1),\ (\lambda-1)/\lambda\}$；$\lambda=-1$ 时化为 $\{-1,2,\tfrac12\}$，$\lambda=\tfrac12$、$2$ 时同理，轨道由 6 缩为 3，对应 2 阶标记置换。但这不是模叠的稳定化子（见 §7 误解 3）。

## 5. 关键性质

| # | 性质 | 出处 | 备注 |
| --- | --- | --- | --- |
| 1 | 预稳定 = 定义 7.1.1 的 (i)(ii)；(iii)(iv) 属稳定映射，不属于预稳定 | p.202；p.192 | 名称最易误解处 |
| 2 | 稳定轨迹 $\overline M_{g,n}\subset\mathfrak M_{g,n}$ 是开子叠；$n+2g<3$ 时为空 | p.192 | 稳定 ⟺ 自同构有限 |
| 3 | $\mathfrak M_{g,n}$ 是 Artin 叠而非 DM 叠：含无限自同构对象 $(\mathbb P^1;0,\infty)$ | p.202；标准事实（B 级） | 故不能对 $\mathfrak M$ 取基本类/相交 |
| 4 | $n+2g\ge3$ 时存在稳定化 $\sigma:\mathfrak M_{g,n}\to\overline M_{g,n}$；$\pi_2$ 是「稳定化」型态射 | p.194；[Knudsen] | 一切忘标记 = 稳定化∘忘点 |
| 5 | 相对虚拟基本类活在双变 Chow 群 $A^*(\overline{\mathcal M}_{g,n}(X,\beta)\to\mathfrak M_{g,n})$，绝对类 $=[\mathfrak M_{g,n}]\cap$ 相对类 | p.202–203，式 (7.17) | $F$ 是全部构造的入口 |
| 6 | $X$ 凸时 $\overline M_{0,n}(X,\beta)$ 具预期维数且 $[\overline M]^{virt}=[\overline M]$；$\mathbb P^r$ 情形 $\dim=dr+r+d+n-3$ | p.193–194；p.203 | 凸 ⟺ 所有亏格 0 稳定映射满足 $H^1(C,f^*T_X)=0$ |

## 6. 推导流程

- **D1** 把「$X$ 里的曲线」换成「带标记曲线 + 映射 $f$」，模空间变为曲线与映射的模空间。依据：p.191–192（§7.1 开篇的 Kontsevich 观点）。
- **D2** 允许结点并为紧性补上 (iii)(iv)，得稳定映射；此时自同构群有限。依据：定义 7.1.1，p.192。
- **D3** 取函子/叠得 $\overline{\mathcal M}_{g,n}(X,\beta)$：粗模空间存在且为射影概形（定理 7.1.3），更精细的版本是固有代数叠（定理 7.1.4）。依据：p.192–193。
- **D4** 只保留 (i)(ii)、忘掉 $f$ 且不作稳定化，得预稳定曲线叠 $\mathfrak M_{g,n}$ 与叠映射 $F$（式 (7.17)）。依据：p.202。
- **D5** $F$ 有内蕴法锥/法层（命题 7.1.6）；将其嵌入由完美障碍理论 $E^\bullet=(R\pi_{n+1*}e_{n+1}^*\Theta_X)^\vee$ 给出的 $h^1/h^0$，得相对虚拟基本类。依据：p.202–203。
- **D6** 与 $[\mathfrak M_{g,n}]$ 相交得绝对虚拟基本类；$X$ 凸时它等于 $[\overline M]$（无需修正）。依据：p.203（定义 7.1.7 及其后）。
- **D7** 用 $\pi_1$（赋值映射）拉回、$\pi_2$（忘点并稳定化）推前，定义 GW 类 $I_{g,n,\beta}=\pi_{2!}\pi_1^*(\cdot)$（式 (7.8)）；积分得不变量（式 (7.9)）。依据：p.194；$\pi_2$ 是态射用 [Knudsen]。
- **D8** 边界情形：GW **类**需 $n+2g\ge3$（$\overline M_{g,n}$ 与 $\pi_2$ 才存在），但 GW **不变量**对 $n,g\ge0$ 都有意义。依据：p.194。

## 7. 常见误解与反例

**误解 1：预稳定曲线就是稳定曲线（或「预稳定」是译本笔误）。** 错：预稳定只要求 (i)(ii)（p.202）。反例即 §4.1，$(\mathbb P^1;0,\infty)\in\mathfrak M_{0,2}$ 的自同构群为 $\mathbb C^*$ 无限；$n+2g=2<3$ 时连 $\overline M_{0,2}$ 都不存在（p.192）。正确说法：预稳定只在结点条件上受约束，稳定化才把它压成稳定曲线。

**误解 2：稳定映射的域曲线必是稳定曲线。** 错，p.194 明说 $C$「不必是 Deligne–Mumford 意义下的稳定曲线」。反例：$X=\mathbb P^1$，$C=\mathbb P^1$，$n=2$，$p_1=0,p_2=\infty$，$f=\mathrm{id}$。定义 7.1.1 的 (iii) 因 $f$ 非常值而空、(iv) 因 $g=0$ 不适用，故它是稳定映射；且 $\mathrm{Aut}(C;p_\bullet;f)=\{\mathrm{id}\}$ 有限（$f=\mathrm{id}$ 迫使 $\varphi=\mathrm{id}$）。但域曲线不稳定（§4.1）。这正是 $F$ 必须忘掉映射而不作稳定化的原因。

**误解 3：$\lambda=-1,\tfrac12,2$ 是 $\overline M_{0,4}$ 的三个轨形点。** 错：这三点来自 $S_4$ 对标记的置换（§4.2 第 6 步），是标记空间的对称，不是模叠稳定化子；$\mathrm{Aut}(C;p_1,\dots,p_4)$ 对 4 个互异有序点恒平凡（PGL$_2$ 三传递，§4.2 第 5 步），故 $\overline M_{0,4}\cong\mathbb P^1$ 是细模空间、无轨形点。轨形现象出现在曲线本身有自同构时（如 $\overline M_{1,1}$ 的 $j=0,1728$）：

$$\mathrm{Aut}(E)\cong\mathbb Z/6\ (j=0),\qquad \mathbb Z/4\ (j=1728).$$

**误解 4：$n+2g<3$ 时 GW 不变量也没有定义。** 错：p.194 说需要 $n+2g\ge3$ 的是 GW **类**（要落在 $H^*(\overline M_{g,n})$ 上），而 GW **不变量**（式 (7.9) 的积分）对 $n,g\ge0$ 都有意义，因为稳定映射叠与虚拟基本类对一切 $n,g\ge0$ 都存在（定义 7.1.1；p.202–203），式 (7.9) 不需要 $\overline M_{g,n}$ 存在。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
| --- | --- | --- |
| Cox–Katz 1999（本书） | p.192–194（§7.1.1–7.1.2）；p.202–203（§7.1.4）；p.221–222（§7.4.2） | 稳定曲线 $\overline M_{g,n}$ 与稳定映射（定义 7.1.1）；预稳定曲线叠 $\mathfrak M_{g,n}$ 与式 (7.17)；相对/绝对虚拟基本类；$\overline M_{0,4}\cong\mathbb P^1$ |
| SY01-24《镜像对称》（Siebert 讲义中译本） | 术语表 #21 叠 p.24；#28 DM 叠 p.35；#30 稳定约化 p.40；#31 稳定映射 p.42；#32 虚拟基本类 p.46 | 术语对照。**冲突**：SY01-24 #21 stack 作「叠」，本书 p.193 起作「代数叠」，按 _冲突表 T3 裁定取「代数叠」（与 DM 叠/Artin 叠的层级区分）。另：SY01-24 走 stable reduction 路线，本书走定义 7.1.1 (iii)(iv)+收缩不稳定分支；SY01-24 无「预稳定曲线」词条（术语缺口），属差异（非冲突） |
| SY01-25《同调镜像对称与环面纤维化》资料卡 | 04-术语文献勘误 §二「极大退化 / 模空间」行（[LTY][Mo][De][Mum][BL]） | **冲突（适用范围）**：其「模空间」指 Hodge 结构的紧化/退化阿贝尔簇模空间，与预稳定曲线叠 $\mathfrak M_{g,n}$ 同名不同对象、适用范围不重叠；按 _冲突表 U4，本卡注明**本书不覆盖 HMS 的辛侧细节**（$A_\infty$-预范畴、Morse 模型只在 SY01-25 出现，本书 Ch.8 仅讲稳定映射与 GW） |
| Deligne–Mumford 1969（[DM]） | Publ. Math. IHES 36, 75–110 | 稳定曲线与 $\overline M_{g,n}$ 的存在性、紧性；本书叠与稳定曲线语言的源头（p.192–193 引用） |
| Knudsen 1983（[Knudsen]） | Math. Scand. 52, 161–199（第 II 篇） | 忘标记/稳定化态射 $\pi_2$ 是态射（p.194 明引）；$\overline M_{g,n}$ 的边界与收缩理论 |
| Behrend 1997（[Behrend]） | Invent. Math. 127, 601–617 | 预稳定曲线叠 $\mathfrak M_{g,n}$、相对虚拟基本类与 $[\mathfrak M]\cap$ 构造（p.202 明引） |
| Behrend–Manin 1996（[BM]） | Duke Math. J. 85, 1–60 | 定理 7.1.4（固有代数叠）与泛稳定映射的存在（p.202 引用） |
| Fulton–Pandharipande 1997（[FP]） | Santa Cruz 1995, PSPM 62 Part 2, 45–96 | $\overline M_{g,n}$ 与 $\overline{\mathcal M}_{g,n}(X,\beta)$ 的显式构造，p.192–193 推荐为入门 |

## 9. 前置与后继

- **前置：** 无（_queue.md 记「—」）。所需最低背景：概形与平坦/固有态射、曲线算术亏格与结点、叠的基本语言（p.193 现场给出 DM 叠与 Artin 叠的用法）。
- **后继：** MS-15（稳定映射与虚拟基本类，直接以 $\mathfrak M_{g,n}$ 与 $F$ 为入口）、MS-05（GW 不变量，用 $\overline M_{g,n}$ 与式 (7.4)）、MS-04（量子上同调）、MS-17（局部化，作用于 $\overline M_{g,n}$ 与 $\overline{\mathcal M}_{g,n}(X,\beta)$）。

## 10. 形式化接口

```lean
-- 只给签名与关键假设，允许 sorry
structure PrestableCurve (g n : ℕ) where
  C : Type u
  [inst : Curve C]                          -- 连通、射影、既约；算术亏格 g
  node : ∀ x : C, IsOrdinaryDoublePoint x   -- 定义 7.1.1 (i)
  pt : Fin n → C
  pt_inj : Function.Injective pt            -- 定义 7.1.1 (ii)
  pt_smooth : ∀ i, SmoothAt (pt i)
  genus_eq : Curve.arithmeticGenus C = g

def PrestableCurve.IsStable (X : PrestableCurve g n) : Prop :=
  ∀ i : ComponentIndex X, 2 * X.genusAt i - 2 + X.specialCount i > 0

-- p.192：n + 2g ≥ 3 时稳定模叠存在、光滑、维数 3g − 3 + n
theorem stable_stack_exists (g n : ℕ) (h : 3 ≤ n + 2 * g) :
    ∃ M : AlgebraicStack, IsDeligneMumford M ∧ IsSmooth M ∧
      stackDim M = 3 * g - 3 + n := by sorry

-- p.202：预稳定曲线叠 𝔐_{g,n} 是 Artin 叠而非 DM 叠
theorem prestable_stack_is_artin_not_dm (g n : ℕ) :
    IsArtinStack (prestableStack g n) ∧ ¬ IsDeligneMumford (prestableStack g n) := by sorry

-- p.194 + [Knudsen]：稳定化态射 σ : 𝔐_{g,n} → M̄_{g,n}
theorem stabilisation_morphism (g n : ℕ) (h : 3 ≤ n + 2 * g) :
    ∃ σ : StackMorphism (prestableStack g n) (stableStack g n), IsStabilisation σ := by sorry

-- p.202–203：忘掉映射 F 与相对/绝对虚拟基本类
def forgetfulMap (X : Scheme) (β : H2 X) (g n : ℕ) :
    StackMorphism (stableMapStack X β g n) (prestableStack g n) := sorry

theorem vfc_absolute_eq_cap_relative (X : Scheme) (β : H2 X) (g n : ℕ) :
    virtualFundamentalClass X β g n =
      chowCap (fundamentalClass (prestableStack g n)) (relativeVFC X β g n) := by sorry
```

## 11. 待核清单

- [ ] _queue.md 表格把 MS-16 记为 L1，而「生产顺序」把 MS-16 列入 L0 批次（MS-03/07/08/10/16）；本卡按用户口径写 L0，需回填 _queue.md。
- [ ] 本书 p.202 以「满足定义 7.1.1 条件 (i)(ii) 的带 $n$ 个标记的亏格 $g$ 曲线」界定预稳定曲线；(i)(ii) 字面不含连通性与亏格，需回到定义 7.1.1 开头「连通的带标记曲线」。英文 OCR p.202 同此措辞（原书表述，非译本笔误），是否加译注待定。
- [ ] 译本索引（chapters/index.tex:1787）在 p.202 处作「预稳定映射」，而正文 chapter07.tex:596 与索引命令（chapter07.tex:302）作「预稳定曲线」；英文 OCR p.202 作 "such curves are called prestable"，倾向正文正确、索引笔误。待核。
- [ ] 冲突回填：SY01-24 术语表 #21「叠」vs 本书「代数叠」（_冲突表 T3 已裁定）；需在术语表下一轮统一措辞。
- [ ] 冲突（适用范围）：SY01-25 卡 04 的「模空间」指 Hodge 结构紧化，与 $\mathfrak M_{g,n}$ 同名不同对象；已按 _冲突表 U4 注明本书不覆盖辛侧，待 lead 确认是否需要并在卡说明。
- [ ] $\mathfrak M_{g,n}$ 的光滑性与局部维数 $3g-3+n$ 未在本书正文给出（本书只给 $\overline M_{g,n}$ 的维数，p.192）；本卡按标准事实（B 级）陈述，待核 [Behrend] §1。
- [ ] 稳定化唯一性（p.194 只说「依次收缩…就得到」）未给证明；本卡按标准事实陈述，待核 [Knudsen]。
- [ ] §4 的 $\mathrm{Aut}$ 与 $S_4$ 计算（含 $\lambda=-1,\tfrac12,2$ 三点、$\overline M_{0,4}$ 无轨形点）为本卡补算，书中未给，待复核。
