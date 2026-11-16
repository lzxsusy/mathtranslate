# U08 / R8 复算：Kapustin–Witten 2006 §11–§12（印刷 pp.184–222）

> 复算员 P5（R8）。本文件与 `calc/recalc_r8.py` 配套：文中每条「核验」都有脚本里的编号（A/B/C/D/E/F），
> 运行 `python calc/recalc_r8.py` 即打印 PASS/FAIL 表。脚本只用标准库，约 0.35 s。
>
> **页与文件**：原文 `source/text/p185.txt`–`p223.txt`；印刷页 N = PDF 第 N+1 页 = 文件 `p{N+1}.txt`（F01 用页脚核验）。
> 页图 `source/pages/KW06.pdf`，渲染 `pdftoppm -f <印刷页+1> -r 200 -png -singlefile`；本复算实际逐字核过的页：
> 印刷 43、184、185、186、195、196、197、199、200、203、204、206、215、217、219、220。
>
> **bar 问题（全部 bar 错的根源）**：文本层没有任何 combining macron（U+0304，全 0 命中，F02），
> 因此所有下标上划线（z̄、Ā、φ̄、ψ̄、λ̄）在 `.txt` 里全部丢失；凡涉及 bar 的公式必须以页图为准。
> 报告与解经本里的 bar 错全部可溯源到「照抄文本层」（F03/F04/F05 给原文文本层的对照串）。
>
> **本文件的判定口径**：A–E 组 PASS = 数学/物理核验通过；F 组 PASS = 「该处出入确实存在」（F 组是证据，不是错误计数）。

---

## 一、c.c. 膜（§11.1；印刷 pp.184–195）

### 1.1 问题

原文如何定义 canonical coisotropic（c.c.）膜？三个具体问题——「支撑是否空间充满」「Ψ 取什么值」「为什么是 A-膜而不是 B-膜」——原文分别给了什么依据？报告 §2.1 的复述是否逐项一致？

### 1.2 原文式与页

| 内容 | 原文式 | 页（印刷 / 文件） |
|---|---|---|
| coisotropic 子流形 $Y$：由 Poisson 交换的 $f_i$ 局部零点定义；$\dim Y\ge \tfrac12\dim X$ | — | p.185 / p186.txt |
| 本文只用 $Y=X$、rank one CP 线丛 $\mathcal L$、$F=dA$ | — | p.185 / p186.txt |
| A-膜条件（$Y=X$、rank one）：$(\omega^{-1}F)^2=-1$ | **(11.1)** | p.185 / p186.txt |
| $\hat N=\omega^{-1}F$ 可积；$\omega,F$ 对 $\hat N$ 为 $(2,0)\oplus(0,2)$ 型；$\omega-iF$ 是 $(2,0)$ 全纯辛形式 | — | p.185 / p186.txt |
| c.c. 解的显式形式 | **(11.2)** $F=(\mathrm{Im}\,\tau)\omega_J,\ \hat N=\omega_K^{-1}\omega_J=I$（另一解 $F,\hat N$ 同时反号） | p.186 / p187.txt |
| 一形式势 | **(11.3)** $\alpha=\dfrac{\mathrm{Im}\,\tau}{2\pi}\int_C|d^2z|\,\mathrm{Tr}\big(\varphi_z\,\delta A_{\bar z}+\varphi_{\bar z}\,\delta A_z\big)$，$F=d\alpha$ | p.186 / p187.txt |
| 更一般的解（不可用） | **(11.4)** $(\mathrm{Im}\,\tau)(a\omega_J+b\omega_I),\ a^2+b^2=1$；$b\ne0$ 时非恰当、周期非 $2\pi\mathbb Z$ | p.186 / p187.txt |
| 唯一性：$G$ 单连通时 c.c. 膜唯一，否则差平坦线丛扭转 | — | p.186 / p187.txt |
| c.c. 膜是 $(A,B,A)$：$I$ 下 A 用 $(11.5)$；$J$ 下 B 因 $F\propto\omega_J$ 是 $(1,1)$ 型；$K$ 下 A | **(11.5)** $(\omega_I^{-1}\omega_J)^2=-1$ | p.186 / p187.txt |
| 只在 $\mathcal M_H$ 光滑部分有意义；整体定义靠底层规范理论边界条件（§12.4） | — | p.186 / p187.txt |
| 交换哈密顿量只能量子化为 $K_M^{1/2}$ 上的微分算子（脚注 53：level $k=-h$） | — | p.195 / p196.txt |

（(11.3) 的 bar 结构由页图确认；文本层 p187.txt:16 记作 `Tr (φz δAz + φz δAz )`，两处 bar 全丢，见 F03。）

### 1.3 逐步推导（A 组核验）

用 $H\simeq\mathbb R^4$ 上的左乘四元数模型：$I=L_i,\ J=L_j,\ K=L_k$，$I^2=J^2=K^2=-1$、两两反对易、$IJ=K$ 等（**A01**）；$\omega_X=g(X\cdot,\cdot)$ 取标准内积。

1. **N̂ 的计算**：$\omega_K^{-1}\omega_J=K^{-1}J=I$（**A02**）；$F=(\mathrm{Im}\,\tau)\omega_J$、$\omega=(\mathrm{Im}\,\tau)\omega_K$ 时 $\omega^{-1}F=\omega_K^{-1}\omega_J=I$，故 $(\omega^{-1}F)^2=I^2=-1$，即 (11.1) 成立（**A03/A04**）；$F,\hat N$ 同时反号的第二解同样满足 (11.1)（**A05**）。
2. **c.c. 膜在 $I$ 下是 A-型**：$(\omega_I^{-1}\omega_J)^2=(-K)^2=-1$（**A06**），即 $\omega_I^{-1}\omega_J$ 本身是复结构，故 (11.1) 对 $I$ 也成立。
3. **(11.4) 族**：$\hat N_K=aI-bJ$，$\hat N_K^2=-(a^2+b^2)\mathbf 1=-\mathbf 1$——**任意** $(a,b)$（$a^2+b^2=1$）在 $K$ 下都是 A-膜（**A07**）。同时 $\hat N_I=b\mathbf 1-aK$、$\hat N_J=a\mathbf 1+bK$：$\hat N_I^2=(b^2-a^2)-2abK$ 要是复结构须 $b=0$，$\hat N_J^2=(a^2-b^2)+2abK$ 要是复结构须 $a=0$，故 $(A,A,A)$ 不可能（**A08**）。⇒ 在 (11.4) 族里 $b\ne0$ 的排除**只靠恰当性/周期量子化**（p.186），与 A-型条件无关；$b=0$ 时 $\hat N_J=\pm\mathbf1$ 平方 $+1$，$J$ 中必为 B-膜。
4. **为什么是 A-膜而不是 B-膜**：B-膜条件是 CP 曲率在相应复结构下为 $(1,1)$ 型。在 $K$ 下 $F=(\mathrm{Im}\,\tau)\omega_J$ 是 $(2,0)\oplus(0,2)$ 型（**A09**），故它不是 $K$ 中的 B-膜；但它满足 (11.1)，故是 $K$ 中的 A-膜。在 $J$ 下 $\omega_J$ 是 $(1,1)$ 型（**A09**），所以它确实是 $J$ 中的 B-膜（E-清单 E12 指出报告此处理由不足，但结论正确）。
5. **空间充满**：$Y=X$、rank one，支撑没有额外约束（原文明确「we will need only the case that $Y=X$ and the A-brane has rank one」），因此 c.c. 膜是空间充满膜，与 Lagrange 膜不同。
6. **Ψ 取何值**：§11.1 的 (11.2) 对应 §11.3 族 $B^{\Psi}_{c.c.}$ 在 $\Psi=0$ 的成员：$\Psi=\mathrm{Re}\,\tau=0$ 时 $B=-\omega_I\mathrm{Re}\,\tau=0$、$F=\mathrm{Im}\,\tau\cos q\,\omega_J$ 且 $q=0$，回到 $F=(\mathrm{Im}\,\tau)\omega_J$（**A12**；与 **C03/C05** 的 $q=0$ 端点一致）。
7. **无瞬子**：$\omega-iF\propto\Omega_I$ 是 $I$ 的 $(2,0)$ 型、且 $\omega$ 非退化（**A11**），故 $(\omega-iF)\partial_0\Phi=0$ 逼 $\partial_0\Phi=0$，边界上常值 ⇒ 处处常值（p.187）。
8. **(11.3) 的可行性**：局部平坦模型里 $\omega_J=dx^1\wedge dx^3-dx^2\wedge dx^4=d(x^1dx^3-x^2dx^4)$ 恰当（**A10**），故 $F=d\alpha$ 可行；在 $\mathcal M_H$ 上 $\omega_J$ 的恰当性/周期整性才是 (11.4) 族被排除的原因（原文 p.186，本模型无法体现整体性质，只能核验局部）。

