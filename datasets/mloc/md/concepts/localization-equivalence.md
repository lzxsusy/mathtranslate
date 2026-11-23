# 局部化等价 $\mathcal{M}_{qc}(D_\lambda)\simeq\mathcal{M}(U_\theta)$

> `mloc/concept/localization-equivalence` · type=concept · track=D · status=draft · verification=source-only

**别名**：localization equivalence、局部化等价、第 3 章定理 1.2、第 3 章推论 1.3、第 3 章定理 1.12

## 摘要

反支配时 $Q\circ\Delta_\lambda$ 是商范畴等价；反支配且正则时 $\Delta_\lambda$ 与 $\Gamma$ 互逆；正则时导出范畴也等价。

## 问题

什么时候每个拟凝聚 $D_\lambda$-模都来自 $U_\theta$-模？局部化在导出范畴上是否也是等价？

## 定义

局部化等价是第 3 章的主定理：在 $\lambda$ 反支配（且正则）时，$\Delta_\lambda$ 与 $\Gamma$ 互为逆函子，$D_\lambda$-模的表示论完全由 $U_\theta$-模决定。反支配保证单位同构与 $\Gamma$ 正合；正则保证每个对象由整体截面生成，从而可以去掉商范畴。

记号：$Q\mathcal{M}_{qc}(D_\lambda)$ 是对「整体截面为零的拟凝聚 $D_\lambda$-模」子范畴取的商范畴，$Q$ 是商函子；$\Phi_\lambda:D(D_\lambda)\to D_{qc}(\mathcal{M}(D_\lambda))$ 是导出范畴的等价；$D^b_{fg}(U_\theta)$、$D^b_{coh}(D_\lambda)$ 分别是有界有限生成/凝聚导出范畴。

## 要点

- 反支配（$n(\lambda)=0$）时 $\Gamma$ 正合、$\varphi$ 同构，但 $\psi$ 只在商范畴中同构；故先得 $Q\circ\Delta_\lambda$ 的等价（第 3 章定理 1.2）。
- 若 $\lambda$ 还正则，C.4.4 保证每个拟凝聚 $D_\lambda$-模由整体截面生成，商范畴还原为 $\mathcal{M}_{qc}(D_\lambda)$，得第 3 章推论 1.3 的等价。
- 导出范畴层面只需 $\lambda$ 正则：$L\Delta_\lambda:D(U_\theta)\to D(D_\lambda)$ 是等价，逆 $R\Gamma$（第 3 章定理 1.12）；有界情形给出 $D^b(U_\theta)\simeq D^b(D_\lambda)$。
- 第 3 章定理 1.6 是另一条等价：$\Phi_\lambda:D(D_\lambda)\to D_{qc}(\mathcal{M}(D_\lambda))$，把 $D_\lambda$-模的导出范畴与上同调拟凝聚的复形范畴等同。
- 有限性版本：$\lambda$ 反支配且正则时 $\Delta_\lambda:\mathcal{M}_{fg}(U_\theta)\to\mathcal{M}_{coh}(D_\lambda)$ 等价（第 3 章命题 1.18）；正则时 $L\Delta_\lambda:D^b_{fg}(U_\theta)\to D^b_{coh}(D_\lambda)$ 等价（第 3 章定理 1.21）。

## 公式

$$$Q\circ\Delta_\lambda:\mathcal{M}(U_\theta)\xrightarrow{\ \sim\ }\mathcal{QM}_{qc}(D_\lambda)\qquad(\lambda\ \text{反支配})$$$

$$$\mathcal{M}(U_\theta)\simeq\mathcal{M}_{qc}(D_\lambda)\qquad(\lambda\ \text{反支配且正则})$$$

$$$L\Delta_\lambda:D(U_\theta)\xrightarrow{\ \sim\ }D(D_\lambda),\qquad R\Gamma\ \text{为其逆}\qquad(\lambda\ \text{正则})$$$

