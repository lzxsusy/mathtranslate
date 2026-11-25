# 甲组卡片报告（card1）

## 1. 张数与总览

任务书 22 张卡全部完成，无缺卡、无清单外卡：

- 概念卡 18 张（`cards/concepts/`），例子卡 4 张（`cards/examples/`）。
- id / type / track 严格按任务书，文件名 = id 末段。
- 每卡均含 summary（20–120 汉字）、以「？」结尾的 question、≥3 条 key_points、≥1 条成对 `$` 的 formulas、≥1 条 theorems、≥1 条 pitfalls、≥2 条 related（至少 1 条跨组）、sources（book/section/pages_zh/pages_en/anchor 齐全，anchor 均指向非空正文行）。
- 例子卡另含 `concept_refs`（≥2 个概念卡 id）、`setup`、`computation`。
- `rights = rewritten`、`status = draft`；全卡无本机绝对路径、无 tab。

最终校验：

```
cd C:\Users\admin\Downloads\_cards_grassmann
"C:\Users\admin\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe" tools\validate_cards.py
```

结果：甲组 22 个文件 **0 ERROR / 0 WARN**；全库仅剩 1 条 error，属别组的
`bicyclic-algebra-faddeev-4.json: 含 tab（.theorems[0].name）`，按纪律未动。

## 2. 每卡一句话

