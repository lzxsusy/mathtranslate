# JP03 译本校读报告

- 底本：`src\JP03_植田一石_ミラー対称性とLagrangeトーラスファイブレーション_10p.pdf`（10 页，日文）
- 校本：`src\chunks\c00.tex`–`c05.tex`（UTF-8 无 BOM、LF；本次逐行核过）
- 方法：公式一律以 300–600dpi 局部裁图（`work\tools\crop.py`）逐符号核对，正文以 `work\split\p001–p010.txt` 文字层对读、疑点再裁图确认。文字层的上划线、上下标全部丢失，凡公式均未据文字层判断。
- 结论：必须修改 5 条（其中严重 1 条），建议修改 19 条（中 3 条、低 16 条）；编号公式 (1)–(27) 全部逐符号核过；除第一节所列两处记号问题（$\R^{>0}$ 的上下标、$\boldsymbol{x}$ 的粗斜体）外，数值系数、指数、上下划线、求和上下限、正斜体均未发现差异。

## 一、必须修改（错译/公式错/漏译）

- [严重] `src\chunks\c02.tex:11` | 原书 p.4 | 原页作 `$M\cong\overline{M}\oplus\Z$` 与 `$(0,1)\in N\cong\overline{N}\oplus\Z$`（第一个 $M$、$N$ 无上划线，第二个有；600dpi 裁图核实），译文作 `$\overline{M}\cong M\oplus\Z$`、`$(0,1)\in\overline{N}\cong N\oplus\Z$`，两处上划线写反 | 建议改为 `$M\cong\overline{M}\oplus\Z$`、`$(0,1)\in N\cong\overline{N}\oplus\Z$`。依据：同段后文 `$\Delta\subset\overline{M}_{\R}$` 是 $n-1$ 维、`$\iota_*:\overline{M}_{\R}\to M_{\R}$` 是嵌入，都要求 $\overline{M}$ 是 $M$ 的子空间；译文写法与此自相矛盾。
- [中] `src\chunks\c04.tex:66` | 原书 p.10 | 原页作「$|\gamma|:\R\to\R,\ t\mapsto|\gamma(t)|$ が単調増加な全単射であるようなもの」（「全」在行末、「単射」在次行行首，500dpi 裁图核实），译文作「是单调递增的单射」，脱「全」字、把「双射」改作「单射」 | 建议照录为「是单调递增的双射」，并另起一行加 `% [Tutor Note: 原页作「全単射」，但 $|\gamma|:\R\to\R$ 若为满射需取到负值，与 $|\gamma|\ge 0$ 矛盾，疑原书笔误；照录不改]`。按本译本「笔误照录 + 注释」原则，不得擅改原文。
- [中] 公式记号 $\R^{>0}$（上标）被写成 $\R_{>0}$（下标），共 5 处：`src\chunks\c02.tex:13`（`$B:=\overline{N}_{\R}\times\R_{>0}$`）、`src\chunks\c02.tex:59`（`$\pi_Y:Y\to\overline{M}_{\R}\times\R_{>0}$`）、`src\chunks\c02.tex:61`（`$L:=\overline{L}\times\R_{>0}$`）、`src\chunks\c03.tex:55`（把 `$\R_{>0}$` 直积到 $L$ 上）、`src\chunks\c04.tex:23`（`$\overline{L}_0:=\overline{N}_{\R_{>0}}$`，原页把 $\R^{>0}$ 放在 $\overline{N}$ 的下标里） | 原书 p.4 的 $\pi_{\check Y}$ 定义行（$\pi_{\check Y}:=(\mu_0,|w|):\check Y\to B:=\overline{N}_{\R}\times\R^{>0}$）、p.7 证明段（「$\R^{>0}$ を直積」）、p.8 的 $\overline{L}_0$ 定义处一律印作上标 $\R^{>0}$（500dpi 裁图核实）。建议 5 处全部改为 `\R^{>0}`；`src\chunks\c04.tex:26` 已写作 `$\R^{>0}$`，可作参照。
- [中] 公式 (7)(9)(10)(11) 中的 $x$：原页排作粗斜体 $\boldsymbol{x}$，译文 `src\chunks\c02.tex:18`（(7) 的 $\{(\boldsymbol{x},u,v)\in\dots\}$）、`src\chunks\c02.tex:34--35`（(9) 的 $\boldsymbol{x}\in\overline{N}_{\C^\times}$、$h(\boldsymbol{x})v_0=uv_1$）、`src\chunks\c02.tex:41--42`（(10) 的 $\chi(\boldsymbol{x},u)$、$|h(\boldsymbol{x})|^2$）、`src\chunks\c02.tex:47--48`（(11) 的 $\chi(\boldsymbol{x},u)$、$|h(\boldsymbol{x})|^2$）均作普通 $x$ | 建议统一改为 `\boldsymbol{x}`，与 `src\chunks\c04.tex:23` 的 `\bm r`、`\bm n` 体例一致。
- [低] `src\chunks\c04.tex:63` | 原书 p.10 首行 | 原页作「……反正準因子を与えることに注意せよ」，译文作「由于典范丛平凡，函数的零点给出反典范因子。」，「ことに注意せよ」未译 | 建议句末补「（注意这一点）」。

