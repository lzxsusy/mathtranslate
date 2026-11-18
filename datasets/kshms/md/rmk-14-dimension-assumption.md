# 假设 $\dim Y>1$：一维情形另行处理

`kshms/remark/rmk-14-dimension-assumption` · track C（Fukaya 与退化） · 原文 注 14

**问题**　为什么后文要假设 $\dim Y>1$，一维情形会带来什么不同？

**摘要**　后文假设 $\dim Y>1$；$\dim Y=1$ 时构造略有不同但更简单，且 $\mathcal{F}^\eta_{\mathrm{unram}}(X^\vee)$ 不依赖 $\eta$，故不能把一般维数结论直接照搬。

**别名**　Remark 14；assumption $\dim Y>1$；一维底流形的例外

## 陈述

以下我们假设 $\dim Y>1$。$\dim Y=1$ 的情形略有不同，但也简单得多（例如见 [P1]）。特别地，在此情形 $\mathcal{F}^\eta_{\mathrm{unram}}(X^\vee)$ 不依赖于 $\eta$。

## 这条注在全文中的作用

这是一条范围声明：它把一般维数与曲线情形分开，避免后文关于横截性与极限的论证在一维失去一般性。$\dim Y=1$ 时整族 $\mathcal{F}^\eta_{\mathrm{unram}}$ 在 $\eta$ 方向不变，说明一维不能当作高维结论的简单特例。

## 易错点

- $\dim Y=1$ 不是被排除，而是被声明为「不同但更简单」；引用定理时要注意是否隐含 $\dim Y>1$。
- 「$\mathcal{F}^\eta_{\mathrm{unram}}(X^\vee)$ 不依赖 $\eta$」是一维情形的特殊结论，不能反推一般维数也如此。
- 这里的 $Y$ 是底流形，$\dim Y>1$ 与纤维维数无关；不要和 $X^\vee$ 的维数混淆。

## 相关卡

- `kshms/concept/prp-05-fukaya-oh-limit-equivalence`
- `kshms/concept/dfn-16-fukaya-objects`
- `kshms/remark/rmk-13-maslov-equals-morse`

## 出处

- Kontsevich–Soibelman, Homological mirror symmetry and torus fibrations（中译注本 SY01-25） §5.2（原文 p.33）；锚点 `源码/chunks/ch05.tex:151-153（注 14）`

> 原文 p33 §5.2；中译注本 ch05.tex:151-153。
