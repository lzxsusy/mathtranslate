# 《同调镜像对称性浅入门》中英术语表

**版本** v3.0（第三轮校定，2026-11-21）
**底本** Raf Bocklandt, *A Gentle Introduction to Homological Mirror Symmetry*, Cambridge University Press, 2021（London Mathematical Society Student Texts 99），365 页。
**适用** 本书中译校定本（`chapters/ch01.tex`–`ch12.tex`）与据其裁出的资料卡。

> 页码约定：表中「首见」为**书页码** p，PDF 页码 = p + 12。机器可读版见 `glossary.tsv`；与 `index-terms.tsv` 同源。

## 一、译名原则

1. **能意译就意译；无通行中文名则保留英文**，绝不硬造生词。保留英文者，正文首见处给出中文释义。
2. 人名、机构名、算法名不译：Fukaya、Lefschetz、Bridgeland、Calabi–Yau、Landau–Ginzburg、Morse、Reeb、Kontsevich、Serre、Beilinson、Maurer–Cartan 等。
3. **同词同译**；一词多义按数学义项分立（如 resolution：奇点「消解」／复形「分解」；cone：锥／映射锥）。
4. 音译只用于已通行、意译反而更糊涂的词（如「阿米巴」）；首见处加脚注说明词源与数学含义。
5. 术语一旦改动，正文、索引 `\index{拼音@显示名}`、本表、`index-terms.tsv`、资料卡五处同步；改动记入 §四。

## 二、关键术语释义

有些词在中文数学文献里没有统一译名，或字面与数学含义相去甚远，第一次出现时足以让读者卡住。下表给出本书的定译与一句解释；正文首见处另有脚注者标〔注〕。

