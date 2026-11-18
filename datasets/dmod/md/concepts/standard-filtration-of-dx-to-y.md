---
id: dmod/concept/standard-filtration-of-dx-to-y
type: concept
track: D
---

# $\mathcal D_{X\to Y}$ 的标准滤过

> 把 $Y$ 上微分算子的阶滤过沿 $\varphi$ 拉回，得相对双模的标准滤过；分次化后只看见 $Y$ 的符号层，与 $T_X$ 无关。

**问题**：$\mathcal D_{X\to Y}$ 的滤过为什么由 $Y$ 的阶给出，分次化后又为什么只看见 $Y$ 的切层？

## 定义

设 $F_p\mathcal D_Y$ 是 $\mathcal D_Y$ 关于 $Y$ 上微分算子阶的滤过。定义 $$\mathcal D_{X\to Y}=\varphi^*(\mathcal D_Y),\qquad F_p\mathcal D_{X\to Y}=\varphi^*(F_p\mathcal D_Y)=\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}(F_p\mathcal D_Y).$$ 这是穷尽且分离的滤过，$F_p\mathcal D_{X\to Y}=0$（$p<0$），$F_0\mathcal D_{X\to Y}=\mathcal O_X$。由 $\mathcal D_Y=\mathcal O_Y\oplus J_Y$（$J_Y$ 是由切层 $T_Y$ 生成的左理想）得 $\mathcal D_{X\to Y}=\mathcal O_X\oplus\varphi^*(J_Y)$，即 $\operatorname{Gr}_0\mathcal D_{X\to Y}=\mathcal O_X$、$F_1/F_0\cong\varphi^*T_Y$。

*记号*：$d=\dim Y$；$D^I=D_1^{i_1}\cdots D_d^{i_d}$，$|I|=i_1+\dots+i_d$；$\operatorname{Gr}_p=F_p/F_{p-1}$；$\xi_j$：$D_j$ 的符号，$\operatorname{Gr}\mathcal D_Y=\operatorname{Sym}(T_Y)=k[\xi_1,\dots,\xi_d]$（局部）；$p_X,p_Y$：余切丛的投影。

## 要点

- 局部取 $\mathcal D_Y$ 的自由基 $D^I$（$I\in\mathbb Z_+^d$，$F_p\mathcal D_Y=\bigoplus_{|I|\le p}\mathcal O_YD^I$），则 $F_p\mathcal D_{X\to Y}=\bigoplus_{|I|\le p}\mathcal O_XD^I$，即滤过按 $Y$-方向的算子阶分层。
- 分次化只留住 $Y$-方向的符号：$\operatorname{Gr}\mathcal D_{X\to Y}\cong\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}\operatorname{Gr}\mathcal D_Y\cong\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}\operatorname{Sym}(T_Y)$，与 $T_X$ 无关。
- 左 $\mathcal D_X$-作用满足乘法估计 $F_p\mathcal D_X\cdot F_q\mathcal D_{X\to Y}\subset F_{p+q}\mathcal D_{X\to Y}$：坐标公式的第二项使一次 $\partial/\partial x_i$ 至多把 $Y$-阶抬高 $1$。
- 浸入 $i:Y\hookrightarrow X$ 的适应坐标下，$i_+V=i_\bullet(V\otimes_{\mathcal D_Y}\mathcal D_{Y\to X})$ 的滤过 $F_p=\bigoplus_{s+|I|\le p}F_sV\otimes D^I$（$I$ 只取法向）给出 $\operatorname{Gr}(i_+V)\cong\operatorname{Gr}V\otimes_kk[\xi_{m+1},\dots,\xi_n]$，这是定理 4.6.8 计算特征簇的入口。

## 关键公式

- $F_p\mathcal D_{X\to Y}=\varphi^*(F_p\mathcal D_Y)$
- $\operatorname{Gr}\mathcal D_{X\to Y}\cong\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}\operatorname{Gr}\mathcal D_Y$
- $F_p\mathcal D_{X\to Y}=\bigoplus_{|I|\le p}\mathcal O_XD^I,\qquad F_p\mathcal D_Y=\bigoplus_{|I|\le p}\mathcal O_YD^I$
- $F_p\mathcal D_X\cdot F_q\mathcal D_{X\to Y}\subset F_{p+q}\mathcal D_{X\to Y}$
- $\operatorname{Gr}_p(i_+V)=\bigoplus_{s+|I|=p}\operatorname{Gr}_sV\otimes_k\xi^I,\qquad I\in\{0\}\times\mathbb Z_+^{n-m}$

## 定理与证明

### 标准滤过的分次化（由 §1 的滤过定义与 §6 的适应坐标得到）（完整）

