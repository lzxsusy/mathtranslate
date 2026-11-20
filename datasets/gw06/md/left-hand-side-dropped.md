# 漏译 “left hand side”，两侧对应失去参照

- **id**：`gw06/correction/left-hand-side-dropped`
- **类型**：correction
- **位置**：§3.4
- **问题**：漏掉 left 之后，为什么「另一侧」会失去意义？

> 「在对应的一侧」丢掉了 left，下一段的「另一侧」便无处可比；这份对应本身是左右两侧的对应。

## 位置

§3.4 首段，s03b-parabolic.tex:35（原文 ramified.tex:50，PDF 第 49 页）

## 原文片段

```latex
在对应的一侧，考虑一个全纯 $G_\C$-丛
```

## 改为

```latex
在对应的左侧，考虑一个全纯 $G_\C$-丛
```

## 依据

英文为 “On the left hand side of this correspondence”。Mehta–Seshadri 定理是一条双向对应：左侧是全纯 $G_\C$-丛（带抛物结构），右侧是带奇点的平坦 $G$-丛。紧接的下一段开头就是「在对应的另一侧」，它只能相对于「左侧」才有内容。漏掉 left 后，读者读到「另一侧」时无从判断另一侧是哪一类对象，整段对应关系的方向感就丢了。

## 说明

只补一个「左」字；「另一侧」原文照旧。

## 批注

### 含糊点拨：两侧各是什么

左侧：$C$ 上带抛物结构的全纯 $G_\C$-丛（等价于带分歧的希格斯丛，$\varphi$ 在 $p$ 处有极点）。右侧：$C$ 上带奇点 $A=\alpha\,d\theta+\dots$ 的平坦 $G$-丛。Mehta–Seshadri 说的是这两类对象之间的一一对应，而 $\alpha$ 是右侧奇点的参数、左侧抛物权，两者的匹配正是第 3 节的中心内容。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §3.4；印刷页 [47] / PDF 页 [48]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03b-parabolic.tex:33-37`
- 该句位于§3.4（小节的起始印刷页为第 47 页，PDF 第 48 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
