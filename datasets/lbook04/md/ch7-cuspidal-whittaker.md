# 尖点表示与 Whittaker 模型

> `lbook04/concept/ch7-cuspidal-whittaker` · 轨 M 模形式与自守表示 · 状态 reviewed · 核验 source-only

**问题：** Whittaker 空间为什么与 $\pi$ 同构，而 Fourier 展开又为什么足以区分不同的自守表示？

**一句话：** 尖点表示是 $\mathcal A_0(G)$ 中的不可约成分；其 Whittaker 空间 $W(\pi,\psi)$ 与 $\pi$ 同构，整体 Whittaker 函数由各局部成分唯一决定，这是重数一定理的证明工具。

**别名：** `cuspidal representation`、`Whittaker model`、`Fourier 展开`

## 定义

尖点条件 $(2.6)$ 使 $\varphi$ 沿幂零方向的积分为零，从而有 Fourier 展开 $\varphi(g)=\sum_{\xi\in\mathbb Q^\times}W_\varphi(\xi g)$。$W_\varphi$ 是 Whittaker 函数，$W(\pi,\psi)$ 是 $\pi$ 的 Whittaker 模型。定理 2.5：限制张量积 $\bigotimes'_v\pi_v$ 不可约容许；定理 2.6：$\mathcal A_0(G)=\bigoplus_\pi\mathcal A_0(\pi)$，重数一（Jacquet–Langlands），强重数一（Miyake、Casselman）。

**记号：** $U$：幂零子群；$\psi$：整体加法特征；$W(\pi,\psi)$：Whittaker 空间；$\mathcal A_0(\pi)$：$\pi$-等型；$S$：分歧位集。

## 要点

- 尖点性 $\iff$ 常数项为零；Fourier 展开把 $\varphi$ 写成 Whittaker 函数沿 $\mathbb Q^\times$ 的和。
- 定理 2.5 的「限制张量积」要求几乎处处取基向量 $\xi_v^0$，否则张量积不是容许模。
- 定理 2.6(iii) 强重数一：$\pi,\pi'$ 在几乎全部位局部同构 $\Rightarrow\pi\cong\pi'$。
- $\operatorname{SL}_n$（$n\ge3$）重数可以 $>1$（Blasius），故重数一是 $\operatorname{GL}(2)$ 的特权。

## 公式

$$
\varphi(g)=\sum_{\xi\in\mathbb Q^\times}W_\varphi(\xi g),\qquad W_\varphi(g)=\int_{\mathbb Q\backslash\mathbb A}\varphi\bigl((\begin{smallmatrix}1&x\\0&1\end{smallmatrix})g\bigr)\psi(-x)\,dx
$$

$$
\mathcal A_0(G)=\bigoplus_\pi\mathcal A_0(\pi),\qquad \dim\mathcal A_0(\pi)=1
$$

## 易错点

- Whittaker 模型的存在性对尖点表示成立，对一般自守表示不成立；不要把 $\mathcal A(G)$ 的所有成分都当作有 Whittaker 模型。
- 强重数一的「几乎全部位」不能减弱为「至少一个位」：一个位的信息远不足；例外位集要有限（或密度 $<1/8$，Ramakrishnan）。

## 批注

**〔背景直觉〕为什么 Whittaker 有用**　Whittaker 函数把表示嵌入 $\mathbb A$ 上的函数空间，于是 $L$ 函数可以用 zeta 积分写出来（第 7 章 §5）；没有它，Rankin–Selberg 与对称平方 $L$ 都无从定义。

**〔含糊点拨〕重数一的两种含义**　书中「重数一」指 $\mathcal A_0(\pi)$ 在 $\mathcal A_0(G)$ 中出现一次（Jacquet–Langlands）；「强重数一」指局部成分决定整体 $\pi$（Miyake/Casselman）。读定理 2.6 时按 (ii)(iii) 分开。

## 相关

[[ch7-automorphic-rep]]、[[ch7-multiplicity-one]]、[[ch6-whittaker]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§2，原书 pp. 141–143（PDF pp. 145–147）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch07.tex:313-429`
