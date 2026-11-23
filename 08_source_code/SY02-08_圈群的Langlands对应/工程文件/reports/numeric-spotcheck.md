# 数值/符号抽查报告（U13 后续任务）

- 抽查对象：`tex/chapters/ch09-2.tex`（U13/ch03b 译）5 个编号公式；`tex/chapters/ch09-1.tex`（U12 译）3 个编号公式。
- 方法：先从 `.tex` 读出公式源码，再对 `pages/pNNN.png` 做 2.0–3.4 倍局部放大，逐符号比对（上下标、check 记号、指数 ±、指标 α 与 i、括号层级、丛/代数的字母）；**未修改任何 `.tex`**。
- 图像页号一律为 PDF 页号（印刷页 = PDF 页 − 14）。

## 抽查结果

| 公式号 | 图像页 | 结论 | 备注 |
|---|---|---|---|
| (9.5-4) | p295（印刷 281） | 一致 | 图像：$\operatorname{ch}W^w_\lambda=e^{w(\lambda+\rho)-\rho}\prod_{\alpha\in\hat\Delta_+}(1-e^{-\alpha})^{-\operatorname{mult}(\alpha)}$。上标 $w(\lambda+\rho)-\rho$、指数 $-\alpha$、幂 $-\operatorname{mult}(\alpha)$、指标集 $\hat\Delta_+$（带 hat）逐一吻合。 |
| (9.6-5) | p301（印刷 287） | 一致 | 3×3 交换图。第 1 行 $(\mathbb{M}_\lambda)^{\hat{\mathfrak{n}}_+}_\lambda\to(\mathbb{V}_\lambda)^{\hat{\mathfrak{n}}_+}_\lambda\to(W_\lambda)^{\hat{\mathfrak{n}}_+}_\lambda$；第 2 行三个 $\operatorname{End}_{\hat{\mathfrak{g}}_{\kappa_c}}$；第 3 行 $\operatorname{Fun}\Op^{\mathrm{nilp},\lambda}_{{}^LG}\to\,?\to\operatorname{Fun}\operatorname{Conn}(\Omega^{-\rho})^\lambda_D$（底行中项原书即印“?”，未补）；六条竖箭头均标 $\simeq$。下标 $\lambda$、上标 $\hat{\mathfrak{n}}_+$、$\mathrm{nilp},\lambda$ 不带 check 均一致。 |
| (9.6-8) | p303（印刷 289） | 一致 | 上图：$(\mathbb{V}_\lambda)^{\hat{\mathfrak{n}}_+}_\lambda\longrightarrow\operatorname{Fun}\operatorname{Conn}(\Omega^{-\rho})^\lambda_D$，下排 $(\mathbb{V}_\lambda)^{\hat{\mathfrak{n}}_+,0}_\lambda\longrightarrow\operatorname{Fun}\Op^{\check\lambda}_{{}^LG}$，两条竖箭头朝上（单射）。$(\hat{\mathfrak{n}}_+,0)$ 的逗号/加号位置、$\lambda$ 下标、右列 $\check\lambda$ 的 check 均一致。 |
| (9.6-16) | p306（印刷 292） | 一致 | 图像：$\prod_{\check\alpha\in\hat\Delta_+}\frac{1-q^{\langle\check\alpha,\lambda+\rho\rangle}}{1-q^{\langle\check\alpha,\rho\rangle}}\prod_{i=1}^{\ell}\prod_{n_i\ge d_i+1}(1-q^{n_i})^{-1}$。内积用 $\check\alpha$、$\lambda+\rho$ 为加号、$n_i\ge d_i+1$（非 $d_i$）、指标集 $\hat\Delta_+$ 与原书一致。原书此处 $\hat\Delta_+$ 疑为 $\Delta_+$ 之笔误，已在 `reports/U13.md` 登记；抽查结论是“译文与图像一致”。 |
| (9.6-22) | p312（印刷 298） | 一致 | 图像：$\operatorname{ch}V_\lambda=\prod_{\check\alpha\in\hat\Delta_+}\frac{1-q^{\langle\check\alpha,\lambda+\rho\rangle}}{1-q^{\langle\check\alpha,\rho\rangle}}$。分母 $\langle\check\alpha,\rho\rangle$、分子指数 $\lambda+\rho$、指标集 $\hat\Delta_+$ 均一致。 |
| (9.2-3) | p268（印刷 254） | 一致 | 图像：$\nabla=\partial_t+t^{-1}(p_{-1}+\mathbf{v}(t))$，$\mathbf{v}(t)\in\check\mu(t)\mathfrak{b}[[t]]\check\mu(t)^{-1}$，$\mathbf{v}(0)=-\check\mu$。$t$ 的指数为 $-1$、$\check\mu$ 的 check、$\mathfrak{b}$ 为哥特体、$\mathbf{v}(0)$ 的负号均一致。 |
| (9.3-6) | p276（印刷 262） | 一致 | 图像：$\mu^{-1}\bigl(\Op^{\mathrm{RS}}_G(D)_{\varpi(-\check\lambda-\check\rho)}\bigr)=\bigsqcup_{w\in W}\operatorname{Conn}(\Omega^{\check\rho})^{\check\rho-w(\check\lambda+\check\rho)}_D$。留数 $\varpi(-\check\lambda-\check\rho)$、上标 $\check\rho-w(\check\lambda+\check\rho)$（$\check\rho,\check\lambda$ 均带 check，$w(\cdot)$ 内为加号）、$\bigsqcup$ 均一致。 |
| (9.3-13) | p282（印刷 268） | **不一致（需更正 ch09-1.tex）** | 图像：$\mathcal{F}'_H\simeq w_0^*\bigl(\Omega^{\check\rho}(\check\rho-w(\check\lambda+\check\rho))\bigr)$。`ch09-1.tex` 现作 `\mathcal{F}'_H\simeq w_0^*(\mathcal{F}_H(\check\lambda+\check\rho)-w(\check\lambda+\check\rho))`。三处不同：① 丛为 $\Omega^{\check\rho}$（非 $\mathcal{F}_H$）；② 扭转余权为 $(\check\rho-w(\check\lambda+\check\rho))$（不是先在 $\check\lambda+\check\rho$ 上取 $\mathcal{F}_H$ 再减）；③ 括号层级应为 $w_0^*(\Omega^{\check\rho}(\text{coweight}))$，现写法把“$-w(\cdots)$”放在丛外。建议改为：`\mathcal{F}'_H\simeq w_0^*\bigl(\Omega^{\check\rho}(\check\rho-w(\check\lambda+\check\rho))\bigr)`。交叉验证：同页下一行“induced connection on $\Omega^{\check\rho}$ … $\operatorname{Conn}(\Omega^{\check\rho}(\check\rho-w(\check\lambda+\check\rho))_D\simeq\operatorname{Conn}(\Omega^{\check\rho})^{\check\rho-w(\check\lambda+\check\rho)}_D$”与图像一致，可确证该式。 |

