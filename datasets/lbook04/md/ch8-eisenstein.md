# Eisenstein 级数与连续谱

> `lbook04/concept/ch8-eisenstein` · 轨 T Tate 与迹公式 · 状态 reviewed · 核验 source-only

**问题：** 为什么 Eisenstein 级数只贡献连续谱，而尖点形式贡献离散谱？

**一句话：** Eisenstein 级数 $E(g,f_{s,k},\chi)=\sum_{\Gamma_\infty\backslash\Gamma}\bar\chi(\gamma)f_{s,k}(\gamma g)$ 在 $\operatorname{Re}s>1$ 收敛，亚纯延拓后其边界值张成 $L^2$ 的连续谱。

**别名：** `Eisenstein series`、`连续谱`、`constant term`

## 定义

对带一个尖点的 $\Gamma$，Eisenstein 级数 $(41)$ 由 $K$-有限函数 $f_{s,k}$ 沿 $\Gamma_\infty\backslash\Gamma$ 求和得到。命题 39：$\operatorname{Re}s>1$ 时绝对收敛；定理 41：$E$ 与常数项 $A_k(s)$ 有亚纯延拓与函数方程；定理 44：$E^*(z,s)$ 除 $s=0,1$ 外解析。连续谱由 $E(g,1/2+it)$（$t\in\mathbb R$）张成，离散谱由 $L_0^2$ 的尖点形式张成，两者在谱展开 $(55)$ 中并列。

**记号：** $\Gamma_\infty$：尖点稳定子；$f_{s,k}$：主系列向量；$E(g,s,\chi)$；$A_k(s)$：常数项；$L_0^2$：尖点谱子空间。

## 要点

- Eisenstein 级数的常数项是 $A_k(s)f+B_k(s)\widetilde f$，函数方程来自 $A_k(s)$ 的矩阵性质（Bernstein–Selberg）。
- 连续谱的谱测度集中在 $\operatorname{Re}s=1/2$ 的线上（$t\in\mathbb R$），由 $M(s)$ 的酉性保证。
- 尖点谱 $L_0^2$ 是离散的：$T_\varphi$ 在 $L_0^2$ 上紧（定理 37），故有特征基。
- 谱展开 $(55)$ 同时含离散和与连续积分，是 Selberg 理论的核心公式。

## 公式

$$
E(g,f_{s,k},\chi)=\sum_{\gamma\in\Gamma_\infty\backslash\Gamma}\bar\chi(\gamma)\,f_{s,k}(\gamma g)
$$

$$
L^2(\Gamma\backslash G)=L_0^2(\Gamma\backslash G)\oplus L_{\mathrm{Eis}}^2(\Gamma\backslash G)
$$

## 易错点

- Eisenstein 级数在 $\operatorname{Re}s>1$ 收敛，但物理解释要用 $s=1/2+it$ 的延拓值；直接对 $(41)$ 取 $s=1/2$ 不收敛。
- 连续谱不是「Eisenstein 级数本身」的和，而是其边界值按 Plancherel 测度积分；把 $E(g,s)$ 当作 $L^2$ 向量要先取 $s=1/2+it$。

## 批注

**〔背景直觉〕为什么有连续谱**　$\Gamma\backslash G$ 非紧，Laplacian 的谱除离散特征值外还有绝对连续部分；Eisenstein 级数正是这部分的本征函数，其「特征值」连续变化，故只能积分不能求和。

**〔含糊点拨〕$s=0,1$ 的极点**　定理 44 说 $E^*$ 除 $s=0,1$ 外解析；这两个极点分别对应常数函数与残数给出的平方可积函数，在谱展开中要单独处理，不能并入连续积分。

## 相关

[[ch8-discrete-spectrum]]、[[ch8-selberg-trace]]、[[ch8-langlands-entry]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§8，原书 pp. 180–184（PDF pp. 183–187）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch08.tex:1397-1648`
