# 第 6 章「定量刻画」疑误记录（review_ch06.md）

记录范围：PDF p.149–p.179（印刷页 141–171）。每条给出原文、所在页（印刷页 / PDF 页）、
疑点与建议改法。均已在正文对应位置以 `% [Tutor Note: 原文疑误 ...]` 标注，译文保留
原文写法，未擅自改动。

| # | 印刷页 / PDF 页 | 原文（摘录） | 疑点 | 建议 |
|---|---|---|---|---|
| 1 | p.144 / PDF p.152 | "to control the Hofer norm of the **communicator** $[\cdot,\cdot]$" | 数学上应为「换位子」commutator；communicator 无此义。 | 改为 "commutator"。 |
| 2 | p.146 / PDF p.154 | 例 6.1.3："if $M$ contains a Darboux ball $U$ of radius $3r$ (i.e. $U$ is $B^{2n}(3r)$), then ... $e(U)=\pi r^2$" | 与同例前半的 $e(B^{2n}(r))=\pi r^2$ 及注 6.1.4 的辛同胚不变性矛盾：应得 $e(U)=e(B^{2n}(3r))=9\pi r^2$。 | 疑为「半径 $3r$ 的 Darboux 球中半径 $r$ 的球（而非整个 $U$）满足 $e=\pi r^2$」；或把 $3r$ 误写。请核对 [221]。 |
| 3 | p.159 / PDF p.167 | 关键观察前："for the contact 1-form $\alpha(=\iota_{\lambda_{\mathrm{std}}}|_{\partial W})$" | 记号 $\iota_{\lambda_{\mathrm{std}}}$ 无定义；本节前文刚定义 $\alpha=\lambda_{\mathrm{std}}|_{\partial W}$，此处 iota 疑为 lambda 之误。 | 改为 $\alpha(=\lambda_{\mathrm{std}}|_{\partial W})$。 |
| 4 | p.167 / PDF p.175 | 例 6.3.5："when restricted at **grading 1** ... the barcode of $\mathbb{V}_W$ at **degree 0** is $\mathbb{B}(\mathbb{V}_W)|_{*=1}=\{(-\infty,0]\}$" | 前后不一致：同一句先称 grading 1，后称 degree 0，而记号 $\mathbb{B}(\mathbb{V}_W)|_{*=1}$ 与下文「grading covers $1,3,5,\cdots$」都指次数 1。 | "degree 0" 应为 "degree 1"。 |
| 5 | p.169 / PDF p.177 | 式 (6.25)：$\ln c_{\mathrm{SH}}(W)=$ "the most **left** endpoint of the intervals in the lowest degree in barcode $\mathbb{B}(\mathbb{V}_W)$" | 与随后计算 $c_{\mathrm{SH}}(B^{2n}(1))=e^{\ln 1}=1$ 矛盾：由例 6.3.5，最低次数区间为 $(-\infty,\ln r]$，其最左端点为 $-\infty$，只有取有限端点（右端点）$\ln r$ 才得 $e^{\ln r}=r$。例 6.4.1 交换图中也写作 "the left end point"。 | 疑为 "the most right endpoint"（或条形码过滤轴方向约定相反）。请核对原文/原图。 |
| 6 | p.168–169 / PDF p.176–177 | 定义 6.4.1 (c2)：$c(\lambda U)=\lambda c(U)$，$\lambda U:=\{\sqrt{\lambda}\cdot x\mid x\in U\}$；命题 6.4.1 证明中却用 $c(B^{2n}(r))=r\,c(B^{2n}(1))$、$w_G(\lambda U)=\sup\{\lambda r'\}=\lambda w_G(U)$ | 量纲不自洽：按 (c2) 的定义，$\lambda U=\{\sqrt\lambda x\}$ 使长度按 $\sqrt\lambda$ 缩放，故 $B^{2n}(r)=r^2 B^{2n}(1)$，应有 $c(B^{2n}(r))=r^2c(B^{2n}(1))$；同理 $w_G(\lambda U)=\sqrt{\lambda}\,w_G(U)$，$\sup$ 中应为 $\sqrt{\lambda}r'$ 而非 $\lambda r'$。全书其他处（例 6.1.3、$c_{\mathrm{SH}}(B^{2n}(1))=1$）又用「容量 = 半径」约定。 | 需统一约定：或取 $\lambda U=\{\lambda x\}$ 且 $c$ 为「面积型」，或保留 $\{\sqrt\lambda x\}$ 而把 $c(B^{2n}(r))=r^2c(B^{2n}(1))$ 与 $\sqrt\lambda$ 写对。建议核对原书此段。 |
| 7 | p.171 / PDF p.179 | "a work from Abbondandolo-**Editmar**-Kang [3]" | 作者姓名疑误：相关作者应为 O. Edtmair（Edtmair, 拼作 E-d-t-m-a-i-r）。 | 改为 "Abbondandolo-Edtmair-Kang"，并核对参考文献 [3]。 |
| 8 | p.151 / PDF p.159 | 例 6.2.5 证明中 "the second equality comes from (6.3) in **Example 6.2.3**" | (6.3) 实际陈述于**事实 6.2.2**；例 6.2.3 只是在其后应用 (6.3)，并未陈述该式。 | 改为 "Fact 6.2.2 中的 (6.3)"。 |

## 非疑误、但已加 Tutor Note 提示的易错点（不在此表重复）

- 定义 6.1.1 的两重下确界与 $H\mapsto H+c(t)$ 不影响 $\|H\|_{\mathrm{Hofer}}$；
- $d_{\mathrm{Hofer}}(\varphi,\psi)=\|\varphi^{-1}\psi\|$ 的次序与双不变性；
- 定理 6.1.2 证明中「$A$ 内部非空 ⇒ 存在支撑在 $A$ 中不交换的 $\varphi,\psi$」；
- 注 6.1.5（Usher）中 $\max/\min$ 由 $M$ 改为 $A$；
- (6.11)–(6.12) 的符号约定与 $f^*\dd\alpha\ge0$ 的推导；
- 命题 6.3.1 的极值原理证明与 (6.15) 的边界定向；
- 例 6.3.3 的斜率窗口 $-4<-\pi/(1-\varepsilon)<-\pi$ 在 $\varepsilon<1-\pi/4$ 时自洽；
- Viterbo 同构 (6.23) 中能量阈值 $\frac{a^2}{2}$ 的来源；
- ECH 容量、$N(a,b)$ 与四维嵌入问题。
