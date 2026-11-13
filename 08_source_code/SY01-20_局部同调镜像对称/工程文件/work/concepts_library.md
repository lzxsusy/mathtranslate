# 概念库（供译手写 conceptbox，中文）

> 使用说明：每条给 3–6 句中文（定义 / 直觉 / 本文何处需要），末行给「参考」。译手可摘取其中
> 2–4 句放进 `\begin{conceptbox}{概念名} ... \end{conceptbox}`，务必保留可信来源。
> 标 ✔ 的 nLab 条目已由 Lead 实测检索到（2026-11-13）；标 ✘ 的是 nLab 上未找到条目、改引
> 权威文献的情况，不要写成「nLab 有此条目」。

## 对数光滑结构与对数爆破（log smooth structure, log blow-up）✔
对数结构是在概形上额外记录一个「边界除子」的层论数据（一个含乘法幺半群的层），使得只在
边界附近退化、内部光滑的几何也能用光滑的语言处理；对数爆破是沿对数结构的理想做爆破，
爆破后代数簇上的边界除子被换成更细的对数结构，而**内部不变**。它在本文中的作用是：把
环簇退化的中心纤维（边界）与一般纤维联系起来，使「沿边界做手术」不改变与 A 模型的关系。
参考：nLab, *logarithmic geometry*（ncatlab.org/nlab/show/logarithmic+geometry）。

## 环簇退化（toric degeneration）
一族代数簇 $X_t\to\mathbb{A}^1$，其一般纤维是光滑的，中心纤维 $X_0$ 是若干环簇沿边界粘成的
「热带式」退化体；$X_0$ 的组合数据（扇、多面体复形）记录了 $X_t$ 的单值性。镜像对称的
Gross–Siebert 纲领正是把 $X_0$ 的扇数据当作 B 侧输入，去搭 A 侧的镜像。
参考：Gross–Siebert, *Intrinsic mirror symmetry*, arXiv:1909.07649, §1–2。

## 环簇与扇（toric variety, fan, moment polytope）✔
环簇是含代数环面 $(\mathbb{G}_m)^n$ 作为稠密开子集的代数簇，完全由其**扇**（格 $N$ 中带
多面体锥的集合）决定：锥 ↔ 仿射开集，扇的公共加细 ↔ 共同加细覆盖。紧环簇对应完备扇，
其矩映射下的像是多面体。本文的线丛、环面丛、Hirzebruch 面都是环簇（或环面纤维化）。
参考：nLab, *toric variety*（ncatlab.org/nlab/show/toric+variety）；Fulton, *Introduction to Toric Varieties*。

## Hirzebruch 面（Hirzebruch surface $F_n$）
$F_n=\mathbb{P}(\mathcal{O}_{\mathbb{P}^1}\oplus\mathcal{O}_{\mathbb{P}^1}(n))$，是 $\mathbb{P}^1$ 上的
$\mathbb{P}^1$-丛；$n$ 与 $-n$ 给出同构，故只依赖 $|n|$。$F_0=\mathbb{P}^1\times\mathbb{P}^1$，
$F_1$ 是 $\mathbb{P}^2$ 的爆破。不同的 $|n|$ 给出不同的复结构，却在辛意义下互相形变，
这正是本文 §1c 用它构造「异域 Weinstein 结构」的原因。
参考：Hartshorne, *Algebraic Geometry*, V.2；本文 §1c。

## 映射柱（mapping cylinder, $M(X,\phi)$）
给定流形/范畴 $X$ 与自同构 $\phi$，映射柱是把 $X\times[0,1]$ 的两端用 $\phi$ 粘起来得到的
对象：空间情形 $M(X,\phi)=X\times_\phi S^1$，范畴情形是 $\phi$ 的映射环面（mapping torus）。
本文的 $M(X,\phi)$ 是 $X$ 与 $\phi$ 的映射柱的复化/辛化版本 $X\times_\phi\mathbb{C}^*$，其上
有坐标 $z$，停止位取 $z+\frac1z=c$ 的两条纤维，正是为了让绕 $S^1$ 一周的单值性恰好是 $\phi$。
参考：Kartal, *Wrapped Fukaya categories of mapping tori*, arXiv:2204.04928（本文引文的 Kartal 修改）。

## 停止位与部分包裹 Fukaya 范畴（stop, partially wrapped Fukaya category）
在带边 Weinstein 流形 $W$ 的边界上取一个闭子集（停止位，stop）$\mathfrak{f}$，只允许
Reeb 流沿边界跑到 $\mathfrak{f}$ 时「停住」，由此得到的 Fukaya 范畴比全包裹版本小、
比紧支版本大，称为部分包裹 Fukaya 范畴 $\mathcal{W}(W,\mathfrak{f})$。停止位的选取控制着
哪些无穷远处的 Reeb 轨道被算进来，因此可以「设计」出某个特定的镜像范畴。
参考：Sylvan, *On partially wrapped Fukaya categories*, arXiv:1601.05080；Ganatra–Pardon–Shende, arXiv:1712.09126。

## 扇形下降与真下降（sectorial descent, proper descent）
把辛流形切成若干 Weinstein 扇形（sector），在扇形上分别构造 Fukaya 范畴，再沿公共边界
用限制函子粘起来——这就是扇形下降；「真」下降要求粘合图表在范畴层面是真正的（同伦）
极限而不是弱极限。本文用它把多个 $\mathbb{P}^1$ 沿节点粘成的链的 A 模型从单块拼出来。
参考：Ganatra–Pardon–Shende, arXiv:1712.09126, §2；本文 §1b。

