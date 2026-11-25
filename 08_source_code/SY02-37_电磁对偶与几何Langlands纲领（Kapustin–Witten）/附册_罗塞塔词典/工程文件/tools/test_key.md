# 盲测评分要点（lead 内部用，不交给被测智能体）

每题满分 1 分，按「关键事实命中数 / 关键事实总数」折算；出现与事实相反的陈述，该题直接 0。

1. $S$-对偶：要点（a）$\tau=\theta/2\pi+4\pi i/g^2\to-1/\tau$；（b）扭化参数 $\Psi$（KW06 里 $\Psi$ 与 $\tau$ 相关，$\Psi=(\tau+\bar\tau)/\tau$ 之类，量级对即可）在 $S$ 下 $\Psi\to-1/\Psi$；（c）$t$ 是扭化后剩下的参数，$S$-对偶下 $t\to t$ 或按 $SU(2)$ 作用（原文 §4.1 有 $t\to (at+b)/(ct+d)$ 的 modular 作用）；（d）A-模型（辛）与 B-模型（复）互换，机理是 Hitchin 模空间的 $I$ 与 $J$ 在 $S$ 下互换（$J\to K$ 等）。
2. 特征膜：$\mathcal M_H$ 上被 Hecke 算子作用为「特征对象」的膜；电特征膜 ↔ Hecke 特征层（$\mathcal D$-模侧，$\mathrm{Bun}_G$ 上），磁特征膜 ↔ 对偶群 ${}^LG$ 侧的层（$\mathrm{Bun}_{{}^LG}$ 上）；$\mathrm{Op}$ / oper 与平坦 ${}^LG$-联络相关。
3. 't Hooft 算子：要点（a）Wilson 线 = 沿曲线/点的 Hecke 算子作用于零膜/电特征膜；（b）'t Hooft 线是 $S$-对偶像，对应磁侧的 Hecke 算子（沿对偶点）；（c）几何实现依赖单极子模空间/仿射 Grassmann 上的卷积；（d）'t Hooft 算子的 OPE 系数 ↔ 磁特征膜（拉格朗日膜 = $\varphi$ 的谱覆盖/纤维）上的交织。
4. $B_{cc}$：数学上是 $\mathcal M_H$ 上支撑在整个空间、由复结构 $I$ 定义的余各向同性 A-膜（$\mathrm{CH}^\bullet$ 上的 B-模型对应物不准确）；与 $\mathcal D$-模 ↔ 余切丛 B-膜的 A-模型化有关；§11 用它把 A-膜范畴翻成 $\mathcal D$-模（$B_{cc}\otimes\cdot$ 给出 A-膜 → $\mathcal D$-模的函子）。
5. $I$（复结构）↔ B-模型；$J$、$K$（辛结构 / 复结构）↔ A-模型；三种扭化对应三个复结构（$t$ 参数化的 twistor line），$S$-对偶把 $I$ 与 $J$ 互换。
6. 扭化：（a）取超荷的 $SU(2)_R$ 子群重新定义自旋；（b）出现标量超荷 $Q$（$Q^2=0$）；（c）$Q$-上同调里的可观测（关联函数）不依赖度规 → 拓扑场论；（d）路径积分只依赖拓扑（相交数、瞬子数）。
7. 单极子 ↔ Hecke：BPS 单极子模空间 $\cong$ 某仿射 Grassmann 的 Schubert 胞腔/卷积图；Nahm 极点给出奇异点数据（磁荷的极点），单极子解沿 $\mathbb R^3$ 上的 Nahm 方程给出模空间，其几何给出 Hecke 算子的卷积实现（Kapustin 的『单极子 = Hecke 算子』）。
8. 几何 Langlands：$A$-膜/$\mathcal D$-模（$\mathrm{Bun}_G$ 侧）与 $B$-膜/相干层/特征层（$\mathrm{Loc}_{{}^LG}$ 侧）的等价；物理实现：$A$-膜 ↔ $\mathcal D$-模（$B_{cc}$ 机制），$B$-膜 ↔ 相干层。
9. $G \leftrightarrow {}^LG$：根/余根互换，$\pi_1(G)\cong Z({}^LG)$、$Z(G)\cong\pi_1({}^LG)$；'t Hooft 通量是磁荷，取离散值于 $\pi_1(G)$（因为 $G$ 的中心/拓扑），Wilson 线是电荷，对应 ${}^LG$ 的中心；这就是 §2 的核心观察。
10. 谱曲线：$\det(\lambda-\phi)=0$ 在 $T^\ast C$ 里给出覆盖 $\Sigma\subset T^\ast C\to C$；Hitchin 纤维化 $\mathcal M_H\to\mathcal B$ 的纤维是 $\Sigma$ 的 Jacobi/Prym 簇；Hitchin 系统可积因为 $\mathcal M_H$ 有 $3$ 个复结构且纤维是阿贝尔簇（可积系统的紧复环面纤维），$I$ 下的全纯辛形式给出可积结构。

## 及格线
- ≥8/10 且无「与事实相反」的表述 → 通过；
- 6–7 或有个别反向错误 → 记下缺哪个词条/哪段解释不足，补写后重测；
- <6 → 词典结构问题，需在 front「怎么用」里补地图或增加总表条目。

## 重点观察
- 被测者能否**不借助外部知识**说出「为什么」（对应机制），而不仅是背下两侧定义；
- 第 3、4、7 题（Hecke 的三重实现）是最能暴露词典是否讲透的地方；
- 若被测者在某题写「词典不足」，记录缺什么——这正是 v1.1 要补的。
