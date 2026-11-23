# trace-abelian — §9 逐段译法 / 公式清单 / 核对记录

译手：abelian　｜　目标文件：`源码/sections/s11-abelian.tex`、`源码/sections/s99-bibliography.tex`　｜　底本 p.42–p.46

## 0. 核对方法

1. `PYTHONIOENCODING=utf-8 python 工程文件/tools/render_pages.py 42-46 --dpi 150` → `工程文件/work/pages/p042–p046.png`（脚本对已存在的页只是 skip，没有重渲染）。
2. 整页 150 dpi 通读，定段落、环境、图、页界。
3. 公式逐条用 PyMuPDF `get_text("blocks")` 取行 bbox，再 `page.get_pixmap(dpi=900~1400, clip=Rect(...))` 裁窄带存 `%TEMP%\fgcrop\*.png`，`read_image` 逐符号核（裁图绕过 read_image 的 1400 px 降采样，下划线、上下标、箭头方向都看得清）。
4. 文本层（`work/src/pNNN.txt`）只用于定位句子；**公式一律以图像为准**。
5. 文献表另做一次字体核对：`page.get_text("dict")` 逐 span 取 font，按 CMR8=正体、CMTI8=斜体、CMITT10=斜体打字机 判定条目里哪一段是斜体（期刊名/丛书名/预印本/网址），据此写 `\textit` / `\url`。

## 1. 页锚（`_check_g.pagemarks` = 42 43 44 45 46）

| 锚 | 形式与位置 | 依据 |
|---|---|---|
| 42 | `\leavevmode\srcpage{42}`，§9.1 正文首句前 | p.42 页首即 "9. THE ABELIAN CASE"，其上无 §8 残余；锚放标题之后、正文之前 |
| 43 | `\leavevmode\srcpage{43}`，命题 9.1 证明结束后、「现在设 $\varphi:W_E\to\Ql^\times$ 是连续特征」之前 | 原文 p.42 末行是 $h^\to{}^*\mathcal{T}_d=\dots$ 与 □，p.43 首行是 "Let now $\varphi:W_E\to\ol{\QQ}_\ell^\times$…"；页界正在证毕与下一段之间。锚放在 `proof` 环境之外，避免 `\srcpage` 落入环境内部 |
| 44 | `\srcpageinl{44}`，§9.2 括号注「……也许我们该在整个猜想中都这样做）」内 | p.43 末行 "maybe we should do" / p.44 首行 "this in the entire conjecture)." ——页界落在括号内句中，只能用行内锚 |
| 45 | `\srcpageinl{45}`，「只依赖于〔p.45〕这个 Weil 反常层……」句中 | p.44 末行 "…all the asked properties in the conjecture depend" / p.45 首行 "only on the isomorphism class…"——页界落在句中 |
| 46 | `\leavevmode\srcpage{46}`，「由此推出」段首 | p.45 末 "This means that $\varphi|_{W_{E_{\mu'}}}$ corresponds to" + 一条展示式；p.46 从 "From this one deduces that" 起 |

## 2. 公式清单（逐条对图核过）

**p.42**

1. `\Bun=\coprod_{d\in\ZZ}\Bun^d`。
2. `[\Spa(\FF_p)/\ul{E}^\times]\xrightarrow{\sim}\Bun^d` —— 分母 $E$ **有下划线**（1400 dpi 确认），$\FF_p$ 无下划线。
3. `\ul{Hecke}^d_\mu=\vec h^{-1}(\Bun^d\times\Spa(E)^\diamond)` —— "Hecke" 在原文**带下划线且为斜体**（400 dpi 原尺寸裁图确认，非副图伪影）。
4. 交换图 #1：`\ul{Hecke}^d_\mu` 上，左 `\overleftarrow h`→`\Bun^{d+k}`，右 `\vec h`→`\Bun^d\times\Spa(E)^\diamond`。
5. `E(k)=E(1)^{\otimes k}`；`\mathcal{LT}_k\wedge\mathcal{LT}_{k'}=\mathcal{LT}_{k+k'}`；$\wedge$ 定义为 $\times_{\ul E^\times}$。
6. Prop 9.1(2)：`\overleftarrow h^*\mathcal T_{d+k}\simeq\vec h^*\mathcal T_d\wedge\mathcal{LT}_{-k}`。
7. 正合列 `0\to\mathbb B^{\varphi=\pi^d}\otimes_E E(k)^\diamond\to\mathbb B^{\varphi=\pi^{k+d}}\to\mathbb B^+_{dR}/\mathrm{Fil}^k\mathbb B_{dR}\to0` —— 首项上标是 $\pi^d$、次项是 $\pi^{k+d}$；`Fil^k` 的 $k$ 是上标，`\mathbb B^+_{dR}` 的 $+$ 也是上标。
8. `\mathbb B(S)=\Gamma(S,\cO_{Y_S})`。
9. `Rf_*\mathcal E=\mathcal T\times_{\ul E^\times}\mathbb B^{\varphi=\pi^i}`。
10. `\vec h^*\mathcal T_d=\overleftarrow h^*\mathcal T_{d+k}\wedge\mathcal{LT}_k`。

