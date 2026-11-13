# 交叉校对报告：tr-05（pp.77–92，tags 4.79–4.184）

校对者：tr-04　　日期：2026-11-04　　校对对象文件：
`work/src/chunks/tr05a.tex`、`tr05b.tex`、`tr05c.tex`（**只读，未修改他人任何文件**）
比对依据：`work/tags_bypage.txt`、`work/pages/pNNN.png`（200 dpi 页面图 + 900–1200 dpi 裁图）、`work/split/pNNN.txt`、`work/figures/fig17–19.png`、`glossary.tsv`、`STYLE_GUIDE.md`、`BRIEF.md`、`TIMELINE.md`。

---

## 1. 结论摘要

| 项 | 结果 |
|---|---|
| 编号公式完整性 | **通过**：4.79–4.184 共 **106 条**，与 `tags_bypage.txt` pp.77–92 逐页完全一致（16/16 页计数与顺序全对，`PASS`） |
| 公式逐符号 | **17 条抽查，16 条一致，1 条错**：**(4.96) 第二个分子应为 $G/\mathcal{Z}$，tr05a 误作 $\mathcal{G}/\mathcal{Z}$**（数学上也不自洽，详见 M1） |
| 结构（标题/图/方框） | **通过**：4.2.3、4.2.4、4.3、4.3.1–4.3.4 标题齐全、页码与 TIMELINE 一致；图 17/18/19 齐全、图注逐句对译；方框类型与数量全对（statementbox 4、definitionbox 2、examplebox 7、notebox 3），跨页方框 2 处（例 4.8 p.82–84、例 4.12 p.89–90）均正确合并 |
| 漏译 | **未发现**（pp.77–92 逐页对过 split 与页面图，段落/脚注/图注无缺；无残留英文整句） |
| 术语 | 块内一致（规范化 / 扭曲扇区 / 离散挠率 / 对偶对称性 / 堆叠 / 上链 / 障碍类…）；**跨块 1 处待 Lead 统一**：「非 Abel」vs「非阿贝尔」；另 2 处记号/批注小疵见可选改 |
| **必须改** | **4 项**：M1 (4.96) 公式抄错；M2 p.92→p.93 跨页句未「开始者写完」（需与 tr06a 联动）；M3/M4 两条 Tutor Note 有事实性错误（会进《译注汇总》） |
| 可选改 | 7 项（见 §7） |

总体判断：**tr-05 三片质量高**：106 条编号公式逐页对位无一缺失，17 条抽查只发现 1 处 $\mathcal{G}$/$G$ 字体误抄；结构、图、方框、漏译全部合格。需处理的是 1 个公式瑕疵、1 个边界规则问题、2 条批注事实错误，其余为统一性建议。

---

## 2. 编号完整性表（`tags_bypage.txt` ⇄ 三片实有）

- tr05a：`4.79 … 4.111`（33 条）；tr05b：`4.112 … 4.157`（46 条）；tr05c：`4.158 … 4.184`（27 条）；合计 **106/106**，**无缺、无重、无跳、无自造**。
- 逐页对位（脚本按 `% [原文 p.N]` 标记归属，与 `tags_bypage.txt` 做集合+顺序比较）：

| 页 | 应有 tags | 实得 | 所在文件 | 判定 |
|---|---|---|---|---|
| p77 | 4.79–4.85（7） | 7 | tr05a | ✓（4.80 在陈述 4.2 框内、4.81/4.82 在陈述 4.3 框内，位置正确） |
| p78 | 4.86–4.90（5） | 5 | tr05a | ✓（4.90 在 p.78 页末） |
| p79 | 4.91–4.95（5） | 5 | tr05a | ✓ |
| p80 | 4.96–4.103（8） | 8 | tr05a | ✓ |
| p81 | 4.104–4.111（8） | 8 | tr05a | ✓（4.109 见 §3-8 排版说明） |
| p82 | 4.112–4.122（11） | 11 | tr05b | ✓（4.115–4.118 在 notebox 内；4.119 起在例 4.8 框内） |
| p83 | 4.123–4.134（12） | 12 | tr05b | ✓（全部在例 4.8 跨页框内） |
| p84 | 4.135–4.140（6） | 6 | tr05b | ✓ |
| p85 | 4.141–4.147（7） | 7 | tr05b | ✓ |
| p86 | 4.148–4.157（10） | 10 | tr05b | ✓ |
| p87 | 4.158–4.162（5） | 5 | tr05c | ✓ |
| p88 | 4.163–4.165（3） | 3 | tr05c | ✓ |
| p89 | 4.166–4.171（6） | 6 | tr05c | ✓ |
| p90 | 4.172–4.176（5） | 5 | tr05c | ✓ |
| p91 | 4.177–4.179（3） | 3 | tr05c | ✓ |
| p92 | 4.180–4.184（5） | 5 | tr05c | ✓ |

