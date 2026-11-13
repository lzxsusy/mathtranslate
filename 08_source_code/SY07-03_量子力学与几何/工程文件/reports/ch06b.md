# ch06b 译校报告（译者：tr04）

## 1. 覆盖范围
- chunk：`ch06b` = PDF p.314–334 = **原书 p.313–333**
- 内容：定理 6.2.10（费多谢夫）及证明 + §6.3 泊松流形（6.3.1 多向量场、6.3.2 泊松流形与泊松上同调、6.3.3 孔采维奇的星乘积）+ §6.4 迹映射（6.4.1 微分分次代数、6.4.2 量子 HKR 映射、6.4.3 费多谢夫阿贝尔联络的扭转、6.4.4 迹映射与指标）+ 第 6 章章末回顾
- 文件：`src/chunks/ch06b.tex`（约 1330 行，33 KB）
- 块界：块首即定理 6.2.10 陈述（原书 p.313 页首），无半句残段；§6.2.5 全球化全部正文在 `ch06a`（块尾止于原书 p.312 的 $(\Gamma_D^{\mathrm{flat}}(M,W),*)\overset{\sim}{\to}(C^\infty(M)[[\lambda]],*_D)$），**无重复**。块尾止于原书 p.333 完整句「……单圈图。」，`\chapterreview` 收束第 6 章，**全书正文在本块结束**。

## 2. 陈述环境编号（全部手工照抄原文，共 38 个）
| 编号 | 原书页 |
|---|---|
| Theorem 6.2.10（费多谢夫） | 313 |
| Definition 6.3.1；Proposition 6.3.2 | 313、314 |
| Definition 6.3.3；Proposition 6.3.4 | 314、315 |
| Example 6.3.5；Example 6.3.6（常值泊松结构） | 315 |
| Example 6.3.7（线性泊松结构）；Definition 6.3.8；Example 6.3.9 | 316 |
| Example 6.3.10 | 317 |
| Definition 6.3.11；Example 6.3.12、6.3.13、6.3.14 | 318 |
| Example 6.3.15；Theorem 6.3.16（孔采维奇） | 319、320 |
| Definition 6.4.1；Example 6.4.2、6.4.3 | 322 |
| Definition 6.4.4；Definition 6.4.5；Proposition 6.4.6；Definition 6.4.7 | 323、324 |
| Proposition 6.4.8 | 325 |
| Definition 6.4.9；Lemma 6.4.10 | 326 |
| Definition 6.4.11；Proposition 6.4.12 | 327 |
| Definition 6.4.13；Proposition 6.4.14 | 330 |
| Definition 6.4.15；Remark 6.4.16；Proposition 6.4.17 | 331 |
| Proposition 6.4.18；Definition 6.4.19；Remark 6.4.20；Theorem 6.4.21 | 332 |

共 3 定理、12 定义（6.3.1、6.3.3、6.3.8、6.3.11、6.4.1、6.4.4、6.4.5、6.4.7、6.4.9、6.4.11、6.4.13、6.4.15、6.4.19）、7 命题、1 引理、2 注、13 例。原文形如 "Theorem 6.2.10 (Fedosov)."、"Example 6.3.6 (Constant Poisson Structure)." 的 4 个人名/别名并入环境参数（`\begin{theorem}{6.2.10（费多谢夫）}`、`{6.3.6（常值泊松结构）}`、`{6.3.7（线性泊松结构）}`、`{6.3.16（孔采维奇）}`），以复现原排法；`crosscheck.py` 已核对编号与结构一致。

