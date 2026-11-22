# 第 4 章通读笔记 · Artin L Functions（E. de Shalit）

底本：PDF 79–93 = 印刷页 73–87；页图 `work/pages/ch04/p0079.png … p0093.png`（150 dpi，文件名数字即 PDF 页）。

## 一、三句话主旨

1. Artin 1923 年把 Dirichlet L 函数从“一维特征”推广到 Galois 群 $G_{\mathbb{Q}}$ 的任意复特征，办法是只看惯性不变量上的 Frobenius 作用，逐素位乘起来。
2. 这样定义的 $L(\chi,s)$ 在函数域情形由 Weil 的上同调理论完全解决（解析延拓、函数方程、RH 全有）；数域情形只能靠 Brauer 诱导定理把它化成若干一维情形之积，因此只得到**亚纯**延拓，解析性正是 Artin 猜想。
3. 全章末节把二维情形与模形式对接：Deligne–Serre 给出权 1 新形式到二维复表示的构造，Weil 逆定理给出反向，Langlands–Tunnell 解决除二十面体外的所有类型，二十面体情形即今日“模性提升”的起点。

## 二、体裁与语气

- 综述（survey），据 2001 年 3 月耶路撒冷教学会议报告写成；作者在标题脚注里自嘲“没有任何结果——但所有错误——属于作者”。
- 有大量“历史点名”（Kronecker 1853、Weber 1886、Artin 1923、Brauer 1947、Weil 1948、Deligne 1974、Langlands 1970、Taylor 1997），译文一律保留年份与原文人名拼写。
- 两处**作者自述的取舍**要留住：坏 Euler 因子“由函数方程好看这一愿望所决定”；Brauer 定理“只能给亚纯，不能给解析”。
- 每节末有 REFERENCES 小段，照录（英文原书目，不改动、不译书名）。

## 三、逐节内容地图（节号按原书，公式号同）

- **1 引言**：本原 Dirichlet 特征 $\chi \bmod m$，$K=\mathbb{Q}(\zeta)$，$G\cong(\mathbb{Z}/m\mathbb{Z})^\times$；(1.1) $\chi_{\mathrm{Gal}}(\sigma_p)=\chi(p)$；(1.2) Euler 积；Kronecker–Weber；Artin 1923 的推广。
- **2 有限群的表示**：半单性；(2.1) 特征；(2.2) 类函数内积；(2.3) $\sum n_i^2=|G|$。
  - **2.1 表示上的运算**：直和、张量积、反偶、限制、诱导；(2.4) 诱导空间 $V=\{f:G\to W,\ f(hg)=\rho(h)f(g)\}$；(2.5) 右平移；(2.6) $\operatorname{Ind}$ 的特征公式；(2.7) Frobenius 互反律；(2.8) 投影公式。正则表示 $\operatorname{Ind}_1^G 1$、单项表示、虚拟表示与表示环 $R_G$。
- **3 Artin L 函数**
  - **3.1 整体域的 Galois 群**：整体域、分解群 $G_{\bar v}$、惯性群 $I_{\bar v}$、$\sigma_v$；阿基米德位的 $G_{\bar v}$ 约定（实/复、复/实）；分歧位有限。
  - **3.2 定义**：(3.1) 乘积；(3.2) $L_v=\det(1-\sigma_vq_v^{-s}|V^{I_{\bar v}})^{-1}$；坏素位与“补丁因子”的说明；(3.3) $\log\det$ 展开；(3.4) 陪集平均；(3.5) $\log L_v$。
  - **3.3 函数域情形**：(3.6) $\operatorname{Jac}[\ell^r]\cong(\mathbb{Z}/\ell^r)^{2g}$；(3.7) $H^1=\operatorname{Hom}(\varprojlim\operatorname{Jac}[\ell^r],\mathbb{Q}_\ell)$；(3.8) $\rho$-等型分量；(无号) $\log L=\sum_n\{|G|^{-1}\sum_g\chi(g^{-1})\Lambda(gF^n)\}q_v^{-ns}/n$；(3.9) $L=Z$；(3.10) $Z=\det(1-Ft|H^1(\rho))$；定理 3.1（Weil）：(i) 多项式 (ii) (3.11) 函数方程 (iii) RH。
  - **3.4 初步性质**：可加性、(3.12) 诱导、(3.13) 膨胀、(3.14)(3.15) 类域论、(3.16) $\zeta_K=\zeta_k\prod_{\chi\ne1}L(\chi,s)^{\chi(1)}$。
