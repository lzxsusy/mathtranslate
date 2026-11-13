# 复核报告：ch01a / ch02a / ch03b（task-17）

复核人：tr02　复核日期：2026-11-07
范围：`src/chunks/ch01a.tex`（原书 p.11–29）、`src/chunks/ch02a.tex`（原书 p.80–107）、`src/chunks/ch03b.tex`（原书 p.180–192）
方法：页标逐页与英文页首句并排比对；陈述编号/类型/所在页三方对齐；公式逐符号开页图核对（抽样页全文核，其余按页抽查）；图逐张与原页比对；术语按 `术语对照表.tsv` 与 tr05 全书专名统一口径复核。

## 一、页标核对

用 `work/review/_mk.py` 把每页英文首句与该页中文首句并排打印，三块逐页过一遍（`work/review/_pages.py` 输出分页字数/句数比仅作辅助，公式密集页的比值离群不作漏译判据）。

| 块 | 页标序列 | 条数 | 缺口 | 重复 |
|---|---|---|---|---|
| ch01a | 11–29 | 21 | 无 | p.21、p.25（同页两段：p.21 后半为测量段起首，p.25 后半为 §1.5 起首；合法） |
| ch02a | 80–107 | 29 | 无 | p.95（§2.5 标题与引言在 p.95 末，p.96 起 3.5.1；修后合法） |
| ch03b | 180–192 | 13 | 无 | 无 |

**改动一处（硬错误）**：`src/chunks/ch02a.tex` 中 `\section{渐近方法}` 前的页标原为 `% [原文 p.96]`，改为 `% [原文 p.95]`。依据：原书 p.95 末尾即「2.5 Asymptotic Method」标题与整段引言（该页末句 "aiming at motivating our later path integral manipulations."），p.96 才从 "2.5.1 Laplace's Method" 起；ch02a 原稿自带的注释「\section{渐近方法} 在原书 p.96」是作者误记。

ch01a 与 ch02a 的页标多数落在段落边界、比真实页首晚一两句（跨页段落整段留在前页段内），内容完整、顺序正确，不按错误处理。

## 二、陈述编号 / 类型 / 所在页

用 `work/review/_stmts.py` 比对英文页中的 `Definition/Theorem/… N.N.N` 与 tex 的 `\begin{env}{N.N.N}`。三块完全一致，无编号错、类型错、页码错：

- ch01a 13 条：定义 1.1.1(p.11)、例 1.1.2/1.1.3(p.12)、注 1.1.4(p.12)、定义 1.1.5/1.1.6(p.14)、注 1.1.7(p.15)、注 1.3.1(p.19)、定义 1.4.1(p.21)、命题 1.4.2(p.22)、注 1.4.3(p.23)、例 1.4.4(p.23)、例 1.4.5(p.24)。
- ch02a 7 条：注 2.2.1(p.85)、命题 2.3.1(p.89)、注 2.3.2(p.89)、例 2.5.1(p.97)、例 2.5.2(p.98)、例 2.5.3(p.100)、例 2.5.4(p.100)。
- ch03b 18 条：例 3.3.7(p.180)、命题 3.4.1(p.182)、命题 3.4.2(p.183)、定义 3.5.1(p.183)、命题 3.5.2(p.183)、例 3.5.3(p.183)、定义 3.5.4(p.184)、命题 3.5.5(p.184)、定义 3.5.6(p.186)、定理 3.5.7(p.186)、定理 3.5.8(p.188)、定理 3.5.9(p.188)、定理 3.5.10(p.188)、定义 3.6.1(p.189)、例 3.6.2(p.189)、命题 3.6.3(p.190)、命题 3.6.4(p.190)、例 3.6.5(p.191)。

英文侧在 ch03b 区间还出现「3.3.5」，那是定理 3.3.6 证明中的交叉引用（陈述本体在 ch03a），不属本块。

## 三、公式核对

