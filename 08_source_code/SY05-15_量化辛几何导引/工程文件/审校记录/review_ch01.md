# 审校记录：第 1 章 辛流形（Symplectic Manifold）

范围：原书印刷页 1–21，扫描 PDF p9–p29。
产出：`qsg/tex/ch01-s01.tex` … `ch01-s07.tex`；图 `qsg/figures/fig_p016_1.png`。

处理原则：凡确认的原书笔误，译文**保留原文写法**并加 `% [Tutor Note: ...]` 注释说明，同时在本文件记录。

---

## 一、确认的原文疑误（按页序）

| # | 位置 | 原文 | 疑点 | 建议改法 |
|---|------|------|------|----------|
| 1 | 印刷 p.2（PDF p.10）命题 1.1.1 证明 | “there exists some $(2k-1)$-form $\alpha$ … such that $\omega=\mathrm{d}\alpha$” | 由 $[\omega^k]=0$ 只能推出 $\omega^k=\mathrm{d}\alpha$；$\omega$ 非退化且在闭流形上，绝不可能恰当（否则 $\int_M\omega^n=0$ 与体积形式矛盾）。此外该句逗号后接大写 “Then”，亦为印刷失误。 | $\omega^k=\mathrm{d}\alpha$ |
| 2 | 印刷 p.4（PDF p.12）例 1.2.2 开头 | “Let $Q$ be a differentiable $n$-dimensional manifold $Q$.” | 句末重复符号 $Q$ | 删去第二个 $Q$ |
| 3 | 印刷 p.4（PDF p.12）定理 1.2.2（Weinstein） | “$(U,\omega_{\mathrm{can}}\|_U)$, where $U\subset T^*M$ is a neighborhood of the zero-section in the cotangent bundle $T^*L$” | 同一个 $U$ 既在 $T^*M$ 又在 $T^*L$ 中；$\omega_{\mathrm{can}}$ 只定义在 $T^*L$ 上 | $U\subset T^*L$ |
| 4 | 印刷 p.5（PDF p.13）例 1.2.3 | “Two different symplectic structures on $\Sigma_g$ are simply rescaling of each other.” | 严格地说应在「相差一个辛同胚 + 常数伸缩」的意义下理解（Moser 稳定性）；一般不存在常数 $c$ 使 $\omega_1=c\,\omega_2$ 逐点成立 | 表述加「在辛同胚与常数伸缩的意义下」限定 |
| 5 | 印刷 p.8（PDF p.16）命题 1.3.1 证明（(i) 的计算） | 第 3 行 $g\big(-\big(\sqrt{AA^{\mathrm T}}\big)^{-1}v,\ \big(\sqrt{AA^{\mathrm T}}\big)^{-1}Aw\big)$ | 由 $\omega(x,y)=g(Ax,y)$、$A^2=-\big(\sqrt{AA^{\mathrm T}}\big)^2$ 只能得到 $g\big(-\big(\sqrt{AA^{\mathrm T}}\big)v,\cdot\big)$；按原文写法第 4、5 行不成立（一般 $A^{-1}\neq-A$） | 指数改为 $-\big(\sqrt{AA^{\mathrm T}}\big)v$ |
| 6 | 印刷 p.15（PDF p.23）1.6 节开头的动机段 | “$Y_1=\mathrm{span}\langle x_1\rangle\subset\R^{2n}$ and $\omega_{\mathrm{std}}\|_N=0$”；其后“$\omega_{\mathrm{std}}\|_N=0$” | 通篇未定义 $N$，按上下文应为 $Y_1$、$Y_k$ | $\omega_{\mathrm{std}}\|_{Y_1}=0$、$\omega_{\mathrm{std}}\|_{Y_k}=0$ |
| 7 | 印刷 p.16（PDF p.24）命题 1.6.1 证明 | “if $\omega_p(v,\cdot)=0$ on $T_p^*L$” | 余向量 $\omega_p(v,\cdot)$ 应作用于切空间 | $T_pL$ |
| 8 | 印刷 p.16（PDF p.24）注 1.6.2 | “take $M=\R^{2n}$ and consider the product symplectic structure defined in (1.4), then the anti-diagonal $\overline\Delta_M=\{(x,-x)\}$ is Lagrangian, while $\Delta_M$ is not.” | 在 (1.4) 的和形式 $\pi_1^*\omega+\pi_2^*\omega$ 下，$\{(x,-x)\}$ 的切向量为 $(v,-v)$，代入得 $2\omega(v,w)\neq0$，故它\emph{不}拉格朗日；而在差形式 $\pi_1^*\omega-\pi_2^*\omega$ 下 $\Delta_M$ 与 $\overline\Delta_M$ 都拉格朗日。两种解读都与原文结论不符 | 和形式下应为「复共轭图像 $\{(x,\bar x)\}$ 拉格朗日、$\Delta_M$ 不拉格朗日」；差形式下应删去「而 $\Delta_M$ 不是」 |
| 9 | 印刷 p.18（PDF p.26）命题 1.7.1 证明 | $\mathcal{L}_{X_{H_t}}\omega=\mathrm{d}\iota_{X_{H_t}}\omega+\iota_{X_{H_t}}\mathrm{d}\omega=\mathrm{d}(\mathrm{d}H_t)=0$ | 按 (1.15) 的约定 $\iota_{X_{H_t}}\omega=-\mathrm{d}H_t$，中间项应为 $\mathrm{d}(-\mathrm{d}H_t)$；结论不变 | 补负号 |
| 10 | 印刷 p.20（PDF p.28）$X$ 的哈密顿性验证 | “$\omega_x(X(x),\cdot)=\mathrm{d}H_t(x)(\cdot)+\cdots=\mathrm{d}(H_t+G_t\circ\psi_t^{-1})(x)(\cdot)$” | 按 (1.15)，每一行的 $\mathrm{d}$ 前都应带负号（第一项为 $-\mathrm{d}H_t$，第二项 $\omega(Y,\cdot)=-\mathrm{d}G_t(Y)$），正确末行为 $-\mathrm{d}(H_t+G_t\circ\psi_t^{-1})$；结论（$X$ 由 $H_t+G_t\circ\psi_t^{-1}$ 生成）不变 | 全链补负号 |
| 11 | 印刷 p.20（PDF p.28）注 1.7.2(ii) | “flow $\varphi_{\tilde H}^t$ can be viewed as the **time-reserving** of $\varphi_H^t$” | 应为 time-reversing（时间反演） | time-reversing |
| 12 | 印刷 p.20（PDF p.28）练习 1.7.3 | “for any time-reparametrization $\alpha(t):[0,1]\to[0,1]$ where $\alpha(0)=0$” | 只给 $\alpha(0)=0$ 不足：为使 $\{\varphi_H^{\alpha(t)}\}$ 在 $t=1$ 有意义并使推论成立，还需 $\alpha(1)=1$ 且 $\alpha$ 单调不减 | 补 $\alpha(1)=1$、$\alpha$ 单调 |
| 13 | 印刷 p.11（PDF p.19）(ii) 面积的定义 | “The $\mathrm{Area}(u)$ … is locally defined by (1.10)” | (1.10) 只给出面积元（被积式），并非面积的积分表达式；属表述省略 | 可写成 $\Area(u)=\int\sqrt{\cdots}\,\dd x\dd y$ |
| 14 | 印刷 p.4（PDF p.12）定理 1.2.1 之后 | “the rigorous statement and its proof will be given in **Section 4.3 in Chapter 5**” | 「4.3 节」按本书记号必属第 4 章；原书目录：第 4 章 Moser's Argument 的 4.3 节为 Neighborhood Theorems（印刷 p.92），第 5 章 Floer Theory 的 5.3 节为 Homological Rigidity。故「Chapter 5」为笔误 | 第 4 章 4.3 节（**本译文已按目录证据直接更正**，并在正文加 Tutor Note；此为全章唯一一处改动原文处） |