| 中文 | 英文 | 首见 | 释义与译名说明 |
|---|---|---|---|
| 阿米巴〔注〕 | amoeba | 224 | 复环面 $(\mathbb C^*)^n$ 中超曲面 $V$ 在逐坐标对数映射 $\operatorname{Log}(z_1,\dots,z_n)=(\log|z_1|,\dots,\log|z_n|)$ 下的像，通常呈一只带腿的厚实变形虫之状。$t\to\infty$ 时阿米巴收缩为热带超曲面，是热带几何的基本对象。中文文献多作「阿米巴」；概念源于 Gelfand–Kapranov–Zelevinsky 关于 $A$-判别式的工作。 |
| 二聚体〔注〕 | dimer | 286 | 环面（更一般地，带标记曲面）上的二部图；边带权，完美匹配的权重和给出多项式 $P(x,y)$，其零点定义镜面曲线。英文 dimer 本义「二聚体」，此处借指图上的二聚体覆盖（= 完美匹配）。 |
| 箭图 | quiver | 70 | 允许重边与自环的有向图；箭图表示给每个顶点赋向量空间、每条箭赋线性映射。表示论与同调镜像对称的基本语言。 |
| 环簇 | toric variety | 219 | 以代数环面 $(\mathbb C^*)^n$ 为稠密开子集的代数簇，由扇（整锥的集合）组合地刻画。旧译「托里克簇」已废。 |
| 扇 | fan | 219 | $N_{\mathbb R}$ 中整锥构成的集合，满足：面属于集合、两锥之交为公共面。是环簇的组合骨架。 |
| crepant 消解 | crepant resolution | 228 | 保持典范类的消解 $\pi\colon\tilde X\to X$，即 $K_{\tilde X}=\pi^*K_X$。三维 Gorenstein 奇点必有之（Bridgeland–King–Reid）。中文文献多保留 crepant；旧译「保典解消」已废。 |
| 矩阵分解 | matrix factorization | 195 | 由势函数 $W$ 定义的 $A_\infty$ 范畴 $\mathrm{MF}(W)$：对象是 $W\cdot\mathrm{id}=pq$ 的因子分解；Landau–Ginzburg 模型 B 侧的核心构造。 |
| gentle 代数 | gentle algebra | 253 | 由箭图与关系给出的代数：每顶点至多 $2$ 入 $2$ 出，每箭至多属一个关系，关系是长度 $2$ 的路径，且无长度 $\ge3$ 的既约圈。中文文献多保留 gentle；旧译「温和代数」已废。 |
| 弦对象／带对象 | string object / band object | 82 | gentle 代数表示分类中的两类对象：弦对象由弦（string，不带圈的路径）给出；带对象由带（band，环状路径）连同参数 $\lambda\in k^*$ 给出，记作 $B(\lambda,n)$。 |
| wrapped Fukaya 范畴 | wrapped Fukaya category | 150 | 允许 Hamiltonian 同胚把拉格朗日膜推向无穷远后取极限的 Fukaya 范畴；与 partially wrapped、stop 配套。保留英文，避免与「绕数」（winding）相混。 |
| stop | stop | 152 | 截断 Reeb 流的超曲面，用于界定 partially wrapped Fukaya 范畴的边界条件。保留英文。 |
| thimble | Lefschetz thimble | 156 | Lefschetz 纤维化中消失圈张成的拉格朗日胞腔（Lefschetz 膜）。保留英文。 |
| 爆破 | blow-up | — | 在一点处把 $\mathbb A^n$ 换成例外除子的标准操作（$\mathrm{Bl}_0\mathbb A^2=\mathbb P(\mathcal O\oplus\mathcal O(-1))$ 等）；旧译「吹起」为字面直译，已废。 |
| 正合三角 | distinguished triangle | 60 | 三角范畴中形如 $A\to B\to C\to A[1]$ 的选定三角，满足 TR1–TR4。香蕉空间与中文文献通作「正合三角」；旧译「区分三角」已改。 |
| 带状图 | ribbon graph | 270 | 带循环序的图（fatgraph），即嵌入曲面的图的组合模型；沿带状图粘合是构造曲面与箭图的标准操作。 |
| 管状图 | tube graph | 275 | 由管（tube）与棱粘合成的图；沿管状图粘合用于把局部块拼成曲面。 |
| 例外序列 | exceptional collection | 167 | 满足 $\operatorname{Ext}^k(E_i,E_j)=0\ (i>j)$ 且 $\operatorname{Ext}^*(E_i,E_i)=\mathbb C\cdot\mathrm{id}$ 的对象序列；Fourier–Mukai 与镜像对称的基本构造。 |
| 球对象 | spherical object | — | 满足 $\operatorname{Ext}^*(E,E)\cong H^*(S^n)$ 的对象；沿其可作球面扭转（spherical twist）。 |
| 轨形 | orbifold | — | 局部为有限群商的空间；轨形点即其商奇点。 |
| 商栈 | quotient stack | 194 | 群作用 $X/G$ 的栈版本，保留稳定化子信息。 |
| 胖点 | fat point | 191 | 由幂零函数层定义的加厚点，如 $\mathbb C[x,y]/(x,y)^2$。 |
| 热带几何 | tropical geometry | 225 | 代数簇在 Log 映射与 $t\to0$ 极限下的分段线性骨架；阿米巴的极限。 |
| SYZ 纤维化 | SYZ fibration | — | Strominger–Yau–Zaslow 机制：互为镜像的 Calabi–Yau 流形带特殊拉格朗日环面纤维化，纤维互为对偶环面。 |
| 稳定条件 | stability condition | 316 | Bridgeland 稳定性：中心荷 $Z$ 与切片 $\mathcal P(\phi)$ 满足支撑性质与 Harder–Narasimhan 性质。 |
| 心 | heart | 325 | 稳定条件对应 $t$ 结构的「心」$\mathcal P((0,1])$，是 Abel 范畴。 |
| 中心荷 | central charge | 322 | $Z\colon K_0(\mathcal D)\to\mathbb C$，稳定条件的中心荷。 |
| 完美匹配 | perfect matching | 316 | 二聚体模型中覆盖每个顶点恰一次的边集；与箭图表示一一对应。 |
| 膜 | brane | 118 | 开弦端点所在的子流形；A-膜为拉格朗日子流形，B-膜为复子流形／相干层。 |
| 消失圈 | vanishing cycle | 156 | Lefschetz 临界值处收缩的圈；thimble 的边界。 |
| 极对偶 | polar dual | 239 | 多面体的配极：$P^\circ=\{y\mid\langle x,y\rangle\le1,\ \forall x\in P\}$。 |
| 反射多边形 | reflexive polygon | 239 | 唯一内部格点为原点的格多边形，其对偶仍为格多边形；对应 del Pezzo 曲面。 |

