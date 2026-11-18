# 译文修订 section-17-k.tex:41

> `seidel/correction/a10-section-17-k-41` ｜ 原书 p.265 ｜ draft

**一句话**：初版此处误译：原书 p265 方框内第二式为 $-\epsilon_{\mathcal A}(\kappa(\epsilon_{\mathcal A}(c_0)))+\kappa(c_0)=0$（已裁图放大核对）

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
-\eps_{\A}(k(\eps_{\A}(c_0)))+k(c_0)=0
```

## 改后

```
-\eps_{\A}(\kappa(\eps_{\A}(c_0)))+\kappa(c_0)=0
```

## 为什么改

原书 p265 方框内第二式为 $-\epsilon_{\mathcal A}(\kappa(\epsilon_{\mathcal A}(c_0)))+\kappa(c_0)=0$（已裁图放大核对）。同句前文刚声明“得到 $(\gamma,\kappa)$”，同一式前项亦作 $\kappa$，此处误作 $k$；$k$ 是原映射 $CF^*(L_0^\#,L_1^\#)\to CF^*(L_0^\#,L_2^\#)[-1]$，$\kappa$ 是它的二阶同伦修正，混用会与 $\stref{引理}{5.3}$(ii) 的 $(\gamma,\kappa)$ 记号冲突。

## 补注

见分章报告 A10；修订总表第 27 条。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.265–265（原书 p.265）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据 A10 分章报告与修订总表；原文页码由 reason 或 page_map 推出。
