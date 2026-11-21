# 7.12.21 中 $[[x_{m+n},\ldots,x_{m+n}]]$ 应从 $m+1$ 起

- **id**：`bdh/correction/m-n-subscript-repeat`
- **类型**：correction
- **位置**：§7
- **问题**：为什么 $R_{mn}$ 的第二个方括号必须从 $x_{m+1}$ 排到 $x_{m+n}$？

> 幂级数变量下标重复 $m+n$，形式纤维的维数就从 $n$ 掉到 1。

## 位置

§7.12 ch07.tex:2804

## 原文片段

```latex
C[x_1,\ldots,x_m][[x_{m+n},\ldots,x_{m+n}]]
```

## 改为

```latex
[[x_{m+1},\ldots,x_{m+n}]]
```

## 依据

(0) 断言 $\operatorname{Spf}R_{mn}$ 是 $C$ 上形式光滑的仿射 $\aleph_0$-形式概形。若第二个方括号只有 $x_{m+n}$ 一个变量，$R_{mn}=C[x_1,\ldots,x_m][[x_{m+n}]]$ 相对 $\operatorname{Spf}C[[x_1,\ldots,x_m]]$ 的形式维数就是 1，与下标 $mn$ 所标的「每次新增 $n$ 个变量」矛盾，也与后文同一构造的写法 $[[x_{m+1},\ldots,x_{m+n}]]$（ch07.tex:2823）不符；形式光滑性要求每一步新增的维数恰为 $n$。

## 说明

译文未改，照原文保留。校订时在 ch07.tex:2805 加 [Tutor Note] 指出应为 $[[x_{m+1},\ldots,x_{m+n}]]$，正文照底本保留原样。这是判断而非事实：依据是同一构造在后文的写法与形式光滑性所需的维数，未对照英文印刷页。

## 批注

### 易错预警：两个 $m+n$ 是排印重复

形式幂级数环 $C[x_1,\ldots,x_m][[x_{m+1},\ldots,x_{m+n}]]$ 有 $m+n$ 个变量；重复写成 $x_{m+n},\ldots,x_{m+n}$ 后只剩一个变量，$\operatorname{Spf}$ 的形式维数随之从 $n$ 掉到 1，与「形式光滑」的断言直接冲突——这是下标抄写错误，不是记号简写。

### 含糊点拨：为什么这里要盯下标

7.12 用 $R_{mn}$ 逼近一般的 $\aleph_0$-形式概形：$m$ 是已取出的有限变量个数，$n$ 是每次新增的变量个数。下标一旦写错，后面用 $x_{m+1},\ldots,x_{m+n}$ 作参数的所有构造（包括 7.12 的归纳极限）都失去依据，读者会以为这个逼近每次只加一个变量。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.12；印刷页 [329] / PDF 页 [329]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:2804-2805`
- 印刷页=PDF 页；页标记 $\SourcePage{330}$ 在 ch07.tex:2813，故 2804–2805 行属 p.329（2805 行为校订者译注）。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
