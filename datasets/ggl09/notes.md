# 09 Witten《Geometric Langlands and the Equations of Nahm and Bogomolny》

arXiv:0905.4795v2（2009-11-06；v1 2009-05-29），37 页。PDF 页序 = 印刷页，p.1 为标题页。

## 一、文章骨架

| 节 | 页 | 一句话 |
|---|---|---|
| §1 Introduction | 1–6 | 把几何 Langlands 的 't Hooft 算子翻译成 $N(\rho)$ 上的特征类，并给出卷积分裂 (1.8)。 |
| §1.1 dual group | 1–2 | $\mathrm{Hom}(T^\vee,U(1))=\mathrm{Hom}(U(1),T)$ 把最高权变成 $U(1)\to T$ 的 clutching 函数。 |
| §1.2 example | 2–3 | $SU(N)/PSU(N)$：$E_\rho$ 是平凡丛在 $p$ 的 Hecke 修改，$N(\rho)$ 是仿射 Grassmannian 的 Schubert cell。 |
| §1.3 principal SL2 | 3 | $h=\mathrm{diag}(N-1,N-3,\ldots)$ 生成 $G^\vee_\mathbb C$ 的主 $\mathrm{SL}_2$ 极大环面，degree 分级即其作用。 |
| §1.4 characteristic classes | 4–5 | $\mathfrak g=\oplus J_i$、$\dim J_i=2d_i-1$；$x_i$ 的次数为 $2d_i-2$，degree 2 的对偶到升算子 $f$。 |
| §1.5 convolution/OPE | 5–6 | $R^\vee_\alpha\otimes R^\vee_\beta$ 的分解 (1.7) 给出 $H^*(N(\rho))$ 的卷积分裂 (1.8)。 |
| §2.1–2.3 bA/bB、Wilson/'t Hooft、$M$ | 6–8 | $F-\varphi\wedge\varphi=\star d_A\varphi$ 与三维 Bogomolny 方程；Wilson 是 holonomy，'t Hooft 是奇点。 |
| §2.4–2.5 Bogomolny with singularity | 8–10 | $S^2\times I$ 上插 't Hooft 奇点，$E_y$ 沿 $y$ 不变、越过奇点作 Hecke 修改，态空间 $H^*(N(\rho))$。 |
| §2.6–2.8 Nahm、对偶 BC、bB 态 | 10–14 | (2.3) 截断为 Nahm 方程 (2.6)；$\vec X=\vec t/y$ 定义 regular pole；$bB$ 态空间 $R^\vee$。 |
| §2.9–2.10 万有特征类、群论插曲 | 15–18 | 下降程序给出 $x_i(S)$；$\gamma^\vee=\frac1{n_g}\gamma^{-1}$。 |
| §2.11–2.12 $bB$ 中的像、融合 | 18–21 | (2.18) 给出 $x_i$ 的像；多标记点时 $\mathcal H=\otimes_\alpha\mathcal H_\alpha$。 |
| §3.1–3.2 twisting、标量场 | 23–28 | $N=4$ 的 $Spin(6)$ 破到 $Spin(2)$；$\mathbb{CP}^1$ 族 TFT，$\Phi$ 分裂出 $\varphi$ 与 $X_1,X_2$。 |
| §3.3 3d 一般构造、quadric、新理论 | 28–32 | $M_3\times S^1$、$Q^2=V$、$P(J)$ 的 quadric 与补集；新理论只 $Z_2$-分级。 |
| §3.4–3.5 Kronheimer 唯一性、Dirichlet 对偶 | 33–35 | 半直线 Nahm 解唯一；Dirichlet 的对偶耦合一族 3d SCFT $T(G^\vee)$。 |

## 二、主定理清单

