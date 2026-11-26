# 第 24 篇 · Hitchin 模空间的量子化、Liouville 理论与几何朗兰兹对应 I

- 作者：J. Teschner（DESY）　arXiv:1005.2846v5（2012-03-06，final ATMP）　83 页
- 底本：`pdf/24_I_1005.2846.pdf`；分页文本 `txt/24/p001.txt`–`p083.txt`
- 卡片：概念 10 张、推导 3 张（`cards/concepts/`、`cards/derivations/`）

## 0. 页码约定

PDF 页序 = 印刷页序，p001 是标题页，p079–p083 是参考文献。本文所有 `p.N` 都指 PDF 第 N 页；
卡片 `sources.pages` 用同一套编号，`anchor` 形如 `A p.38 eq (5.34)`。

## 1. 一句话

Hitchin 可积系统的量子化与 Liouville 理论是同一件事的两个图像：Liouville 的共形块在
$\epsilon_2\to0$ 时给出 Hitchin Hamiltonians 的本征函数（Yang 势），在 $b\to\infty$（临界层
$k\to-2$）时退化为 opers 与 local systems；而 Liouville 的 $b\leftrightarrow1/b$ 自对偶把这两个
极限串成 WZNW$_{\check k}\leftarrow$Liouv$_b\to$WZNW$_k$ 的三角，其共形块关系就是量子几何
Langlands 对应。

## 2. 文章骨架

| 节 | 页 | 一句话 |
|---|---|---|
| 1 Introduction | 1–7 | 四维 $\mathcal N=2$ 的低能有效作用量 ↔ 可积系统；两张图 (1.1)(1.3) 把量子化、hyperkähler 旋转、Liouville、WZNW 串起来 |
| 2 Classical Hitchin system | 7–11 | 自对偶方程 (2.1)、Hitchin 纤维化、谱曲线、分离变量、action-angle 变量 |
| 3 Isomonodromic deformations | 11–22 | Hitchin 模空间 = 平坦联络模空间；opers、Schlesinger/Garnier、实切片、Teichmüller 分量、$\zeta\to0$ 极限 |
| 4 Quantization | 22–29 | 量子化三方案（a/b/c′）；Baxter 方程；半经典与复量子化；单值性推出 SU(1,1) |
| 5 Liouville theory | 29–43 | 共形块与粘接；退化场与 BPZ；半经典极限 = Yang 势；重源；$b\to0$ 极限回到等单值 |
| 6 Liouville as quantum local systems | 43–53 | Fock–Goncharov 坐标、长度算子、Kähler 量子化、$\mathrm{Hom}(\pi_1,\mathrm{PSL}(2,\mathbb R))$ 的正则量子化 |
| 7 GLC and CFT | 53–58 | BD 量子化回顾；WZNW 共形块与 Hecke；临界层的共形块 = opers 上的 D-模 |
| 8 Quantum GLC | 59–75 | KZ；$g=0$ 的 Θ 扭转构造；modular duality；退化场 = 量子 Hecke；量子局部系统；高秩与推广 |
| 9 Concluding remarks | 75–78 | 与 AGT/规范论的关系；高秩 Toda 与 $\mathcal W$-代数；两张图的对偶 |

## 3. 主命题清单

