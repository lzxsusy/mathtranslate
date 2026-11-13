# tr-04 块交叉校对报告（原文 pp.51–63）

- **校对者**：tr-07（Lead 指派交叉校对，只出报告、不改被校对文件）
- **日期**：2026-11-03
- **被校对文件**：`work/src/chunks/tr04a.tex`（pp.51–54）、`tr04b.tex`（pp.55–58）、`tr04c.tex`（pp.59–63）
- **负责 tag 区间**：5.24–5.47、6.1–6.5
- **校对素材**：`work/pages/p051.png … p063.png`（200 dpi）+ 裁剪放大图（`work/tmp/tr04_*.png`）+ `work/split/p051.txt … p063.txt` + `work/figures/{fig3,eq537,eq539}.png`

## 0. 结论摘要

**总体质量高。** 29 条编号公式全部齐全、无重复、无跳号、无自造；我把 29 条全部对着页面图像逐符号过了一遍（Lead 指定的必查项 (5.33)、(5.31)(5.32)、(5.44)–(5.47)、(6.1)–(6.5) 全在其中），**只发现 1 处必须改的数学符号错误**（p.61 的 $\overline{\mathbb{C}}$ 漏了上横线）。正文无整段漏译，8 条脚注齐全，Figure 3 与 Table 3 处理正确；后者是原书真实存在的表（p.61），因此 **STYLE_GUIDE §7 的表格清单需要 Lead 更新**。另有若干可选改：$q$ 脚标的花体/正体、术语统一、图宽、2 处批注勘误、2 处页界注释位置、1 处措辞。

| 类别 | 数量 |
|---|---|
| 编号公式（应/实） | 29 / 29 |
| 逐符号抽查 | 29 条（全部） |
| 必须改 | **1** |
| 可选改 | 8 |

---

## 1. 编号公式完整性（lead 任务 1）

`tags_bypage.txt` 在 p.51–63 的清单与 tr04 实际 `\tag{}` 逐页对照：

| 页 | tags_bypage | tr04 实际 | 结论 |
|---|---|---|---|
| p51 | 5.24, 5.25, 5.26, 5.27, 5.28 | 同 | ✅ |
| p52 | 5.29, 5.30（5.28 为行文引用） | 5.29, 5.30 | ✅ |
| p54 | 5.31, 5.32 | 同 | ✅ |
| p55 | 5.33, 5.34 | 同 | ✅ |
| p56 | 5.35, 5.36 | 同 | ✅ |
| p57 | 5.37, 5.38, 5.39 | 同 | ✅ |
| p58 | 5.40, 5.41 | 同 | ✅ |
| p59 | 5.42, 5.43 | 同 | ✅ |
| p60 | 5.44, 5.45, 5.46, 5.47 | 同 | ✅ |
| p62 | 6.1, 6.2 | 同 | ✅ |
| p63 | 6.3, 6.1（引用）, 6.4, 6.5 | 6.3, 6.4, 6.5 | ✅ |

- 合计唯一编号 **29 条**，脚本 `work/tmp/tagcheck_tr04.py` 检查：`missing=[]`、`extra=[]`、`duplicates=[]`。
- 页界注释齐全：tr04a 覆盖 p51–54，tr04b 覆盖 p55–58，tr04c 覆盖 p59–63，**13 页一个不缺**。
- 与上游（tr-03 止于 5.23）、下游（tr-05 起于 6.6）无重叠。

---

## 2. 公式逐符号抽查（lead 任务 2；打了 ★ 的是 Lead 指定必查项）

方法：用 200 dpi 页图 + 需要处 700–1600 dpi 裁剪放大，逐符号比对上下标归属、指标 $i/j/I/J$、$\epsilon_1$ vs $\epsilon_2$、分子/分母归属、求和/求积范围、\bar/\overline、花体 vs 正体。

