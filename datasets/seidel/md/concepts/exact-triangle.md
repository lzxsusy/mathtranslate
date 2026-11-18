# 殊三角（正合三角）

> `seidel/concept/exact-triangle` ｜ track A ｜ draft

**一句话**：三角范畴里代替正合列的结构：X→Y→Z→TX，满足 TR1–TR4；在 Tw A 中由映射锥给出。

**自测**：为什么三角范畴的公理里要害是「第三个态射 Z→TX」，而不是前两个？

## 定义

三角范畴是带平移自等价 $T$ 的加性范畴，连同一族殊三角
$$X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}TX,$$
满足：TR1 每个态射可补全为殊三角；TR2 旋转后仍是殊三角；TR3 态射之间的交换方块可补成态射；TR4（八面体公理）保证锥的复合相容。在 $\Tw\A$ 中，殊三角取映射锥
$$X\xrightarrow{f}Y\to\Cone(f)\to TX .$$

记号：$T$ 也记作 $[1]$ 或 $S$；$\Cone(f)$ 是 $f$ 的映射锥。

## 要点

- 第三个态射 $h:Z\to TX$ 不是装饰：没有它，三角就退化成「两个复合为零」的序列。
- TR4 是三角范畴最不直观的公理；它保证「锥的锥」与八面体相容。
- 由殊三角取 $\Hom$ 得到两条长正合列（协变与反变），这是三角结构最主要的推论。

## 公式

$$X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}TX,\qquad h\in\hom(Z,TX)$$
$$\cdots\to H^i(X)\to H^i(Y)\to H^i(Z)\xrightarrow{h_*}H^{i+1}(X)\to\cdots$$

## 定理与证明

### 殊三角给出长正合列

对三角范畴中的殊三角 $X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}TX$，取 $\Hom(W,-)$ 得长正合列
$$\cdots\to\Hom(W,X)\to\Hom(W,Y)\to\Hom(W,Z)\xrightarrow{h_*}\Hom(W,TX)\to\cdots .$$

（complete；来源：原书 p.34–40 §3）

1. $g\circ f=0$ 与 $h\circ g=0$ 是殊三角的公理，故复合为零。  
   为什么：TR1 的一部分；在 $\Tw\A$ 中由锥的构造直接验证。
2. 对任意 $a:W\to Z$ 使 $h\circ a=0$，由 TR3 的补全性质，$a$ 经过 $g$ 分解。  
   为什么：把 $a$ 与零态射组成交换方块，用三角的补全公理。
3. 正合性在 $\Hom(W,-)$ 上逐点成立，故得长正合列。  
   为什么：第 1、2 步分别给「复合为零」与「核包含像」，反向包含由旋转三角重复同样论证。

## 易错点

- 第三个态射的符号不是任意的：$(f,g,h)$ 是殊三角时，$(f,g,-h)$ 一般不是。
- 不要把三角范畴当成「带长正合列的范畴」；TR4 是独立公理，不能由长正合列推出。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§3，p.34–40（原书 p.34–40 §3）

关联：`seidel/concept/twisted-complex`、`seidel/concept/split-generation`、`seidel/deriv/mapping-cone`

来源说明：原书 p.34–40 §3；译者注 A03-04（nLab triangulated category，B 级）。
