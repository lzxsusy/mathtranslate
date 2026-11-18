# 把映射锥写成扭曲复形

> `seidel/deriv/mapping-cone` ｜ track A ｜ draft

**目标**：构造态射 $f:X\to Y$ 的映射锥，并证明它就是扭曲复形 $(Y\oplus X,\delta)$。

**自测**：为什么映射锥可以看成一个只有两项的扭曲复形？

## 前提

- $\A$ 是 dg 范畴，$f:X\to Y$ 是次数 $1$ 的闭态射（$df=0$）。
- 取 $X_0=Y$、$X_1=X$，$V^0=V^1=\K$。

## 步骤

1. **定义 $\delta^{1,0}=f$，其余分量为零。**  
   为什么：这是唯一的非零连接，总次数为 $1$（$f$ 次数 $1$，张量因子次数 $0$）。  
   锚点：原书 p.35 §3e（证据 A）

2. **严格下三角：按 $F^0=Y\oplus X$、$F^1=X$、$F^2=0$ 取滤过，商上微分为零。**  
   为什么：$\delta$ 只把第 $0$ 层送到第 $1$ 层。  
   锚点：原书 p.35 §3e（证据 A）

3. **MC 方程：$\delta^2=0$，$d\delta=0$（$f$ 闭），故 $d\delta+\delta^2=0$；高阶项因 $\delta^2=0$ 消失。**  
   为什么：$\A$ 是 dg 范畴时 MC 只到二次。  
   锚点：原书 p.35 §3e（证据 A）

4. **$d_T=d+\delta$ 的矩阵是 $\begin{pmatrix}d_Y&f\\0&d_X\end{pmatrix}$，其 $H^0$ 正是 $\Cone(f)$。**  
   为什么：按 $Y\oplus X$ 分块读出。  
   锚点：原书 p.35 §3e（证据 A）

## 结果

$(Y\oplus X,\delta)$ 是扭曲复形，且 $H^0$ 与映射锥一致；由此 $\Tw\A$ 含全部锥。

## 缺口

- $\A$ 非 dg 时，锥仍需 MC 方程的高阶项；上述构造只给出 dg 情形。

## 易错点

- $\delta$ 的分量方向写反会得到「上锥」而非锥，同调不同。
- $\delta$ 的总次数必须是 $1$；$f$ 的次数写错会使 MC 方程不成立。
- 锥的微分矩阵是 $\begin{pmatrix}d_Y&f\\0&d_X\end{pmatrix}$，符号取决于 $f$ 的次数与分块顺序。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§3e，p.35–36（原书 p.35 §3e）

关联：`seidel/concept/twisted-complex`、`seidel/concept/exact-triangle`、`seidel/deriv/twisted-differential`

来源说明：据原书 §3e（p.35–36）转述；译者注 A05-xx。