| 页 | 式 | 核对内容（要点） | 结论 |
|---|---|---|---|
| 51 | (5.24) | $\prod_{\alpha\in\Delta}\Upsilon_b(\langle\alpha,ra\rangle)$；脚注 42 的 Vandermonde $\prod_{\alpha\in\Delta}(\langle\alpha,ra\rangle)$ | ✅ |
| 51 | (5.25) | $\prod_{w\in R}$、分母 $\Upsilon_b(\frac{b+1/b}{2}+\langle w,ra\rangle)$、指标 $R$ | ✅ |
| 51 | (5.26) | $\Upsilon_b(\cdots)\to\Upsilon_b(\cdots+rm)$，$+rm$ 位置正确 | ✅ |
| 51 | (5.27) | 左右两端参数 $(a,k,\xi,\bar k,\bar\xi)$、三个因子顺序 | ✅ |
| 51 | (5.28) | $\int\dd a\,Z_{cl}(a,q\bar q)Z_{one-loop}Z_{inst}(a,q)Z_{inst}(a,\bar q)$；$\vert q\vert^{r^2\vert a\vert^2}$ | ✅ |
| 52 | (5.29) | $\sum_{\text{all }k_I\ge0}$、$\prod_I q_I^{k_I}$、$\int_{\prod_I\mathcal M_{G_I,k_I}}$、$\dd\xi$ | ✅ |
| 52 | (5.30) | $F_{pert}+\lim_{\epsilon_1,\epsilon_2\to0}(\epsilon_1\epsilon_2\log Z_{inst})$ | ✅ |
| 54 | ★(5.31) | 箭图：$M_i$ 方框在 $\mathrm{SU}(N_i)$ 椭圆节点**上方**、竖线相连；节点间水平连线、$\cdots$ 位于 $\mathrm{SU}(N_2)$ 与 $\mathrm{SU}(N_p)$ 之间（原图 p.54 同构） | ✅ |
| 54 | ★(5.32) | $Z_{inst}[\prod U(N_i)]=\sum_{k_1\ge0,\dots,k_p\ge0}z_1^{k_1}\cdots z_p^{k_p}Z^{(k)}_{inst}$ | ✅ |
| 55 | ★(5.33) | **分子**：$\prod_{i,F,I}(m^i_F-\phi^i_I)\prod_{i=1}^{p-1}[\prod_{I,J}S(\phi^{i+1}_J-\phi^i_I)\prod_{A,J}(\phi^{i+1}_J-a^i_A+\epsilon_1+\epsilon_2)\prod_{I,B}(a^{i+1}_B-\phi^i_I)]$；**分母**：$\prod_i[(\frac{\epsilon_1\epsilon_2}{\epsilon_1+\epsilon_2})^{k_i}\prod_{I\ne J}S(\phi^i_I-\phi^i_J)\prod_{A,I}(\phi^i_I-a^i_A+\epsilon_1+\epsilon_2)(a^i_A-\phi^i_I)]$。两处关注点（$\prod_{I\ne J}S(\phi^i_I-\phi^i_J)$ 与 $\prod_{I,B}(a^{i+1}_B-\phi^i_I)$）**均正确**；$S(\phi)=-(\phi+\epsilon_1)(\phi+\epsilon_2)/[\phi(-\phi-\epsilon_1-\epsilon_2)]$ 亦正确 | ✅ |
| 55 | (5.34) | $\{\phi^i_I\}=\{a^i_A+(r-1)\epsilon_1+(s-1)\epsilon_2\}$，$r,s$ 的 $-1$、$\lambda^i_A$ 位置 | ✅ |
| 56 | (5.35) | $Z_{inst}[\prod\mathrm{SU}(N_i)]=Z_{inst}[\prod\mathrm{U}(N_i)]/(\mathrm{U}(1)\ \text{factor})$ | ✅ |
| 56 | (5.36) | $(\mathrm{U}(1)\ \text{factor})\simeq\prod_{1\le i\le j\le p}(1-z_i\cdots z_j)^{c_{ij}}$ | ✅ |
| 57 | (5.37) | 裁图 `eq537.png` 与 p.57 原图逐节点一致（Spin(4)—USp(2)—Spin(4) = 两列 SU(2) 方框 + 中央 SU(2) 椭圆，X 交叉连线），无原编号 | ✅ |
| 57 | (5.38) | $\tilde\tau=\tau+\sum_{n\ge0}c_n e^{2\pi i n\tau}$ | ✅ |
| 57 | (5.39) | 裁图 `eq539.png` 与 p.57 原图一致：$\mathrm{T}[\mathfrak{so}(4),\text{带分支切割的圆柱}]=\mathrm{T}[\mathfrak{su}(2),\text{四点球面}]$（花体 $\mathfrak{so}/\mathfrak{su}$ 与原图一致） | ✅ |
| 58 | (5.40) | 两行：$q_{\mathrm{so}(4)}=\sqrt{16\lambda(2\tau_{IR})}=16e^{\pi i\tau_{IR}}+O(e^{3\pi i\tau_{IR}})$；$q_{\mathrm{su}(2)}=\lambda(\tau_{IR})=q_{\mathrm{so}(4)}(1+\frac{q_{\mathrm{so}(4)}}{4})^{-2}=16e^{\pi i\tau_{IR}}-128e^{2\pi i\tau_{IR}}+O(e^{3\pi i\tau_{IR}})$；系数 $-128$ 正确。**唯脚标花体/正体不符**（见 §6，可选改） | ✅（符号全对） |
| 58 | (5.41) | $Z_{T,gauged}=\int[\mathrm{D}A\,\mathrm{D}\lambda\,\mathrm{D}\phi]e^{-S_{SYM}[A,\lambda,\phi]}Z_T[A,\lambda,\phi]$ | ✅ |
| 59 | (5.42) | 两行：$\lim_{t\to+\infty}\int[\mathrm{D}A\mathrm{D}\lambda\mathrm{D}\phi]e^{-S_{SYM}-tQV_{vector}}Z_T$；$\int_{QV_{vector}=0}[\mathrm{D}A\mathrm{D}\phi]e^{-S_{SYM}}Z^{vector}_{one-loop}Z_T$ | ✅ |
| 59 | (5.43) | $\prod_I[\sum_{k_I,\bar k_I\ge0}\int_{\mathfrak h_I\times\mathcal M_{G_I,k_I}\times\mathcal M_{G_I,\bar k_I}}\dd a_I\dd\xi_I\dd\bar\xi_I]\{\prod_I[|q_I|^{r^2|a_I|^2}q_I^{k_I}\bar q_I^{\bar k_I}Z^{vector}_{one-loop}]\prod_L Z_{T_L}\}$ | ✅ |
| 60 | ★(5.44) | $\int[\mathrm{D}\Phi_{3d}]e^{-S_{3d}[\Phi_{3d}]}Z_{North}[\Phi_{3d},q,\bar q]Z_{South}[\Phi_{3d},q,\bar q]$（**两半球都带 $(q,\bar q)$**，与原图一致） | ✅ |
| 60 | ★(5.45) | $\int\dd a\,Z_{cl,3d}[a]Z_{one-loop,3d}[a]Z_{North}[a,q]Z_{South}[a,\bar q]$（此处才拆成 $q$ / $\bar q$） | ✅ |
| 60 | ★(5.46) | $\sum_{\vert\Phi\rangle\in\mathcal H[S^3_b]}\langle HS^4_b\,North\vert\Phi\rangle\langle\Phi\vert HS^4_b\,South\rangle$ | ✅ |
| 60 | ★(5.47) | $\sum_{\vert a\rangle\in\mathcal H[S^3_b],\,Q\vert a\rangle=0}\cdots$（限定 $Q$-不变态） | ✅ |
| 62 | ★(6.1) | $[L_m,L_n]=(m-n)L_{m+n}+\frac{1}{12}\delta_{m+n=0}(m^3-m)C$ | ✅ |
| 62 | ★(6.2) | $[L_0,\mathcal O]=h_{\mathcal O}\mathcal O,\ [\bar L_0,\mathcal O]=\bar h_{\mathcal O}\mathcal O$ | ✅ |
| 63 | ★(6.3) | $L_n\vert V\rangle=\bar L_n\vert V\rangle=0,\ n\ge1$ | ✅ |
| 63 | ★(6.4) | $\mathbb L_{-Y}\bar{\mathbb L}_{-\bar Y}\vert V\rangle:=L_{-m_1}\cdots L_{-m_k}\bar L_{-n_1}\cdots\bar L_{-n_l}\vert V\rangle$（黑体 L 与 L 上的 bar 归属正确） | ✅ |
| 63 | ★(6.5) | 两点：$g_{12}\delta_{h_1=h_2}\delta_{\bar h_1=\bar h_2}z_{12}^{-2h_1}\bar z_{12}^{-2\bar h_1}$；三点：$C_{123}z_{23}^{h_1-h_2-h_3}z_{31}^{h_2-h_3-h_1}z_{12}^{h_3-h_1-h_2}\times\bar z_{23}^{\bar h_1-\bar h_2-\bar h_3}\bar z_{31}^{\bar h_2-\bar h_3-\bar h_1}\bar z_{12}^{\bar h_3-\bar h_1-\bar h_2}$，指数与 $z$ 的配对逐一核对 | ✅ |

