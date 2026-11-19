# ch01 校订记录（part1：§1、§2.1–§2.6.3，原文印刷 p.1–16）

- 校订对象：`源码/part1_zh.tex`（338 行，改后 55954 字节）
- 对照底本：`原文/Witten_1506.04293v3_EN.pdf`（arXiv:1506.04293v3）、`原文/EN_layout.txt`（pdftotext -layout）、`原文/EN_part1.txt`
- 术语依据：`校对记录/索引术语.tsv`（92 条）、`源码/bibliography.tex`（\cite 键与原文编号）
- 自动检查：`工程文件/tools/check_part.py` 通过（braces/`$`/环境/`%`/UTF-8 均 OK，transnote 计数 15）
- 统计：**P1 0 处（未发现误译/漏译/增译/译反/丢限定词/交叉引用错）、P2 4 处（术语 2、记号 2）、译注 15 条、原文疑误 4 处（照译不改，见下）**

## 一、改动清单

| 序号 | 位置 | 类型 | 原文 | 原译 | 改为 | 依据 |
|---|---|---|---|---|---|---|
| 1 | part1_zh.tex:35 | 术语 | a one-form on C with values in the adjoint representation | 取值于伴随表示的一个**单形式** | 取值于伴随表示的一个 **1-形式** | one-form 在 part2_zh.tex 作「1-形式」4 处、「一形式」5 处，part3_zh.tex 作「1-形式」1 处，part4_zh.tex 作「一形式」1 处，part1 独用「单形式」，属一译多名；且「单」与本文 monodromy 的「单值变换」相混淆 |
| 2 | part1_zh.tex:138 | 术语 | holomorphic one-forms | 由全纯**单形式**组成 | 由全纯 **1-形式**组成 | 同上；同段与前文应统一 |
| 3 | part1_zh.tex:123 | 记号（公式） | half the dimension of $M_H$ | 数目等于 `${\cal M}_H$` 维数的一半 | 数目等于 `$\MH$` 维数的一半 | 全篇（含本行前后、式 (2.3)–(2.35)）一律用宏 `\MH`（preamble 定义的花体 M_H），仅此一处手写 `{\cal M}_H`，破坏记号一致 |
| 4 | part1_zh.tex:164 | 记号（公式） | for a given q ∈ D | 对于给定的 `$q\in D$` | 对于给定的 `$\qq\in D$` | 原文该处用花体 q；同句后半「随着 `$\qq$` 变化」及全篇其余 20 余处均用 `\qq`，此一处为漏改 |

> 说明：第 3、4 条属记号一致性（P2「公式/术语一译多名」的同类），不改语义；已确认不涉及 `\label`/`\ref`/`\cite`。

## 二、原文疑误（照译不改，按施工细则只报告）

| 序号 | 位置 | 类型 | 原文 | 原译 | 改为 | 依据 |
|---|---|---|---|---|---|---|
| 5 | part1_zh.tex:51 | 原文疑误 | where K is the canonical bundle of **E** | 其中 $K$ 是 **$E$** 的典范丛 | 不改（照译） | K 是曲线 C 的典范丛（同句 $H^0(C,K\otimes\ade)$ 只用 C 的 K）；PDF p.6（printed p.5）确印作 E。**数学上应为 of C** |
| 6 | part1_zh.tex:69 | 原文疑误 | the full hyper-Kähler structure of **Σ** | 不会看到 **$\Sigma$** 的完整超凯勒结构 | 不改（照译） | 上下文讲的是 $\MH$ 的超凯勒结构在复结构 I 中的可见部分，且前句主语为 $\MH$；PDF p.8（printed p.7）确印作 Σ。**应为 of $M_H$** |
| 7 | part1_zh.tex:92 | 原文疑误 | $(w_2,w_3,\dots,w_n)$ | `$(w_2,w_3,\dots,w_n)$` | 不改（照译） | 紧接前文定义 $n=2,\dots,N$ 且 ${\cal V}=\oplus_{n=2}^N H^0(C,K^n)$，末项应为 $w_N$；PDF p.9 确印作 $w_n$ |
| 8 | part1_zh.tex:23 | 原文疑误 / 译者补正 | and **now** it produces a pair of topological field theories | 以及它**如何**产生由 $S$-对偶性交换的一对拓扑场论 | 不改（保留译者补正） | 原文 now 与句意不合（疑为 how）；译者按 how 译，语义正确，属对原文笔误的既有处理，不动 |