| 编号 | 位置 | 命题 |
|---|---|---|
| S1 | p.5 eq (1.4) | 局部几何 Langlands：$\widehat{\mathfrak g}$-local systems ↔ $\mathrm{Bun}_G$ 上的 D-模 |
| S2 | p.6 eq (1.7)–(1.9) | WZNW$_{\check k}\leftarrow$Liouv$_b\to$WZNW$_k$ 三角，$\check k+2=(k+2)^{-1}=-b^2$，称 quantum GLC |
| S3 | p.9 eq (2.6)–(2.8) | 谱曲线 $\Sigma$ 与 SOV 辛同构 $T^*M_H\to(T^*C)^{[d]}$，$d=3g-3+n$ |
| S4 | p.14–15 eq (3.10)–(3.18) | $\mathrm{Op}_{sl_2}(C_{g,n})$ 复维 $3g-3+n$，是 $T^*T(C)$；单值映射局部双全纯且保辛 |
| S5 | p.16–17 eq (3.21)–(3.26) | 等单值形变 = Schlesinger 方程；$d=n-3$ 时化为 Garnier 系统，$(\kappa,w)$ 是 Darboux 坐标 |
| S6 | p.19 eq (3.33)–(3.34) | $d=0$ 实切片 = Teichmüller 分量；常负曲率度量的能量-动量张量给 $t(y)=-(\partial_z\phi)^2+\partial_z^2\phi$ |
| S7 | p.25 eq (4.5)–(4.6) | 复量子化的单值性 ⇒ $K=\mathrm{diag}(1,-1)$ 与 $\mathrm{Re}(a_r)=\pi\epsilon n_r$ |
| S8 | p.28–29 eq (4.18)–(4.22) | 分离变量：$M_r^\dagger KM_r=K$ 的充要条件是表示共轭进 $\mathrm{SU}(1,1)$；唯一给出态 $\lvert q\rangle$ |
| S9 | p.37–40 eq (5.29)–(5.42) | 半经典共形块 $=e^{-b^2W}\prod\chi_k$；$H_r=-\partial_{z_r}W$；实/复量子化条件差因子 2 |
| S10 | p.49 eq (6.19)–(6.20) | Kähler 量子化波函数 = Liouville 共形块 $\Psi^\sigma_l(q)=F^\sigma_q(p)$，$p_\gamma=l_\gamma/(4\pi\epsilon_1)$ |
| S11 | p.56–57 eq (7.13)–(7.15) | 临界层共形块非零 ⟺ $t_r(y)$ 是全局 oper 的 Laurent 展开；$\mathrm{Op}_{^L\mathfrak g}\to\widehat{\mathfrak g}_{\mathrm{crit}}$ 共形块 |
| S12 | p.62 eq (8.5)–(8.8) | $\tilde G=u\delta(\sum\mu)\Theta_n(y\lvert z)F$ 把 BPZ 解变成 KZ 解 |
| S13 | p.70–71 eq (8.43) | 量子单值 $M_\gamma$ 的本征值 ↔ 共形块的基；临界层退化为 (7.1) |
| S14 | p.73–75 eq (8.50)–(8.60) | 推广：$\Phi^+_{(2,2)}$ 插入给重源 $e^{-b\varphi}$，$H_s,E_s$ 与 $\kappa_r$ 对偶；$W=$ 半经典块 |

## 4. 与库内已译文献的接口

| 库内篇 | 接口点 | 差别 |
|---|---|---|
| 01（kw06，电磁对偶与 GLC，67 卡） | 同一个几何 Langlands 对应；`canonical coisotropic brane`、特征膜的 brane 词典 | kw06 从拓扑扭化 $A/B$-膜出发，本文从共形块与 opers 出发，全文无 brane 语言；本文多了 $b\leftrightarrow1/b$ 的 CFT 机制 |
| 02（规范理论、分歧与 GLC） | 分歧在 GLC 中的位置（本文 §2.1 的正则奇点、§4.2 的抛物结构） | 本文只处理 tame 情形（正则奇点），野分歧完全未涉及 |
| 06（镜像对称、Hitchin 方程与 Langlands） | Hitchin 模空间的 A/B-膜与 Langlands 对偶 | 本文用 SOV/谱曲线/opers，不走镜像对称；结论是同一模空间的另一套坐标 |
| 11（量子力学路径积分的新视角） | 量子化的第三种方案 c′：不构造标量积，改用 Yang 势的临界点 | 本文没有路径积分测度，只有半经典块与量子化条件；与 11 的「定义」路线互补 |
| 16（几何内窥与镜像对称） | Langlands 对偶群 $^LG$（本文只 $\mathrm{SL}(2)$，对偶群 $=\mathrm{PSL}(2)$） | 内窥（endoscopy）在本文完全未出现；本文的「对偶」是水平 $k\leftrightarrow\check k$ |
| 23（四维规范场论中的纽结不变量） | 四维 $\mathcal N=4$ 与几何 Langlands 的物理起源；'t Hooft 算子 | 本文从二维 CFT 出发，四维只作为动机（§1、§5.5.7 的 [NS]/[AGT]） |
| 28（bdh，Hitchin 量子化与 Hecke 特征层） | BD 量子化、D-模、Hecke 特征层 | bdh 给几何构造（中心、水平性），本文给 $g=0$ 的显式解（共形块、Θ 扭转）；本文 §7.1 引 [BD] 的 $3g-3$ 个算子 |
| 36（朗兰兹纲领与共形场论讲义） | 整体图景与术语定名（local system、oper、Hecke 特征层） | 36 是综述性图景，本文是可计算的 $g=0$ 版本 |