## 3. 公式核对
逐页回页面图像核对（p314–p334 全页 150 dpi），关键式另做 300 dpi 裁图（`work/review/` 下 chk 系列）：
- 费多谢夫定理证明：$f*_D g=\sigma(\sigma^{-1}(f)*\sigma^{-1}(g))=fg+O(\lambda)$、$\frac1\lambda[f,g]_{*_D}=\sigma\bigl(\sum\omega^{ij}\frac{\partial\sigma^{-1}f}{\partial y^i}\frac{\partial\sigma^{-1}g}{\partial y^j}+O(\lambda)\bigr)$（p.313）
- 斯豪滕–奈恩黑斯括号 $[X_1\wedge\cdots\wedge X_m,Y_1\wedge\cdots\wedge Y_n]_{\mathrm{SN}}$ 的 $(i,j)$ 双重求和与帽子记号（p.314）
- 命题 6.3.4 证明的四步链：$\{\{f,g\}_P,h\}_P+\text{cyclic}=\sum P^{ij}\partial_i(P^{kl}\partial_kf\partial_lg)\partial_jh+\text{cyclic}=\cdots=\bigl(\tfrac12\sum P^{ij}\partial_iP^{kl}\partial_k\wedge\partial_l\wedge\partial_j\bigr)(df\otimes dg\otimes dh)=([P,P]_{\mathrm{SN}})(df\otimes dg\otimes dh)$（p.315）
- 定理 6.3.16 的图展开 $\sum_{\Gamma}\frac{\lambda^n}{n!}B_\Gamma$、权 $W_\Gamma$ 与 $S[X,\eta]=\int_H\eta_idx^i+\tfrac12\int_HP^{ij}(x)\eta_i\wedge\eta_j$（p.320–321）
- $S^1$-关联映射的长式：四行 `align*`，指数用 `\exp\Bigl(...\Bigr)`，末行 $f_0(y)\cdots f_m(y)\big|_{y^{(1)}=\cdots=y^{(m)}=y}$（p.326）
- $\widehat d=\sum_i dy^i\frac{\partial}{\partial y^i}$、$\rho^\lambda(f_0\otimes\cdots\otimes f_m)=\frac1{m!}\langle f_0\otimes\widehat df_1\otimes\cdots\otimes\widehat df_m\rangle_{S^1}$（p.327）
- $\Delta=\sum\omega^{ij}(x)\frac{\partial}{\partial y^i}\iota_{\partial_{y^j}}$、$D=\nabla+\frac1\lambda[\gamma,-]_*$、$e^{-\Lambda_{\gamma/\lambda}}(\nabla+b)e^{\Lambda_{\gamma/\lambda}}=D+b-\frac1\lambda\Lambda_{R_\omega^\nabla+\omega_\lambda}$（p.328–330）
- 别列津积分 $\int_{\mathrm{Ber}}s:=\frac1{n!}\bigl(\tfrac12\sum\omega^{ij}\iota_{\partial_{y^i}}\iota_{\partial_{y^j}}\bigr)^n s\big|_{y^i=0,dy^i=0}$、$\operatorname{Tr}(s):=\int_M\int_{\mathrm{Ber}}\rho_D^\lambda(s)$（p.331–332）
- 定理 6.4.21 与代数指标定理 $\operatorname{Tr}(1)=\int_Me^{-\omega_\lambda/\lambda}\widehat A(M)$（p.332–333）

页标记：源文本页标记是 PDF 页，已统一减去 1 改为原书页；补齐原先缺的 p.318（`align*` 内 `&=-d(\sum\omega_{ki}dx^i)\\` 与 `&=d\varphi(\partial_{x^k})` 之间）、p.322、p.323，现 313–333 共 **21 个页标记连续无缺口**。

## 4. 图
`python tools\figtool.py auto 314 334` 得 5 张候选，逐张 read_image 判定：
| 文件 | 来源页 | 处理 |
|---|---|---|
| `figures/fig_p320_a.png` | 320 | 裁切 PNG（宽 0.68\textwidth），两张树图并排 |
| `figures/fig_p321_a.png` | 321 | 裁切 PNG（宽 0.75），图序列 $f$—$g$、单 $P$、双 $P$、$\cdots$ |
| `figures/fig_p321_b.png` | 321 | 裁切 PNG（宽 0.42），双圈图 |
| `figures/fig_p326_a.png` | 326 | 裁切 PNG（宽 0.30），圆周上 $\theta_0,\theta_1,\theta_2,\theta_m$ 循环次序 |

4 张均为纯几何线条、图内无英文整句，保留原图不重绘，图后均写 `% [图：原书 p.N，图内文字照原样保留]`，**无题注**。
另：p.330、p.331 两个交换图（$\Omega^\bullet(M,W)\xrightarrow{\rho^\lambda}\cdots$ 与 $(\Omega^\bullet(W),D+b)$ 的方块）用行内 `tikzpicture` 按原图重绘，不计入图清单。

