# 「完全拓扑李代数」应为「完备拓扑李代数」

- **id**：`bdh/correction/complete-topological-lie-algebra`
- **类型**：correction
- **位置**：§1
- **问题**：为什么「完全拓扑李代数」必须改成「完备拓扑李代数」？

> complete 在 1.2 节被译成「完全」，与同段「完备化代数」不一致，读者会以为是另一种拓扑性质。

## 位置

§1.2 ch01.tex:159

## 原文片段

```latex
完全拓扑李代数
```

## 改为

```latex
完备拓扑李代数
```

## 依据

英文原文是 complete topological Lie algebra。同段把 $\overline{\operatorname{Sym}}\Theta_S$ 称作「完备化代数」，而 complete 说的正是对这个完备化拓扑（有限维李代数的投射极限）取极限后不再产生新元素；术语表把 complete 冻结为「完备」。译作「完全」会与 full、totally 一类的既有译名相混，也让同一段先出「完备化」、再出「完全」而看不出是同一个词。

## 说明

译本改译：ch01.tex:159 两处、ch01.tex:166 一处；「完备化」等既有一致译法未动。依据是术语表与同段上下文，未对照英文印刷页。

## 批注

### 易错预警：complete 不是「完全」

complete 在拓扑代数里的意思是「对给定拓扑完备」：取完备化之后不再添加新元素。中文「完全」容易对应 full、totally 等另一类概念，与 completeness 无关。本书同一段里既有「完备化代数」又有「完备拓扑李代数」，两个译名必须同源，否则读者会以为是两种对象。

### 含糊点拨：完备是对哪个拓扑而言

这里的拓扑来自 $\mathfrak{k}=\operatorname{Lie}K$ 作为开子代数的嵌入：$\mathfrak{g}$ 是有限维李代数沿这个开子代数取投射极限的结果，complete 指的就是对这个极限拓扑完备。脱离拓扑说「完全」，读者无法判断这是在讲收敛性、还是讲李代数本身的性质。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §1.2；印刷页 [13, 14] / PDF 页 [13, 14]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch01.tex:159-166`
- 印刷页=PDF 页；行 159 在 p.13，行 166 在 p.14，两页各一处。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
