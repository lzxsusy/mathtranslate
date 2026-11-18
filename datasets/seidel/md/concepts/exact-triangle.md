# 殊三角（正合三角）

> `seidel/concept/exact-triangle` ｜ track A ｜ draft

**一句话**：三角范畴里代替正合列的结构：X→Y→Z→TX，满足 TR1–TR4；在 Tw A 中由映射锥给出。

**自测**：为什么三角范畴的公理里要害是「第三个态射 Z→TX」，而不是前两个？

## 定义

三角范畴是带平移自等价 $T$ 的加性范畴，连同一族殊三角
$$X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}TX,$$
满足：TR1 恒等三角 $X\xrightarrow{\id}X\to0\to TX$ 是殊三角，且每个态射可补全为殊三角；TR2 旋转后仍是殊三角；TR3 态射之间的交换方块可补成态射；TR4（八面体公理）保证锥的复合相容。在 $\Tw\A$ 中，殊三角取映射锥
$$X\xrightarrow{f}Y\to\Cone(f)\to TX .$$

记号：$T$ 也记作 $[1]$ 或 $S$；$\Cone(f)$ 是 $f$ 的映射锥。

## 要点

- 第三个态射 $h:Z\to TX$ 不是装饰：没有它，三角就退化成「两个复合为零」的序列。
- TR4 是三角范畴最不直观的公理；它保证「锥的锥」与八面体相容。
- 由殊三角取 $\Hom$ 得到两条长正合列（协变与反变），这是三角结构最主要的推论。

## 公式

$$X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}TX,\qquad h\in\hom(Z,TX)$$
$$(X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}TX)\ \text{殊}\iff (Y\xrightarrow{g}Z\xrightarrow{h}TX\xrightarrow{-Tf}TY)\ \text{殊}$$

## 定理与证明

### 殊三角给出长正合列

对三角范畴中的殊三角 $X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}TX$ 与任意对象 $W$，有两条长正合列
$$\cdots\to\Hom(W,X)\to\Hom(W,Y)\to\Hom(W,Z)\xrightarrow{h_*}\Hom(W,TX)\to\cdots,$$
$$\cdots\to\Hom(TX,W)\to\Hom(Z,W)\to\Hom(Y,W)\to\Hom(X,W)\to\cdots .$$

（sketch；来源：原书 p.40 Cor 3.15、p.41 §3i）

1. $g\circ f=0$：把恒等三角 $X\xrightarrow{\id}X\to0\to TX$ 用 $(\id_X,f)$ 映入 $X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}TX$，由 TR3 补全后中间方块的交换性给出 $g f=0$。  
   为什么：这是 TR1 与 TR3 的标准推论（先在恒等三角上补全，再读中间的方块）。
2. 反变情形：设 $\psi:Y\to W$ 满足 $\psi\circ f=0$。把 $X\to Y\to Z\to TX$ 与 $0\to W\xrightarrow{\id}W\to0$ 用 $(0,\psi)$ 作成三角态射，TR3 补出 $\gamma:Z\to W$ 使 $\gamma\circ g=\psi$。  
   为什么：第一个方块 $0=\psi\circ f$ 交换；补全后的第二个方块正是所求的分解。
3. 协变情形由旋转（TR2，原书 Cor 3.17）后对反变情形重复同一论证得到；再对旋转迭代，即得两条含所有平移的长正合列。  
   为什么：旋转后的三角仍殊（原书 Cor 3.17 即 TR2），故同一 TR3 论证可用。

缺口：第 3 步只说明路线；两条长正合列的完整链条（含 $T^{\pm1}$ 的平移）没有逐项写出。

## 易错点

- 第三个态射的符号不是任意的：$(f,g,h)$ 是殊三角时，$(f,g,-h)$ 一般不是。
- 不要把三角范畴当成「带长正合列的范畴」；TR4 是独立公理，不能由长正合列推出。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§3，p.34–40（原书 p.34–40 §3）

关联：`seidel/concept/twisted-complex`、`seidel/concept/split-generation`、`seidel/deriv/mapping-cone`

来源说明：原书 p.34–40 §3；译者注 A03-04（nLab triangulated category，B 级）。