$$$D^b(U_\theta)\simeq D^b(D_\lambda),\qquad D^b_{fg}(U_\theta)\simeq D^b_{coh}(D_\lambda)$$$

## 相关定理

### 第 3 章定理 1.2（反支配时的商范畴等价）

设 $\lambda\in\mathfrak{h}^*$ 反支配。则 $Q\circ\Delta_\lambda:\mathcal{M}(U_\theta)\to Q\mathcal{M}_{qc}(D_\lambda)$ 是范畴等价，其逆为 $\Gamma$。

证明状态：`complete`

1. $\lambda$ 反支配时，第 3 章引理 1.1 给出 $\varphi_V:V\to\Gamma\Delta_\lambda(V)$ 对一切 $V$ 同构。
   - 为什么：第 3 章引理 1.1 的假设正是 $\lambda$ 反支配。
2. 余单位 $\psi_W:\Delta_\lambda\Gamma(W)\to W$ 的核 $K$ 与余核 $C$ 满足 $\Gamma(K)=\Gamma(C)=0$，故 $Q(\psi_W)$ 是同构。
   - 为什么：$\Gamma$ 正合（第 2 章推论 3.2），对 $0\to K\to\Delta\Gamma W\to W\to C\to0$ 取 $\Gamma$，用 $\Gamma\Delta\Gamma W\cong\Gamma W$ 与五引理。
3. $\varphi$ 与 $Q\psi$ 互为逆（在商范畴中），故 $Q\Delta_\lambda$ 是等价，逆为 $\Gamma$。
   - 为什么：三角恒等式 $\Gamma\varphi=\mathrm{id}$、$Q(\psi)\circ Q(\Delta\eta)=\mathrm{id}$ 给出。

### 第 3 章推论 1.3（反支配正则时的范畴等价）

设 $\lambda\in\mathfrak{h}^*$ 反支配且正则。则 $\Delta_\lambda:\mathcal{M}(U_\theta)\to\mathcal{M}_{qc}(D_\lambda)$ 是范畴等价，逆为 $\Gamma$。

证明状态：`sketch`

1. $\lambda$ 正则时，C.4.4 保证每个拟凝聚 $D_\lambda$-模由整体截面生成，故没有整体截面为零的非零对象，$Q$ 在 $\mathcal{M}_{qc}(D_\lambda)$ 上为等价。
   - 为什么：正则使 $\psi_W$ 的核与余核必为零，商范畴还原。
2. 于是第 3 章定理 1.2 的 $Q\circ\Delta_\lambda$ 等价给出 $\Delta_\lambda$ 本身的等价。
   - 为什么：$Q$ 已是等价，复合等价当且仅当 $\Delta_\lambda$ 等价。

> 缺口：第 3 章推论 1.3 的关键一步依赖 C.4.4：$\lambda$ 反支配且正则时每个拟凝聚 $D_\lambda$-模由整体截面生成。C.4.4 指参考文献 [9]、[10] 所载的未刊讲义（译本 annote ch03a.tex:39-41 说明本书无附录、编号照录），本卡只引用该结论，未展开其证明。

### 第 3 章定理 1.6（导出范畴的等价 $\Phi_\lambda$）

设 $\lambda\in\mathfrak{h}^*$。则 $\Phi_\lambda:D(D_\lambda)\to D_{qc}(\mathcal{M}(D_\lambda))$ 是范畴等价。

证明状态：`sketch`

1. 用平移把 $\lambda$ 化到反支配正则的情形；平移是范畴等价且保持拟凝聚性。
   - 为什么：平移原理（第 2 章引理 2.1、2.2 与 $V(\mu)$）允许改变 $\lambda$。
2. 反支配正则时 $\Delta_\lambda$ 正合且与 $\Gamma$ 互逆（第 3 章推论 1.3），导出范畴上 $\Phi_\lambda$ 为等价。
   - 为什么：阿贝尔范畴等价诱导导出范畴等价。