### 1.4 结论

- c.c. 膜 = $Y=X$（空间充满）、rank one、$F=(\mathrm{Im}\,\tau)\omega_J$、$\hat N=I$；是 $(A,B,A)$ 型；在 $G$ 单连通时唯一（否则差平坦线丛扭转）。特别地：**它是 $K$ 中的 A-膜而非 B-膜，因为 $F$ 在 $K$ 下是 $(2,0)\oplus(0,2)$ 型**；$\Psi=0$。
- 报告的 (11.1)–(11.5)、唯一性、$(A,B,A)$ 三重复述与原文逐项一致；唯一实质问题是 (11.3) 的 bar（E1）与 $K$ 侧理由不足（E12）。

### 1.5 与报告的差异

| 报告位置 | 差异 | 级别 |
|---|---|---|
| 行 53 | (11.3) 写成 $\varphi_z\delta A_z+\varphi_{\bar z}\delta A_{\bar z}$；页图正确为 $\varphi_z\delta A_{\bar z}+\varphi_{\bar z}\delta A_z$ | 中（E1） |
| 行 61 | 「在 $K$ 下当然是 A-型：$\omega$ 本身取成 $(\mathrm{Im}\,\tau)\omega_K$」理由不足；正确依据是 $F$ 在 $K$ 下非 $(1,1)$ 型 | 低（E12） |

---

## 二、A-膜 ⇒ D-模（§11.2；印刷 pp.196–200）

### 2.1 问题

把原文「每个 $K$ 型 A-膜都是 $K_M^{1/2}$ 上微分算子层的模」的机制拆成 4–6 步并给 locator；检查报告是否漏掉「为什么 c.c. 膜给 D-模（而一般 A-膜不给）」「为什么 c.c. 膜唯一」这两个问题。

### 2.2 原文式与页