- **4 Brauer 定理、亚纯延拓与函数方程**
  - **4.1 阿基米德 Euler 因子**：(4.1) $\Gamma_{\mathbb{R}},\Gamma_{\mathbb{C}}$；(4.2) $n_\pm$；(4.3) $L_v$。
  - **4.2 Artin 导子**：(4.4) $f(\chi,v)=|G_0|^{-1}\sum_i|G_i|\operatorname{codim}V^{G_i}$；(4.5) $\mathfrak{f}(\chi)=\prod v^{f(\chi,v)}$；整数性（Artin / Hasse–Arf）。
  - **4.3 亚纯延拓与函数方程**：(4.6) $\Lambda(\chi,s)$；(4.7) $\Lambda(\chi,1-s)=W(\chi)\Lambda(\tilde\chi,s)$；定理 4.1；两步走（类域论 + Brauer）。
  - **4.4 Brauer 诱导定理**：定理 4.2；$p$-初等子群；(4.8) $\operatorname{Ind}_p$；Brauer–Tate 1951 证明梗概（幂零群全单项、$A=\mathbb{Z}[\zeta]$、两条构造）；(4.9) $\Lambda(\chi,s)=\prod\Lambda(\chi_i,s)^{n_i}$；GRH 推论。
- **5 Artin 猜想**：猜想 5.1；推论 5.2；例 5.1（Aramata–Brauer，增广表示）；归入 Langlands 纲领。
- **6 局部常数**：(6.1) $W(\chi)=\tau(\chi)/(\sqrt f i^\delta)$；(6.2) Gauss 和；三条初等性质；实特征与正交性、Fröhlich–Queyrut；(6.3) $W=\prod_vW_v$；(6.4) $\mathfrak{f}_v(\chi)$；(6.5) $W_v=\tau(\chi_v)/\sqrt{N\mathfrak{f}_v}$；Langlands 1970 的宣布与 Deligne 1974 的证明；(6.6)–(6.10) 良定性与可延拓/强可延拓的区别。
- **7 与模形式的关系（GL(2)）**：奇表示；定理 7.1（Deligne–Serre）(7.1)(7.2)；模 $\ell$ 逼近与黏合；Rankin 的解析结果；定理 7.2（Weil 逆定理）(7.3)；强 Artin 猜想；有限子群分类 $A_4,S_4,A_5$；定理 7.3（Langlands–Tunnell）；二十面体情形与 Taylor。

## 四、逐条核过的公式（抽取件不可信处）

pdftotext 把绝大多数公式打散，以下全部回页图核对，页图坐标已记在 `work/crop_*.png`：

