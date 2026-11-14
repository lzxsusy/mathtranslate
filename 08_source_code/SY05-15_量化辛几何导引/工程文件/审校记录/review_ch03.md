# 审校记录：第 3 章 切触几何（Contact Geometry）

范围：原书印刷页 52–85，扫描 PDF 第 60–93 页。译文文件：
`qsg/tex/ch03-s01.tex` … `ch03-s07.tex`。

以下「原文疑误」在译文中**一律保留原文写法**并加 `% [Tutor Note: 原文疑误——…]`
批注；唯一例外是第 1 条（$\R^n\to\R^{2n+1}$）——它是纯记号笔误、不涉及任何公式内容，
译文直接按 $\R^{2n+1}$ 排印并加注说明。请教授复核。

---

## 一、已确认的疑误（硬错误，正文已加批注）

| # | 位置（印刷页 / PDF 页） | 原文 | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | 注 3.2.1，p.56 / p.64 | "there are other contact forms on $\R^n$" | 所列 $\alpha'$、$\alpha''$ 含 $x_i,y_i,z$ 共 $2n+1$ 个坐标，显系 $\R^{2n+1}$ 之误 | 改为 $\R^{2n+1}$（译文中已按 $\R^{2n+1}$ 处理并加注） |
| 2 | 图 3.3 及例 3.2.2，p.57 / p.65 | 图注标注 $\xi_{(x,\theta,z)}$ | 本例取柱坐标 $(r,\theta,z)$，下标首字母应为 $r$ | 改为 $\xi_{(r,\theta,z)}$（原图不改，译文加注） |
| 3 | 例 3.2.3，p.59 / p.67 | $\gamma_a=\{(z_1,0)\in\partial E(a,b)\mid |z_1|=a\}$；$\gamma_b$ 同 | 按 (3.7) 的 $E(a,b)$ 定义（$\lvert z_1\rvert^2/a+\lvert z_2\rvert^2/b\le1$），在 $\partial E$ 上取 $z_2=0$ 得 $\lvert z_1\rvert^2=a$，故应为 $\lvert z_1\rvert=\sqrt a$；周期 $\pi a,\pi b$ 与 (3.9) 一致，说明只是半径处笔误 | 改为 $\lvert z_1\rvert=\sqrt a$、$\lvert z_2\rvert=\sqrt b$ |
| 4 | 辛化段落，p.61 / p.69 | "the symplectization assembles $\R$-many contact manifolds $(M,\omega)$" | $M$ 是切触流形，其上并无辛形式 $\omega$ | 改为 $(M,\xi)$ |
| 5 | p.62 / p.70 公式 | $(\dd r\wedge\alpha+\dd\alpha)((v\partial/\partial r,R_\alpha,w),\eta)=v+\dd\alpha(v,\eta)$ | $v$ 是 $\partial_r$ 方向的标量，$\dd\alpha(v,\eta)$ 无意义；按上下文应为 $\dd\alpha(w,\eta)$，且 $\eta=R_\alpha$ 时该项为 $0$ | 改为 $\dd\alpha(w,\eta)$ |
| 6 | 式 (3.19)，p.64 / p.72 | $J(u(s,t))\frac{\partial u_\R}{\partial t}=\alpha(\frac{\partial u_M}{\partial s})$，随后写「即 $\frac{\partial u_\R}{\partial t}=-\alpha(\frac{\partial u_M}{\partial s})$」 | 两式符号不相容：由 $J(\partial_r)=R_\alpha$ 知左端对 $\alpha$ 求值即 $\frac{\partial u_\R}{\partial t}$，故第一式应为负号（或应写右端为 $-\alpha(\cdot)R_\alpha$） | 建议把中间式写成 $J(u)\frac{\partial u_\R}{\partial t}+\alpha(\frac{\partial u_M}{\partial s})R_\alpha=0$ |
| 7 | 式 (3.25)，p.69 / p.77 | $\varphi(t)\to\pm\infty\ (t\to\pm\infty)$ | 同一定义正文规定 $\varphi:\R\to(-1,1)$，且例中 $\varphi=\frac2\pi\arctan x$，极限为 $\pm1$ | 改为 $\varphi(t)\to\pm1$ |
| 8 | 定理 3.3.1，p.69 / p.77 | $u:(\dot\Sigma\setminus\Gamma,j)\to(SM,\dd(\ee^r\alpha),J)$ | 按本节记号 $\dot\Sigma=\Sigma\setminus\Gamma$ 已含刺点集，再减 $\Gamma$ 重复 | 改为 $(\dot\Sigma,j)$ |
| 9 | 例 3.4.3，p.73 / p.81 | "This corresponds to item (iii) in Remark 3.4.4" | 注 3.4.4 中第 (iii) 项是「$z'\ne0$ 而 $x'=0$，不可能」；描述前沿投影曲线终止的是第 (ii) 项（$z'=x'=0$） | 改为 item (ii) |
| 10 | p.77 / p.85 | "reveals a Hamiltonian feature of $\Op{Cont}_0(M,\omega)$" | 切触流形应记 $(M,\xi)$ | 改为 $\Op{Cont}_0(M,\xi)$ |
| 11 | 定义 3.7.1，p.83 / p.91 | "For a contact manifold $(M,\omega)$" | 同上 | 改为 $(M,\xi)$ |

