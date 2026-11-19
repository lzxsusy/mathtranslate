# ch02 校订记录（part2：§2.6.4–§2.7.2、§3 全部，原文印刷 p.17–34）

- 校订对象：`源码/part2_zh.tex`（445 行，改后 13 条 `\transnote{}`）
- 对照底本：`原文/Witten_1506.04293v3_EN.pdf`（arXiv:1506.04293v3）、`原文/EN_part2.txt`（带 `[[PDF p.N | printed p.M]]` 页锚）
- 术语依据：`校对记录/索引术语.tsv`（92 条）、`源码/bibliography.tex`（\cite 键与原文编号）
- 自动检查：`python 工程文件/tools/check_part.py 源码/part2_zh.tex` → **OK**（braces/`$`/环境/`%`/UTF-8 均通过，transnote 计数 13）
- 统计：**P1 1 处（漏限定词）、P2 1 处（专名）+ P2 1 处（术语统一，5 行）、译注 13 条、原文疑误 8 处（照译不改，见第三节）**

> 页码说明：`EN_part2.txt` 的页锚 `[[PDF p.N | printed p.M]]` 用 0 起的 PDF 页号，**实际 PDF 页 = printed M + 2**；下文核对均按 printed 页号 +2 取页。

## 一、改动清单

| 序号 | 位置 | 类型 | 原文 | 原译 | 改为 | 依据 |
|---|---|---|---|---|---|---|
| 1 | part2_zh.tex:3 | 漏译（限定词）·P1 | this answer … has a nice interpretation, **which was essentially described in section 4.3 of [5]** | 文献 [5] 第 4.3 节**实际上**已经描述了这一解释 | 文献 [5] 第 4.3 节**实质上**已经描述了这一解释 | essentially 表“本质上/大体上”，与“实际上（in fact）”不同；原译丢失该限定词，读者会误以为 [5] §4.3 已完整给出此解释。原文 §2.6.4 首段；printed p.17 |
| 2 | part2_zh.tex:54 | 专名 ·P2 | For $N=2$, $\xi$ is the second **Stieffel-Whitney** class $w_2(E)$ | 第二 **Stieffel-Whitney** 类 | 第二 **Stiefel–Whitney** 类 | 标准名称为 Stiefel–Whitney；原文此处拼作 Stieffel 属 Witten 笔误（[KW] §7.1 同误拼），中文译文按标准名称改正并在此登记。原文 §2.6.6；printed p.18 |
| 3 | part2_zh.tex:352/359/369/386/389 | 术语（一译多名）·P2 | holomorphic one-forms；a one-form $\omega^a$ | 全纯**一形式**（3 处）、**一形式** $\omega^a$（2 处） | 全纯 **1-形式**；**1-形式** $\omega^a$（共 5 处） | 本文件原已 4 处作「1-形式」，5 处作「一形式」，前后不一；`索引术语.tsv` 与 part1 校订（ch01 改动清单第 1–2 条）均定「1-形式」。已全篇统一，现 `一形式` 0 处、`1-形式` 9 处 |

> 第 3 条只动术语写法，不涉语义、`\label`、`\ref`、`\cite`、公式。

## 二、译注清单（13 条，均实查来源；A 级为主，B 级标“待核”）

