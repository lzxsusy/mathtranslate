# B · §1 骨架与 k 量子化

> 依据：`witten1989/sections/s01-cs-action.tex`（据 pages300 逐符号核对）、`deliver/校勘与审校批注汇总.md`、河野俊丈《场论与拓扑学》中译 §2.5。页锚＝印刷页（PDF = 印刷 − 350）。

**一句话**：§1 把"解释 Jones 多项式"换成一个不需要度规的场论；代价是只能取一阶 CS (1.3)，而 $e^{iL}$ 要在大规范变换下良定义，就把 $k$ 逼成整数。这一步是 **argue**，不是 **prove**。

## 一、五问

### 1. (1.2) 为何弃用 [src p.353]
度规出现两处，角色不同：$\sqrt g$ 是体积元，可换成任一正定体积形式（只要定向）；$g^{ik}g^{jl}$ 把两个 $F$ 缩成标量，无内积不可替（三维中 $F\wedge F$ 是 4-形式，恒零）。故"$\sqrt g$ 可救、$g^{ik}g^{jl}$ 不可救"（据上下文重建）。实质不是 YM 不好，是 (1.2) 依赖 $g$，其配分函数不可能是拓扑不变量；三维无度规二阶项不存在，只能退到一阶 CS。

### 2. (1.3) 两性质 [eq 1.3, src p.354]
(a) **只依赖定向**：被积式是 3-形式，分量式只出 $\varepsilon^{ijk}$、不出 $g^{ij}$。
(b) **变分给 $F=0$（可复算）**：

$$\delta\!\int\Tr\!\left(A\mathrm dA+\tfrac23A^3\right)=\int\big[2\Tr(\delta A\wedge\mathrm dA)+2\Tr(\delta A\wedge A^2)\big]=2\int\Tr(\delta A\wedge F)$$

（边界项 $\mathrm d\Tr(\delta A\wedge A)$ 闭流形为零）⇒ $\delta L=\frac{k}{2\pi}\int\Tr(\delta A\wedge F)$，$\forall\delta A\Rightarrow F=0$。系数是 $k/2\pi$ 不是 $k/4\pi$（一阶变分带因子 2）；算错会在 §2 驻相差 2。

### 3. (1.4) 绕数 → $k\in\mathbb Z$ [src p.354]
规范群 $\mathrm{Map}(M,G)$ 不连通，由 $[M,G]$ 分类；紧致单群 $\pi_3(G)\cong\mathbb Z$ ⇒ 每个 $g$ 带整数绕数 $m$（$M=S^3$ 即映射度）。规范变换下 $\Delta L=\frac{k}{4\pi}\cdot\frac13\int\Tr(g^{-1}\mathrm dg)^3$；取 $\Tr$ 使 $\frac{1}{24\pi^2}\int\Tr(g^{-1}\mathrm dg)^3=m$（$SU(N)$ 定义表示正是如此），得 $\Delta L=\frac{k}{4\pi}\cdot 8\pi^2m=2\pi k\,m$。原文 (1.4) 只写 $\mathrm{const}\cdot m$，$2\pi k$ 是取定归一化后的值。单值性 $e^{i\Delta L}=1\ \forall m\iff k\in\mathbb Z$，$m=1$ 给必要性。

### 4. 证明还是论证 [src p.354]
**argue**，三条：(i) 只证了经典作用量指数在 $\mathcal A/\mathcal G$ 良定义，测度 $\mathcal D\mathcal A$ 的规范不变性未证（(1.6) 的 $\mathcal D\mathcal A$ 原文只当形式记号 [p.355]）；(ii) 充分性用的正是"$k\in\mathbb Z\Rightarrow e^{iL}$ 下降"，再**假设**测度随之下降；(iii) 原文说"对任意 $G$ 可唯一确定 $\Tr$ 归一化，使条件为 $k\in\mathbb Z$"[p.354]——把内容放进约定：常数 $2\pi k$ 是归一化的结果，不是定理。事后 RT 1991 在组合侧严格化；§2 标架反常平移 $k+c_2/2$（译本 p.365 $\delta=n_a^2/2k$ 与 (2.32) $2\pi i n_a^2/k$ 差因子 2，引用先校，校勘 D5）。

### 5. (1.5)(1.6) 纽结 → Wilson 线；两变量 [src p.355]
(1.5) $W_R=\Tr_R P\exp\oint A$：$P$ 路径排序、和乐只共轭类良定义故须取表示迹、不需度规。(1.6) 把链环变成沿 $C_i$ 插入 Wilson 线；$Z$ 只依赖 $C_i$ 嵌入的同痕类 ⇒ 拓扑不变量。原文措辞 **"we will claim"**：断言，非证明。参数：$SU(N)$+所有 $R$ 取定义表示 ⇒ 两变量 $(N,k)$，都可解析延拓为复值；$SO(N)$+$N$ 维 ⇒ Kauffman[p.355]。显式关系 $q=\exp(2\pi i/(N+k))$[eq 4.21]（$SU(2)$ 时 $e^{2\pi i/(k+2)}$）：整数 $k$ ↔ $q$ 为单位根。截面看即共形块空间中的标记点[src p.366]。

