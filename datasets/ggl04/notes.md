# 04 Gukov–Witten《Branes and Quantization》读记

底本：arXiv:0809.0305v2，72 页。**PDF 页 = 印刷页 + 1**（p001 为标题页，p002 页脚 1，p003 页脚 2）；本包所有页码一律用 PDF 页序。

## 1. 骨架

一条链：辛流形 $(M,\omega)$ → 复化 $(Y,\Omega=\omega_J+i\omega_K)$ → 以 $\omega_Y=\omega_K$ 取 A-模型 → 空间填充的秩 1 余各向同性膜 $B_{cc}$（曲率 $\omega_J$）→ 支撑在 $M$ 上的 Lagrange 膜 $B'$ → 弦空间 $H=\{(B_{cc},B')\text{ strings}\}$ 即量子化；$(B_{cc},B_{cc})$ 弦给非交换代数 $A$，它作用在 $H$ 上；反全纯对合 $\tau$ 给 hermitian 内积。§3 用 $SU(2)$、$SL(2,\mathbb R)$ 的表示论逐例验证，§4 把它用到 Chern–Simons。

关键点在于**分工**：$\omega$ 只出现在 $B_{cc}$ 的曲率里，$B'$ 只负责支撑与平坦线丛。因此同一个 $A$ 能作用在所有 $(B_{cc},B)$ 上，这正是本文与几何量子化最不同之处。

## 2. 主定理清单（含我是否核过）

| 位置 | 内容 | 核对情况 |
| --- | --- | --- |
| p14 (2.1)(2.2) | $\Omega=\omega_J+i\omega_K$，$I^t\omega_J=-\omega_K$，$I^t\omega_K=\omega_J$ | 与 $I^2=-1$ 相容，已验 |
| p16–17 (2.3)–(2.7) | $(B_{cc},B_{cc})$ 边界条件，$f$ 全纯 $\Leftrightarrow$ 保超对称 | 与 (2.4) 在 $F=\omega_J$ 时 $(g-F)^{-1}(g+F)=J$ 一致 |
| p22 (2.14)(2.15) | $H=\oplus_i H^i(M,K^{1/2}\otimes N)$ | 与 p35 的维数 $n$ 相容（$K^{1/2}=\mathcal O(-1)$） |
| p26–27 (2.17)–(2.21) | $\tau$ 的三条条件与内积 $\langle\psi,\psi'\rangle=(\Theta\tau\psi,\psi')$ | 与 p28 的经典极限 $\int_M\psi(\tau x)\psi(x)$ 一致 |
| p29–30 (3.2)(3.7) | $\int_S\Omega/2\pi=h^{-1}\mu$；$J^2=(\mu^2-1)/4$ | 直接算过 $\int_S dy\wedge dz/x=2\pi\mu$，符号对 |
| p34–35 (3.19)–(3.21) | $\mu=n$，$\dim H=n$，$J_z$ 谱 $-(n-1)/2,\dots,(n-1)/2$ | 与 $j=(n-1)/2$、$J^2=(n^2-1)/4$ 自洽 |
| p37 (3.28) | 主系列 $J^2=-(\gamma^2+1)/4$ | 抽文丢括号，已用 PDF 渲染核对 |
| p42–44 (3.38)(3.42)(3.44) | $a_nb_n=J^2-(s+n)(s+n+1)$；范数关系 | 与 (3.44) 有乘/除冲突，见 errata E2 |
| p45 (3.45) | 万有覆盖离散系列 $s_-=(\beta+1)/2$ | 与 (3.36) $J^2=s_-(s_--1)$ 联立得 $(\beta^2-1)/4$，验过 |
| p51 (3.54)–(3.57) | $s=\delta+ib+\mathrm{const}$，$b=\gamma/2$，$\mu/2=s+n+1/2$，$J^2=(s+n)(s+n+1)$ | 四式连锁，已逐步验 |
| p55 (3.62)–(3.64) | $h(J_x,J_y,J_z)h^{-1}=(-J_x,-J_y,J_z)$；$h\psi_s=c(-1)^s\psi_s$ | 与 $SU(2)/SL(2,\mathbb R)$ 为 inner real forms 一致 |
| p60–62 (3.66)–(3.74) | $D$-模、$\mathbb{CP}^1\setminus\{0,\infty\}$、$\epsilon\to0$ 分裂 | 只作定性核对 |
| p64–69 (4.1)–(4.8) | $\omega^*$、$H=H^0(M,L_*^{bk}\otimes K^{1/2})$、$bk=k+h$、$k+h=k_\varphi+h_\varphi$ | 与 csw 旧卡的 $k+h^\vee$ 一致 |

## 3. 与已译篇/旧卡的接口

