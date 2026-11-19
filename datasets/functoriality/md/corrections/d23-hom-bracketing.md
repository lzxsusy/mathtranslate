# 原文 p.56：式 (120) 的括号位置

> `functoriality/correction/d23-hom-bracketing` ｜ 原书 p.56 ｜ draft

**一句话**：$H(\hom(\Phi(\overline Y))(\pt),\pt)$ 的括号把 $\Phi(\overline Y)$ 与 $(\pt)$ 割开，应读作先取值再取态射复形。

**自测**：式 (120) 里 $\hom$ 的第二个参数到底是 $(\pt)$ 还是别的？

## 初版

```
$H(\hom(\Phi(\ol Y))(\pt),\pt)$
```

## 改后

```
$H\bigl(\hom(\Phi(\ol Y)(\pt),\pt)\bigr)$
```

## 为什么改

按第 2 章约定 $\hom(X,Y)=\CF^*(X,Y)$ 取两个参数；应先取 $\Phi(\overline Y)$ 在 $\pt$ 上的值，再取它与 $\pt$ 的态射复形。

## 补注

中译本照录原文括号，加译注说明读法。

## 易错点

- $\hom(X,Y)=\CF^*(X,Y)$ 有两个参数，不能只喂一个。
- 不要把它读成 $\hom(\Phi(\overline Y))$ 的一元函数。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§5.3，p.56–56（原书 p.56）

关联：`functoriality/concept/floer-field-theory`、`functoriality/concept/floer-cohomology`

来源说明：英文底本 applications.tex 式 (120)（A 级）；对照第 2 章的 $\hom$ 约定与 §5.6 同类写法。
