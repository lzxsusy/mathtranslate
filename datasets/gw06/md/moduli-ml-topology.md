# M_L(α;p) 的拓扑

- **id**：`gw06/concept/moduli-ml-topology`
- **类型**：concept
- **位置**：§3.5
- **问题**：M_L(α;p) 的第二上同调里，哪些部分来自底 M、哪些来自纤维 G/L，为什么中央扩张 Z→H²→Λ_wt 决定了仿射外尔群的作用？

> M_L(α;p) 是以 M 为底、G/L 为纤维的纤维化，Leray 谱序列给出 H² 的短正合列，并暴露出仿射权格这一关键结构。

## 定义

对给定的 $G_\mathbb C$-丛 $E$ 与抛物子群 $\mathbb P$，$p$ 处所有可能的抛物结构构成 $G_\mathbb C/\mathbb P\cong G/\mathbb L$。因此（在每一点都由稳定丛代表的范围之内）$\mathcal M_\mathbb L(\alpha;p)$ 是以 $\mathcal M$ 为底、$G_\mathbb C/\mathbb P$（复解析版）或 $G/\mathbb L$（辛版）为纤维的纤维化。用 Leray 谱序列逐级计算，$H^2(\mathcal M_\mathbb L(\alpha;p);\mathbb Z)$ 由 $H^2(\mathcal M;\mathbb Z)\cong\mathbb Z$ 与 $H^2(G/\mathbb L;\mathbb Z)=\Lambda_{\mathrm{wt},\mathbb L}$ 拼成，得到短正合列 $0\to\mathbb Z\to H^2\to\Lambda_{\mathrm{wt},\mathbb L}\to0$。这个扩张不是平凡的：它把 $\Lambda_{\mathrm{wt}}$ 嵌成一个中央扩张，正是第 3.7 节仿射外尔群作用的代数来源。

**记号**：$\mathcal M$：无抛物结构的稳定 $G_\mathbb C$-丛模空间、$\Lambda_{\mathrm{wt}}$：权格、$\Lambda_{\mathrm{wt},\mathbb L}$：$\mathbb L$-不变子格、$\mathfrak L$：行列式线丛

## 关键点

- $G_\mathbb C/\mathbb P$ 与 $G/\mathbb L$ 作为实（辛）流形相同：前者是复解析描述，后者是辛描述，不能把后者当复流形谈全纯性。
- 纤维化只在 $\mathcal M$ 的奇点之外、且每点可由稳定丛代表时成立；一般地失效处余维随亏格 $g_C$ 与秩 $r$ 增大而增大。
- 对单连通 $G$，$H^2(\mathcal M;\mathbb Z)\cong\mathbb Z$ 由行列式线丛 $\mathfrak L$ 的第一陈类生成；$H^2(G/\mathbb T;\mathbb Z)=\Lambda_{\mathrm{wt}}$。
- 短正合列 $0\to\mathbb Z\to H^2(\mathcal M_\mathbb L(\alpha;p);\mathbb Z)\to\Lambda_{\mathrm{wt},\mathbb L}\to0$ 可分裂；分裂方式决定仿射外尔群的平移部分。
- $G=PSU(N)$ 且特征类为 $N$ 阶时所有半稳定丛都是稳定的，纤维化精确成立。

## 公式

```latex
0\to H^2(\mathcal M;\mathbb Z)\to H^2(\mathcal M_\mathbb L(\alpha;p);\mathbb Z)\to H^2(G/\mathbb L;\mathbb Z)\to 0
```
```latex
H^2(G/\mathbb T;\mathbb Z)=H^1(\mathbb T;\mathbb Z)=\Lambda_{\mathrm{wt}}
```
```latex
0\to\mathbb Z\to H^2(\mathcal M(\alpha;p);\mathbb Z)\to\Lambda_{\mathrm{wt}}\to 0
```

## 定理

**H² 的中央扩张**：对单连通 $G$ 与纤维化 $G/\mathbb L\to\mathcal M_\mathbb L(\alpha;p)\to\mathcal M$，有短正合列 $0\to\mathbb Z\xrightarrow{c_1(\mathfrak L)}H^2(\mathcal M_\mathbb L(\alpha;p);\mathbb Z)\to\Lambda_{\mathrm{wt},\mathbb L}\to0$。

证明：sketch（§3.5，式 (3.38)–(3.47)）

1. Leray 谱序列的 $E_2^{0,0}=\mathbb Z$、$E_2^{0,2}=H^2(G/\mathbb L)$、$E_2^{2,0}=H^2(\mathcal M)=\mathbb Z$，其余相关格为零。 —— 纤维 $G/\mathbb L$ 的 $H^1$ 为零（单连通），故低次项只剩这几格。
2. 所有相关微分消失，谱序列退化。 —— 作者给出二维情形的退化论证；一般情形下用 $d_2$ 的非零会与 $H^2$ 含仿射权格矛盾来排除。
3. 故有短正合列，且 $H^2(\mathcal M)$ 由 $c_1(\mathfrak L)$ 生成。 —— 谱序列退化后 $H^2$ 是各 $E_2^{p,q}$（$p+q=2$）的扩张；$\mathfrak L$ 生成 $H^2(\mathcal M;\mathbb Z)$ 是已知事实。

缺口：原文未给一般情形的微分消失证明，只对二维情形断言。

## 常见错误

- 把 Leray 表的行标当成底次数：作者把纤维次数放竖直、底次数放水平，与标准 $E_2^{p,q}=H^p(B;H^q(F))$ 的方向相反，照标准读会把 $H^2(\mathcal M)$ 与 $H^2(G/\mathbb L)$ 的位置颠倒。
- 以为纤维化总成立：$\mathcal M$ 的奇点处、或稳定抛物丛的底丛不稳定时纤维化失效。
- 把 $G_\mathbb C/\mathbb P\cong G/\mathbb L$ 当成复流形同构：$G/\mathbb L$ 只是实（辛）流形，全纯性只在 $G_\mathbb C/\mathbb P$ 一侧有意义。

## 批注

### 易错预警：谱序列表的指标方向

式 (3.40) 的表把纤维次数 $p$ 放竖直、底次数 $q$ 放水平，与通常 $E_2^{p,q}=H^p(B;H^q(F))$ 的行列方向相反。总次数 $p+q=2$ 的三格是 $H^2(G/\mathbb L)$、$0$、$H^2(\mathcal M)$；若按标准方向读，正合列的方向就会反过来。

### 含糊点拨：为什么中央扩张就是仿射外尔群

仿射外尔群是 $\Lambda_{\mathrm{cochar}}$ 对通常外尔群的扩张。这里 $H^2$ 的短正合列把 $\Lambda_{\mathrm{wt}}$ 扩张一个 $\mathbb Z$，对偶地给出余特征格方向的平移；第 3.7 节正是把这套上同调结构翻译成仿射外尔群在 $H^*(\mathcal M_H)$ 上的作用。

### 背景直觉：底与纤维各管一半参数

无抛物结构时模空间是 $\mathcal M$；加上 $p$ 处抛物结构后多出的自由度正是「在 $p$ 处选一个与 $\mathbb P$ 共轭的子群」，即 $G/\mathbb L$。因此 $\mathcal M_\mathbb L(\alpha;p)$ 的拓扑 = 底的拓扑 ⊗ 纤维的拓扑，只是两者被一个中央扩张扭在一起。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §3.5；印刷页 [50, 55] / PDF 页 [51, 56]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03b-parabolic.tex:78-200`
- 纤维化、Leray 谱序列与 H² 正合列见 PDF 第 51–56 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