> 说明：(5.33) 我独立复核了 Lead 特别关注的两处——分母 $\prod_{I\ne J}S(\phi^i_I-\phi^i_J)$ 与分子 $\prod_{I,B}(a^{i+1}_B-\phi^i_I)$——**tr04b 抄写完全正确**（$I\ne J$ 是不等号而非 $I\neq j$；$a^{i+1}_B$ 的上标是 $i+1$、下标 $B$，与图一致）。

---

## 3. 漏译检查（lead 任务 3）

1. **逐段对照**：把 `split/p051.txt … p063.txt` 全读一遍，与 tr04 三文件逐段对应。结论：**无整段缺失**。含：p.51 五个式子及两段说明、p.52 Omega 背景/预势两段与脚注 43、p.53 三个方法 bullet、p.54 递推关系 bullet + 三小段 + 显式公式段、p.55 (5.33)/(5.34)/Exercise 5.4/U(1) 因子段、p.56 Figure 3 图注 + (5.35)(5.36)、p.57 取向轨形段 + (5.37)–(5.39)、p.58 双覆盖段 + (5.40) + §5.4 两个小标题段、p.59 局域化 (5.42)(5.43) + 全纯因子化、p.60 三小段 + (5.44)–(5.47)、p.61 §6 引言 + Table 3、p.62 §6.1 + Virasoro 段 + Exercise 6.1 + 共形维数段、p.63 主算子段 + Exercise 6.2 + 两点/三点函数段。
2. **引文多重集比对**（代理指标）：把 tr04 三文件按 `% [原文 p.N]` 切页，与文字层逐页比对 `[n]` 引文集合：**合计 86 / 86 完全一致**；页级差异只有两处"跨页段归属"（见 §8），内容无缺。
3. **脚注**：原书 p.51–p.63 共 8 条脚注（42–49），tr04 三文件 `\footnote{}` 恰为 4+3+1=8，逐条内容核对一致（含 p.54 脚注 45 的"第 56 页"自我引用、p.61 脚注 49 的 Sicily/triskelion 说明）。
4. **习题**：Exercise 5.4、6.1、6.2 三条齐全，`\begin{exercise}{…}` 编号正确。