| 序号 | 位置 | 主题与增量 | 来源 |
|---|---|---|---|
| ① | L7（§2.6.4） | D-膜 K 理论 ⇒ 陈-帕顿丛须与法丛旋量丛张量，$W=T^*C$ 的法丛为 $K$，故 $\U^2\cong K$；$w_2(C)\neq0$ 时无整体平方根，只能平坦 $\mathrm{Spin}_c$，次数 $g_C-1$ | A：Witten, *D-Branes And K-Theory*, arXiv:hep-th/9810188 §4.3（判据 $c_1(L)\equiv w_2(N)\bmod 2$）；原文 §2.6.4、式 (2.33) |
| ② | L26（§2.6.5） | “典范阿贝尔簇”=有不依赖选择的零点；奇 $N$ 时 $\psi^*(K^{(N-1)/2})$ 直接存在，偶 $N$ 须先取 $K^{1/2}$，除以 $\Gamma_N$ 恰消去该依赖 | A：原文 §2.6.3、§2.6.5 式 (2.36)–(2.38)；Frenkel–Witten, arXiv:0710.5939 §10 |
| ③ | L54（§2.6.6） | 't Hooft 磁通：$C$ 二维 ⇒ 分类只看 $\pi_1(PSU(N))=\Bbb Z_N$，$H^2(C,\Bbb Z_N)\cong\Bbb Z_N$；$N=2$ 时 $\xi=w_2$；$U(N)$ 提升时 $\xi\equiv c_1\bmod N$ | A：[KW]（arXiv:hep-th/0604151）§7.1；原文 §2.6.6 |
| ④ | L73（§2.6.6） | 非平凡 gerbe=离散 $B$-场：$U(1)$-gerbe 由 $H^2(X,U(1))$ 分类，其上向量丛“扭曲”存在（$v_{ki}v_{jk}v_{ij}=b_{ijk}$） | A：[KW] §7.2；B：nLab “gerbe”（Last revised 2026-02-14，2026-11-19 访问，待核）；原文 §2.6.6/§3.2 |
| ⑤ | L81（§2.6.7） | 一般 $G$ 用 cameral 覆盖（$|W|$ 重，正则纤维 = Cartan），谱覆盖 = cameral 覆盖与小表示的纤维积 | A：Donagi–Gaitsgory, arXiv:math/0005132 §2、§9；原文 §2.6.7 |
| ⑥ | L112（§2.7.1） | 特选截面 = 不稳定丛 $E=K^{1/2}\oplus K^{-1/2}$ 给出的标准点（$w\neq0$ 时稳定）；一般稳定 $E$ 交点 $2^{3g-3}$，故“唯一”只在退化处成立 | A：Hitchin, Proc. LMS (3) 55 (1987) 59–126；原文 §2.7.1、§2.6.3 |
| ⑦ | L153（§2.7.2） | oper 的义项（带横截/正则联络的 $G$-丛，$\mathrm{PSL}(2)$ 情形 = 射影结构）；oper 模空间即希钦截面的来源，故只“几乎”典范（依赖 $K^{1/2}$） | A：Beilinson–Drinfeld, *Quantization Of Hitchin's Integrable System And Hecke Eigensheaves*（原文 §2.7.2 所引 [12]） |
| ⑧ | L176（§3） | 唯一特选点 ⇒ 标准主极化，$\cF'\cong\mathrm{Pic}^0(\cF)$；格 = 电荷格/磁荷格，即 GNO 对偶的几何形式 | A：Goddard–Nuyts–Olive, Nucl. Phys. B125 (1977) 1–28；原文 §3 |
| ⑨ | L217（§3.1） | CS 作用量 $I=(1/2\pi)\int A\wedge dB$ 变分给出边界辛形式；$1/2\pi$ 使周期 $\in2\pi\Bbb Z$，故预量子化线丛 $\cal T$ 存在唯一 | A：Ramadas–Singer–Weitsman, Commun. Math. Phys. 126 (1989) 409；原文 §3.1 式 (3.1)–(3.3) |
| ⑩ | L288（§3.3） | 两个 $\psi^*$ 同名异义：(3.15) 为闭链提升 $H_1(C)\to H_1(D)$（$\psi_*\psi^*=N$），线丛情形为拉回 $\mathrm{Pic}(C)\to\mathrm{Pic}(D)$ | A：原文 §3.3 式 (3.15)(3.16)、§2.6.6 式 (2.36)–(2.39) |
| ⑪ | L316（§3.3） | $\FF=\mathrm{Hom}(\Gamma^*,U(1))$，$\Gamma^*$ 无挠 ⇒ 紧环面 ⇒ 连通；无挠来自 $\psi_*$ 满射（$\psi^*H_1(C)$ 为饱和子格），与 §2.6.3 复几何预言互证 | A：原文 §3.3 式 (3.19)–(3.23)；Hausel–Thaddeus, arXiv:math/0205236 |
| ⑫ | L397（§3.4） | $\psi_*$ 为迹映射：满射、核维数 $g_D-g_C$；$\Tr\varphi=0$ ⇒ $\lambda=y\,dz\in\ker$，故 $\partial\lambda/\partial H_a$ 给出核的一组基 | A：原文 §3.4 式 (3.32)(3.33)；Hitchin, Duke Math. J. 54 (1987) 91–114 |
| ⑬ | L444（§3.4.1） | 归一化链条：$|d^2z|=i\,dz\wedge d\bar z$、$\int\delta=1$、$\partial_{r_i}=-\partial_z$ 给出 (3.38) 的 $-i\pi$ 与 (3.39)；并判定原文脚注「曲率 $f=da$」中 $f$ 是标量函数，$da=2\bar\partial\partial f=2\pi i\sum n_i\delta$，与 (3.38) 差因子 2 并不矛盾 | A：原文 §3.4.1 式 (3.37)–(3.39) 及脚注；2026-11-19 核对 |

