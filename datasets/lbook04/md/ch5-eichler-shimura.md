# Eichler–Shimura 同余与模性

> `lbook04/concept/ch5-eichler-shimura` · 轨 L L 函数 · 状态 reviewed · 核验 source-only

**问题：** Eichler–Shimura 关系 $\widetilde T_p=F+V$ 为什么能推出模曲线 $L$ 函数分解成本征形式 $L$ 函数的乘积？

**一句话：** 在 $X_0(N)$ 的 Tate 模上，Hecke 算子 $\widetilde T_p$ 等于 Frobenius $F$ 加其对偶 $V$；于是 $T_p$ 的特征值 $a_p$ 正是曲线 Frobenius 特征值之和，从而 $L(X_0(N),s)=\prod_i L(f_i,s)$。

**别名：** `Eichler–Shimura 关系`、`$\widetilde T_p=F+V$`、`模性定理`

## 定义

设 $p\nmid N\ell$。$\varphi:E\to E^{(p)}$ 为 $p$ 次 Frobenius，$\widetilde\varphi$ 为其对偶（Verschiebung），在 $V_\ell$ 上 $F=\varphi_*$，$V=\widetilde\varphi_*$，$FV=VF=p$。Eichler–Shimura 同余说 $\widetilde T_p=F+V$（$(5.5)$）。由 Weil 1948（曲线的 RH）$F$ 的特征值 $\lambda_i,\bar\lambda_i$ 满足 $|\lambda_i|=\sqrt p$，于是 $a_{p,i}=\lambda_i+\bar\lambda_i$；代 $t=p^{-s}$ 得 $L(X_0(N),s)=\prod_i L(f_i,s)$（推论 5.2；坏位由 Carayol 的局部计算补上）。

**记号：** $X_0(N)=\overline{\Gamma_0(N)\backslash\mathfrak H}$：模曲线；$J_0(N)=\operatorname{Jac}(X_0(N))$；$V_\ell=T_\ell J_0\otimes\mathbb Q_\ell$；$F,V$：Frobenius 与 Verschiebung；$\widetilde T_p$：Tate 模上的 Hecke 算子。

## 要点

- $F$ 是 $p$ 次 Frobenius 的诱导映射，$V$ 是对偶同源 $\widetilde\varphi$ 的诱导；$FV=VF=p$。
- $\widetilde T_p=F+V$ 把几何 Frobenius 与 Hecke 对应联系起来，是「同余关系」的精确形式。
- 曲线 RH（Weil 1948）：$|\lambda_i|=\sqrt p$，故 $|a_{p,i}|\le2\sqrt p$，与 §3.1 的 Hasse 界一致。
- 推论 5.2：$L(X_0(N),s)=\prod_i L(f_i,s)$；坏位因子是 Carayol 的贡献，不能由 $(5.5)$ 直接取 $p\mid N$ 得到。

## 公式

$$
\widetilde T_p=F+V,\qquad FV=VF=p
$$

$$
\prod_i(1-\lambda_i p^{-s})(1-\bar\lambda_i p^{-s})=\prod_i(1-a_{p,i}p^{-s}+p^{1-2s})
$$

$$
L(X_0(N),s)=\prod_i L(f_i,s)
$$

## 易错点

- $F$ 的次数是 $p$、$V$ 是 $1$（对偶同源），不要写成两个同次数映射；特征值乘积为 $p$ 正来自这一点。
- 推论 5.2 的坏位不是逐位代入 $(5.6)$，需要 Carayol 的局部计算；只读好位会漏掉导子处的一致性。

## 批注

**〔背景直觉〕$\lambda+\bar\lambda$ 从哪来**　$V=pF^{-1}$ 在 $V_\ell$ 上成立，故 $\widetilde T_p$ 的特征值就是 $\lambda+\bar\lambda$；与 §3.1 的 $a_p$ 对照，这正好把「模形式的 Hecke 特征值」翻译成「曲线的 Frobenius 迹」。

**〔易错预警〕$\ell$ 与 $p$ 的选取**　$(5.5)$ 的证明取 $p\nmid N\ell$；$p=\ell$ 时 $F,V$ 退化，需另作处理。推论 5.2 的乘积对全部 $p$ 成立，但坏位因子由 Carayol 的局部模型算出。

## 相关

[[ch5-elliptic-l]]、[[ch5-hecke-eigenform]]、[[ch5-gross-zagier]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§5.1–5.2，原书 pp. 104–105（PDF pp. 109–110）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:489-562`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§6.2，原书 pp. 107（PDF pp. 112）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch05.tex:579-605`