## 5. 记号核对

| 符号 | 本文用法 | 易混处 |
|---|---|---|
| $\epsilon_1,\epsilon_2$ | $\epsilon_1=\hbar b$、$\epsilon_2=\hbar/b$（(1.2)） | 与 Nekrasov 的 $\epsilon_{1,2}$ 同号；极限 $\epsilon_2\to0$ 对应 $b\to\infty$ |
| $k,\check k$ | $k$ 是 $\widehat{\mathfrak{sl}}_2$ 水平；$\check k+2=(k+2)^{-1}=-b^2$（(1.8)） | 临界层是 $k\to-2$，此时 $\check k\to\infty$；不要写成两者同时临界 |
| $l_r$ | opers 坐标；$l_r=p_r/(4\pi\epsilon_1)$（(5.33)）；与 SW 的 $a$ 由 $l_r=(4\pi/\epsilon)a_r$（(3.44)）联系 | $l$、$a$、$p$ 三个变量都出现在 §5.5，混用会差 $4\pi$ |
| $\delta_r,\Delta_r$ | $\Delta_r=\alpha_r(Q-\alpha_r)$；$\delta_r=\lim b^{-2}\Delta_r$（(5.30)）；Gaudin 侧 $t\sim-j(j+1)/(y-z)^2$ | 比较 (4.18) 与 (3.15) 得 $j(j+1)=-\Delta$，符号别丢 |
| $H_r$ | §2/§3 是 Hitchin Hamiltonians/accessory parameters；§4 是 Gaudin Hamiltonians；§5 是 $-\partial_{z_r}W$ | 三个用法在 $d=0$ 时一致，但 §4 的是算子、§2 的是函数 |
| $q$ | §5 的粘接参数 $q=(q_1,\dots,q_{3g-3+n})$；§3.5 的 $q_r$ 是 $T(C)$ 的 Fenchel–Nielsen 坐标 | 同一个字母两套含义，读 (3.18) 与 (5.17) 时要看清上下文 |
| $W$ 与 $S_L$ | $S_L(q)=2\mathrm{Re}(W^\sigma_q(l_s))$（(5.35)） | $W$ 只定义到 $q$-无关函数；$S_L$ 是经典作用 |
| $w_r,\kappa_r$ | apparent singularity 的位置与残数（(3.15)）；重源插入时 $w_r$ 是 $e^{-b\varphi}$ 的位置（(5.43)） | 两种 $w_r$ 用法不同，见 (8.58) 的订正（errata E3） |

## 6. 外部校正五项动作清单

