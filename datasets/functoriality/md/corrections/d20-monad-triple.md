# 原文 p.61：单子三元组 $(T,\mu,\nu)$ 应为 $(T,\mu,\eta)$

> `functoriality/correction/d20-monad-triple` ｜ 原书 p.61 ｜ draft

**一句话**：伴随诱导的单子被写成 $(T,\mu,\nu)$，但单子的单位是 $\eta$。

**自测**：单子是 $(T,\mu,\eta)$，这里为什么写成 $\nu$？

## 初版

```
its associated monad is exactly $(T,\mu,\nu)$
```

## 改后

```
$(T,\mu,\eta)$
```

## 为什么改

单子是三元组 $(T,\mu,\eta)$：$\mu$ 为乘法、$\eta$ 为单位；同段式 (134) 与 $\mod T$ 的定义均写 $\eta$。

## 补注

中译本保留原文，加译注说明应为 $(T,\mu,\eta)$。

## 易错点

- $\nu$ 在本节没有定义，不要当成第三种结构映射。
- 单子只有乘法 $\mu$ 与单位 $\eta$ 两个结构映射。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§5.7.1，p.61–61（原书 p.61）

关联：`functoriality/concept/monad`、`functoriality/concept/eilenberg-moore`

来源说明：英文底本 applications.tex §5.7.1（A 级）；对照同段式 (134) 与紧随的 $\mod T$ 定义。