## 三、原文疑误（照译不改，按施工细则只报告）

| 序号 | 位置 | 类型 | 原文 | 原译 | 改为 | 依据 |
|---|---|---|---|---|---|---|
| 4 | part2_zh.tex:50–51 | 原文疑误（括号） | `ψ_*(ℒ⊗ψ^*𝒮)) = ψ_*(ℒ)⊗𝒮`（ψ* 后无左括号、末尾多一右括号） | 照译 | 不改 | printed p.18 / PDF 20 目视核对，原文确如此（pdf 文本层亦作 `ψ∗(L ⊗ ψ∗S))`）；属公式符号，细则禁改 |
| 5 | part2_zh.tex:52 | 原文疑误（漏 $\det$） | `det(ψ_*(ℒ⊗ψ^*(𝒮))) = ψ_*(ℒ)⊗𝒮^N` | 照译 | 不改 | 数学上应为 $\det\psi_*(\cal L)\otimes\cal S^N$（左边是线丛、右边秩 $N$）；printed p.18 原文即漏右边 $\det$ |
| 6 | part2_zh.tex:234 | 原文疑误（$\zeta^*$ 应为 $\psi^*$） | $\cal L'=\cal L\otimes\zeta^*(K^{-(N-1)/2})$ | 照译 | 不改 | printed p.26 / PDF 28 原文确作 $\zeta^*$；同段上一行为 $\psi^*(K^{(N-1)/2})$，典范点由 $\psi$ 拉回给出，故 $\zeta$ 应为 $\psi$ |
| 7 | part2_zh.tex:338 | 原文疑误（笔误） | let $p_i$, $i-1,\dots,k$ | 设 $p_i$、$i-1,\dots,k$ | 不改 | printed p.29 / PDF 31 原文确作 $i-1$，应为 $i=1,\dots,k$ |
| 8 | part2_zh.tex:399 | 原文疑误（措辞） | we remove **$N$** commuting Hamiltonians by setting $\Tr\varphi=0$ | 去掉 **$N$** 个对易哈密顿量 | 不改 | printed p.32 / PDF 34 原文确作 $N$；但 $\Tr\varphi=0$ 只是一个方程，$SU(N)$ 相对 $U(N)$ 只去掉 1 个哈密顿量（$g_C$ 个差来自别处），原文措辞可疑 |
| 9 | part2_zh.tex:410 | 原文疑误（自相矛盾） | Shifting $\gamma$ by any other element of $\Gamma$ would destroy … | 用 $\Gamma$ 的任何其他元素平移 $\gamma$，则会破坏…… | 不改 | printed p.33 / PDF 35 原文如此；与上句“用 $\Gamma$ 的元素平移不改变……”直接矛盾，疑 any other element 应为 any element outside $\Gamma$ 之类 |
| 10 | part2_zh.tex:437 | 原文疑误（脚注记号） | curvature **$f=da=2\pi i\sum n_i\delta_{r_i}$** | 具有曲率 **$f=da=2\pi i\sum n_i\delta_{r_i}$** | 不改（原脚注保留） | printed p.34 / PDF 36 原文如此；$f$ 是标量函数，曲率应为 $da=2\bar\partial\partial f=2\pi i\sum n_i\delta$（见译注⑬） |
| 11 | part2_zh.tex:66 | 原文混用（记号） | the action of $J(C)$（其余处写 $\mathrm{Jac}(C)$） | 通过 $J(C)$ 的作用 | 不改 | 原文英文亦在 $J(C)$ 与 $\mathrm{Jac}(C)$ 间混用，中文照译；不属误译 |

