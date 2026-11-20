---
id: MS-24
zh: Berglund–Hübsch 转置与轨形镜像
en: Berglund–Hübsch transpose and orbifold mirror symmetry
aliases: [BH 转置, 广义 Berglund–Hübsch 转置法则, 轨形镜像]
layer: L2
prereqs: [MS-09, MS-23]
sources:
  - "A 级：Cox–Katz 1999, p.093–095（PDF p.093–095，印刷 p.070–072）§4.4.3：书内唯一使用「广义 Berglund–Hübsch 转置法则」处；式 (4.30)–(4.33)、指数公式、2:1 覆盖"
  - "A 级：Cox–Katz 1999, p.089–092（PDF，印刷 p.066–069）§4.4.1–4.4.2：Voisin–Borcea 三维簇、N/N'、定理 h^{1,1}=11+5N−N'、h^{2,1}=11+5N'−N"
  - "A 级：Cox–Katz 1999, p.040（PDF，印刷 p.017）§2.2 与 p.084–085（PDF，印刷 p.061–062）§4.2：五次镜像=五次/G 的解奇异化；G 阶 125；M 的子格 M_1 指数 125、M/M_1≅G"
  - "A 级：Cox–Katz 1999, p.431–433（PDF）附录 A §A.2–A.4：轨形定义 A.2.1、命题 A.2.2、推论 A.2.3、命题 A.3.1；p.449–451（PDF）附录 B.4：LG 理论、手征环、LG 轨形与扭曲部分、例 B.4.1"
  - "A 级：Berglund–Hübsch 1993, Nucl. Phys. B393 (1993) 377–391, hep-th/9201014（书内未收，见 §11）：指数矩阵转置与相群条件的原始定义"
  - "A 级：Candelas–de la Ossa–Katz 1995, Nucl. Phys. B450 (1995) 267–292, hep-th/9412117 §3.1（书内 [CdK]）：广义转置法则与指数公式"
  - "B 级：SY01-24 术语表 #1 镜像对称 p.7、#54 多胞体 p.73、#58 反身多胞体 p.81；SY01-25 资料卡 04（HMS/SYZ 入口）"
status: draft
review:
  drafter: agent-240
  reviewer: lead
  blindtest: pending
glossary_refs: [SY01-24 术语表 第 1 条「镜像对称」p.7, 第 54 条「多胞体」p.73, 第 58 条「反身多胞体」p.81, _冲突表 T5、T6、U1]
symbols_refs: ['$q$', '$d$', '$\Delta$', '$A$', '$\hat q$', '$\hat d$', '$J$（全 1 矩阵）', '$[M:\varphi(\hat N)]$', '$\Omega$']
updated: 2026-11-20
---
# MS-24 Berglund–Hübsch 转置与轨形镜像
## 1. 一句话
用指数矩阵转置造出候选镜像，再除以相群取轨形。

## 2. 为什么需要它
- **衔接 Batyrev 与 Voisin–Borcea**：§4.4.3 要证 Voisin–Borcea 三维簇 $V_{\rm VB}^\circ$ 就是方程 (4.30) 的 Batyrev 镜像 $V_{\rm Bat}^\circ$，但书 p.093 明说这一对偶「并不显然」——$P(3,3,2,2,2)$ 是 Fano 环面簇而 $P(25,25,20,16,14)$ 不是（引理 3.5.6）。书内正是靠 [CdK] 的广义 BH 转置把 (4.30) 的指数数据搬到 (4.31)，才得到「更初等的证明」（PDF p.093、p.095）。
- **解释「缺失的镜像」**：§4.1.3（PDF p.083）说 7555 个加权射影 CY 的 Hodge 数图只显示部分对称性；§4.4.3 末段（PDF p.095）把「缺失的镜像」解释为不能用加权射影空间表示的 Batyrev 对偶。没有（广义）BH 转置这一机制，Batyrev 对偶的图表就补不全。
- **轨形是常态**：五次超曲面的镜像不是流形，而是五次/$G$ 的解奇异化（$G\cong(\mathbb Z_5)^3$，阶 125，PDF p.040）；附录 A 的轨形语言与附录 B.4 的 LG 轨形正是为此准备，§12.2.3（PDF p.425）又用 McKay 对应解释 $V/G$ 的 Hodge 数来源。