## 其他发现（非抽查项，供参考）

1. **定理类编号已与原书对齐**：按 Lead 新改的“单一共享计数器 + `[section]`”，重跑 `check.ps1` 后 `ch09-2` 打印的编号陈述为：§9.4 命题 9.4.1、9.4.2；§9.5 命题 9.5.1、引理 9.5.2、定理 9.5.3；§9.6 定理 9.6.1、引理 9.6.2、命题 9.6.3、9.6.4、9.6.5、定理 9.6.6、命题 9.6.7——与原书逐一吻合（本片段独立编译时章号为 0，合成后为 9）。`ch09-1` 的 §9.3 贡献 6 个编号陈述（9.3.1–9.3.6），`ch09-2` 开头的接续段贡献第 7 个（定理 9.3.7），同样吻合；两文件均 `CHECK OK`。
2. `ch09-1.tex` 中 `\Op^{RS}` 作斜体上标（如 (9.3-6)），原书印作直立体 RS；仅排版差异，不影响数学内容，若统一风格可改为 `\Op^{\mathrm{RS}}`。
3. 抽查中未发现 `ch09-2.tex` 有符号错误；5/5 一致。`ch09-1.tex` 抽查 3 个，2 个一致、1 个（(9.3-13)）需更正。

## 自检

- 三个被抽查的 `ch09-1` 公式所据图像页分别为 p268、p276、p282；五个 `ch09-2` 公式为 p295、p301、p303、p306、p312，与正文 `\tag` 逐一对应。
- 未修改任何 `.tex` 文件；本报告为唯一新增文件。
