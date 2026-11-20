# 「被余根格所作的一个扩张」把扩张核写成了施动者

- **id**：`gw06/correction/extension-kernel`
- **类型**：correction
- **位置**：§3.7
- **问题**：为什么「A 被 B 所作的扩张」在短正合列里是错的？

> 仿射外尔群是外尔群的一个扩张，扩张核是余根格；原译「被……所作的扩张」既是病句，也颠倒了核与群。

## 位置

§3.7，s03c-topology.tex:178

## 原文片段

```latex
$\AffWeyl$ 是 ${\mathcal W}$ 被 $G$ 的余根格所作的一个扩张（extension）：
```

## 改为

```latex
$\AffWeyl$ 是 ${\mathcal W}$ 的一个扩张（extension），扩张核（kernel）为 $G$ 的余根格（coroot lattice）：
```

## 依据

数学内容是短正合列 $1\to\Lambda_{\mathrm{cort}}\to\AffWeyl\to{\mathcal W}\to 1$：$\AffWeyl$ 由 ${\mathcal W}$ 与平移格 $\Lambda_{\mathrm{cort}}$ 拼成，$\Lambda_{\mathrm{cort}}$ 是核，不是「施动者」。原译「被……所作的一个扩张」按汉语语法把余根格放到施动位置，读者会以为「余根格扩张了外尔群」，方向恰好相反；而且「扩张」在代数里有固定含义（extension of A by B 指核为 B），含糊的措辞会连带影响对下一段$\Weyl$ 平凡作用在 $\Z$ 上的理解。

## 说明

按原文 “an extension of ${\mathcal W}$ by the coroot lattice” 重写为「扩张核为……」，并把箭头序列在该译注下补全。

## 批注

### 含糊点拨：extension of A by B 的方向

英文 “extension of $A$ by $B$” 的标准读法是：以 $B$ 为核、以 $A$ 为商的扩张，即 $1\to B\to E\to A\to 1$。中文若译「A 被 B 扩张」几乎无法读懂，写成「E 是 A 的扩张，核为 B」最稳。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §3.7；印刷页 [67] / PDF 页 [68]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03c-topology.tex:175-181`
- 该句位于§3.7（小节的起始印刷页为第 67 页，PDF 第 68 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
