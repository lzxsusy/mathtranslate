# 晶体与 D-模（cdm14）资料卡 · 骨架图

这张图是 Gaitsgory–Rozenblyum（arXiv:1111.2087v4）的逻辑骨架：先把测试环约化、造出 de Rham 预栈 $X_{\mathrm{dR}}$，把晶体定义为它上面的层；再证左右两种晶体等价、Kashiwara 引理成立；然后用下降与归纳函子把晶体写成无穷小群胚上的全化；接着装两个 $t$-结构，证明与 D-模的经典等价；最后把线丛/gerbe 的扭化加进来，得到扭晶体。箭头上的数字是原文**印刷页**；概念卡是节点，推导卡是把节点连起来的边。

```text
引言 p.1–11   [O] overview
                 │  晶体 = $X_{\mathrm{dR}}$ 上的层；光滑时 = D-模；含非线性推广
                 ▼
§1  p.12–15   [A] dr-prestack ──deriv──▶ dr-kan
                 │   $Y_{\mathrm{dR}}(S)=Y({}^{\mathrm{cl,red}}S)$；dR 保极限/余极限
                 ├──▶ classically-formally-smooth（π₀ 满 ⟹ Čech 神经覆盖）
                 └──▶ laft-and-dr（laft ⟹ $Y_{\mathrm{dR}}$ 仍 laft 且经典）
                 ▼
§2  p.15–25   [B] left-crystal ──┬──▶ right-crystal（IndCoh，$f^!$ 拉回）
                 │                │
                 │                └──▶ upsilon-comparison ──deriv──▶ upsilon-equiv
                 │                       （$F\mapsto F\otimes\omega$ 给出左右等价）
                 └──▶ kashiwara ──deriv──▶ kashiwara-equiv
                        （$\Crys^r(Z)_X=\ker j^{\dagger,r}\simeq\Crys^r(X)$）
                 ▼
§3  p.25–30   [C] infinitesimal-groupoid（$X\times_{X_{\mathrm{dR}}}X\rightrightarrows X$）
                 ├──▶ h-descent ──deriv──▶ h-descent-proof（h/fppf 下降）
                 ├──▶ induction-right ──deriv──▶ right-induction（$\ind^r\dashv\oblv^r$，单子性）
                 └──▶ induction-left（需最终余连接；反例 $k[\alpha]$）
                 ▼
§4  p.30–41   [D] left-t-structure ──▶ left-vs-right-shift（光滑 $n$ 维差 $[-n]$）
                 ├──▶ right-t-structure ──deriv──▶ right-t-exact（$\ind^r$ t-正合）
                 ├──▶ indscheme-t-structure（逐 $X_\alpha$）
                 ├──▶ left-completeness（左完备）
                 ├──▶ coarse-induction（$\Psi_X$ 左完备化；Gorenstein ⇔ 穿过 $\Xi_X$）
                 └──▶ abelian-heart（$D(\Crys^r(X)^\heartsuit)\simeq\Crys^r(X)$）
                 ▼
§5  p.41–49   [E] integral-transform（核 $D^r_X=(\widehat\Delta_X)_*\omega$）
                 ├──▶ diff-operators（$D^l_X\simeq\mathrm{Diff}_X$）
                 └──▶ crystals-vs-dmodules ──deriv──▶ cdm-equiv
                        （$\Crys^r(X)\simeq D\text{-}\mathrm{mod}^r(X)$）
                 ▼
§6  p.48–58   [F] gm-gerbe（三种版本）──▶ twisting（$\mathrm{Tw}(Y)=\ker p^*_{\mathrm{dR}}$）
                 ├──▶ twist-picard（$\mathrm{Tw}(Y)\simeq\tau^{\le2}(H_{\mathrm{dR}}\times_H*)[2]$）
                 └──deriv──▶ twist-three（四版本等价）
                 ▼
§7  p.58–65   [G] twisted-crystals（$\Crys^{T,l}$、$\Crys^{T,r}$，$\Upsilon$ 仍等价）
                 └──▶ twisted-t-structure（左/右 t-结构、左完备）
```

## 三条阅读路径

| 目的 | 顺序 |
| --- | --- |
| 想弄懂「晶体是什么」 | `overview` → `dr-prestack` → `left-crystal` → `right-crystal` → `upsilon-comparison` → `kashiwara` |
| 想弄懂「为什么等于 D-模」 | `kashiwara` → `induction-right` → `abelian-heart` → `integral-transform` → `diff-operators` → `crystals-vs-dmodules` |
| 想弄懂「扭化与扭晶体」 | `gm-gerbe` → `twisting` → `twist-picard` → `twisted-crystals` → `twisted-t-structure` |
