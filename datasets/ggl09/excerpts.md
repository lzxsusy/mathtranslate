# 09 精译节选

[p.9]
$bA$ 模型放在 $W=S^2\times I$ 上，再乘一条时间方向的 $\mathbb R$。边界条件是混合的：$I$ 的一端取 Dirichlet，另一端取 Neumann；此外在 $W$ 内沿 $L=c\times\mathbb R$ 放一个 't Hooft 奇点。于是要解的是带奇点的 Bogomolny 方程 (2.2)。把丛 $E\to C\times I$ 限制到 $C\times\{y\}$ 得到全纯 $G_\mathbb C$ 丛 $E_y$；关键事实是：作为全纯丛，$E_y$ 与 $y$ 无关，只差一个自然同构。证明只需一个短计算：Bogomolny 方程的 $(y,\bar z)$ 分量给出 $F_{y\bar z}=-iD_z\varphi_0$，等价于 $[\partial_y+A_y+i\varphi_0,\partial_{\bar A}]=0$；因此 $\bar\partial_A$ 沿 $y$ 方向只差一个复规范变换。当 $y$ 越过奇点所在的位置 $y=r$ 时，$E_y$ 发生跳变，而这个跳变正是在 $c\in C$ 处的一次 Hecke 修改。这个独立性是 §2.4 的全部内容：它把四维的 Bogomolny 方程化成一个复几何的陈述，从而可以用仿射 Grassmannian 的语言描述 't Hooft 算子的类型。

[p.14]
$bB$ 模型保留 $N=4$ 超对称的一个子代数，其 $R$-对称 $Spin(6)$ 破到 $Spin(2)$；这个 $Spin(2)$ 通常称为『鬼数』(ghost number)。在 $bA$ 模型里，上同调按 degree 的分级就是由这个 $Spin(2)$ 的作用给出的；在 $bB$ 模型里，$\sigma^\vee$ 的鬼数为 2，相应的生成元是 $2(X_1\partial/\partial X_2-X_2\partial/\partial X_1)$。正则 Nahm 极点 $\vec X=\vec t/y$ 在『$X_1$–$X_2$ 平面的旋转』与『由 $t_3$ 生成的规范变换』的联合作用下不变；因此 $bB$ 模型的分级实际上来自 $t_3$，而 $t_3$ 生成的是 $G^\vee$ 的主 $\mathrm{SL}_2$ 子群的极大环面。这一点是本篇把两边的分次对齐的关键：在 $bA$ 中，$x_i$ 的次数 $2d_i-2$ 正是这个鬼数的偏移，两边的分级因此可以逐项比较，而不只是形式上对应。

[p.30]
$P(J)\cong\mathbb{CP}^3$，$SL(2,\mathbb C)$ 在其中的轨道由二次型分类。使 $Q^2=0$ 的点正是二次型的零点，它们构成一个非退化的二次曲面 $Q\cong\mathbb{CP}^1\times\mathbb{CP}^1$；商掉 $SL(2,\mathbb C)$ 后得到 $\mathbb{CP}^1$ 族 $Z$-分级拓扑场论，它来自四维理论的紧化，其中两个点分别是 $G$ 的 $bA$ 模型与 $bB$ 模型，一般点给出量子几何 Langlands。二次曲面的补集则不同：它是单个 $SL(2,\mathbb C)$ 轨道，可以用一个 $2\times 2$ 矩阵 $K$ 表示，$K$ 非零二次型的条件就是 $\det K\neq0$，稳定子是 $\mathbb Z_2$。因此这个理论只有 $\mathbb Z_2$-分级，而不是 $Z$-分级；它不由四维紧化产生，而且不区分 $G$ 与 $G^\vee$；这正是本篇标题中『第三种理论』的意思。
