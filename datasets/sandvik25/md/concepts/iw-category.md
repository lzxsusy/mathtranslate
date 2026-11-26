# Iwahori–Whittaker 范畴 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$

> `sandvik25/concept/iw-category` · 轨道 C · Iwahori–Whittaker 侧 · 状态 dev

> **先自测**：IW 范畴是怎么从仿射旗簇的等变范畴里切出来的，它为什么自带一个右作用？

## 一句话

取 $I_u^+$（$I^+$ 的幂幺根）经 $\chi\colon I_u^+\to\mathbb G_a$ 的 Whittaker 扭曲，定义 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$；反常 $t$-结构限制其上，且 $\mathcal D^b_c(I\backslash\mathrm{Fl}_G)$ 从右侧卷积作用于它。

## 定义

令 $I_u^+$ 为 $I^+$ 的幂幺根（$LG\to G$ 下 $U^+$ 的原像）。固定 $U^+$ 的 pinning 得 $U^+/[U^+,U^+]\cong\prod\mathbb G_a$，定义 $\chi\colon I_u^+\to U^+\to U^+/[U^+,U^+]\cong\prod\mathbb G_a\xrightarrow{\text{sum}}\mathbb G_a$。IW 范畴定义为 $\mathrm{Fl}_G$ 上 $(I_u^+,\chi^*(\mathcal L_{\mathrm{AS}}))$-等变 $\mathbb Q_\ell$-层导出范畴，记 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$。

**记号**：$\mathcal P_{\mathrm{IW}}$ 为限制在其上的反常层子范畴；$\star_I$ 为右卷积 $\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)\times\mathcal D^b_c(I\backslash\mathrm{Fl}_G)\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$。

## 要点（为什么需要它）

1. 「右作用」而非双模结构：$\star_I$ 只从右边作用于 IW 侧，因为 $I$ 与 $I_u^+$ 的等变性只在右侧相容——这决定了 §5 里 $\mathrm{Av}^{\mathrm{IW}}$ 只能写成 $\Delta^{\mathrm{IW}}_0\star_I(-)$。
2. 反常 $t$-结构限制到 IW 范畴上不是自动的：正因为 Whittaker 层的消没性质，才有命题 4.3.1 的最高权结构。
3. 此范畴同时是 §4 的目标与 §5 的起点：$F^{\mathrm{IW}}$ 的终点就是它，而定理 5.0.1 说整个几何侧等价于它。
4. 讲义在这里换了设置（注 4.0.1）：从 Betti 换到 étale、$\mathbb Q_\ell$-层、$\ell\neq p$；此前所有讨论都有显然的 étale 类比。

## 核心公式

$$
$\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G):=\mathcal D^b_{(I_u^+,\chi^*\mathcal L_{\mathrm{AS}})}(\mathrm{Fl}_G)$$(-)\star_I(-)\colon\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)\times\mathcal D^b_c(I\backslash\mathrm{Fl}_G)\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$
$$

$$
$(-)\star_I(-)\colon\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)\times\mathcal D^b_c(I\backslash\mathrm{Fl}_G)\to\mathcal D^b_{\mathrm{IW}}(\mathrm{Fl}_G)$
$$

## 常见误解

- 把 $I_u^+$ 与 $I$ 搞混：$I_u^+$ 是 pro-unipotent 根，$\chi$ 定义在它上面；$I$ 是完整的 Iwahori，只出现在右侧卷积因子里。
- IW 范畴里的对象不是「$I$-等变层」：它是「$I_u^+$ 等变、但带 Whittaker 扭曲」，所以不能直接套用 $\mathcal P_I$ 的结论。

## 相关卡

[Whittaker 层与 $(H,\chi^*\mathcal L_{\mathrm{AS}})$-等变范畴](../concepts/whittaker-sheaves.md) · [IW 反常层的最高权结构（命题 4.3.1）](../concepts/iw-highest-weight.md) · [主函子 $F^{\mathrm{IW}}$ 与 Arkhipov–Bezrukavnikov 等价（定理 5.0.1）](../concepts/functor-fiw.md)

## 出处（印刷页）

- A p.9（A p.9）

> 说明：§4.2 全在 p.9；$\chi$ 的合成与 $\star_I$ 同页定义。
