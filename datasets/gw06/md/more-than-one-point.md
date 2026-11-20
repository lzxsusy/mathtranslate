# 「一个以上」把 more than one 放宽成 ≥1

- **id**：`gw06/correction/more-than-one-point`
- **类型**：correction
- **位置**：§3.6
- **问题**：「一个以上」与 “more than one” 在什么情形下会给出不同的数学结论？

> 英文 “more than one point” 是至少两个点，译作「一个以上点」在汉语口语里可含一个，量词范围被放宽。

## 位置

§3.6 末段，s03c-topology.tex:324

## 原文片段

```latex
位置依赖于与一个以上点相关的参数
```

## 改为

```latex
位置依赖于与多于一个点相关的参数
```

## 依据

原文 “at a location that depends on parameters associated with more than one point”。汉语「一个以上」在书面语中严格指 $>1$，但口语与多数读者的第一反应包含「一个」，而多点整体奇点恰恰只对点数 $s\geq 2$ 出现：它要求各分歧点的参数彼此关联，$s=1$ 时只是单点奇点，不构成整体奇点。量词一旦放宽，读者会以为单点也归入此类，与紧接的「实余维四」论断冲突。

## 说明

按英文改为「多于一个点」；同段其余各处「整体奇点」措辞未动。

## 批注

### 易错预警：汉语的「以上」有歧义

「一个以上」= $>1$ 还是 $\geq 1$，取决于语境，数学文本里应避开。译 “more than one” 用「多于一个」，译 “at least one” 用「至少一个」，译 “more than one” 绝不能用「一个以上」。同类还有「不少于／不超过／以内」。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §3.6；印刷页 [67] / PDF 页 [68]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03c-topology.tex:318-324`
- 该句位于§3.7（小节的起始印刷页为第 67 页，PDF 第 68 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