- **ch01a p.25 全文逐式核**：正则交换关系、$\hat p$ 在周期边界条件下的伴随性三步、$\psi=e^{2\pi ix}$ 的本征态与不确定性反例，逐符号与原页一致。仅一处保真度修正：原文 $\frac14\left\|\langle[\hat x,\hat p]\rangle_\psi\right\|^2$ 用了双竖线范数记号，原稿写成 `\abs{}`，已改 `\norm{}`。
- **ch01a p.24–25**：$[\hat A,\hat B]$ 公共本征向量推导、定义 1.4.1、命题 1.4.2 与证明（$\tilde A,\tilde B$ 平移技巧、Cauchy–Schwarz）与原文一致（读 draft 页 11–12 与 p.22–23 页图对照）。
- **ch02a p.85 全文逐式核**：自由粒子核的高斯积分、$K_0$ 显式式、注 2.2.1 的虚时间与热核算子、2.2.2 无穷小时间四步展开，逐符号一致。
- **ch02a p.93 全文逐式核**：谐振子 $\hat H$、路径积分核、作用量、经典解 $x_{cl}$、作用量展开四行、椭圆算子 $A=-\frac{\rd^2}{\rd t^2}-\omega^2$、高斯积分结果 $(\frac{m}{\pi\ii\hbar})^{1/2}(\det A)^{-1/2}$，逐符号一致。
- **ch03b**：本块由我本人逐页以 150dpi 页图核对译出；本次复核抽查 p.181（Moyal 乘积六步推导）、p.187（博雷尔引理估计）、p.192（拉盖尔多项式展开），与页图一致。
- 三块内无 `equation` 环境、无自动编号；`(*)` 标签、`cases`、`align*` 用法符合手册。

## 四、图

- **ch01a 3 幅 TikZ**（p.20 双缝装置、p.20 经典图像、p.21 量子图像）逐幅与原页图对照。前两幅几何、标注位置一致。第三幅原文画的是两孔向右发出的红色同心波前弧线，原稿画成两条从孔到屏的直线箭头，波前语义丢失；已改为以两孔为圆心、半径 0.5/0.9/1.3/1.7、开角 ±48° 的红色圆弧，保留屏上的蓝色干涉图样与 $P$ 标注。
- **ch02a 4 幅 TikZ**：p.98 复围道（$x$/$y$ 轴、过原点倾角 $\theta$ 的蓝线 $C_\theta$、两个箭头、$\theta$ 弧、「$\theta>0$ 且很小」）与原图一致；p.106 Stokes 射线（竖直双箭头＋「$\lambda$ 平面」方框）一致；p.107 anti-Stokes 分区（「$\lambda$ 平面」方框、水平双箭头、「反斯托克斯射线」、上下两个 $\int_{C_\pm^\lambda}$ 占主导）一致；p.107 跨线小图（「$\lambda$ 平面」方框、虚轴、跨轴的弯曲箭头）一致。
- **ch02a 16 幅裁图**：抽查 `fig_p107_b.png`（$z$ 平面双曲线支与 $p_\pm$）、`fig_p107_c.png`（跨 Stokes 射线的三联小图＋大箭头），裁切干净无残字，图内文字保留原样并配 `\fignote{}`。
- **ch03b 1 幅裁图 `fig_p187_a.png`**：$\chi(t)$ 与 $2/t$ 曲线图，完整清晰。

## 五、本次改动清单（6 处）

1. `src/chunks/ch02a.tex`：`\section{渐近方法}` 前页标 `p.96` → `p.95`（硬错误）。
2. `src/chunks/ch01a.tex`：`Hugh Everett` → `休·埃弗里特（Hugh Everett）`（lead 指派）。
3. `src/chunks/ch01a.tex`：`David Mermin` → `戴维·默明（David Mermin）`（lead 指派）。
4. `src/chunks/ch01a.tex`：$\frac14\abs{\langle[\hat x,\hat p]\rangle_\psi}^2$ → `\norm{}`（原文双竖线）。
5. `src/chunks/ch01a.tex`：p.21 量子图像 TikZ 的直线箭头改为两孔波前弧线（几何保真）。
6. `src/chunks/ch03b.tex`：在 `\section{复合公式}` 之前补 §3.3 的 `\takeaway{}`（76 汉字：振荡积分定义、无驻点时 $O(\hbar^\infty)$、莫尔斯引理化二次型、驻定相位首项的 $|\det\partial^2\varphi|^{-1/2}$ 与 $e^{\frac i4\pi\sgn\partial^2\varphi}$ 相位、后文连接公式与渐近展开的来源）。第 3 章至此 6 节 6 条齐。

另：`reports/ch03b.md` 与 `work/term_requests_ch03b.md` 中「Kohn–Nirenberg 量子化（保留拉丁）」已按 tr05 全书专名统一改为「科恩–尼伦伯格量子化（Kohn–Nirenberg）」，与 `ch03a.tex:409`、`ch03b.tex:211/213` 一致。

## 六、术语