1. **[T1] 卷积分裂**（p.6, (1.8)）：$H^*(N(\rho_\alpha))\otimes H^*(N(\rho_\beta))=\oplus_\gamma N^\gamma_{\alpha\beta}H^*(N(\rho_\gamma))$；规范理论侧是 Wilson 的张量积与 't Hooft 的分解。
2. **[T2] $E_y$ 的刚性**（p.9）：$bA$ 的 Bogomolny 方程在 $S^2\times I$ 上使全纯丛 $E_y$ 与 $y$ 无关；越过 't Hooft 奇点时跳变为 Hecke 修改。
3. **[T3] 态空间**（p.10）：$bA$ 的物理态空间是 $\mathcal H=H^*(N(\rho))$，$N(\rho)$ 是 Bogomolny 解的模空间。
4. **[T4] 截断到 Nahm 方程**（p.12）：(2.3) 在 $A=0$、$\varphi=X_3dy$、$\sigma^\vee=(X_1+iX_2)/\sqrt2$ 下化为 (2.6)。
5. **[T5] regular Nahm pole**（p.12–13）：$\vec X=\vec t/y$（$\vartheta$ 主嵌入）定义边界条件；非阿贝尔 S-对偶把 Neumann 送到『Dirichlet + pole』。
6. **[T6] $bB$ 态空间**（p.14）：Nahm 解唯一，模空间一点，故 $\mathcal H=R^\vee$；分级由主 $\mathrm{SL}_2$ 的 $t_3$ 给出。
7. **[T7] 下降与同伦不变**（p.16）：$x_i(S)=\int_SP_i^{(2)}$ 是 $Q$-闭算符，只依赖 $[S]$，等于 $H^{2d_i-2}(N(\rho))$ 中的杯积。
8. **[T8] 二次型对偶**（p.18）：$\gamma^\vee=\frac1{n_g}\gamma^{-1}$，$P_i(\sigma)=(\sqrt{n_g}\gamma^\vee)^{d_i}P_i^\vee(\sigma^\vee)$。
9. **[T9] $bB$ 中的像**（p.20）：$x_i=n_g^{d_i/2}(\gamma^\vee)^{d_i-1}\partial P_i^\vee/\partial\sigma^\vee$；$d_i=2$ 时是主 $\mathrm{SL}_2$ 的升算子。
10. **[T10] 第三种理论**（p.30–31）：$P(J)$ 的 quadric 上给出 $\mathbb{CP}^1$ 族 $Z$-分级 TFT；补集给出唯一 $Z_2$-分级理论，不区分 $G$ 与 $G^\vee$，$\tau$ 无关。
11. **[T11] Nahm 解唯一性**（p.33–34）：用 (3.16) 与 $T(G^\vee)$ 的 (3.17) 拼接，再由 Kronheimer 定理得半直线解唯一，即 $\vec X=\vec t/y$。

## 三、与已译文献的接口

| 篇 | 接口 |
|---|---|
| 01 KW06（hep-th/0604151） | 本篇的直接前身：[1] 的 $bA$/$bB$、Wilson/'t Hooft、Bogomolny 方程、§10.4 的 OPE 都被引用；T1、T2、T3 与 KW06 §9–10 逐条对应。 |
| 02 Gukov–Witten（hep-th/0612073） | 分歧（ramification）与 ramified Hecke 算子；本篇只取 $C=\mathbb{CP}^1$ 的无分歧情形，接口在 $N(\rho)$ 的 Schubert cell 描述。 |
| 06 Witten（0802.0999） | mirror 对称与 Hitchin 方程；本篇 §3 的 $\mathbb{CP}^1$ 族 TFT 与『$bA$ of $G$ = $bB$ of $G^\vee$』正是该篇图像的四维版本。 |
| 11 Witten（1009.6032） | 量子力学路径积分的新看法；与本文无公式接口，只在『用经典奇点定义量子边界条件』的方法论上相通。 |
| 16 Frenkel–Witten（0710.5939） | 内窥（endoscopy）与 mirror；$n_g$ 与 $G^\vee$ 的根长比在那边也出现，可对照 T8。 |
| 23 Gaiotto–Witten（1106.4789） | 4 维 $\mathcal N=4$ 的扭化与 3d-4d 耦合；$T(G^\vee)$ 与那边的规范理论边界条件是同一类对象。 |
| 28 Beilinson–Drinfeld | Hecke 特征层、oper、$N(\rho)$ 的数学背景；T1 的『Hecke 算子 = 't Hooft 算子』词典在此有严格版本。 |
| 36 Frenkel（hep-th/0512172） | Langlands/CFT 讲义；'t Hooft 算子与 Hecke 算子的对应、$R^\vee$ 的角色可作入门对照。 |

## 核对与勘误

### 外部来源

| # | 出处 | 定位 | 用途 |
|---|---|---|---|
| 1 | KW06（hep-th/0604151） | §9.1 p.127 eq(9.5)；§10.4 | Bogomolny 方程与 Hecke 修改解；Wilson/'t Hooft 的 OPE 对应 T1–T3 |
| 2 | datasets/kw06 卡 `bogomolny-equation`、`s-duality`、`thooft-operator` | 卡内 B 源 p.127 eq(9.5)、p.11 eq(2.16) | 核对 (2.2)、$\tau\to-1/(n_g\tau)$ 与 $n_g$ 的用法 |
| 3 | ggl12（0807.3720）p.46–47 eq(3.19) | §3.3 | regular Nahm pole $\vec\varphi=\vec t/y+\ldots$ 与主嵌入 |
| 4 | ggl21（0804.2902）p.34 eq(3.7)、p.42 eq(3.24) | §3 | Nahm 复形式 $DX/Dy=0$、Slodowy slice 与 Kronheimer 模空间 |
| 5 | nLab "Nahm's equation" | Properties 节 | $dX^3/dy+[X^1,X^2]=0$ 与 $\vec X=\vec t/y$ 解 |
| 6 | arXiv:0905.4795v1 | p.32 eq(3.14) | 与 v2 的符号差异（v1 作 $+$，v2 作 $-$） |