- 主命题（p.196 / p197.txt）：*every A-brane in complex structure $K$ is a module for the sheaf of differential operators on $K_M^{1/2}$.*
- 层化限制（p.196）：只能在 $\mathcal M_H$ 中形如 $T^*V$（$V\subset\mathcal M$）的开集上把代数/模层化；故每个 $K$ 型 A-膜给 $\mathcal D_{K_M^{1/2}}$ 的模层。
- 无瞬子修正（p.196）：c.c. 膜与任意 $K$ 型 A-膜的 $(B_{c.c.},B')$ 弦无瞬子修正（盘瞬子在 c.c. 边界上必须常值，解析性 ⇒ 全常值）。
- 自同态代数（p.187–195）：$(B_{c.c.},B_{c.c.})$ 弦 = 对 $\hat N=I$ 的全纯函数的非交换形变；(11.12)–(11.16) 粘合、正则量子化；$c^{(ijk)}\in H^2(\mathcal M,\mathbb C)$，$c\in2\pi\mathbb Z$ 时得 $D_L$，否则 $D_{L^\gamma}$；$H^2(\mathcal M(G,C),\mathbb C)$ 一维 ⇒ 最一般是 $D_{L^\gamma}$；时间反演 + opposite 代数 $\mathrm{opp}(D_L)=D_{L^{-1}\otimes K_X}$ ⇒ $L^2=K$ ⇒ $L=K^{1/2}$（p.193–194）。
- 模的具体表示（p.197–198）：$(B_{c.c.},B')$ 态 = $\mathcal N^{-1}$ ⊗（费米零模丛）的截面；限制到 $\varphi=0$ 时 $\mathcal N$ 的连接为零故删去；费米零模空间 $=T_p\mathcal M$（法向费米子无零模）；量子化得 $\mathcal M$ 上旋量，$ \mathcal M$ 复 ⇒ 旋量丛 $=K_{\mathcal M}^{1/2}\otimes\bigoplus_{i=0}^{\dim\mathcal M}\Omega^{0,i}$；BRST 算子 $Q=\bar\partial$；物理弦层 $=K^{1/2}$ 的全纯截面层，即 $\mathcal D_{K^{1/2}}$ 的模。作者原话：*This construction gives, possibly, a more direct explanation of why the sheaf of rings derived from the c.c. brane is precisely $\mathcal D_{K_M^{1/2}}$, rather than $\mathcal D_{\mathcal L}$ for some other $\mathcal L$.*（脚注 54：$j>0$ 的 $\Omega^j$ 对小开集上同调无贡献，可略。）
- charge conjugation 论证（p.198）：$\mathcal M=\mathbb R\times I\times C$，$\mathbb R$ 为时间方向；只有 $C$ 上 twist、时间方向无 twist ⇒ 有伴随 $Q^\dagger$，$\{Q,Q^\dagger\}=H$；charge conjugation 交换 $Q,Q^\dagger$ ⇒ CP 丛必是 $\mathcal M$ 的自旋丛（排除 $K^{1/2}\otimes$ 其它线丛）。

### 2.3 逐步推导：六步机制（逐条 locator 与核验，对应报告 §3.1 的六步）

| # | 步骤 | 原文 locator | 核验 |
|---|---|---|---|
| 1 | 开弦端点：任意两膜 $\mathcal B,\mathcal B'$ 的 $(\mathcal B,\mathcal B')$-弦是 $(\mathcal B,\mathcal B)$-弦代数的模（开闭 TQFT 公理，图 6） | p.196 | 机制性陈述，无独立数值核验 |
| 2 | 层化：$(\mathcal B,\mathcal B')$ 弦构成模**层**；可层化开集限于 $T^*V$ 型 ⇒ $K$ 型 A-膜 ⇒ $\mathcal D_{K_M^{1/2}}$ 模层 | p.196 | 同上 |
| 3 | 无瞬子修正：$(B_{c.c.},B')$ 弦的盘瞬子在 c.c. 边界常值 ⇒ 微扰论精确 | p.196 | 与 §11.1 第 7 条（**A11**）同一机制 |
| 4 | 自同态代数：全纯函数 → Poisson 形变 → 正则量子化 (11.12)–(11.16) → $D_{L^\gamma}$；时间反演 ⇒ $K^{1/2}$ | p.187–195 | **B04** 核 (11.12)(11.15) 的对易子；**B05** 核 (11.16) 粘合相容；**B01/B02/B03** 核旋量丛与自旋条件 |
| 5 | 模的具体形式：费米零模 = $T_p\mathcal M$ → 旋量丛 $K^{1/2}\otimes\oplus\Omega^{0,j}$ → $Q=\bar\partial$ → 全纯截面层 | p.197–198 | **B01**（$2^n$ 维 = 秩）、**B06**（$\bar\partial^2=0$）、**B07**（例 1，$n=2$） |
| 6 | charge conjugation：$Q^\dagger$ 存在 ⇒ CP 丛 = 自旋丛（不给 $K^{1/2}\otimes L$ 留余地） | p.198 | 与 **B02/B03** 的线丛论证互补 |
| 7 | 例：$G=U(1)$ 手算 (11.17)–(11.25)：$\mathcal M_H=T^*\mathrm{Jac}$、纤维=$\mathrm{Jac}$、态=$L\otimes\mathcal N^{-1}$ 的全纯截面、量子化算符给 $\mathrm{Jac}$ 上平坦连接、$\upsilon=0$ 时才酉 | p.199–200 | 见第 5 节 E 清单 (11.17)–(11.25) 的 bar 问题；结论 $H_1(C,\mathbb Z)\cong H_1(\mathrm{Jac},\mathbb Z)$ 是 Poincaré 对偶 |

### 2.4 结论：报告有没有漏掉那两个「为什么」

- **「为什么 c.c. 膜给 D-模，而一般 A-膜不给」——这个提法本身需要修正**：原文的主命题是**所有** $K$ 型 A-膜都给 $\mathcal D_{K^{1/2}}$ 的模层，没有「一般 A-膜不给」这回事。真正的区别是**代数层 vs 模层**：一般 A-膜只给模层，c.c. 膜是范畴里的万有对象，它的**自同态代数**才是 $\mathcal D$；这正是报告行 428「正则表示/Yoneda」那一步。报告覆盖了这一点（§2.2 行 135/137/139 与 §3.1 行 428），**没有漏**。
- **「为什么 c.c. 膜唯一」**：报告行 55 已给「$G$ 单连通时唯一，否则差平坦线丛扭转」，**没有漏**；但行 428 的「存在且唯一」把条件省略了（E15）。
- 报告唯一没有明说的是：第 5 步里「为什么偏偏是 $K^{1/2}$ 而不是某个 $D_L$」有两个独立论证（时间反演 + charge conjugation），报告行 123/139 分开提到，但 §3.1 汇总处没有 cross-reference。属组织性小瑕（E17 的一部分）。

### 2.5 与报告的差异

| 报告位置 | 差异 | 级别 |
|---|---|---|
| 行 87 | (11.10) 写成 $\mathrm{Tr}(\varphi_z\delta A_z)$，应 $\delta A_{\bar z}$ | 中（E2） |
| 行 149/153/157/159/163/165 | (11.17)–(11.25) 的 bar 系统性丢失，且 (11.19) 项序也反（页图为 $\varphi_{\bar z}\delta A_z-\varphi_z\delta A_{\bar z}$） | 中（E3–E7） |
| 行 428 | 「存在且唯一」漏 $G$ 单连通；「Yoneda」措辞可再保守（报告同段已注「尚未严格」，建议统一） | 低（E15/E17） |

---

## 三、ξ 与扭化微分算子（§11.3；印刷 pp.201–206）

### 3.1 问题与一个术语声明

任务书要求「§11.3 的 ξ 与扭化微分算子」。**但原文与我们的解经本中都没有 ξ**（原文全篇用 $\Psi=\theta/2\pi=\mathrm{Re}\,\tau$；解经本 33_flesh_dmod.tex 亦无 `\xi`，F25）。因此本节的 ξ 只能是一个**定义出来的**量：

$$\boxed{\;\xi:=\Psi-h\;}$$

其中 $h$ 是对偶 Coxeter 数。这个定义不是任意选的：原文 p.206 的结论正是「任意 $\Psi$ 下 c.c. 弦代数 = $L^{\Psi-h}$ 上全纯微分算子层；$\Psi=h$ 时为普通微分算子层」，所以「扭化指数」本来就等于 $\Psi-h$。（此项记 N1。）

### 3.2 原文式与页

| 内容 | 原文式 | 页（印刷 / 文件） |
|---|---|---|
| 取实 $\Psi$ | **(11.26)** $\Psi=\theta/2\pi=\mathrm{Re}\,\tau$ | p.201 / p202.txt |
| B-场 | **(11.27)** $B=-\omega_I\,\mathrm{Re}\,\tau$；$B$ 沿 Hitchin 纤维非平坦 ⇒ 纤维一般不再是 A-膜 | p.201 / p202.txt |
| gauge 变换与可解性 | **(11.28)** $B\to B-d\lambda,\ A\to A+\lambda|_Y$；**(11.29)** $F+B|_Y=0$；$[B|_Y/2\pi]$ 非整则无 rank-one A-膜 | p.201–202 |
| $\Psi$ 扭化后的 c.c. 代数 | $B^{\Psi}_{c.c.}$ 代数 $=\mathcal D_{K_M^{1/2}\otimes L^{\Psi}}$（$L$=行列式线丛 (4.10)） | p.202 / p203.txt |
| 膜方程 | **(11.30)** $(\omega^{-1}(F+B))^2=-1$，$\omega=(\mathrm{Im}\,\tau)\omega_K$ | p.203 / p204.txt |
| 显式解 | **(11.31)** $F=\mathrm{Im}\,\tau\cos q\,\omega_J,\ \sin q=-\mathrm{Re}\,\tau/\mathrm{Im}\,\tau$ | p.203 / p204.txt |
| 复结构 | **(11.32)** $I(\Psi)=\omega^{-1}(F+B)=I\cos q-J\sin q$（脚注 57：$I(\Psi)=I_w$，$w=i\tan(q/2)$） | p.203 / p204.txt |
| 全纯坐标 | **(11.33)** $A'_{\bar z}=A_{\bar z}-i\tan\tfrac q2\,\varphi_{\bar z},\quad \varphi'_z=\varphi_z+i\tan\tfrac q2\,A_z$ | p.203 / p204.txt |
| Hitchin 第二纤维化 | **(11.34)** $\pi_0:(A_{\bar z},\varphi_z)\to A_{\bar z}$（仅 $\Psi=0$ 全纯） | p.203 / p204.txt |
| 新 $\bar\partial$-联络 | **(11.35)** $D'_{\bar z}=D_{\bar z}-i\tan\tfrac q2\,\varphi_{\bar z}=\partial_{\bar z}+A_{\bar z}-i\tan\tfrac q2\,\varphi_{\bar z}$ | p.203 / p204.txt |
| 齐次对象（纤维坐标） | **(11.36)** $D'_z=\varphi_z+i\tan\tfrac q2\,D_z$ | p.204 / p205.txt |
| $\lambda$-连接 | **(11.37)** $\nabla(fs)=f\nabla s+\lambda\,\partial f\wedge s$，$\lambda=i\tan(q/2)$；$\lambda=1$ 普通 $\partial$，$\lambda=0$ 为 $\mathrm{End}(E)\otimes T^*X$ 截面 | p.204 / p205.txt |
| 整数 $\Psi=n$ | $B_n$ 支撑 $\varphi=0$、CP $=L^n$ 满足 (11.29)；态 $=K^{1/2}\otimes L^n\otimes\bigoplus_{j=0}^{n}\Omega^{0,j}$ ⇒ 代数 $\mathcal D_{K^{1/2}\otimes L^n}$ | p.204–205 |
| 作用量与线性性 | **(11.38)** $S=\int\Phi^*(\omega-iF-iB)=-i\,\mathrm{Im}\,\tau\int\Phi^*(\cos q\,\omega_J+\sin q\,\omega_I+i\omega_K)$；**(11.39)** $\Omega'=\frac{\mathrm{Im}\tau}{\pi}\delta\int_C\mathrm{Tr}(\varphi_z\delta A'_{\bar z})-i\,\mathrm{Re}\,\tau\int_C\mathrm{Tr}(\delta A'_z\delta A'_{\bar z})$ | p.205–206 / p206–p207.txt |
| 退化点 | $K_{\mathcal M}\cong L^{-2h}$ ⇒ 代数 $=\mathcal D_{L^{\Psi-h}}$；$\Psi=h$ 时为普通微分算子层；S-对偶 + $T^h$ 把 $\mathcal M_H({}^LG)$ 零膜映到 $M$ 上普通 D-模 | p.206 / p207.txt |

（(11.33)–(11.35) 的 bar 由页图 `kw_p203.png` 放大逐字核验；解经本行 386 的第一式缺 bar，见 N9。）

### 3.3 逐步推导：ξ 的定义与两例

由 $K_{\mathcal M}\cong L^{-2h}$ 得 $K_{\mathcal M}^{1/2}=L^{-h}$，故

$$K_{\mathcal M}^{1/2}\otimes L^{\Psi}=L^{\Psi-h}=L^{\xi}.$$

| ξ | Ψ | 线丛 | 代数 | 说明 |
|---|---|---|---|---|
| $\xi=-h$ | $\Psi=0$ | $L^{-h}=K^{1/2}$ | $\mathcal D_{K^{1/2}}$ | §11.1–§11.2 的 c.c. 膜 |
| $\xi=0$ | $\Psi=h$ | $L^0=\mathcal O$ | $\mathcal D$（普通微分算子层） | 原文 p.206 的退化点 |
| $\xi=1$ | $\Psi=h+1$ | $L$ | $\mathcal D_L$ | 第一个「非平凡但 honest」的扭化 |
| $\xi=n-h$ | $\Psi=n$ | $L^{n-h}$ | $\mathcal D_{K^{1/2}\otimes L^n}$ | 与 p.204–205 的整数 $\Psi$ 结果一致 |

**例 1（ξ=0，即 Ψ=h）**：取 $G=SU(3)$，$h=3$，则 $\Psi=3$，$K_M^{1/2}\otimes L^3=L^{-3}\otimes L^3=\mathcal O$，代数退化为普通 $\mathcal D$（**C01/C08**）。这正是原文「$\Psi=h$ 时为普通微分算子层」以及报告行 245/415–420 的结论。
**例 2（ξ=1，即 Ψ=h+1）**：同 $G=SU(3)$，$\Psi=4$，$K_M^{1/2}\otimes L^4=L$，代数 $=\mathcal D_L$——与 c.c. 膜 $\Psi=0$ 的 $\mathcal D_{K^{1/2}}$ 是不同线丛上的 D-模（**C01/C02**）。整数 $\Psi=n$ 的一般公式（p.204–205）在此 $n=h+1$ 时给出 $K^{1/2}\otimes L^n$，两边一致。

### 3.4 逐步推导的数值/符号核验（C 组）

1. **指数算术（C01）**：对 5 个群（$SU(2),h=2$；$SU(3),h=3$；$G_2,h=4$；$SO(8),h=6$；$E_8,h=30$）× 6 个 $\Psi$（$0,h,h+1,2h,-1,h-2$）核 $-h+\Psi=\Psi-h$，全部成立。
2. **两个例子（C02/C08）**：$\xi=0,1,-h$ 的对应关系与 $K^{1/2}\otimes L^h=\mathcal O$、$K^{1/2}\otimes L^{h+1}=L$ 逐项核验。
3. **$I(\Psi)$ 是复结构（C03/C04）**：四元数矩阵直接验证 $(I\cos q-J\sin q)^2=-\mathbf 1$（4 组 $\tau$），端点 $q=0\Rightarrow I$、$q=\pi/2\Rightarrow -J$。
4. **(11.31) 满足 (11.30)（C05）**：由 $F,B$ 的矩阵直接算 $\big(\omega^{-1}(F+B)\big)^2=-\mathbf 1$（4 组 $\tau$；注意 $\omega=(\mathrm{Im}\,\tau)\omega_K$ 的归一化）。
5. **$\lambda=i\tan(q/2)$（C06/C07）**：$\lambda=0\Leftrightarrow q=0\Leftrightarrow\Psi=0$；小 $\Psi$ 时 $\lambda\approx-i\Psi/(2\mathrm{Im}\,\tau)$，即**线性于 $\Psi$**——与原文 f(Ψ)=Ψ 的微扰论证（(11.38)(11.39) 算到 $1/(\mathrm{Im}\,\tau)^2$ 阶）一致。$\lambda=0$ 时 (11.36) 退化为 $D'_z=\varphi_z$（$\mathrm{End}(E)\otimes T^*X$ 的截面）；$q$ 实 ⇒ $\lambda$ 纯虚，所以原文「$\lambda=1$ 为普通 $\partial$」只是 $\lambda$-连接定义里的基准语义，不是物理取值。

### 3.5 结论

- **ξ 不是原文的量**；唯一自然定义是 $\xi=\Psi-h$（扭化指数）。$\xi=0$（$\Psi=h$）退化为普通 D-模；$\xi=1$（$\Psi=h+1$）给 $\mathcal D_L$；$\xi=-h$（$\Psi=0$）给 $\mathcal D_{K^{1/2}}$（与 §11.2 的结果吻合，验证了定义的自洽性）。
- 两个例子（$\xi=0,\xi=1$）在指数算术、$I(\Psi)$ 复结构、$\lambda$ 线性展开三处都过。
- 一个原文自带的 caveat 值得记录：$q$ 实要求 $|\mathrm{Re}\,\tau|\le\mathrm{Im}\,\tau$，原文 p.203 明说「因 $\mathrm{Im}\,\tau$ 可任意大，$q$ 极小，最终效应线性于 $\Psi$」——即上面的几何解释是弱耦合/小 $q$ 展开，$f(\Psi)=\Psi$ 的论证本身是微扰的。

### 3.6 与报告的差异

| 报告位置 | 差异 | 级别 |
|---|---|---|
| 行 209/213/217 | (11.33)(11.34)(11.35) 的 $\bar z$ 全丢（页图三式全带 $\bar z$） | 中（E8） |
| 行 241 | (11.39) 第一项写成 $\delta A'_z$，页图是 $\delta A'_{\bar z}$ | 中（E9） |
| 行 231 | 脚注 58 的「两种代数结构」处理与原文一致 | — |

---

## 四、三类膜的守恒超荷（§12.1–§12.4；印刷 pp.207–220）

### 4.1 问题

列表 (B,B,B)/(B,A,A)/(A,B,A) 各保哪两个超荷（原文的 $T$、$T'$ 组合），核报告 §3.2 的表；用 $\Gamma$ 矩阵代数验证至少两组。

### 4.2 原文式与页

- 框架（p.207–208）：$\mathcal M=\mathbb R^2_+\times C$；twisting 条件 **(12.1)** $\Gamma^{2367}\epsilon=\epsilon$（同 (5.3)）；边界条件保持**两个拓扑超荷** ⇒ 共 4 个超对称 = 四维 16 个的 $1/4$ BPS，二维看 $1/2$ BPS；$Q$ 被保持则 $Q^\dagger$ 也被保持，$\{Q,Q^\dagger\}=H$。
- 第一构造（p.211）：**(12.9)** $T=\Gamma^{04}$，$T\lambda|=\lambda|$；**(12.10)** $(T-1)\delta\lambda=\tfrac12[T,\Gamma^{IJ}F_{IJ}]\epsilon$；**(12.11)** $\sum_{I\ne0,4}(\Gamma^{0I}F_{4I}-\Gamma^{4I}F_{0I})\epsilon=0$；**(12.12)** $\Gamma^0\Gamma^4\epsilon=\epsilon\Rightarrow F_{0I}+F_{4I}=0$；**(12.13)–(12.16)** 超流、$\delta A_I=i\epsilon\Gamma_I\lambda$、$\sum_{I,J\ne0,1,4}\Gamma^{IJ}F_{IJ}\epsilon=0$ ⇒ Hitchin 方程 $F_{23}-F_{67}=F_{27}-F_{36}=F_{26}-F_{73}=0$；$F_{IJ}|=0$ 除 $I,J\in R=\{2,3,6,7\}$。
- 第二构造（p.214）：**$\tilde T=T\Gamma^{2367}=\Gamma^{023467}$**，$\tilde T\lambda|=-\lambda|$；**(12.17)(12.18)(12.19)**（$\Gamma^{1589}\epsilon=-\epsilon$ 等）。
- (B,A,A)（p.215）：**(12.20)** $\epsilon_\ell\to\epsilon_\ell e^{-i\pi/4},\ \epsilon_r\to\epsilon_r e^{+i\pi/4}$；**(12.21)** $\epsilon\to\epsilon'=\frac{1+\hat\Gamma}{\sqrt2}\epsilon$，$\hat\Gamma=\Gamma^0\Gamma^1\Gamma^2\Gamma^3$ 量四维手征；**(12.22)** $T'=\frac{1+\hat\Gamma}{\sqrt2}T\frac{1-\hat\Gamma}{\sqrt2}$；**(12.23)** $T=\Gamma^0\Gamma^4\Rightarrow T'=\Gamma^1\Gamma^2\Gamma^3\Gamma^4$；**(12.24)**（见第 5 节）。
- (A,B,A)（p.217–219）：**(12.28)** $T'=-\Gamma_{15}\Gamma_{2-7}\Gamma_{3+6}$（旋转不变）；$T'\lambda|=\pm\lambda|$ 两族；S-对偶后 **(12.30)** $\hat T=\frac{1+\hat\Gamma}{\sqrt2}T'\frac{1-\hat\Gamma}{\sqrt2}=-\frac{\Gamma_{15}}{2}\big((\Gamma_{26}+\Gamma_{37})-\hat\Gamma(\Gamma_{23}+\Gamma_{67})\big)$，要求 $\hat T\epsilon=\Gamma^{2367}\epsilon=\epsilon$。

### 4.3 逐步推导（一）：三类膜的「两个超荷」

| 类型 | 第二个不破缺条件（$T$ 型算子） | 与 (12.1) 合起来 | 页 | 核验 |
|---|---|---|---|---|
| (B,B,B) | $T=\Gamma^{04}$（(12.9)；另一实现 $\tilde T=\Gamma^{023467}$） | $T\epsilon=\epsilon$ 且 $\Gamma^{2367}\epsilon=\epsilon$ ⇒ 4 | p.211–214 | **D06/D08/D14** |
| (B,A,A) | $T'=\Gamma^{1234}$（(12.23)；第二实现 $T''=T'\Gamma^{2367}=-\Gamma^{1467}$） | $T'\epsilon=\epsilon$ 且 $\Gamma^{2367}\epsilon=\epsilon$ ⇒ 4 | p.215–217 | **D04/D05/D08/D14** |
| (A,B,A) | $T'=-\Gamma_{15}\Gamma_{2-7}\Gamma_{3+6}$（(12.28)，直接构造；S-对偶后 $\hat T$ (12.30)） | $T'\epsilon=\epsilon$（或 $\hat T\epsilon=\epsilon$）且 $\Gamma^{2367}\epsilon=\epsilon$ ⇒ 4 | p.217–220 | **D09/D10/D11/D14** |

注：原文的记号 $T'$ 在 §12.3 是 $\Gamma^{1234}$，在 §12.4 被**重新使用**为 $-\Gamma_{15}\Gamma_{2-7}\Gamma_{3+6}$；§12.4 还有 $T''=-\Gamma_{15}\Gamma_{2+7}\Gamma_{3-6}$。这是原文的记号拥挤（N2），解经本行 540 已显式声明改用 $\mathcal T$ 以避免混淆。

### 4.4 逐步推导（二）：$\Gamma$ 矩阵验证（D 组，32×32 Lorentz 号差）

构造：10 个 Euclid $\Gamma^E$（$\{\Gamma^E_a,\Gamma^E_b\}=2\delta_{ab}$），令 $\Gamma_0=i\Gamma^E_1$、$\Gamma_i=\Gamma^E_{(i+1)\bmod10}$（$i=1..9$），得 $\{\Gamma_I,\Gamma_J\}=2\eta_{IJ}$，$\eta=\mathrm{diag}(-1,1,\dots,1)$（**D01**）。

- **D02/D03**：十维手征 $\hat\Gamma=\Gamma^0\cdots\Gamma^9$ 满足 $\hat\Gamma^2=1$、未破缺半空间 16 维；四维 $\hat\Gamma=\Gamma^0\Gamma^1\Gamma^2\Gamma^3$ 满足 $\hat\Gamma^2=-1$，故 $P_\pm=(1\pm\hat\Gamma)/\sqrt2$ **互逆**而非投影（$P_+P_-=1$）。这一点是 (12.21)–(12.23) 自洽的前提（**E09**）：若误用 Euclid 号差（$\hat\Gamma^2=+1$），$P_-P_+=0$，(12.22) 给出 $T'=0$。
- **D04**：$T'=P_+T\,P_-=\Gamma^1\Gamma^2\Gamma^3\Gamma^4$ 精确成立（(12.23)）。
- **D05**：$[T',\Gamma^{2367}]=0$、$T'^2=1$、$T''=T'\Gamma^{2367}=-\Gamma^{1467}$、$T''^2=1$。$T'$ 与 $\Gamma^{2367}$ 对易是因为两个指标 $\{2,3\}$ 与 $\{1,2,3,4\}$ 交叠数为 2（**D13**）。
- **D06**：$\tilde T=T\Gamma^{2367}=\Gamma^{023467}$，$\tilde T^2=1$、$[\tilde T,\Gamma^{2367}]=0$。
- **D07**：$\{T,T'\}=0$（不同族的超流确实不同）。
- **D08**：$\dim\{\hat\Gamma_{10}=+1,\ \Gamma^{2367}=+1\}=8$；再加 $T$ 得 4（$T=\Gamma^{04}$、$\Gamma^{1234}$、$-\Gamma^{1467}$、$\Gamma^{023467}$ 四种都给 4）⇒ $4/16=1/4$ BPS、$4/8=1/2$ BPS（与原文 p.208 一致）。
- **D09/D10/D11**（(12.28) 与 (12.30)）：$T'=-\Gamma_{15}\Gamma_{2-7}\Gamma_{3+6}$ 满足 $T'^2=1$ 且与 $\Gamma^{23}+\Gamma^{67}$ 对易（旋转不变性）；$\hat T=P_+T'P_-$ 与 (12.30) 右端精确相等，$\hat T^2=1$、$[\hat T,\Gamma^{2367}]=0$。**记号陷阱**：这里的 $\Gamma_{15}$ 必须按 §2 的约定读作**乘积** $\Gamma^1\Gamma^5$；若读作 §12.4 新定义的 $\Gamma_{1+5}=(\Gamma_1+\Gamma_5)/\sqrt2$，则 $T'^2=-1$、(12.30) 不成立（**D11**，见 N5）。
- **D12**：$\tilde T\Gamma^{1589}=-\hat\Gamma_{10}$，配合 $\tilde T\epsilon=\hat\Gamma_{10}\epsilon=\epsilon$ 得 $\Gamma^{1589}\epsilon=-\epsilon$（(12.19) 的来源）。

### 4.5 结论

报告 §3.2 的表与类型判断正确：三类膜各保两个拓扑超荷（+2 个伴随 = 4 个超对称，四维 $1/4$ BPS、二维 $1/2$ BPS）；(B,B,B) 的算子是 $\Gamma^{04}$、(B,A,A) 是 $\Gamma^{1234}$、(A,B,A) 是 $-\Gamma_{15}\Gamma_{2-7}\Gamma_{3+6}$（或其 S-对偶像 (12.30)）；三者都与 $\Gamma^{2367}$ 对易，故两个条件相容、共同 $+1$ 本征空间 4 维。$\Gamma$ 代数的四组独立核验（D04/D05、D06/D08、D09/D10、D12/D13）全部通过。

### 4.6 与报告的差异

| 报告位置 | 差异 | 级别 |
|---|---|---|
| 行 345 | (12.22)–(12.23) 正确，但未注明 $\hat\Gamma^2=-1$（Lorentz 号差）这一前提；按 Euclid 读会得 $T'=0$ | 低（E14） |
| 行 434–441 表 | 表本身正确；仅 (B,B,B) 行「带全纯 CP 丛的空间填充膜」应为「带平坦规范场的空间填充膜」（p.215 third construction） | 低（E16） |

---

## 五、§12.3 的修改 Neumann 条件与 $[\varphi_2,\varphi_3]=F_{67}=0$（印刷 pp.215–217）

### 5.1 问题

逐式抄出 (12.24)(12.25)(12.26)(12.27) 并核符号（含 bar）；验证「要求 $\Gamma^{2367}\epsilon=\epsilon$ 不破缺 ⇒ $F_{26}-F_{73}=F_{27}-F_{36}=0$」这一步。

### 5.2 原文式与页

**(12.24)**（p.215 / p216.txt）：
$$\Big(\sum_{I,J\in\{1,2,3,4\}}+\sum_{I,J\notin\{1,2,3,4\}}\Big)\Gamma^{IJ}F_{IJ}\,\epsilon=0 .$$
由 (12.24) ⇒ $F_{0I}|=0\ (I>4)$，故 $A_I$ 对 $I>4$ 施 Dirichlet；取 $A_I|=0\ (I=5,8,9)$；「Higgs 场」$\varphi_2=A_6,\ \varphi_3=A_7$，$\varphi_z=\tfrac12(\varphi_2-i\varphi_3)$。**若 (12.24) 对所有满足 $\Gamma^{1234}\epsilon=\epsilon$ 的 $\epsilon$ 成立（不加 $\Gamma^{2367}\epsilon=\epsilon$），则 $[\varphi_2,\varphi_3]=F_{67}=0$。**

**(12.25)**（p.216）：
$$F_{12}|-F_{34}|=0,\qquad F_{13}|-F_{42}|=0,\qquad F_{14}|-F_{23}|=0,$$
（「which follow from imposing (12.24) with $\Gamma_{1234}\epsilon=\epsilon$」；注意 $F_{42}=-F_{24}$。）

**(12.26)**（p.216）：
$$F_{26}|-F_{73}|=0,\qquad F_{27}|-F_{36}|=0 .$$
「These equations are equivalent to $D_{\bar z}\varphi_z=0$, which is the "complex" Hitchin equation.」由「要求 $\Gamma^{2367}\epsilon=\epsilon$ 的超对称不破缺、令边界上费米子变分为零」得到；物理含义：$A_{\bar z}$（决定 $E$ 的全纯结构）可涨落、$\varphi_z$ 的特征多项式固定 ⇒ 膜支撑 Hitchin 纤维（原文用 "Presumably"）。

**(12.27)**（p.217 / p218.txt）：$T''=T'\Gamma^{2367}=-\Gamma_{1467}$；imposing $T''\epsilon=\epsilon$ 与 $T''\lambda|=+\lambda|$（**注意是 $+$**）得
$$\big[\Gamma^{IJ}F_{IJ},\,T''\big]\epsilon=0,$$
同样给 $A_6=\varphi_2,A_7=\varphi_3$ Dirichlet、$A_2,A_3$ Neumann。

原文紧接着的自我提醒（p.216）：**$[\varphi_2,\varphi_3]=0$ 不是 Hitchin 方程**；正确应为 $[\varphi_2,\varphi_3]-F_{23}=0$，多出的项 "presumably" 来自流向红外的 RG 流量子修正。

### 5.3 逐步推导（E 组）

1. **(12.24) 的来源（E08/D13）**：由 $T'\lambda|=-\lambda|$ 与 $T'\epsilon=\epsilon$，超对称要求 $(T'+1)\delta\lambda|=0$，$\delta\lambda=\tfrac12\Gamma^{IJ}F_{IJ}\epsilon$。对每一对 $\{I,J\}$，$T'\Gamma^{IJ}=(-1)^{\#(\{I,J\}\cap\{1,2,3,4\})}\Gamma^{IJ}T'$：mixed 项在 $\epsilon$ 上自动为零（因为 $T'\epsilon=\epsilon$），both-in/both-out 项留下 —— 正是 (12.24)。（脚本对 45 对逐一核验。）
2. **(12.24) ⇒ $F_{67}=0$、$F_{0I}=0$（E01）**：把 (12.24) 强加到 8 维空间 $\{\hat\Gamma_{10}=+1,\ \Gamma^{1234}=+1\}$ 上（未知量 = (12.24) 里出现的 21 个 $F_{IJ}$），线性系统零空间 3 维，被强制为零的分量包括 $F_{67}$ 与 $F_{0I}\ (I=5,\dots,9)$ ⇒ 原文这一步成立。
3. **(12.24) 的两个半支（E02/E02b）**：both-in 半（6 项）在同一个 8 维空间上给出**恰好 (12.25) 三式**（零空间 3 维）；both-out 半（15 项）给出 15 个分量全为零（含 $F_{67}$）。⇒ (12.25) 与 $[\varphi_2,\varphi_3]=0$ 来自同一个「8 维」条件。
4. **若只对 4 维不破缺空间施加 (12.24)（E03）**：$\{\hat\Gamma_{10}=+1,\ \Gamma^{2367}=+1,\ \Gamma^{1234}=+1\}$（4 维）上完整 (12.24) 的零空间 4 维，第三式被修正为
$$F_{14}-F_{23}+F_{67}=0,$$
即 $F_{67}$ 不再被单独逼零。⇒ 原文「对所有 $\Gamma^{1234}\epsilon=\epsilon$ 成立」这一**额外加强**才是 $[\varphi_2,\varphi_3]=0$ 的真正来源；4 维条件下得到的是 Hitchin 型关系。这是本次复算最意外的一条（见第 5.5 与 N12）。
5. **(12.26) 从哪里来（E04）**：在 $(12.27)$ 的 $T''$ 条件下，与 $T''$ 反对易的 24 个分量构成系统；在 4 维不破缺空间上零空间 4 维，**精确给出** $F_{26}+F_{37}=0$（即 $F_{26}-F_{73}=0$，因 $F_{73}=-F_{37}$）与 $F_{27}-F_{36}=0$ ⇒ (12.26) 成立。原文把 (12.26) 归在 $T'$ 构造的「$\Gamma^{2367}$ 不破缺」段；复算表明它更自然地从 $T''$ 构造（(12.27)）得到（两者等价，原文也说 $T''$ 构造「同样给 Dirichlet/Neumann」）。
6. **(12.26) ⇔ $D_{\bar z}\varphi_z=0$（E05）**：取 $\varphi_2=A_6,\varphi_3=A_7$ 为标量（$\partial_6=\partial_7=0$），$A_{\bar z}=\tfrac12(A_2+iA_3)$、$\varphi_z=\tfrac12(\varphi_2-i\varphi_3)$，则
$$F_{26}=D_2\varphi_2,\quad F_{27}=D_2\varphi_3,\quad F_{36}=D_3\varphi_2,\quad F_{73}=-D_3\varphi_3,$$
从而
$$D_{\bar z}\varphi_z=\tfrac14\Big[(F_{26}-F_{73})-i(F_{27}-F_{36})\Big].$$
矩阵恒等式数值核验通过 ⇒ 「复 Hitchin 方程」的说法精确成立。
7. **$[\varphi_2,\varphi_3]=F_{67}$（E06）**：$\varphi_2,\varphi_3$ 是标量，$F_{67}=\partial_6A_7-\partial_7A_6+[A_6,A_7]=[\varphi_2,\varphi_3]$。
8. **(12.26) 与 (12.16) 的关系（E07）**：(12.26) 两式正是 (12.16) Hitchin 自对偶方程中的后两式（文本层 p214/p217 可检索），与 (B,A,A) 膜的 Hitchin 方程自洽。
9. **符号核对（页图）**：(12.24)–(12.27) 逐字核过——特别是 (12.26) 的 Dirichlet 竖线 $|$ 与 $F_{26}-F_{73}$（不是 $F_{26}+F_{73}$；因 $F_{73}=-F_{37}$，它与 (12.16) 的 $F_{26}-F_{73}=0$ 是同一式）；(12.27) 的 $T''\lambda|=+\lambda|$ 是 **加号**（与 §12.3 的 $T'\lambda|=-\lambda|$ 相反），报告行 365 抄对了。

### 5.4 结论

- (12.24)–(12.27) 的符号（含 bar）全部核过；(12.24) 的投影结构、$F_{67}=0$、$F_{0I}=0$、(12.25) 三式、(12.26) 两式、$D_{\bar z}\varphi_z=0$ 的等价性、$[\varphi_2,\varphi_3]=F_{67}$ 均成立。
- 「$\Gamma^{2367}$ 不破缺 ⇒ (12.26)」这一步成立，但**最干净的推导在 $T''$ 构造一侧**（E04）；在 $T'$ 构造一侧，$\Gamma^{2367}$ 条件与 (12.24) 结合只额外给出 $F_{14}-F_{23}+F_{67}=0$（E03），要得到 (12.26) 需要 (12.27) 或等价的 Dirichlet 场边界条件。
- 原文「$[\varphi_2,\varphi_3]=0$ 不是 Hitchin 方程、正确应为 $[\varphi_2,\varphi_3]-F_{23}=0$」的自评成立；本复算补充了一个定量来源：$F_{67}$ 是否被逼零取决于对 8 维（所有 $\Gamma^{1234}\epsilon=\epsilon$）还是 4 维（真正不破缺）空间施加 (12.24)。

### 5.5 与报告的差异

| 报告位置 | 差异 | 级别 |
|---|---|---|
| 行 361 | 「等价于 $D_z\varphi_z=0$」写成 $D_z$，页图为 $D_{\bar z}\varphi_z=0$ | 中（E10） |
| 行 363 | 对 `[φ₂,φ₃]=0` 与 RG 修正的复述与原文一致 | — |
| 行 365 | $T''=-\Gamma_{1467}$、$T''\lambda|=\lambda|$ 抄对 | — |
| 行 479（§5 第 5 条） | 报告把「$[\varphi_2,\varphi_3]=0$ 与量子修正」列为「程度：高，全节最不放心」；本复算给出可定量复跑的结构（E03/E04），可把不确定度降为「结构已清楚，只剩原文 'presumably' 的物理解释」 | 低（非错误，见 E17） |

---

## 六、E 清单（报告错，分级）

> 判定基准：原文页图。报告 bar 错均可溯源到文本层（F03–F05 给出文本层对照串），属系统性转写问题，不改变结论，但**公式的符号结构是错的**。

### 高

（无）——没有影响结论或物理判断的错误。

### 中（11 条；公式的 bar/项序错）

| # | 报告行 | 错误 | 正确（页图） | 页 |
|---|---|---|---|---|
| E1 | 53 | (11.3) $\varphi_z\delta A_z+\varphi_{\bar z}\delta A_{\bar z}$ | $\varphi_z\delta A_{\bar z}+\varphi_{\bar z}\delta A_z$ | 185 |
| E2 | 87 | (11.10) $\mathrm{Tr}(\varphi_z\delta A_z)$ | $\delta A_{\bar z}$ | 189 |
| E3 | 149 | (11.17) $a_z\delta A_z+a_{\bar z}\delta A_{\bar z}$ | $a_z\delta A_{\bar z}+a_{\bar z}\delta A_z$ | 199 |
| E4 | 153 | (11.18) 同 E1 型 | $\varphi_z\delta A_{\bar z}+\varphi_{\bar z}\delta A_z$ | 199 |
| E5 | 157 | (11.19) $\varphi_z\delta A_z-\varphi_{\bar z}\delta A_{\bar z}$ | $\varphi_{\bar z}\delta A_z-\varphi_z\delta A_{\bar z}$（bar 与项序都反） | 199 |
| E6 | 159 | (11.20) $\dot A_z,\dot A_{\bar z}$ 互换；(11.21) $\varphi_z\dot A_z$ | (11.20) 第一项 $\dot A_{\bar z}$、第二项 $\dot A_z$；(11.21) $\dot A_{\bar z}$ | 199 |
| E7 | 163/165 | (11.24) 缺外层括号、$\delta/\delta A_z$ 应带 $\bar z$；(11.25) 的 $\upsilon_z,a_z$ 应带 $\bar z$（$\delta/\delta A_z$ 本身对） | (11.24) $\varphi_z\to-i\pi(\mathrm{Im}\tau)^{-1}\big(\delta/\delta A_{\bar z}+(i\mathrm{Im}\tau/2\pi)\upsilon_z-(i/2\pi)a_z\big)$；(11.25) $\delta/\delta A_z-(i\mathrm{Im}\tau/2\pi)\upsilon_{\bar z}-(i/2\pi)a_{\bar z}$ | 200 |
| E8 | 209/213/217 | (11.33)(11.34)(11.35) 的 $\bar z$ 全丢 | 三式全带 $\bar z$（见 §3.2） | 203 |
| E9 | 241 | (11.39) 第一项 $\delta A'_z$ | $\delta A'_{\bar z}$ | 206 |
| E10 | 361 | (12.26) 后 $D_z\varphi_z=0$ | $D_{\bar z}\varphi_z=0$ | 216 |
| E11 | 408 | (12.34) $\delta\varphi_z\wedge\delta A_z+\delta\varphi_{\bar z}\wedge\delta A_{\bar z}$ | $\delta\varphi_z\wedge\delta A_{\bar z}+\delta\varphi_{\bar z}\wedge\delta A_z$ | 220 |

### 低（6 条；措辞/理由/前提）

| # | 报告行 | 问题 |
|---|---|---|
| E12 | 61 | 「在 $K$ 下当然是 A-型：$\omega$ 本身取成 $(\mathrm{Im}\,\tau)\omega_K$」理由不足；应说 $F=(\mathrm{Im}\,\tau)\omega_J$ 在 $K$ 下是 $(2,0)\oplus(0,2)$ 型（非 $(1,1)$），故不能是 B-膜 |
| E13 | 143 | 同段先写 type F 是 $(A,B,A)$ 型、又写「$(B,A,A)$ 型膜正是本节的 type F 膜」，自相矛盾（承原文 p.198 笔误，见 N3/N4）；表 3.2 用的是 $(B,A,A)$ |
| E14 | 345 | (12.22)–(12.23) 未注明 $\hat\Gamma^2=-1$（Lorentz 号差）这一前提；按 Euclid 读会得 $T'=0$（D03/E09） |
| E15 | 428 | 「c.c. 膜存在且唯一」漏 $G$ 单连通条件（否则差平坦线丛扭转，行 55 已给对） |
| E16 | 436 | (B,B,B) 行「带全纯 CP 丛的空间填充膜」应为「带平坦规范场的空间填充膜」（原文 p.215 第三构造） |
| E17 | 428/479 | 「Yoneda 正则表示」措辞偏强（报告同段已注「尚未严格」）；§5 第 5 条的不确定度可下调（本文件 §5.3 第 4 条） |

---

## 七、N 清单（任务书 / 我们的解经本 / 术语勘误，非报告之错）

| # | 对象 | 内容 |
|---|---|---|
| N1 | **任务书术语** | 「§11.3 的 ξ」：原文与解经本均无 $\xi$；原文参数是 $\Psi=\theta/2\pi=\mathrm{Re}\,\tau$。本复算按 $\xi:=\Psi-h$ 解释（使 $\xi=0$ 对应普通 D-模）。建议任务书改称「$\Psi$（扭化指数 $\Psi-h$）」。 |
| N2 | **任务书/原文记号** | 原文的 $T'$ 被用了两次：§12.3 的 $T'=\Gamma^{1234}$ 与 §12.4 的 $T'=-\Gamma_{15}\Gamma_{2-7}\Gamma_{3+6}$；§12.4 还有 $T''=-\Gamma_{15}\Gamma_{2+7}\Gamma_{3-6}$。核对时须区分。 |
| N3 | **原文笔误** | p.184（p185.txt:14）：「the magnetic eigenbranes … are branes of type (A, B, A)」应为 $(B,A,A)$（Hitchin 纤维在 $I$ 复、$J,K$ Lagrange；与 p.76–78、p.207 矛盾，F06/F08）。 |
| N4 | **原文笔误** | p.198（p199.txt:11）：type F 膜「This is a brane of type (A, B, A)」同上，应为 $(B,A,A)$。 |
| N5 | **原文记号陷阱** | (12.28) 的「$\Gamma_{15}$」按 §2 约定是乘积 $\Gamma^1\Gamma^5$（无 $\pm$ 号的 $\Gamma_{IJ}$），不是 §12.4 新定义的 $\Gamma_{1+5}=(\Gamma_1+\Gamma_5)/\sqrt2$。混用会使 $T'^2=-1$、(12.30) 不成立（D11）。原文未明说。 |
| N6 | **原文约定** | §12 的 $(\hat\Gamma=(1\pm\cdots)/\sqrt2)$ 公式依赖 **Lorentz 号差** $\Gamma_0^2=-1$（故 $\hat\Gamma^2=-1$、$P_\pm$ 互逆而非投影）；原文说「避免 Wick rotation」，但把 $\hat\Gamma$ 称「四维手征」易被误读为投影（D03/E09/E14）。 |
| N7 | **解经本行 55** | 「两者维数相同（都是 $2\dim M(G,C)$ 与 $\dim M(G,C)$ 的关系）」表述自相矛盾：实际 $\dim\mathcal M_H=2\dim\mathcal M\ne\dim\mathcal M$。 |
| N8 | **解经本行 56/309/344** | 把 Hitchin 纤维/type F/磁特征膜写成 $(A,B,A)$（应 $(B,A,A)$），与行 523 的 $(B,A,A)$ 自相矛盾；承原文 N3/N4 的笔误。 |
| N9 | **解经本行 386/409/578** | (11.33) 第一式缺 $\bar z$、$\pi_0$ 与 (11.35) 的 $\bar z$ 全丢（行 386）；(11.39) 第一项缺 bar（行 409）；(12.34) bar 错（行 578）——与报告 E8/E9/E11 同源（照抄文本层）。 |
| N10 | **解经本页锚** | `\anchor{src p.N}` 实际用 PDF 页（=印刷页+1）：如行 542 的 `src p.218` 对应 (12.28) 在印刷 217；而 `sections/00_front.tex:68` 声称「两者页码一致（印刷页）」——系统性 +1 与声明不符（F24/F27）。 |
| N11 | **解经本行 180** | 「$(A,A,A)$ 不可能」的论证经数值复核**成立**（$\hat N_I^2=(b^2-a^2)-2abK$、$\hat N_J^2=(a^2-b^2)+2abK$；A-型于 $I$ 须 $b=0$、于 $J$ 须 $a=0$）。本复算最初怀疑其有误，实为正确（A08/F26）。 |
| N12 | **原文论证的另一种读法** | p.216 的「$[\varphi_2,\varphi_3]=0$ 为经典结果、多余项来自量子修正」：本复算显示 $F_{67}$ 是否被逼零取决于对 8 维（所有 $\Gamma^{1234}\epsilon=\epsilon$）还是 4 维（真正不破缺）空间施加 (12.24)——4 维下第三式为 $F_{14}-F_{23}+F_{67}=0$（E03）。原文的「量子修正」不是唯一可能的解释。 |
| N13 | **解经本行 55（其二）** | 「D-模生活在 $\mathcal M=M(G,C)$」是简化：原文 p.196 明确说只做 $\mathcal M(G,C)$ 不够、要在 $\mathrm{Bun}_G(C)$ 栈上（本文件 §2.2 第 2 步）。建议加注。 |
| N14 | **页图 vs 文本层** | 原文文本层没有任何 combining macron（F02），(11.3)(11.10)(11.17)–(11.25)(11.33)–(11.39)(12.26)(12.34) 的 bar 全丢；任何「以文本层为准」的转写都会出现 E1–E11 型错误。 |

---

## 八、PASS/FAIL 统计

脚本：`calc/recalc_r8.py`（纯标准库 python，`python calc/recalc_r8.py`，约 0.35 s，退出码 0 = 全 PASS）。

| 组 | 条目 | PASS | FAIL |
|---|---|---|---|
| A. §11.1 c.c. 膜（第 1 件） | A01–A12（12） | 12 | 0 |
| B. §11.2 A-膜 ⇒ D-模（第 2 件） | B01–B07（7） | 7 | 0 |
| C. §11.3 $\xi=\Psi-h$（第 3 件） | C01–C08（8） | 8 | 0 |
| D. §12 三类膜超荷（第 4 件） | D01–D14（14） | 14 | 0 |
| E. §12.3 (12.24)–(12.27)（第 5 件） | E01,E02,E02b,E03–E09（10） | 10 | 0 |
| F. 文本层/页锚/报告与解经本出入 | F01–F27（27） | 27 | 0 |
| **合计** | **78** | **78** | **0** |

- 报告错（E）：**高 0 / 中 11 / 低 6**（共 17 条）。
- 勘误（N）：**14 条**（任务书术语 1、原文笔误/记号/约定 5、解经本 8 条含页锚）。
- 最意外一条：**§12.3 的 $[\varphi_2,\varphi_3]=F_{67}=0$ 取决于「(12.24) 对 8 维还是 4 维超荷空间施加」**——4 维（真正不破缺）下第三式自动变成 $F_{14}-F_{23}+F_{67}=0$（E03），故原文所说的「经典分析得多余项、需量子修正」可能只是把条件加强到 8 维的产物；同一系统在 $T''$ 构造下则干净地给出 (12.26)（E04）。
- 报告未发现的实质错误：无；报告的问题集中在 bar 转写（11 条中 10 条）与 $(A,B,A)/(B,A,A)$ 的原文笔误继承（E13）。
