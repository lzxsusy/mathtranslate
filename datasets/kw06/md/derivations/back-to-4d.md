# 三类膜回到四维：§12 检查表

> `kw/deriv/back-to-4d` · 轨道 E · Langlands 与翻译器 · 状态 dev · 8 步

> **要回答的问题**：怎样从四维超对称的边界条件反推出三类膜，每一种膜由哪个对合 $T$ 产生？

## 一句话

回到四维半空间 $\mathbb R^2_+\times C$：用对合 $T$ 猜费米子边界条件，由 $\delta\lambda$ 推出玻色条件，再检验超流法向消失，得到 $(B,B,B)$ 零膜、$(B,A,A)$ Hitchin 纤维与 $(A,B,A)$ c.c. 膜三类边界条件。

## 目标

用四步法逐个构造零膜、Hitchin 纤维膜与 c.c. 膜，并说明各自的边界条件与几何支撑。

## 前提

- B p.208：四维理论在 $\mathbb R^2_+\times C$ 上，边界为 $x^1=0$。
- B p.210 eq (12.6)：超流 $J_I=\frac12\Gamma^{KL}F_{KL}\Gamma_I\lambda$，边界条件要求 $\varepsilon J_1=0$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 四步法：选一个对合 $T$（猜费米子边界条件 $T\lambda\|=\pm\lambda\|$），由 $(T\mp1)\delta\lambda=0$ 与 $\delta\lambda=\frac12\Gamma^{IJ}F_{IJ}\varepsilon$ 推出玻色边界条件，最后验证超流法向分量消失并寻找超对称态。 | 这条流程把「猜边界条件」变成可检验的算法，避免从头解超对称变分。 | `B p.210` | A·原文明确写了 |
| 2 | 取 $T=\Gamma^{04}$、$T\lambda\|=\lambda\|$：$(T-1)\delta\lambda=0$ 给 $F_{0I}+F_{4I}=0$（(12.11)），对应玻色条件 $A_0+A_4=0$（零方向）与其余方向 Dirichlet。 | 费米子条件通过 $\delta\lambda$ 的 $F$ 依赖直接翻译成规范场的组合条件。 | `B p.211 eq (12.11)` | A·原文明确写了 |
| 3 | 超对称态要求 $F$ 在 $(2,3,6,7)$ 平面自对偶，即 (12.16)：$F_{23}-F_{67}=0$、$F_{27}-F_{36}=0$、$F_{26}-F_{73}=0$；这正是 Hitchin 方程，故边界值就是 $M_H$ 上一点 $p$ 的零膜。 | 零膜是 $(B,B,B)$ 型：它在三种复结构下都是复子流形，而 Hitchin 方程恰好刻画出这一点。 | `B p.213 eq (12.16)` | A·原文明确写了 |
| 4 | 第二构造取 $\tilde T=T\Gamma^{2367}=\Gamma^{023467}$、$\tilde T\lambda\|=-\lambda\|$：得到 (12.17)-(12.19) 的边界条件（1589 平面反自对偶），在平坦时空保 8 个超荷，但奇异点处两个构造可能不等价。 | 这显示同一个物理解可以有多种四维提升，暗示边界条件不是唯一确定的。 | `B p.214 eq (12.17)` | A·原文明确写了 |
| 5 | 用 $S$ 变换 $\varepsilon_l\mapsto\varepsilon_l e^{-\ii\pi/4}$、$\varepsilon_r\mapsto\varepsilon_r e^{\ii\pi/4}$ 并投影 $\varepsilon'=(1+\hat\Gamma)/\sqrt2\,\varepsilon$（$\hat\Gamma=\Gamma^0\Gamma^1\Gamma^2\Gamma^3$），得 $T'=\Gamma^1\Gamma^2\Gamma^3\Gamma^4$；$T'\lambda\|=-\lambda\|$ 给出 (12.20)-(12.24)：$F_{0I}\|=0$（$I>4$）、$A_5=A_8=A_9=0$、$[\varphi_2,\varphi_3]=F_{67}=0$、$\varphi_z$ 特征多项式 Dirichlet 固定。 | $S$ 对偶把原来的边界条件换成另一组，正是寻找 $(B,A,A)$ 膜的必经之路。 | `B p.215 eq (12.20)` | A·原文明确写了 |
| 6 | 再要求 $\Gamma^{2367}\varepsilon=\varepsilon$ 的超荷不变，得 $F_{26}-F_{73}=F_{27}-F_{36}=0$，即 $D_{\bar z}\varphi_z=0$（(12.26)）；于是膜的支撑是特征多项式的纤维，即 Hitchin 纤维 $F$，类型为 $(B,A,A)$。 | $D_{\bar z}\varphi_z=0$ 说明 $(E,\varphi)$ 是 Higgs 丛，其模空间正是 $M_H$，故支撑自然是 Hitchin 纤维。 | `B p.216 eq (12.26)` | A·原文明确写了 |
| 7 | 混合构造取 $T'=-\Gamma^{15}\Gamma^{2-7}\Gamma^{3+6}$（同时旋转 $x^2\text{-}x^3$ 与 $x^6\text{-}x^7$ 平面）：$T'\lambda\|=\lambda\|$ 给 $A_2-\varphi_3$、$A_3+\varphi_2$ 固定而 $A_2+\varphi_3$、$A_3-\varphi_2$ 自由，即 $W'=\{A_z+\ii\varphi_z\ \text{固定}\}$（(12.28)）；$W'$ 在 $J$ 中复且对 $\Omega_J$ 拉格朗日，故给 $(A,B,A)$ 膜。 | 复性与拉格朗日性同时成立，才符合 $(A,B,A)$ 型的定义（$J$ 中 A-膜、$I,K$ 中 B-膜）。 | `B p.217 eq (12.28)` | A·原文明确写了 |
| 8 | 对 $W'$ 作 $S$ 对偶：$\hat T=\frac12(1+\hat\Gamma)T'(1-\hat\Gamma)=-(\Gamma^{15}/\sqrt2)\big[(\Gamma^{26}+\Gamma^{37})-\hat\Gamma(\Gamma^{23}+\Gamma^{67})\big]$，其 $\hat T\lambda\|=-\lambda\|$ 给 (12.31) 的修正 Neumann 与 $F_{0J}=0$（$J=4,8,9$）；丢大质量分量后得 (12.32)，与 σ-模型混合边界比较可知 (12.33)-(12.34) 中 $f_{MN}=\omega_{MN}$，即目标空间规范场 $f=\omega_J$。 | 最后这条等式说明 $(A,B,A)$ 膜在四维提升下的边界条件由 $\omega_J$ 完全确定，与超引力中的一般混合边界条件一致。 | `B p.220 eq (12.34)` | A·原文明确写了 |