**p.43**

11. `\chi:E^\times\xrightarrow[\sim]{\Art}W_E^{ab}\xrightarrow{\varphi}\Ql^\times`（$\sim$ 在箭头**下**）。
12. `\mathcal G|_{\Bun^d}=\mathcal T_d\times_{\ul E^\times,\chi}\Ql`。
13. `\mathcal F_\varphi=\mathcal G|_{\Bun_{\ol\FF_q}}`。
14. **(10)** 两行：`\vec h_!(\overleftarrow h^*\mathcal G)|_{\Bun^d\times\Spa(E)^\diamond}=\mathcal T_d\times_{\ul E^\times}\mathcal{LT}_{-k}\times_{\ul E^\times,\chi}\Ql=\mathcal G|_{\Bun^d}\boxtimes(\chi\circ\chi_{\mathcal{LT}})^{-k}` —— 第二行指数 $-k$ 在括号外。
15. 两条：`\Art\circ\chi_{\mathcal{LT}}(\sigma)=1` 若 $\sigma=\Art(\pi)$；`=σ^{-1}` 若 $\sigma$ 落在惯性子群的像里。
16. `\vec h_!(\overleftarrow h^*\mathcal F_\varphi)|_{\Bun^d_{\ol\FF_p}\times\Spa(\breve E)^\diamond}=\mathcal F_\varphi|_{\Bun^d_{\ol\FF_p}}\boxtimes r_\mu\circ\varphi|_{I_E}` —— 原文此处写 $\ol\FF_p$（不是 $q$），照排；$\breve E$ 用 `\breve`。
17. `\Isom((L,\pi^{-d}\sigma),(L,\delta\sigma))=\{g\in L^\times\mid g\delta\sigma=\pi^{-d}\sigma g\}`。
18. `g^\sigma=\delta\pi^d g`。
19. `\mathcal T_\delta=\mathcal T_d\wedge T_{\delta\pi^d}`；单值性 `\Frob_q\mapsto\delta\pi^d`。
20. `\kappa:\mathrm B(T)\xrightarrow{\sim}X_*(T)_\Gamma`；`\Bun=\coprod_{[\mu]\in X_*(T)_\Gamma}\Bun^{[\mu]}` —— 两处 $\Gamma$ **都是下标**（1400 dpi 核）。

**p.44**

21. 交换图 #2：`\ul{Hecke}^{\bar\mu'}` 上，`\Bun^{[\mu+\mu']}` / `\Bun^{[\mu]}\times\Spa(E)^\diamond`；$\bar\mu'$ 的横线盖住 $\mu'$。
22. Prop 9.3：`\ul{Hecke}^{\bar\mu'}=\Bun\times\Spa(E_{\mu'})^\diamond`，`\vec h=\mathrm{Id}\times\mathrm{can}_{E_{\mu'}|E}`。
23. `H^1(W_E,\hat T)=\Hom(T(E),\Ql)`（此处原文无 $\times$，后文同式有 $\times$，两处照原文分别排）。
24. `x_b:[\Spa(\ol\FF_q)/\ul T(E)]\xrightarrow{\sim}\Bun^{-\kappa(b)}_{\ol\FF_q}` —— 分母 $T(E)$ **整体带下划线**。
25. `\Frob^*x_b=x_{b^\sigma}`、`\Frob^*\mathcal T_b=\mathcal T_{b^\sigma}`、`b^\sigma=b^{-1}.b.b^\sigma`（原文如此）。
26. **(11)** `\Weil_b:\Frob^*\mathcal T_b\xrightarrow{\sim}\mathcal T_b`。
27. `T_{b,b'}=\{g\in T(L)\mid gbg^{-\sigma}=b'\}` —— 指数是 $-\sigma$。
28. `\mathcal T_b\wedge T_{b,b'}=\mathcal T_{b'}`。
29. `g:\mathcal T_b\xrightarrow{\sim}\mathcal T_{b'}`、`g\circ\Weil_b=\Weil_{b'}\circ\Frob^*g`、`\Frob^*g=g^\sigma`。
30. `\mathcal F|_{\Bun^{[\mu]}_{\ol\FF_q}}=\mathcal T_b\times_{\ul T(E),\chi}\Ql`。

