# BRIEF · SY02-20《几何 Satake、范畴迹与志村簇的算术》

## 原文

| 项 | 内容 |
| --- | --- |
| 原题 | Geometric Satake, categorical traces, and arithmetic of Shimura varieties |
| 作者 | 朱歆文（Xinwen Zhu），加州理工学院 |
| 场合 | Current Developments in Mathematics 2016 会议报告 |
| 版本 | arXiv:1810.07375，2018 年，50 页，amsart 11pt |
| 结构 | 6 节 21 小节，76 个定理类对象（含 1 个被 `\quash` 隐藏）、65 个编号公式、48 条文献 |
| 文件 | `工程文件/work/原文/main.tex`（2671 行）、`工程文件/work/pdf/src.pdf`（50 页） |

**原文性质。** 会议综述，不是专著：定义与主要定理给全，证明多半只给梗概，大量细节引文献。
全篇以反常层、叠、$p$ 进群表示论与 Shimura 簇的现代语言写成。第 1 节是引言，
第 2–5 节是主干（几何 Satake → 范畴迹 → 迹的几何 Satake 版本 → 算术应用），第 6 节是附录。

## 一句话主旨

几何 Satake 把 $G$ 的仿射 Grassmann 簇上的反常层范畴等同于对偶群 $\hat G$ 的表示范畴；
对它取范畴迹，就得到一个作用于 Shimura 簇模 $p$ 纤维上同调的新代数 $\mathbf J$，
而这正是 $p$ 进几何与 Shimura 簇算术之间的第二条通道。

## 五步逻辑链

1. **几何化。** 球面 Hecke 代数 $H_G$ → 仿射 Grassmann 簇 $\Gr$ → 反常层范畴 $\Sat_G=\on{P}_K(\Gr)$
   → 几何 Satake 等价 $\Sat_G\simeq\on{Rep}_{\Ql}(\hat G)$（定理 2.1.15）。
2. **动机化。** $\Sat_G^0$ 由 $(\Gr_\mmu,m)$ 生成 → 忠实嵌入 $\on{H}(\cdot,\cdot)\hookrightarrow\Hom_{\on{Mot}^*}$
   （引理 2.2.1）→ 幂等完备化得 $\Sat^m_G$，取 $v=q$ 后与 $\on{Rep}(\hat G^T)$ 等价（注 2.2.4）。
3. **范畴化。** 代数的迹（余中心）→ $\sigma$-扭迹函子与 $\Tr_\sigma(\mC)$（命题 3.1.1）
   → 有限 Hecke 范畴 $\on{D}^C(X)$ 上的 $S$-算子（构造 3.2.5、推论 3.2.6）
   → 有限版 $S=T$（命题 3.2.9，用 Braverman–Varshavsky 迹公式）。
4. **仿射化。** 局部 Shtuka 的模空间 $\Sht^\loc$ → 有限维逼近 $\Sht^{\loc(m,n)}_\mmu$
   → 对应范畴 $\on{P}^\Hk(\Sht^\loc_{\bar k})$（§4.2）→ 定理 4.3.1：存在 $S$ 使下图交换，
   $S(\mO)=\widetilde{\delta_e}$，且 $S$ 在 $\mathbf J=\Ql[\hat G\sigma]^{\hat G}$ 上给出 Satake 同构。
5. **算术落地。** $\loc_p:\Sh_\mu\to\Sht^\loc_\mu$（命题 5.1.1）→ $\mathbf J$ 作用在
   $\on{H}^*_c(\Sh_{\mu,\overline\bF_v})$ 上（定理 5.1.3）→ 猜想 5.1.4（$S=T$）
   → Tate 轮：定理 5.2.1 用相交数矩阵给出轮类映射的单射性，进而得到 Tate 猜想的部分情形。

## 分块表