## 三、保留英文与不译清单

| 保留原文 | 理由 |
|---|---|
| Fukaya、Lefschetz、Bridgeland、Calabi–Yau、Landau–Ginzburg、Morse、Reeb、Kontsevich、Serre、Beilinson、Maurer–Cartan、Koszul、Hochschild、Ext、Tor、Hom | 人名／专名；中文文献一律保留 |
| wrapped / partially wrapped / stop / thimble / proper | 中文译名（卷绕、停止子、顶针、固有）均有歧义或与常用义冲突，保留英文并在首见处解释 |
| crepant（消解） | 中文文献多保留 crepant；硬译「保典」无依据 |
| gentle（代数） | 中文文献保留 gentle；「温和」易与 tame（温和型）相混 |
| $A_\infty$、dg、CY、LG、HMS、SYZ、SFT | 通行缩写 |
| Ext 群／Ext 环、Tor、K 群、$K_0$ | 记号本身即标准写法 |

## 四、第三轮术语变更记录（v3.0）

| 旧 | 新 | 处数 | 理由 |
|---|---|---|---|
| 保典解消 | crepant 消解 | 7 | 「保典」为生造音译，无文献依据；第 12 章原已用「crepant 解消」，本轮统一并补脚注 $K_{\tilde X}=\pi^*K_X$ |
| 解消 | 消解 | 11 | 中文数学标准作「消解」（奇点消解）；与「分解」分工 |
| 泛型 | 通有 | 20 | 「泛型」是编程术语；代数几何标准作「通有」（generic） |
| 温和代数／温和 $A_\infty$ 代数 | gentle 代数／gentle $A_\infty$ 代数 | 68 | 中文文献保留 gentle；且「温和」与 tame（温和型）相混 |
| 区分三角 | 正合三角 | 1 | 香蕉空间「三角范畴」条目与中文文献通作「正合三角」（exact triangle） |
| 相干层／拟相干层 | 凝聚层／拟凝聚层 | 72 | 中文代数几何标准作「凝聚层」「拟凝聚层」；「相干」为直译 |
| 吹起 | 爆破 | 7 | blow-up 的标准中文名是「爆破」；「吹起」为字面直译 |
| 一般的（generic 义） | 通有 | 14 | 与「泛型→通有」同一裁定，各章审稿统一 |
| 盘泡 | 圆盘泡 | 1 | 与「球面泡」并列，明确泡的维数 |
| （无） | 阿米巴首见脚注 | 1 | 音译词首次出现须给词源与数学定义 |
| （无） | 中英混排空格规范化 | 76 | 排版体例（如「gentle 代数」而非「gentle代数」） |

## 五、外部依据

- 香蕉空间：[箭图](https://bananaspace.org/wiki/箭图)、[箭图代数](https://bananaspace.org/wiki/箭图代数)、[环簇](https://www.bananaspace.org/wiki/环簇)、[三角范畴](https://bananaspace.org/wiki/三角范畴)（「正合三角」）、[镜像对称](https://bananaspace.org/wiki/镜像对称)（Fukaya 范畴、凝聚导出范畴）。本站对脚本访问返回 Cloudflare 挑战，条目正文经搜索引擎索引核读。
- R. Bocklandt, *A Gentle Introduction to Homological Mirror Symmetry*, CUP 2021（本书底本，术语以原书用法为准）。
- I. M. Gelfand, M. M. Kapranov, A. V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants*, Birkhäuser 1994, Ch. 6（amoeba）；M. Forsberg, M. Passare, A. Tsikh, *Laurent determinants and arrangements of hyperplane amoebas*, Adv. Math. 151 (2000)（amoeba 的另一独立来源）；G. Mikhalkin, *Amoebas of algebraic varieties and tropical geometry*, 2004。
- D. Maclagan, B. Sturmfels, *Introduction to Tropical Geometry*, AMS 2015（热带几何、扇与环簇）。
- 张梦蝶、章超，《Gentle 代数的矩阵模型及其整体维数》（中文文献保留「gentle 代数」的用例）。

## 附录 A　全书索引术语总表（按首见章排列）

<!--APPENDIX-->