结论：**编号完整性 PASS**（不仅总数对，逐页归属也对；本块没有像 p.65/69/73 那样的「纯图页」，每页都有编号公式）。

---

## 3. 逐符号核对表（900–1200 dpi 裁图，逐字符比对）

> 裁图存档：`work/tmp/rv_*_4_*.png`、`rv2_*_4_*.png`（`pymupdf` 定位 tag 后整行裁切，900 dpi；(4.96) 另加 1200 dpi 局部复核）。

| # | 页 | tag | 原文（裁图转写） | tr05 实有 | 判定 |
|---|---|---|---|---|---|
| 1 | 77 | (4.80) | $[\beta]\in H^2\!\left(G^{(0)},U(1)\right).$ | `[\beta]\in H^2\left(G^{(0)},U(1)\right)` | ✓ |
| 2 | 78 | (4.90) | $\mathcal{I}_{d+1}[B_{p_i+1}]=\exp(2\pi iS^{\mathrm{eff}}_{d+1})$ | `\exp\left(2\pi\ii S^{\text{eff}}_{d+1}\right)` | ✓（原文微分用斜体 $i$；译作 $\ii$ 符合项目惯例） |
| 3 | 79 | (4.91) | $\mathcal{I}_{d+2}=dS^{\mathrm{eff}}_{d+1}$ | `\mathcal{I}_{d+2}=\dd S^{\text{eff}}_{d+1}` | ✓（同上，$\dd$ 为项目规范） |
| 4 | 79 | (4.93) | $\mathcal{I}_{d+2}=\int dB_2^e\wedge dB^m_{d-2}\equiv\int F_3^e\wedge F^m_{d-1}$ | 同 | ✓（含 $\equiv$、$F_3^e$、$F^m_{d-1}$ 下标） |
| 5 | 80 | (4.96) | $\dfrac{\mathcal{G}}{G^{(1)}}=\dfrac{G/\mathcal{Z}}{G^{(1)}}\equiv\dfrac{G}{\mathcal{X}},\ \mathcal{X}\subseteq Z(G)$ | $\dfrac{\mathcal{G}}{G^{(1)}}=\dfrac{\mathcal{G}/\mathcal{Z}}{G^{(1)}}\equiv\dfrac{G}{\mathcal{X}}$ | **✗ 第二个分子误作 $\mathcal{G}$**（原文为普通斜体 $G$，1200 dpi 裁图确认；见 M1） |
| 6 | 80 | (4.101) | $W_2=i(w_2)+\widetilde{B}^e_2$ | `W_2=i(w_2)+\tilde{B}_2^e` | ✓（$\tilde{B}$ 与 $\widetilde{B}$ 字形可接受） |
| 7 | 81 | (4.106) | $\delta\widetilde{B}^e_2=i(\mathrm{Bock}(B^e_2))$ | 同 | ✓ |
| 8 | 81 | (4.107) | $\delta w_2=-\mathrm{Bock}(B^e_2)$ | 同 | ✓（负号、直体 Bock） |
| 9 | 81 | (4.109) | 两行长正合列 + 弯箭头 $H^p(M,C)\to H^{p+1}(M,A)$ 标 Bock | `gathered` 两行，次行行首 `\xrightarrow{\ \mathrm{Bock}\ }` | ✓（语义等价的重排，tr05a 第 239 行批注已声明；与原文两行布局的差异属版式） |
| 10 | 82 | (4.112) | $S\to S+2\pi s(d)\int\Lambda^m_{d-3}\cup_\eta\delta w^m_2,\ s(d)=(-1)^d$ | 同（含 $w^m_2$ 上标 $m$） | ✓（原文确印 $w^m_2$，tr05b 已加批注；见 O4） |
| 11 | 82 | (4.113) | $Z[B_2^e,B^m_{d-2}+d\Lambda^m_{d-3}]=\exp(-2\pi i s(d)\int\Lambda^m_{d-3}\cup_\eta\mathrm{Bock}(B^e_2))\times Z[\cdots]$ | 同（$d\Lambda$，非 $\delta\Lambda$） | ✓ 照录；但原文此处 $d\Lambda$ 与 (4.111) 的 $\delta\Lambda$ 不一致，建议补批注（O7） |
| 12 | 83 | (4.126) | 首行 $0\to\mathcal{Z}\to\mathcal{X}=Z(G)\to G^{(1)}\to 0$；次行以「$=0\to\mathbb{Z}_2\to\mathbb{Z}_4\to\mathbb{Z}_2\to0$」 | `aligned`，& 置于次行「=」前 | ✓（对齐点与原文一致） |
| 13 | 86 | (4.156) | $\mathcal{Y}=\widehat{G^{(d-3)}/H^{(d-3)}}\subseteq\mathcal{Z}$ | 同（宽 hat 覆盖整个商） | ✓ |
| 14 | 87 | (4.161) | $\mathcal{I}_4[B_2]=\exp\!\left(\pi i\int\dfrac{\mathcal{P}(B_2)}{2}\right)$ | 同（$\mathcal{P}$、分母 2） | ✓（批注表述见 O5） |
| 15 | 91 | (4.177) | $g\in G^{(p)}=\widehat{\widehat{G}}^{(p)}=\widehat{G}^{(d-p-2)}$ | 同（双 hat + $(p)$ 在外） | ✓ |
| 16 | 92 | (4.183)/(4.184) | $d=2p+2$；$(q,t)=(\widehat{g},g)\in\widehat{G}^{(p)}\times G^{(p)}$ | 同 | ✓ |
| 17 | 89 | (4.171) | $\exp(i\pi\int b_2)=\exp(i\pi\int w_2)$ | 同 | ✓ |