| # | id | 类型 | track | 一句话内容 | 主要定理（证明状态） | 中译/英文页 | anchor |
|---|---|---|---|---|---|---|---|
| 1 | `grassmann/concept/berezin-toeplitz-quantization` | 概念 | 1 | 由 Toeplitz 算子系数定义的 $\star_\sigma^{BT}$ 是 $(M_\sigma,\omega)$ 的微分形变量子化，且 $k^{-1}$ 与 $(k+n/2)^{-1}$ 两种展开由 $\varphi(h)=\frac{2h}{2+nh}$ 唯一平移。 | 定理 11（reference） | 21/24 | `chapters/ch01.tex:641` |
| 2 | `grassmann/concept/curve-operator` | 概念 | 1 | TQFT 曲线算子 $Z_k^{(n,d)}(\gamma,\lambda)$ 是配边值而非函数乘法算子，$k\to\infty$ 时渐近等于 Toeplitz 算子 $T_{h_{\gamma,\lambda}}^{(k)}$。 | 定理 4（sketch） | 8/11 | `chapters/ch01.tex:47` |
| 3 | `grassmann/concept/formal-hitchin-connection` | 概念 | 1 | 以 $h=1/(k+n/2)$ 为形式参数，Hitchin 联络展开为 $D_V f=V[f]+\tilde D(V)(f)$，一阶项唯一且 $\tilde D=0\bmod h$。 | 定理 6（reference） | 12/15 | `chapters/ch01.tex:175` |
| 4 | `grassmann/concept/formal-trivialization` | 概念 | 1 | 形式平凡化是满足 $D_V(P(f))=0$、模 $h$ 为恒等的算子值映射，一阶项为 $\frac14\Delta+i\nabla_{X_F''}$。 | 定理 7（sketch） | 12/15 | `chapters/ch01.tex:213` |
| 5 | `grassmann/concept/hitchin-connection` | 概念 | 1 | 在刚性 Kähler 族上 Hitchin 联络保持子丛 $H^{(k)}$，显式公式含 $\frac{1}{4k+2n}\{\Delta_{G(V)}+2\nabla_{G(V)dF}+4kV'[F]\}$ 修正。 | 定理 5（sketch） | 11/14 | `chapters/ch01.tex:165` |
| 6 | `grassmann/concept/rigid-kahler-family` | 概念 | 1 | 刚性指 $\bar\partial_\sigma(G(V)_\sigma)=0$，即 Kähler 族沿 $V$ 不变形；它是定理 5/9 不可省的前提。 | 定理 9（sketch） | 17/20 | `chapters/ch01.tex:443` |
| 7 | `grassmann/concept/toeplitz-operator` | 概念 | 1 | $T_{f,\sigma}^{(k)}(s)=\pi_\sigma^{(k)}(fs)$ 是 $H^0(M_\sigma,\mathcal L_\sigma^k)$ 上的 Toeplitz 算子，其乘积展开给出 Schlichenmaier 星积系数。 | 定理 10（reference） | 19/22 | `chapters/ch01.tex:543` |
| 8 | `grassmann/concept/verlinde-bundle` | 概念 | 1 | 纤维为 $H^0(M_\sigma,\mathcal L^k)$ 的丛 $\mathcal V_k\to\mathcal T$ 带自然 Hermite 结构，其射影化容有平坦 $\Gamma$-不变联络。 | 定理 1（reference） | 9/12 | `chapters/ch01.tex:85` |
| 9 | `grassmann/example/factorization-along-a-curve` | 例子 | 1 | 沿 $\gamma$ 切开并把两边界粘成两点得 $\Sigma'$，配边空间与 End 都按边界标号 $\mu$ 直和分解。 | 式 (3)（reference） | 9/12 | `chapters/ch01.tex:66` |
| 10 | `grassmann/example/holonomy-star-product` | 例子 | 1 | 和乐函数在 Berezin–Toeplitz 星积下的首项是乘积、一阶项是 Goldman 括号，即 $h_{\gamma_1}\star h_{\gamma_2}=h_{\gamma_1}h_{\gamma_2}-\frac{ih}{2}h_{\{\gamma_1,\gamma_2\}}+O(h^2)$。 | 定理 8（complete，4 步） | 13/16 | `chapters/ch01.tex:269` |
| 11 | `grassmann/concept/koszul-cohomology` | 概念 | A | $K_{p,q}(X,\mathcal F,L)$ 是 Koszul 复形的中间上同调，度量 $L$ 的正规生成性与合冲。 | 定理 2.6（complete，3 步） | 34/38 | `chapters/ch02.tex:148` |
| 12 | `grassmann/concept/bogomolov-inequality` | 概念 | 3 | 稳定无挠层的 $\ch_2$ 上界；曲面情形化为 $c_1^2(L)\le 4d$，是 Reider 论证的「稳定支」。 | 应用 2.1（complete，3 步）；经典形式（reference） | 57/62 | `chapters/ch03.tex:110` |
| 13 | `grassmann/concept/bridgeland-stability-condition` | 概念 | 3 | 倾斜心 $\mathcal A_s$ 上的稳定性：由中心荷 $Z$ 的相位定义，并要求 HN 滤过存在。 | 命题 3.6（complete，4 步） | 55/60 | `chapters/ch03.tex:34` |
| 14 | `grassmann/concept/central-charge-and-phase` | 概念 | 3 | $Z_{s+it}(E)=-d_{(s,t)}(E)+it\,r_s(E)$，相位 $\varphi=\frac1\pi\arg Z$ 决定稳定对象，参数 $(s,t)$ 落在半圆盘内。 | 推论 3.4（sketch）；推论 3.7（complete，3 步） | 63/68 | `chapters/ch03.tex:432` |
| 15 | `grassmann/concept/reiders-theorem` | 概念 | 3 | 充裕 $L$ 满足 $c_1^2(L)>(d+1)^2$ 及曲线条件时，$K_S+L$ 分离长度 $d$ 的子概形（$H^1=0$）；推论给 Fujita 曲面情形。 | Reider 定理（complete，4 步）；推论（reference） | 58/63 | `chapters/ch03.tex:175` |
| 16 | `grassmann/concept/thaddeus-pair` | 概念 | 3 | 把 Reider 的扩张看成 $\mathcal A_s$ 中的态射，用倾斜心统一曲面上「稳定丛—割线簇」的 Thaddeus 对。 | 存在性（reference）；曲面 Ext 计算（complete，2 步） | 56/61 | `chapters/ch03.tex:42` |
| 17 | `grassmann/concept/torsion-pair-and-tilt` | 概念 | 3 | 由斜率阈值 $s$ 切出的 $(\mathcal F_s,\mathcal T_s)$ 是挠对，其倾斜心 $\mathcal A_s=\{H^{-1}\in\mathcal F_s,H^0\in\mathcal T_s\}$ 是本章稳定性的舞台。 | 应用 3.1（complete，2 步）；HRS 定理（reference） | 60/65 | `chapters/ch03.tex:247` |
| 18 | `grassmann/concept/wall-and-wall-crossing` | 概念 | 3 | 参数 $(s,t)$ 变动时稳定对象在墙 $t=\sqrt{\frac14-\frac{2d}{H^2}}$ 处由稳定变不稳定，模空间发生翻转。 | 命题 4.1（complete，3 步） | 56/61 | `chapters/ch03.tex:88` |
| 19 | `grassmann/example/s-half-dichotomy` | 例子 | 3 | $s=1/2$ 时 $f\in\Hom_{\mathcal A_{1/2}}(L\otimes\mathcal I_Z,\mathcal O_S[1])$ 的单射性恰好等价于对应秩 2 层 $E$ 的半稳定性，复现第 2 节二分法。 | 例（complete，3 步） | 62/67 | `chapters/ch03.tex:364` |
| 20 | `grassmann/example/slope-comparison-semicircle` | 例子 | 3 | 两类对象的斜率比较可同乘正分母、展开消项，最终化为半圆内点的条件 $t^2<s(1-s-2e)$。 | 例（complete，3 步） | 64/69 | `chapters/ch03.tex:462` |
| 21 | `grassmann/concept/affine-grassmannian` | 概念 | A | $\mathrm{Gr}=G^\vee(\mathcal K)/G^\vee(\mathcal O)$，轨道由支配权标号，微小权轨道闭且射影，闭包由支配序给出。 | 定理 2.1（sketch） | 84/92 | `chapters/ch05.tex:62` |
| 22 | `grassmann/concept/gv-sheaf` | 概念 | A | $\operatorname{codim}V^i(\mathcal F)\ge i$ 的层，等价于 Fourier–Mukai 变换支集的余维条件与 $\mathbf R\Delta\mathcal F$ 满足 $WIT_g$。 | 定理 2.3（reference） | 137/152 | `chapters/ch08.tex:44` |

## 3. sketch 清单及原因（6 张）

| 卡 | 定理 | 为何只能 sketch |
|---|---|---|
| `curve-operator` | 定理 4 | 原文只给「主要思想」（用 Kac 的 $S$ 矩阵显式式 (4) 与 [A1] 的 Bohr–Sommerfeld 集），极限论证细节全部推到 [A7]，本章无可逐步展开的证明。 |
| `formal-trivialization` | 定理 7 | 一阶项的存在与形式在 §4 命题 3 才给出，而命题 3 推出的是 $P=\mathrm{Id}-h(\frac14\Delta+i\nabla_{X_F''})+O(h^2)$（负号），与定理 7 的加号相反（译注 872）；符号未定，不能按 complete 写。 |
| `hitchin-connection` | 定理 5 | 定理本身由引理 2、3、4 合成，而引理 2、4 的证明在 [A6]，本章只引用；正文只补了「引理 4 → 引理 3」与 $u(V)$ 的化简。 |
| `rigid-kahler-family` | 定理 9 | 同定理 5：三个引理里引理 2、4 的证明在 [A6]，本章只给引理 4→3 的推导与刚性条件的用法。 |
| `central-charge-and-phase` | 推论 3.4 | 原文只有一句「由命题 3.3」，没有展开 $r_s=0$ 时 $d_{(s,t)}\ge0$ 的推导；补全需要额外的格点/正性论证，故记 sketch 并在 `gap_note` 写明。 |
| `affine-grassmannian` | 定理 2.1 | 本章证明仅三行，实质输入是 [MVi] 定理 7.3 的几何 Satake 等价（反常层、半小性、分解定理都未展开），故记 sketch 而非 complete。 |

其余 16 张的主定理为 complete（章内有可逐步展开的证明）或 reference（原文明确只引文献）。

## 4. id / related 冲突

- **id 无冲突**：22 个 id 与任务书逐一对应，未改 id、未写清单外卡；文件名与 slug 一致。
- **related 无悬空**：全部 related 都是当时 `cards/` 下真实存在的 id。写卡中期，别组卡先引用了尚未落盘的 `affine-grassmannian`、`gv-sheaf` 等，validate 一度报 18 条 dangling；这两张落盘后自动消解。最终全库只剩 1 条别组 error（`bicyclic-algebra-faddeev-4.json` 的 tab），未动别人的文件。
- **跨组要求满足**：每张卡至少 1 条跨组 related，取自 `parabolic-bundle`、`geometric-satake-correspondence`、`factorization-property`、`coherent-system`、`alpha-stable-coherent-system`、`slope-of-effective-divisor`、`clifford-index` 等（均非甲组）。
- **页码口径**：一律用 pymupdf 实测的中文 PDF 页作 `pages_zh`，`pages_en` 按章偏移（ch01 +3、ch02 +4、ch03 +5、ch05 +8、ch08 +15）。批注里的「中译 p.N」偶与实际页差 1–2，已在逐卡核对后以实测为准（例如 ch03 anchor 88：批注 57、实测 56；anchor 462：批注 63、实测 64；ch08 定义 2.1：批注由「原书 p.144」推得中译 138，实测 137）。

## 5. 存疑（5 条）

1. **和乐星积首项**：中译 p.13（英文原书 p.18 同印）把首项写作 $h_{\gamma_1\gamma_2,\lambda_1\cup\lambda_2}$，与星积的 $c^{(0)}=fg$ 表面冲突（相交曲线 $h_{\gamma_1}h_{\gamma_2}\neq h_{\gamma_1\gamma_2}$）。卡片按正确数学写乘积首项，并在 pitfalls 点明「原印如此，见 errata」；但无法确证是笔误还是某种特殊配对约定。
2. **ch03 推论 3.9(ii) 的 $C^2\ge1$**：原文省略过甚，批注 7 与笔记都未能重构，疑有循环论证之嫌。它影响 Reider 型定理的定量版本，若后续有人补全，应回改 `reiders-theorem` 或 `bogomolov-inequality` 的相应步骤。
3. **ch05 定理 2.1 的证明等级**：正文只有三行，且全部依赖 [MVi] 定理 7.3；我记作 sketch。若项目标准把「给出证明思路 + 明确引用」也算 complete，则应改为 complete，但 `gap_note` 的信息仍建议保留。
4. **ch01 定理 7 与命题 3 的符号冲突**：定理 7 的一阶项写 $+\frac14\Delta+i\nabla_{X_F''}$，§4 命题 3 推出的是同式带负号，译注 872 说「按推导应带负号」。卡片按命题 3 的负号写 formal-trivialization，并在 pitfalls 记录定理 7 原文的加号；究竟哪个是定稿符号，需对照作者原稿或 [A6]。
5. **ch08 定义 2.1 的页码**：批注 2 给「63–80 行，原书 p.144」，按 ch08 换算（中译 = 原书 − 6）应为中译 138，但 pymupdf 在 137 页检出「命题与定义：$GV$-层」与「以下条件等价」。差一页可能因定义环境跨页；卡片取实测 137/152，若审校以批注为准需统一。
