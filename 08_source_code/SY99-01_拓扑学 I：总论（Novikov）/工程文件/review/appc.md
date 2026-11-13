# 核验报告 · appc（原书 p.292–298，附录 §4：三维流形新不变量与 TQFT）

核验人：译者戊　　作者：译者辛　　日期：2026-11-10

## 结论
通过（已作两处忠实度修正）。逐页核对 7 页（`pages\p299.png`–`p305.png`）：§4 全节、两个编号公式 (4.1)(4.2)、一个无编号 Remark、5 条 Tutor Note、两张裁图（图 A.13、图 A.14）与全部公式均与原书对得上，无内容性错误。原先的「Dijgraaf 拼写照原」与「p.294 页标记跨句」已处理，现只剩 1 条措辞建议。

## 必须改（影响正确性）
无。（本轮已由核验人完成两处修正，见文末「修正记录」。）

## 建议改（可读性/忠实度）
1. **第 107 行（原书 p.296）**：`(a) 对的 $0$-圈关联函数等于 $\eta_{ij}$` 中「对的」是 "of pairs" 的硬译，单独成句略显生硬；建议改「一对场的 $0$-圈关联函数等于 $\eta_{ij}$」。同理 (b) 的「三元组的」建议与之统一为「三个场的」或「三元组的」。

## 抽查记录（逐页）
- **p.292**（`pages\p299.png`）：$Z(M^3)=\int DA\exp\{ikS(A)\}$、$i^2=-1$；$k$ 为整数的依据（耦合常数的拓扑量子化：Novikov 1981、Deser–Jackiw–Templeton 1982、Witten 1983；$\exp\{ikS\}$ 单值）；CS 作用量「局部形式」$S(A)=\Tr(\partial_iA_i-\partial_jA_j+\frac23A^3)$（原书排印如此，Note 正确）；Heegaard 分解与 Witten 的 Hamilton 化、Axelrod–Singer（及特殊情形 Kontzevich）的 $1/k\to\infty$ 扰动级数；Reshetikhin–Turaev 的严格定义；Lickorish–Zieschang–Novikov 的 Reeb 纤维化与「管化」；Dehn 与 Alexander 的归功；Kirby 第一运算（加不打结分支、以「墙」$\R^2\subset\R^3$ 隔开、框的环绕系数 $\pm1$）——一致。
- **p.293**（`p300.png`）：第二 Kirby 运算（$L_i,L_j$、平行移位 $L_i^1$、Jordan 弧、带框连通和 $\bar L_j$、换成 $L_i^1,\bar L_j$）；图 A.13（$2\pi$-twist）；「3 维流形学家偏爱两运算的某种组合」段（带框不打结圆周围圆盘、横截分支、移去该分支后作 $2\pi$ 扭转）；框、标准法标架 $\{S^1,S_1^1\}=0$、沿闭 Jordan 曲线的手术由框的环绕系数完全决定；带框链环的环绕矩阵与指标 $i(L)$（对角化后严格负元素个数）；黑板框与平行链环——一致。
- **p.294**（`p301.png`）：带整数标号的图（第 $q$ 个分支取 $i_q$ 个平行拷贝，共 $i_1+\cdots+i_n$ 分支）；$I_r=\{0,1,\dots,r-2\}$、$\langle\langle L\rangle\rangle=\sum_c\lambda_{c(1)}\cdots\lambda_{c(n)}S_{D_L}(A,A^{-1};\delta)$、$\delta=-A^2-A^{-2}$；$TR(M_L^3)=\delta^{-i(L)}\langle\langle L\rangle\rangle$ 为拓扑不变量（条件 $r\ge3$、$A=\exp\{i\pi/2r\}$、$\lambda_q$ 满足超定线性组 $\delta^j=\sum_{i=0}^{i=r-2}\lambda_iT_{i+j}$）；$T_j$ 与图 $D_j$（图 A.14）；「尚未用于解决任何拓扑问题」的评论；TQFT 引入（Segal–Atiyah 公理，与 Eilenberg–Steenrod 同调公理类比）——一致。
- **p.295**（`p302.png`）：$n$ 维 TQFT 公理：$(n-1)$ 维闭流形 $V\mapsto$ Hilbert 空间 $H_V$、配边 $W$（$\partial W=V_1\cup V_2$）$\mapsto$ 线性映射 $f_W:H_{V_1}\to H_{\bar V_2}$、$f_W\in H_{V_1\cup V_2}=H_{V_1}\otimes H_{\bar V_2}^*$、公理 $H_V=H_{\bar V}^*$；柱体给恒等映射；$V=\partial W_1=\partial W_2$ 时数 $\langle f_{W_1},f_{W_2}\rangle$ 是 $W_1\cup W_2$ 的不变量；古典拓扑中仅有的两个例子（偶维流形的 Euler 示性数、$4k$ 维带边流形的符号差，1960 年代中期 Rohlin 与作者的「可加性引理」）；$n=2$ 的「裤形」曲面与 $C_{jk}^i$、Frobenius 代数定义——一致。
- **p.296**（`p303.png`）：$\eta_{ij}=(\ ,\ )$、$\langle fg,h\rangle=\langle f,gh\rangle$；关联函数 (a)–(d) 与 $H^k=\eta^{ij}e_ie_j$；参数族与公理化（Witten、Dijgraaf、Verlinde 兄弟；Dijgraaf 为原书拼写，已照原加注）；Frobenius 几何、算子 $\partial_i-zC_{ik}^j$ 与零曲率、$F(t)$ 作为「自由能」；$h_{j,m}$ 与 (4.1)；Remark（$H_V$ 为 Calaby–Yau 流形上同调环的偶部、量子形变、Yau–Kontzevich–Manin–Tian–Ruan–Piunikhin–Givental–Salamon–MacDuff；$V=S_1$ 下标笔误 Note 正确）；Dijgraaf–Witten 方案与 $h_j$、$h_{j,0}=t^i\eta_{ij}$、$H_{j,m}=\int h_{j,m}(t(X))dX$——一致（建议改 1）。
- **p.297**（`p304.png`）：$\eta$ 常数、$C(t)$ 由含时 Frobenius 代数族的结构常数构成；(4.2) $\eta_{ij}=\partial_1\partial_i\partial_jF(t)$ 与「第一个基向量对应单位元」；结合性方程 (4.1)(4.2)（(4.1) 最难研究）；Dubrovin 的 Frobenius 几何描述（$\eta_{is}C_{jk}^s$ 对称、联络 $\partial_i-zC_{ik}^j$ 曲率零）；Dijgraaf–Witten (1991) 的平坦坐标与「无色散族」；$H_{j,m}$ 作为对易 Hamilton 量（流体力学型）、时间 $T^{j,m}$、$X=T^{1,0}$、$t^j=T^{j,0}$；Dubrovin–Novikov 意义下的 Hamilton 形式与《现代几何学》第二卷；$\bar F(X,T)$、初条件 $\bar F(X,T)=F(t)$ 与「无色散弦」条件 $\partial_X\bar F=\sum T^{j,m}\partial_{T^{j,m-1}}\bar F+\frac12\eta_{ij}T^{i,0}t^{j,0}$——一致。
- **p.298**（`p305.png`）：0-圈关系 $\partial^3_{(i,m),(j,n),(k,p)}\bar F=(\partial^2_{(i,m-1),(l,0)}\bar F)\eta^{ls}(\partial^3_{(s,0),(j,n),(k,p)}\bar F)$；$k$ 维圈引力延拓猜想、$n=1$ 的 KdV 族与 Schrödinger 势 $u(X)=(\partial_X)^2F=X$；Schrödinger 势作为整系数形式幂级数与代数曲线模空间上的 Chern 数（Kontzevich 1992，并证明 Witten 猜想）；Dubrovin 讲义（SISSA 1994）；$n=2$、$\eta_{11}=0,\eta_{12}=1,\eta_{22}=0$ 时 $F(t)=\frac12t_1^2t_2+f(t_2)$；结语（本领域尚欠严格证明、无好综述）与致谢段（Kauffman《Knots and Physics》、Bar–Natan 讲义、Dubrovin 讲义、私人交谈）——一致。

