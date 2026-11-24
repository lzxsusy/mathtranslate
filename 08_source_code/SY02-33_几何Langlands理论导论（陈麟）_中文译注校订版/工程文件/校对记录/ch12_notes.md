## 待注 ch12.tex:23（原 PDF p60）

- 原文：The functor $f_!$ is already subtle topologically: for instance, for $\mathrm{pt}\to S^1$, the result corresponds to a local system with an infinite Jordan block.
- 概念：$f_!$ 是 $f^*$ 的左伴随，由带紧支撑的左 Kan 延拓给出；对 $\mathrm{pt}\to S^1$，$f_!(k)$ 是普遍覆盖 $\mathbb R$ 上的紧支撑函数，单值化 $\mathbb Z$ 以平移作用，所得 $\mathbb Z$-局部系统无限维，且单值算子恰是一个无限 Jordan 块——所以它不能留在可构造/有限秩范畴内。
- 读者缺什么：只读译文会以为要点是“无限维”，看不到“单个无限 Jordan 块”这一结构信息；也不清楚这个例子为什么能说明 $f_!$ 的微妙。
- 建议来源：nLab "Kan extension"；nLab "six operations"。

## 待注 ch12.tex:33–35（原 PDF p60–p61）

- 原文：… an action of the spectral monoidal category $\mathrm{Perf}(\mathrm{Maps}(Y,B\check G))$, or of its presentable $\mathrm{QCoh}$-completion …, on a dualizable DG category $\mathcal C$ is encoded by the following factorization data. For every finite set $I$, one has a monoidal functor $\mathrm{Rep}(\check G)^{\otimes I}\to\mathrm{End}(\mathcal C)\otimes\mathrm{LocSys}(Y^I)$, compatible with all maps of finite sets.
- 概念：Betti 局部到整体定理（[NY19]、[AGK$^+$20a]）：在可对偶 DG 范畴 $\mathcal C$ 上给谱幺半范畴的作用，等价于给一族与有限集映射相容的幺半函子 $\mathrm{Rep}(\check G)^{\otimes I}\to\mathrm{End}(\mathcal C)\otimes\mathrm{LocSys}(Y^I)$；对角映射 $Y^J\to Y^I$ 负责相容性方块。
- 读者缺什么：不理解“作用”为何能被这族函子完全编码（可对偶性加 $\QCoh$ 的幺半结构）、$\mathrm{End}(\mathcal C)$ 是什么、$\mathrm{LocSys}(Y^I)$ 记录了什么。
- 建议来源：nLab "factorization algebra"；nLab "dualizable object"。

## 待注 ch12.tex:43–46（原 PDF p61）

- 原文：The local Hecke categories are organized into a Ran-category expression $\mathrm{Rep}(\check G)_{\mathrm{Ran}}\simeq\operatorname{colim}_I(\mathrm{Rep}(\check G)^{\otimes I}\otimes\DMod(X^I))$, with transition maps built from diagonals.
- 概念：Ran 空间 $X_{\mathrm{Ran}}$ 是有限子集配置空间的余极限；Ran 范畴即沿 $I\mapsto X^I$ 的余极限，过渡映射来自对角映射 $X^I\to X^J$，从而把因子化结构编码成一个范畴。de Rham 侧把它记作 $\Rep(\checkG)_{\mathrm{Ran}}$。
- 读者缺什么：不知道 Ran 空间的余极限定义、为什么 Hecke 范畴要组织成 Ran 范畴，也不清楚它的核为何“很大”并与消失猜想相关。
- 建议来源：nLab "Ran space"；nLab "factorization algebra"。

## 待注 ch12.tex:86（原 PDF p62）

- 原文：$\mathrm{LocSys}^{\mathrm{restr}}_{\check G}(S):=\mathrm{Fun}^{\otimes,\mathrm{r.t.ex.}}(\mathrm{Rep}(\check G),\mathrm{QLisse}(S\times X))$.
- 概念：受限谱叠的点函子定义：取张量函子 $\Rep(\checkG)\to\operatorname{QLisse}(S\times X)$，并要求右 $t$-正合（r. t. ex.）；用 $\operatorname{QLisse}$ 取代 $\LocSys$，使族只沿 $X$ 的零奇异支撑方向变动；对仿射 $S$ 可启发式地看成 $\QCoh(S)\otimes\operatorname{QLisse}(X)$-值。
- 读者缺什么：不明白为什么必须加“右 $t$-正合”（不加则函子过多、失去几何意义），也不知道 $\operatorname{QLisse}(S\times X)$ 与 $\QCoh(S)\otimes\operatorname{QLisse}(X)$ 的差别。
- 建议来源：nLab "t-structure"；nLab "Tannaka duality"。

## 待注 ch12.tex:120–128（原 PDF p63）

- 原文：For a dualizable DG category $\mathcal C$ and an endofunctor $F:\mathcal C\to\mathcal C$, the same formula gives an object of $\mathrm{Vect}$: $\mathrm{Tr}(F;\mathcal C):=[\mathrm{Vect}\xrightarrow{\mathrm{coev}}\mathcal C\otimes\mathcal C^\vee\xrightarrow{F\otimes\mathrm{Id}}\mathcal C\otimes\mathcal C^\vee\xrightarrow{\mathrm{ev}}\mathrm{Vect}]$.
- 概念：范畴迹：把有限维线性代数的迹公式搬到对称幺半 DG 范畴，$\mathrm{coev}$/$\mathrm{ev}$ 是 $\mathcal C$ 的对偶单位与余单位；结果落在 $\mathrm{Vect}$ 中（一个复形）。取 $F=\Fr$ 时它应当就是 $\Bun_G(\mathbb F_q)$ 上的函数空间。
- 读者缺什么：不清楚“可对偶（rigid）范畴”的条件、为什么迹落在 $\mathrm{Vect}$ 而不是 $\mathcal C$ 里，也不知道它与 Hochschild 同调的关系。
- 建议来源：nLab "categorical trace"；nLab "dualizable object"。

## 待注 ch12.tex:142–144（原 PDF p63）

- 原文：$\mathrm{LocSys}^{\mathrm{restr},\Fr}_{\check G}:=\mathrm{LocSys}^{\mathrm{restr}}_{\check G}\times_{\mathrm{LocSys}^{\mathrm{restr}}_{\check G}\times\mathrm{LocSys}^{\mathrm{restr}}_{\check G},\Delta,(\mathrm{Id},\Fr)}\mathrm{LocSys}^{\mathrm{restr}}_{\check G}$, whose points are restricted Weil $\check G$-local systems.
- 概念：用 $(\mathrm{Id},\Fr)$ 与对角 $\Delta$ 的纤维积取 Frobenius 不动点；其点满足 $\Fr(\sigma)\cong\sigma$，即带 Frobenius 结构的“受限 Weil $\check G$-局部系统”。借此把迹提升为拟凝聚层，取全局截面即回到自守迹空间。
- 读者缺什么：不明白为什么用纤维积（而非等化子）刻画不动点、纤维积要在导出/$\infty$-范畴意义下取，以及 Weil 局部系统的定义。
- 建议来源：nLab "Frobenius morphism"；nLab "geometric Langlands correspondence"。
