# 丙组卡片交付报告（ch5 + ch8）

- 交付张数：**19 张**（概念 15 + 例子 4），与任务书清单逐条对齐，id / type / track 未改。
  - ch5（track `5`）：9 张 = 概念 7 + 例子 2
  - ch8（track `8`）：10 张 = 概念 8 + 例子 2
- 落盘位置：`_cards_grassmann/cards/concepts/*.json`（15）与 `_cards_grassmann/cards/examples/*.json`（4）。
- 校验：`python tools/validate_cards.py` 全库 **83 张卡（概念 67 + 例子 16），0 error / 0 warn**，我的 19 张在其中全部通过；`related` 的 11 条跨组链接在兄弟组落盘前后由「无法解析」自动转为通过（详见第三节）。
- 页码一律用中译 PDF 页 `pages_zh` 与英文 PDF 页 `pages_en`（ch5：en = zh + 9，首页例外；ch8：en 从 zh + 16 起漂到 + 17），不用书末印刷页码；anchor 全部回读 `Grassmannians-精读/source/chapters/chNN.tex` 对应行号，确认非空且是定义 / 命题 / 定理 / 例的起始行。

## 一、每卡一句话

### ch5（9，Kamnitzer《Beilinson–Drinfeld 格拉斯曼流形与辛纽结同调》）

| # | id | 一句话 |
|---|---|---|
| 1 | `concept/local-convolution-grassmannian` | 局部卷积 $\widetilde{\mathrm{Gr}}^{\underline\lambda}$ 记录一串逐点 Hecke 修正 $L_0\xrightarrow{\lambda_1}L_1\to\cdots\to L_k$，其像恰是闭轨道 $\overline{\mathrm{Gr}^{\lambda_1+\cdots+\lambda_k}}$，把「微小权」的几何变成可算的链空间。 |
| 2 | `concept/hecke-modification` | 单个 $(P,\varphi)$ 的 Hecke 型是模 $\mathrm{Aut}(\mathcal{O})$ 良定义的支配序类，$\mathbb{P}^1$ 上则有 Finkelberg–Mirković 的夹逼判据；它是「不会因平凡化选取而变」的那部分信息。 |
| 3 | `concept/geometric-satake-correspondence` | 几何 Satake 说 $\mathrm{Gr}$ 上 $G^\vee(\mathcal{O})$-等变反常层（球 Hecke 范畴）与 $G$ 的表示范畴张量等价，$\mathbb{C}_{\mathrm{Gr}^\lambda}[\dim]\mapsto V_\lambda$；整章的技术骨架。 |
| 4 | `concept/global-convolution-grassmannian` | 把局部链搬到 $X^n$ 上：记住中间丛的族 $\widetilde{\mathrm{Gr}}^{\underline\lambda}_{X^n}$ 在小对角线上给出卷积积，正则点上才是乘积，前推 $R^k\tilde p_*\mathbb{C}$ 因而是常值层。 |
| 5 | `concept/global-singular-grassmannian` | 只记最终丛与整体同构、把每点型放宽为 $\le\sum_{x_i=x}\lambda_i$，得到 $X^n$ 上的族；对角点纤维奇异（闭轨道），是本章真正要解的对象。 |
| 6 | `concept/factorization-property` | 点集分成互不相交的 $J_1\sqcup J_2$ 时，$U=\{$跨组点不重合$\}$ 上 $\mathrm{Gr}^{\underline\lambda}_U\cong(\mathrm{Gr}^{\lambda^1}_{X^{J_1}}\times\mathrm{Gr}^{\lambda^2}_{X^{J_2}})|_U$：碰撞只发生在同一组内。 |
| 7 | `concept/partial-grothendieck-resolution-and-nilpotent-slice` | 用分块矩阵 $S_{m,k}=E_{m,k}+\ker(\cdot F_{m,k})$ 造出幂零切片，其部分 Grothendieck 解消 $\widetilde{\mathfrak{gl}}_N^\pi$ 就是「$Y$ 保旗且在相邻商上作标量」的矩阵集合。 |
| 8 | `example/sl2-two-point-collision` | $SL_2$、$\underline\lambda=(\omega,\omega)$ 两点相撞：卷积纤维 $=\mathbb{P}^1$、奇异纤维 $=\overline{\mathrm{Gr}^{2\omega}}$，维数 $1=\tfrac12\cdot2$ 是全章唯一能一行验完的半小性。 |
| 9 | `example/comparison-theorem-with-slices` | 取 $G=SL_m$、$\lambda_i=\omega_{\pi_i}$ 时，$(_0)\widetilde{\mathrm{Gr}}$ / $(_0)\mathrm{Gr}$ 与切片解消 $\widetilde S^\pi_{m,k}\to S^\pi_{m,k}$ 同构且两方图交换——Mirković–Vybornov / Ngô 的比较定理。 |

