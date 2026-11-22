# ch04b 施工报告（pp.29–31，§4.3 + §4.4）

- **范围**：p029 起「4.3. Non-resonance」至 p031 末 §4.4 证明（4.4.6）结束。含 4.3.1–4.3.3、注 4.3.1.1、记号 4.3.2.2、定理 4.3.3.1、4.4.1（引理 4.4.1.1 判别准则）、4.4.2–4.4.6（形式 étale、稳定化子、提升同构类、$H^\circ$ 平凡性）。
- **内容摘要**：定义 $R_X\subset\e^\times$ 为 Frobenius 在 $H^1_\et(X,\e)\oplus H^2_\et(X,\e)$ 上的特征值集（$1\notin R_X$，$q\in R_X$）；对 $H$ 的有限维表示定义 $\ch_V: H^{ad}/H\times\AA^1\to\AA^1$，开集 $(H^{ad}/H)^{\nonres}$ 由 $\prod_{\lambda\in R_X}\ch_{\mathfrak h}([h],\lambda)\neq0$ 刻画。定理 4.3.3.1：$\tau_H$ 在非共振开集上是同构。§4.4 用「形式 étale + $\e$-点上 1-群胚同构」判别，切复形计算给出形式 étale 等价于非共振；再用 Zariski 闭包 $H^\circ$、$\theta=\Ad_{\rho(F)}$ 与 (4.6)(4.7) 证明 $H^\circ$ 平凡，从而本质满。
- **编译**：初编译 pgf 报 `No shape named tikz@f@3-1-5`，且 `\pnum` 计数 11（应为 9）；删去 4.4.3 切复形段与 4.4.6 $V$ 论证段两处误加的 `\pnum{}` 后 exit 0、5 页、0 Overfull，编号对齐（4.3.1–3、4.4.1–6）。
- **技术处理**：引理 4.4.1.1 的 (ii1)(ii2) 用 enumerate；切复形 $C_{\et}(X,\mathfrak h_\sigma[1])^\ZZ$、$\Ker(\id-\varphi_\sigma)$ 逐符号核；(4.6)(4.7) 的 $\rho_0(Fg)=\theta(\rho_0(g))$、$\rho_0(Fg)=\lambda\rho_0(g)$ 对图核。
- **原文缺陷/疑难**：p029 注 4.3.1.1 引 Weil 猜想「$q\in R_X$」处原文括注「though this is not relevant for us」照译；p030 引理 4.4.1.1 的「locally almost of finite type」按「局部几乎有限型」。
- **遗留**：与 ch04c 在 p031 交界，§4.5 起归 ch04c；合成后确认 4.3.3.1 出现在 p029 之后、编号定理 4.3.3.1 正确。