---

## 4. Figure 3（p.56）

| 检查项 | 结果 |
|---|---|
| 是否用 `fig3.png` | ✅ `\includegraphics[width=0.75\textwidth]{fig3.png}`（文件存在，1356×673） |
| 是否用 `\figtitle{3}{…}` | ✅ |
| 图注是否照译 | ✅ 逐句对照："$U(4)\times U(4)\times U(3)$ 规范理论的膜构造。最左侧的 U(4) 因子带两个基本超多重态（由横向 D6 膜插入，图中记作 $\otimes$），最右侧的 U(3) 因子带一个基本超多重态。在这个例子中，每个规范群都是渐近自由的。" 与原图注一致（含 $\otimes$ 说明） |
| 位置是否在第二次引用附近 | ✅ 原文两次引用：p.54 "as depicted in Figure 3"（tr04a 有"如图 3 所示"）、p.55 "depicted in Figure 3"（tr04b 有"图 3 所示"）。图声明在 tr04b 的 p.56 段首，正好紧接第二次引用、与原书"图 3 浮在 p.56 顶部"一致 |
| 可选 | 宽度 0.75\textwidth≈12 cm，原图约 9 cm（≈0.56–0.6\textwidth），略偏大，建议 0.6\textwidth（见可选改 4） |

---

