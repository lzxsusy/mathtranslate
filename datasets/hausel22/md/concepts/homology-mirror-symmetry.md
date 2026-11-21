# 同调镜像对称

> `hausel22/concept/homology-mirror-symmetry` · 轨道 A · 镜像对称与几何 Langlands · 状态 dev

> **先自测**：为什么范畴等价比 Hodge 数相等更强？

## 一句话

同调镜像对称断言镜像两边的边界条件范畴等价：一侧的 Fukaya 范畴等于另一侧凝聚层的导出范畴。

## 定义

Kontsevich 1994 年提出：镜像对 $X,Y$ 之间应当有 $Fuk(X,\omega_X)\cong D^b(Y,I_Y)$，即 $X$ 的 Fukaya 范畴（辛侧）与 $Y$ 上凝聚层的导出范畴（复侧）等价。本文在 Hitchin 系统上把它具体化为 $\mathscr{S}:D^b(\M_\DR)\simeq Fuk(\M^\vee_\DR)$，见式 (2.4)。

**记号**：$Fuk(X,\omega_X)$；$D^b(Y,I_Y)$；$\mathscr{S}$；$\M_\DR,\M^\vee_\DR$。

## 要点（为什么需要它）

1. HMS 蕴含 Hodge 数相等（范畴等价给出上同调的同构），反之不成立，所以它严格更强。
2. HMS 里的等价是范畴层面的：它不仅匹配对象，还匹配态射与 Ext 群，因此能解释镜像对称的全部数值巧合。
3. 本文用的是 HMS 的「经典极限」版本：把 $D^b(\M_\DR)\simeq Fuk(\M^\vee_\DR)$ 一阶近似成 $D^b(\M_\Dol)\simeq D^b(\M^\vee_\Dol)$，即式 (2.5)，由 Donagi–Pantev 提出。
4. 增强镜像对称 = HMS + 超 Kähler 膜的匹配 + Wilson 算子与 Hecke 算子的交换，三项缺一不可。

## 核心公式

$$
$$\mathscr{S}:D^b(\M_\DR)\simeq Fuk(\M^\vee_\DR)$$$$\mathscr{S}:D^b(\M_\Dol)\simeq D^b(\M^\vee_\Dol)$$
$$

$$
$$\mathscr{S}:D^b(\M_\Dol)\simeq D^b(\M^\vee_\Dol)$$
$$

## 定理与证明（或缺口）

### 经典极限（Donagi–Pantev）

沿 Hitchin 底 $\calA$ 的一般点，相对 Fourier–Mukai 变换给出等价 $\mathscr{S}:D^b(\M_\Dol)\simeq D^b(\M^\vee_\Dol)$，并且满足 Hecke–Wilson 交换关系。

> 证明状态：**sketch**。原文只说 Donagi–Pantev 提出并部分证明；延拓到奇点上的修改没有写出。

出处：`A p.2234 eq (2.5)`

## 常见误解

- HMS 的左边是辛侧的 Fukaya 范畴，右边是复侧的凝聚层导出范畴；写反（把 $Fuk$ 放在复结构上）是最常见的错误。
- 式 (2.4) 的两个目标是 $\M_\DR$ 与 $\M^\vee_\DR$（$J$ 结构），不是 $\M_\Dol$；$\M_\Dol$ 出现在经典极限式 (2.5) 里。
- 经典极限只是「一阶近似」，不要把它当成 HMS 的等价命题。
- 把 $\mathscr{S}$ 说成「Fourier–Mukai 变换」时要加「相对 $\calA$ 的」：在一般点上它是相对 FM，整体上仍需修改。

## 相关卡

[镜像对称（三个方面）](../concepts/mirror-symmetry.md) · [几何 Langlands 的经典极限 $\mathscr{S}$](../concepts/classical-limit-langlands.md) · [增强镜像对称](../concepts/enhanced-mirror-symmetry.md) · [经典极限 $\mathscr{S}$ 与算子的交换](../derivations/s-intertwines-operators.md)

## 出处（印刷页）

- A p.2231（A p.2231）
- A p.2234（A p.2234 eq (2.4)）
- A p.2234（A p.2234 eq (2.5)）

> 说明：A=原文 §2.2 的 Kontsevich 表述与 §2.5 的经典极限；B=把「HMS 强于 Hodge 数相等」的理由补成范畴匹配态射；C=增强镜像对称三项的并列说法取自 §2.5 末段的原文归纳。最没把握处：相对 FM 变换在奇点处的修改，原文只说「必须作修改」。