## 3. 定义（全假设）
分三层：BH 1993 的原始定义（书外 A 级）、本书实际使用的 [CdK §3.1] 广义版本（书内无一般陈述，只有示范）、轨形对象本身（附录 A、B.4）。

### 3.1 背景数据
$q=(q_0,\dots,q_4)$ 为归一化正整权，$P(q)$ 为对应加权射影空间，$d=\sum_i q_i$，坐标 $x_i$ 的权为 $q_i$。加权齐次超曲面写作 $f=\sum_{i=0}^4 c_i x^{a_i}$，$a_i\in\mathbb Z^5$ 为单项式指数向量，齐次性即 $a_i\cdot q=d$。

### 3.2 (a) Berglund–Hübsch 1993 的原始定义（A 级，书外）
假设（缺一不可）：

- (H1) $M=\{f=0\}\subset P(q)$ 是三维 Calabi–Yau 超曲面；$f$ 恰含 5 个单项式、5 个变量（minimal），故指数矩阵 $A=(a_{ij})$（行 $i$=单项式、列 $j$=变量）为 $5\times5$ 整矩阵且 $\det A\ne0$；
- (H2) $f$ 拟光滑：$\partial f/\partial x_j$ 只在原点同时为零（等价于 $f=0$ 在 $P(q)$ 中拟光滑）；
- (H3) 系数 $c_i\ne0$（作镜像族参数）；
- (H4) 转置权：存在正整向量 $\hat q$ 使 $\sum_i\hat q_i a_{ij}=\hat d\ (j=0,\dots,4)$、$\hat d=\sum_i\hat q_i$；$\hat q$ 整体缩放给出同一个 $P(\hat q)$，取本原即可。

构造：

- (B1) 转置多项式 $\hat f(y)=\sum_{j=0}^4\hat c_j\,y^{A^{\mathsf T}_j}$：转置后第 $j$ 个单项式的指数向量是 $A$ 的第 $j$ 列（即 $\hat f$ 的指数矩阵为 $A^{\mathsf T}$）；
- (B2) $\hat W=\{\hat f=0\}\subset P(\hat q)$；
- (B3) 镜像条件：设 $\mathcal Q_M\cong\mathbb Z_d$ 为量子对称（$x_j\mapsto\lambda^{q_j}x_j$，$\lambda^d=1$），$\mathcal G_M$ 为其余相群；取 $\hat W$ 相群的子群 $H$，使联合相群 $\mathcal Q_W:=\mathcal Q_{\hat W}\times H\cong\mathcal G_M$ 且商 $\mathcal G_W:=\mathcal Q_{\hat W}/H\cong\mathcal Q_M$；此时 $W:=\hat W/H$（按 $H$ 取轨形商）称为 $M$ 的镜像。$H$ 的存在性在 [BH93] 中逐例验证，没有闭式定义。特例：若 $A$ 与 $A^{\mathsf T}$ 只差行列重排（Fermat 型 $A=dI$ 即自转置），则 $\hat f$ 与 $f$ 同型，镜像为 $M/P_M$，$P_M$ 为保持全纯体积形式 $\Omega$ 的相群。

### 3.3 (b) 本书使用的广义版本（[CdK §3.1]；书 p.093–095 的示范）
输入是 Batyrev 数据而非多项式：

- (G1) $q$ 归一化且 $P(q)$ Fano（引理 3.5.6：所有 $q_i\mid d$）；
- (G2) $M=\{a\in\mathbb Z^5:q\cdot a=0\}$，$\Delta=\{a\in M_{\mathbb R}:a_i\ge-1\}$ 为自反多胞形（书 p.093：因 $P(q)$ Fano，$\Delta$ 自反；判据为命题 3.5.5）；
- (G3) 取 $\Delta\cap M$ 中 5 个格点 $a_0,\dots,a_4$，使 $0$ 在 $\operatorname{conv}(a_i)$ 内部；等价地，$a_i$ 满足唯一正互素关系 $\sum_i\hat q_i a_i=0$（书式 (4.33)，书称「可以验证」）；
- (G4) $A$ 为以 $a_0,\dots,a_4$ 为行的 $5\times5$ 矩阵。