## 5. 术语增补（已记 `work/term_requests_ch06b.md`）
| 英文 | 译法 | 页 |
|---|---|---|
| Schouten–Nijenhuis bracket | 斯豪滕–奈恩黑斯括号 | 314 |
| Schouten bracket | 斯豪滕括号 | 314 |
| polyvector field | 多向量场 | 313 |
| Poisson bivector | 泊松双向量 | 314 |
| Lichnerowicz complex / cohomology | 利赫内罗维奇复形／上同调 | 316 |
| Lie–Poisson structure | 李–泊松结构 | 316 |
| quantum HKR map | 量子 HKR 映射 | 327 |
| Weyl bundle | 外尔丛 | 328 |
| formal Weyl algebra | 形式外尔代数 | 326 |
| Berezin integral | 别列津积分 | 331 |
| BV operator | BV 算子 | 328 |
| Darboux coordinates | 达布坐标 | 321 |
| differential graded algebra (DGA) | 微分分次代数 | 322 |
| Hochschild chain complex | 霍赫希尔德链复形 | 323 |
| Maurer–Cartan element / equation | 毛雷尔–嘉当元素／方程 | 324 |
| twisting | 扭转 | 324 |
| Fedosov abelian connection | 费多谢夫阿贝尔联络 | 328 |
| Nest–Tsygan | 涅斯特–齐甘 | 333 |
| correlation (S¹-correlation) | 关联（S¹-关联） | 326 |
| flat section | 平坦截面 | 328 |
| gluing | 粘合 | 329 |

沿用术语表：泊松流形／结构／代数、辛流形、形变量子化、星乘积（star product）、霍赫希尔德上同调、格斯坦哈伯括号、微分分次李代数、毛雷尔–嘉当方程、孔采维奇、费多谢夫、迹映射、迹泛函、循环上同调、托德类、$\hat A$ 亏格、指标定理。Moyal 一词术语表注「保留」，正文作「Moyal 乘积」「Moyal 星乘积」。

## 6. Tutor Note
本块未加 Tutor Note（源文未发现需要提示的笔误或记号冲突）。两处版式判断记录于此而非正文批注：
1. `\paragraph{...}` 在 book 类中是 run-in 标题，会与紧随的陈述环境并排成「泊松流形 定义 6.3.3.」；原书这些标题（Poisson Manifold、Kontsevich's Star Product、Twisting Construction、Local Case、Global Case 等）均独占一行，故 9 处 `\paragraph{...}` 后一律补 `\par`。
2. 源文 "Berezin integral" 原文即用 `∫_Ber` 记号，中文作「别列津积分」，符号照抄。

## 7. 存疑
- 原书 p.329 引理「$\widehat d$ 与 Moyal 乘积相容」的表述在原书中较简，正文按原意直译，未补充论证。
- 原书 p.333 末段提到 "one-loop"（单圈），中文作「单圈图」，与术语表「单圈」一致。
- 本块草稿 standalone 编译时 §6.3 显示为 0.1（无 `\chapter`），合书后应为 6.3，属预期。

## 8. 编译自检
```
powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch06b
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch06b.pdf   (24 页)
python tools\lint.py ch06b  →  OK ch06b 字符 33169 节 2 小节 7 陈述 38 公式 148 图 4(TikZ 2)；合计：问题 0 条，提示 0 条
python tools\crosscheck.py ch06b → 原节=9 译节=9 页标=21 陈述=38；OK 结构与编号一致
```
首轮唯一问题是定义 6.4.9 的长 `align*` overfull 64.07 pt，拆成 4 行后清零。已渲染 `work/preview/ch06b_1..24.png` 逐页目检：公式与原书一致、无溢出页边、全角标点正常、4 张裁图清晰、2 个交换图位置正确、`\takeaway` 与 `\chapterreview` 版式正常。

## 9. 状态
**完成并通过自检**（2026-11-07，Lead 复跑验收通过）。第 6 章（全书正文）在本块结束。
