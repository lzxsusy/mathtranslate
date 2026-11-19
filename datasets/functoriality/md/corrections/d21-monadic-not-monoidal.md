# 原文 p.64：monoidal 应为 monadic

> `functoriality/correction/d21-monadic-not-monoidal` ｜ 原书 p.64 ｜ draft

**一句话**：把 Barr–Beck 的结论说成伴随是 monoidal，但下文结论是单子性（monadic）。

**自测**：为什么这里写 monoidal 推不出后面的 Eilenberg–Moore 等价？

## 初版

```
the following adjunction is monoidal
```

## 改后

```
the following adjunction is monadic
```

## 为什么改

紧随的结论是该伴随诱导出 Eilenberg–Moore 范畴与 $\Fuk M$ 的等价，即单子性；monoidal 只指张量结构，推不出此结论。

## 补注

中译本保留原文 monoidal，加译注说明应为 monadic。

## 易错点

- monoidal 指张量结构，与单子性判据无关。
- 紧接的结论是 $\Fuk M$ 与 $\mod T$ 等价，只有 monadic 才蕴含它。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§5.7.2，p.64–64（原书 p.64）

关联：`functoriality/concept/barr-beck`、`functoriality/concept/monad`

来源说明：英文底本 applications.tex §5.7.2（A 级）；对照紧随的等价式与 Mac Lane VI.7 单子性定理。
