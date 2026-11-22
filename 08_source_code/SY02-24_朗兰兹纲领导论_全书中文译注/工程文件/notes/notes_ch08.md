# 第 8 章 通读笔记（Daniel Bump, *Spectral Theory and the Trace Formula*）

## 一、版本与页面对应

- 原文：`work/en/ch08_raw.txt`，范围 PDF 156–199 = 印刷页 153–196，共 44 页。
- 页图：`work/pages/ch08/p0156.png`–`p0199.png`（**文件名即 PDF 页号**；`mutool draw -o p%04d.png` 实际按页号命名，并非从 0001 起）。
- 换算：**印刷页 n = PDF 页 n+3**。例：p0156 = 印刷 153（章首页），p0199 = 印刷 196（只有 [53] 一行）。
- 页眉：偶数页 `154 Daniel Bump`，奇数页 `8. Spectral Theory and the Trace Formula`。
- 本章无编号段落（原书只有定理、命题、引理 1–55 与公式 (1)–(60)），故 `ch08.tex` 未使用 `\ob`；节号照原书 1–10。

## 二、结构（10 节）

1. **谱问题**（印刷 153–155）：$\Delta=-y^2(\partial_x^2+\partial_y^2)$；命题 1（基本区域边界成对测地弧）、命题 2（对称正定，(2) 为边界积分）；定理 3（$\mathcal H^\circ$ 交换，Gelfand）、定理 4（$V^K$ 至多一维）、命题 5（$V(k)$ 至多一维）；$T_\phi$ 的核 (4)、命题 6 (5)、定理 7（紧）、自伴条件 (6)、定理 8、定理 9（$L^2(X)$ 有 $\Delta$ 特征基）、引理 10（Langlands）、定理 11（$L^2(\Gamma\backslash G)$ 分解）；末段用全纯模形式构造无 $K$-不变向量的不可约子空间（权 $k$ 全纯离散序列）。
2. **积分算子环**（155–161）：右正则表示、$\mathfrak g$ 与 $U(\mathfrak g)$；Casimir 元 (3) $-4\Delta=H\cdot H+2R\cdot L+2L\cdot R$；$\mathcal H$、$\mathcal H^\circ$；adelic 推广（$\Gamma=\mathrm{SL}(2,\mathbb Z)$、$Z_{\A}$、$K_p$、$\mathcal H_p$、$T_p$）。
3. **Green 函数与谱预解式**（161–166）：Property S；Cayley 变换 $r=(y-1)/(y+1)$ 与 (7)；引理 12；$g_s(z,\zeta)$；定理 13 (8) 五条；定理 14（表示公式）；命题 15（$G_s$ 绝对收敛）；定理 16 (9)；定理 17（谱离散、自伴延拓）；例外特征值与 Randol、Selberg 猜想。
4. **球函数**（166–169）：$\lambda$-球函数；定理 18 (10)(11)；$f_s$ (12)；定理 19 (13)(14)；定理 20（$\chi_\lambda$ 是特征）；主系列 (15)、$M(s)$ (16)、$f_{s,k}$ (17)、$M(s)f_{s,k}$ (18)、酉性与补系列、(19)。
5. **Plancherel 公式**（169–172）：(20)(21)；定理 21 (22)；Iwasawa 坐标 (23)；定理 22；引理 23–25 (24)–(27)；定理 22 的证明 (28)(29)；命题 26（$g\mapsto\phi$ 满）。
6. **Selberg 迹公式**（173–175）：(30)；定理 27（迹类）(31)(32)；定理 28 (33)；定理 29 (34)；双曲/椭圆、$N(\gamma)$ (35)、$N_0$；定理 30 (36)；定理 31 (37)。
7. **Selberg zeta 函数**（175–180）：定理 32（$h$ 的解析性放宽）；定理 33（Weyl 律）；定理 34 (38)（显式公式）；注 1–4（注 4 为有限域曲线类比）；$Z(s)$、定理 35、引理 36、(39) 与解析延拓。
8. **带一个尖点的群**（180–185）：(40) 尖点形式；定理 37（Gelfand–Graev–Piatetski-Shapiro，$T_\phi|_{L_0^2}$ 紧）；定理 38；Eisenstein 级数 (41)；命题 39 (42)；常数项 (43)；命题 40 (44)(45)(46)；定理 41（亚纯延拓与函数方程）；Bernstein–Selberg 原则；命题 42、43；(47) 与定理 44。
9. **谱展开**（185–188）：(48)；命题 45、46；(49)(50)；命题 47 (51)、48；命题 49 (52)(53)(54)；命题 50；定理 51 (55) 及 (56)–(58)。
10. **提升与迹公式**（188–192）：Brauer 群、约化迹/范数、$\mathcal H$、$T_\phi$、定理 52 (59)；命题 53；定理 54 (60)；Jacquet–Langlands 对应；定理 55；$\mathrm{GO}(4)\leftrightarrow\mathrm{GSp}(2)$。