## 二、查资料

### A. 河野 §2.5（中译 PDF p.84–88 = 原书 p.70–74）
走法：CS 泛函 → 临界点＝平坦联络 → 大规范变换只改整数 → 辛形式/复线丛 → Marsden–Weinstein 商 → 共形块截面。

| 项 | 河野（$SU(2)$ 固定） | Witten |
|---|---|---|
| CS | (2.33) $\frac{1}{8\pi^2}\int\Tr(A\mathrm dA+\frac23A^3)$，**不含 $k$**；$Z=\int e^{2\pi ik\,CS}$（原书 p.73） | (1.3) $\frac{k}{4\pi}\int$，$e^{iL}$ |
| 临界点 | 命题 2.21：$CS(A+ta)=CS(A)+\frac{t}{4\pi^2}\int\Tr(F\wedge a)+O(t^2)$ | $\delta L=\frac{k}{2\pi}\int\Tr(\delta A\wedge F)$ |
| 大规范 | (2.36) $CS(g^*A)=CS(A)-\int g^*\sigma$，$\int g^*\sigma=\deg\in\mathbb Z\Rightarrow CS\in\mathbb R/\mathbb Z$ | (1.4) $+$const$\cdot m$ |
| 相空间 | (2.37) $\omega=-\frac{1}{8\pi^2}\int_\Sigma\Tr(\alpha\wedge\beta)$；商 $\cong\mathrm{Hom}(\pi_1,G)/G$ | §3[p.367] |

关系：$2\pi ik\cdot\frac{1}{8\pi^2}=\frac{ik}{4\pi}$ ⇒ $CS_{\text{河野}}=L/(2\pi k)$；临界系数比 $\frac{k/2\pi}{1/4\pi^2}=2\pi k$ 自洽。三处"2"别混：(1.3) 形式 $k/4\pi$ 与分量 $k/8\pi$ 差 2（由 $\int\Tr A\mathrm dA=\frac12\int\varepsilon\Tr A_i(\partial_jA_k-\partial_kA_j)$ 吸收），与 $2\pi$ 的账无关。差异：河野固定单连通 $SU(2)$，Witten 用任意紧致单群。

### B. errata「(1.2) 漏 1/4」
**不影响 Q1，且该疑点已被判否**：s01 tex「复核记录」(tr2, 2026-10-27) 对照 `pages300/page-03.png` 逐符号核，原刊 (1.2) 即 $\int\sqrt g\,g^{ik}g^{jl}\Tr(F_{ij}F_{kl})$，**无 1/4、无负号**；与 $-\frac14\int\sqrt g\Tr F^2$ 的差别全来自脚注 1 的 $\Tr$ 归一化（Cartan–Killing 倍数）+ 反厄米约定。`校勘汇总:15` 亦记"照印、系数已吸收进脚注 1"，非疑误（`已译资料清单` §B-T0 的二手转述应以此为准）。与 Q1 无关：依赖度规的是 $\sqrt g$ 与 $g^{ik}g^{jl}$ 的**结构**，与常数无关。别写"原文漏 1/4"。

## 三、预设质询
1. **(1.3) 的 $k$ 与 (3.2) 的 $4\pi/k$ 是同一个 $k$**：(3.1) 只是 (1.3) 取 $A_0=0$ 后逐项重写（立方项冻结），零重标度；$\theta=\frac{k}{8\pi}\int\varepsilon^{ij}\Tr A_i\delta A_j$ 之逆给 $4\pi/k$，其"2"来自 $\varepsilon$ 与 $\delta A_1\wedge\delta A_2$ 的约定，非两个耦合。(4.21) 的 $k$ 同此（WZW 能级 $k+N$）。
2. **换表示**：$\Tr$ 归一化固定后常数即 $2\pi k$，与 $R$ 无关；但 WZW 能级是 $k+h^\vee$（$SU(N)$ 时 $N$，见 (4.21) 分母 $N+k$）。**原文没写"长根平方=2"**——后人标准化（Kac 书一类），须标"据上下文重建"。

## 四、最虚
- 河野 (2.37) 与 (3.1) 只核到作用量/指数层面（$2\pi ik/8\pi^2=ik/4\pi$、临界系数比 $2\pi k$）；**辛形式层面未逐项核**（河野带负号、$1/8\pi^2$ 与 $k/8\pi$ 间还差 $\pi$ 的位次）。
- (1.4) 的 $2\pi k$ 原文未给，是按标准归一化算的（重建）。
- 一般 $G$ 的"唯一归一化"未独立验算，只复核 $SU(N)$ 定义表示。

## 五、锚点
(1.2) p.353；(1.3)(1.4)"必要且充分" p.354；(1.5)(1.6)"we will claim"、两变量、Kauffman p.355；定向/复共轭 p.356；截面标记点 p.366；$q$ eq 4.21；河野 (2.33)–(2.37) 原书 p.71–73。
