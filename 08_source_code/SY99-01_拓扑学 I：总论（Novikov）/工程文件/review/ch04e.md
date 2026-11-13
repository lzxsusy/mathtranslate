# 核验报告 · ch04e（原书 p.187–p.202）

核验人 tr-ji ｜ 作者 tr-wu ｜ 2026-11-10

## 结论

需修改（3 条必须改：块末跨页句未完；4 处页标记插在句中；1 处术语违 glossary。另有 4 条建议改）

## 必须改（影响正确性）

1. **块末跨页句未完**（→ `ch04e.tex` 第 447 行末）。原书 p.202 末句是 `Hence the infinite portions of the homotopy groups of any simply-connected manifold`，在 p.203 续为 `can be obtained rather elementarily from the algebra Λ*(M^n) …`。按跨页句归起始页所在块的规则，ch04e 应在块末把全句写完整，即把 `ch04f.tex` 第 2 行的前半句（「可以相当初等地由 $M^n$ 上形式构成的代数 $\Lambda^*(M^n)$ 得到」）并入本块，ch04f 改从下一句「此结果可看作 de Rham 定理（见前文）的同伦论类比。」起。现在 ch04e 以半句收尾、ch04f 又以半句开头，两块都不自足。

2. **4 处页标记插在句中**（→ `ch04e.tex` 第 35、228、341、360 行）。核对原书：p.187 末句「……光线沿最短时间的路径」在 p.188 续为「传播的原理……」；p.194 末「……它们由」在 p.195 续为「「周期」给出。」；p.198 末「（我们可以写」在 p.199 续为「作 $H_j(\tilde M;[\omega])$」；p.199 末「……用于」在 p.200 续为「得到不等式 (2.58) 的同调群……」。这四处的标记都落在句子中间，LaTeX 会在该处另起一段，印出来就是「……的路径」后面换段缩进再「传播的原理」，正是 lead 明令禁止的「禁插句中」。`audit_pagemarks.py` 抓不到它们，因为标记前一行是空行（该脚本把空行一律判为合法）。改法：把标记移到最近的句界之后（第 36 行那句闭合括号之后再放 p.188），其余三处同理移到句号之后。

3. **术语违 glossary**（→ `ch04e.tex` 第 102 行）：「其中 $\Sigma$ 表示双角锥（suspension）」——`work/glossary.tsv` 定 suspension = 悬挂，全书统一用「悬挂」。同块 p.190 的 (2.45) 与该句同处，改一处即可。

## 建议改

1. **$H_j(M;K^+)$ 被悄悄改成 $H_j(\tilde M;K^+)$**（→ `ch04e.tex` 第 339 行两处、第 356 行）。原书 p.198 末与 p.199 都印作 $H_j(M;K^+)$、$H_j(M;K^+_\kappa)$（无波浪号），而同一页下文又印 $H_j(\hat M;K^+)$，原书自身不一致。译文一律取 $\tilde M$，读者是读得通的，但按「原书笔误照排 + 批注」的规则，宜照原书印 $M$，同时在批注里指出「原书此处作 $M$，按上下文（链复形取自 $\tilde M$）应为 $\tilde M$」。
2. **脚注 3 人名拼法未注**（→ 第 356 行脚注）：原书印 `Sirokav`（通行拼法 Sirakov），译文照录是对的，但宜补一句「原书拼作 Sirokav」。
3. **脚注 5 人名拼法未注**（→ 第 406 行脚注）：原书印 `A. Salomon`、`Rabinovich`（通作 Salamon、Rabinowitz）。该脚注已为 `Chern--Simon` 加了注，这两个人名建议一并注出，体例才一致。
4. **例 1、例 2、例 3 用 `\para{例 N.}` 而非 example 环境**（→ 第 262、264、290 行）。原书这三段是同一体例的 `Examples. 1./2./3.`，而 ch04d 的同名结构用的是 `example{1}`…`example{4}`。两块处理不一致，建议由 lead 裁定统一口径（本块例 3 末尾的手写 `\hfill$\square$` 已正确补上原书的 □，若改环境则改用 `example*` 之外的写法需一并调整）。

## 抽查记录

体例抽查：16 个页标记（187–202，递增无重复）；31 个编号公式 (2.36)–(2.66)，连续、无重号、无自造；陈述环境 2 个（p.191 `remark`，原书有 □，用无星版 ✓；p.193 `example`，原书有 □，用非星版且 □ 落在原书位置 ✓）；Tutor Note 7 条（≥ 16/3）；`python work/check_chunk.py src/chunks/ch04e.tex` 通过，0 error；末尾 `% CHUNK ch04e DONE` 有。

逐页（页图 `pages/p194.png`–`p209.png`）：

