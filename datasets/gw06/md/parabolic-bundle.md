# 抛物丛

- **id**：`gw06/concept/parabolic-bundle`
- **类型**：concept
- **位置**：§3.4
- **问题**：微分几何里「A 在 p 处有 α·dθ 奇点」与复几何里「丛在 p 处带抛物结构」为什么是同一件事？

> 在一点把结构群约化到抛物子群，就得到抛物丛；Mehta–Seshadri 定理把它与带 α 型奇点的平坦丛一一对应。

## 定义

设 $E\to C$ 是 $G_\mathbb C$-丛，$\mathbb P\subset G_\mathbb C$ 是抛物子群，$\mathbb L$ 是 $\mathbb P$ 的列维子群。在 $p$ 处给 $E$ 一个抛物结构，就是把 $E$ 在 $p$ 处的结构群约化到 $\mathbb P$；所有可能的约化构成的空间同构于 $G_\mathbb C/\mathbb P$。微分几何一侧则是：取正则的 $\alpha\in\mathfrak t$，令 $U=\exp(-2\pi\alpha)$，考虑 $C\setminus p$ 上绕 $p$ 的单值性共轭于 $U$ 的平坦 $G$-丛，等价地考虑方程 $F=2\pi\alpha\,\delta_p$ 的解模去在 $p$ 处取值于 $\mathbb L$ 的规范变换。Mehta–Seshadri 定理断言：稳定抛物 $G_\mathbb C$-丛的模空间与这个带奇点平坦丛的模空间相同。物理上抛物结构记录的是面算符在 $p$ 处把规范群破缺到 $\mathbb L$ 的方式。

**记号**：$\mathbb P$：抛物子群、$\mathbb L$：$\mathbb P$ 的列维部分、$U=\exp(-2\pi\alpha)$：绕 $p$ 的极限单值性、$\mathcal M(\alpha;p)$：带单值性 $U$ 的平坦丛模空间

## 关键点

- 抛物结构的选择 = 在 $p$ 处选一个与 $\mathbb P$ 共轭的子群，参数空间是 $G_\mathbb C/\mathbb P$；换成紧群就是 $G/\mathbb L$。
- 对应成立的前提是 $\alpha$ 严格 $\mathbb L$-正则：$G$ 中与 $U=\exp(-2\pi\alpha)$ 交换的子群恰为 $\mathbb L$。
- 辛观点下，联络空间的辛形式为 $\omega=-{1\over4\pi}\int_C\Tr\delta A\wedge\delta A$，矩映射为 $\mu=-{1\over2\pi}\int_C\Tr\epsilon F$，其零点条件对带奇点联络恰是 $F=2\pi\alpha\delta_p$。
- 对复化群 $\mathcal G_\mathbb C$ 取商给出稳定抛物丛，对紧群 $\mathcal G$ 取商给出 $\mathcal M(\alpha;p)$，二者由 Kempf–Ness 一致。
- $\alpha$ 一身二任：既是奇点强度，又是 $p$ 处的抛物权重，所以 $\mathbb L$-正则性与稳定性门槛是同一件事的两面。

## 公式

```latex
F=2\pi\alpha\delta_p
```
```latex
\omega=-{1\over 4\pi}\int_C\Tr\delta A\wedge\delta A
```
```latex
\mu=-{1\over 2\pi}\int_C\Tr\epsilon F
```
```latex
U=\exp(-2\pi\alpha)
```

## 定理

**Mehta–Seshadri（推广 Narasimhan–Seshadri）**：对严格 $\mathbb L$-正则的 $\alpha$，稳定抛物 $G_\mathbb C$-丛的模空间与 $\mathcal M(\alpha;p)$ 相同；当抛物结构平凡时退化为「稳定 $G_\mathbb C$-丛 = 平坦 $G$-丛」。

证明：sketch（§3.4，式 (3.35)–(3.37)）

1. 联络空间带辛形式 $\omega$ 与矩映射 $\mu$，其辛商为 $\mathcal M(\alpha;p)$。 —— $\mu=0$ 即 $F=2\pi\alpha\delta_p$，模掉在 $p$ 处取值于 $\mathbb L$ 的规范变换。
2. 把辛商按 Kempf–Ness 重读为对复化群的 GIT 商。 —— 仿射（或 Kähler）空间上群作用的辛商等于复化群的 GIT 商，稳定点对应稳定丛。
3. GIT 商就是带 $\mathbb P$ 型抛物结构的稳定丛的模空间。 —— GIT 稳定性由 $\alpha$ 给出的抛物权重下的斜率判据刻画。

缺口：稳定性判据的细节原文未展开，只引 Mehta–Seshadri。

## 常见错误

- 把「抛物结构」与「抛物希格斯丛」混为一谈：前者只管丛在 $p$ 处的约化，后者还要求希格斯场 $\varphi$ 在 $p$ 处有极点、留数取值于 $\mathfrak p$。
- 在 $\alpha$ 非严格 $\mathbb L$-正则时仍照搬一一对应：此时与 $U$ 交换的群比 $\mathbb L$ 大，抛物结构不唯一，对应失效。
- 把 $\mathcal M(\alpha;p)$ 的下标 $\mathbb L$ 读成 Langlands 对偶群：它指列维子群，与 ${}^L G$ 无关。

## 批注

### 易错预警：抛物结构不是「在 p 处加个标记」

抛物结构是结构群的约化 $G_\mathbb C\rightsquigarrow\mathbb P$，等价于在 $p$ 处选一个滤过并赋权重。只把它记成「$p$ 处有个特殊点」会丢掉权重 $\alpha_i$，而这些权重正是稳定性判据与 $\alpha$ 的对应所在。

### 含糊点拨：「相同」是哪一级的相同

Mehta–Seshadri 给出的是模空间作为复（辛）流形的同构，而不只是双射。原文用它来把微分几何的奇点描述翻译成复几何的稳定性描述，因此稳定性条件必须与 $\alpha$ 的取值精确对应，不能只对「一般」$\alpha$ 断言。

### 背景直觉：为什么偏偏在一点

面算符支撑在曲面 $D$ 上，与 $C$ 相交于一点；四维到二维的约化把这一个交点变成 $C$ 上的一个标记点。于是「面算符的连续参数」在几何一侧就表现为「一点处的抛物/奇点数据」，这就是整套对应的物理来源。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §3.4；印刷页 [47, 49] / PDF 页 [48, 50]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03b-parabolic.tex:9-77`
- 抛物丛与 Mehta–Seshadri 定理见 PDF 第 48–50 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
