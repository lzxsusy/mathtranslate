# ch05b 译校报告（译者：tr07）

## 1. 覆盖范围
- chunk：`ch05b` = PDF p.273–297 = **原书 p.272–296**
- 内容：例 5.2.4（一维谐振子）续段 + §5.3 海森堡群（5.3.1 海森堡李代数、5.3.2 海森堡群、5.3.3 薛定谔表示、5.3.4 巴格曼–福克表示）+ §5.4 几何量子化（5.4.1 狄拉克量子化原理、5.4.2 格罗嫩沃尔德–范霍夫定理、5.4.3 预量子化、5.4.4 极化与量子态、5.4.5 量子算子）+ 第 5 章章末回顾
- 文件：`src/chunks/ch05b.tex`（约 34 KB、1465 行、229 个公式）
- 块界：块首落在例 5.2.4 正文中段（PDF p.272 = 原书 p.271 末句续到下一行），已回看 PDF p.272 页图把句子补全，文件头写 `% [块界：本句起于 PDF p.272 中段，已按前页图补全；此为上一块例 5.2.4 的续文]`，与 ch05a **无重复**。块尾止于原书 p.296 完整句「……就有正确的本征值 $(n+\frac12)\hbar$。」，随后 `\takeaway` 与 `\chapterreview` 收束，**第 5 章在本块结束**。

## 2. 陈述环境编号（全部手工照抄原文）
| 编号 | 名称 | 原书页 |
|---|---|---|
| Definition 5.3.1 | 薛定谔表示算子 $T_\hbar(\mathbf r,\mathbf s,\lambda)$ | p.274 |
| Proposition 5.3.2 | $T_\hbar$ 的复合法则 | p.274 |
| Theorem 5.3.3 | 斯通–冯·诺依曼定理 | p.275 |
| Definition 5.3.4 | 巴格曼–福克空间 $\mathcal{F}_n$ | p.276 |
| Proposition 5.3.5 | $\mathcal{F}_n$ 的完备性 | p.276 |
| Proposition 5.3.6 | 伴随关系 $\langle z^if|g\rangle_\hbar=\langle f|\hbar\pa_{z^i}g\rangle_\hbar$ | p.276 |
| Proposition 5.3.7 | $\{\lambda_I\}$ 是 $\mathcal{F}_n$ 的正交归一基 | p.277 |
| Proposition 5.3.8 | $\norm{z^if}_\hbar^2=\hbar\norm f_\hbar^2+\norm{\hbar\pa_{z^i}f}_\hbar^2$ | p.278 |
| Theorem 5.4.1 | 格罗嫩沃尔德–范霍夫定理 | p.282 |
| Definition 5.4.2 | 预量子化线丛 | p.285 |
| Definition 5.4.3 | 可量子化辛流形 | p.287 |
| Example 5.4.4 | $M=T^*X$ 的预量子化 | p.287 |
| Example 5.4.5 | $S^2$ 的可量子化条件 $A\in\frac{\hbar}{2}\Z$ | p.287 |
| Definition 5.4.6 | 极化 | p.288 |
| Definition 5.4.7 | $P$-极化截面 | p.288 |
| Example 5.4.8 | $\R^{2n}$ 上两种极化给出的波函数 | p.289 |
| Example 5.4.9 | $\C^n$ 的凯勒极化与 Segal–Bargmann 空间 | p.289 |
| Example 5.4.10 | 复流形上的全纯量子化 | p.290 |
| Example 5.4.11 | $\CP^1$、$\mathcal{O}(k)$ 与 $\mathrm{su}(2)$ 自旋 $k/2$ 表示 | p.291 |
| Definition 5.4.12 | $P$-保持函数 | p.292 |
| Proposition 5.4.13 | $Q(f)\psi$ 仍是 $P$-极化截面 | p.292 |
| Example 5.4.14 | $\R^{2n}$ 上 $P$-保持函数的量子化 | p.293 |
| Example 5.4.15 | 凯勒量子化中 $Q(\mathscr{H})=\hbar z\frac{\pa}{\pa z}$ | p.294 |

