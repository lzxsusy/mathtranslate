# 't Hooft 算符

> `gtgl15/concept/thooft-operator` · 轨道 D · 't Hooft 算符与赫克修正 · 状态 dev

> **先自测**：为什么一个带奇点的线算符，在 2d 有效描述里恰好等于“在 $p$ 处做一次赫克修正”？

## 一句话

't Hooft 算符是带 Dirac 单极奇点的磁线算符；一般 $G$ 由同态 $U(1)\to G$（GNO 对偶权）分类，在 $\Sigma\times C$ 描述里它变成 $p$ 处的赫克修正。

## 定义

Wilson 半 BPS 线算符是 $W({}^LR,S)=\operatorname{Tr}_{{}^LR}P\exp(-\oint_S(\mathcal A+i\varphi))$（eq (4.8)）。't Hooft 算符在其支撑线附近引入奇点：$U(1)$ 电荷 1 的情形的经典解为 $F=\frac{i}{2}\star_3\frac{1}{|\vec x|}$、$\varphi=\frac{i}{2|\vec x|}ds$（eq (4.9)）。一般 $G$ 的磁荷由同态 $\rho:U(1)\to G$ 的同伦类（等价地 ${}^LG$ 的支配最高权/不可约表示 ${}^LR$）分类，这是 GNO 对偶。在 $\Sigma\times C$ 的 3d 有效描述（$I\times C$）中，超对称方程约化为 Bogomolny 方程 $F=\star D\varphi_s$（eq (4.11)）；进一步化为复方程 $[D_i,D_j]=0$（eq (4.15)）与 $\mu=0$（eq (4.16)）。由 $[D_1,D_2]=0$ 得 $\bar D_z$ 与 $y$ 无关（eq (4.17)），故 $\bar\partial$ 只在插入点 $p$ 处跳变，去掉 $p$ 后平凡——这正是赫克修正。

**记号**：$T({}^Lw,p)$；$\rho:U(1)\to G$；${}^Lw$；$p$；Bogomolny 方程；$\mu$。

## 要点（为什么需要它）

1. 't Hooft 算符 = 线算符 + 单极奇点：不仅有 $F$ 的奇点，$\varphi$ 也必须奇异（eq (4.9)）。
2. 磁荷分类由 GNO：$U(1)\to G$ 的同态类 ↔ ${}^LG$ 的支配最高权 ↔ 不可约表示 ${}^LR$。
3. 在 2d 有效描述中，'t Hooft 算符对应 $p\in C$ 处全纯结构的跳变，即赫克修正。
4. 超对称方程化成两个复方程（eq (4.15)(4.16)），这是证明“'t Hooft = Hecke”的技术核心。
5. 包含 Higgs 场时（$\S4.5$）修正还要求 $\varphi$-不变，把 Hecke 修正限制在谱覆盖的 $N$ 个点上。

## 核心公式

$$
$$W({}^LR,S)=\operatorname{Tr}_{{}^LR}P\exp\left(-\oint_S(\mathcal A+i\varphi)\right)$$$$F=\star D\varphi_s,\qquad [D_i,D_j]=0,\qquad \mu=\sum_i[D_i,D_i^\dagger]=0$$
$$

$$
$$F=\star D\varphi_s,\qquad [D_i,D_j]=0,\qquad \mu=\sum_i[D_i,D_i^\dagger]=0$$
$$

## 定理与证明（或缺口）

### 't Hooft 算符等价于赫克修正

在 $p$ 处插入 't Hooft 算符，等价于在 $p$ 处对全纯丛做一次类型由 ${}^LR$ 决定的赫克修正。

> 证明状态：**sketch**。原文给出主要步骤；非 minuscule 权时的 monopole bubbling 未处理。

出处：`A p.41`

## 常见误解

- 't Hooft 算符不是纯磁单极子：它带 $\varphi$ 的奇点，且是线算符不是粒子。
- 磁荷不是用 $H^2$ 或 $\pi_1$ 随便标的：GNO 用 $U(1)\to G$ 的同态类，半单情形对应 ${}^LG$ 的支配权。
- 在 4d 中 't Hooft 与 Wilson 不能同时局部对角化；它们对偶，不是同一组算符。
- $p$ 必须是谱覆盖的非分歧点、$\varphi(p)$ 正则半单，本文才给出干净的赫克修正；否则有 bubbling。

## 相关卡

[赫克修正与赫克变换](../concepts/hecke-modification.md) · [线算符](../concepts/line-operators.md) · [磁本征膜](../concepts/magnetic-eigenbranes.md) · [谱覆盖、判别式与分歧除子](../concepts/spectral-cover.md) · ['t Hooft 算符 $\leftrightarrow$ $p$ 处赫克修正（$U(1)$）](../derivations/thooft-hecke-u1.md)

## 出处（印刷页）

- A p.39–43（A p.41 eq (4.12)）
- A p.40（A p.40 eq (4.10)）
- A p.48–54（A p.49 eq (4.34)）

> 说明：A=原文 $\S4.3$ 的 eq (4.8)–(4.17) 与 GNO 分类、$\S4.5$ 的 $\varphi$-不变条件；B=把“'t Hooft = Hecke”整理成三步；C=非 minuscule 的边界按 $\S4.5.3$ 的说明补。最没把握处：eq (4.16) 的 moment map 与复方程的等价性原文只给结论。
