# $\mathcal L(\mathbb R^2)=\mathbb{RP}^1$ 上的马斯洛夫指标

> `geoq/example/maslov-index-rp1` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：在 $\mathbb R^2$ 上「绕一圈」的马斯洛夫指标为什么是 $2$ 而不是 $1$？

## 一句话

平面上的拉格朗日格拉斯曼流形是射影直线；绕单位圆一圈的环路经行列式平方后绕两圈，指标为 $2$。

## 设定

取 $(V,\omega)=(\mathbb R^2,\omega_1)$，把 $\mathbb R^2$ 与 $\mathbb C$ 等同。考虑环路 $\gamma:S^1\to\mathcal L(\mathbb R^2)$，$\gamma(\theta)=e^{i\theta}$，它代表过原点的直线 $\mathbb Re^{i\theta}$。

## 计算

**第 1 步**：每条直线都是拉格朗日：$\dim L=1=\frac12\dim V$，且 $\omega_1(u,u)=0$ 对一切 $u$ 成立，故 $\omega_1|_{L\times L}=0$。

> 为什么：斜对称形式在任意一维子空间上必然为零，维数又恰为一半，两条都满足。

**第 2 步**：等同 $\mathcal L(\mathbb R^2)=\mathbb{RP}^1=\operatorname{U}(1)/\operatorname{O}(1)$：$\operatorname{U}(1)=S^1$ 以旋转可迁地作用在直线上，$L=\mathbb R\cdot1$ 的稳定化子是 $\operatorname{O}(1)=\{\pm1\}$。

> 为什么：轨道–稳定化子定理：轨道就是全体直线，稳定化子是把 $L$ 映到自身的旋转，即 $\pm1$。

**第 3 步**：写成 $S^1/\mathbb Z_2$ 后，$z\mapsto z^2$ 给出同胚 $\mathbb{RP}^1\cong S^1$，因为 $z$ 与 $-z$ 代表同一条直线。

> 为什么：平方映射的纤维恰好是 $\{\pm z\}$，正是商掉的 $\mathbb Z_2$。

**第 4 步**：$\det:\operatorname{U}(1)\to S^1$ 就是 $z\mapsto z$，故 $\det^2(z)=z^2$；它在 $z=\pm1$ 上都取值 $1$，因此下降为映射 $\mathcal L(\mathbb R^2)\to S^1$。

> 为什么：下降的障碍只有 $\det$ 在 $\operatorname{O}(1)$ 上的符号，平方把它消成 $1$。

**第 5 步**：沿环路计算：$\det^2\circ\gamma(\theta)=e^{2i\theta}$。$\theta$ 从 $0$ 走到 $2\pi$ 时幅角总共增加 $4\pi$，绕数为 $4\pi/2\pi=2$。

> 为什么：绕数 = 幅角总增量 / $2\pi$；指数上的系数 $2$ 直接给出因子 $2$。

## 结果

$m(\gamma)=2$，即 $\gamma$ 对应 $2\in\mathbb Z\cong\pi_1(\mathcal L(\mathbb R^2))$；它是生成元的两倍，而不是生成元。

## 复核

(i) $\gamma(\theta+\pi)=-e^{i\theta}$ 与 $\gamma(\theta)$ 是同一条直线，故 $\theta\mapsto\gamma(\theta)$ 在 $[0,\pi]$ 上已闭合，这一段是指标 $1$ 的生成元；(ii) $\det^2$ 诱导 $\pi_1(\mathcal L)\cong\pi_1(S^1)=\mathbb Z$，指标 $2$ 与「绕两圈」相符；(iii) 反向环路 $\gamma(-\theta)$ 的指标为 $-2$，与同态性 $m(\gamma^{-1})=-m(\gamma)$ 一致。

## 易错点

- 别把 $\gamma(\theta)=e^{i\theta}$ 当成 $\mathbb{RP}^1$ 的生成元：$\theta$ 与 $\theta+\pi$ 表示同一条直线，这个环路在 $\mathcal L(\mathbb R^2)$ 里实际绕了两圈。
- 若把 $\det^2$ 换成 $\det$：它在 $\operatorname{O}(1)=\{\pm1\}$ 上不恒定，无法下降为 $\mathcal L$ 上的函数；此时 $\det\circ\gamma=e^{i\theta}$ 的绕数 $1$ 并不是马斯洛夫指标。
- 绕数的符号依赖 $S^1$ 的定向；把 $e^{i\theta}$ 换成 $e^{-i\theta}$ 会让指标整体变号，但绝对值仍为 $2$。

## 用到哪些概念

- [马斯洛夫指标与 $\mathcal L(V)$ 的基本群](../concepts/maslov-index.md)
- [拉格朗日子空间与格拉斯曼流形](../concepts/lagrangian-grassmannian.md)

## 相关卡

- [标准辛基给出的两张拉格朗日子空间](../examples/standard-lagrangian-subspaces.md)
- [相容复结构与可缩性](../concepts/compatible-complex-structure.md)

## 出处

- §5.1.3 例 5.1.17 的设定，p.258（PDF p.259），源码 `ch05a.tex:533-543`
- §5.1.3 指标计算 $m(\gamma)=2$，p.259（PDF p.260），源码 `ch05a.tex:550-559`