## 结论

四步法给出三类膜：$T=\Gamma^{04}$ 给 $F$ 在 $(2,3,6,7)$ 自对偶即 Hitchin 方程，对应 $M_H$ 上一点的 $(B,B,B)$ 零膜；$S$ 对偶后的 $T'=\Gamma^1\Gamma^2\Gamma^3\Gamma^4$ 给 $D_{\bar z}\varphi_z=0$，支撑在 Hitchin 纤维上的 $(B,A,A)$ 膜；混合对合 $T'=-\Gamma^{15}\Gamma^{2-7}\Gamma^{3+6}$ 给 $W'=\{A_z+\ii\varphi_z\ \text{固定}\}$ 上的 $(A,B,A)$ 膜，其目标空间规范场 $f=\omega_J$。

## 缺口

- 经典条件 $[\varphi_2,\varphi_3]=F_{67}=0$ 与 $M_H$ 定义中的 $[\varphi_2,\varphi_3]-F_{23}=0$ 之差被解释为 IR 量子修正，原文未证明（B p.216）。
- 时间反演下 Chan-Paton 丛只允许平凡或二阶平坦丛，这一限制原文只作讨论未定论（B p.217）。

## 最容易讲错的地方

- $(12.28)$ 在印刷页 217，不在 218；引用时容易差一页。
- 三类膜的型别是 $(B,B,B)$ 零膜、$(B,A,A)$ Hitchin 纤维、$(A,B,A)$ c.c. 膜；原文 p.184、p.198 有两处把 $(B,A,A)$ 误写成 $(A,B,A)$。
- $T$、$T'$ 与 $T'=-\Gamma^{15}\Gamma^{2-7}\Gamma^{3+6}$ 是三个不同的对合，给出三类不同的膜，不要混用。

## 相关卡

[c.c. A-膜、开弦代数与 A-膜→D-模](../derivations/a-to-dmod.md) · [Ψ ≠ 0：λ-连接与扭化 D-模](../derivations/psi-lambda.md) · [BPS 态](../concepts/bps-state.md) · [拓扑扭化](../concepts/topological-twist.md)

## 出处（印刷页）

- B p.207–220（B p.211 eq (12.11)）

> 说明：steps 的 provenance 分布：A×8（共 8 步）；gaps 2 条、pitfalls 3 条。