输出：$\hat q=(\hat q_0,\dots,\hat q_4)$、$\hat d=\sum_i\hat q_i$，以及镜像方程

$$\hat f=\sum_{i=0}^4 c_i\,x^{e_i}=0,\qquad e_i\ \text{为}\ A+J\ \text{的第}\ i\ \text{列},\ J\ \text{为全 1 矩阵},$$

即「把 $\hat a_i$ 的每个分量加 1」再齐次化（书 p.095）。若每个 $e_i$ 的 $\hat q$-次数都等于 $\hat d$，则 $\hat f=0$ 是 $P(\hat q)$ 中的 $\hat d$ 次超曲面，镜像族由 $c_i$ 参数化。

指数（覆盖次数）：$\hat N=\mathbb Z^5/\mathbb Z\hat q$，$\varphi:\hat N\to M,\ \hat w_i=[e_i]\mapsto a_i$，书 p.094 给出

$$[M:\varphi(\hat N)]=\frac{\det(A+J)}{d\,\hat d},$$

并转引 [CdK §3.1]（书称该公式在 [CdK] 中「陈述但未给证明」）。

假设小结：$\det(A+J)\ne0$；$a_i$ 张成以 $0$ 为内点的单形；$\hat f$ 齐次性（$e_i\cdot\hat q=\hat d$）；取哪些格点由 [CdK] 规定，并非总取 $\Delta$ 的顶点——书内主例中 $a_2,a_3$ 就是棱内点（§4.1，另见 §11）。

### 3.4 轨形与轨形镜像
- 轨形（定义 A.2.1，PDF p.431）：每点有邻域解析等价于 $U/G$ 的原点邻域，$G\subset GL(d,\mathbb C)$ 为除恒等元外不含复反射的有限子群；「轨形」与「$V$ 流形」可互换；环面簇情形等价于扇单纯、$G$ 为有限 Abel 群。
- 三维 CY 轨形：$V$ 是 CY 当且仅当 $K_V$ 平凡且 $H^i(V,\mathcal O)=0\ (1\le i\le d-1)$（PDF p.431）；三维极小 CY 轨形光滑（推论 A.2.3，PDF p.431–432），但解奇异化并不唯一（PDF p.040：不同选法复模相同、$B$ 模型关联函数相同）。
- 物理侧：LG 轨形（附录 B.4，PDF p.449–451）——超势 $F$ 加权齐次、手征环 $\mathbb C[\phi]/(\partial F)$；取 $\eta$ 为本原 $d$ 次单位根，对 $(\eta^{d_1},\dots,\eta^{d_k})$ 的作用取轨形，得扭曲部分与扭曲真空 $V_i$；例 B.4.1 缺的 3 个形变在 $V_4$ 中补足。

**本书用法**：Cox–Katz 没有给出 BH 转置的一般陈述（p.093 明言「这里不描述一般情形，而说明它对 $P(q)$、$q=(3,3,2,2,2)$ 如何起作用」），也没有「轨形镜像」的独立定义；书内「轨形」按附录 A 的解析/代数几何定义使用，「LG 轨形」按附录 B.4 使用，§4.4.3 只在一个例子上演示 [CdK] 的广义法则。与 [BH93] 相比，广义版本多了全 1 平移 $J$、少了相群条件 $H$ 的显式构造——这一出入见 §11。

## 4. 最小例子（能算出）
### 4.1 书内主例：$P(3,3,2,2,2)$ 的 Fano 超曲面 $\leftrightarrow$ $P(25,25,20,16,14)$
**第 1 步（Fano 与 $\Delta$）** $q=(3,3,2,2,2)$，$d=12$；$3\mid12$、$2\mid12$，故 Fano（引理 3.5.6，PDF p.070），$\Delta$ 自反。$\Delta\cap M$ 的 5 个格点（书式 (4.32)，PDF p.094）为

$$a_0=(3,-1,-1,-1,-1),\ a_1=(-1,3,-1,-1,-1),\ a_2=(-1,-1,4,0,-1),$$
$$a_3=(-1,-1,-1,4,0),\ a_4=(-1,-1,-1,-1,5).$$