### 逐项核对

- **(2.2)/(2.6)**：KW06 §9.1 p.127 eq(9.5) 与 nLab 给出同一 Bogomolny/Nahm 方程；$\vec X=\vec t/y$ 的奇异解在两处都有，与本篇 (2.7) 一致。
- **$n_g$**：KW06 p.11 eq(2.16) 的 $\tau\to-1/(n_g\tau)$ 与 datasets/kw06 的 `s-duality` 卡给出同一个 $n_g$（长短根长度平方之比）；本篇 (2.13) 的 $\gamma^\vee=\frac1{n_g}\gamma^{-1}$ 与它相容。
- **Nahm pole**：ggl12（0807.3720）p.46–47 的 (3.19) 写 $\vec\varphi=\vec t/y+\ldots$，并称 $\vec t$ 为 $\mathfrak{su}(2)$ 三元组、$\vartheta$ 主嵌入；与本篇 §2.7 的 regular pole 定义相同。
- **Slodowy slice**：ggl21（0804.2902）p.42 eq(3.24) 与 p.34 eq(3.7) 的复形式、横截切片，与本篇 (3.16) 后的『一般 $\vartheta$ 时模空间是 Slodowy slice』一致。
- **T10 的 $Q^2=V$**：KW06 §3–4 的扭化给出同一超对称代数；本篇 §3.3 的 $Z_2$-分级新理论是 v2 的独立贡献，外部无第二处可核，故只作单源记录，不据此改动任何公式。
- **v1 vs v2**：v1 p.32 eq(3.14) 作 $\{Q',\tilde\nu\}=\nu+\{Q,[Q',\Theta]\}$，v2 改为 $\nu-\{Q,[Q',\Theta]\}$；v1 同页上一行已写 $-\{Q,[Q',\Theta]\}+\{V,\Theta\}$，故 v1 自身矛盾，v2 的修正与 Jacobi 恒等式一致。这是版本差异，不是本篇笔误，故只记于此，不入 errata。

### 勘误

- **E1（low，open）**：p.19 eq (2.15) 印刷为 $P_i^{(2)}=\langle\partial P_i/\partial\sigma^\vee,\star F\rangle+\langle\partial^2P_i/\partial\sigma^{\vee2},\psi\wedge\psi\rangle$，左端与 $\partial P_i$ 都漏了 $\vee$。按紧邻正文『$\mathcal P_i^{\vee(r)}$』与 (2.16) 的 $P_i^{\vee(2)}$，应读作 $P_i^{\vee(2)}$ 与 $\partial P_i^\vee/\partial\sigma^\vee$。PDF 渲染（external/pages/p-19.png）确认是印刷如此，不是提取错误；arXiv v1（v1.txt:1040）同样缺 $\vee$，说明是原稿就有的记号滑落。只有一处独立线索（本篇自身的 (2.16) 与正文），故置信度 low，保留原文照录，卡片 `bb-dual-of-xi` 与 `dual-formula-218` 的 provenance_note 标『存疑（见 errata E1）』。

## 不懂

1. **(2.9) 的系数与符号**：我从 (2.8) 的 2-形式部分解 $P_i^{(2)}$，只能定到 $\langle\partial P_i/\partial\sigma,F\rangle+\langle\partial^2P_i/\partial\sigma^2,\psi\wedge\psi\rangle$ 的形状，$\psi\wedge\psi$ 项的 $1/2$ 与符号依赖 $\psi$ 的归一，原文未给中间步骤，我未能唯一复现（D2 的 gap）。
2. **(2.17) 的积分**：$w$ 处外电荷的电场 $\propto(\gamma^\vee)^{-1}$ 且正比于表示矩阵，这是物理论证；$(\gamma^\vee)^{-1}$ 的精确系数依赖 $S$ 的定向与 $e^\vee$ 的归一，我只懂图像，没做严格计算。
3. **Kronheimer 定理的假设**：原文脚注 9 说 Kronheimer 还允许无穷远共轭到指定三元组，而正文只用『解唯一』；这两者的精确对应（尤其一般 $\vartheta$ 的 Slodowy slice 情形）我没完全对上。
4. **$T(G^\vee)$ 的存在性**：§3.4 把 Dirichlet 的对偶说成耦合一族 3d SCFT $T(G^\vee)$，其 Higgs 分支是 $X(G^\vee)$；这是引用 [6,7]，我没有独立验证这族 SCFT 的构造。
5. **$n_g$ 的根论来源**：若 $G$ 非单连通，$n_g$ 与 Langlands 对偶的 Borel 子群、根格的指标之间的关系，我没有算清；本篇只处理单连通单群，我按此理解。
