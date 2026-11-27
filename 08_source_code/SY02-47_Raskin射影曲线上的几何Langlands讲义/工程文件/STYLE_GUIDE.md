# STYLE_GUIDE · SY02-47

本文件是本工程文风的唯一标准。`work/glossary.tsv` 管术语，本文件管「什么样算好中文」。

## 1. 语气与句法

- 学术书面语，不用口语连接：不写「那么」「所以说」「可以看到」，写「因此」「所以」「可见」。
- 一句一个判断，≤60–70 汉字。长句拆在逻辑接点：条件 / 主句 / 结论 / 附注各成一句。
- 主语尽量显式：原文 `This shows that…` 译「这说明……」而非「由此可知……」。
- 禁止翻译腔：
  - ✗ 被……所…… ✓ 由……给出 / 记作
  - ✗ 对……进行讨论 ✓ 讨论……
  - ✗ 具有……的性质 ✓ 满足…… / 是……
  - ✗ 通过……的方式 ✓ 用…… / 以……
  - ✗ 在……的情况下 ✓ 若…… / 当……
- 不添加原文没有的评价：✗「这个想法非常深刻」；✓ 照译 `a key insight` =「一个关键想法」。
- 讲义体保留第二人称与祈使语气：「回忆」「注意」「验证」「证明」。

## 2. 逻辑连接词对照（强制）

| 原文 | 译 | 原文 | 译 |
| --- | --- | --- | --- |
| Thus | 因此 | In particular | 特别地 |
| Hence | 从而 | Conversely | 反之 |
| Therefore | 所以 | Similarly / Likewise | 类似地 / 同样地 |
| Consequently | 于是 | Indeed | 事实上 |
| Moreover | 此外 | Note that | 注意 |
| However | 然而 | Recall that | 回忆 |
| Nevertheless | 尽管如此 | More precisely | 更确切地说 |
| On the other hand | 另一方面 | In fact | 实际上 |
| As a consequence | 作为推论 | For this reason | 出于这个原因 |

**原文没有连接词，译文不得添加。** 原文用 `and` 并列，中文用「，」或「并且」，不要升格成「因此」。

## 3. 排版

- 中文与拉丁字母/数字之间一个半角空格：`p 进数`、`G-丛`（连字符紧贴）、`第 5 节`、`2025 年`。
- 全角标点：，。；：？！（）「」；公式内的逗号与括号用半角。
- 引号用「」，不用 “ ”；书名用《》，论文名用「」或斜体原文。
- 数学模式里的中文用 `\text{...}`，不要直接写中文。
- 破折号用 `——`（两个 em dash），不用 `--`。
- 列表（原文 `1. 2. 3.`）用 `enumerate`，保持编号自动。
- 小节标题按 `\subsection{...}`；条目按环境（`definition`、`construction`、`remark`、`proposition`、`theorem`、`corollary`、`exercise`、`question`、`conjecture`）自动编号。

## 4. 数学写法

- 范畴名正体：$\Bun_G$、$\Jac$、$\Shv$、$\Rep$、$\Vect$、$\QCoh$、$\IndCoh$、$\Coh$、$\Perf$、$\DMod$、$\LS$。
- 群名斜体：$G$、$\Gd$、$T$、$B$、$N$、$P$、$\LG$；李代数为哥特体 $\gc$。
- 层与函子：$f_!$（下叹号）、$f_*$、$f^!$（上叹号）、$f^*$；不要写成 $f!$。
- 单位对象 $\one$；对角 $\Delta$；张量 $\otimes$；外张量 $\boxtimes$；直和 $\oplus$。
- 域：$\Ql$、$\Zl$、$\Fq$、$\Fp$、$\C$、$\R$、$\Gm$、$\A^1$。
- 系数域用 $\e$，单位对象用 $\one$，避免与群 $G$ 混淆。
- 引用他人定理：`（Gaitsgory–Raskin 2024，定理 6.1.3）`，年份与编号之间用中文逗号。

