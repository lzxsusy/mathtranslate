# 5.4.8 证明中 $\widetilde{\mathfrak g\otimes K}$ 的波浪号范围

- **id**：`bdh/correction/widetilde-g-otimes-k`
- **类型**：correction
- **位置**：§5
- **问题**：为什么 $(\tilde{\mathfrak g}\otimes K,G(O))$ 必须写成 $(\widetilde{\mathfrak g\otimes K},G(O))$？

> 波浪号只盖住 $\mathfrak g$，把中心扩张 $\widetilde{\mathfrak g\otimes K}$ 读成了 $\tilde{\mathfrak g}\otimes K$。

## 位置

§5.4 ch05.tex:569

## 原文片段

```latex
(\tilde{\mathfrak{g}}\otimes K,G(O))
```

## 改为

```latex
(\widetilde{\mathfrak{g}\otimes K},G(O))
```

## 依据

2.5.1 定义的中心扩张记作 $\widetilde{\mathfrak g\otimes K}$，5.6.11 明说「2.5.1 中 $\widetilde{\mathfrak g\otimes K}$ 的定义」；本段 5.4.8 的 Harish–Chandra 对在 ch05.tex:586 也写作 $(\operatorname{Der}O\ltimes\widetilde{\mathfrak g\otimes K},\operatorname{Aut}^0_Z O\ltimes G(O))$。若波浪号只盖 $\mathfrak g$，$\tilde{\mathfrak g}\otimes K$ 既不是 2.5.1 的中心扩张，也就不是 5.4.8 中 Harish–Chandra 模真正作用的那个李代数，括号里它同 $G(O)$ 的配对无从谈起。

## 说明

译本改译：只改 ch05.tex:569 这一处；同段 ch05.tex:588 仍作 $\tilde{\mathfrak g}\otimes K$（本轮未改，待统一）。判断依据是 2.5.1/5.6.11 的定义与相邻行 586，未对照英文印刷页。

## 批注

### 易错预警：波浪号盖住谁是实质问题

$\widetilde{\mathfrak g\otimes K}$ 表示 $\mathfrak g\otimes K$ 的中心扩张（仿射李代数），$\tilde{\mathfrak g}\otimes K$ 则是「某个 $\mathfrak g$ 的扩张再张量 $K$」。括号范围不同，对象就不同，Harish–Chandra 模的定义域随之改变；这两种写法在源码里只差一对花括号，靠肉眼极难分辨。

### 背景直觉：为什么这里必须用中心扩张

5.4.8 的定理说 $P\overset{c}{\circledast}\mathit{Vac}'$ 是 $\mathit{Vac}'$ 的直和，证明把左端写成 $H^i(GR,P\lambda^{-1})$。$\mathit{Vac}'$ 是 $\mathfrak g\otimes K$ 的中心扩张的模，不是 $\mathfrak g\otimes K$ 的模，所以 Harish–Chandra 对的第一项必须带中心扩张，否则 $P\lambda^{-1}$ 这个系数模根本落不进去。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §5.4；印刷页 [220] / PDF 页 [220]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch05.tex:562-572`
- 印刷页=PDF 页；页标记 $\SourcePage{221}$ 在 ch05.tex:602，故 562–572 行属 p.220。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
