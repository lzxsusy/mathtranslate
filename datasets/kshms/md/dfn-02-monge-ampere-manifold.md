# Monge–Ampère 流形

`kshms/concept/dfn-02-monge-ampere-manifold` · track A（CFT 与几何退化） · 原文 定义 2

**问题**　为什么把「度量是某个局部势函数的 Hessian、且其行列式为常数」作为环面纤维化对偶的几何语言？

**摘要**　三元组 $(Y,g,\nabla)$：$\nabla$ 平坦，$g$ 在仿射坐标下是局部势函数 $K$ 的 Hessian，且 $\det(\partial_i\partial_jK)$ 为常数；这是环面纤维化对偶的几何语言。

**别名**　Monge–Ampère manifold；Monge–Ampère 流形；仿射 Hessian 流形（affine Hessian manifold）

## 陈述

Monge–Ampère 流形（Monge–Ampère manifold）是一个三元组 $(Y,g,\nabla)$，其中 $(Y,g)$ 是带度量 $g$ 的光滑黎曼流形，$\nabla$ 是 $T_Y$ 上的平坦联络，且满足：
a) $\nabla$ 在 $Y$ 上定义了一个仿射结构；
b) 在仿射坐标 $(x_1,\dots,x_n)$ 下，$g$ 的矩阵 $\bigl((g_{ij})\bigr)$ 由 $\bigl((g_{ij})\bigr)=\bigl((\partial^2K/\partial x_i\partial x_j)\bigr)$ 给出，其中 $K$ 是某个光滑实值函数；
c) 满足 Monge–Ampère 方程 $\det\bigl((\partial^2K/\partial x_i\partial x_j)\bigr)=\mathrm{const}$。

## 记号

$(Y,g)$：光滑黎曼流形；$\nabla$：$T_Y$ 上的平坦联络（一般不是 $g$ 的 Levi-Civita 联络）；$(x_1,\dots,x_n)$：$\nabla$ 的仿射坐标，$n=\dim Y$；$K$：局部光滑实值势函数；$((g_{ij}))$：$g$ 在仿射坐标下的矩阵。

## 要点

- 数据是三件套 $(Y,g,\nabla)$：$\nabla$ 平坦给出仿射结构，$g$ 是这个结构的 Hessian 度量，$K$ 是局部势函数；(c) 是对 $K$ 的行列式约束。
- $K$ 只在 $\nabla$ 的仿射坐标下局部给出；换仿射坐标时 $K$ 相差一个仿射函数，故「$g$ 是 Hessian 度量」是坐标无关的断言，而 $K$ 本身不是整体函数。
- (c) 等价于 $g$ 在仿射坐标下的矩阵行列式为常数，故其体积形式是坐标体积的常数倍。
- 原文紧接着指出：若 $Y$ 紧致，则它的有限覆盖是环面（引 [CY]）；并给出 K3 曲面椭圆纤维化的非紧例子，其底为 $\mathbb{C}P^1\setminus\{z_1,\dots,z_{24}\}$。

## 公式

$$\bigl((g_{ij})\bigr)=\bigl((\partial^2K/\partial x_i\partial x_j)\bigr)$$

$$\det\bigl((\partial^2K/\partial x_i\partial x_j)\bigr)=\mathrm{const}$$

## 易错点

- $\nabla$ 是任意的平坦联络，一般不等于 $g$ 的 Levi-Civita 联络；不要默认 $\nabla$ 由 $g$ 决定。
- (b) 只在仿射坐标下陈述：$\partial^2K/\partial x_i\partial x_j$ 里的偏导是相对仿射坐标的，换到一般坐标就不再是 Hessian。
- 这里的 Monge–Ampère 方程是实 Hessian 矩阵的行列式为常数，不要与复流形上的复 Monge–Ampère 方程混为一谈。
- 本条只提供语言，不声称任何流形都满足它；后续 Gross–Siebert 纲领把它发展成镜像构造，不在本文范围。

## 相关卡

- `kshms/concept/dfn-01-maximal-degeneration`
- `kshms/concept/conj-01-collapse-gh-limit`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §3.2（原文 p.17）；锚点 `源码/chunks/ch03.tex:20-29（定义 2）`

> 原文 p17–p18 §3.2：定义起于 p17，条件 a)–c) 排在 p18；译本 ch03.tex:199-210 与 p17–p18 逐句对应；items.tsv 记原文页 17。
