# ch16.tex 审读问题（对照英文原 PDF p76–p83）

## ch16.tex:41（原 PDF p77）

- 原文：Assume H1 → H2 has unipotent kernel.
- 原译：假设 $H_1\to H_2$ 是核为幺幂群的满同态。
- 类型：增译
- 改法：假设 $H_1\to H_2$ 的核为幺幂群。
- 理由：原文只假设核幺幂，没有要求满射；补“满”加强了引理的前提（引理对非满射的同态也成立），会让读者误以为满射是必要条件。

## ch16.tex:197（原 PDF p82）

- 原文：Thus in types A, B, C, D the finite étale cover is already forced to be trivial.
- 原译：因此，在 $A$、$B$、$C$、$D$ 型中，该有限 étale 覆盖已被迫为平凡的一重覆盖。
- 类型：增译
- 改法：因此，在 $A$、$B$、$C$、$D$ 型中，该有限 étale 覆盖已被迫为平凡覆盖。
- 理由：原文的“trivial”指覆盖平凡，即代数常值 $\mathcal A_{G,\mathrm{irr}}\simeq\cO^{\oplus n}$，并未断言 $n=1$；加“一重”等于提前使用 16.10 才证出的结论。

## ch16.tex:212（原 PDF p83）

- 原文：The Whittaker chart used in the calculation is the open stratum in the usual Drinfeld compactification.
- 原译：计算中所用的 Whittaker 图册，是通常的 Drinfeld 紧化中的开层。
- 类型：术语
- 改法：计算中所用的 Whittaker 图卡，是通常的 Drinfeld 紧化中的开层。
- 理由：“chart”是单个图卡；本书“图册”专指叠的图册（见 ch02.tex:38、ch04.tex:40、ch11.tex:19），用在这里会把一个开子叠说成覆盖，与“是……开层”自相矛盾。

## ch16.tex:219（原 PDF p83）

- 原文：The object Wi restricts to the clean exponential object χ^!_glob E on this chart.
- 原译：对象 $W_i$ 在这一图册上限制为洁净指数对象 $\chi_{\mathrm{glob}}^!\mathcal E$。
- 类型：术语
- 改法：对象 $W_i$ 在这一图卡上限制为洁净指数对象 $\chi_{\mathrm{glob}}^!\mathcal E$。
- 理由：与 212 行是同一个 chart，指计算所用的那一个图卡，不是图册。
