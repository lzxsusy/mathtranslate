# 莫尔斯流与最速下降曲线

> `pi/concept/morse-flow` · 轨道 C · 渐近方法与半经典 · 状态 draft

> **先自测**：流方程 $\mathrm{d}z/\mathrm{d}u=-\overline{f'(z)}$ 为什么能描出经过鞍点的最速下降曲线？

## 一句话

用流方程 $\mathrm{d}z/\mathrm{d}u=-\overline{f'(z)}$ 生成最速下降曲线：$\operatorname{Im}f$ 守恒、$\operatorname{Re}f$ 单调下降，鞍点的稳定/不稳定流形给出围道的两支。

## 定义

最速下降曲线可以看成复平面上一族轨道的并。取实参数 $u$，令轨道满足流方程 $\mathrm{d}z/\mathrm{d}u=-\overline{f'(z)}$，并要求 $u\to-\infty$ 时 $z(u)$ 趋于鞍点 $z_0$（$f'(z_0)=0$）。沿轨道 $f$ 的虚部不变、实部单调下降，所以轨道落在 $\operatorname{Im}f$ 的水平集上，并朝 $e^{\lambda f}$ 衰减的方向走。鞍点的不稳定流形（$u$ 增大时离开鞍点的那支）给出下降围道的两半；稳定流形（$u\to+\infty$ 时进入鞍点的那支）是 $\operatorname{Re}f$ 上升的方向，不能用作下降围道。对 $\operatorname{Re}f$ 来说，非退化鞍点是 Morse 指标 $1$ 的临界点（复维 $n$ 时指标为 $n$）。

**记号约定**：$u\in\mathbb{R}$ 为流参数；$z_0$ 为非退化鞍点（$f''(z_0)\ne0$）；$W^{\mathrm{u}},W^{\mathrm{s}}$ 记不稳定、稳定流形；$\lambda>0$，记号按书中 §2.5.3 起的写法 $\int e^{\lambda f}\mathrm{d}z$（若写成 $\int e^{-\lambda f}\mathrm{d}z$，把 $f$ 换成 $-f$）。

## 要点

- 流方程右边取共轭，是为了让 $\mathrm{d}f/\mathrm{d}u=-|f'|^2$ 成为实数：虚部守恒、实部单调。
- $\operatorname{Im}f$ 守恒说明整条轨道落在一条水平集上；$\operatorname{Re}f$ 递减给出方向，两者合起来唯一确定最速下降曲线。
- 鞍点是非退化临界点：线性化给出两个实特征值 $\pm|f''(z_0)|$，一个方向离开（不稳定）、一个方向进入（稳定）。
- 作下降围道只取不稳定流形（离开鞍点时 $\operatorname{Re}f$ 下降的那支）；稳定流形是 $\operatorname{Re}f$ 上升的方向，选错会使 $e^{\lambda f}$ 发散。
- Morse 指标：$\operatorname{Re}f$ 在非退化鞍点的黑塞行列式为 $-|f''|^2<0$，指标为 $1$（复维 $n$ 时为 $n$），所以鞍点必有一个上升、一个下降方向。

## 关键公式

$$
\dfrac{\mathrm{d}z}{\mathrm{d}u}=-\overline{f'(z)},\qquad \lim_{u\to-\infty}z(u)=z_0
$$

$$
\dfrac{\mathrm{d}f}{\mathrm{d}u}=-|f'(z)|^2
$$

$$
\operatorname{Im}f(z(u))=\operatorname{Im}f(z_0),\qquad \dfrac{\mathrm{d}}{\mathrm{d}u}\operatorname{Re}f(z(u))=-|f'(z(u))|^2\le0
$$

$$
z(u)=\pm e^{Au}e^{\frac{\mathrm{i}}{2}(\pi-\theta)},\qquad \alpha=Ae^{\mathrm{i}\theta},\quad f(z)=\dfrac{\alpha z^2}{2}
$$

$$
\det H_{\operatorname{Re}f}(z_0)=-|f''(z_0)|^2<0
$$

## 定理与证明

### 流保持虚部、压低实部

设 $z(u)$ 满足 $\mathrm{d}z/\mathrm{d}u=-\overline{f'(z)}$。则 $\operatorname{Im}f(z(u))$ 为常数，$\operatorname{Re}f(z(u))$ 单调不增，且只在临界点取等号。

**完整证明**

1. 用链式法则：$\mathrm{d}f/\mathrm{d}u=f'(z)\,\mathrm{d}z/\mathrm{d}u=-f'(z)\overline{f'(z)}=-|f'(z)|^2$。
   - *为什么*：代入流方程即得；共轭保证乘积是模方。
2. 右端是实数，故 $\mathrm{d}(\operatorname{Im}f)/\mathrm{d}u=0$。
   - *为什么*：导数的虚部为零，说明虚部沿轨道不变。
3. 实部满足 $\mathrm{d}(\operatorname{Re}f)/\mathrm{d}u=-|f'|^2\le0$，等号只在 $f'(z)=0$ 时成立。
   - *为什么*：模方非负；这给出 $|e^{\lambda f}|=e^{\lambda\operatorname{Re}f}$ 沿轨道只减不增。
4. 因此轨道是 $\operatorname{Im}f$ 的一条水平集，方向由 $\operatorname{Re}f$ 下降确定；从鞍点出发的两支合起来就是下降曲线。
   - *为什么*：水平集加单调方向唯一确定曲线，极限条件把鞍点选作起点。

来源：ch02a.tex:1139-1150（原书 p.100）

### 非退化鞍点的 Morse 指标为 1

设 $f$ 在 $z_0$ 解析、$f'(z_0)=0$、$f''(z_0)\ne0$。则实函数 $\operatorname{Re}f$ 在 $z_0$ 的黑塞行列式为 $-|f''(z_0)|^2$，故 $z_0$ 是 Morse 指标 $1$ 的鞍点：一个特征方向上升、另一个下降。

**完整证明**

1. 记 $u=\operatorname{Re}f$。在临界点 $z_0$ 的黑塞矩阵为 $H=\begin{pmatrix}u_{xx}&u_{xy}\u_{xy}&u_{yy}\end{pmatrix}$，且 $u$ 调和：$u_{xx}+u_{yy}=0$。
   - *为什么*：解析函数的实部满足拉普拉斯方程，这是柯西–黎曼方程的直接推论。
2. 由 $f''=u_{xx}-\mathrm{i}u_{xy}$ 得 $|f''(z_0)|^2=u_{xx}^2+u_{xy}^2$，于是 $\det H=u_{xx}u_{yy}-u_{xy}^2=-(u_{xx}^2+u_{xy}^2)=-|f''(z_0)|^2<0$。
   - *为什么*：行列式为负说明两个特征值异号，临界点不是极值而是鞍点。
3. 异号特征值意味着 Morse 指标（负特征值个数）为 $1$；沿负特征方向 $\operatorname{Re}f$ 下降，这正是流的不稳定方向。
   - *为什么*：流沿 $\operatorname{Re}f$ 减小的方向离开鞍点，故下降围道取不稳定流形。

来源：ch02a.tex:1139-1150、1196-1204（原书 p.100、102）；Morse 指标按标准定义补充

### 稳定流形与不稳定流形

在非退化鞍点 $z_0$ 附近，流的两条特征轨道给出稳定流形 $W^{\mathrm{s}}$（$u\to+\infty$ 时趋于 $z_0$，$\operatorname{Re}f$ 上升）与不稳定流形 $W^{\mathrm{u}}$（$u\to-\infty$ 时趋于 $z_0$，$\operatorname{Re}f$ 下降）；二者都在水平集 $\operatorname{Im}f=\operatorname{Im}f(z_0)$ 上，合起来是该水平集过 $z_0$ 的两支。

**证明提纲**

1. 线性化：$\mathrm{d}w/\mathrm{d}u=-\overline{f''(z_0)}\,\bar w$，$w=z-z_0$；取 $w=e^{\mathrm{i}\varphi}s$ 得两个实特征方向，特征值为 $\pm|f''(z_0)|$。
   - *为什么*：一个方向轨道指数离开鞍点（不稳定），另一个指数进入（稳定）。
2. 沿离开方向 $\operatorname{Re}f$ 下降、沿进入方向上升；由 $\operatorname{Im}f$ 守恒，两支都落在同一水平集上。
   - *为什么*：这解释了为什么下降围道只取水平集的一支，而不是整条水平集。

> **缺口**：书中只用图说明流的走向，未证明稳定/不稳定流形定理，也未处理 $f''(z_0)=0$ 的退化鞍点；本卡只做线性化，全局流形与水平集的一致性是 Morse 理论的标准结论（书中引 [60]），此处未展开。


来源：ch02a.tex:1139-1150、1184-1204（原书 p.100–102）

## 易错点

- 流方程里的共轭不能丢：若写成 $\mathrm{d}z/\mathrm{d}u=-f'(z)$，则 $\mathrm{d}f/\mathrm{d}u=-f'^2$ 不再是实数，$\operatorname{Im}f$ 不守恒。
- 符号约定：本节流对应 $\int e^{\lambda f}\mathrm{d}z$，$\operatorname{Re}f$ 沿流递减才是下降；对 $\int e^{-\lambda f}\mathrm{d}z$ 要把 $f$ 换成 $-f$，否则选到上升分支。
- 鞍点是 $\operatorname{Re}f$ 的鞍点而不是极值：整条水平集含上升、下降两支，只能取下降支作围道。
- 退化鞍点 $f''=0$ 时线性化失效（如 $f=z^3$ 有三条射线），不能套用 $\pm|f''|$ 的特征值。
- Morse 指标数的是 $\operatorname{Re}f$ 在实二维中的负特征值个数（等于 $1$），不是复函数 $f$ 的指标；复维 $n$ 时指标为 $n$。

## 相关卡

- [最速下降法](../concepts/steepest-descent.md)
- [$\alpha z^2/2$ 的鞍点流线与最速下降围道](../examples/stokes-rays-linear.md)
- [高斯积分 $\int_C e^{\mathrm{i}\lambda z^2}\mathrm{d}z$ 的最速下降围道](../examples/steepest-descent-gaussian.md)

## 出处

- §2.5.3 莫尔斯流，p.100–102（PDF p.101–103），源码 `ch02a.tex:1137-1211`