## 二、存疑（需人工确认）

| # | 位置 | 原文 | 疑点 | 建议 |
|---|---|---|---|---|
| 13 | 定理 3.5.1，p.76 / p.84 | "for any closed contact manifold $(M,\xi)$, the contactomorphism group $\Op{Cont}(M,\xi)$ is a simple group" | 对闭流形被证明为单群的通常是恒等分支 $\Op{Cont}_0(M,\xi)$（Banyaga–Rybicki 型定理）。若字面指整个 $\Op{Cont}$，则当 $\Op{Cont}$ 不连通时，真子群 $\Op{Cont}_0$ 将在单群中成为非平凡正规子群，产生矛盾。原文紧接的一段也正是拿 $\Op{Cont}_0$ 与 $\Op{Ham}$ 作比较 | 建议按 $\Op{Cont}_0(M,\xi)$ 理解，或补充「当 $\Op{Cont}=\Op{Cont}_0$ 时」的连通性假设；译文中保留原文表述并加批注 |
| 14 | 命题 3.7.1 与例 3.7.2，p.84 / p.92 | 例 3.7.2 说「群 $\widetilde{\Op{Cont}_0}(M,\xi)$ 中存在正可缩环路」；命题说「$\Op{Cont}_0(M,\xi)$ 中不存在任何正的可缩环路」 | 两处所指的群不一致（万有覆叠 vs 底群）；实际上「正的可缩环路」应理解为 $\Op{Cont}_0$ 中的环路（作为 $\widetilde{\Op{Cont}_0}$ 中的类） | 统一表述为「$\Op{Cont}_0(M,\xi)$ 中的正的可缩环路」 |

## 三、非错误但易混的记号（译文加「记号提示」批注，未计入疑误）

| # | 位置 | 说明 |
|---|---|---|
| A | 例 3.2.1，p.55 / p.63 | $\alpha_{\mathrm{std}}\wedge(\dd\alpha_{\mathrm{std}})^n=\dd z\wedge\dd x_1\wedge\dd y_1\wedge\cdots$ 与直接计算相差常数因子 $n!$（$n=1$ 时恰为等式）；原文只关心非零性，故不算错，但逐符号核对时勿当恒等式 |
| B | §3.3，p.66–p.68 | 目标空间写作 $(M,\omega,J)$（沿用 §1.4 的一般辛流形记号），与本章作为切触流形的 $M$ 同名异义 |
| C | §3.2 注 3.2.3 段落，p.61 / p.69 | 「Liouville 流形」与「Liouville 域」交替出现，前者非紧、后者带边界，阅读时须区分 |
| D | 例 3.7.4，p.85 / p.93 | $(S^*_gM,\xi=\lambda_{\mathrm{can}}\rvert_{S^*_gM})$ 把切触结构 $\xi$ 直接写成切触形式；按 §3.2 (3.12) 的记号应理解为 $\xi=\ker(\lambda_{\mathrm{can}}\rvert_{S^*_gM})$ 或直接写 $(S^*_gM,\lambda_{\mathrm{can}})$ |

## 四、无法辨认的符号

无。全部 34 页均已逐页核对；公式 (3.1)–(3.45) 编号与原文一致（共 45 个编号公式）。

## 五、译文图片清单（16 幅，均按 300 dpi 从扫描页裁剪）

| 图号 | 文件 | 印刷页 / PDF 页 |
|---|---|---|
| 图 3.1 | `figures/fig_p063_1.png` | p.55 / p.63 |
| 图 3.2 | `figures/fig_p064_1.png` | p.56 / p.64 |
| 图 3.3 | `figures/fig_p065_1.png` | p.57 / p.65 |
| 图 3.4 | `figures/fig_p070_1.png` | p.62 / p.70 |
| 图 3.5 | `figures/fig_p073_1.png` | p.65 / p.73 |
| 图 3.6 | `figures/fig_p074_1.png` | p.66 / p.74 |
| 图 3.7 | `figures/fig_p074_2.png` | p.66 / p.74 |
| 图 3.8 | `figures/fig_p075_1.png` | p.67 / p.75 |
| 图 3.9 | `figures/fig_p076_1.png` | p.68 / p.76 |
| 图 3.10 | `figures/fig_p077_1.png` | p.69 / p.77 |
| 图 3.11 | `figures/fig_p080_1.png` | p.72 / p.80 |
| 图 3.12 | `figures/fig_p081_1.png` | p.73 / p.81 |
| 图 3.13 | `figures/fig_p082_1.png` | p.74 / p.82 |
| 图 3.14 | `figures/fig_p084_1.png` | p.76 / p.84 |
| 图 3.15 | `figures/fig_p091_1.png` | p.83 / p.91 |
| 图 3.16 | `figures/fig_p092_1.png` | p.84 / p.92 |