| 接口对象 | 关系 | 差异 |
| --- | --- | --- |
| 库内 `kw/concept/canonical-coisotropic-brane`（Kapustin–Witten 2006） | 同一个 $B_{cc}$：条件 $(\omega^{-1}F)^2=-1$、$F=\mathrm{Im}\,\tau\,\omega_J$ | 该文用 $\tau$ 的虚部写曲率，本篇用超 Kähler 的 $\omega_J$；译名沿用「典范余各向同性膜」 |
| 库内 `ggl19/concept/distinguished-coisotropic-brane` | 同构造的另一种命名（distinguished c.c. brane），边界代数即全纯函数代数量子化 | 该文取 $F=\mathrm{Im}\,\tau\,\omega_K$，本篇取 $F=\omega_J$，只差复结构约定 |
| 库内 `csw/concept/half-form-correction` | 半形式移位 $K^{1/2}=L^{-h^\vee}$、$k_{\rm eff}=k+h^\vee$ | 与本篇 (4.4)(4.5) 的 $bk=k+h$ 是同一事实，符号/归一不同 |
| 库内 `mloc/concept/harish-chandra-module` | $(g,K)$-模的代数定义 | 本篇给几何实现（曲线膜的 $J_z$ 谱 $s+n$），不重复定义 |
| 库内 `sy38/deriv/gl2-triple-and-casimir` | 最低权 Casimir $s(s-1)$ 型 | 与本篇 (3.36) 同构，可用于校 (3.45) |
| 库内 `geoq/concept/overview-geometric-quantization` | 几何量子化 $H_P=\Gamma_P(L\otimes\sqrt K_M)$ | 本篇 §2.3 明确说两者只在超 Kähler 极化下一致 |

没有逐篇打开 02/06/11/16/23/28/36 等 SY* 篇目，只在需要外部核对时用了上表中的旧卡；这一点在 workflow 里也记了。

## 4. 版本差异（v1 → v2）

v1 71 页、v2 72 页。逐词 difflib 得 74 个差异块，实质只有 5 处：

1. **§1.5 末新增一段**（约 488 字符）：$Y$ 的 A-模型自同构中保持 $B_{cc}$ 的那些会作用在 $A$ 上作为自同构；本文的看法里它们正是 $(\Omega)$ 的辛同构。这是唯一新增的实质论述。
2. 新增一句指向 [25]（Chervov–Rybnikov）的替代算法提示。
3. 脚注 3 位置移动（文字未变）。
4. 参考文献插入 [23] Belov-Kanel–Kontsevich，旧 [23]→[24]（Freed–Witten）、旧 [24]→[25] 顺延。
5. 其余全是页脚数字位移。

**正文公式与式号无改动**，所以本包式号可直接对照 v2 抽文；v1 的抽文与 diff 记录放在 `external/`。

## 5. 核对与勘误

### 外部来源

| 外部来源 | 位置 | 它说什么 | 与本篇对照 | 结论 |
| --- | --- | --- | --- | --- |
| 库内卡 `kw/concept/canonical-coisotropic-brane`（Kapustin–Witten, hep-th/0604151） | 该卡 sources B p.185 eq (11.1)、p.191–195 | 典范余各向同性膜满足 $(\omega^{-1}F)^2=-1$，$F=\mathrm{Im}\,\tau\,\omega_J$，配 $(A,B,A)$ 膜 | 本篇 §2.1 的同一条件，$F=\omega_J$ | 一致；用于 E1 的依据1 |
| 库内卡 `ggl19/concept/distinguished-coisotropic-brane` | 该卡 §4 | 取 $F=\mathrm{Im}\,\tau\,\omega_K$ 的余各向同性膜，边界代数 $[f,g]=-i(\mathrm{Im}\tau)^{-1}\Omega_J^{-1}(df,dg)+\cdots$ | 本篇 (2.1)–(2.2)、§2.2 的 $A$ | 一致；用于 E1 的依据2 |
| 库内卡 `csw/concept/half-form-correction` | 该卡（源 witten1989 §2） | $H=\Gamma_P(M,L^{\otimes k}\otimes K^{1/2})$，$K^{1/2}=L^{-h^\vee}$，$k_{\rm eff}=k+h^\vee$ | 本篇 (4.4)(4.5)：$H^0(M,L_*^{bk}\otimes K^{1/2})$，$bk=k+h$ | 同为半形式移位，一致 |
| 库内卡 `mloc/concept/harish-chandra-module` | 该卡定义节 | $(g,K)$-模：有限生成、$Z(g)$ 局部有限、$K$-代数作用 | 本篇 §3.7 只给几何实现与 $J_z$ 谱 $s+n$ | 术语一致，定义不重复 |
| 库内卡 `sy38/deriv/gl2-triple-and-casimir` | 该卡 steps | 最低权 Casimir 取 $s(s-1)$ 型（$(k^2-2k)/4$） | 本篇 (3.36) $J^2=s_-(s_--1)$ | 结构一致，用于校 (3.45) |
| nLab `geometric+quantization`（2026-11-27 抓取，HTTP 200） | 词条正文 | 预量子化线丛曲率 $-(i/\hbar)\omega$，极化空间 $\Gamma_P(L\otimes\sqrt{K_M})$ | 本篇 §2.3 与几何量子化的对比 | 一致；仅作背景核对 |

另：nLab 的 `coisotropic+brane` 页不存在（404），未作为依据；arXiv 的 v1 PDF 已取回放在 `external/` 供复核。

### 五项动作回填（XREF §4）