## 5. Table 3（p.61）——原书确有第三个表，STYLE_GUIDE 需更新

**核实**：p.061.png 显示一个带深色标题条的表格，标题正是 *"**Table 3:** Basics of AGT. In Liouville CFT conventions, change $Q$ to $Q/2$."*，并含 10 行数据 + 两个旋转的分组标签（Parameters / Building blocks）。因此 **tr04c 收 Table 3 是对的**，而 `STYLE_GUIDE §7` 写的"原文只有 Table 1、Table 2、缩写表"不准确。

逐行核对 tr04c 的表（全部一致）：

| 原文 | tr04c |
|---|---|
| 表头 Gauge theory / Toda-Liouville CFT | 规范理论 / Toda–Liouville 共形场论 ✅ |
| Partition function on $S^4_b$ / Toda correlator on $C$ | $S^4_b$ 上的配分函数 / $\mathcal C$ 上的 Toda 关联函数 ✅ |
| Parameters：Squashing parameter $b=\sqrt{\epsilon_1/\epsilon_2}$ / Toda coupling constant $b$ | 压扁参数 / Toda 耦合常数 $b$ ✅ |
| Gauge couplings in 4d / Complex structure of $C$ | 4d 规范耦合 / $\mathcal C$ 的复结构 ✅ |
| Dual gauge theory descriptions / Pants decompositions of $C$ | 对偶规范理论描述 / $\mathcal C$ 的裤子分解 ✅ |
| Full tame puncture of mass $m$ / Vertex operator $\hat V_{Q+rm}$ | 质量为 $m$ 的满驯服穿刺 / 顶点算子 $\hat V_{Q+rm}$ ✅ |
| Building blocks：Coulomb branch parameter $a$ / Internal momentum $\alpha=Q+ra$ | Coulomb 分支参数 $a$ / 内部动量 $\alpha=Q+ra$ ✅ |
| Gauge one-loop determinant / Inverse two-point function | 规范单圈行列式 / 两点函数之逆 ✅ |
| Matter one-loop determinant / Three-point structure constant | 物质单圈行列式 / 三点结构常数 ✅ |
| Classical action contribution / Conformal block leading term | 经典作用量贡献 / 共形块领头项 ✅ |
| Instanton partition function / Conformal block power series | 瞬子配分函数 / 共形块幂级数 ✅ |

- 表题位置：tr04c 把 `\tabtitle{3}` 放在 `\end{tabular}` 之后（表下）。与 c01 的 Table 1、tr01a 的 Table 2 的工程约定一致，**不必改**（虽然原书标题条在表上）。
- **Lead 待办**：更新 `STYLE_GUIDE §7`（表格共 3 个 + 缩写表），并检查 `main.tex`/`c00.tex` 是否另有"表格清单"需要同步。tr04c 文件里已有注释提醒，但那是注释、不进排版。