3. 平移回来即得一般 $\lambda$。
   - 为什么：等价在平移下保持。

> 缺口：第 3 章定理 1.6 的证明在译本 ch03a.tex:113-123：经平移设 $\lambda$ 反支配正则后，构造自然态射并用 C.4.1 判定它是拟同构。C.4.1 指参考文献 [9]、[10] 的未刊讲义（annote ch03a.tex:39-41），本书无附录；本卡的三步骨架只保留平移归约，未展开 C.4.1 的判定准则。

### 第 3 章定理 1.12（正则时的导出等价）

设 $\lambda\in\mathfrak{h}^*$ 正则。则 $L\Delta_\lambda:D(U_\theta)\to D(D_\lambda)$ 是范畴等价，逆为 $R\Gamma$。

证明状态：`sketch`

1. 对 $V^\bullet\in D(D_\lambda)$ 取 $\Gamma$-零调消解 $C^\bullet$，对 $\Gamma(C^\bullet)$ 取投射消解 $P^\bullet$，构造自然态射 $L\Delta_\lambda R\Gamma(V^\bullet)=\Delta_\lambda(P^\bullet)\to C^\bullet$。
   - 为什么：消解的存在性与 $L\Delta_\lambda$、$R\Gamma$ 的定义。
2. 由第 3 章定理 1.6 与第 3 章引理 1.11，$R\Gamma\circ L\Delta_\lambda\cong\mathrm{id}$；再检查 $R\Gamma(\psi_{V^\bullet})$ 是拟同构。
   - 为什么：第 3 章引理 1.11：$\lambda$ 正则时 $R\Gamma L\Delta_\lambda\cong\mathrm{id}$ 于 $D(U_\theta)$。
3. 由 C.4.1，$\psi$ 是函子同构，故 $L\Delta_\lambda$ 与 $R\Gamma$ 互逆。
   - 为什么：C.4.1 是同构判定准则。
4. 取有界复形得 $D^b(U_\theta)\simeq D^b(D_\lambda)$；有限生成/凝聚情形由第 3 章定理 1.21 给出。
   - 为什么：等价保持有界性与有限生成性。

> 缺口：第 3 章定理 1.12 的证明在译本 ch03a.tex:167-175：构造 $\psi:L\Delta_\lambda R\Gamma\to\mathrm{id}$，再用 C.4.1 判定 $\psi$ 是函子同构。C.4.1 为外部未刊讲义（annote ch03a.tex:39-41），本卡未展开该判定准则，故标 sketch。

## 易错点

- 阿贝尔范畴的等价需要 $\lambda$ 同时反支配与正则；只正则时只有导出范畴等价（第 3 章定理 1.12），不要混用。
- 反支配但非正则时，$\Delta_\lambda$ 不是 $\mathcal{M}_{qc}$ 上的等价，只能在商范畴 $Q\mathcal{M}_{qc}$ 中成立（第 3 章定理 1.2）。
- $Q$ 是商函子，$Q\mathcal{M}_{qc}$ 的对象不是普通模；把第 3 章定理 1.2 写成「$\mathcal{M}_{qc}$ 等价」会丢掉「整体截面为零」的障碍。
- $D_\lambda=D_{X,\lambda+\rho}$；平移与等价都在这个约定下成立，换回第 1 章记号时 $\rho$ 要同步移动。

## 相关卡

- `mloc/concept/localization-functor-delta`
- `mloc/concept/global-sections-functor`
- `mloc/concept/nonvanishing-theorem`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · §1 局部化等价 · p.[36, 37, 38, 39]（PDF [40, 41, 42, 43]） · `源码/chapters/ch03a.tex:51-63（第 3 章定理 1.2、第 3 章推论 1.3）、ch03a.tex:113-123（第 3 章定理 1.6）、ch03a.tex:167-175（第 3 章定理 1.12）`