共 23 个带编号陈述（1 定理 5.3.3、1 定理 5.4.1、6 定义、6 命题、9 例）。编号全部照抄原文，同节共用计数器，未用自动编号。

## 3. 公式核对
逐页回 `work\pages\p273.png`–`p297.png`（150 dpi）核对，关键式另做 300 dpi 裁图。核对要点：
- p.272 谐振子：$\frac{1}{2\pi}\oint_C\lambda=\frac{1}{2\pi}\oint_Cp\rd x=\frac{E}{\omega}$、$\omega=\sqrt{k/m}$、$m(C)=2$、$\frac{E}{\hbar\omega}-\frac12\in\Z$、$E=\hbar\omega(n+\frac12)$。
- p.274–275：BCH 群律、$T_\hbar$ 的显式作用与复合法则（$\lambda_1+\lambda_2+\frac12(\mathbf r_1\cdot\mathbf s_2-\mathbf r_2\cdot\mathbf s_1)$）、$\mathrm{Ad}_{T_\hbar}$ 的两条作用。
- p.276–277：$\mathcal{F}_n$ 内积 $\frac{1}{(\pi\hbar)^n}\int\rd^{2n}z\,\ol fge^{-\abs z^2/\hbar}$、$\lambda_I=\mathbf z^I/\sqrt{\hbar^{|I|}I!}$、多重圆盘估计。
- p.279–280：$\rho_\hbar(\mathbf w)$ 的 BCH 相位 $e^{\frac{i}{\hbar}\operatorname{Im}(\ol{\mathbf w}_1\cdot\mathbf w_2)}$、显式公式、$\mathcal{B}$ 的积分核与酉性五行。
- p.281–283：Moyal 乘积左右导数记号、$[f,g]_*=i\hbar\{f,g\}+\frac{(i\hbar)^3}{24}\cdots$、Groenewold 证明中 $[x^3,p^3]_*$ 与 $[x^2p,xp^2]_*$ 的系数。
- p.285–287：$[Q(f),Q(g)]$ 展开、$F_\nabla=-\frac{i}{\hbar}\omega$、$\left[\frac{i}{2\pi}F_\nabla\right]=c_1(\mathcal{L})$、整性条件 $\frac{1}{2\pi\hbar}\int_\Sigma\omega\in\Z$。
- p.288–291：极化的三条要求（用 ①②③ 字符逐条列出）、$L^2(M,\mathcal{L})_P$、凯勒情形的 $F_\nabla$ 链、$\mathcal{O}_{\CP^1}(k)$ 的转移函数与 $H^0$、$\omega=ik\hbar\frac{dz\wedge d\ol z}{(1+\abs z^2)^2}$。
- p.292–296：HRR 与 $\dim H^0\sim k^n\vol_\omega(M)$、$[\nabla_X,Q(f)]$ 六行链、Example 5.4.14 的 $\left[\frac{\pa}{\pa p_k},V_f\right]$、$V_f$ 的复坐标形式与 $Q(f)$ 三行化简、$Q(\mathscr{H})=\hbar z\frac{\pa}{\pa z}$。

版式说明：向量用粗正体 `\mathbf`；算子名 `\operatorname{Sp}`、`\mathrm{Ad}`、`\mathrm{ch}`、`\mathrm{td}`、`\mathrm{su}(2)`、`\operatorname{Im}`；上划线统一用 `\ol`（preamble 宏）；宽帽 `\wh`；哈密顿量用 `\mathscr{H}`；薛定谔表示算子下标是 $\hbar$（原文如此，非 $h$）。原文引用编号（定理 4.4.1、§5.4.2、§6.1.3 等）照抄未改。

## 4. 图
`python tools\figtool.py auto 273 297` 返回 **0 张候选**：本块原书没有图，无需裁剪或重绘。

