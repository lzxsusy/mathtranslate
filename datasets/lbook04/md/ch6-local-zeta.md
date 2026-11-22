# 局部 zeta 积分与 L 因子

> `lbook04/concept/ch6-local-zeta` · 轨 T Tate 与迹公式 · 状态 reviewed · 核验 source-only

**问题：** 为什么局部 $L$ 因子可以读成一维分布空间里两组自然基之间的比例常数？

**一句话：** 对每个位 $v$，zeta 积分 $z(s,\omega;f)=\int_{F^\times}f\omega\omega_s\,d^\times x$ 给出 $S'(\omega\omega_s)$ 中的非零元素；它等于局部 $L$ 因子乘一个标准分布 $z_o$，故 $L$ 因子就是「最大公分母」。

**别名：** `Tate 积分`、`zeta integral`、`局部 L 因子`

## 定义

固定位 $v$，$F=k_v$。定义 $S'(\omega)=\{\lambda:r'(a)\lambda=\omega(a)\lambda\}$；定理 3.4：$\dim S'(\omega)=1$。zeta 积分在 $\operatorname{Re}s>0$ 收敛，且 $f\mapsto z(s,\omega;f)$ 是 $S'(\omega\omega_s)$ 中的非零元素。无分歧时取 $\tau=[1]-[\varpi^{-1}]$ 把支集推入 $F^\times$，得 $z_o$ 使 $z(s,\omega)=L(s,\omega)z_o(s,\omega)$（$(3.6)$）；$L$ 是使 $z/L$ 整、且对每个 $s$ 可取 $f$ 使其非零的最小分母。

**记号：** $S(F)$：Schwartz–Bruhat 空间；$S'(F)$：缓增分布；$\omega_s(x)=|x|^s$；$d^\times x=\mu|x|^{-1}dx$；$z_o$：标准分布；$\tau$：把支集推到 $F^\times$ 的差分。

## 要点

- 轨道分解 $F=\{0\}\cup F^\times$ 给出正合列 $(3.1)(3.2)$；一维性来自引理 3.2（$F^\times$ 上的分布由 $\omega\,d^\times x$ 张成）与引理 3.3（支在 $0$ 的分布）。
- 无分歧：$z=(1-tq^{-s})^{-1}z_o$；分歧：$L_v=1$，$z_o:=z$；阿基米德：$\mathbb R$ 上 $L=\pi^{-s/2}\Gamma(s/2)$，$\mathbb C$ 上 $L=(2\pi)^{1-s}\Gamma(s)$。
- 命题 3.5：$z_o=L^{-1}z$ 整、处处为基；归一化 $\operatorname{vol}(\mathcal O^\times)=1$ 使 $\langle z_o,f^o\rangle=1$。
- $z_o$ 的选取依赖 $\psi$ 与测度，但 $L$ 因子不依赖：换 $\psi$ 只改变 $\varepsilon$ 因子。

## 公式

$$
z(s,\omega;f)=\int_{F^\times}f(x)\,\omega\omega_s(x)\,d^\times x
$$

$$
z(s,\omega)=L(s,\omega)\,z_o(s,\omega),\qquad L(s,\omega)=(1-tq^{-s})^{-1}\ (\text{无分歧})
$$

$$
L(s,\omega)=\pi^{-s/2}\Gamma(s/2)\ (F=\mathbb R),\qquad L(s,\omega)=(2\pi)^{1-s}\Gamma(s)\ (F=\mathbb C)
$$

## 易错点

- 收敛域是 $\operatorname{Re}s>0$，不是 $\operatorname{Re}s>1$：局部积分靠 $f$ 的紧支性收敛；整体 Euler 乘积才需要 $\operatorname{Re}s>1$。
- 无分歧时不要漏掉 $(3.4)$ 的 $\tau=[1]-[\varpi^{-1}]$：正是它把 $z$ 的支集从 $\mathcal O$ 推到 $F^\times$，从而分离出 $1-tq^{-s}$ 因子。

## 批注

**〔背景直觉〕最大公分母**　书中注 $(3.9)$：$z(s,\omega;f)/L(s,\omega)=\langle z_o(s,\omega),f\rangle$ 对每个 $f$ 整、且对每个 $s$ 有 $f=f^o$ 使其非零。用初等说法：$L$ 是让所有 $z(s,\omega;f)$ 同时成为整函数的最小分母，故局部函数方程只能差一个 $\varepsilon$。

**〔易错预警〕$\omega_s$ 的记法**　§3 的 $\omega_s(x)=|x|^s$ 是「扭转」，与准特征 $\omega$ 的局部成分 $\omega_v$ 不是一回事；$z(s,\omega;f)$ 里的 $\omega\omega_s$ 读作「$\omega$ 扭 $|\cdot|^s$」，排印上两个 $\omega$ 容易混。

## 相关

[[ch6-quasi-character]]、[[ch6-local-equation]]、[[ch6-whittaker]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3 本征分布与 zeta 积分，原书 pp. 114–118（PDF pp. 119–123）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch06.tex:173-324`