---

## 6. 术语与物理表述（对照 glossary）

### 6.1 与 glossary 一致的（抽查）
Coulomb 分支、超多重态/半超多重态、双基本表示、三基本表示、瞬子配分函数、配分函数、单圈行列式、局域化、共形块、主算子、后代、中心荷、裤子分解、箭图/箭图尾巴、tinkertoy（保留）、贝塔函数、渐近自由、共形窗口（未用）、穿刺点、杨图、手征代数、Liouville 共形场论、Seiberg–Witten 曲线、预势、Killing 型 —— 均符合。

### 6.2 建议（可选）
1. **orientifold**：tr04b 用"取向轨形（orientifold）"。项目 glossary 未收此词，tr-07 的块用"定向折叠（orientifold）"（tr07c）。建议统一（推荐"定向折叠（orientifold）面"），并请 Lead 收入 glossary。
2. **twist defect**：tr04b 用"扭折缺陷（twist defect）"。文献常见"扭曲缺陷"。若项目无既定译法，建议统一为"扭曲缺陷（twist defect）"。
3. **"（伴随 $m\to-m$）"**（tr04a:20）：原文 "(with mass $m\to-m$)"。"伴随"在物理中文里默认指 adjoint（本段通篇在谈表示论），易误读为"伴随表示"。建议改为"（质量相应取 $m\to-m$）"。
4. **"位形参数 $q$"**（tr04b:66）：原文 "the position $q=e^{2\pi i\tau}$ arising in the class S construction"。译"位形参数"可通，若能改"位形（position）$q$"更贴。
5. **"只不过是把左端换成右端"**（tr04a:14，指 (5.26) 的替换）：意思可懂但不够清楚，建议"只是作如下替换：……"。

---

## 7. 批注（Tutor Note）勘误

### 7.1 必须改的批注错误
**p.58 (5.40) 批注的算术**（tr04b:92）：写的是
> $\sqrt{16\lambda(2\tau_{IR})}=16e^{\pi i\tau_{IR}}(1-4e^{2\pi i\tau_{IR}}+\cdots)^{1/2}=16e^{\pi i\tau_{IR}}-32e^{3\pi i\tau_{IR}}+\cdots$

正确推导：$\lambda(2\tau_{IR})=16q^2-128q^4+\cdots$（$q=e^{\pi i\tau_{IR}}$），故
$16\lambda=256q^2(1-8q^2+\cdots)$，开方得 $16q(1-8q^2)^{1/2}=16q-64q^3+\cdots$。
即根号内系数应是 **$-8$**（不是 $-4$），末项应是 **$-64e^{3\pi i\tau_{IR}}$**（不是 $-32$）。原文只写 $+O(e^{3\pi i\tau_{IR}})$，两种写法都"相容"，但批注作为"数值锚点"必须自身正确。
建议替换为：`$(1-8\ee^{2\pi\ii\tau_{\mathrm{IR}}}+\cdots)^{1/2}=16\ee^{\pi\ii\tau_{\mathrm{IR}}}-64\ee^{3\pi\ii\tau_{\mathrm{IR}}}+\cdots$`。

### 7.2 可选改的批注问题
**p.59 批注引错式号**（tr04c:48）：批注说"这正是 **(5.44)** 中 $Z_{North}$ 只含 $q$、$Z_{South}$ 只含 $\bar q$ 的原因"。但 (5.44) 两半球都带 $(q,\bar q)$，真正拆开是 (5.45)。建议把 `(5.44)` 改为 `(5.45)`。

