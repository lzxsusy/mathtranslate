# STYLE_GUIDE · SY02-28

## 1. 文体

- 学术书面语，句子短于原文；英文长句拆成两到三个中文句，不逐词硬搬。
- 第一人称复数照译「我们」；作者自指的「we」不改成「本文」。
- 原文的 italics 强调在译文中用 \emph；定理名、猜想名不加引号，首字母大写照原文。
- 中文标点：句号「。」、逗号「，」、顿号「、」、引号「」；数学模式内用英文标点。
- 人名首次出现给中文＋英文，如「蓝凯文（K.-W. Lan）」；此后只用中文。已有通用译名者（Fontaine、Deligne、Scholze）不再附英文。
- 破折号用「——」，不用 `--`（LaTeX 中写 ---）。

## 2. 术语表（本工程强制）

| 英文 | 中文 | 备注 |
| --- | --- | --- |
| p-adic local system | $p$ 进局部系统 | 不写「p-进」 |
| étale | 平展 | 不写「埃塔勒」 |
| étale site | 平展 site | 首次出现可注「平展拓扑」 |
| rigid analytic variety | 刚性解析簇 | |
| rigid analytic space | 刚性解析空间 | |
| affinoid | 仿射体 | 首次出现附英文 |
| perfectoid field | 完美胚域 | |
| tilt | 倾斜 | $K^\flat$ 读作「$K$ 的倾斜」 |
| adic space | adic 空间 | 保留 adic |
| Shimura variety / datum | 志村簇 / 志村数据 | |
| reflex field | 反射域 | |
| eigenvariety | 特征簇 | |
| special point | 特殊点 | |
| canonical model | 典范模型 | |
| geometric (Fontaine–Mazur) | 几何的 | 首次出现引原文 |
| de Rham | de Rham | 不译 |
| crystalline | 晶体 | 「晶体表示」 |
| semi-stable | 半稳定 | |
| potentially semi-stable | 潜半稳定 | |
| Hodge–Tate weights | Hodge–Tate 权 | |
| period ring / sheaf | 周期环 / 周期层 | |
| de Rham period sheaf | de Rham 周期层 | |
| pro-étale site | pro-平展 site | |
| toric chart | 环面坐标卡 | |
| standard étale | 标准平展 | |
| generic point | 泛点 | |
| residue field | 剩余域 | |
| good reduction | 好归约 | |
| anisotropic | 各向异性 | |
| split | 分裂 | |
| subquotient | 子商 | |
| Tate twist | Tate 扭 | |
| higher direct image | 高阶顺像 | |
| proper smooth morphism | 紧合光滑态射 | |
| Griffiths transversality | Griffiths 横截性 | |
| integrable connection | 可积联络 | |
| nilpotent Higgs bundle | 幂零 Higgs 丛 | |
| filtered module | 滤过模 | |
| regular singularity | 正则奇点 | |
| logarithmic connection | 对数联络 | |
| perverse sheaf | 反常层 | |
| D-module | $D$-模 | |
| Betti | Betti | 不译 |
| monodromy | 单值群 / 单值性 | 群用「单值群」 |
| geometric connected | 几何连通 | |
| closed point | 闭点 | |
| generic fiber | 泛纤维 | |
| base change | 基变换 | |
| pullback / pushforward | 拉回 / 顺像 | |
| tensor functor | 张量函子 | |
| semi-linear action | 半线性作用 | |
| filtration | 滤过 | |
| associated graded | 分次 | |
| ingredient | 构件 / 环节 | 不写英文 |

## 3. 编号与引用

- 定理 `thm`、命题 `prop`、引理 `lem`、推论 `cor`：均 `[section]`，编号形如 2.1。
- 注 `rmk`：独立 `[section]` 计数，编号形如 1.1；与定理编号并行，不要合并。
- 猜想：原文无编号者用 `conj*`；若后文出现带号猜想，再建 `conj`。
- 公式：`\numberwithin{equation}{section}`，编号 (2.1)；行内公式尽量不编号。
- 引用：`\cite{Sch2}`、`\cite[§8.2]{Sch2}`；多键 `\cite{AG,AGT}`。参考文献键沿用原文（AG、AGT、Be、BC、BM、Br2、DM、Fa、He、Ki、KL1、KL2、Mi1、Sch1、Sch2、Sim 等）。
- 交叉引用：`\ref{thm:1.1}`、`\eqref{eq:...}`；label 用「类型:原文编号」，如 `thm:1.3`、`rmk:1.5`、`sec:intro`。

## 4. 数学记号

- $\Qp,\Zp,\Q_\ell,\Z_\ell$ 用 `\Qp`、`\Zp`、`\Ql`、`\Zl`；不要写 `\mathbb{Q}_p`。
- $\BdR$、$\BdRp$、$\OX$、$\OXB$、$\Xk$ 用宏；$\mathcal X$ 专指环化空间。
- 茎：$\bar L_x$（`\bar{L}_x`）；几何点：$\bar x$；完备化代数闭包：$\khb$（`\khb`）。
- $\Gal(\bar k/k)$ 用 `\Gal`；$\Spa$、$\Sh$、$\gr$、$\Fil$ 用宏。
- 交换图暂不需要；若后文出现，用 tikz-cd，节点不留空格。
- 公式中的中文只在 `\text{}` 内出现；`\text{}` 内不写数学。

## 5. 译注

- 标记：`\zy{...}`，独立脚注序列「译 1、译 2」。
- 只写三类：(a) 易错预警；(b) 原文表述存疑（必须写「原文作……，此处存疑，待核」）；(c) 必要的背景提示（须给依据，无依据则写明「译者按（上下文推断，无外部依据）」）。
- 不写读后感、不写与原文无关的扩展。

## 6. 交付前检查

1. `xelatex` 三遍无 `^!`；2. `grep -c "??"` 为 0；3. 无 `Overfull \hbox` 超过 5pt；4. 定理/注编号与原文逐条对齐；5. `refs.tex` 键与正文 `\cite` 一一对应；6. BRIEF 分块表状态已更新。