| 块 | 节 | 原文行 | 编号对象 | 目标文件 |
| --- | --- | --- | --- | --- |
| ch01 | §1 引言 | 368–384 | — | `chunks/ch01.tex` |
| ch02 | §2 节首 + §2.1 经典 Satake | 385–481 | 1 例、3 公式 | `chunks/ch02.tex` |
| ch03 | §2.1 格论例子、Witt 向量 | 482–547 | 1 注、2 例、1 引理 | `chunks/ch03.tex` |
| ch04 | §2.1 仿射 Grassmann 簇的定义 | 548–604 | 1 定理、1 注、1 例 | `chunks/ch04.tex` |
| ch05 | §2.1 Schubert 簇与 Satake 范畴 | 607–676 | 2 例、1 引理、若干公式 | `chunks/ch05.tex` |
| ch06 | §2.1 卷积积与几何 Satake 定理 | 677–742 | 1 定理、1 注、1 引理 | `chunks/ch06.tex` |
| ch07 | §2.2 动机 Satake（前） | 743–810 | 1 引理、1 注 | `chunks/ch07.tex` |
| ch08 | §2.2 动机 Satake（后） | 810–944 | 2 引理、1 例、1 注 | `chunks/ch08.tex` |
| ch09 | §3 节首 + §3.1 范畴迹 | 945–1009 | 1 命题、2 注 | `chunks/ch09.tex` |
| ch10 | §3.1 命题证明 | 1010–1131 | 2 注、1 例 | `chunks/ch10.tex` |
| ch11 | §3.1 $S_V$ 与 $K$-环 | 1132–1184 | 1 命题、3 注 | `chunks/ch11.tex` |
| ch12 | §3.2 节首与两例 | 1192–1305 | 2 例、1 注、1 引理 | `chunks/ch12.tex` |
| ch13 | §3.2 $S$-算子 | 1310–1419 | 1 构造、1 推论 | `chunks/ch13.tex` |
| ch14 | §3.2 有限版 $S=T$ | 1420–1494 | 1 命题、1 注 | `chunks/ch14.tex` |
| ch15 | §4 节首 + §4.1 局部 Shtuka | 1495–1600 | 2 例、2 注 | `chunks/ch15.tex` |
| ch16 | §4.1 有限维逼近 | 1601–1740 | 1 例、1 注、若干公式 | `chunks/ch16.tex` |
| ch17 | §4.1 命题 + §4.2 开头 | 1741–1830 | 1 命题、1 注 | `chunks/ch17.tex` |
| ch18 | §4.2 对应范畴 | 1830–1931 | 2 注、1 命题 | `chunks/ch18.tex` |
| ch19 | §4.3 + §5.1 前段 | 1932–2044 | 1 定理、2 注、1 命题 | `chunks/ch19.tex` |
| ch20 | §5.1 定理与猜想 | 2045–2120 | 2 定理、1 猜想、3 注 | `chunks/ch20.tex` |
| ch21 | §5.2 Tate 轮 | 2121–2210 | 1 定理、1 注、1 例 | `chunks/ch21.tex` |
| ch22 | §6 节首 + §6.1 前段 | 2211–2380 | 1 定义、2 引理、1 例子 | `chunks/ch22.tex` |
| ch23 | §6.1 前推/拉回 | 2386–2478 | 2 引理 | `chunks/ch23.tex` |
| ch24 | §6.2 对应范畴 | 2479–2554 | 1 引理、1 注 | `chunks/ch24.tex` |
| ch25 | 参考文献 | 2555–2671 | 48 条 `\bibitem` | `chunks/ch25.tex` |

合计 **140 个编号对象**（75 个定理类 + 65 个编号公式），与原 PDF 逐条一致
（`工程文件/scripts/sim_numbering.py` → `orig 140 / mine 140 / mismatch 0`）。
原文 76 个定理类对象中，注 `R: cat tr infty cat`（原文 1185–1190 行）被作者用 `\quash{}` 包住，
PDF 中不出现，译文同样剔除，故计 75。

## 施工流程（每块）

1. 从 `工程文件/work/原文/main.tex` 取本块行段，对照 `work/pdf/src.pdf` 对应页核公式。
2. 环境名照原文（thm/prop/lem/cor/ex/rmk/construction/…），全部挂在 `thm` 计数器上。
3. `\label`/`\ref`/`\eqref`/`\cite` 的 key 一字不改；不手写任何编号。
4. 数学模式里的中文一律 `\text{}`；tikz-cd 单元里同样；amscd 中文标注写 `@V{\text{…}}VV`。
5. 整书编译（`bash 源码/build.sh`，两遍 xelatex），查 `!`、Overfull、Missing character、未定义引用。
6. 写 `工程文件/reports/chNN.md` 记录原文行、编号对象、译注、坑。

## 纪律与已知坑

- **定理与公式是两个独立计数器**：`\newtheorem{thm}{定理}[subsection]` + `\numberwithin{equation}{subsection}`，
  不能像 SY02-17 那样把定理挂到 equation 计数器上，否则既丢段号又错位。
- `\quash{}` 段必须剔除，否则其后所有定理编号整体错一位（译文不译该段，`资料卡/04` 有记录）。
- `xy` 必须在 tikz 之后加载；`\resizebox` 不能包 tikz-cd（`&` 的 catcode 出错）。
- `port_macros2.py` 对一行多个 `\nc{..}{..}` 只展开第一个，故需 `\newcommand{\nc}{\newcommand}` 兜底。
- `\allowdisplaybreaks[2]` 必须在 `amsmath` 之后。
- 中文写脚本输出时先 `export PYTHONIOENCODING=utf-8`，否则 stdout 走 cp936，落盘成 GBK。
- 译注用 manyfoot 的独立序列 `trans`（印作「译注 N」），与原文自带脚注的计数器互不干扰。
