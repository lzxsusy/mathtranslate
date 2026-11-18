# 概览与第 1 章 校对报告（主控）

校对范围：`chapters/overview.tex`（72 行，原书 p.7–9）与 `chapters/ch01.tex`（332 行，原书 p.10–23）。
外部依据：nLab `monodromy`（last revised 2026-11-09）、`mirror symmetry`（2024-04-01）、`Calabi-Yau manifold`（2026-01-06）；英文原文 `orig_full.txt` 第 158–1046 行。

改动 4 条，另记 4 条「原文如此」。

| # | 位置 | 类别 | 现译 | 改为 | 依据 | 置信度 |
|---|---|---|---|---|---|---|
| 1 | overview.tex:27 | 表述 | 使这两个数不再交换 | 使这两个数不再被互换 | 原文 p.8 "some other X′ where these are not flipped"；"交换"易误读为 Hodge 数的乘法交换 | 高 |
| 2 | ch01.tex:116 | 数学 | 现在对其中保持全纯体积形式的子群 $G=(\mathbb{Z}/5)^3$ 取有限商 | 现在对其中的一个子群 $G=(\mathbb{Z}/5)^3\subset(\mathbb{Z}/5)^4$（即固定一个坐标、例如令 $\zeta_0=1$ 的那些元素）取有限商 | 原书 p.15 只写 $G=(\mathbb{Z}/5)^3\subset(\mathbb{Z}/5)^4$，未加「保持全纯体积形式」；该条件对 $(\mathbb{Z}/5)^4$ 全体成立而非只对 $(\mathbb{Z}/5)^3$，原译把一个不分辨子群的条件当成了选取条件。Cox–Katz 的标准取法即固定 $x_0$ | 高 |
| 3 | ch01.tex:161 | 表述 | $N_d$ 是次数为 $d$ 的有理曲线，即亏格 $g=0$ 曲线的 Gromov–Witten 计数 | $N_d$ 是次数为 $d$ 的有理曲线（即亏格 $g=0$ 的曲线）的 Gromov–Witten 计数 | 原句"是……曲线"与"的计数"错配，逗号断开后中心语悬空 | 高 |
| 4 | ch01.tex:277、330 | 术语 | 单值化（monodromy） | 单值变换（monodromy）；\Term{danzhi} 索引词条同步改为「单值变换」 | 原文 p.21 "This has something to do with monodromy…the monodromy of $z^{A(0)}$ reflects the monodromy $T$"；nLab `monodromy`（2026-11-09）。「单值化」在中文里固定指 uniformization（单值化定理），与 monodromy 不是一回事；且 ch03.tex:401 已用「单值变换」，全书不一致 | 高 |

## 原文如此（不改为好，已在此留痕）

1. overview.tex:25「以某个十维空间 $\mathbb{R}^{1,3}\times X$ 为靶空间的超对称 $\sigma$ 模型」——原文 p.7 即写作 "super-symmetric σ-models with target some 10-dimensional space R^{1,3}×X"，并带脚注"To have an anomaly free theory"。物理学上世界面 σ 模型的靶空间是 $X$，$\mathbb{R}^{1,3}\times X$ 是十维时空；这是讲授者本人的说法，不改，仅记录。
2. overview.tex:10 例 0.1 标题：原文作 "Quartic in P⁴"，但例题内容是五次超曲面，属原文笔误；译本作「五次超曲面」正确，不回调。
3. overview.tex:57「Lian、Liu 与 Yau」：原文作 "Lian, Liu, and Yan"，Yan 为 Yau 的笔误；译本正确。
4. ch01.tex:147/152/153 特殊纤维：原文先说 "smooth for z ≠ 0,1"，随后又列 $z=5^{-5}$ 与 $z=1$，与 $z=(5\psi)^{-5}$ 自相矛盾（$\psi=0$ 对应 $z=\infty$，不是 $1$）。译本统一为 $z\neq0,5^{-5},\infty$、$z=\infty$ 即 $\psi=0$，与数学一致，保留。

## 逐句对照中确认无误的重点（抽样）

- 模空间维数 $126-1-24=101$、$h^1(\Theta_X)=101$、Hodge 菱形 101/101（原书 p.10–14）。
- 射影消解中例外除子计数：10 条 $C_{ij}$ 各 4 个 + 10 个 $P_{ijk}$ 各 6 个 = 100，加超平面类得 $h^{1,1}=101$（原书 p.16）。
- 镜像族 $f_\psi=\sum x_i^5-5\psi x_0\cdots x_4$、$z=(5\psi)^{-5}$、$z=5^{-5}$ 处 125 个三维 $A_1$ 奇点在同一个 $(\mathbb{Z}/5)^3$ 轨道上（原书 p.17）。
- Picard–Fuchs 算子 $[\theta^4-5z(5\theta+1)(5\theta+2)(5\theta+3)(5\theta+4)]\varphi=0$；$c_3(z)=6/z-2\cdot5^5/(1-5^5z)$；$n_1=2875,n_2=609250,n_3=317206375$（原书 p.21–23）。
- Kontsevich 1994 ICM 与 HMS 的范畴表述 $D\,\mathrm{Fuk}(X)=D^b(\mathcal{O}_Y)$，与 nLab `mirror symmetry`「Kontsevich 1994 … equivalence of $A_\infty$-categories」一致。