## 四、已核对范围

- 已核对 §2.6.4 与 K 理论的关系（L1–14，6 段）：$W=T^*C$ 的实辛结构、A-模型/拉格朗日子流形、秩 1 与秩 $N$ 陈-帕顿丛、法丛平方根、次数 $c_0'=c_0+N(g_C-1)=g_D-1$、式 (2.33) 与第 4.3 节出处；限定词 essentially 已改。
- 已核对 §2.6.5 酉群（L15–30，6 段）：$\Tr\varphi$ 与 $(g_C-1)N^2+1$、$\mathrm{Pic}_{c_0+m}(D)$、$c=0$ 分支、式 (2.36)(2.37)、奇/偶 $N$ 与自旋结构、第 \ref{elmag} 节交叉引用。
- 已核对 §2.6.6 群 $PSU(N)$（L31–74，12 段）：$\Gamma_N$、式 (2.38)(2.39)(2.40)(2.41)(2.42)、$\xi\in H^2(C,\Bbb Z_N)$、't Hooft 磁通、$ad(E)$ 与 $U(N)$ 提升、万有覆盖与不除 $\Gamma_N$、与 $\MH(SU(N))$ 的 $S$-对偶、gerbe 与 \ref{gerbes}/\ref{dualap}、[KW] §7、[dongai]。
- 已核对 §2.6.7 其他规范群的谱覆盖（L75–82，3 段）：小表示与 $SO(N),Sp(N),G_2$、$E_8$ 的抽象方法、cameral 覆盖（译注⑤）。
- 已核对 §2.7 引子与 §2.7.1 $SU(N)$ 情形（L83–147，14 段）：$E=K^{1/2}\oplus K^{-1/2}$ 不稳定、$SL(2,\Bbb C)$ 自同构、$\varphi$ 的矩阵形式、$u\neq0$ 稳定、式 (2.46) $\zeta:V\to\MH$、交点 $2^{3g-3}$、$y^2=w/2$、${\cal N}=\psi^*(K^{-1/2})$、${\cal L}=\psi^*(K^{1/2})$、$SU(N)$ 的 $E=\oplus K^{(N-1)/2-\dots}$、$w_n\in H^0(C,K^n)$、$\Tr\varphi^n=w_n$（已用 $N=3$ 验算）。
- 已核对 §2.7.2 任意 $G$ 的截面（L148–164，7 段）：Kostant 主 $SU(2)$ 嵌入、opers（\cite{BeD}，译注⑦）、几乎典范性、$SU(2)/PSU(2)=SO(3)$、奇偶 $N$、$G=SU(N)/\Gamma$ 条件、伴随型 $G$ 的像为 $SO(3)$、$E_8$ 的典范阿贝尔簇纤维、\ref{whichline}。
- 已核对 §3 引子（L165–179，7 段）：$S$-对偶 = $T$-对偶 + 底空间几何对称（原脚注：酉群时只是缩放）、SYZ、超凯勒、对偶复环面定义（Poincaré 线丛 ${\cal T}\to\F\times\F'$、唯一特选点、主极化、典范阿贝尔簇，译注⑧）。
- 已核对 §3.1 例子（L180–220，14 段）：$S\times S'$ 的 $\omega=dx\wedge dy/2\pi$、$B=-ix\,dy/2\pi$、和乐 $e^{ix},e^{iy}$、对偶格 $\Gamma,\Gamma^*$、$J$ 自对偶、式 (3.1)(3.2)(3.3)、CS 作用量与预量子化（译注⑨）、$\cite{rsw,axelrod}$、\ref{ugduality}。
- 已核对 §3.2 酉群的情形（L221–263，20 段）：$\MH(PSU(N))$ 的 $N$ 个分支、$\xi$ 对偶为离散 $B$-场、偶 $N$ 的 $K^{1/2}$、式 (3.4)–(3.10)、范映射 $\mathrm{Nm}$ 与 $\det\psi_*$ 差 $K^{-N(N-1)/2}$、$\FF_{SU(N)}=\mathrm{Nm}^{-1}({\cal O})$、$F^\perp=\psi^*\mathrm{Jac}(C)$、Hausel–Thaddeus 初等证明、\ref{gerbes}/\ref{topview}/\ref{dualap}。
- 已核对 §3.3 拓扑观点（L264–329，18 段）：$\psi_*$ 满射（$y^N-z$ 局部模型）、式 (3.11)–(3.25)、正合列、分裂、$\psi_*=0\oplus1$、$\psi_*\psi^*=N$、对偶正合列、$\Gamma^*=H_1(D)/\psi^*H_1(C)$、$\FF^{(0)}=\mathrm{Hom}(\Gamma,U(1))$、$\Gamma\subset\Gamma^*$、判别式证同构、连通性与环面（译注⑩⑪）。
- 已核对 §3.3.1 $\FF_{SU(N)}$ 的刻画（L330–344，5 段）：$\mathrm{Nm}^{-1}({\cal O})$ 的除子生成、式 (3.26)、用可除 $N$ 的逆命题。
- 已核对 §3.4 辛形式（L345–424，20 段）：Abel–Jacobi 映射、$\lambda=y\,dz$、$P(y,z;H_a)=0$、$\omega^a=\partial\lambda/\partial H_a$、式 (3.27)–(3.33)、链无关性、$d\qq_i$ 的含义、$dX\wedge dH$、1 次齐次、$SU(N)$ 的 $\tilde\omega^a$ 与 $\psi_*\tilde\omega^a=0$、$g_D-g_C$（译注⑫）。
- 已核对 §3.4.1 与规范理论的比较（L425–445，8 段）：式 (3.34)–(3.39)、$a_{\bar z}=\partial_{\bar z}f$、$\bar\partial\partial f=i\pi\sum n_i\delta$、$f\sim\tfrac12\ln|z-r_i|^2$、脚注、$|d^2z|=i\,dz\wedge d\bar z$、与 (3.31) 一致（译注⑬）。
- 交叉引用核对：`\ref{hitchfibr}`→§2.4、`whichline`→§2.6.3、`gerbes`→§6.3、`ugduality`→§6.4、`dualap`→§6.5、`topview`→§3.3、`character`→§3.3.1、`compgauge`→§3.4.1、`elmag`→§7.1.2、`zolk`→(2.4)、`jofo`→(2.31)、`xofo`→(2.32)、`ywo`→(2.33)、`yudo`→(2.34)、`olpp`→(3.1)、`ivo`→(3.2)、`ploko`→(3.3)、`t_*`→(3.4)–(3.39) 全表逐一核对，**无错误**。
- `\cite` 与公式编号：全部 `\label`—`\eqref`/`\ref` 对应经 `main.aux`/源文件双向核对，与原文编号一致；未改任何 `\label`、`\ref`、`\cite`。

## 五、存疑未改

1. **术语「$\FF$ / 纤维」**：§2.6.4–2.7 用「纤维」指希钦纤维化的纤维，§3 亦同；未改。
2. **「希格斯丛」与「希钦对」并用**：§2.7.2 以下多处「希钦对 $(E,\varphi)$」与「希格斯丛 $(E,\varphi)$」交替出现，原文 same object 两种称呼（Hitchin pair / Higgs bundle），中文随原文，未统一（若全书统一，可在附录术语表说明二者同义）。
3. **「皮卡群」/「Picard 群」**：正文一律作「皮卡群 ${\rm Pic}$」，符术语表，未改。
4. **$J(C)$ vs $\mathrm{Jac}(C)$**（tex:66）：原文英文即混用，中文照译，仅记第三节第 11 条。
5. **`\index{}` 词条未动**：新增译注不引入新索引项，避免与 part1/part3 索引重复。
6. **原文疑误 8 处**（第三节 4–11 条）：均按细则「公式符号/原文笔误只登记、不改译文」处理；若 lead 统一出校记，建议在附录 A 按 printed 页号（p.18/26/29/32/33/34）逐条出注。
