# ch04c 施工报告（pp.31–37，§4.5 + §4.6）

- **范围**：p031 起「4.5. Setup for the proof of Theorem 3.5.2.1」至 p037 末 §4.6.5（正则化迹与函数方程），§4.7 之前。含 4.5.1–4.5.6、4.6.1–4.6.6（引理 4.6.4.1、引理 4.6.6.4、注 4.6.5.1–4.6.5.3、例 4.6.5.1、注 4.6.6.1–4.6.6.3）。
- **内容摘要**：§4.5 定义 $\delta(t)=\prod_{\lambda\in R_X}\ch_{\check{\mathfrak g}}(t,\lambda)$（$W$-不变，诱导 $\check T/\!/W\to\AA^1$），构造 (4.8) 的交换图并在 $\LS^{\arthm,\circ}_{\check G}$ 上定义 $\delta_{\check G}$、在 $\LS^{\arthm,\circ}_{\check T}$ 上定义 $\delta_{\check T}$，把定理 3.5.2.1 化为 (4.9) 与 §4.5.6 的满射性。§4.6 用 K-理论类 $\cl$ 与范畴迹计算 $\tau^{\IndCoh}_{0,*}(\mathcal O_{B\check H})$ 与 $\mathcal O_{\LS^{\restr}_{\check H}}$ 的类比值：引理 4.6.4.1 断言两者相差 $\zeta^*_X(1)^{\dim H}$，证明经玩具模型 $V\times\Omega^0W$ 的 Koszul 复形、行列式比与 Grothendieck 迹公式，再沿中心列 $1=H_0\subset\cdots\subset H_r=H$ 归纳。§4.6.5 用正则化迹解释发散级数（例：$\sum\lambda^i$ 与 $1/(1-\lambda)$），§4.6.6 把 $H$ 换成 $S\ltimes H$ 得到 $\zeta^*_{X,H,S}$、$p_{X,H,S}$、$q_{X,H,S}$ 与引理 4.6.6.4。
- **编译**：`test_ch04c.tex`，xelatex exit 0，10 页，0 Overfull，0 Missing character。
- **技术处理**：$\check{\mathfrak g}$、$\mathfrak h$、$\Omega^{\infty-1}$、$\Omega^\infty\tr$、$\vol_{\check T}$ 逐符号核；$\zeta_X(t)=P_X(t)/((1-t)(1-qt))$ 与 $\zeta^*_X(t)=(1-t)\zeta_X(t)$ 核；Koszul 复形 (4.11)、行列式比 (4.12) 与中心列归纳按页面图重排；脚注 37–47 原样保留。
- **原文缺陷/疑难**：p033 引理 4.6.4.1 的 $\alpha$ 作用、$\Omega^\infty\tr_{\mathcal C}(\mathcal T)$ 记号照录；p035 例 4.6.5.1 中「$\lambda$ is an arbitrary element of the field $\lambda$」原文如此（$\lambda\in\e$ 与字段名 $\lambda$ 混用），照译并保留 `% [Tutor Note: 原文此处以 λ 兼指域元素与域本身，疑为笔误，按“域 e 的任意元素 λ”译]`。
- **遗留**：与 ch04d 在 p037/p038 交界，§4.7 起归 ch04d；合成后确认 4.5 六段、4.6 六段与引理 4.6.4.1/4.6.6.4 编号。
