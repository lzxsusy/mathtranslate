# 「对 (L,α) 决定」把决定者与被决定者说反

- **id**：`gw06/correction/determines-reversed`
- **类型**：correction
- **位置**：§3.5
- **问题**：「对 $X$ 决定 $Y$」为什么在数学句子里是主客颠倒？

> 英文 “$(\mathbb L_1,\alpha_1)$ determines a parabolic subgroup” 是前者决定后者，译成「对……决定」后主客颠倒。

## 位置

§3.5，s03b-parabolic.tex:411（原文 ramified.tex:636，PDF 第 62 页）

## 原文片段

```latex
对 $(\mathbb{L}_1,\alpha_1)$ 决定一个抛物子群 $\EUP_1$，对 $(\mathbb{L}_2,\alpha_2)$ 决定一个包含 $\EUP_1$ 的抛物子群 $\EUP_2$
```

## 改为

```latex
由 $(\mathbb{L}_1,\alpha_1)$ 决定一个抛物子群 $\EUP_1$，由 $(\mathbb{L}_2,\alpha_2)$ 决定一个包含 $\EUP_1$ 的抛物子群 $\EUP_2$
```

## 依据

「对……决定」在汉语里读作「针对……（我们）决定」，决定者成了隐含的「我们」，而数学内容恰恰是参数对决定抛物子群。上一段同一构造写作「由 $\alpha$ 决定的博雷尔子群」，体例也不一致。这不是风格问题：极限 $\alpha_1\to\alpha_2$ 的纤维化结构依赖于「$\EUP_1\subset\EUP_2$ 由参数对决定」这一方向，主客一颠倒，嵌套关系就无从谈起。

## 说明

两处均改为「由……决定」；未动 $\EUP_1,\EUP_2$ 与下标。

## 批注

### 含糊点拨：这层嵌套从哪来

给定 $\alpha$，中心化子 $\mathbb{L}=\{g:g\alpha g^{-1}=\alpha\}$ 是列维子群，再由 $\alpha$ 的正性挑出抛物子群 $\EUP\supset\mathbb{L}$。当 $\alpha_2$ 趋于$\alpha_1$ 所在的壁时，$\mathbb{L}_1\subset\mathbb{L}_2$，于是 $\EUP_1\subset\EUP_2$，两组抛物结构之间出现纤维化 $\M_{\mathbb{L}_2}\to\M_{\mathbb{L}_1}$。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 §3.5；印刷页 [50] / PDF 页 [51]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03b-parabolic.tex:409-413`
- 该句位于§3.5（小节的起始印刷页为第 50 页，PDF 第 51 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
