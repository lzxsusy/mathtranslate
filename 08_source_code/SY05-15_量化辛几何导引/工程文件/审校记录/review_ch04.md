# 第 4 章 审校记录（review_ch04.md）

范围：原书第 4 章 *Moser's Argument*，印刷页 86–100，扫描 PDF 第 94–108 页。
处理原则：译文**保留原文写法**并就地加 `% [Tutor Note: ...]` 说明；下表给出原文、页码、
疑点与建议改法，供教授定夺。标记「确信」者为可完全确定之笔误，「待核」者需对照作者原稿
或后续版本确认。

| # | 位置（印刷页 / PDF 页） | 原文 | 疑点 | 建议改法 | 把握 |
|---|---|---|---|---|---|
| 1 | p.87 / p.95，4.1 切触段落 | $(\psi_0)_*\xi_0=\xi_t$ | $\psi_0=\mathrm{id}$，左端恒为 $\xi_0$，除非 $\xi_t$ 恒等于 $\xi_0$，否则该式对一般 $t$ 不成立 | 改为 $(\psi_t)_*\xi_0=\xi_t$（与同页下文定理 4.1.2 的表述一致） | 确信 |
| 2 | p.88 / p.96，例 4.1.1 末段 | "contactomprhic" | 拼写错误 | "contactomorphic" | 确信 |
| 3 | p.89 / p.97，例 4.2.1 | "there exists $\beta\in H^1(M;\R)$ such that $\omega_1=\omega_0+\dd\beta$" | $H^1(M;\R)$ 的元素是上同调类，不能对其取外微分 $\dd\beta$ | 改为「存在 $1$-形式 $\beta\in\Omega^1(M)$ 使得 $\omega_1=\omega_0+\dd\beta$」 | 确信 |
| 4 | p.97 / p.105，定理 4.3.3 | $\varphi^*(\omega|_V)=\omega_{\mathrm{can}}|_V$ | $\varphi\colon U\to V$ 的定义域为 $U\subset T^*L$，而 $\omega_{\mathrm{can}}$ 是 $T^*L$ 上的形式；左端已是 $U$ 上的形式 | 右端改为 $\omega_{\mathrm{can}}|_U$ | 确信 |
| 5 | p.100 / p.108，引理 4.3.1 证明末式 | $=\dd\bigl(\int_0^1\varphi_t^*(\iota_{X_t}(\omega_1-\omega_0))\bigr)\,\dd t$ | $\dd t$ 被排在右括号之外。按定义 $\omega_1-\omega_0=\int_0^1\frac{\dd}{\dd t}\varphi_t^*(\omega_1-\omega_0)\dd t=\int_0^1\varphi_t^*\dd\iota_{X_t}(\omega_1-\omega_0)\dd t=\dd\bigl(\int_0^1\varphi_t^*\iota_{X_t}(\omega_1-\omega_0)\dd t\bigr)$，故 $\dd t$ 应在积分号内、右括号内 | 改为 $\dd\bigl(\int_0^1\varphi_t^*(\iota_{X_t}(\omega_1-\omega_0))\,\dd t\bigr)$ | 确信 |
| 6 | p.100 / p.108，引理 4.3.1 证明 | "$\varphi_t(\exp(q,v)):=\exp(q,tv)$，for any $(q,v)\in V$" | $\exp$ 只定义在 $U\subset NQ$ 上，且公式要求 $(q,tv)\in U$；$(q,v)\in V$ 中的 $V=\exp(U)$ 不是合适的作用域 | 改为 "for any $(q,v)\in U$" | 待核（可能只是记号混用） |
| 7 | p.100 / p.108，引理 4.3.1 证明末句 | "run Moser's argument for $\omega_t=\omega_0+t\,\dd\sigma$, where $t\sigma$ are the required 1-forms" | 若 $\omega_t=\omega_0+t\,\dd\sigma$，则按 (4.1) 所需的族是固定的 $\sigma_t\equiv\sigma$，而非 $t\sigma$；作者的用意应是「$\omega_t-\omega_0=\dd(t\sigma)$」 | 改为 $\sigma_t\equiv\sigma$；或改写为 $\omega_t=\omega_0+\dd(t\sigma)$ 并说明所需族为 $t\sigma$（两种写法需统一） | 待核 |
| 8 | p.87 / p.95，注 4.1.1 | "deformation of volume forms $\{\sigma_t\}$ ... where $\sigma_t$ is both non-degenerate and closed" | (i) 以 $\sigma_t$ 记体积形式族，与 (4.1) 的 $1$-形式 $\sigma_t$ 记号冲突；(ii)「非退化且闭」是辛形式的刻画，一般体积形式不必闭。结合定理 4.2.1 的准确表述，原意应是「把辛形式换成体积形式、把沿 $t$ 导数写成恰当形式，论证照样成立」 | 体积形式族改用 $\{\tau_t\}$；并核对「闭」这一条件是否必要 | 待核 |
| 9 | p.93 / p.101，定理 4.3.1 证明 | "$\varphi|_0=\mathbf 1$" | 作为集合 $\{0\}$ 上的「限制」记号略显含混，原意应为 $\varphi(0)=0$（在 $Q=\{0\}$ 上为恒等） | 可改写为 $\varphi(0)=0$，或统一使用 $\varphi|_Q=\mathbf 1$（$Q=\{0\}$） | 待核（记号问题） |
| 10 | p.100 / p.108 | "let us give the prove of Lemma 4.3.1" | 语法笔误（prove → proof） | 改为 "give the proof" | 确信（仅英文，不影响译文） |