- 禁用译法 grep（算符/特征值/特征向量/汉密尔顿/赫米特/薛定锷/几率…）三块零命中。
- Hessian：全书统一「黑塞（黑塞矩阵）」，`ch02a.tex:1001` 已是「黑塞矩阵」，三块内无「海森矩阵」（`海森堡` 是 Heisenberg，正常）。`ch03a.tex:987` 的 `\operatorname{Hess}\varphi` 属 `\operatorname{}` 内数学算子名，按 tr05 口径保留拉丁。
- 星号：`ch03b` 统一 `\star`（Moyal）与 `\star_{KN}`（标准量子化）；ch01a、ch02a 无 `\ast`/`\star`，不存在混用。
- 专名：Weyl→外尔、Wigner→维格纳、Borel→博雷尔、Laguerre→拉盖尔、Calderón–Vaillancourt→卡尔德隆–韦扬库尔、Hörmander→赫尔曼德，均已成中文；`Zworski 的书`、`Coleman [10]` 类文献指称按 tr05 口径保留。
- 未决术语：无新增，见 `work/term_requests_review_ch0102.md`（仅登记黑塞、科恩–尼伦伯格的定稿）。

## 七、自检

```
ch01a: LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch01a.pdf (20 页)
ch02a: LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch02a.pdf (30 页)
ch03b: LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch03b.pdf (16 页)
```

```
OK   ch01a  字符 23400  节 5 小节 16 陈述 13 公式 124 图 1(TikZ 3) 批注 0
OK   ch02a  字符 35841  节 5 小节 15 陈述  7 公式 201 图16(TikZ 4) 批注 0
     · \section=5 但 \takeaway=4（§2.5 跨块，节末 takeaway 由 ch02b 补写，属预期）
OK   ch03b  字符 25308  节 3 小节  7 陈述 18 公式  77 图 1(TikZ 0) 批注 0
     · \section=3 但 \takeaway=4（§3.3 跨块，takeaway 补在本块，§3.3 属 ch03a 起、ch03b 止，属预期）
合计：问题 0 条，提示 2 条
```

两条提示均为跨块 takeaway 归属，非缺陷：ch02a 的 §2.5 takeaway 确已在 `ch02b.tex:20` 补写；ch03b 的 §3.3 takeaway 经本次补写后第 3 章 6 节 6 条齐。

## 八、存疑（已由 lead 裁定，2026-11-07）

1. `ch01b` 起始处的块界注释称 ch01a 末句为「该态 $\psi$ 的能量。」，与 ch01a 末页（p.29）实际收束一致，未发现重复或截断。
2. `ch01a` p.20 双缝装置图的墙标注原译作「墙（双孔）」，比原文 "wall" 多出解释性说明。**lead 已改回「墙」**（双孔由图形本身体现），本次复核后重编验证 `LOG` 五项全 0。
3. 原书 p.190 "a substitute for the the nonexistent joint probability distribution" 的 "the" 重复属原书笔误，译文按单次处理、不加 `% [Tutor Note]`。**lead 裁定同意**：纯笔误（拼写重复、缺冠词）不影响数学者一律静默处理，不写批注。
4. 原书 p.190 命题 3.6.4 的界 $-\frac{1}{(\pi\hbar)^n}\le\mathrm{Wig}_\psi\le\frac{1}{(\pi\hbar)^n}$ 与第 2 章高斯积分约定一致，未改。
5. `ch02a` 的 §2.5 标题在 p.95 末（原书排版如此），故 `\section{渐近方法}` 落在 p.95 页段内、正文主体在 p.96 之后。**lead 裁定不补第二个 p.96 页标**：页标只标「这段起于原书哪页」，一处内容一个标，重复标会造成「缺页」误判。

## 九、可复用工具（留给后续复核）

本次用的逐页对照已做成模板，后续块不必重写：

- `work\review\_mk_table.py`：`python work\review\_mk_table.py <块名…>` 生成 `work\review\pagecheck_<块>.md`，四栏表（页 | 英文页首句 | 译文段首句 | 判定）＋缺口/重复自检行；跳过注释、纯公式段与绘图行，小节标题显示为「〔节 X〕」。
- `work\review\逐页核对表_模板.md`：原则、判定取值（✓ / △ 跨页段落 / ✗ 错号 / 图 / 重 / 缺）、顺手要看的四件事、收口标准。
- `work\review\_stmts.py`：陈述编号/类型/所在页三方比对。
- 本报告第一、二节的结论均由这三个脚本产出，判定列由人眼填。
