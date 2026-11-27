# STYLE_GUIDE · SY02-45

本文件是本工程文风的唯一标准，与 `work/TASK-translator.md`（施工契约）配套：契约管流程与自检，本文件管「什么样算好中文」。

## 1. 语气与句法

- **学术书面语，不用口语连接**：不写「那么」「所以说」「可以看到」，写「因此」「所以」「可见」。
- **一句一个判断**，≤60–70 汉字。长句拆在逻辑接点：条件 / 主句 / 结论 / 附注各成一句。
- **主语尽量显式**：原文 `This shows that…` 译「这说明……」而非「由此可知……」——「由此」在中文里指向不明，是本工程的重点纠偏对象。
- **禁止翻译腔**：
  - ✗ 被……所…… ✓ 由……给出 / 记作
  - ✗ 对……进行讨论 ✓ 讨论……
  - ✗ 具有……的性质 ✓ 满足……/ 是……
  - ✗ 通过……的方式 ✓ 用……/ 以……
  - ✗ 在……的情况下 ✓ 若……/ 当……
- **不添加原文没有的评价**：✗「这个想法非常深刻」；✓ 照译 `a key insight`=「一个关键想法」。
- **术语首现**：中文 +（English）一次；之后只用中文。保留英文的术语（shtuka/oper/Gestalt/suave/prim）不括注中文，首现给一句斜体解释。

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

- 中文与拉丁字母/数字之间**一个半角空格**：`p 进数`、`G-丛`（连字符紧贴）、`第 5 节`、`2025 年`。
- 全角标点：，。；：？！（）「」；公式内的逗号与括号用半角。
- 引号用「」，不用 “ ”；书名用《》，论文名用「」或斜体原文。
- 数学模式里的中文用 `\text{...}`，不要直接写中文。
- 破折号用 `——`（两个 em dash），不用 `--`。
- 列表（原文 `1. 2. 3.`）用 `enumerate`，保持编号自动。

## 4. 数学写法

- 范畴名正体：$\Bun_G$、$\LocSys_{\Gd}$、$\IndCoh_{\Nilp}$、$\Perv$、$\Rep$、$\D_{\qc}$、$\Hck$、$\Gr$、$\Sht$。
- 群名斜体：$G$、$\Gd$、$T$、$U$、$B$、$\LG$；李代数为哥特体 $\gc$。
- 层与函子：$f_!$（下叹号）、$f_*$、$f^!$（上叹号）、$f^*$；不要写成 $f!$。
- 单位对象 $\mathbf 1$；对角 $\Delta$；张量 $\otimes$；直和 $\oplus$。
- 域：$\Ql$、$\Zl$、$\Fq$、$\Fp$、$\C$、$\R$、$\Gm$、$\A^1$。
- 无穷范畴记 $\mathcal D(X)$、$\PrL$；不写「无穷范畴」缩写 D∞。
- 引用他人定理：`（Gaitsgory–Raskin 2025a，定理 0.2.2）`，年份与编号之间用中文逗号。

## 5. 三类 setting 的固定译名（易串错）

| 原文 | 固定译名 | 备注 |
| --- | --- | --- |
| Betti setting | Betti 情形 | 保留 Betti |
| de Rham setting | de Rham 情形 | 保留 de Rham |
| étale setting | étale 情形 | 保留 étale |
| $\Ql$-sheaves | $\Ql$-层 | |
| nilpotent singular support | 幂零奇异支撑 | |
| Hecke-lisse | Hecke-lisse | 不译 |
| ind-prim / suave | ind-prim / suave | 不译 |
| Gestalt / Gestalten | Gestalt / Gestalten | 不译，首现释义「（一种把环与范畴逐层打包的几何对象）」 |
| transmutation | transmutation | 不译 |
| shtuka | shtuka | 不译；复 shtukas |
| oper | oper | 不译；复 opers |
| Weil 化 | Weil 化 | `Weil-ized` |
| 完美复形 | 完美复形 | perfect complex |
| 归纳凝聚层 | 归纳凝聚层 | ind-coherent |

## 6. 译注写法

`\yizhu{内容}{等级（出处）}`，只三类，每条都要能追溯到来源：

```latex
\yizhu{Bourbaki 报告体例常省略曲线 $X$ 的亏格假设；此处按上下文取 $g\ge 1$。}{B（上下文；参 AGKRV 2020b §1）}
```

- 术语背景：给 A/B 级来源（论文、nLab、Stacks Project）；
- 原文省略：说明省了什么、依据在哪；
- 原文笔误：给页码 + 判断依据；
- 纯推断写「译者按（上下文推断，无外部依据）」，不许伪装成 A/B 级。
- 每节 ≤6 条。译注不是炫技，是补不可省略的信息。

## 7. 反面清单（见到即改）

- 「由此可得」「由上可知」——指代不明，改成具体的「由定理 5.9，……」。
- 「众所周知」——原文没有就别加。
- 「我们可以看到」——删。
- 「进行了深入的研究」——改为「研究了」。
- 「这是一个非常重要的问题」——原文没有 `important` 就删。
- 一段里出现三个以上「因此」——必有两个该换成「从而」「所以」「于是」。