| # | 核什么 | 怎么核 | 结论 |
|---|---|---|---|
| 1 | 主定理陈述与符号 | 摘要 + v1 全文 + 库内 17/25 号卡 + Kapustin 0811.3264 | (1.4)(1.9) 的陈述与 v1 一致；(1.8) 的 $\check k+2=(k+2)^{-1}=-b^2$ 与 §8.4 的 (8.14) 自洽 |
| 2 | 关键公式系数/符号 | 本篇 + v1 §4.6 + Nekrasov–Shatashvili 0908.4052 (2.17)(2.18) + Teschner hep-th/0104158 | (5.38) 的 $\pi\epsilon k$ 与 (5.41) 的 $2\pi\epsilon k$ 分别对应 v1 (4.28) 与 (4.26)，一致；Y 角/融合规则 (5.47) 有笔误（E1） |
| 3 | 命题编号交叉引用 | 正文中引用 (3.15)(5.51)(8.58) 处逐一回查 | (3.41) 的 $\delta_{r,s}$（E2）与 (8.58) 的 $z_r$（E3）是编号/指标错位 |
| 4 | 数值/维数一致性 | $\dim M_H=6g-6+2n$、$\dim\mathrm{Op}=3g-3+n$、$\dim\{\vartheta\mid\mathrm{div}\vartheta\ge D\}=3g-3+n-d$ | 三处自洽：$M_H$ 是 $d$ 维底上的 $d$ 维环面纤维化；$d=0$ 时 $\mathrm{Op}=T^*T(C)$ 与 $T(C)$ 同维 |
| 5 | 记号与前后定义 | §1 与 §5、§8 对照；v1（§4.6）与 v5（§5.5）的编号位移 | §5.5 把 v1 的 §4.6 扩写；$W$ 的 $q$-无关函数修正是 v5 新增（脚注 4 明说更正旧版） |

## 7. 我不懂 / 未验算的地方

1. §1 图 (1.1) 的箭头 (D)「$\epsilon_2$ = quantum hyperkähler rotation」只有一句话解释（p.3），
   我没有把它与 §8.4 的 modular duality 计算逐项对上。
2. §4.1 的方案 a/b/c′ 中，c′ 与 a/b 的等价性（即 Yang 势临界点为什么等于量子化谱）原文只有
   [NS] 的引用与 Toda 链的类比，没有一般证明；我在卡片里记成 B。
3. §5.4 的完备性（(5.28) 是 (5.24) 的完备解）原文脚注 3 自认文献中无完整证明，只能拼
   $g=0,n=4$ 与 $g=1,n=1$ 两块。
4. §6.5 的长度表示与 §6.7 的 Riemann–Hilbert 问题：我接受「共形块是唯一解」，但没有独立验算
   $q_\gamma H_\gamma\sim(l_\gamma/4\pi)^2-1/4$ 的渐近。
5. §8.5.8 的量子 Drinfeld–Sokolov reduction 我只读了结论（插 $\tilde\Phi_{k/2}(0|w)$ 等价于施加
   $J^-(w)=0$、减少一个 $e^{-(1/b)\varphi}$），没有验证 (8.46) 的 OPE 系数。
6. 高秩推广（§9.2 的 (9.1)–(9.3)）我完全没有验算，只按原文抄了关系式。
7. 本库缺少 01/02/06/11/16/23/28/36 的包正文（只有 MANIFEST 里的工程名），所以 §4 的接口表
   是按 XREF 的题名与既有卡内容写的概念性对接，没有逐句核对那 8 篇的原文。

## 8. 核对与勘误

### 外部来源