## 二、建议修改（术语/语病/体例）

- [中] `src\chunks\c03.tex:42` | 原书 p.7 | 原页「$s$ が Lagrange 切断である事と、$\nabla$ が正則構造を定める事は同値である」，译文作「因此，$s$ 是 Lagrange 截面与 $\nabla$ 定出全纯结构，二者等价。」——两个「…事」的并列被压平，读者会把「$s$ 是 Lagrange 截面与 $\nabla$」连读 | 建议「因此，「$s$ 是 Lagrange 截面」与「$\nabla$ 定出全纯结构」二者等价。」
- [低] `src\chunks\c01.tex:36` | 原书 p.3 | 原页「トーリック多様体の中の完全交差として与えられる Calabi--Yau 多様体」，译文作「作为完全交给出的 Calabi--Yau 流形」，「完全交」与紧跟的「给」字连排，读者易把它误读成动词「交给」 | 建议「作为完全交（complete intersection）给出的 Calabi--Yau 流形」，或加注说明「完全交」即原文「完全交差」。同处 `\textbf{}` 为空命令（原页无粗体），应删除。
- [中] `src\chunks\c01.tex:36` | 原书 p.3 | 原页「数学的に厳密に定式化できる対象で、超弦理論の持っている情報の一部を取り出していると期待されるものを用いる必要がある」，译文「必须使用那些可以被严格表述、并且被期待从超弦理论所携带的信息中提取出了其中一部分的对象」，被动与完成时叠加，句子过长 | 建议「必须使用这样的对象：它在数学上可以被严格表述，并且被期待提取出了超弦理论所含信息的一部分」。
- [中] 术语「指標」不统一：`src\chunks\c01.tex:26` 作「特征群」（原页 p.2「$T$ の指標群 $M=\Hom(T,S^1)$」），`src\chunks\c02.tex:11`、`src\chunks\c04.tex:63` 作「环面特征」（原页 p.4「トーラスの指標 $\chi_{(0,1)}$」、p.10「$M$ の指標」）；`work\glossary.tsv` 未收此条 | 建议统一为「特征标」（单数）、「特征标群」（群），并把该条补进 `work\glossary.tsv`。
- [低] `src\chunks\c04.tex:26` | 原书 p.9 | 原页「注意深く Hamilton 関数を選ぶ」，译文「适当选取 Hamilton 函数」，「注意深く」是「仔细」 | 建议「仔细选取 Hamilton 函数」。
- [低] `src\chunks\c02.tex:61` | 原书 p.5 | 原页「より正確には、$U$ の $\overline{N}_{\C^\times}$ への射影」，译文「与 $U$ 到 $\overline{N}_{\C^\times}$ 的投影」，集合不能与映射相交 | 建议「与 $U$ 到 $\overline{N}_{\C^\times}$ 的投影的像」。
- [低] `src\chunks\c03.tex:52` | 原书 p.7 | 「并且除 Hamilton 同痕外唯一」生硬 | 建议「并且在 Hamilton 同痕意义下唯一」。
- [低] `src\chunks\c03.tex:55` | 原书 p.7 | 「稍有不同的设定下的类似结果」两个「的」叠用 | 建议「设定略有不同时的类似结果」。
- [低] `src\chunks\c04.tex:41` | 原书 p.9 | 「环面 Calabi--Yau 流形的例子，有……；」句法不完整 | 建议「作为环面 Calabi--Yau 流形的例子，有……；」。
- [低] `src\chunks\c04.tex:61` | 原书 p.9 | 原页「焦点-焦点特異点（focus-focus singularity）」，译文「focus-focus 奇点」，英文括注不全；同句「环面的一个 cycle 塌缩」的 cycle 未译；「小平记号」缺名 | 建议「焦点–焦点奇点（focus-focus singularity）」「环面的一个闭链（cycle）塌缩」「小平（Kodaira）记号」。
- [低] `src\chunks\c04.tex:19` | 原书 p.8 | 「数出从带 $3$ 个标记点的圆盘到 $M$ 的、满足 Floer 方程与适当边界条件的映射，就使……」缺宾语中心语 | 建议「数出……这类映射的个数，就使……」。
- [低] `src\chunks\c04.tex:38` | 原书 p.9 | 「组合地定义的函数」（原页「組み合わせ的に定義された関数」）生硬 | 建议「由组合方式定义的函数」。
- [低] `src\chunks\c01.tex:46` | 原书 p.3 | 「对 K3 曲面，$L$ 是特殊 Lagrange 子流形，与 $L$ 经超 K\"ahler 旋转后成为复子流形，二者等价」两分句间无连接，易误读 | 建议「对 K3 曲面而言，「$L$ 是特殊 Lagrange 子流形」与「$L$ 经超 K\"ahler 旋转后成为复子流形」这两种说法等价」。
- [低] `src\chunks\c00.tex:8` | 原书 p.1 | 原页「概正則写像が非退化であるとは、……の形に表せることを指す」，译文「从殆复流形到 Riemann 面的伪全纯映射称为非退化，是指……写成 $(z_1,\dots,z_n)\mapsto z_1^2+\cdots+z_n^2$ 的形状」——「であるとは…を指す」译成了「称为……，是指」，且「的形状」冗赘 | 建议「所谓从殆复流形到 Riemann 面的伪全纯映射非退化，是指适当地取殆复局部坐标后可以写成 $(z_1,\dots,z_n)\mapsto z_1^2+\cdots+z_n^2$ 的形式」。
- [低] `src\chunks\c00.tex:12` | 原书 p.1 | 原页「ある意味で対極にあり」，译文「在某种意义上与之处于对极」，「对极」生僻 | 建议「在某种意义上恰好与之相对」。
- [低] `src\chunks\c01.tex:26` | 原书 p.2 | 「取值为 $M$ 的对偶群 $N\cong\pi_1(T)$ 的卷数」连读歧义 | 建议「以及取值为 $N\cong\pi_1(T)$（即 $M$ 的对偶群）的卷数」。
- [低] `src\chunks\c05.tex:1` | 原书 p.10 | 首行用「% c05 —— 参考文献（原书 p.10 末）」代替页标记，STYLE_GUIDE 要求每页开头写 `% ===== 原书 p.N =====` | 建议首行改为 `% ===== 原书 p.10 =====`，把原说明移到该行之后。
- [低][原书可疑] `src\chunks\c02.tex:13` | 原书 p.4 | 原页「$\pi_{\check Y}:=(\mu_0,|w|)$」，而 `src\chunks\c02.tex:11` 定义的是全纯函数 $w_n$，此处突然出现 $|w|$，原页未说明二者关系 | 建议照录并加 `% [Tutor Note: 原页此处作 $|w|$，前文定义的是 $w_n$，二者关系未说明，疑原书笔误；照录不改]`。
- [低][原书可疑] `src\chunks\c02.tex:11` | 原书 p.4 | 原页「$X$ はトーラス不変なアファイン開集合 $X\subset\C[z_1,\dots,z_n]$ を貼り合わせて得られ」——500dpi 裁图确认原页确印 $\C[z_1,\dots,z_n]$（多项式环），而「仿射开集」应指 $\C^n$ 中的开集，记号可疑；译文照录但未加注 | 建议加 `% [Tutor Note: 原页写作 $X\subset\C[z_1,\dots,z_n]$（多项式环），而「仿射开集」通常指 $\C^n$ 中的开集；疑原书笔误；照录不改]`。