## 5. 术语增补（见 `work/term_requests_ch05b.md`）
| 英文 | 译法 | 页 |
|---|---|---|
| symplectic basis | 辛基 | 272 |
| symplectomorphic (vector spaces) | 辛同构 | 272 |
| indicator function | 示性函数 | 277 |
| Bargmann–Fock representation | 巴格曼–福克表示 | 279 |
| Segal–Bargmann transform | Segal–Bargmann 变换 | 280 |
| prequantization condition | 预量子化条件 | 287 |
| quantizable | 可量子化的 | 287 |
| Liouville 1-form | 刘维尔 1-形式 | 289 |
| Kähler potential | 凯勒势 | 290 |
| hermitian holomorphic line bundle | 厄米全纯线丛 | 290 |
| positive line bundle | 正线丛 | 292 |
| Euler characteristic | 欧拉示性数 | 292 |
| Hirzebruch–Riemann–Roch theorem | 希尔策布鲁赫–黎曼–罗赫定理 | 292 |
| P-preserving | P-保持的 | 292 |
| Blattner–Kostant–Sternberg kernel | 布拉特纳–科斯坦特–斯滕伯格核（BKS 核） | 293 |
| half-density | 半密度 | 295 |
| canonical line bundle | 典范线束 | 296 |

沿用术语表：辛流形、辛形式、哈密顿向量场、泊松括号、极化、实极化、凯勒极化、预量子化线丛、整性条件、托德类、陈类、联络、曲率、线丛、截面、图卡、矩映射、刘维尔测度、海森堡群、海森堡代数、薛定谔表示、巴格曼、福克、外尔量子化、Moyal 乘积、星乘积、形变量子化。
表内 `symplectomorphism=辛同胚` 指流形之间；本块 p.272 是辛**向量空间**之间的同构，故用「辛同构」，已在增补表注明。

## 6. Tutor Note（正文照原文，未改）
1. 原书 p.276（命题 5.3.5 证明末行）：$\langle f|f\rangle\le\frac{(\pi\hbar)^n}{(\pi R^2)^n}\cdots$，按量纲似应为 $(\pi\hbar)^{n/2}$。
2. 原书 p.280（$\mathcal{B}$ 酉性验证）：第三、四行的指数按原文录入，依上一步推导应为 $-\frac{1}{4\hbar}(\mathbf x-\mathbf y)\cdot(\mathbf x-\mathbf y)$。

## 7. 存疑
- 原书 p.291（例 5.4.10 末）写 "P-potential sections are holomorphic sections of $\mathcal{L}$"，"potential" 疑为 "polarized" 之误；中文按「$P$-极化截面」处理，未加批注。
- 原书 p.294 记 $g^{\ol mj}$ 为 $g_{j\ol m}$ 的逆矩阵，却写 $\sum_{\ol m}g_{i\ol m}g^{\ol mj}=\delta_i{}^j$（左边下标是 $i$）；照抄原文，读法不受影响。
- 原书 p.295 称函数「at most linear in $\ol z^i$」，而对应条件是 $\frac{\pa^2}{\pa\ol z^i\pa\ol z^j}f=0$；两者一致，照译。
- 本块 standalone 编译时节号显示为 0.3/0.4（无 `\chapter`），合书后应为 5.3/5.4，属预期。

## 8. 编译自检
```
powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch05b
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch05b.pdf   (26 页)

python tools\lint.py ch05b
OK   ch05b   汉字 34436  节 2 小节 9 陈述 23 公式 229 图 0(TikZ 0) 批注 2
合计：问题 0 条，提示 0 条
```
修错记录：① 首轮 file:line=1，残留一处 `\ov{\langle s_1,s_2\rangle}` 未改成 `\ol`（该处 `\ov` 后换行，先前批量替换漏掉）；② 补 p.274、p.290 两处页标记（lint 提示居多）；③ p.277「特征函数」改「示性函数」（lint 提示歧义）。已渲染 26 页 `work/preview/ch05b_1..26.png` 抽查：公式与原书一致、无溢出页边、全角标点正常、`\takeaway`/`\chapterreview` 版式正常。

## 9. 状态
**完成并通过自检**（2026-11-07）。下一块：`ch06a`（PDF 298–313，原书 p.297–312，第 6 章章首）。