逐坐标代入 $q\cdot a_i$：$a_0$ 给 $9-3-2-2-2=0$；$a_2$ 给 $-3-3+8+0-2=0$；$a_4$ 给 $-3-3-2-2+10=0$，均满足；各坐标 $\ge-1$，故 $a_i\in\Delta\cap M$。

**第 2 步（对偶权）** 书式 (4.33) 断言 $25a_0+25a_1+20a_2+16a_3+14a_4=0$。验证第 2 坐标：$-25-25+80-16-14=0$；第 3 坐标：$-25-25+0+64-14=0$；第 4 坐标：$-25-25-20+0+70=0$。故 $\hat q=(25,25,20,16,14)$、$\hat d=100$。

**第 3 步（$A+J$ 与指数）** 以 $a_i$ 为行：

$$A+J=\begin{pmatrix}4&0&0&0&0\\0&4&0&0&0\\0&0&5&1&0\\0&0&0&5&1\\0&0&0&0&6\end{pmatrix},\qquad \det(A+J)=4\cdot4\cdot5\cdot5\cdot6=2400,$$

指数 $=\dfrac{2400}{d\,\hat d}=\dfrac{2400}{12\cdot100}=2$（书 p.094 引 [CdK §3.1]；书因此说 $\varphi_*$ 是 2:1 覆盖，PDF p.094–095）。

**第 4 步（镜像方程）** $A+J$ 的五列为 $(4,0,0,0,0)$、$(0,4,0,0,0)$、$(0,0,5,0,0)$、$(0,0,1,5,0)$、$(0,0,0,1,6)$，齐次化得

$$\hat f=c_0u^4+c_1v^4+c_2y^5+c_3yz^5+c_4zw^6=0,$$

正是书式 (4.31)（PDF p.094）。次数检验：$4\cdot25=100$、$5\cdot20=100$、$20+5\cdot16=100$、$16+6\cdot14=100$，各单项式 $\hat q$-次数都等于 $\hat d$ ✓。

**第 5 步（非 Fano 侧）** $\hat d=100$，但 $16\nmid100$、$14\nmid100$，故 $P(25,25,20,16,14)$ 非 Fano（引理 3.5.6）。这正是书 p.093 说「(4.30) 与 (4.31) 之间的对偶性并不显然」的原因；书用 2:1 覆盖与椭圆曲线二阶同源把它归到 Voisin–Borcea 镜像（PDF p.095）。