### ch8（10，Pareschi–Popa《阿贝尔簇上的正则性 III》）

| # | id | 一句话 |
|---|---|---|
| 10 | `concept/m-regular-sheaf` | 把 GV 条件 $\operatorname{codim}V^i\ge i$ 加严成 $>i$ 就得到 $M$-正则层；这条「强一阶」条件让平移族的截面能扫过参数方向，是后文所有生成性定理的源头。 |
| 11 | `concept/torsion-freeness-criterion` | $GV$ 层 $M$-正则 $\iff$ $\widehat R\Delta\mathcal{F}$ 无挠：用 $R^i\hat S\mathcal F\cong\mathrm{Ext}^i(\widehat R\Delta\mathcal F,\mathcal O_{\hat X})$ 把几何条件翻成同调代数条件。 |
| 12 | `concept/nefness-of-gv-sheaves` | 阿贝尔簇上每个 GV 层都 nef：归约到主极化后用 $\mathcal{O}(-m\Theta)$ 的 $IT_g$ 性造出 $\varphi_m^*\mathcal F\otimes\mathcal{O}(m\Theta)$ 的 $M$-正则性，再取 $m\to\infty$ 的 $\mathbb{Q}$-扭曲极限。 |
| 13 | `concept/continuously-globally-generated` | 「连续整体生成」要求对**每个非空开集** $U\subset\mathrm{Pic}^0$，$\bigoplus_{\alpha\in U}H^0(\mathcal F\otimes\alpha)\otimes\alpha^{-1}\to\mathcal F$ 满射；比固定有限个 $\alpha$ 的整体生成强得多。 |
| 14 | `concept/m-regularity-index` | $m(L)$ 是使 $L\otimes\mathfrak m_{x_1}^{k_1}\otimes\cdots\otimes\mathfrak m_{x_p}^{k_p}$（所有互异点、$\sum k_i=l$）都 $M$-正则的最大 $l$；定理 7.4 证明其渐近斜率 $\rho(L)$ 被 Seshadri 常数 $\varepsilon(L)$ 夹住且 $\ge1$。 |
| 15 | `concept/m-theta-regular` | $m$-$\Theta$-正则 = $\mathcal F((m-1)\Theta)$ 是 $M$-正则的；阿贝尔版 Castelnuovo–Mumford 引理（定理 7.24）说 $0$-$\Theta$-正则就整体生成、且对各阶 $k\Theta$ 乘法满射。 |
| 16 | `concept/picard-bundle` | 曲线 $C$ 上 $\deg n\ge2g-1$ 的线丛经 Fourier–Mukai 变成 $J(C)$ 上的 Picard 丛 $E$，$\mathbb{P}E\cong C_n$；它是负的，必须先张 $\otimes^kE\otimes\mathcal{O}(\Theta)$ 才回到可消没的世界。 |
| 17 | `concept/semihomogeneous-bundle` | $t_x^*E\cong E\otimes\alpha$（$\alpha\in\mathrm{Pic}^0$）的丛：Mukai 说它半稳定、有强 Jordan–Hölder 滤过，且可由同源拉回成线丛直和 / 前推成线丛，于是 $M$-正则性变成一条 $IT_0$ 判据。 |
| 18 | `example/elliptic-curve-regularity` | 椭圆曲线上 $L$ 是 $M$-正则 $\iff\deg L\ge1$，且 $m(L)=p(L)=d-1$，于是 $m(n\Theta)=n-1$；高亏格下这条线性公式完全误导。 |
| 19 | `example/verlinde-bundle-regularity` | Verlinde 丛 $E_{r,k}=\det_*\mathcal{O}(k\Theta_N)$ 经 $r_J$ 拉回成 $\bigoplus\mathcal{O}(kr\Theta_N)$，故 $0$-$\Theta$-正则 $\iff k\ge r+1$、$(-1)$-$\Theta$-正则 $\iff k\ge2r+1$，正好复现 Popa 的整体生成 / 正规生成阈值。 |