1. **主定理陈述与符号**：主定理是「$H=\{(B_{cc},B')\text{ strings}\}$ 是 $(M,\omega_J)$ 的量子化，$A$ 作用其上」；符号 $\Omega,\omega_J,\omega_K,I,J,K$ 在 §2.1 一次给定，§3 未改。未见陈述级错误。
2. **关键公式的系数/符号**：(3.7) 的 $(\mu^2-1)/4$ 与 §3.2 的 $\mu=n$、$j=(n-1)/2$ 自洽，并由此定出 (3.5) 的 $c=-1/4$；$\int_S\Omega/2\pi=h^{-1}\mu$ 我按 $\Omega=h^{-1}dy\wedge dz/x$ 直接积分复核，符号与 $2\pi$ 因子都对。只有 (3.44) 的乘/除与 (3.28) 的括号需要处理（见「### 勘误」）。
3. **命题编号与交叉引用**：p.51 的 (3.56) 自称由 (3.11) 推出，实际要 (3.16)/(3.17)（E3）。其余交叉引用抽查 (3.38)→(3.42)→(3.44)、(4.4)→(4.5)→(4.8) 均对得上。
4. **数值/维数一致性**：$S^2$ 上 $\dim H=n$、$j=(n-1)/2$；主系列 $J^2=-(\gamma^2+1)/4\le-1/4$；互补系列 $-1/4<J^2<0$；CS 的 $bk=k+h$（$SU(2)$ 时 $h=2$）。均自洽。
5. **记号前后一致**：$J$ 在 §2 是使 $\omega_J$ 为 $(1,1)$ 型的复结构，§4 脚注 6 自认与 [39] 的 $I$ 撞名；$\tau$ 与 $\tilde\tau=h\tau$ 两个对合易混；$\delta$ 既是单值又是主系列标签。三处都已在卡片里显式区分。

### 勘误

- **E1（high，fixed）** p.65 把 $B_{cc}$ 写成 "the canonical isotropic brane"。按其自身 §2.1 的定义 $I=\omega_Y^{-1}F$、$I^2=-1$，$F=\omega_J$ 给的是**余各向同性**膜；库内 kw06 与 ggl19 两张独立旧卡都称 coisotropic。卡片 `ggl04/concept/cs-quantization` 按订正写并记 corrections。
- **E2（medium，fixed）** p.44 式 (3.44) 印成乘积 $(n(n+1)-J^2)|(\psi_{n+1},J_+\psi_n)|^2$；由本篇自己的 (3.38) 与 (3.42) 联立应为**除以** $((s+n)(s+n+1)-J^2)$（$s=0$ 时分母 $n(n+1)-J^2$）。用 $S^1$ 显式模型（$\nu_n\equiv1$、$a_n=c-n$、$c=-1/2+i\nu$）检验：除法给 1，乘积给 $((n+1/2)^2+\nu^2)^2\ne1$。两种写法对「相邻范数反号」的结论都成立，故是无害笔误；卡片 `ggl04/concept/unitarity-by-tau` 按除法写。
- **E3（low，open）** p.51 (3.56) 引 (3.11)，实际用到 (3.16)/(3.17)。这是交叉引用不足而非数学错误，卡片 `ggl04/concept/harish-chandra-curve` 保留原文写法，provenance 标「存疑」。
- **已排除的疑点**：(3.28) 在抽文里作 "−γ2 + 1 / 4"，一度像是 $(1-\gamma^2)/4$；PDF p37 渲染实印 $J^2=-(\gamma^2+1)/4$，是分数线丢括号，**不入 errata**。同理 (3.42) 抽文看起来像乘法，渲染 p43 确认是除法，原文无误。

## 6. 不懂

1. 「只渐近 $SL(2,\mathbb R)$ 不变」的精确判据。原文自认不知道 “sufficiently close” 的正确条件（p.50），我也没有独立判据，只能按「$\ell$ 在无穷远趋于 $w_2$ 轴」操作。
2. (3.64) 中 $c$ 的选取：奇维 $c$ 实、偶维 $c$ 须纯虚，原文说依赖固定点的选择，$c=\pm i$ 之间没有自然选择。我没弄懂这个二义性在物理上对应什么。
3. $K^{1/2}$ 与平坦 $\mathrm{Spin}^c$ 结构在 K-理论意义下的精确等价。原文（p.23–24）只用它论证「没有平坦 $\mathrm{Spin}^c$ 结构就不能这样量子化」，我给不出证明。
4. §4 里映射类群的中心扩张「未算出」（p.66），以及 (4.8) 与 [40] 一圈修正的具体对应，我只照抄结论，没有验算。
5. §3.8 可约膜的形变参数 $\epsilon\sim ab$ 与「三个实参数 $\delta,\mathrm{Re}\,\epsilon,\mathrm{Im}\,\epsilon$」的模空间维数，我没有独立数过。
6. §2.3 关于「无平坦 $\mathrm{Spin}^c$ 结构的辛流形」（$SO(p,q)$、$p+q$ 奇、$p,q\ge4$ 的最小轨道）为何是最小反例，没有核。