## 反常 Schober（perverse Schober）✔（perverse sheaf 部分）
Schober 是「反常层」的范畴化：把每个开集上的反常层换成 dg 范畴、把限制/推出函子换成
函子，得到球面上的球状函子（spherical functor）配置。它与「沿节点粘合」的 A 模型一一对应，
是本文处理多单值性时反面（B 侧）的粘合语言。
参考：nLab, *perverse sheaf*；Kapranov–Schechtman, *Perverse Schobers*, arXiv:1411.2772。

## 单值性与 Dehn 扭转（monodromy, Dehn twist）
沿一个环路走一圈回到原处时，纤维被一个自同构（单值变换）作用；在辛几何中，环绕一个
Lagrangian 球面的单值变换就是 Dehn 扭转（twist）。本文的 $\phi$ 是镜像自同构，绕 $S^1$
一周的单值性由它给出；A 侧的 Dehn 扭转与 B 侧的 $-\otimes L^{-1}$ 互为镜像。
参考：Seidel, *Fukaya Categories and Picard–Lefschetz Theory*, §16–17。

## Künneth 公式与扭 Künneth 公式（Künneth, twisted Künneth）✔
Künneth 公式说：两个空间的（上）同调的张量积给出乘积空间的上同调；在范畴层面则是
$\mathrm{Perf}(X)\otimes\mathrm{Perf}(Y)\simeq\mathrm{Perf}(X\times Y)$ 型的等价。扭 Künneth 公式
处理「带一个由线丛/群作用给出的扭」的情形：此时张量积要换成带扭的版本（例如只取某权重的
部分），这正是本文 §6 把 G-等变层与 Fukaya 范畴的 Künneth 对接起来的技术核心。
参考：nLab, *Künneth theorem*（ncatlab.org/nlab/show/Künneth+theorem）；本文 §6c。

## dg 范畴与 A∞ 范畴（dg category vs A∞ category）✔
dg 范畴的 Hom 复形带结合乘法；A∞ 范畴的乘法只在同伦意义下结合，由无穷多个高阶运算
$m_1,m_2,m_3,\dots$ 组成。任何 dg 范畴可看作 $m_{\ge 3}=0$ 的 A∞ 范畴，而 Fukaya 范畴
天然是 A∞ 范畴、其「上同调层面」给出普通范畴。本文所有函子都在 A∞/dg 层面陈述。
参考：nLab, *dg-category*；Keller, *On differential graded categories*, arXiv:math/0601185。

## 完美模与导出范畴（perfect module, derived category）
模的导出范畴是把复形当作对象、拟同构当作可逆态射的形式化；「完美模」是可由自由模的
有限复形表示的那些模，几何上对应向量丛的复形（$\mathrm{Perf}(X)=\mathrm{Perf}(\mathrm{QCoh}(X))$）。
本文的 B 侧对象是 $\mathrm{Coh}$ 的 dg 提升，A 侧出现的是完美模，两边通过 HMS 对应。
参考：Keller, arXiv:math/0601185；nLab, *perfect complex*。

## 轨道范畴与导出自等价（orbit category, derived auto-equivalence）
给定 dg 范畴 $\mathcal{A}$ 与群 $G$ 在其上的（强）作用，轨道范畴 $\mathcal{A}/G$ 的**对象与 $\mathcal{A}$ 相同**，态射取
$$\operatorname{Hom}_{\mathcal{A}/G}(L,K)=\bigoplus_{g\in G}\hom_{\mathcal{A}}(g(L),K),$$
合成由作用的结构约束与结合约束给出；若作用只由单个自同构 $F$ 生成（$G=\mathbb{Z}$），即得 Keller 意义下的（三角/导出）轨道范畴，三角版本需取直和补全。本文用 $\mathcal{C}/G$ 描述「商掉一个群作用」的 B 侧（§3c），并在 §5c 证明它与 A 侧商掉 $G$ 的包裹 Fukaya 范畴（§4b）相对应。
参考：Keller, *On triangulated orbit categories*, arXiv:math/0610212；本文 §3c、§5c 推论。

## G-等变层与权空间分解（G-equivariant sheaf, weight space decomposition）✔
$G$-等变层是在每点 $x$ 的纤维上给 $G$-作用、并与层结构相容的数据；对 $G=\mathbb{G}_m$
（或对角环面）作用，任何等变层可按特征标分解成权空间直和。本文的 B 侧把 $\mathbb{P}^1$
上的 $\mathbb{G}_m$-等变层按权分解，恰好与 A 侧绕 $S^1$ 的单值性/停止位选择对应。
参考：nLab, *equivariant sheaf*（ncatlab.org/nlab/show/equivariant+sheaf）；本文 §5b–5c。

## Eilenberg–Zilber 收缩与 Čech 复形（Eilenberg–Zilber contraction, Čech complex）
Čech 复形用开覆盖的交来计算层上同调；Eilenberg–Zilber 映射把两个链复形的张量积与
它们的（序）双复形比较，收缩（contraction）则给出同伦逆与同伦算子，从而把双复形上的
计算归约到对角线上。附录 A 用这套古典工具验证扭 Künneth 公式所需的同伦共轭。
参考：Eilenberg–Zilber, *On products of complexes*, Amer. J. Math. 75 (1953)；本文附录 A。

## 异域 Weinstein 结构（exotic Weinstein structure）
同一个光滑流形上可以有无穷多个互不（精确）辛同构的 Weinstein 结构；它们作为辛流形彼此
不同，但其上的包裹 Fukaya 范畴却可能等价。本文由 Hirzebruch 面 $F_n$（$n\ge 0$ 不同）
造出一族这样的结构，说明「A 模型看不见 B 侧的复结构差异」。
参考：本文 §1c 推论；Kartal, arXiv:2204.04928。