- **p.187**：正定性 (2.36)、四类 Lagrange 量 a)–d)、(2.37) Finsler 型、(2.38) 长度泛函、可逆性、(2.39) Maupertuis 度量（两行、标签在第二行）——一致；页末「……路径」跨页，见必须改 2。
- **p.188**：道路空间 $\Omega(x_0,x_1)$、$\Omega^+(M^n)$、Arzelà 原理、变分导数与临界测地线、指标 $i(\gamma_0)$ 与共轭点、CW 复形胞腔与测地线一一对应——一致。
- **p.189**：(2.40) 两行；Fet 两条闭测地线；Gromoll–Meyer 的 Betti 数线性增长；Lyusternik–Shnirelman $m(S)\ge\operatorname{cat}(X/M^n)$、$X/S^2\sim\RP^2$、$m(S)\ge3$；脚注 2（Taimanov 综述）；Bott 的 $SU_{2n}$：Killing 形式 $\langle X,Y\rangle=\Re\Tr(X\bar Y^T)$、极小测地线子流形 $\cong G^\C_{2n,n}\cong U_{2n}/(U_n\times U_n)$、非极小指标 $\ge2n+2$、同伦群同构到 $2n$ 维——一致。
- **p.190**：(2.41)(2.42)(2.43)(2.44)(2.45) 逐个符号核对一致；$\pi_j(O_n)$ 与 $\pi_j(U_n)$ 表 9 列数值（Z/2,Z/2,0,Z,0,0,0,Z,Z/2 与 0,Z,0,Z,0,Z,0,Z,0）与页图完全一致；$\dim K<n-10$、$\dim K<2n-4$ 一致。
- **p.191**：正向极限 $O,U,Sp$、$\Omega^4O=Sp$、$\Omega^4Sp=O$、$\Omega^2U=U$；`Remark`（球面不可平行化由 Bott 周期性推出、奇数 $n$ 时 $\pi_{n-1}(SO_n)$ 中 2 阶元素、$\pi_{2n}(U_n)=\Z_{n!}$、Adams 结果不可这样推出，□）——一致。
- **p.192**：(2.46)(2.47)、Hopf 定理、外生成元与多项式生成元的维数、特征 $p>0$ 与对偶（Pontryagin 对偶）代数、Browder、Mislin–Hilton、Quillen–Sullivan 的 $p$-局部化——一致。
- **p.193**：Pontryagin 环同构于 Lie–Whitehead 超代数的包络代数、关系式 $x_ix_j-(-1)^{\dim x_i\dim x_j}x_jx_i=[x_i,x_j]$；`Example` 的 (2.48) 两行、(2.49) 两行；**原书两处二项式系数确实都印作 $\binom{p}{p+q}$**（页图可证），译者批注判断正确；Hopf 构造 $f_\psi:S^{2n+1}\to S^{n+1}$ 与两个嵌入——一致。
- **p.194**：Hopf 不变量 $h(f,\psi)=m_1m_2$、两个度映射、Hopf 与 Adams 的结果、可除代数维数 2/4/8、多值泛函的缘起（刚体、理想流体、Dirac 磁单极）、$S(x)=\int_{x_0}^x\omega$、(2.50)——一致。
- **p.195**：(2.51) 两行、(2.52)；覆盖与局部常值差、叶状结构、临界点与 Morse 指标、(2.53)——一致；页末「……它们由」跨页，见必须改 2。
- **p.196**：(2.54)、量子化的定义、例 1（Browder–Levine–Hsiang–Farrell，见 §5）、例 2（$\Omega^+(N^k)\to N^k$ 纤维丛、截面、(2.55)(2.56)、$E$ 与 $e$、$0\ne[\Omega]$、$K(\pi,1)$ 嵌入）——一致。
- **p.197**：同态单射与 $\Omega^+_0(N^k)$ 上单值性、例 3（(2.57)、手征场、3-形式/5-形式、$q=2$ 或 4、□ 位置）、局部泛函 $S^{(\alpha)}$ 与 Stokes 定理——一致。
- **p.198**：量子化与 Feynman 振幅、Novikov(1981)/Deser–Jackiw–Templeton(1982)/Witten(1983)、平凡丛情形的 Hurewicz 同态、$K^+$ 完备化与 Laurent 级数条件——一致（符号问题见建议改 1）。
- **p.199**：$b_j$、$q_j$ 与 (2.58)；Farber 的严格性；$K^+_\kappa$ 与 $\kappa=(\kappa_1:\cdots:\kappa_k)$、条件 $\sum\kappa_jm_j>-N(q)$、$(K^+_\kappa)^{\mathrm{Stable}}$；脚注 3（Sirokav、Pazhitnov–Ranicki）——一致（人名见建议改 2）。
- **p.200**：固定端点问题无 Morse 类比；$p^{-1}(\psi(N^n))=\bigcup N^n_j$、(2.59)、同伦 $\Phi$、(2.60)、$m_{i+1}(l^E)\ge\max_pb_i^{(p)}(N^n)$、脚注 4——一致。**(2.60) 原书右端确印作 $\hat l^E(N^n_{(0,\dots,0)})=0$、与左端严格不等式矛盾，译者批注判断正确**；同处原书把靶空间印作 $F$（应为 $\tilde M$），批注也指出，正确。
- **p.201**：(2.61) 用于 (2.38) 型泛函、$\bar\Phi$、Taimanov 定理 a) b)、「闭链向负值区域转移」、脚注 5、Polyakov–Vigman 例、(2.62)——一致（人名见建议改 3）。
- **p.202**：(2.63) 与 a) b) 性质、(2.64)、Chen–Sullivan、dga 与极小自由扩张 (2.65)、$C^1_q$ 构造、包含序列、(2.66)——一致。**(2.66) 前一行正文原书印 $C^q(A)$（上标）、(2.66) 印 $C_q(A)$（下标），译者批注判断正确**。页末句跨块，见必须改 1。