补充检查（页面图 200 dpi 逐式对读，未单列裁图）：(4.79)(4.83)–(4.85)(4.86)–(4.89)(4.92)(4.94)(4.95)(4.97)–(4.100)(4.102)–(4.105)(4.108)(4.110)(4.111)(4.114)–(4.118)(4.119)–(4.136)(4.137)–(4.140)(4.141)–(4.147)(4.148)–(4.152)(4.153)–(4.157)(4.158)–(4.160)(4.162)–(4.165)(4.166)–(4.169)(4.170)(4.172)–(4.175)(4.176)(4.178)–(4.182) 均与裁图/页面图一致（含 $\mathcal{G}$/$G$、$\mathcal{Z}$/$\mathbb{Z}_2$、$\widehat{\ }$ 位置、$s(d)$ 与 $s(p)$ 的区别）。

---

## 4. 结构（标题 / 图 / 方框 / 编号层级）

| 项 | 原文位置 | tr05 实现 | 判定 |
|---|---|---|---|
| 4.2.3 Anomaly Theory and Anomaly Polynomial | p.77（(4.82) 之后） | tr05a `\subsubsection{反常理论与反常多项式}`，位置正确 | ✓ |
| 4.2.4 Mixed 't Hooft Anomaly for a Non-Abelian Gauge Theory | p.79（(4.95) 之后） | tr05a `\subsubsection{非 Abel 规范理论的混合 't Hooft 反常}` | ✓ |
| 4.3 Gauging | p.84 | tr05b `\subsection{规范化（gauging）}` | ✓ |
| 4.3.1 Definition | p.84 | tr05b `\subsubsection{定义}` | ✓ |
| 4.3.2 Discrete Torsion | p.87 | tr05c `\subsubsection{离散挠率（discrete torsion）}` | ✓ |
| 4.3.3 Dual Symmetries Obtained After Gauging | p.88 | tr05c `\subsubsection{规范化后得到的对偶对称性}` | ✓ |
| 4.3.4 Gauging Exchanges Twisted and Charged Sectors | p.90 | tr05c `\subsubsection{规范化交换扭曲扇区与带电扇区}` | ✓ |
| 图 17（p.78） | 页面顶部，图注对译 | tr05a 有 `fig17.png`（width 0.92）+ 图注（M_{d+1}/M_d/I_{d+1}/T、bulk 两图语义全保留） | ✓ |
| 图 18（p.91） | 顶部，图注对译 | tr05c 有 `fig18.png`（0.9）+ 图注（含「严格地说只有 O 在 G^(p) 下不带荷时」） | ✓ |
| 图 19（p.92） | 顶部，图注对译 | tr05c 有 `fig19.png`（0.85）+ 图注 | ✓ |
| 蓝色 Statement | 4.2(p.77)、4.3(p.77)、4.4(p.84)、4.5(p.88) | `statementbox` ×4，编号 4.2/4.3/4.4/4.5 照原文 | ✓ |
| 绿色 Definition | 4.6(p.78)、4.7(p.90) | `definitionbox` ×2 | ✓ |
| 橙色 Example | 4.8–4.14（p.82/85/86/87/89/91/92） | `examplebox` ×7，编号照原文 | ✓ |
| 粉色带标题 notebox | p.81、p.82、p.88（共 3） | `notebox` ×3（上同调相伴长正合列 / Bockstein 的消失 / 不可逆的表示对称性） | ✓ |
| 跨页方框合并 | 例 4.8（p.82→84）、例 4.12（p.89→90） | 均合并为单框，`% [原文 p.N]` 标记保留在框内 | ✓ |
| 行内小标题 | 各 `\para{}`（三个障碍类 / 联系各障碍类 / 障碍类 $w_2$ 的非闭性 / 计算 't Hooft 反常 / 开流形上的 SPT 相 / 反常理论 / 反常多项式 / 例子 / 对偶的对偶 / 扭曲变为带电 / 带电变为扭曲 / 带电+扭曲变为扭曲+带电 / SPT 相的叠加…） | 全部译为 `\para{}` | ✓ |
| 编号层级 | 4.2→4.2.1→4.2.2（tr-04）→4.2.3→4.2.4→4.3→4.3.1… | tr05 只用 `\subsubsection`/`\subsection`，自动编号与原文一致 | ✓ |

---

## 5. 漏译 / 多译检查（pp.77–92 逐页对 split + 页面图）

**未发现漏译**。逐页核对的段落清单（全部有对应译文）：

- p.77：(4.79) 引句、「Thus, we obtain the following statement」、陈述 4.2 全部文字、「We can easily generalize (4.76)」、陈述 4.3 全部文字、4.2.3 标题、「For the discussion…」、SPT Phases on Open Manifold 段、(4.83)–(4.85)。
- p.78：图 17 + 图注、「where $Z_\partial$…」段、Anomaly Theory 段、(4.86)、「The combined hybrid…」段、定义 4.6 框内全部、(4.89)、Anomaly Polynomial 段、(4.90)。
- p.79：(4.91)、「as is familiar…」、「The 't Hooft anomaly $\mathcal{I}_d$…」段、Examples 段、三条 bullet（Maxwell / 离散规范理论 / 2d 离散 0-形式）、「See the remark…」、4.2.4 标题与引言段。
- p.80：Three Obstructions 段 ×2、Relating the Obstructions 段、(4.97)–(4.103)。
- p.81：Non-Closure 段、(4.104)(4.105)、Bockstein 定义段、(4.106)(4.107)、notebox 全部文字（含「每一行中的映射…」）、Computing 段、(4.111)。
- p.82：(4.112)–(4.114)、notebox 全部（含 $\pi\circ s=1$、$\mathcal{X}=\mathcal{Z}\times\mathcal{Y}$、$\mathcal{Y}\cong G^{(1)}$）、例 4.8 开头。
- p.83：例 4.8 中段（全部公式与「where $\cup$ is the standard cup product」等）。
- p.84：例 4.8 尾、4.3、4.3.1、「Concretely this means…」、(4.137)–(4.140)、陈述 4.4。
- p.85：Gauging Electric… 段、例 4.9 全部、一般化段、(4.144)–(4.147)。
- p.86：Gauging Magnetic… 段、例 4.10 全部、一般化段、(4.152)–(4.157)。
- p.87：4.3.2、(4.158)(4.159)、两段正文、例 4.11 全部。
- p.88：4.3.3、两段、陈述 4.5、「Note the restriction…」、notebox 全部。
- p.89：Dual of Dual 段、(4.166)–(4.169)、「Thus we indeed return…」、Gauging Electric… 段、例 4.12 开头与 (4.170)(4.171)。
- p.90：例 4.12 尾（跨页框）、(4.172)–(4.175)、4.3.4、Twisted becomes Charged 段、定义 4.7、(4.176)。
- p.91：图 18 图注、「identified with the identity…」、(4.177)–(4.179)、例 4.13、Charged to Twisted 段。
- p.92：「leads us back…」、图 19 图注、(4.180)–(4.184)。

无原文没有的多译内容；无整句残留英文（脚本扫描：唯一长英文串均为数学/保留术语 SPT、Yang–Mills、't Hooft、Dirac、discrete torsion、dual symmetries）。pp.77–92 原文无脚注，故无脚注遗漏。

---

## 6. 术语一致性

**块内一致，问题在跨块**：

1. **「非 Abel」vs「非阿贝尔」（跨块，需 Lead 全局裁决）**：tr05a/b/c 全用「非 Abel」（共 3+6+5 处）；`c01`、`tr03a/b/c` 也用「非 Abel」，但 `tr01a/b`、`tr04a`、`tr06b`、`tr07a/c`、`tr08a/b` 用「非阿贝尔」。同一本书两种写法，建议统一（见 M/O1）。
2. **$\cup_\eta$ 排版**：tr05 三片全用 `\cup_\eta`（下标形式）；tr04 两片用 `\underset{\eta}{\cup}`（正下方）。同一记号两种排版，建议由 Lead 统一（O8）。
3. **$\hat{\mathcal{Z}}$ vs $\widehat{\mathcal{Z}}$**：tr05b 的 (4.124)、(4.152) 用 `\hat{\mathcal{Z}}`，tr05c 的 (4.172) 用 `\widehat{\mathcal{Z}}`（同书 tr04 用 `\widehat{\mathcal{Z}}`）。建议统一为 `\widehat{\mathcal{Z}}`（O2）。
4. 其他与 glossary 一致：规范场/背景场/规范变换/上链/群上同调/障碍类/离散挠率/扭曲扇区/不可逆对称性/不可逆/对偶对称性/Pontryagin 对偶/单连通群/场强/SPT 相/异常（无反常用）/拉回/堆叠（stacking，tr05 新用，块内 4 处一致）。
5. **本报告补登术语**（glossary 暂无，供 Lead 汇总）：stacking→堆叠；gauged theory→规范化理论；quantum symmetries→量子对称性；dual symmetries→对偶对称性；gauge-inequivalent→规范不等价；Lagrange multiplier→Lagrange 乘子；Bockstein map→Bockstein 映射；long exact sequence→长正合列；splitting/split→分裂（可裂）；faithful→忠实（tr-04 已登）；cocharacter→余特征标；descent procedure→下降程序；anomaly theory→反常理论。

---

## 7. 必须改 / 可选改（每项给可替换文本）

### 【必须改】（4 项）

**M1｜tr05a.tex :149｜(4.96) 第二个分子抄错：$\mathcal{G}/\mathcal{Z}$ → $G/\mathcal{Z}$**
原文（p.80，1200 dpi 裁图确认）：$\dfrac{\mathcal{G}}{G^{(1)}}=\dfrac{G/\mathcal{Z}}{G^{(1)}}\equiv\dfrac{G}{\mathcal{X}}$：第一个分子为花体 $\mathcal{G}$，第二、三个分子为普通斜体 $G$。tr05a 第二个分子误作 `\mathcal{G}/\mathcal{Z}`，**既非原文，数学上也不自洽**（$(\mathcal{G}/\mathcal{Z})/G^{(1)}=(G/\mathcal{Z}^2)/G^{(1)}$），且与该文件第 154 行批注给出的推导 $\mathcal{G}/G^{(1)}=(G/\mathcal{Z})/(\mathcal{X}/\mathcal{Z})=G/\mathcal{X}$ 相矛盾。替换（整行）：

```latex
\frac{\mathcal{G}}{G^{(1)}}=\frac{G/\mathcal{Z}}{G^{(1)}}\equiv\frac{G}{\mathcal{X}}\,,\qquad \mathcal{X}\subseteq Z(G)\,, \tag{4.96}
```

**M2｜tr05c.tex 末尾 + tr06a.tex :4｜p.92→p.93 跨页句未按「开始者写完」收尾**
p.92 末句由 tr-05 开始：「设 $\mathcal{O}$ 是 $\mathcal{T}$ 中具有下述性质的算符 (4.184)」，其「其中 $q$ 表示…$t$ 表示…」的收尾从句被写在 **tr06a.tex 第 4 行**（p.93 内容），违反 BRIEF「谁开始这句谁写完」。内容本身不缺不重（tr06a 已代写），但若 Lead 要严格执行规则，需两文件联动：
- tr05c.tex 在 `\tag{4.184}` 的 `\end{equation}` 之后补：
```latex
其中 $q$ 表示在 $G^{(p)}$ p-形式对称性下的电荷，$t$ 表示算符 $\mathcal{O}$ 所处的、关于 $G^{(p)}$ p-形式对称性的扭曲扇区。
```
- tr06a.tex 第 4 行删去上述从句，保留 `% [原文 p.93]` 与紧接的「在规范化后的理论 $\mathcal{T}/G^{(p)}$ 中，算符 $\mathcal{O}$ 具有性质」。
> 若 Lead 决定「按现状接受」（无缺口、无重复，仅归属不同），可将本项降级为「已知偏差」。

**M3｜tr05a.tex :18｜(4.80) 批注事实错误：$H^1(\mathbb{Z}_2,U(1))\neq 0$**
现注称「若误写成 $H^1$ 就会得到 $H^1(\Z_2,U(1))=0$，与『2d 存在非平凡 $\Z_2$ SPT』矛盾」。实际 $H^1(\Z_2,U(1))=\mathrm{Hom}(\Z_2,U(1))=\Z_2\neq 0$，锚点失效（会进《译注汇总》，属事实错误）。建议替换为次数锚点：

```latex
% [Tutor Note: p.77 式 (4.80)——2d 玻色 SPT 相由 $[\beta]\in H^2(G^{(0)},U(1))$ 刻画（Dijkgraaf–Witten），$\beta$ 是 $G^{(0)}$ 的 $\C^\times$ 值 2-上链，$\delta\beta=1$ 即上闭链条件（式 (4.75)）。次数锚点：配分函数取 (4.76) 的 $\int A_1^*\beta$，被积的是 2-上链，只能在 2 维面上积分，故必须是 $H^2$（若写成 $H^1$，$\beta$ 是 1-上链，$\int_{\text{2-单纯形}}\beta$ 无定义）。例：$H^2(\Z_2,U(1))=\Z_2$，恰对应 2d 的平凡相与一个非平凡相。英文原词：group cohomology with coefficients in $U(1)$。]
```

**M4｜tr05c.tex :198｜(4.178)–(4.179) 批注事实错误：$\delta_g$ 应为 3-上链**
现注称「对 $\Z_2$ 1-形式对称性，$\delta_g$ 是 $M_{d-3}$ 上的 $\Z_2$ 值 **2-上链**」。按 (4.178)，左边 $\delta B_{p+1}$ 是 $(p+2)$-上链；$p=1$ 时为 **3-上链**，故支撑在 $M_{d-3}$（余维 3）上的 $\delta_g$ 也必须是 3-上链。替换片段：

```latex
对 $\Z_2$ 1-形式对称性，$\delta_g$ 是支撑在 $M_{d-3}$ 上、取值于 $\Z_2$ 的 3-上链（因为 $\delta B_2$ 是 3-上链，$M_{d-3}$ 余维为 3），$\delta b_2=\delta_g$ 表示 $b_2$ 沿围绕 $M_{d-3}$ 的 2-球面有 $\Z_2$ 通量 $g$，与 (2.105) 的荷定义一致。
```

### 【可选改】（7 项）

**O1｜tr05a/b/c｜「非 Abel」→「非阿贝尔」（需与 c01、tr-03 一并改；跨块统一）**
替换：`非 Abel` → `非阿贝尔`（tr05a 3 处、tr05b 6 处、tr05c 5 处；如 Lead 决定采用「非 Abel」，则反向改 tr-01/04/06/07/08）。glossary 无此条，建议同时回写 glossary。

**O2｜tr05b.tex :74、:261｜`\hat{\mathcal{Z}}` → `\widehat{\mathcal{Z}}`（与 (4.172) 及全书统一）**
替换：`G^{(d-3)}=\hat{\mathcal{Z}}=\Z_2` → `G^{(d-3)}=\widehat{\mathcal{Z}}=\Z_2`；`G^{(d-3)}=\hat{\mathcal{Z}}` → `G^{(d-3)}=\widehat{\mathcal{Z}}`。

**O3｜tr05a.tex :64｜批注「下式 (4.86)」→「上式 (4.86)」**
(4.86) 在 (4.88) 之前，改「下式」为「上式」即可：`而下式 (4.86) 给的是` → `而上式 (4.86) 给的是`。

**O4｜tr05b.tex :19｜批注列证含 (4.115)，但 (4.115) 不含 $w_2$**
(4.115) 是 $[\mathrm{Bock}(B_2^e)]=0$，没有 $w_2$。替换：`而 (4.107)、(4.115)、(4.135) 以及例 4.8 中的 (4.127) 都写成 $w_2$` → `而 (4.107)、(4.135) 以及例 4.8 中的 (4.127) 都写成 $w_2$`。

**O5｜tr05c.tex :42｜(4.161) 批注「$\mathcal{P}(B_2)$ 取偶值」表述过强**
严格说法是 $\mathcal{P}(B_2)$ 为 $\Z_4$ 值 4-上链、$\int\mathcal{P}(B_2)$ 只在模 4 意义下良定义，相位只依赖这一模 4 数据。替换：

```latex
% [Tutor Note: p.87 式 (4.161)——$\mathcal{P}$ 是 Pontryagin 平方（见 (3.193) 附近）。对 $\Z_2$ 值 2-上链 $B_2$，$\mathcal{P}(B_2)$ 是 $\Z_4$ 值 4-上链，故 $\int\mathcal{P}(B_2)$ 只在模 $4$ 意义下良定，相位 $\exp(\pi\ii\int\mathcal{P}(B_2)/2)$ 正由这一模 $4$ 数据给出；分母 2 与 (3.193) 的归一化配套，漏掉它会使 (4.162) 中 $\SO(3)_-$ 的离散 theta 角错档。]
```

**O6｜tr05c.tex :109｜(4.169) 批注 Koszul 幂次推导差一个符号**
注称 $(-1)^{(p+1)(d-p-1)}$ 在 $d-p-1$ 为奇数时「约化为 $(-1)^p$」；实际指数奇偶为 $p+1$，即 $(-1)^{p+1}$。建议删去该中间推导，只留可核对结论与锚点：

```latex
% [Tutor Note: p.89 式 (4.167)–(4.169)——$b_{p+1}$ 与 $b_{d-p-1}$ 都是奇数次形式时交换产生的 Koszul 符号与 $d$ 的奇偶共同给出 (4.169) 的 $(-1)^p$，这与 (4.94) 的 $s(p)=(-1)^p$ 同源。可核对锚点：$p=1,d=4$ 时 (4.169) 直接给出 $b_2=-B^{\text{new}}_2$，与原文「up to a sign」措辞一致。]
```

**O7｜tr05b.tex｜(4.113) 建议补一条原文笔误批注**
原文 (4.113) 的宗量写作 $B^m_{d-2}+d\Lambda^m_{d-3}$（微分 $d$），而同一段的规范变换 (4.111) 是 $B^m_{d-2}\to B^m_{d-2}+\delta\Lambda^m_{d-3}$（上链微分 $\delta$）；离散情形应为 $\delta\Lambda$。tr05b 照录无误，但未加提示。建议在 (4.113) 后补：

```latex
% [Tutor Note: p.82 式 (4.113)——原文宗量写作 $B^m_{d-2}+d\Lambda^m_{d-3}$（微分 $d$），与 (4.111) 的离散规范变换 $+\delta\Lambda^m_{d-3}$ 不一致；按离散上链的上下文应为 $\delta\Lambda^m_{d-3}$。译文照录原文并在此说明。]
```

**O8｜版式统一（Lead 裁决）｜`\cup_\eta` vs `\underset{\eta}{\cup}`**
tr05（及 tr01b/01c/06/07）用 `\cup_\eta`（下标在右下），tr04 用 `\underset{\eta}{\cup}`（$\eta$ 正下方）。二者都是合法 LaTeX，编译后字形不同；建议全书统一（若按原文字形，$\eta$ 在 $\cup$ 正下方，则应统一为 `\underset{\eta}{\cup}`）。

---

## 8. 边界接缝复核

1. **tr-04 → tr05a（p.76/77）**：tr04c 末为 p.76「群上链的拉回」notebox 与 (4.78)；tr05a 首行为 p.77「注意，对 1-群上链 $\lambda$ 作替换 (4.79)…」。与原文 p.76 末 / p.77 首严格对应，**无重复、无缺口** ✓。
2. **tr05a → tr05b（p.81/82）**：tr05a 以 (4.111)（p.81 末行）结束；tr05b 以「由耦合项 (4.27) 可见，作用量被修改为 (4.112)」开始，与 p.82 首段一致，**衔接干净** ✓。
3. **tr05b → tr05c（p.86/87）**：tr05b 以 (4.157) 结束（p.86 末）；tr05c 以 4.3.2 标题开始（p.87），**衔接干净** ✓。
4. **tr05c → tr06a（p.92/93）**：**有问题**——tr05c 停在 (4.184) 的「设 $\mathcal{O}$ 是 $\mathcal{T}$ 中具有下述性质的算符」，其必需的「其中 $q$…$t$…」从句由 tr06a 首段代写（见 **M2**）。内容不缺不重，但归属违反「开始者写完」，需 Lead 裁决（联动修改或记为已知偏差）。
5. 另一类边界：**跨页方框**（例 4.8 p.82–84、例 4.12 p.89–90）均正确合并为单框、`% [原文 p.N]` 标记保留在框内，未出现「一框拆两框」✓。

---

## 9. 校对方法与可复核性

- **编号**：脚本抽取三片 `\tag{x.y}`（106 条），与 `tags_bypage.txt` pp.77–92 做「逐页集合 + 顺序」比较（结果 16/16 页 `OK`，总区间 4.79→4.184 逐 1 递增 `PASS`）；并核对每页 `% [原文 p.N]` 标记齐全（tr05a 77–81、tr05b 82–86、tr05c 87–92）。
- **公式**：`pymupdf` 在 PDF 内用 `page.search_for('(4.xx)')` 定位 tag 的精确 bbox，再以 900 dpi 裁切整行（(4.96) 额外 1200 dpi 局部），逐字符比对上下标/字体（`\mathcal` vs 普通斜体、`\widehat` 覆盖范围、$s(d)$/$s(p)$、正负号、分母 2 等）。裁图存档于 `work/tmp/rv_*`、`rv2_*`。
- **结构/漏译**：逐页读 200 dpi 页面图 + split 文字层（p080、p084 等含 NUL 的文字层已用 UTF-8 容错解码），按段落清点标题、图注、方框、脚注。
- **术语**：`Select-String` 统计全书各 chunk 的关键词频（非阿贝尔/非 Abel、算子/算符、堆叠、扭曲扇区、离散挠率、`\cup_\eta` 与 `\underset` 等），定位跨块不一致。
- **未做的事**：未编译、未修改任何他人文件；本报告全部结论可由上述存档裁图与脚本复现。