## 已核对但判为无误的易混点

- p.91 / p.99，(4.12)：$\bigl[\frac{\dd}{\dd t}\omega_t\bigr]=\frac{\dd}{\dd t}[\omega_t]$ 的
  第一个等号确实来自「对任意 $2$-闭链 $C$ 可交换 $\frac{\dd}{\dd t}$ 与 $\int_C$」，不是笔误。
- p.91 / p.99，"（正确进路 I）" 中 $\Delta\tau_t=\dd(\delta\tau_t)\iff\delta(\dd\tau_t)=0$
  的等价性成立（因 $\Delta\tau_t=\dd\delta\tau_t+\delta\dd\tau_t$ 且 $\Delta\tau_t=\frac{\dd}{\dd t}\omega_t$）。
- p.96 / p.106，$\omega(Jv,Jw)=\omega(v,w)=0$ 与 $g_J(v,Jw)=\omega(v,-w)=-\omega(v,w)=0$
  均正确（用 $J^2=-\mathbf 1$ 与 $J$ 的 $\omega$-相容性）。
- p.97 / p.107，定理 4.3.3 证明中 $(\psi^*\omega)_{(q,0)}=-y_2^*(x_1)+y_1^*(x_2)$ 与
  $\omega_{\mathrm{can}}=y_1^*(x_2)-y_2^*(x_1)$ 一致，符号无误。
- p.96 / p.104，例 4.3.1 的流计算：$u=x/(1+t)$、$v=y$、$w=z-xyt/(1+t)$，时间 1 映射
  给出 $(x/2,y,z-xy/2)$，与 (4.20) 一致。

## 图目录（统一从扫描页 300 dpi 裁剪，置于 qsg/figures/）

| 文件 | 原书位置 | 说明 |
|---|---|---|
| `fig_p100_1.png` | p.92 | 引理 4.3.1 的交换图（无编号示意图） |
| `fig_p101_1.png` | p.93 | Figure 4.1 Darboux 定理 |
| `fig_p101_2.png` | p.93 | Figure 4.2 $V$ 上的辛结构 |
| `fig_p102_1.png` | p.94 | Figure 4.3 切触几何中的 Darboux 定理 |
| `fig_p105_1.png` | p.97 | Figure 4.4 管状邻域定理 |
| `fig_p106_1.png` | p.98 | Figure 4.5 $JTL$ 与 $TL$ 关于 $g_J$ 正交 |
| `fig_p108_1.png` | p.100 | Figure 4.6 乘积流形中 $f$ 的图像 |
