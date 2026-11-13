# ch04a 译校报告

## 1. 覆盖范围
- chunk：`ch04a` = PDF p.194–222 = **原书 p.193–221**（29 页）
- 内容：第 4 章「希尔伯特空间上的算子」章首（p.193）+ §4.1 自伴算子（§4.1.1–§4.1.6，p.193–205）+ §4.2 谱定理（§4.2.1–§4.2.7，p.205–221）
- 文件：`src/chunks/ch04a.tex`（1865 行，汉字约 4.63 万）
- 小节：13 个 `\subsection`；`\section` 2 个（自伴算子 / 谱定理），各带一条 `\takeaway`
- 块界：开头即 `\chapter{希尔伯特空间上的算子}`，块首完整；文件末句「则 $\lambda_0$ 不再是 $A+\epsilon\chi_{\lambda_0}(A)$ 的谱点。」为原书 p.221 章末完整句，文件末尾已写
  `% [块界：本块止于原书 p.221（第 4 章末），下接原书 p.222，由 ch04b 承译。]`
- 页首标记 `% [原文 p.N]` 共 29 条，p.193–p.221 逐页齐全（无缺、无重）

## 2. 陈述环境编号（68 条，全部手工照抄原文，编号连续无缺）
| 编号 | 类型 | 页 | 编号 | 类型 | 页 |
|---|---|---|---|---|---|
| 4.1.1 | Definition | 193 | 4.2.1 | Definition | 205 |
| 4.1.2 | Definition | 194 | 4.2.2 | Definition | 205 |
| 4.1.3 | Example | 194 | 4.2.3 | Example | 205 |
| 4.1.4 | Definition | 195 | 4.2.4 | Proposition | 205 |
| 4.1.5 | Theorem（闭图像定理） | 195 | 4.2.5 | Proposition | 206 |
| 4.1.6 | Example | 195 | 4.2.6 | Theorem | 207 |
| 4.1.7 | Definition | 195 | 4.2.7 | Proposition | 207 |
| 4.1.8 | Proposition | 196 | 4.2.8 | Corollary | 208 |
| 4.1.9 | Example | 196 | 4.2.9 | Proposition | 208 |
| 4.1.10 | Definition | 197 | 4.2.10 | Example | 208 |
| 4.1.11 | Definition | 197 | 4.2.11 | Example | 209 |
| 4.1.12 | Proposition | 197 | 4.2.12 | Example | 209 |
| 4.1.13 | Example | 198 | 4.2.13 | Definition | 210 |
| 4.1.14 | Proposition | 199 | 4.2.14 | Definition | 210 |
| 4.1.15 | Corollary | 199 | 4.2.15 | Proposition | 210 |
| 4.1.16 | Proposition | 199 | 4.2.16 | Theorem | 210 |
| 4.1.17 | Example | 199 | 4.2.17 | Theorem（赫格洛茨表示） | 211 |
| 4.1.18 | Proposition | 200 | 4.2.18 | Definition | 212 |
| 4.1.19 | Proposition | 200 | 4.2.19 | Example | 212 |
| 4.1.20 | Proposition | 201 | 4.2.20 | Proposition | 212 |
| 4.1.21 | Definition | 201 | 4.2.21 | Theorem（谱定理） | 214 |
| 4.1.22 | Proposition | 202 | 4.2.22 | Definition | 215 |
| 4.1.23 | Definition | 203 | 4.2.23 | Proposition | 216 |
| 4.1.24 | Proposition | 203 | 4.2.24 | Theorem（谱定理—投影值测度） | 216 |
| 4.1.25 | Proposition | 203 | 4.2.25 | Proposition | 217 |
| 4.1.26 | Definition（亏指数） | 204 | 4.2.26 | Remark | 217 |
| 4.1.27 | Definition（凯莱变换） | 204 | 4.2.27 | Definition（谱的类型） | 217 |
| 4.1.28 | Proposition | 204 | 4.2.28 | Proposition | 217 |
| 4.1.29 | Proposition | 204 | 4.2.29 | Proposition | 218 |
| 4.1.30 | Example | 205 | 4.2.30 | Proposition | 218 |
| | | | 4.2.31 | Theorem（外尔判别法） | 218 |
| | | | 4.2.32 | Definition（紧算子） | 219 |
| | | | 4.2.33 | Example | 219 |
| | | | 4.2.34 | Proposition | 219 |
| | | | 4.2.35 | Proposition | 219 |
| | | | 4.2.36 | Example（施瓦茨核） | 220 |
| | | | 4.2.37 | Theorem（紧自伴算子） | 220 |
| | | | 4.2.38 | Proposition | 221 |

