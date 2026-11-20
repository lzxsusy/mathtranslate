# 仿射赫克代数与赫克算符

- **id**：`gw06/concept/affine-hecke-algebra`
- **类型**：concept
- **位置**：§4.6
- **问题**：赫克算符的『修正』与 (4.18) 的线丛张量积是什么关系，为什么两者合起来才是仿射赫克代数的作用？

> 仿射外尔群的赫克形变：基 $T_w$ 满足 $T_s^2=(q-1)T_s+q$；其 $\mathbb C[\Lambda_{\cort}]$ 部分在 K-理论上就是线丛张量积 (4.18)，与 't Hooft 算符的赫克修正合成一个代数。

## 定义

仿射赫克代数 $\mathcal H_{\rm aff}$ 是仿射外尔群 $\AffWeyl=\Lambda_{\cort}\rtimes\Weyl$ 的群代数的形变：作为向量空间同构于 $\mathbb C[\Lambda_{\cort}]\rtimes\mathbb C[\Weyl]$，基 $T_w$ 在长度可加时满足 $T_wT_{w'}=T_{ww'}$，且 $(T_s+1)(T_s-q)=0$。其中 $\mathbb C[\Lambda_{\cort}]$ 部分在 $K$-理论上表现为与线丛作张量积 $\mathcal U\mapsto(\oplus_i{\mathcal L}^{v_i})\otimes\mathcal U$，即 (4.18) 的群半环作用；$T_s$ 部分则是 't Hooft 算符穿过点 $q$ 时对丛的赫克修正。物理上，'t Hooft 算符与威尔逊算符的复合给出这些算符的代数；§4.6 中带非正则单值性 $V$ 时，这一代数被非阿贝尔群 $\mathcal V_U$ 的作用补充，作用在整族膜而非单一膜上。这正是原文把赫克算符与 (4.18) 的线丛张量积并置讨论的原因，两者共同生成同一个代数。

**记号**：$\mathcal H_{\rm aff}$：仿射赫克代数、$T_w$：赫克代数的标准基、$q$：形变参数（$q=1$ 退化为群代数）、$\mathcal V_U$：非正则单值性下作用在范畴上的群

## 关键点

- $\mathcal H_{\rm aff}$ 的 $\mathbb C[\Lambda_{\cort}]$ 部分对应 (4.18) 的线丛张量积；$q=1$ 时退化回群代数 $\mathbb C[\AffWeyl]$。
- $T_s$ 对应点 $q$ 处的赫克修正：'t Hooft 算符插入时把丛沿 $q$ 扭转，与线丛张量积合成同一个代数。
- 非正则 $V$ 时 $\mathcal V_U$ 一般不可约地作用，赫克算符的本征膜不再唯一，只剩范畴。
- 经 $S$-对偶与 c.c. 膜，这族膜对应 $\M(\alpha,p;G)$ 上被 $\mathcal V_U$ 作用的扭曲 $\mathcal D$-模。
- 群半环允许直和与正整数倍，故 (4.18) 中会出现 $\oplus_i{\mathcal L}^{v_i}$ 形式的元素。

## 公式

```latex
{\mathcal U}\to \left(\oplus_{i=1}^w{\mathcal L}^{v_i}\right)\otimes {\mathcal U}.
```
```latex
{\mathcal V}_{Y,\mathbb{L}}=\Lambda_\cort^\mathbb{L}\rtimes{\mathcal W}_{Y,\mathbb{L}}.
```
```latex
{\mathcal V}_Y=\Lambda_\cort\rtimes \Weyl_Y.
```

## 常见错误

- 把 $\mathcal H_{\rm aff}$ 当成有限外尔群的赫克代数：$\Lambda_{\cort}$ 带来的平移部分正是 (4.18) 那一项，丢掉它就无法解释 ${\mathcal V}_Y$ 的单参数族。
- 以为 $\mathcal V_U$ 是赫克算符的子群：它是额外作用在范畴上的非阿贝尔群，与赫克算符共同生成但不包含于其中。
- 把 (4.18) 写成单个线丛：群半环允许直和与重数 $w$，写成单丛会漏掉赫克代数的整性。

## 批注

### 易错预警：(4.18) 是群半环而非群

原文说 ${\mathcal V}_Y$ 的元素的正整数线性组合构成『群半环』；因此 (4.18) 允许 $\oplus_i{\mathcal L}^{v_i}$ 这样的直和与重数 $w$，这不是群作用而是半环作用，把它写成单个线丛会漏掉赫克代数的整性。原文特意点明『群半环』，正是为了保留 $w$ 重直和这一整性，而不是只留一个线丛。

### 含糊点拨：赫克算符与 't Hooft 算符的关系

在相对论性规范理论中 't Hooft 算符就是赫克修正的实现：它在 $q$ 处插入奇点并改变丛的粘合。因此原文『't Hooft／赫克算符』连写不是两个对象，而是同一个几何操作在物理与代数两侧的名字。把二者当成两种独立算符会重复计数，也会让 (4.18) 与 $T_s$ 的作用次序失去意义。

### 背景直觉：为什么仿射赫克代数会出现在这里

线算符的复合代数在几何朗兰兹中由 $\mathbb C[\Lambda_{\cort}]$（线丛扭转）与 $T_s$（赫克修正）生成，这正是仿射赫克代数；它在 $K$-理论上的表示就是 $K(\MH)$ 上那族单值性作用的代数化，所以 §4.5 的 ${\mathcal V}_Y$ 与 §4.6 的赫克算符是同一件事的两面。这正是原文把 §4.5 的 ${\mathcal V}_Y$ 与 §4.6 的赫克算符并列讨论的原因。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §4.6；印刷页 [106, 108] / PDF 页 [107, 109]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s04b-lines.tex:520-640`
- 非正则 $V$、$\mathcal V_U$ 与 (4.18) 的作用见 PDF 第 107–109 页（印刷 106–108 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