## 二、术语与记号说明（已写入正文 Tutor Note）

- `//`：原书用以标记例子结束的记号，见 p.1 脚注；译文照排为 `//` 并在首个例子处保留脚注。
- $\mathcal{J}(M,\omega)$、$\Lambda_n$ 分别用花体 $\mathcal{J}$ 与 $\Lambda$，与原文一致；原书排版 $\mathcal{J}$ 与 $J$ 极易混淆，已在 1.3 节注明。
- (1.11) 中的 $\mathbf{1}_{n\times n}$ 按 SPEC 统一用 `\mathbf{1}`（不用 `\mathbb{1}`）。
- (1.13) 的辛球/辛柱约定：$B^{2n}(R)=\{\sum(x_i^2+y_i^2)\le R\}$，即半径为 $\sqrt R$；与常见「半径 $r$」写法差一个平方，已加 Tutor Note。
- 定理 1.3.1 的 Newlander–Nirenberg 上标 167、各处 [n] 均为原书文献编号，译文保留为 `\textsuperscript{}` 与 `[n]`。

## 三、待编辑确认

1. `preamble.tex` 未定义 `wfact`（“事实”环境）。本译文用 preamble 已有的 `\whead{事实}{1.3.1}` 手工排版（与 `ch02-s01.tex` 的做法一致）。若 Lead 认为宜增补环境，建议在 preamble 加
   `\newenvironment{wfact}[1]{\whead{事实}{#1}}{\par\medskip}`；否则无需改动。
2. 全书统一的 `//` 记号：第 2 章译文用了 `\hfill$\square$`，本章按原文用 `//`。若 Lead 要求全章统一，可批量替换。