§4.1 共 30 条、§4.2 共 38 条，与原文英文清单逐条对应，无跳号、无自编号。

## 3. 公式核对（逐页回 150dpi 页图核对；关键式另做 300dpi 裁图）
- 伴随算子图：$\Gamma(A^*)=\{(\psi,\varphi)\mid\ip{\psi}{A\varphi}=\ip{A^*\psi}{\varphi}\}$ 与 $A\subseteq A^*$ 的定义式（p.195–196）
- 动量算子 $A=-\ii\frac{\mathrm d}{\mathrm dx}$、$\Dom(A)=H^1([0,1])$，边界项 $-\ii\varphi_1\overline{\varphi_2}\big|_0^1$（p.198）
- 亏指数 $d_\pm(A)=\dim\Ker(A^*\mp\ii)=\dim\Ran(A\pm\ii)^\perp$（p.204）
- 凯莱变换等距性 $\norm{(A+\ii)\varphi}=\norm{(A-\ii)\varphi}=\norm{A\varphi}+\norm{\varphi}$（平方意义，p.204）
- 预解恒等式 $R_A(z)-R_A(w)=(z-w)R_A(z)R_A(w)$、$\norm{R_A(z)}\le 1/\abs{\Imag z}$（p.206）
- 赫格洛茨表示 $m(z)=\int_\R\bigl(\frac{1}{\lambda-z}-\frac{\lambda}{1+\lambda^2}\bigr)\rd\mu(\lambda)$（p.211）
- 乘算子模型 $U^{-1}AU=M_\lambda$、$f(A)=U\bigl(\bigoplus_k M_{f(\lambda),\mu_k}\bigr)U^{-1}$、$A=\int_\R\lambda\,\rd\mathbb{P}_A(\lambda)$（p.214–217）
- 谱分类 $\sigma_{ess}(A)=\sigma(A)\setminus\sigma_{disc}(A)$ 及其两行 `aligned` 排法（p.217）
- 外尔序列 $\norm{\varphi_n}=1,\ \varphi_n\xrightarrow{w}0,\ (A-\lambda)\varphi_n\to0$；$\varphi_n\in\Ran\chi_{(\lambda-1/n,\lambda+1/n)}(A)\cap\Span\{\varphi_1,\cdots,\varphi_{n-1}\}^{\perp}$（p.218）
- 紧算子逼近 $\norm{G\varphi-\varphi_i}=\norm{P(A\varphi-\varphi_i)}<\epsilon$、$\norm{A-G}<2\epsilon$（p.220）
- 施瓦茨核估计 $\abs{(A\varphi)(\mathbf x)}^2\le\norm{\varphi}_{L^2}^2\int\abs{K}^2\rd\mathbf y$、$\norm{A}\le\norm{K}_{L^2(\R^{2n})}$（p.220）
- 紧自伴谱定理最后一步 $\abs{\lambda}-\epsilon\le\abs{\ip{\varphi_n}{A\varphi_n}}=\abs{\ip{\varphi_n}{(A-A_n)\varphi_n}}\le\frac1n$（p.221）
- 弱收敛一律记 $\varphi_n\xrightarrow{w}0$（原文 $w$ 在箭头上方），未用自定义宏。