## 体例抽查
- 页标记：`% [原文 p.292]`…`% [原文 p.298]` 共 7 个，递增、无重复 ✓；p.294 处跨页句已合并、标记移到段末，复查合规 ✓。
- 公式：原书本节仅 (4.1)(4.2) 两个编号公式，`tag 2` 与之一致 ✓；其余 display 均无编号 ✓。
- 图：A.13、A.14 两张裁图齐全（`src\figures\figA13.png`、`figA14.png`），裁图不含原书图题，`\figtitle` 中文另写 ✓。
- 陈述：Remark 用 `remark{}`（空参数）承载，原书确为无编号 "Remark."，符合体例；check_chunk 对空编号给出 WARN，属已知允许项 ✓。
- Tutor Note：5 条（要求 ≥ 7/3 ≈ 2.3，即 ≥ 3）✓，单行、无 `%` 字符 ✓。
- `% CHUNK appc DONE` 在末行 ✓。
- check_chunk 复跑：页 292..298、tag 2、陈述 1、Note 5、OK（0 error，1 条空编号 WARN）。

## 修正记录
- 2026-11-10：原书 p.296、p.297 三处把 Dijkgraaf 拼作 **Dijgraaf**（已放大原书核对，`work\crops\p303_dij1.png`）。按「笔误照原排＋注」原则，正文三处改为 Dijgraaf，并在原 p.296 段后新增 Tutor Note 说明「读者按 Dijkgraaf 理解即可」。由核验人直接改（lead 授权）。
- 2026-11-10：p.294 页标记原插在句中（「……若 $D$ 是链环的任一图，我们将把」与「同一个图 $D$……」之间），已由作者 tr-xin 合并句段、标记移到段末，复查合规。