参考文献 [1]–[53]，印刷 192–196；已按页图逐条重抄（原文 OCR 把 Hecke 印成 Heeke、Fröhlich 印成 Frohlich、$\mathbb R$ 印成 IR 等，均已改正；条目本身的排印错误照录）。

## 三、原书笔误与照录说明（已在译文中照录并出注或在此记录）

1. p.155 摘要下第一段：“spectral theory $f\backslash SL(2,\mathbb R)$”缺字，应为 “of $\Gamma\backslash SL(2,\mathbb R)$”。译文按文义补足。
2. p.168 把 $\pi_s^+$、$\pi_s^-$ 称为“奇、偶主系列”，与 (15) 中 $P_s^+$ 取 $\epsilon=0$ 及同页下文“只有偶主系列 $\pi_s^+$ 含 $K$-不变向量”自相矛盾；应为“偶、奇”。译文照录并出译注。
3. p.169 (21) 印作 $h(t)=\int g(u)e^{iut}dt$，应为 $du$；同页证明又印作 $\int_{\infty}^{\infty}g(u)e^{itu}du$，上下限应为一 $\infty$ 与 $\infty$。译文照录并出校勘注。
4. p.172 证明 (ii) 处 “Since $g$ is even and $g'$ is odd, we have the Fourier inversion formula $g(u)=\frac1\pi\int_0^\infty h(t)e^{-itu}dt$”：右端当作实部理解（$h$ 偶），否则与实值 $g$ 差一虚部。照录。
5. p.176 “in the cricital strip” 拼写错误（critical）。译文作“临界带”，不另出注。
6. p.184 “Recall that $f_{s,k}$ was defined by (15)”——实为 (17)。照录。
7. p.179 末 $Z(s)=\exp\int_\infty^s\frac{Z'(s)}{Z(s)}ds$ 积分变量与被积函数同名，属记号混用。照录。
8. p.189 “Gel bart”、p.191 “Sketchofproof” 等为排版粘连，译文不受影响。
9. p.186 (55) 中 $j$ 从 $0$ 到 $N$，而 (56)(58) 中从 $1$ 到 $N$；原书如此，照录（$j=0$ 对应常数函数）。
10. (36) 证明中第二行出现 $|\log(N_0)|$，是换元后 Jacobi 因子的绝对值；照录。

## 四、疑点清单（未完全解决，共 4 条）

1. **(18) 的归一化常数**：$\tilde f_{k,1-s}=(-i)^k\sqrt\pi\,\frac{\Gamma(s)\Gamma(s-\frac12)}{\Gamma(s+\frac k2)\Gamma(s-\frac k2)}f_{k,1-s}$ 依 Bump [6, Prop. 2.6.3] 照录，未独立验算 $\sqrt\pi$ 与 $(-i)^k$ 的约定（不同文献对 $M(s)$ 的归一化可差一个 $\pi^{s-1/2}\Gamma$ 因子）。
2. **p.172 的 Fourier 反演**：见上第 4 条，按“取实部”理解才能与 $g$ 实值相容；原书未说明。
3. **定理 31 中 $\sum_N$ 的含义**：陈述说 “if $\log(N)$ runs through the lengths of closed geodesics”，求和指标是全部闭测地线长度而非素测地线；与定理 30 的 $N=N(\gamma)$ 一致，但原文措辞易被误读为按素测地线求和。译文按“全部闭测地线”处理。
4. **命题 45 证明中 $\int_{\Gamma\backslash G}\to\int_{\Gamma_\infty\backslash G}$ 的一步**：原文直接换域，实际用到 $f$ 的 $\Gamma$-不变性与展开 $\Gamma_\infty\backslash\Gamma$；这一步在非紧情形需要体积有限，原书未提。译文照译。

## 五、新增/统一术语（本章首次出现者）

| 英文 | 译名 | 备注 |
| --- | --- | --- |
| spectral problem | 谱问题 | 节题 |
| non-Euclidean Laplacian | 非欧 Laplacian | 保留 Laplacian 不译“拉普拉斯算子” |
| fundamental domain | 基本区域 | |
| geodesic arc | 测地弧 | |
| admissible representation | 容许表示 | |
| $K$-finite vector | $K$-有限向量 | |
| spherical Hecke algebra | 球 Hecke 代数 | $\mathcal H^\circ$ |
| spherical function | 球函数 | $\omega_\lambda$、$f_s$ |
| Green's function | Green 函数 | 不译“格林函数” |
| automorphic Green's function | 自守 Green 函数 | $G_s(z,\zeta)$ |
| spectral resolvent / resolvent | 谱预解式／预解式 | $R(s,\Delta)$ |
| exceptional eigenvalue | 例外特征值 | $\lambda\in(0,\frac14)$ |
| principal series (odd/even) | 主系列（奇／偶） | 依 $-I$ 的特征值 |
| complementary series | 补系列 | |
| discrete series | 离散序列 | 全纯离散序列 |
| holomorphic discrete series | 全纯离散序列 | |
| intertwining operator | 缠绕算子 | $M(s)$ |
| Plancherel formula / measure | Plancherel 公式／测度 | |
| trace class | 迹类 | |
| Hilbert–Schmidt | Hilbert–Schmidt | 不译 |
| orbital integral | 轨道积分 | |
| prime geodesic | 素测地线 | $N_0$ |
| closed geodesic | 闭测地线 | $N$ |
| cusp / cusp form | 尖点／尖点形式 | |
| constant term | 常数项 | $f_0$、$E_0$ |
| incomplete theta series | 不完全 theta 级数 | |
| Eisenstein series | Eisenstein 级数 | |
| normalized Eisenstein series | 归一化 Eisenstein 级数 | $E^*$ |
| scattering matrix | 散射矩阵 | $A(s)$、$c(s)$ |
| residual spectrum | 剩余谱 | $\eta_j$ |
| continuous spectrum | 连续谱 | |
| rapid decay | 速降 | |
| Siegel set | Siegel 集 | |
| Weyl's law | Weyl 律 | |
| explicit formula | 显式公式 | Riemann–von Mangoldt |
| Selberg zeta function | Selberg zeta 函数 | $Z(s)$ |
| Brauer group | Brauer 群 | |
| central division algebra | 中心除代数 | 次数 $p^2$ |
| reduced trace / reduced norm | 约化迹／约化范数 | |
| functorial lifting | 函子性提升 | |
| Jacquet–Langlands correspondence | Jacquet–Langlands 对应 | |
| supercuspidal representation | 超尖点表示 | |
| Steinberg representation | Steinberg 表示 | |
| theta correspondence | theta 对应 | $\mathrm{GO}(4)\leftrightarrow\mathrm{GSp}(2)$ |

## 六、译注（13 条）

| # | 位置 | 类型 | 要点 |
| --- | --- | --- | --- |
| 1 | §1 末 | 易错预警 | $\Delta$ 的符号与 $\lambda=s(1-s)$ 参数化；§3 的 $\lambda=-s$ 与后文 $s=\frac12+it$ 非同一条数 |
| 2 | §2 末 | 背景直觉 | 定理 3 即 Satake 同构 $\mathcal H_p^\circ\cong\mathbb C[X_*(T)]^W$ |
| 3 | §3 定理 13 后 | 含糊点拨 | (7) 的两解为 Legendre $P$、$Q$；球函数对应 $P$，Green 函数对应 $Q$ |
| 4 | §3 末 | 背景直觉 | 例外特征值 $\leftrightarrow$ $Z(s)$ 在 $(1/2,1)$ 的零点；Selberg 猜想与 Kim–Sarnak 下界 $975/4096$ |
| 5 | §4 (15) 后 | 易错预警 | 奇偶命名颠倒，按 $-I$ 的特征值 $(-1)^\epsilon$ 理解 |
| 6 | §5 末 | 含糊点拨 | 只涉偶主系列之由；$\int_0^\infty$ 与 $\int_{-\infty}^\infty$ 差因子 2 |
| 7 | §6 末 | 背景直觉 | (37) 两项的几何含义与缺失的椭圆项 |
| 8 | §7 (38) 后 | 背景直觉 | 显式公式各项的来源；$h(\pm i/2)$ 对应 $H^0,H^2$ |
| 9 | §7 末 | 背景直觉 | $Z$ 的零点结构与“RH 无条件成立” |
| 10 | §8 (46) 后 | 背景直觉 | $A(s)=\xi(2s-1)/\xi(2s)$（$\mathrm{SL}(2,\mathbb Z)$）与散射矩阵 |
| 11 | §9 末 | 背景直觉 | (55) 三项 $=$ 剩余谱 $+$ 离散谱 $+$ 连续谱 |
| 12 | §10 末 | 背景直觉 | 定理 55 即 Jacquet–Langlands 对应 |
| 13 | §5 (21) 后 | 校勘 | (21) 的 $dt$ 应为 $du$，上下限印作 $\infty$ |

来源分级：全部为 A 类（原书、经典教材 Hejhal/Iwaniec/Knapp/Whittaker–Watson/Ingham、作者论文 Selberg/Randol/Kim–Sarnak/Satake/Jacquet–Langlands/Gelbart–Jacquet）。

## 七、自测

临时目录 `work/tmp_ch08/build/`，`testmain.tex` 取 `src/main.tex` 的导言区加 `\setcounter{chapter}{7}\input{ch08}`，xelatex 三遍：

- error 0，undefined 0，Overfull 0，Underfull 0，Missing character 0；
- 输出 36 页，`src/chapters/ch08.tex` 2152 行；
- 公式编号 (1)–(60) 各出现一次，定理/命题/引理编号 1–55 与原书一致。
