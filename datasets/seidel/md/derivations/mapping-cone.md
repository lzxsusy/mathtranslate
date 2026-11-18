# 把映射锥写成扭曲复形

> `seidel/deriv/mapping-cone` ｜ track A ｜ draft

**目标**：把次数 $0$ 的闭态射 $f:X\to Y$ 的映射锥写成两项扭曲复形 $(SX\oplus Y,\delta)$，并证明它与抽象锥一致。

**自测**：为什么映射锥可以看成一个只有两项的扭曲复形？

## 前提

- $\A$ 是 dg 范畴，$f:X\to Y$ 是次数 $0$ 的闭态射（$df=0$）。
- 取 $X_0=X$、$X_1=Y$，$V^0=V^1=\K$；锥的对象是 $C=SX\oplus Y$，$S$ 是移位函子。

## 步骤

1. **定义 $\delta^{1,0}=S(f)$（作为 $\hom^1(SX,Y)$ 的元素），其余分量为零：$\delta=\begin{pmatrix}S(d_X)&0\\S(f)&d_Y\end{pmatrix}$。**  
   为什么：(3.28) 的矩阵只有左下块 $S(c)$ 非零；$c$ 是次数 $0$ 的 cocycle，$S(c)$ 才是次数 $1$。  
   锚点：原书 p.48 §3p（证据 A）

2. **取滤过 $F^0=C$、$F^1=Y$、$F^2=0$；商 $C/F^1\cong SX$ 上的诱导微分为零，故 $\delta$ 严格下三角。**  
   为什么：$S(d_X)$ 本身严格下三角，$Y$ 这一块单独成层。  
   锚点：原书 p.48 §3p（证据 A）

3. **MC 方程等价于 $X,Y$ 各自的 MC 加上 $f$ 是 cocycle；dg 情形即 $d\delta+\delta^2=0$，因为 $\delta$ 只有一个非零块，$\delta^2=0$。**  
   为什么：原文 (3p) 明言「MC 方程等价于各 $Y_k$ 的 MC 与 $c$ 是 cocycle」；块结构使 $\delta^2=0$。  
   锚点：原书 p.48 §3p（证据 A）

4. **按未移位分块写出 $d_T=\begin{pmatrix}d_X&0\\f&d_Y\end{pmatrix}$，其 $H^0$ 是 $\Cone(f)$（p.48 末段用 Yoneda 嵌入把这个扭曲复形与抽象锥等同）。**  
   为什么：把 $S$ 吸收进分块即得标准锥矩阵；$f$ 落在左下块 $\delta^{1,0}$。  
   锚点：原书 p.48 §3p（证据 A）

## 结果

$\Cone(f)=(SX\oplus Y,\delta)$ 是扭曲复形，$H^0$ 与抽象映射锥一致；$\Tw\A$ 因此对锥封闭，并带正合三角（p.49 (3q)）。

## 缺口

- $\delta$ 的次数 $1$ 来自移位 $S$：写成 $\begin{pmatrix}d_X&0\\f&d_Y\end{pmatrix}$ 时 $f$ 本身仍是次数 $0$ 的态射，不可记成次数 $1$。
- $\A$ 非 dg 时锥要用 (3.28) 的高阶 MC（$\mu^{\ge3}$ 项），本卡只写 dg 情形。

## 易错点

- 把 $f$ 写成次数 $1$、或把 $\delta^{1,0}$ 的方向写成 $Y\to X$，都会得到上锥而非锥，同调不同。
- $\delta$ 的总次数必须是 $1$：这是 $S(f)$ 的次数，不是 $f$ 的次数。
- 矩阵块的左右位置取决于分块顺序 $(SX,Y)$；换顺序时 $f$ 换到右上块并带符号。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§3p，p.48–49（原书 p.48 §3p）

关联：`seidel/concept/twisted-complex`、`seidel/concept/exact-triangle`、`seidel/deriv/twisted-differential`

来源说明：据原书 §3p（p.48–49）(3.28) 转述；抽象锥见 §3e（p.35）。译者注 A02-08、A03-09。