- (3.11) 的 $\epsilon=at^{d(\rho)}$、$a=(-1)^{d(\rho)}\det(F|H^1(\bar Y,\mathbb{Q}_\ell)(\rho))$（p0084 放大核对）。
- (6.1) 分母是 $\sqrt f\,i^\delta$（p0089 放大核对），不是 $\sqrt{f i^\delta}$。
- (4.2) 的 $n_-=\dim V/V^{G_{\bar v}}$ 是**商空间**维数，不是 $V^{G_{\bar v}}$ 的余维（两者数值相同，但写法不同）。
- (2.4) 的函数方程是 $f(hg)=\rho(h)f(g)$（左协变），(2.5) 却是右平移 $f(g'g)$。
- (3.8) 是 $\operatorname{Hom}_G(V,H^1\otimes\overline{\mathbb{Q}}_\ell)$，不是 $\operatorname{Hom}(V,H^1)$。
- (4.6) 里 $\mathfrak{f}(\chi)$ 的指数是 $|d_k|^{\chi(1)}$，即判别式带 $\chi(1)$ 次幂。

## 五、疑点清单（未在译文中擅自改动者）

1. **$|G|=p^a l$ 的字母冲突**（p.82）：书中用小写字母 $l$（ell）表示 $|G|/p^a$，与全文表示素数的 $\ell$ 只差字体。已出译注说明，正文照录。
2. **"Tunnel" 拼法**（p.87，定理 7.3）：标准拼法为 Tunnell（J. Tunnell）。译文正文用 Tunnell，脚注说明原书作 Tunnel。
3. **(3.11) 中 $\epsilon$ 含 $t^{d(\rho)}$**：字面上 $\epsilon$ 不是常数。已按原书照录，并在译注中解释为“把 $t^{d}$ 并入根数”的 Weil 式写法；未判为笔误，因为无法排除作者用的是这一套约定。
4. **定理 7.3 中 $G=\operatorname{Im}(\rho)$ 与括注 $\tilde G$ 混用**：前面定义 $G\subset GL(2,\mathbb{C})$、$\tilde G$ 为其在 $PGL(2,\mathbb{C})$ 中的像，定理陈述里两者混写。译文照录 $G$，括注照录 $\tilde G$。
5. **$F$ "of order $q$"**（p.77）：字面是“$q$ 阶”，但 Frobenius 的阶是 $q$ 的幂、不动域为 $\mathbb{F}_q$。译文作“$q$ 次幂的 Frobenius 自同构”，不另出注。
6. **例 5.1 的非 Galois 情形**：$\zeta_K/\zeta_k$ 全纯对非 Galois $K/k$ 未决，书中说“由猜想可推出”，属实；译注只解释技术原因，不展开。
7. **参考文献 [2] "Notes d'un cours a Orsay"**：法语应为 "à Orsay"，原书漏音符；照录，不改。

## 六、新增术语（本库此前未统一者，本章固定用法）

| 英文 | 本章译法 | 备注 |
| --- | --- | --- |
| Artin conductor | Artin 导子 | 记号 $\mathfrak{f}(\chi)$ |
| inertia group | 惯性群 | 与“分解群”对 |
| higher ramification groups | 高阶分歧群 | $G_0\supset G_1\supset\cdots$ |
| monomial (representation/character) | 单项（表示/特征） | |
| virtual representation | 虚拟表示 | |
| class function | 类函数 | |
| regular representation | 正则表示 | |
| contragredient | 反偶 | $\rho^\vee$、$\tilde\chi$ |
| Frobenius reciprocity | Frobenius 互反律 | |
| projection formula | 投影公式 | |
| $p$-elementary subgroup | $p$-初等子群 | |
| augmentation representation | 增广表示 | |
| isotypical component | 等型分量 | |
| Artin root number | Artin 根数 | $W(\chi)$ |
| local constant | 局部常数 | $W_v(\chi)$ |
| augmented L-series | 增广 L 级数 | $\Lambda(\chi,s)$ |
| extendibility / strong extendibility | 可延拓性 / 强可延拓性 | Langlands 术语 |
| newform / eigenform | 新形式 / 本征形式 | |
| nebentypus | nebentypus（旁特征） | 保留原文 |
| odd (representation) | 奇的 | $\det\rho$ 把复共轭送到 $-1$ |
| strong Artin conjecture | 强 Artin 猜想 | |
| modularity | 模性 | |

## 七、编号与版式处理

- 原书章内节号是 1–7、小节 2.1/3.1–3.4/4.1–4.4，公式号 $(n.m)$ 与小节号同源。为使 $(2.1)$ 出现在第 2 节、$(4.9)$ 出现在第 4 节，本章开头先 `\let\chFourOldTheSection\thesection`，再把 `\thesection` 局部改为 `\arabic{section}`；章末用 `\let\thesection\chFourOldTheSection` 恢复 book 类原义，以免影响后一章。
- `\ob` 在本章无处可用：原书没有“编号独立段落”这类块，编号只出现在公式与定理上，故公式用 `\tag`、定理用粗体标题，均照原书号。此点已在交稿说明中注明。
- 定理/猜想/例一律作 `\par\medskip\noindent\textbf{定理 3.1（A.~Weil）}\quad`（与 ch02 一致）。
- 译注 13 条，全部为 A 级（经典教材、综述或原书自身），未用 B 级网络源。分布：§1 一条、§2.1 一条、§2 末一条、§3.2 一条、定理 3.1 后一条、§3.4 一条、§4.1 一条、§4.2 一条、§4.4 两条、§5 一条、§6 一条、§7 一条。
- 定理 7.3 标题作 Tunnell，脚注说明原书作 “Tunnel”；其余原书笔误一律照录，见疑点清单。

## 八、编译自测（隔离目录 `work/tmp_ch04/`，只载入本章）

- 做法：复制 `src/main.tex`，删去除 ch04 之外的 `\InputIfFileExists` 行，复制 `src/chapters/ch04.tex`，在该目录连跑三遍 xelatex。
- 结果：0 error、0 undefined、0 overfull、0 underfull、0 missing character。日志里只剩主文件前言自带的 3 条 xeCJK “Redefining CJKfamily” 警告，与本章无关。
- 版面：正文 14 页（自章首页起算），章题、作者、节号 1–7 与公式号 $(n.m)$ 全部照原书。末页只剩 §7 的三条参考文献，是隔离编译断页所致；全书合排时会随前后章移动。
- §7 标题含数学，曾触发 hyperref 的 “Token not allowed in a PDF string” 警告，已用 `\texorpdfstring` 消除。

