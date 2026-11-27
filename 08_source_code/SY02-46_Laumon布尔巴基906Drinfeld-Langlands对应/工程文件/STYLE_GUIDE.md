# STYLE_GUIDE · SY02-46

本文件管「什么样算好中文」；`work/TASK-translator.md` 管流程与自检。两者冲突时以本文件
的数学与文风条款为准，流程条款以 TASK 为准。

## 1. 语气与句法

- 学术书面语。不写「那么」「所以说」「可以看到」，写「因此」「所以」「可见」。
- **一句一个判断，≤60–70 汉字**。长句拆在逻辑接点：条件 / 主句 / 结论 / 附注各成一句。
- 主语尽量显式。原文 `This shows that…` 译「这说明……」，不写「由此可知……」。
- 禁止翻译腔：
  - ✗ 被……所…… ✓ 由……给出 / 记作
  - ✗ 对……进行讨论 ✓ 讨论……
  - ✗ 具有……的性质 ✓ 满足…… / 是……
  - ✗ 通过……的方式 ✓ 用…… / 以……
  - ✗ 在……的情况下 ✓ 若…… / 当……
- 不添加原文没有的评价。`a key insight` = 「一个关键想法」，不是「非常深刻的想法」。

## 2. 逻辑连接词对照（强制）

| 法文 | 译 | 法文 | 译 |
| --- | --- | --- | --- |
| donc | 因此 | en particulier | 特别地 |
| ainsi | 从而 / 这样 | inversement | 反之 |
| par conséquent | 所以 | de même | 同样地 |
| il en résulte que | 于是 | en effet | 事实上 |
| de plus | 此外 | notons que | 注意 |
| cependant | 然而 | rappelons que | 回忆 |
| néanmoins | 尽管如此 | plus précisément | 更确切地说 |
| d’autre part | 另一方面 | en fait | 实际上 |
| or | 然而 / 而 | c’est-à-dire | 也就是说 |
| d’où | 由此 | autrement dit | 换言之 |
| bien entendu | 当然 | dorénavant | 此后 |
| soit | 设 | on a | 有 |

原文没有连接词，译文不得添加。`et` 并列用「，」或「并且」，不升格为「因此」。

## 3. 排版

- 中文与拉丁字母/数字之间**一个半角空格**：`秩 n 向量丛`、`第 5 节`、`G-丛`（连字符紧贴）、
  `2002 年`。
- 全角标点：，。；：？！（）「」；公式内的逗号与括号用半角。
- 引号用「」，不用 “ ”；书名用《》，论文名用「」或斜体原文。
- 数学模式里的中文用 `\text{...}`。
- 破折号用 `——`。
- 列表用 `enumerate`，编号自动。

## 4. 数学写法

- 范畴、叠、函子名正体：$\Fib_n(X)$、$\Coh^d_0(X)$、$\Mod^d_i(X)$、$\Perv(S)$、$\Four_{V/S}$、
  $\Rad_{P(V)/S}$、$\Hck_n(X)$、$\Aut_E$、$\operatorname{Ext}^1$。
- 层与函子：$f_!$、$f_*$、$f^!$、$f^*$；不写 $f!$。
- 对偶：$V^\vee$（不用 $V^*$，原文用 $\vee$；$V^*$ 只用于对偶复形 $D$ 之外的场合时须核对原文）。
- 域与空间：$\C$、$\Ql$、$\A^1$、$\Gm$、$\Pv(V)$、$B(\Gm)$、$X^{(d)}$、$X^{(d)}_{\rss}$。
- 旗：$L_\bullet = (0 = L_0 \subset L_1 \subset \cdots \subset L_n = L)$；$s_\bullet$、$s_j$。
- 张量：$\otimes$、$\boxtimes$（外张量积）；直和 $\oplus$；幂 $\Sym^{d_x}$。
- 引用他人结果：`（Deligne，[Il] 推论 2.10）`，方括号编号照原文。

## 5. 固定译名（节选；全表见 glossary.tsv）

| 法文 | 中文 |
| --- | --- |
| faisceau pervers | 反常层 |
| système local | 局部系统 |
| champ algébrique | 代数叠 |
| champ quotient | 商叠 |
| gerbe | gerbe（不译） |
| D-Module holonome | holonomic $D$-模（holonomic 不译） |
| perversité intermédiaire | 中间反常 |
| prolongement intermédiaire | 中间延拓 |
| prolongement par zéro | 零延拓 |
| faisceau gratte-ciel | 摩天层 |
| modification inférieure | 下修改 |
| transformation de Fourier homogène | 齐次 Fourier 变换 |
| transformation de Radon | Radon 变换 |
| fonction caractéristique d’Euler-Poincaré | Euler–Poincaré 示性函数 |
| faisceau pervers propre | proper 反常层（proper 不译） |
| morphisme propre | 紧合态射 |
| théorème d’annulation | 消没定理 |
| descente | 下降 |
| rang générique | 一般秩 |

## 6. 译注写法

`\yizhu{内容}{等级（出处）}`，只三类，每条都要能追溯到来源：

```latex
\yizhu{原文「propre」在此是 (0.2) 定义的层论术语，与态射的「紧合」无关。}{A（原文 (0.2)；参 BBD Astérisque 100）}
```

- 术语背景：给 A/B 级来源；
- 原文省略：说明省了什么、依据在哪；
- 原文笔误：给页码 + 判断依据；
- 纯推断写「译者按（上下文推断，无外部依据）」，不许伪装成 A/B 级。
- 每节 ≤6 条。译注不是炫技，是补不可省略的信息。

## 7. 反面清单（见到即改）

- 「由此可得」「由上可知」——指代不明，改成具体的「由定理 2.2，……」。
- 「众所周知」——原文没有就别加。
- 「我们可以看到」——删。
- 「进行了深入的研究」——改为「研究了」。
- 「这是一个非常重要的问题」——原文没有 `important` 就删。
- 一段里三个以上「因此」——必有两个该换成「从而」「所以」「于是」。
