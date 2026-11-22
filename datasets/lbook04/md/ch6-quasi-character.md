# 准特征与 Hecke 特征

> `lbook04/concept/ch6-quasi-character` · 轨 T Tate 与迹公式 · 状态 reviewed · 核验 source-only

**问题：** 为什么要求准特征在主对角线 $k^\times$ 上平凡，而不只在某个子群上平凡？

**一句话：** 准特征是 $\mathbb A^\times\to\mathbb C^\times$ 的连续复特征、在 $k^\times$ 上平凡；它在每个位分解为局部特征之积，无分歧位由 $t_v=\omega_v(\varpi_v)$ 完全决定。

**别名：** `quasicharacter`、`Hecke character`、`Grössencharakter`

## 定义

定义 2.1：$\omega:\mathbb A^\times\to\mathbb C^\times$ 连续同态，且 $\omega|_{k^\times}=1$（$k$ 对角嵌入 $\mathbb A^\times$）。若 $\omega$ 取值在单位圆上则称特征；有限阶者恰对应 Dirichlet 特征（§1）。每个 $\omega$ 分解为 $\bigotimes_v\omega_v$，$k_v^\times=\mathcal O_v^\times\times\varpi_v^{\mathbb Z}$；$\omega_v$ 无分歧 $\iff$ 在 $\mathcal O_v^\times$ 上平凡 $\iff$ $\omega_v(x)=t_v^{\operatorname{ord}_v(x)}$。$L^S(s,\omega)=\prod_{v\notin S}(1-t_vq_v^{-s})^{-1}$ 在 $\operatorname{Re}s>1$ 绝对收敛。

**记号：** $\mathbb A$：阿代尔环；$\mathbb A^\times$：伊代尔群；$\omega_v$：局部成分；$t_v=\omega_v(\varpi_v)$；$S$：分歧位集；$q_v$：剩余域大小。

## 要点

- $(1.1)$ $\mathbb A^\times\cong k^\times\times\mathbb R^\times_+\times\widehat{\mathbb Z}^\times$（$k=\mathbb Q$）；分解不唯一（$\pm1$ 的二义），故只有对偶特征才良定义。
- 无分歧位：$\omega_v$ 由 $t_v$ 决定；分歧位：由导子 $c(\omega_v)$ 与在 $\mathcal O_v^\times$ 上的取值决定。
- Dirichlet 特征 $=$ 有限阶准特征；$\omega=1$ 时 $L(s,\omega)=\zeta_k(s)$（Dedekind zeta）。
- Hecke 的 Grössencharakter 就是这里的准特征；类域论把它与射线类群特征对应。

## 公式

$$
\omega:\mathbb A^\times\to\mathbb C^\times,\qquad \omega|_{k^\times}=1
$$

$$
\omega=\bigotimes_v\omega_v,\qquad \omega_v(x)=t_v^{\operatorname{ord}_v(x)}\ (v\notin S)
$$

$$
L^S(s,\omega)=\prod_{v\notin S}\bigl(1-t_v\,q_v^{-s}\bigr)^{-1}
$$

## 易错点

- $(1.1)$ 的分解不唯一：$\alpha\in k^\times$ 与 $\pm1$ 可同时调整，故「把 $\omega$ 写成 $\alpha tu$ 再取值」只在模掉二义后有意义。
- 无分歧形式 $t_v^{\operatorname{ord}}$ 只在 $v\nmid$ 导子时成立；分歧位必须保留 $\omega_v$ 在 $\mathcal O_v^\times$ 上的非平凡限制。

## 批注

**〔含糊点拨〕特征 vs 准特征**　中译注把 quasicharacter 统一译作「准特征」，但原书有时只把取值在 $\mathbb C^1$ 的叫 character；定义 2.1 用「连续复特征」统称，读到「特征」时看上下文是否要求 $|\omega|=1$。

**〔背景直觉〕为什么是 $\mathbb A^\times$ 而不是理想类群**　理想类群特征只看见有限位；$\mathbb A^\times$ 同时含阿基米德位与所有有限位，故能统一处理 $\Gamma$ 因子与导子。Tate 论文的全部技术就是把「和 over 理想」换成「$\mathbb A^\times$ 上的积分」。

## 相关

[[ch6-local-zeta]]、[[ch6-global-tate]]、[[ch7-automorphic-rep]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§1–§2，原书 pp. 110–113（PDF pp. 115–118）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch06.tex:22-172`