### 7.3 已验证正确的批注（独立复算）
- p.51 (5.25)–(5.26)：$\Upsilon_b(b+1/b-x)=\Upsilon_b(x)$、$\Upsilon_b=\Upsilon_{1/b}$ 与 $b=1$ 数值锚点 $\Upsilon_1(1/2)=1/(\Gamma(1/2)\Gamma(3/2))=2/\pi$ ✅
- p.52 $\epsilon_1=b/r,\ \epsilon_2=1/(rb)$、$\epsilon_1\epsilon_2=1/r^2$、$|a|^2=-\operatorname{Tr}(a^2)$ 的量纲链 ✅
- p.55 (5.33) 因子核对、$S(\phi)$ 的归一化与 $\phi\to\infty$、$\phi\to0$ 行为 ✅
- p.56 (5.36) 与 Heisenberg 顶点关联函数指数为荷的双线性的自洽性 ✅
- p.62 Exercise 6.1：我独立重算 $\tilde C=kC,\ \tilde L_n=L_{kn}/k+\delta_{n=0}(k-1/k)C/24$ 的 Jacobi/对易子，$C$ 的系数确为 $\frac{1}{12}mk(m^2-1)=\frac{k}{12}(m^3-m)$，与批注一致 ✅
- p.63 (6.5) 指数恒等式 "$\sum_j$（每个 $i$ 的指数）$=-2h_i$" ✅
- p.61 Table 3 批注：$Q\to Q/2$ 后 $h=\alpha(Q-\alpha)=Q^2/4-r^2a^2$ ✅
- （trivial）tr04b:92 注释里的分隔线写成 `------`（六个连字符），建议改 `——`；不影响编译。

---

## 8. 页界注释位置（仅注释，不影响排版/阅读，可选改）

1. **p.52 / p.53**（tr04a:61–63）：`% [原文 p.53]` 标在 bullet 列表之前，但"…and the / moduli space for each gauge group factor has one connected component…There are several methods…[127].44"这段的字面后半在 p.53。建议把标记移到"而每个规范群因子的模空间…"之前（句中断页，与 tr-07 自己块的处理方式一致）。
2. **p.61 / p.62**（tr04c:100–104）：`\subsection{二维 CFT 与 Liouville 共形场论}` 及其引言段在 p.61 标记下，但原书 §6.1 标题与首段在 **p.62 顶部**。建议把 `% [原文 p.62]` 移到 `\subsection` 之前。

> 这两处只影响"页码对照注释"，不影响正文与编译；tr04 其他页界（p56、p57、p58、p59、p60、p61、p63）均已核对正确。

---

## 9. 结构与编译风险自检

- `\tag{}`：29 条，唯一、有序，与 tags_bypage 一致。
- 环境配对：`begin`/`end` 12/11/16 对 12/11/16；花括号 194/194、219/219、284/284 平衡；`$` 成对（逐行检查无疑似）。
- `\left`/`\right`：tr04b 5/5、tr04c 2/2；tr04a 的 1 个 `\left` 是注释里的 `\leftrightarrow`，无问题。
- UTF-8 无 BOM、LF；无 `\documentclass`/`\usepackage`/`\newcommand`/`**`。
- 图片：`fig3.png`、`eq537.png`、`eq539.png` 均在 `work/figures/`，按 STYLE_GUIDE §6bis 裁图（无原编号）✅。
- 表格：`booktabs` + `multirow` + `rotatebox`（graphicx）均为 preamble 已加载宏包 ✅。
- (5.31) 的 TikZ：节点/连线/标签与原图一致（`baseline={(0,0.05)}`）；因无法编译，建议 Lead 编译后目测一下 $M_i$ 方框与节点的间距。

---

## 10. 汇总

### 必须改（1 条）
| # | 位置 | 原文/原图 | 现状 | 改法（可直接替换） |
|---|---|---|---|---|
| 1 | tr04c.tex **第 69 行**（p.61） | 原图 p.61 第 3 行：$\mathcal{C}=\overline{\mathbb{C}}\setminus\{z_1,\ldots,z_n\}$（有**上横线**，即扩充复平面/黎曼球去掉穿刺点） | `在黎曼面 $\cC=\C\setminus\{z_1,\dots,z_n\}$ 上约化` —— 漏了上横线 | `在黎曼面 $\cC=\overline{\C}\setminus\{z_1,\dots,z_n\}$ 上约化` |