$F_p\mathcal D_{X\to Y}=\varphi^*(F_p\mathcal D_Y)$ 是穷尽、分离的滤过，且 $\operatorname{Gr}\mathcal D_{X\to Y}\cong\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}\operatorname{Gr}\mathcal D_Y$；局部上 $F_p\mathcal D_{X\to Y}=\bigoplus_{|I|\le p}\mathcal O_XD^I$。

1. 局部取 $\mathcal D_Y$ 关于阶滤过的自由基：$\mathcal D_Y=\bigoplus_I\mathcal O_YD^I$，$F_p\mathcal D_Y=\bigoplus_{|I|\le p}\mathcal O_YD^I$。  
   *为什么*：$\mathcal D_Y$ 局部自由于 $\mathcal O_Y$，阶滤过按基元素的阶分层，这是 §5 中 Bernstein 滤过的标准形式。
2. $\varphi^*$ 与直和交换且 $\mathcal O_X$ 在 $\varphi^{-1}\mathcal O_Y$ 上平坦，故 $\varphi^*(F_p\mathcal D_Y)=\bigoplus_{|I|\le p}\mathcal O_XD^I$，滤过穷尽且分离。  
   *为什么*：光滑态射使 $\mathcal O_X$ 成为平坦 $\varphi^{-1}\mathcal O_Y$-模，平坦模与直和、与滤过的逐层取交都相容。
3. 逐次取商得 $\operatorname{Gr}_p\mathcal D_{X\to Y}=\bigoplus_{|I|=p}\mathcal O_XD^I\cong\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}\operatorname{Gr}_p\mathcal D_Y$，汇总即 $\operatorname{Gr}\mathcal D_{X\to Y}\cong\mathcal O_X\otimes_{\varphi^{-1}\mathcal O_Y}\varphi^{-1}\operatorname{Gr}\mathcal D_Y$。  
   *为什么*：分次化逐次取商，而 $\operatorname{Gr}_p$ 的计算在第 2 步的直和分解上逐项进行，张量积与直和交换。
4. 把 $\operatorname{Gr}\mathcal D_Y$ 识别为 $\operatorname{Sym}(T_Y)$，并用坐标公式 $\partial/\partial x_i(P\otimes S)=\partial P/\partial x_i\otimes S+\sum_jP\,\partial(y_j\circ\varphi)/\partial x_i\otimes\partial S/\partial y_j$ 逐项数阶，得乘法估计 $F_p\mathcal D_X\cdot F_q\mathcal D_{X\to Y}\subset F_{p+q}\mathcal D_{X\to Y}$。  
   *为什么*：公式的第一项不改变 $Y$-阶，第二项至多抬高 $1$，故 $X$-阶为 $p$ 的算子作用后 $Y$-阶至多增加 $p$。

*出处*：§1（第 36–47、173–175 行）与 §6（引理 4.6.2、4.6.3）的综合 / 原书 p.99、p.115


## 易错点

- $F_p\mathcal D_{X\to Y}$ 是 $Y$-方向的阶，不是 $X$-方向的阶：$\mathcal D_{X\to Y}$ 不是 $\mathcal D_X$，其滤过也不由 $X$ 的向量场阶给出。
- 分次化后的 $\operatorname{Gr}\mathcal D_{X\to Y}$ 只依赖 $\varphi^{-1}T_Y$，与 $T_X$ 无关；用 $T_X$ 写 $\operatorname{Gr}$ 等于把 $\mathcal D_{X\to Y}$ 误当成 $\mathcal D_X$。
- 左 $\mathcal D_X$-作用不保持单个 $F_q$：$\partial/\partial x_i$ 可把 $Y$-阶抬高 $1$，能用的只有乘法估计 $F_p\cdot F_q\subset F_{p+q}$。
- 浸入情形基底 $D^I$ 只取法向指标（$I\in\{0\}\times\mathbb Z_+^{n-m}$），把切向指标也算进 $I$ 会使基重复计数。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§1 双模 $\mathcal D_{X\to Y}$ 的滤过，p.99-100-101-102（PDF p.105-106-107-108），`源码/chapters/chap4.tex:36-47（$\mathcal D_{X\to Y}=\mathcal O_X\oplus\varphi^*(J_Y)$）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§1 坐标作用公式，p.99-100（PDF p.105-106），`源码/chapters/chap4.tex:173-175（$\partial/\partial x_i(P\otimes S)$ 的公式）`
- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§6 浸入的适应坐标与基，p.115-116（PDF p.121-122），`源码/chapters/chap4.tex:830-845（引理 4.6.3）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/order-filtration-of-dn`
- `dmod/concept/bimodule-dx-to-y`
- `dmod/concept/direct-image-of-immersion`
