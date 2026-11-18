# 只考虑虚维数 $\le 0$ 的模空间

`kshms/remark/rmk-16-virtual-dimension` · track D（Morse 机器） · 原文 注 16

**问题**　Morse $A_\infty$-范畴的复合为什么只对虚维数 $\le 0$ 的模空间计数？

**摘要**　与 Fukaya 范畴一样，Morse 侧只考虑虚维数不超过零的模空间 $\mathcal{M}(T;f_0,\dots,f_k;x_0,\dots,x_k)$；维数严格为负时 $T$-横截条件迫使它为空。

**别名**　Remark 16；virtual dimension $\le 0$；负维模空间为空

## 陈述

与 Fukaya 范畴的情形一样，这里只考虑（虚）维数小于或等于零的空间 $\mathcal{M}(T;f_0,\dots,f_k;x_0,\dots,x_k)$。在维数严格为负的情形，我们的条件意味着该模空间为空。

## 这条注在全文中的作用

它把复合 $m_k$ 的求和限制在零维模空间上：只有零维才计点，负维自动为空，正维不进入 $m_k$ 的计数。这是 §6 定义 20 的 $m_k$ 公式只出现 $\deg\mathcal{M}$ 的前提。

## 易错点

- 「虚维数」是按指标算出的预期维数，不是模空间的实际维数；实际维数可能更大。
- 负维时为空是 $T$-横截条件的结果，不是定义里直接规定的。
- 原文此注还有第二段（第二纲集上 $T$-横截序列的存在性），中译本把它移出注环境作正文（ch06.tex:140-142）；读「注 16」时不要以为只此一段。

## 相关卡

- `kshms/concept/dfn-18-t-transversal`
- `kshms/concept/dfn-20-morse-composition`
- `kshms/remark/rmk-17-perturbation-general`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §6.2（原文 p.39）；锚点 `源码/chunks/ch06.tex:132-138（注 16）`

> 原文 p39 §6.2；中译注本 ch06.tex:132-138。原文此注含两段，中译本把第二段（第二纲集上 $T$-横截序列的存在性）移出注环境作正文（ch06.tex:140-142），注的边界与原文不同。