| 来源 | 定位 | 核了什么 |
|---|---|---|
| arXiv:1005.2846v1（本包 `external/v1.txt`） | §4.6 eq (4.23)–(4.28) | v1 的 Yang 势四条量子化条件与 v5 (5.38)(5.41)(5.42) 对应；v1 (4.24) 无 $q$-无关函数修正，正是 v5 脚注 4 说更正之处；(5.47) 的笔误在 v1 同样存在 |
| Nekrasov–Shatashvili, arXiv:0908.4052（`external/0908.4052.txt`） | (2.17)(2.18)、§6 | Yang 势 $W(a;\epsilon)$ 的定义与 $\partial W/\partial a_i=2\pi i n_i$、$E_k=\partial W/\partial t_k$；支撑 (5.41) 的 $2\pi\epsilon k$ 形式 |
| Kapustin, arXiv:0811.3264（`external/0811.3264.txt`） | §2–§3 | 量子几何 Langlands 的量子化描述（平联络模空间的量子化、$q=-i\,\mathrm{Im}\,\tau\propto1/\hbar$）；支撑本文 (1.9) 的「quantum GLC」用法 |
| Teschner, hep-th/0104158（`external/t01.txt`） | §4 eq (73)–(74)、§6 Thm 1 | 零点解耦与退化融合通道 $\alpha\to\alpha\pm\alpha_{m,n}$、$2\alpha_{m,n}=-mb-nb^{-1}$；用于判 (5.47) 的笔误（E1）与 (5.25) 的 $\pm$ 通道 |
| 库内 25 号包（ggl25）卡 `quantum-teichmuller-liouville-dictionary` | p.16 eq (5.33) | 该卡记 $p_\gamma=l_\gamma/(4\pi b)$，与本文 (6.20) 的 $p_\gamma=l_\gamma/(4\pi\epsilon_1)$ 在 $\epsilon_1=\hbar b$、$\hbar=1$ 时一致 |
| 库内 17 号包（ggl17）卡 `hecke-eigensheaf-correlators` | p.108 §7.1 | 「$\dim G(C)(g-1)$ 个全纯微分算子」与本文 §7.1 的 $3g-3$（$G=\mathrm{SL}(2)$ 时 $3g-3$）一致 |

### 勘误

- **E1（medium，fixed）** p.42 (5.47)：$[V_{-b/2}]\cdot[V_\alpha]=[V_{\alpha-b/2}]+[V_{\alpha-b/2}]$ 第二项与第一项重复。
  依据1：同篇 p.35 (5.25) 的 $\pm$ 两通道；依据2：hep-th/0104158 §4 (73)–(74)、§6 Thm 1（$2\alpha_{m,n}=-mb-nb^{-1}$）。
  订正为 $[V_{\alpha+b/2}]$；影响卡 `ggl24/concept/degenerate-fields-bpz`（已加 `corrections`）。
- **E2（medium，fixed）** p.21 (3.41)：$\{\kappa_k,w_l\}=\delta_{r,s}$ 中 $r,s$ 在该式未定义。
  依据1：p.17 (3.26) 的 $\{\kappa_r,w_s\}=\delta_{r,s}$；依据2：同页 (3.40) 的指标为 $r,k$、左式为 $k,l$。
  订正为 $\delta_{k,l}$；影响卡 `ggl24/concept/isomonodromic-schlesinger`。
- **E3（medium，fixed）** p.75 (8.58)：末项分母写作 $y-z_r$，但 apparent singularity 在 $w_r$、残数 $\kappa_r$。
  依据1：p.14 (3.15) 与 p.43 (5.51)(5.52)；依据2：v1 §5.7 对应式两处均写 $y-w_r$。
  订正为 $y-w_r$；影响卡 `ggl24/concept/degenerate-fields-bpz`。
- **E4（low，open，存疑）** p.8：$\theta=0$ 切片「clearly isomorphic to $\mathrm{Bun}_G$」。
  该句是 Hitchin 复结构（Higgs 对）下的陈述，$\mathrm{Bun}_G$ 应读作度 0 稳定丛模空间；
  若直接对 (2.1) 取 $\theta=0$ 得 $F_A=0$（平坦联络），二者经 Hitchin 复结构旋转等同，不是同一个复结构，
  「clearly isomorphic」略去了稳定性/半稳定性条件。只有本篇内部这一处措辞问题，
  按纪律保留原文，卡 `ggl24/concept/hitchin-selfduality-equations` 的 `provenance_note` 标「存疑」。