## 二、证明状态统计与 sketch 清单

24 条 `theorems`：**complete 13 / sketch 4 / reference 7**。原则：章内有逐步证明的写 `complete`（steps 每步带 `text` + `why`）；原文只给引文或「由构造直接看出」的写 `sketch` 并在 `gap_note` 点明缺哪一步；只作文献定位的写 `reference`。

| 卡 | 定理 | 为什么只能 sketch / 缺什么 |
|---|---|---|
| `global-singular-grassmannian` | 命题 2.4（整体奇异族的纤维） | 原文对「小对角线纤维 $=\overline{\mathrm{Gr}^{\lambda_1+\cdots+\lambda_n}}$」只给构造 + 引 [MVi] 引理 6.1 的常值性；缺「正则点乘积 $\to$ 闭包取极限」的逐步验证（需先证两族在正则点同构，再用上半连续夹逼）。 |
| `partial-grothendieck-resolution-and-nilpotent-slice` | 部分解消的像与切片的纤维结构 | 像的描述（$\mathfrak{gl}_N^\pi$ = $\pi$ 加细特征值分划的矩阵）原文只引 Ngô 引理 2.3.1 / Mirković–Vybornov 定理 5.3；缺「$Y$ 在 $W_i/W_{i-1}$ 上作标量 $\Rightarrow$ 特征值重数受 $\pi$ 控制」的完整反向。 |
| `comparison-theorem-with-slices` | 定理 4.1（比较定理） | 作者自述证明只给梗概：缺「优选基 $[e_1],\dots,[z^{k-1}e_m]$ 是基 $\iff V\cong\mathcal{O}(k)^{\oplus m}$」与「$B$ 的像张满商」这两步（已写进 `gap_note`）。 |
| `continuously-globally-generated` | 命题 5.5（极大 Albanese 维数下的生成性） | 缺 $R^ia_*\omega_Y=0$ 与 $V_a^i(\omega_Y)=V^i(a_*\omega_Y)$ 的等同（投影公式的逐纤维核对），以及 Green–Lazarsfeld / Ein–Lazarsfeld 的余维输入如何拼成 (i)(ii)。 |

`reference` 7 条（章内不重证、只作定位）：`factorization-property`（定理 3.1 引 [BD] §5.3.10）、`global-convolution-grassmannian`（命题 2.3 引 [MVi] 引理 6.1）、`hecke-modification`（命题 2.2 引 [FM] 命题 10.2）、`local-convolution-grassmannian`（卷积积的像与半小性，引 [BD]/[MVi]）、`m-theta-regular`（定理 7.24 = [PP1] Thm 6.3）、`picard-bundle`（命题 7.22 引 [vGI]）、`semihomogeneous-bundle`（命题 7.26 = [Muk3] Prop 6.18）。

`complete` 的 13 条中，较硬的几条：几何 Satake 的纤维函子相容（3 步）、命题 2.8 的无挠判别（3 步，绕到引理 2.9 的谱序列）、定理 4.1 的 nef 性（2 步：归约主极化 + $\mathbb{Q}$-扭曲取极限）、定理 7.4 的 $\rho\le\varepsilon$（3 步，用式 (14) 与引理 7.8）、例 7.37 的阈值算术（$kr+r^2(m-1)\ge1$ 给出 $k\ge r+1$ / $2r+1$）。

## 三、id / related 冲突与处理