**依据**：① p.61 图像放大的字形明确显示 $\mathbb{C}$ 上有横线；② 物理上 class S 的 $C$ 是**紧**黎曼面去穿刺点（$\overline{\mathbb{C}}\setminus\{n\text{ 点}\}$），写成 $\mathbb{C}\setminus\{\cdot\}$ 是非紧的，与紧黎曼面/双覆盖论证不符；③ 同段下文谈"复结构/模参数"，只有紧化曲线才有模参数 $q$ 的标准定义。

### 可选改（8 条）
| # | 位置 | 现状 | 建议 |
|---|---|---|---|
| 2 | tr04a:20（p.51） | `表示 $R$ 与 $\bar R$ 中的超多重态是等价的（伴随 $m\to-m$）` | `表示 $R$ 与 $\bar R$ 中的超多重态是等价的（质量相应取 $m\to-m$）`（"伴随"易被读成 adjoint） |
| 3 | tr04b:84/86/87/90（p.58） | $q$ 的脚标用了花体：`q_{\fso(4)}`、`q_{\fsu(2)}` | 改为正体 `q_{\mathrm{so}(4)}`、`q_{\mathrm{su}(2)}`（原图 p.58 的 $q_{\mathrm{so}(4)}$ 是**正体**；正文"$\fso(4)$ 曲线"等处的**花体保留**，原图那里确是 $\mathfrak{so}(4)$） |
| 4 | tr04b:36（p.56） | `\includegraphics[width=0.75\textwidth]{fig3.png}` | `width=0.60\textwidth`（原图宽约 9 cm ≈ 0.56–0.6\textwidth） |
| 5 | tr04b:92（p.58 批注） | `(1-4\ee^{2\pi\ii\tau_{\mathrm{IR}}}+\cdots)^{1/2}=16\ee^{\pi\ii\tau_{\mathrm{IR}}}-32\ee^{3\pi\ii\tau_{\mathrm{IR}}}` | `(1-8\ee^{2\pi\ii\tau_{\mathrm{IR}}}+\cdots)^{1/2}=16\ee^{\pi\ii\tau_{\mathrm{IR}}}-64\ee^{3\pi\ii\tau_{\mathrm{IR}}}`（推导见 §7.1） |
| 6 | tr04c:48（p.59 批注） | `这正是 (5.44) 中 $Z_{North}$ 只含 $q$、$Z_{South}$ 只含 $\bar q$ 的原因` | `这正是 (5.45) 中 $Z_{North}$ 只含 $q$、$Z_{South}$ 只含 $\bar q$ 的原因` |
| 7 | tr04b:59（p.57） | `带有取向轨形（orientifold）面的膜构型` | `带有定向折叠（orientifold）面的膜构型`（与 tr-07 块统一；建议收入 glossary） |
| 8 | tr04b:66（p.57） | `扭折缺陷（twist defect）` | `扭曲缺陷（twist defect）`（若项目另有约定可忽略） |
| 9 | tr04a:14（p.51） | `因此…只不过是把左端换成右端：` | `因此…只是作如下替换：` |
| 10 | tr04a:63 / tr04c:104 | p.53、p.62 页界注释位置（见 §8） | 分别移到"而每个规范群因子的模空间…"之前、`\subsection` 之前 |

> 说明：第 10 条只是 `% [原文 p.N]` 注释的行位置，不影响编译与阅读，故列在可选。

### Lead 待办（非 tr04 文件改动）
- 更新 `STYLE_GUIDE §7`：原书表格共 **3 个**（Table 1 p.10、Table 2 p.13、**Table 3 p.61**）+ 缩写表（p.105）；并检查 `main.tex`/目录是否有表格清单需要同步。
- 建议把 `orientifold = 定向折叠（orientifold）` 收入 glossary。