## 三、已核对范围

- 已核对 §1 引言（L1–9，4 段）：与 EN 逐句对应；面算符/温和分歧/野分歧、$^L\neg G$ 记号、路线图 \ref{compacthitchin}/\ref{dualtori}/\ref{thooftheckeop} 均正确。
- 已核对 §2.1 预备知识（L11–31，8 段）：d 维 QFT 三级层级、2+2=4 论证、拓扑扭曲、$\R^2\times C$ 与 $\Sigma\times C$、$\MH$ 作为 $\sigma$-模型靶空间、$\Y$ 与 $\CW=T^*\Y$、叠与 Atiyah–Bott 模型；两条作者原注（\label{partial}、p.2 关于 $g_C\geq2$ 的注）完整。
- 已核对 §2.2 希钦方程（L33–73，15 段，式 (2.1)–(2.4)）：(2.1)(2.2) 的符号与上下标（$F_{z\bar z}-[\phi_z,\phi_{\bar z}]$、$D_{\bar z}\phi_z=D_z\phi_{\bar z}$、$\F=0$、$D\star\phi=0$、$\F$ 的 Re/Im 分解）逐个核对；两种写法→复结构 I、J；半稳定性原注（\label{semicon}）与 Corlette 定理引用；超凯勒度量 (2.3)、超凯勒商 $\CW///\G$、$\Omega_I$ (2.4)、复辛商与 $\nu_I$、$\Omega_I=\omega_J+i\omega_K$ 与 K 型 A-模型；限定词（only/precisely/generically/not necessarily 等）全部对应。
- 已核对 §2.3 $\MH$ 与余切丛（L75–84，4 段）：稳定/半稳定蕴含方向、$(E,0)$、$T_E\M=H^1$–Serre 对偶–$H^0$、$T^*\M\hookrightarrow\MH$、$\Omega_I$ 限制、$T^*\M$ 像的余维与原注（第 \ref{distinguished} 节）、叶状结构与拉格朗日叶。
- 已核对 §2.4 希钦纤维化（L86–106，5 段，式 (2.5)–(2.6)）：$w=\Tr\varphi^2\in H^0(C,K^2)\cong\C^{3g-3}$、卡西米尔不变量与次数 $d_i$、$\sum_i(2d_i-1)=\dim G$、$\dim H^0(C,K^d)=(2d-1)(g-1)$、$\dim{\cal V}=(g-1)\dim G$、$\dim\FF$ 与满射定性论证（$2^{3g-3}$）。
- 已核对 §2.5 完全可积性（L108–131，10 段，式 (2.7)）：$\frac12\dim\MH$ 个 $H_a$、$H_a=\int\alpha_a\wedge\Tr\varphi^2$、$\CW$ 上泊松括号论证、辛约化、$H_{a,i}=\int\alpha_{a,i}{\cal P}_i(\varphi)$ 与 $\alpha_{a,i}\in H^1(C,K^{1-d_i})$（已按 $K\otimes K^{-d_i}=K^{1-d_i}$ 复核，指标无误）、上同调类无关性、流与纤维化对易、复环面与谱曲线、拉格朗日纤维。
- 已核对 §2.6.1 基本概念（L133–237，24 段，式 (2.8)–(2.22)）：本征值问题（$y\in K|_\pp$）、$\det(y-\varphi)=0$、$N=2$ 化简、谱曲线 $D\to C$ 与 $W$、分支点（$4g_C-4$、亏格 $4g_C-3$ 的欧拉示性数论证）、判别式次数 $N(N-1)$、分歧除子度数 $2N(N-1)(g_C-1)$ 与 $g_D=g_C+(N^2-1)(g_C-1)$、本征线丛 ${\cal N}$、$SU(2)$ 局部模型 (2.11)–(2.14)、核/余核 $\cal L$、$(2.15)$–$(2.20)$ 的 $s=u+2yt$ 验证（$s=(y,1)^T$、$u=(-y,1)^T$、$t=(1,0)^T$ 与 $y^2=z$ 一致）、${\cal L}\cong{\cal N}({\cal R})$ 与 ${\cal L}\cong{\cal N}\otimes\psi^*(K^{N-1})$。
- 已核对 §2.6.2 阿贝尔化（L239–290，13 段，式 (2.23)–(2.29)）：$E_\pp=\oplus_i{\cal N}_{\qq_i}$、${\cal L}$ 版本的分解、推前定义、$E=\psi_*({\cal L})$、局部模型延拓（(2.27)–(2.28) 的 $G=-C,H=D$ 验算成立）、$\varphi=\psi_*(y)$ 及「$(\varphi-y)\chi$ 置零」的等价关系表述（与 EN 逐字对应，无逻辑走样）。
- 已核对 §2.6.3 会出现哪些线丛？（L292–338，11 段，式 (2.30)–(2.35)）：$\psi_*({\cal O})$ 的展开与 ${\cal O}\oplus K^{-1}\oplus\dots\oplus K^{-(N-1)}$、拉回情形、第一陈类 $d=-N(N-1)(g_C-1)$ 与 $c_0=N(N-1)(g_C-1)$（黎曼–罗赫原注完整）、$\mathrm{Pic}_{c_0}(D)$ 与 $\dim=g_D$、$\Lambda({\cal L})=\det\psi_*({\cal L})$、$\FF_{SU(N)}=\Lambda^{-1}({\cal O})$、$\otimes_i{\cal L}_{\qq_i}\cong\C$、$K^{1/2}$ 特选点与奇/偶 $N$ 差别（引 [23]）、末尾指向第 \ref{distinguished} 节。
- 交叉引用核对：`\ref{compacthitchin}`→§2、`prelims`→§2.1、`hitcheq`→§2.2、`hitchfib`→§2.3、`hitchfibr`→§2.4、`complete`→§2.5、`spectral`→§2.6.1、`whichline`→§2.6.3、`distinguished`→part2_zh.tex:84（§2.7）、`dualtori`→part2_zh.tex:166、`topview`→part2_zh.tex:265（§3.3）、`thooftheckeop`→part3_zh.tex:2（§4）、`elmag`→part4_zh.tex:261（§7.1.2）、`\ref{partial}`→L23 原注内 label，全部正确。
- `\cite` 核对：KW/frenkel/GW/Wild/FW/GaiW,GaiW2/WittenKhov/EW1-3/BeD/AB/Corlette/Hitchin/HitchinDuke/DonagiMarkman/donga 共 24 处，键与 bibliography 编号、正文所指文献一致。

## 四、存疑未改

1. **【术语】「单值变换」（monodromy）**：通行译法作「单值表示/单值化」，术语表 `索引术语.tsv` 已定为「单值变换」，正文一致，本轮只把易混的「单形式」改为「1-形式」，未动「单值变换」。
2. **【语气】L162「始终只有一个 Jordan 块」**：原文 "if and only if φ has only one Jordan block for each eigenvalue"，译文「始终」为补出的语气词，语义不变，不属 P1/P2，未改。
3. **【术语】L129「固有性」（properness）**：正文已用引号并括注「纤维的紧致性」，读者可解，未改；若全书统一，可在附录术语表补条。
4. **【记号】L338 附近「二阶平坦线丛」**：指 2-挠率平坦线丛，译法可接受，未改。
5. **【原文疑误 4 处】**（第 5–8 行）：按细则不动译者对原文笔误的既有处理，仅在报告中登记；若 lead 统一出校记，建议在附录 A 逐条出注。
6. **【数学严格性】§2.4 末「$2^{3g-3}$ 个解」**：原文本身是启发式计数（Bézout 式），译文照译无误，已由译注⑩说明其性质，正文未改。