1. **11 条跨组 `related` 曾长期报「无法解析」**：`grassmann/concept/gv-sheaf` ×6（`m-regular-sheaf`、`torsion-freeness-criterion`、`nefness-of-gv-sheaves`、`continuously-globally-generated`、`m-regularity-index`、`elliptic-curve-regularity`）、`grassmann/concept/affine-grassmannian` ×5（`factorization-property`、`geometric-satake-correspondence`、`global-singular-grassmannian`、`hecke-modification`、`local-convolution-grassmannian`）。两条内容上都是非引不可：GV 层是 $M$-正则的定义前提（定义 2.7 直接建在 GV 上），仿射格拉斯曼是局部卷积在 $X=\mathbb{A}^1$ 的特例。校验器的 `related` 只认磁盘上真实存在的卡，于是甲组落盘前一直是 error；我**按真实语义保留、不换成「安全」假 id**，甲组 `gv-sheaf.json` / `affine-grassmannian.json` 落盘后这两批 error 自动清零，全库随之 0 error。
2. **同一机制下已自动清零的还有**：`grassmann/concept/koszul-cohomology`（`m-theta-regular`），以及更早的 `curve-operator`、`parabolic-bundle`、`partial-desingularization`、`grassmann/example/factorization-along-a-curve`。结论是：跨组互链只要 id 在 `tmp/cards-ids.md` 里真实存在、语义对得上，就不该为了「当下能过校验」而降级成同组链接；依赖会在兄弟组落盘时自然消失。
3. **绝对路径正则的误报**（同类坑乙组也踩了）：校验器 `[A-Za-z]:\\` 会把形如 `$\mathrm{Gr}^k:\ L_0$` 的公式判成「本机绝对路径」。`local-convolution-grassmannian` 首版即因此误报，改成冒号后加空格（`\mathrm{Gr}^k :\ L_0`）后消失，公式语义不变。
4. 我 19 张卡无 id / type 冲突：ch5 全部 `track "5"`、ch8 全部 `track "8"`，type 与 id 末段一致；例子卡的 `concept_refs` 全部指向概念卡 id。

## 四、存疑（5 条）

1. **引理 7.8 与定义 7.6 差一**：按定义 7.6，$s(L^{n+1},x)\ge m(L^n)$ 给出的是 $(m(L^n)-1)$-射流充裕，而命题 7.7 与式 (14) 用的像是 $m(L^n)$-射流充裕；疑 [PP2] 的约定差一。渐近取 $\sup$ 后 $\rho$ 不变、定理 7.4 不受影响，但推论 7.11 / 7.12 的精确常数（$\sqrt g\,n$、$(g!)^{1/g}n$）可能随之改一。卡里按正文写，未擅自改常数。
2. **椭圆曲线上 $m(L)=p(L)=d-1$ 是我自算的**：原书例 7.14 只给结论；我按 $\deg(L(-\sum k_ix_i))=d-\sum k_i$ 论证「互异点不改变结果」，但这依赖「所有互异点组、所有 $\sum k_i=l$」的正确量化（批注 12），若把定义读成「存在某些 $k_i$」则结论不同。
3. **空集余维按 $+\infty$ 读**：$g=1$ 时定义 2.7 的三个条件都要求 $V^i$ 为空（余维 $=1$ 不满足 $>1$），若把空集余维记 $0$，例 7.14 会自相矛盾。我按 $+\infty$（等价 $\dim V^i\le g-i-1$）解读，并写进 `m-regular-sheaf` 与 `elliptic-curve-regularity` 两卡的 pitfalls；原文未明说。
4. **定理 7.24 章内不重证**：它是 [PP1] Thm 6.3 的重述，故用 `reference`。若项目统一要求「书内出现的定理都 complete」，需要另找 [PP1] 补 steps；这属于标准取舍，不是缺漏。
5. **§6 的 $\mathrm{Pic}^0(X)$ 应为 $\mathrm{Pic}^0(Y)/\mathrm{Alb}(Y)$**（ch08.tex:411/419/447/455，英文原书同错）。这不在我 19 张卡范围内，只在报告记录，供丁组 / 审校处置。

## 五、页码与 anchor 核对方法

- ch5：中译 PDF 82–93 / 英文 PDF 90–103；ch8：中译 PDF 135–159 / 英文 PDF 150–177。中译 PDF 页 $=$ 印刷页码 $+6$，工程一律用 PDF 页。
- 每张卡的 anchor 都用「定义 / 命题 / 定理 / 例」的起始行（如 `chapters/ch05.tex:296`、`chapters/ch08.tex:771`），并回读该行确认非空、编号与卡内陈述对得上；正文段落卡（`local-convolution-grassmannian` 68 行、`global-convolution-grassmannian` 132 行等）取的是该段首行。
- 页码逐条用分页文本实测（中英各一份）：定理 7.34 中译 p.157（不是 p.155），命题 7.22 中译 p.152，定理 7.30 中译 p.154，定理 7.18 跨中译 150–151（卡里 `sources.pages_zh` 取 anchor 所在页 150，`theorem.source` 注明陈述在 p.151）。