## 三、已核对无误的清单（抽核，供 Lead 复核）

- 编号公式 (1)–(27) 全部与 300–600dpi 原页逐符号核对一致，重点复验项如下：
  - (1) `c01.tex:7` $-\frac{\partial^2}{\partial x^2}\Psi(x)=E\Psi(x)$；(2) `c01.tex:13` $\Map(S^1,T)\to\R,\ \gamma\mapsto\int_{S^1}(d\gamma/d\theta)^2\,d\theta/2\pi$；(3) `c01.tex:18` $E=m^2/R^2+R^2w^2$；(4) `c01.tex:31` $\frac{1}{n!}\omega^n=(-1)^{n(n-1)/2}\left(\frac{\sqrt{-1}}{2}\right)^n\Omega\wedge\overline{\Omega}$（上划线已核）；(5) `c01.tex:41` $D^b\mathrm{Fuk}\,Y\cong D^b\mathrm{coh}\,\check Y$。
  - (6) `c02.tex:7` 与 (4) 同型、多 $f^n$；(7) `c02.tex:19` $Y=\{(\boldsymbol{x},u,v)\in\overline{N}_{\C^\times}\times\C^2\mid h(\boldsymbol{x})=uv\}$；(8) `c02.tex:30`；(9) `c02.tex:36`；(10) `c02.tex:43`；(11) `c02.tex:49`；(12) `c02.tex:56`（原页两分支前都印 $\pi$、$\frac{1}{2}|u|^2$ 居中，易误读为 $\pi\cdot\frac12$；译文照录，正确。$h_{t,1}$ 原页未定义，`c02.tex:58` 已加 Tutor Note）。
  - (13) `c03.tex:14` 三段 `gathered`，指数 $\beta_i-\alpha_i$、末行 $z_{\alpha,n}=z_{\beta,n}$ 无误；(14) `c03.tex:22` $z_i=\exp 2\pi(x_i+\sqrt{-1}y_i)$；(15) `c03.tex:30` $\nabla:=d+2\pi\sqrt{-1}\sum_{i=1}^{n}\xi_i(x)dy_i$；(16) `c03.tex:35` $F_\nabla=2\pi\sqrt{-1}\sum_{i,j}\frac{\partial\xi_j}{\partial x_i}dx_i\wedge dy_j$；(17) `c03.tex:40` $F_\nabla^{(2,0)}=\pi\sum_{i,j}(\frac{\partial\xi_j}{\partial x_i}-\frac{\partial\xi_i}{\partial x_j})dz_i\wedge dz_j$（系数是 $\pi$ 不是 $2\pi$，已核）；(18) `c03.tex:45` $\mathrm{HF}^*(s_0,s)\cong\Hom^*(\mathcal O_{\check X(B^{\mathrm{sm}})},\mathcal L_\nabla)\cong H^*(\mathcal L_\nabla)$。
  - (19) `c04.tex:12` $(du-X_H\otimes dt)^{0,1}=0$；(20) `c04.tex:17` $\mathbf m_1([\gamma])=\sum_{\gamma'}n_{\gamma,\gamma'}[\gamma']$；(21) `c04.tex:36` $p_{\bm n,i}\cdot p_{\bm n',i'}=\sum_{j=0}^{\ell(\bm n,\bm n')}\binom{\ell}{j}p_{\bm n+\bm n',i+i'+j}$（求和上限 $\ell(\bm n,\bm n')$、下标 $i+i'+j$ 已核）；(22) `c04.tex:44`；(23) `c04.tex:49` $\Omega=\mathrm{Res}\left[\frac{dz}{z}\wedge\frac{du\wedge dv}{uv-f(z)}\right]=\frac{dz}{z}\wedge\frac{du}{u}$；(24) `c04.tex:54` $\pi_Y:Y\to B:=\R^2,\ (z,u,v)\mapsto\left(\log|z|,\frac{1}{2}(|u|^2-|v|^2)\right)$；(25) `c04.tex:59` $\{(\log|\alpha_0|,0),\dots,(\log|\alpha_n|,0)\}\subset B$；(26) `c04.tex:69` $D^b\mathcal W\cong D^b\mathrm{coh}\,\check Y$；(27) `c04.tex:74` $Y=\{(z,u_1,v_1,u_2,v_2)\in\C^\times\times\C^4\mid u_1v_1=z-a,\ u_2v_2=z-b\}$。
- 未编号公式均已核：`c02.tex:52--55` 的分段函数（$\epsilon<\lambda$ 分支）；`c04.tex:21` $\theta=\sum_{i=1}^{n}r_id\theta_i$（原页上限印 $n$，与坐标 $i=1,\dots,n-1$ 不符，`c04.tex:22` 已有 Tutor Note，合格）。
- 原书笔误「照录 + 加注」核对合格：p.6「$\alpha,\beta\in\Delta\cap\Z^{n-1}$」（`c03.tex:6` 照录、`c03.tex:17` 加注）；p.8 Liouville 流形印作 $M$ 的三处（`c04.tex:7` 注）；p.8「$\sum_{i=1}^{n}r_id\theta_i$」；p.4「$dz_n\wedge\cdots\wedge dz_n$」；p.5 $h_{t,1}$；p.10「Fleor」（`c04.tex:24`）；`c05.tex:29`「An-singlarities」；`c02.tex:22` 把原页「$Y$ 的复结构参数」与「$\check Y$ 的辛结构」对调一句加注说明。
- 页标记与 chunk 标记：`c00`–`c04` 每页 `% ===== 原书 p.N =====`（p.1–p.10）齐全、顺序正确，`c04.tex:65` 起交接 p.10 正确；六个 chunk 末尾 `% CHUNK cNN DONE pages …` 与实际页码逐一相符（c00 p1 / c01 p2–p3 / c02 p4–p5 / c03 p6–p7 / c04 p8–p10 / c05 p10）。
- 定理题名：`c03.tex:51` `\begin{theorem}[{[CPUa, Theorem 1.1]}]`、`c04.tex:29` `\begin{theorem}[{[CPUa, Theorem 1.2]}]` 与 p.7、p.9 原页一致；两处定理陈述逐句核对无漏译（含「C 代数の同型 $\mathrm{HW}^*_{\mathrm{ad}}(L_0)\cong H^0(\mathcal O_{\check Y})$ が存在する」）。
- 文献：`c05.tex` 10 条与 p.10 原页逐条对应，顺序、编号、MR 号、作者缩写一致；正文引用一律纯文本（`[AAK]`、`[SYZ96]`、`[CPUa, Theorem 1.1]` 等），全库无 `\cite`、`\ref`、`\label`、`\newcommand`、`\documentclass`、`\usepackage`；UTF-8 无 BOM、纯 LF（逐文件校验）。
- 术语：对照 `work\glossary.tsv` 抽查全部命中——深谷圏→Fukaya 范畴、巻かれた→wrapped（保留英文）、連接層→相干层、トーリック→环面、アメーバ→amoeba、クレパント→crepant、校正形式/校正部分多様体→校准形式/校准子流形、Hamilton アイソトピー→Hamilton 同痕、反正準因子→反典范因子、通常二重点→普通二重点、特異点解消→奇点消解、双対→对偶；人名与专名（Givental、Lian–Liu–Yau、Kontsevich、Strominger–Yau–Zaslow、Donaldson、[Abo09]、Maslov、Floer、Lefschetz、Riemann、Morse、Hodge）均保留英文，未发现误译。
- 中文文字质量：全库无半角标点混入中文、无「的的」「， ，」「。。」「、、」；无「被……所」「进行……的」「对于……而言」句式（唯一「对于」在 `c01.tex:4`「对于在半径为 $2\pi R$ 的圆周上运动的自由粒子」，用法正常）；未发现「我們」等繁体混入。英数与中文之间空格、全角标点使用合乎 STYLE_GUIDE。