**p.45**

31. `\delta=N_{E_{\mu'}/E_n}(\mu'(\pi_{\mu'}))\in T(E_n)`。
32. `\rho_{\delta,\mu'}:\Gamma^{ab}_{E_{\mu'}}\to T(E)`。
33. `N_{\mu'}:E^\times_{\mu'}\xrightarrow{\mu'}T(E_{\mu'})\xrightarrow{N_{E_{\mu'}/E}}T(E)`。
34. 两条：`\rho_{\delta,\mu'}\circ\Art(x)=N_{\mu'}(x)^{-1}`（$x\in\cO^\times_{E_{\mu'}}$）、`\rho_{\delta,\mu'}\circ\Art(\pi_{\mu'})=1`。
35. Prop 9.5：`\overleftarrow h^*\mathcal T_{b\delta}\simeq\vec h^*\mathcal T_b\wedge T^{cris}_{\delta,\mu'}`，$T^{cris}_{\delta,\mu'}$ 的 $cris$ 是斜体上标。
36. `\mathbb C_p=\widehat{\ol{E}}`。
37. `(V\otimes_E\cO_{X_{\mathbb C_p^\flat}})|_{X_{\mathbb C_p^\flat}\setminus\infty}\xrightarrow{\sim}\mathcal E(V_{E_n},\rho(\delta)\sigma)|_{X_{\mathbb C_p^\flat}\setminus\infty}`。
38. `\rho_*(\mathcal E_b\wedge T^{cris}_{\delta,\mu'})|_{X_{\mathbb C_p^\flat}\setminus\infty}\xrightarrow{\sim}\rho_*(\mathcal E_{b\delta})|_{X_{\mathbb C_p^\flat}\setminus\infty}`；$\rho_*\mathcal E_b=\mathcal E(V_L,\rho(b)\sigma)$。
39. `\hat\mu'\in X^*(\hat T)^{\Gamma_{E_{\mu'}}}`。
40. `{}^L\mu':{}^LT_{E_{\mu'}}\to\Ql^\times`；`{}^LT_{E_{\mu'}}=\hat T\rtimes\Gamma_{E_{\mu'}}`。
41. `r_{\mu'}=\Ind_{E_{\mu'}|E}{}^L\mu'`。
42. `H^1(W_E,\hat T)=\Hom(T(E),\Ql^\times)`。

**p.46**

43. `\chi\circ N_{E_{\mu'}/E}:E^\times_{\mu'}\xrightarrow[\sim]{\Art}W^{ab}_{E_{\mu'}}\xrightarrow{{}^L\hat\mu'\circ\varphi_{W_{E_{\mu'}}}}\Ql^\times` —— 原文箭头上标签是 ${}^L\hat\mu'\circ\varphi_{W_{E_{\mu'}}}$（$\varphi$ 的 $W_{E_{\mu'}}$ 直接作下标，图上无竖线）。

## 3. 逐段译法决策

| 位置 | 原文 | 处理 | 依据 |
|---|---|---|---|
| p.42 | "Let us note $\mathcal T_d$ for the corresponding universal $\ul{\QQ}_p^\times$-torsor" | 「记 $\mathcal T_d$ 为……万有 $\ul{\QQ}_p^\times$-torsor」 | 「万有」与 glossary 无冲突；$\QQ_p$ 带下划线已核 |
| p.42 | "This is the torsor of isomorphisms between $\cO(d)$ and the universal line bundle" | 「它是 $\cO(d)$ 与 $\Bun^d$ 上万有线丛之间同构构成的 torsor」 | 拆成两个小句，避免「是……的 torsor」长定语 |
| p.42 | "This defines a rank 1 pro-étale local system … and thus a $\ul E^\times$-torsor" | 「这给出……一个秩 1 pro-étale 局部系统，从而给出……$\ul E^\times$-torsor」 | pro-étale 按 glossary 不译 |
| p.42 | 正合列前的 "There is an exact sequence of sheaves over $\Spa(E)^\diamond$" | 「$\Spa(E)^\diamond$ 上有层正合列」 | 短句 |
| p.42 | "Up to taking the dual modification one can suppose $k\ge0$ too" | 「再取对偶修正，还可设 $k\ge0$」 | modification=修正 |
| p.43 | "This is not still the local system we are looking for." | 「**这仍不是**我们要找的局部系统。」 | 原文斜体断言，按 SPEC 用 `\emph` |
| p.43 | "does not always descend to $\Bun$ (in our case in this section because $\chi(\pi)$ may not be an $\ell$-adic unit)" | 「并不总能下降为 $\Bun$ 上的层（在本节的场合，因为 $\chi(\pi)$ 可能不是 $\ell$-进单位）」 | 括注照拆，不并入主句 |
| p.43 | "The realization of local class field theory in the torsion points of the Lubin–Tate group tells us that" | 「局部类域论在 Lubin–Tate 群挠点上的实现告诉我们」 | 保留「实现」这一技术词 |
| p.43 | "on $\Bun^d_{\ol\FF_p}$" | 照排 $\ol\FF_p$，不改 $q$ | 疑点 D7，见报告 |
| p.44 | "we take the opposite of the sign convention in the conjecture like in the $\mathrm{GL}_1$-case, the degree of a vector bundle being the opposite of $\kappa$" | 「我们采用与猜想中相反的符号约定，如同 $\mathrm{GL}_1$ 情形；向量丛的次数取为 $\kappa$ 的相反数」 | 原文逗号连排两件事，中文改用分号断开 |
| p.44 | "According to local class field theory $H^1(W_E,\hat T)=\Hom(T(E),\ol{\QQ}_\ell)$. We thus have a character" | 保持「按局部类域论，……。于是有特征」两小句 | 不改逻辑顺序 |
| p.44 | "This defines a $T(E)$-torsor $\mathcal T_b$ over $\Bun^{-\kappa(b)}_{\ol\FF_q}$." | 「这给出……上的 $T(E)$-torsor $\mathcal T_b$」 | 「定义」→「给出」更顺；不损义 |
| p.45 | "Let $E_n\vert E$ be the maximal unramified extension in $E_{\mu'}$" | 「其中 $E_n\vert E$ 是 $E_{\mu'}$ 中的最大非分歧扩张」 | unramified=非分歧 |
| p.45 | "the pair $(\delta,\mu')$ is admissible" | 「$(\delta,\mu')$ 是可容许对」 | 新增术语建议 |
| p.45 | "Take $(V,\rho)\in\Rep_E(T)$ a linear representation of $T$" | 「取 $(V,\rho)\in\Rep_E(T)$，即 $T$ 的一个线性表示」 | 同位语改「即」，避免「一个……的线性表示」 |
| p.45 | "Projecting via … taking into account the Γ-action and making ρ vary one obtains the result as in 9.1." | 「经……投影，计入 $\Gamma$-作用并让 $\rho$ 变动，即得 9.1 中的结果」 | 「即得」对应 one obtains |
| p.45 | "Note"（引出 $N_{\mu'}$ 的展示式） | 「记」 | 原文 Note 在此是祈使「记下」 |
| p.45 | "which defines a character ${}^L\mu'$" | 「它定义特征」 | 与前句「$\hat\mu'$ 定义」重复但原文如此 |
| p.46 | "The Hecke property is deduced from this and the preceding formulas" | 「Hecke 性质由这一点以及前面关于 $\rho_{\delta,\mu'}\circ\Art$ 的公式推出」 | 拆为两个小句 |

**版式决定**

- 原文 p.44 末「Let /（展示式）/ be a Langlands parameter and /（展示式）/ be the corresponding character」三行排，中文改排成一句行内式：`设 $\varphi:W_E\to{}^LT$ 为 Langlands 参数，$\chi:T(E)\to\Ql^\times$ 为类域论给出的相应特征` —— 只动版式，不动文字与顺序。
- 同理 p.45 的「We now note /（展示式）/ for the corresponding $T(E)$-torsor」改为行内。
- 两张交换图都包在 `\[ … \]` 里；原先裸 `tikzcd` 在段中被断行，出现孤字。
- (10) 用 `aligned` 两行，`\tag{10}` 硬保原文号，`\label{eq:9.10}`；同理 (11) 用 `\tag{11}`、`\label{eq:9.11}`。原文其余展示式无号，均未编号（符合「原文无号不擅加号」；报告已说明）。

## 4. 原文笔误登记（均未改原文）

| # | 原文 | 应为 | 译文处理 |
|---|---|---|---|
| 1 | "this is an **isomorphic** if we equip…" | an isomorphism | 译「这就是同构」，`\yizhuw` 说明 |
| 2 | "The **chocaracter** $\mu'$ defines" | cocharacter | 译「余特征」，`\yizhuw` 说明 |
| 3 | "This defines a **cristalline** representation" | crystalline | 译「晶体表示」，`\yizhuw` 说明（同页第二处 "The cristalline representation" 同处理） |
| 4 | "if $\mathcal T$ is the corresponding $\ul E^\times$-torsor of isomorphisms between $\cO(i)$ and $\mathcal T$" | 第二个 $\mathcal T$ 应为 $\mathcal E$ | 照字面译，`\yizhuw` 说明 |
| 5 | "For $b\in T(L)$ **here is** an isomorphism" | there is | 译「有……同构」，笔误在中文里消失，登记于报告 D5 |
| 6 | "the $n$-th iterate of the **descente** datum" | descent | 译「下降数据」，不注 |
| 7 | $\Bun^d_{\ol\FF_p}$（p.43 两处） | 应为 $\ol\FF_q$ | 照排 $p$，登记 D7 |
| 8 | "if $b\in T(E)$ this Weil descent datum on $\mathcal T_b$ is never effective unless $b$ is a root of unity" | 语义可疑（否命题反了） | 照字面译，登记 D4 |

## 5. 文献表核对

- 结构：`\begin{thebibliography}{32}` + 32 条 `\bibitem`；编号由环境自动生成，与原文 [1]–[32] 一致；条目文字、作者、年份、卷期页一字未改。
- 斜体范围按字体判定：CMTI8（斜体）标期刊名/丛书名/预印本名/网址；CMR8（正体）标作者、标题、卷期页。
  - 例外：`\url{}` 那几条原文用 CMITT10（斜体打字机），为便于整书统一，改用 `\url`（正体打字机）。
- 照抄不改的原文特殊处：`shimura`（小写 s，[2]）、`langlands`（小写，[7]）、`Shimura`（大写，[19]）、`J. Amer. Math. Soc,`（[19] 缺句点）、`witt vector affine grassmannian`（[29] 全小写）、`geometric satake`（[32] 小写）、`Supercuspidal l-packets`（[14]）、`S.W. Shin`（[31] 无空格）、`[11] (352):Exp. No. 1057, x, 509–534`、`[26] Forum Math. Pi, 1:e1, 77, 2013`。
- p.46 末尾作者地址（`\textsc{Laurent Fargues, CNRS, …}` + `\textit{E-mail address:} …`）排在 `\end{thebibliography}` 之后，属可选保留项（报告 D9）。

## 6. 自检记录

```
build.bat check sections/s11-abelian.tex g    → _check_g.pdf 5 页，grep "^!" = 0，Overfull = 0
build.bat check sections/s99-bibliography.tex b → _check_b.pdf 3 页，grep "^!" = 0，Overfull = 0
_check_g.pagemarks = 42 43 44 45 46
```

- 无 `??`；无空段落；5 个 `\srcpage` 都不在脚注或环境内部（p.43 的锚已移到 `\end{proof}` 之后）。
- 五页 120 dpi 逐页看过：标题、两张交换图、正合列、(10)(11)、四个命题、例 9.4、链式映射均正常；无孤字、无溢出。
- 术语抽查：局部 Langlands 对应、Weil 群、Frobenius（不译）、环面、特征层、Kottwitz 集、基本的、Bun、Weil 限制、σ-共轭、修正、局部系统、反常层、等晶体、Hecke 叠、pro-étale（不译）——均与 glossary 一致。
