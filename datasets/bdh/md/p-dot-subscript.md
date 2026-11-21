# 7.11.18 中 $p^{\cdot}_{U_i\Omega}$ 漏了上标点

- **id**：`bdh/correction/p-dot-subscript`
- **类型**：correction
- **位置**：§7
- **问题**：为什么 7.11.18 里的 $p_{U_i\Omega}$ 必须写成 $p^{\cdot}_{U_i\Omega}$？

> Hecke 卷积定义里的 $p$ 少一个上标点，成了本章未定义的投影。

## 位置

§7.11 ch07.tex:2576

## 原文片段

```latex
\bar m_{U_i}\cdot p_{U_i\Omega}(F_n\boxtimes T_{j(n,i)})
```

## 改为

```latex
\bar m_{U_i}\cdot p^{\cdot}_{U_i\Omega}(F_n\boxtimes T_{j(n,i)})
```

## 依据

7.6 的卷积定义（ch07.tex:725）是 $F\overset{c}{\circledast}T:=\bar m_{Y\cdot}p^{\cdot}_{Y\Omega}(F\boxtimes T)$，其中 $p^{\cdot}_{Y\Omega}$ 是带 $\Omega$-结构的投影；7.11.18 只是把它搬到归纳概形的 $U_i$ 上，两处（2576、2580）都必须沿用同一记号。漏掉上标点后 $p_{U_i\Omega}$ 在本章没有定义，而 $p^{\cdot}$ 的那个点正是 $\Omega$-结构随 $f$ 拉回的全部信息所在：少了它，$(F_n\circledast T)_i$ 的定义里就出现一个来历不明的映射，7.11.12 的 $f^{\cdot}_\Omega$ 也无从代入。

## 说明

译本改译：改 ch07.tex:2576 与 2580 两处 $p_{U_i\Omega}\to p^{\cdot}_{U_i\Omega}$；7.11.18 其余文字未动。依据是 7.6 的卷积定义与 7.11.12 的 $f^{\cdot}_\Omega$ 记法，未对照英文印刷页。

## 批注

### 易错预警：上标点是 $\Omega$-结构的记号

本章 $p^{\cdot}_{Y\Omega}$、$f^{\cdot}_\Omega$、$m^{\cdot}_\Omega$ 的上标点不是装饰，而是表示「把 $\Omega$-复形沿映射拉回」这一操作；不带点的 $p_{U_i\Omega}$ 只是一个投影，没有 $\Omega$-结构的信息。排版时漏点，公式表面上仍成立，实际含义已经丢了。

### 含糊点拨：为什么这两处必须一起改

2576 定义 $(F_n\circledast T)_i$，2580 定义 $(F_n\circledast T)'_i$；后者要映到前者，靠的正是同一个 $p^{\cdot}_{U_i\Omega}$。只改一处会出现两个不同记号，读者会以为 $(F_n\circledast T)'_i$ 用了另一种拉回，7.11.18 的拟同构也就无法验证。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.11；印刷页 [317] / PDF 页 [317]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:2572-2580`
- 印刷页=PDF 页；页标记 $\SourcePage{318}$ 在 ch07.tex:2596，故 2572–2580 行属 p.317。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
