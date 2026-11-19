# 原文 p.31：同伦公式的三处书写问题

> `functoriality/correction/d11-homotopy-equations` ｜ 原书 p.31 ｜ draft

**一句话**：同伦定义式中张量积链缺 $\otimes$、式 (71) 换行处重复 $+$、下方两复合的顺序写错。

**自测**：式 (70)-(71) 与下方两处复合到底哪里写错了，怎样读才对？

## 初版

```
$\hom(X_{d-1},X_d)\otimes\cdots\hom(X_0,X_1)$；(71) 行末行首各一个 $+$；下方并列 $\Phi_{L_{12}}\circ\Phi_{L_{23}}$
```

## 改后

```
第二处 $\cdots$ 前补 $\otimes$；(71) 只保留一个 $+$；并列项应为 $\Phi_{L_{13}}$
```

## 为什么改

张量积链须逐个因子以 $\otimes$ 相连；(71) 的换行重复了加号；$\Phi_{L_{12}}\circ\Phi_{L_{23}}$ 在范畴上不可定义，应为 $\Phi_{L_{13}}$。

## 补注

中译本按原文照录，并在相应位置加两条译者按。

## 易错点

- 不要把式 (71) 换行处的两个 $+$ 读成两项之和，那是重复的加号。
- 复合顺序由所在范畴决定：$\Phi_{L_{12}}$ 与 $\Phi_{L_{23}}$ 只在一个方向可复合。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§3.6，p.31–31（原书 p.31）

关联：`functoriality/concept/phi-sharp`、`functoriality/deriv/mww-composition`

来源说明：英文底本 functors.tex §3.6（A 级）；对照同页 MWW 复合定理的陈述。