## 5. 三类 setting 的固定译名（易串错）

| 原文 | 固定译名 | 备注 |
| --- | --- | --- |
| Betti setting | Betti 情形 | 保留 Betti |
| de Rham setting | de Rham 情形 | 保留 de Rham |
| $\ell$-adic setting | $\ell$-进情形 | 保留 $\ell$-进 |
| perverse sheaf | 反常层 | **不用**「错致层」「永涵层」 |
| lisse sheaf | lisse 层 | 不译；与 locally constant 同义 |
| cuspidal | 尖点 | cuspidal sheaf = 尖点层 |
| Hecke eigensheaf | Hecke 特征层 | 不用「本征层」 |
| constant term | 常数项 | constant term functor = 常数项函子 |
| Whittaker coefficient | Whittaker 系数 | 保留 Whittaker |
| geometric Satake equivalence | 几何 Satake 等价 | 保留 Satake |
| affine Grassmannian | 仿射 Grassmann 簇 | 保留 Grassmann |
| ind-coherent sheaves | 归纳凝聚层 | 记号 $\IndCoh$ 保留 |
| perfect complex | 完美复形 | |
| quasicoherent | 拟凝聚 | |
| six-functor formalism | 六函子形式化 | |
| correspondence | 对应 | |
| constructible sheaf | 可构造层 | |
| local system | 局部系统 | |
| flat connection | 平坦联络 | |
| D-module | D-模 | |
| de Rham / Betti / étale | 不译 | |
| condensed | 凝聚态 | |
| shtuka / oper / leg | 不译 | 复数加 s |
| nilpotent singular support | 幂零奇异支撑 | |
| singular support | 奇异支撑 | |
| microlocal | 微局部 | |
| microstalk | 微茎 | |
| cotangent bundle | 余切丛 | |
| Borel subgroup | Borel 子群 | |
| maximal torus | 极大环面 | |
| reductive group | 约化群 | |
| split | 分裂 | |
| simply connected | 单连通 | |
| unipotent radical | 单幂根 | |
| parabolic | 抛物 | |
| Levi subgroup | Levi 子群 | |
| Langlands dual group | Langlands 对偶群 | |
| Eisenstein series | Eisenstein 级数 | |
| Kac–Moody localization | Kac–Moody 局部化 | |
| critical level | 临界水平 | |
| spherical vector | 球向量 | |
| automorphic form / representation | 自守形式 / 自守表示 | |
| function field | 函数域 | |
| generic rank | 通用秩 | |

## 6. 译注写法

`\yizhu{内容}{等级（出处）}`，只三类，每条都要能追溯到来源：

```latex
\yizhu{原文此处写 $\Gamma(X,L)\setminus 0$；当 $d>2g-2$ 时纤维的维数是 $d-g$，而不是 $d+1-g$，故应为射影化 $\mathbb P\Gamma(X,L)$。}{A（维数计算；B：Feng 讲义 \S2）}
```

- 术语背景：给 A/B 级来源（原始论文、经典教材、nLab、Stacks Project）；
- 原文省略：说明省了什么、依据在哪；
- 原文笔误：给页码 + 判断依据；
- 纯推断写「译者按（上下文推断，无外部依据）」，不许伪装成 A/B 级。
- 每节 ≤8 条。译注不是炫技，是补不可省略的信息。

## 7. 反面清单（见到即改）

- 「由此可得」「由上可知」——指代不明，改成具体的「由定理 5.9，……」。
- 「众所周知」——原文没有就别加。
- 「我们可以看到」——删。
- 「进行了深入的研究」——改为「研究了」。
- 「这是一个非常重要的问题」——原文没有 `important` 就删。
- 一段里出现三个以上「因此」——必有两个该换成「从而」「所以」「于是」。
- 「配対」「尖点性」以外的日文汉字混入——逐一改成简体中文。