## 4. 图
| 图 | 页 | 处理 |
|---|---|---|
| $\varphi_n$ 分段折线（红线，标注 $1$、$1/n$、$1$、$\varphi_n$） | 原书 p.195 | 裁切 `figures/fig_p196_a.png`，`width=0.34\textwidth`，注释 `% [图：原书 p.195，图内文字照原样保留]`；图内只有数学符号，无英文单词，故不重绘、不加 `\fignote` |
- `python tools\figtool.py auto 194 222` 全段仅检出这一张真图；其余括号、矩阵、箭头、根号延长线均为数学符号装饰，未嵌图（已逐页目检确认）。

## 5. 术语增补（详见 `work/term_requests_ch04a.md`，共 40 条）
- 本段新增重要的：可闭的（closable）、算子的闭包、亏指数（deficiency index）、有下界、凯莱变换、等距、本质值域、谱基、循环向量、赫格洛茨表示、里斯表示定理、概率测度、**指示函数（characteristic function of a set，避免与 eigenfunction 本征函数混淆）**、极化恒等式、孤立点、聚点、常投影、外尔判别法/外尔序列、一致有界性定理、双边理想、有限秩、相对紧、对角线论证、施瓦茨核、柯西–施瓦茨不等式、紧扰动。
- 表内已有并严格照用：self-adjoint 自伴的、symmetric 对称算子、essentially self-adjoint 本质自伴的、adjoint 伴随、unitary 酉的、projection 投影、spectral measure 谱测度、projection-valued measure 投影值测度、Borel 博雷尔、spectral theorem 谱定理、resolvent 预解式、domain 定义域、densely defined 稠密定义的、compact operator 紧算子、essential spectrum 本质谱、point spectrum 点谱。

## 6. 编译自检
```
cd <本地路径>
powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch04a

LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch04a.pdf   (33 页)
```
- `python tools\lint.py ch04a`：`OK ch04a  汉字 46254  节 2 小节 13 陈述 68 公式 281 图 1(TikZ 0) 批注 2`，问题 0 条。
- 已把 `work\tmp_ch04a.pdf` 逐页转图抽查（`work\preview\ch04a_*.png`）：章标题、陈述头、`\takeaway` 框、图、长对齐式均正常，无溢出页边，中文标点全角。
- 说明：单块编译时章号/节号从 1 起算（页眉显示「1.2 谱定理」「第 1 章」），合书由 Lead 统一，不影响内容。

## 7. Tutor Note（2 条，均≤120 字）
1. p.196 例 4.1.9 中原文写 `$\forall\varphi\in\Dom(A)$`，但该例只出现 $M_f$、$A$ 未定义，按上下文应为 $\Dom(M_f)$。
2. p.220 命题 4.2.35 证明中原文写 relatively bounded（相对有界），按论证（$A(W)$ 相对紧、$B$ 连续）应为 relatively compact（相对紧），译文照录原文。

## 8. 存疑（均照录原文，未擅改数学内容）
1. p.195 定义 4.1.4 末句「此时 $\overline A$ 称为 $A$ 的闭包」中，原文把 $\overline A$ 写成 $A$；译文按最合理读法写 $\overline A$。
2. p.203 命题 4.1.25 证明中 $\Ker(A^*-(z+\epsilon))$ 原文漏共轭横线（应为 $A^*-\bar z-\epsilon$ 一类），译文照录 `A^*`。
3. p.211 定理 4.2.17 证明中的模长等式：
   $\abs{\frac{1+\lambda \ii y}{\ii y(\lambda-\ii y)}}=\sqrt{\frac{1+\lambda^2y^2}{y^2+\lambda^2y^2}}$，
   分母按原式化简易得 $y^2(1+\lambda^2)$，与原书根号内分母 $y^2+\lambda^2y^2$ 不完全一致，疑为原文笔误；照录，未改。
4. p.219 命题 4.2.35 证明中「$A(W)$ 相对有界」疑为 relatively compact 之误，见上 Tutor Note 2。

## 9. 遗留
- 无。本块已完成，`ch04b` 自原书 p.222（PDF 223）起译，与本块不重叠。
