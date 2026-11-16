# 哈密顿流是辛同胚（$f=\tfrac12q^2$ 与 $f=q^1q^2$）

> `geoq/example/hamiltonian-flow-symplectomorphism` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：解一次哈密顿方程，为什么流的拉回会让辛形式的修正项自动消失？

## 一句话

对 $f=\frac12q^2$ 解出 $V_f=q\,\partial_p$ 与 $\varphi_t(q,p)=(q,p+tq)$，直接验证 $\varphi_t^*\omega=\omega$；$f=q^1q^2$ 时交叉项同样相消。

## 设定

取 $M=T^*\mathbb{R}\cong\mathbb{R}^2$，$\omega=dp\wedge dq$，$\lambda=p\,dq$。先取 $f(q)=\frac12q^2$，再取 $T^*\mathbb{R}^2$（坐标 $q^1,q^2,p_1,p_2$）与 $f=q^1q^2$。哈密顿向量场由 $\iota_{V_f}\omega=df$ 定义。

## 计算

**第 1 步**：解 $V_f$：写 $V=a\partial_q+b\partial_p$，则 $\iota_V\omega=b\,dq-a\,dp$；令它等于 $df=q\,dq$，比较系数得 $b=q$、$a=0$，即 $V_f=q\,\partial_p$。

> 为什么：先写出 $\iota_V\omega$ 的坐标式再逐项比对，是解 $\iota_V\omega=df$ 的标准方法。

**第 2 步**：解流：$\dot q=0$、$\dot p=q$，故 $\varphi_t(q,p)=(q,\,p+tq)$；这是沿纤维的平移，$q$ 不变。

> 为什么：右端只依赖常数 $q$，直接积分即可；几何上 $f$ 只依赖 $q$ 时流只推动动量。

**第 3 步**：验证保辛：$\varphi_t^*dq=dq$、$\varphi_t^*dp=d(p+tq)=dp+t\,dq$，故 $\varphi_t^*\omega=(dp+t\,dq)\wedge dq=dp\wedge dq+t\,dq\wedge dq=\omega$。

> 为什么：修正项是 $t\,dq\wedge dq$，外积反对称使它自动为零，这正是保辛的机制。

**第 4 步**：二维底流形验证：$f=q^1q^2$ 时 $V_f=q^2\partial_{p_1}+q^1\partial_{p_2}$，$\varphi_t(q,p)=(q^1,q^2,p_1+tq^2,p_2+tq^1)$，于是 $\varphi_t^*\omega=(dp_1+tdq^2)\wedge dq^1+(dp_2+tdq^1)\wedge dq^2=\omega+t(dq^2\wedge dq^1+dq^1\wedge dq^2)=\omega$。

> 为什么：两个修正项是同一个 $2$-形式的两面，符号相反恰好抵消；一般 $n$ 时对应海森矩阵的对称性与外积的反对称性。

**第 5 步**：作用在拉格朗日子流形上：$L_\alpha=\{(q,\alpha(q))\}$ 在 $\varphi_1$ 下变成 $\{(q,\alpha(q)+q)\} = L_{\alpha+d(\frac12q^2)}$；特别地 $\varphi_1(L_0)=L_{df}$。

> 为什么：逐点计算纤维平移量 $df$，与 $\varphi_1(L_\alpha)=L_{\alpha+df}$ 的定义逐点吻合。

## 结果

$\varphi_t(q,p)=(q,p+tq)$ 是哈密顿流，$\varphi_t^*\omega=\omega$ 对一切 $t$ 成立，故它是辛同胚；$\varphi_t$ 还构成单参数群（$\varphi_s\circ\varphi_t=\varphi_{s+t}$），且把 $L_\alpha$ 送到 $L_{\alpha+df}$。

## 复核

雅可比与特例：$\varphi_t$ 的微分在基 $(\partial_q,\partial_p)$ 下满足 $d\varphi_t(\partial_q)=\partial_q+t\,\partial_p$、$d\varphi_t(\partial_p)=\partial_p$，按 $q$ 行 $(1,0)$、$p$ 行 $(t,1)$ 排列，行列式为 $1$，与保面积一致；取 $t=1$、$(q,p)=(1,2)$ 得 $(1,3)$，与 $p+tq$ 的公式吻合。

## 易错点

- 只有 $f=f(q)$ 时 $q$ 才不动；若 $f$ 依赖 $p$，$V_f$ 含 $-\partial_{p_i}f\,\partial_{q^i}$ 项，流会同时移动 $q$，$\varphi_t(q,p)=(q,p+tdf)$ 不再成立。
- 符号：此处 $\omega=dp\wedge dq$、$\iota_{V_f}\omega=df$ 给出 $V_f=+q\partial_p$；换用 $\omega=dq\wedge dp$ 会得到 $-q\partial_p$，两者的流互为时间反演。
- 保辛不等于哈密顿：本例的流由 $f$ 生成，但一般辛同胚（如环面上的常向量场平移）并不来自整体哈密顿函数。

## 用到哪些概念

- [辛同胚与哈密顿流](../concepts/symplectomorphism.md)
- [哈密顿向量场与泊松括号](../concepts/hamiltonian-vector-field.md)

## 相关卡

- [恰当拉格朗日 $L_{df}$ 与相函数（$f=q^1q^2$）](../examples/exact-lagrangian-phase-function.md)

## 出处

- §5.1.4 例 5.1.32：哈密顿流是辛同胚，p.263（PDF p.264），源码 `ch05a.tex:785-812`
