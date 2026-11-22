# 椭圆曲线的 Hasse–Weil L 函数

> `lbook04/concept/ch5-elliptic-l` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** 为什么 $E$ 的 $L$ 函数在好位恰好是二次因子 $(1-a_p p^{-s}+p^{1-2s})^{-1}$，而坏位只留下一次因子或 $1$？

**一句话：** 对每条 $\mathbb Q$ 上椭圆曲线 $E$，把各素数处的 $a_p=1+p-\#E(\mathbb F_p)$ 组装成 Euler 乘积：好位因子 $(1-a_p p^{-s}+p^{1-2s})^{-1}$，坏位按归约类型截断。

**别名：** `Hasse–Weil L-function`、`E 的 L 函数`、`Euler 因子`

## 定义

定义 $L(E,s)=\prod_p L_p(E,s)$。对 $p\nmid N$ 取 $\ell\ne p$，$V_\ell=T_\ell E\otimes\mathbb Q_\ell$ 上几何 Frobenius $\varphi_p$ 的两个特征值 $\lambda,\lambda'$ 满足 $\lambda\lambda'=p$（Weil 配对），且 $a_p=\lambda+\lambda'=1+p-\#\widetilde E(\mathbb F_p)$，故 $L_p=(1-a_p p^{-s}+p^{1-2s})^{-1}$。乘性归约（$p\|N$）时惯性不变空间一维，$L_p=(1-a_p p^{-s})^{-1}$，$a_p=\pm1$；加性归约时 $L_p=1$。Euler 乘积在 $\operatorname{Re}s>3/2$ 绝对收敛，因为 $|a_p|\le 2\sqrt p$。

**记号：** $E/\mathbb Q$：椭圆曲线；$N$：导子；$V_\ell$：$\ell$ 进 Tate 模；$I_p$：惯性群；$\sigma_p$：几何 Frobenius；$a_p=1+p-\#\widetilde E(\mathbb F_p)$。

## 要点

- $(3.1)$ $L_p=\det\bigl(1-p^{-s}\sigma_p\mid(V_\ell)^{I_p}\bigr)^{-1}$ 是定义，对 $\ell\ne p$ 与 $\ell$ 的选取无关。
- 好位：$\lambda\lambda'=p$ 来自 Weil 配对，故局部因子是二次多项式；$|a_p|\le 2\sqrt p$ 即 Hasse 界。
- 乘性归约：$(3.5)$ 一次因子，$a_p=\pm1$；加性归约：$(3.6)$ $L_p=1$。
- $(3.7)$ $L(E,s)=\prod_p L_p$ 在 $\operatorname{Re}s>3/2$ 收敛；每个局部因子都是 $\mathbb Z_p$ 上有理函数的 Euler 因子。

## 公式

$$
L(E,s)=\prod_p L_p(E,s),\qquad L_p=\det\bigl(1-p^{-s}\sigma_p\mid (V_\ell)^{I_p}\bigr)^{-1}
$$

$$
L_p=(1-a_p p^{-s}+p^{1-2s})^{-1},\qquad a_p=1+p-\#\widetilde E(\mathbb F_p)
$$

$$
L(E,s)=\prod_p\bigl(1-a_p p^{-s}+p^{1-2s}\bigr)^{-1},\qquad \operatorname{Re}s>3/2
$$

## 易错点

- 不要把 $a_p$ 的符号弄反：本书约定 $a_p=1+p-\#E(\mathbb F_p)$，于是 $\#E(\mathbb F_p)=1+p-a_p$。
- 坏位不能一律代入 $a_p$：乘性归约用一次因子、加性归约 $L_p=1$，导子指数按 §3.2 的四条规则算。

## 批注

**〔易错预警〕$p$ 与 $\ell$ 的角色**　定义 $(3.1)$ 里取样 $\ell\ne p$；$\ell=p$ 时 $V_\ell$ 的分歧由另一套机制控制。书中注 (a) 强调必须取惯性不变空间，才得到与 $\ell$ 无关的局部因子。

**〔背景直觉〕为什么是二次因子**　$V_\ell$ 是秩 $2$ 自由 $\mathbb Z_\ell$ 模；好位 Frobenius 的两个特征值 $\lambda,\lambda'$ 满足 $\lambda\lambda'=p$（Weil 配对 $e_N$ 的相伴性，§2.2），故 $\det(1-t\varphi_p)=1-a_p t+p t^2$，代 $t=p^{-s}$ 即 $(3.3)$。

## 相关

[[ch5-hecke-eigenform]]、[[ch5-bsd]]、[[ch5-eichler-shimura]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3.1，原书 pp. 97–98（PDF pp. 102–103）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:268-329`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3.2，原书 pp. 99（PDF pp. 104）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:330-345`