**第 6 步（Hodge 数）** (4.30) 的 Voisin–Borcea 数据为 $(N,N')=(1,10)$（不动点集 $y^6+z^6+w^6=0$ 是 $\mathbb P^2$ 中 6 次曲线，亏格 $(6-1)(6-2)/2=10$；定理 4.4.2，PDF p.089），于是

$$h^{1,1}(V)=11+5\cdot1-10=6,\qquad h^{2,1}(V)=11+5\cdot10-1=60,$$

镜像 $(N,N')=(10,1)$ 给出 $(h^{1,1},h^{2,1})=(60,6)$，即 $\chi(V)=2(6-60)=-108$、$\chi(V^\circ)=+108$，Hodge 数互换 ✓。

### 4.2 锚例：Fermat 五次自转置
$f=x_0^5+\cdots+x_4^5\subset\mathbb P^4$，$q=(1,1,1,1,1)$，$d=5$；$\Delta=\{a\in\mathbb Z^5:\sum_i a_i=0,\ a_i\ge-1\}$ 的 5 个顶点是 $a_i=5e_i-(1,1,1,1,1)$，即 $(4,-1,-1,-1,-1)$ 等（书 PDF p.084）。

- **数据与指数**：$A=5I-J$，故 $A+J=5I$，$\det(A+J)=5^5=3125$；$\sum_i a_i=5\cdot1-5\cdot1=0$，正互素关系给出 $\hat q=(1,1,1,1,1)$、$\hat d=5$；指数 $=3125/(5\cdot5)=125$。
- **与 $|G|=125$ 吻合**：书 p.084–085 独立算出 $\Delta$ 的顶点生成 $M$ 中指数为 125 的子格 $M_1$，且 $M/M_1\cong G$（Greene–Plesser 群，$G=\{(a_0,\dots,a_4)\in(\mathbb Z_5)^5:\sum a_i\equiv0\}/\mathbb Z_5$，阶 $5^4/5=125$，PDF p.040）；$\mathbb P_{\Delta^\circ}=\mathbb P^4/G$。同一条指数公式给出 125，与相群阶一致。
- **镜像仍是同一个方程**：$A+J=5I$ 的每一列都是 $5e_i$，故 $\hat f=\sum_i c_i x_i^5$——自转置。但镜像空间是 $\mathbb P_{\Delta^\circ}=\mathbb P^4/G$ 中的超曲面族（书 eq:quintic-general-mirror，PDF p.085 的 $a_0x_0^5+\cdots+a_5x_0x_1x_2x_3x_4=0$）的解奇异化（PDF p.040），不是 $\mathbb P^4$ 中同一条超曲面。
- **Hodge 数**：$h^{1,1}(V)=1$（超曲面，Lefschetz）；$h^{2,1}(V)=\dim(R/I)_5=\binom{9}{4}-25=126-25=101$，其中 $R=\mathbb C[x_0,\dots,x_4]$、$I=(\partial f/\partial x_i)=(x_i^4)$，其 5 次部分由 25 个单项式 $x_i^4x_j$ 张成（Griffiths 留数理论，B 级标准）。故 $\chi(V)=2(1-101)=-200$，镜像 $h^{1,1}=101$、$h^{2,1}=1$、$\chi=+200$，互换 ✓。

## 5. 关键性质（3–6 条，带出处）
| # | 性质 | 出处（书页/文献） | 备注 |
|---|------|------------------|------|
| 1 | 转置是对合：转置两次回到原多项式；只有「5 单项式/5 变量、指数矩阵可逆」的 minimal 情形封闭 | [BH93] §1；书未给一般陈述 | 一般多项式转置后未必再 minimal |
| 2 | 自转置（Fermat 型）时镜像=原模型除以相群：五次情形镜像=五次/$G$，$G$ 阶 125 | [BH93]；书 PDF p.040、p.084–085 | 这是 Greene–Plesser 构造的 BH 解释 |
| 3 | 对偶权由唯一正互素关系给出：$\sum_i\hat q_i a_i=0$，$\hat d=\sum_i\hat q_i$ | 书式 (4.33)，PDF p.094 | 书称「可以验证」，一般存在性待核 |
| 4 | 指数公式 $[M:\varphi(\hat N)]=\det(A+J)/(d\hat d)\in\mathbb Z$ | 书 PDF p.094（引 [CdK §3.1]，书称未给证明） | 书内主例 $=2$；五次 $=125$ |
| 5 | Fano/非 Fano 互补：原模型 Fano（$q_i\mid d$）时镜像通常非 Fano（例中 $16\nmid100$、$14\nmid100$） | 书 PDF p.093（引理 3.5.6）、p.095 | 故不能直接用 Batyrev 对偶，须 BH 覆盖解释 |
| 6 | 镜像只在族/形变意义下相同：2:1 覆盖由 $E\to E'$ 二阶同源解释，$E$ 与 $E'$ 互为形变 | 书 PDF p.095 | 一般 $(N,N')$ 的严密性待核 |

## 6. 推导流程（D1…Dn）
- **D1** $P(q)$ Fano ⇒ $\Delta$ 自反：由 $q_i\mid d$（引理 3.5.6，PDF p.070）与命题 3.5.5（$\Delta$ 自反 $\Leftrightarrow P_\Delta$ Fano 且 $\Delta$ 为反典范多胞形），见书 p.093。
- **D2** 取格点与对偶权：$a_0,\dots,a_4\in\Delta\cap M$ 张成以 $0$ 为内点的单形 ⇒ 唯一正互素关系 $\sum_i\hat q_i a_i=0$（书式 (4.33)，PDF p.094）。
- **D3** 格与映射：$\hat N=\mathbb Z^5/\mathbb Z\hat q$、$\hat w_i=[e_i]$、$\varphi:\hat N\to M,\ \hat w_i\mapsto a_i$；书 p.094 断言 $\varphi$ 良定义并诱导 $\hat N_{\mathbb R}\cong M_{\mathbb R}$。
- **D4** 环面几何：取极大射影细分 $\Sigma^\circ$，得环面爆破 $\hat X\to P(\hat q)$ 与有限态射 $\varphi_*:\hat X\to X_{\Sigma^\circ}$，其次数为 $[M:\varphi(\hat N)]$（PDF p.094）。
- **D5** 指数计算：$d=q\cdot(1,\dots,1)$、$\hat d=\hat q\cdot(1,\dots,1)$，$[M:\varphi(\hat N)]=\det(A+J)/(d\hat d)$（PDF p.094，引 [CdK §3.1]）。
- **D6** 拉回超曲面：对偶映射 $\varphi^t:N\to\hat M$ 使 $w_i\mapsto\hat a_i$（$A$ 的第 $i$ 列），$f=\sum c_it^{w_i}\mapsto\hat f=\sum c_it^{\hat a_i}$，再把每个分量加 1 齐次化（PDF p.095）。
- **D7** 结论：$\varphi_*:V_{\rm VB}^\circ\to V_{\rm Bat}^\circ$ 为 2:1；由 $E\to E'$ 二阶同源与形变性得 $V_{\rm Bat}^\circ=V_{\rm VB}'^\circ$，故就镜像族而言一致（PDF p.095）。
- **D8** 一般化方向：7555 列表中的「缺失镜像」= 不能用加权射影空间表示的 Batyrev 对偶，用非 Fano 解释的变体处理（PDF p.095 末段；铺垫见 p.083）。

## 7. 常见误解与反例（≥2）
1. **误解：BH 转置就是「把指数矩阵转置」。** 反例：(4.30) 的指数矩阵是 $\operatorname{diag}(4,4,6,6,6)$，转置后不变，按字面理解得到的还是 (4.30) 本身，得不到 (4.31)；书 p.093 也明言不描述一般情形，实际演示的 [CdK] 法则以 $\Delta\cap M$ 的 5 个格点为输入、输出 $A+J$（多一个全 1 平移，PDF p.094–095）。经典 BH 与广义法则不是同一陈述（§11）。
2. **误解：模型自转置 ⇒ 镜像就是它自己。** 反例：Fermat 五次自转置，但镜像不是 $\mathbb P^4$ 中同一个五次簇，而是五次/$G$ 的解奇异化（PDF p.040、p.084–085）；Hodge 数 $1/101\leftrightarrow101/1$、$\chi$ 由 $-200$ 变 $+200$；此外 BH 条件还要求相群同构 $\mathcal Q_W\cong\mathcal G_M$、$\mathcal G_W\cong\mathcal Q_M$（[BH93] 式 (1.2)），并不是恒等。
3. **误解：$\varphi_*$ 是 2:1 就说明 $V_{\rm VB}^\circ\ne V_{\rm Bat}^\circ$，BH 证明失败。** 边界：2:1 来自 $E\to E'$ 的二阶同源，$E$、$E'$ 互为形变，故两者在镜像族意义下相同（PDF p.095）；但书内只对 $(N,N')=(1,10)$ 情形验证，一般情形的严密性待核。
4. **误解：轨形镜像 = 直接取商簇 $V/G$。** 反例：$\mathbb P^4/G$ 奇异，超曲面继承奇点（PDF p.040），必须解奇异化并保持 CY；三维 Gorenstein 终端轨形虽光滑（推论 A.2.3，PDF p.431–432），解消仍不唯一（PDF p.040）。

## 8. 在文献中的坐标
| 文献 | 位置 | 它在那里干什么 |
|------|------|----------------|
| Cox–Katz 1999 | PDF p.093–095（印刷 p.070–072），§4.4.3 | 书内唯一应用：用 [CdK] 广义 BH 转置证明 $V_{\rm VB}^\circ=V_{\rm Bat}^\circ$；式 (4.30)–(4.33)；指数 $2400/(12\cdot100)=2$；2:1 覆盖；末段「缺失的镜像」 |
| Cox–Katz 1999 | PDF p.089–092 §4.4.1–4.4.2；p.040 §2.2；p.084–085 §4.2；p.431–433 附录 A；p.449–451 附录 B.4；p.425 §12.2.3 | $N/N'$ 与定理 $h^{1,1}=11+5N-N'$；五次镜像=五次/$G$ 解奇异化（$M/M_1\cong G$，阶 125）；轨形定义 A.2.1 与推论 A.2.3；LG 轨形与扭曲部分；McKay 对应与轨形 Euler 数 [Vafa1,Roan2] |
| SY01-24 术语表 | #1「镜像对称」p.7、#14「大复结构极限」p.18、#54「多胞体」p.73、#58「反身多胞体」p.81 | 未收 orbifold / Berglund–Hübsch / 转置 / LG 条目，无定义可逐条比对。**冲突：T5（多胞体 vs 本书「多胞形」）、T6（反身多胞体 vs 本书/_冲突表裁定「自反多胞形」）**——本卡按本书口径用「多胞形/自反多胞形」 |
| SY01-25 资料卡 04 | 一、核心术语 25 条（l.7 HMS、l.37 [Ko]/[SYZ]） | 未收轨形/BH/LG 条目；其镜像对称入口为 SYZ/T-对偶 + HMS。**冲突：U1（镜像对称层次）**——本卡按本书把 BH 转置当构造性定理，不把 HMS 设为唯一主线 |
| Berglund–Hübsch 1993 | Nucl. Phys. B393 (1993) 377–391；hep-th/9201014，§1 式 (1.1)–(1.2)、Table 1–2 | 原始定义：指数矩阵转置、相群条件 $\mathcal Q_W\cong\mathcal G_M$、$\mathcal G_W\cong\mathcal Q_M$、Fermat 型自转置、$D_k$ 非自转置反例（**书内未收此文**，见 §11） |
| Candelas–de la Ossa–Katz 1995 | Nucl. Phys. B450 (1995) 267–292；hep-th/9412117 §3.1（书 p.093/094 引） | 书内「广义 Berglund–Hübsch 转置法则」的出处；指数公式的陈述（书称未给证明）；7555 例与「缺失镜像」的处理 |
| Batyrev 1994（书内 [Batyrev4]） | J. Algebraic Geom. 3 (1994) 493–535；alg-geom/9310003（定理号待核） | Batyrev 对偶：自反多胞形给出镜像族；本卡用 $q_i\mid d$（引理 3.5.6）连接 BH 转置；附录 A 命题 A.2.2 引其定理 2.2.9（书引，页待核） |

## 9. 前置与后继
- 前置：**MS-09**（自反多胞形；命题 3.5.5、引理 3.5.6 是本卡 §3/§4 判据来源）；**MS-23**（nef 分拆与 Batyrev 镜像构造，第 4 章 §4.5；本卡需先有 Batyrev 对偶框架，该卡尚未写出，见 §11）；另建议读 MS-07（环面簇/扇）、MS-08（多胞形与扇的对应）、MS-20（附录 B 的 LG/SCFT 语言）。
- 后继：第 4 章 §4.4 Voisin–Borcea（本卡主要应用）；第 12 章 §12.2.2 K3 与 Arnold 奇异对偶、§12.2.3 McKay 对应（PDF p.424–425）；第 8 章 GW/镜像定理（$B$ 模型侧陈述）；外部后继 [CdK]、[BK2] 综述。

## 10. 形式化接口（Lean 可 sorry）
```lean
import Mathlib.LinearAlgebra.Matrix.Determinant
import Mathlib.Analysis.Convex.Hull

open Matrix

/-- 权 q 的 Fano 判据（书 p.070 引理 3.5.6）：d = Σ q_i 且每个 q_i ∣ d。 -/
def IsFanoWeight (q : Fin 5 → ℕ) (d : ℕ) : Prop :=
  (∑ i, q i = d) ∧ ∀ i, 0 < q i ∧ q i ∣ d

/-- 广义 BH 转置的输入：Δ ∩ M 的五个格点 a_i（行向量）。 -/
structure BHData where
  a : Fin 5 → Fin 5 → ℤ
  q : Fin 5 → ℕ
  d : ℕ
  fano : IsFanoWeight q d
  memM : ∀ i, (∑ j, (q j : ℤ) * a i j) = 0
  originInterior : (0 : Fin 5 → ℝ) ∈
    interior (convexHull ℝ (Set.range (fun i j => (a i j : ℝ))))

/-- 书内主例的 A+J（PDF p.094）。 -/
def voisinExponents : Matrix (Fin 5) (Fin 5) ℤ :=
  !![4, 0, 0, 0, 0; 0, 4, 0, 0, 0; 0, 0, 5, 1, 0; 0, 0, 0, 5, 1; 0, 0, 0, 0, 6]

/-- 覆盖指数 [M : φ(N̂)] = det(A+J)/(d·d̂)（书 p.094，引 [CdK §3.1]）。 -/
def coveringIndex (A : Matrix (Fin 5) (Fin 5) ℤ) (d dhat : ℕ) : ℚ :=
  ((A.det : ℚ) / (d * dhat))

/-- 书内主例：$q=(3,3,2,2,2)$、$d=12$、$\hat q=(25,25,20,16,14)$、$\hat d=100$ 时指数为 2。 -/
theorem voisinBorceaIndex : coveringIndex voisinExponents 12 100 = 2 := by
  sorry

/-- 唯一正互素关系给出对偶权（书式 (4.33)）；一般存在性未证。 -/
theorem existsUniqueDualWeight (D : BHData) :
    ∃ qhat : Fin 5 → ℕ, (∀ i, 0 < qhat i) ∧ (∑ i, (qhat i : ℤ) • D.a i = 0) := by
  sorry
```

接口语义：`BHData` 的五个格点决定 $A+J$ 与镜像方程；系数 $c_i$ 的族与相群作用 $H$ 未形式化（依赖 LG 轨形的物理定义，见 §11）。

## 11. 待核清单
- [ ] 队列位置提示只写「附录 A；第 12 章」，漏了正文唯一应用处 §4.4.3（PDF p.093–095）与物理侧定义处附录 B.4（PDF p.449–451）；按 MS-09 卡先例登记，待队列维护者补
- [ ] 本书参考书目未收 Berglund–Hübsch 1993 原文（references.tex 只有 [BK1]/[BK2]/[BKK]），§8 原始文献行取自书外；待确认是否有意省略
- [ ] 书 p.093 明言不描述一般情形；p.094 指数公式转引 [CdK §3.1] 且书称未给证明——待核 [CdK §3.1] 的完整陈述与证明位置
- [ ] p.094 的 5 个格点如何从 (4.30) 算出、取点规则是什么；且 $a_2=(-1,-1,4,0,-1)$、$a_3=(-1,-1,-1,4,0)$ 并非 $\Delta$ 的顶点（$\Delta$ 的顶点为 $v_i=(12/q_i)e_i-u$，$u=(1,1,1,1,1)$），书只说「张成以 0 为内点的单形」——待核 [CdK §3.1]
- [ ] $\hat q$ 的存在唯一性（正互素关系）书称「可以验证」，未给一般证明；待核
- [ ] 五次情形 $A+J=5I$、$\det=3125$、指数 125 与 $|G|=125$（PDF p.040、p.084–085 的 $[M:M_1]=125$）是巧合还是 BH 法则的必然——待核；本卡 §4.2 只作数值互证
- [ ] 五次镜像是「五次/$G$ 的解奇异化」的严格出处在书 p.040（Greene–Plesser [GPl]，原书未展开）；$h^{2,1}=101$ 本卡用 Jacobian 环算出，与书 p.082 的 Batyrev 公式及 p.085 的「$\Delta^\circ$ 收缩」叙述的关系待核
- [ ] 「相群」「量子对称」：本卡按 [BH93] 的 $\mathcal Q_M/\mathcal G_M$ 与附录 B.4 的相群作用使用；本书正文似无系统定义，中文译名（相群/相位群）待统一
- [ ] SY01-24 术语表未收 orbifold/转置/LG 条目、SY01-25 资料卡 04 未收 BH/LG 条目：建议在 _冲突表 登记术语缺环（T5/T6 已裁定，U1 已登记）
- [ ] MS-23 卡尚未写出（资料卡目录中无该卡）；本卡 prereq 暂指向 _queue.md 第 31 行（MS-23 行），待 MS-23 完成后补链接与前置内容

注：本卡 status 保持 draft（待核非空）；以上条目关闭后再考虑 frozen。
