# 原文记号宏（harvmac → LaTeX）对照表

本文件由 `gw/conv.py` 自动生成。原文是 1990 年代 harvmac 手写源码，作者用了大量记号宏；
转换器把它们原样移植进了导言区 `macros.tex`，因此**片段里可以、也应该原样保留这些宏**，
这样数学与原文逐字一致。下面给出每个宏的 LaTeX 展开，供核对渲染与改稿时查用。

| 宏 | LaTeX 展开 | 说明 |
|---|---|---|
| `\eurm` | `{\fam\eurmfam\relax#1}` |  |
| `\eusm` | `{\fam\eusmfam\relax#1}` |  |
| `\cmmib` | `{\fam\cmmibfam\relax#1}` |  |
| `\gx` | `g_{#1}` |  |
| `\DefWarn` | `` |  |
| `\II` | `\bm{I}` |  |
| `\EUU` | `\mathcal{U}` |  |
| `\EUV` | `\mathcal{V}` |  |
| `\EUT` | `\mathcal{T}` |  |
| `\EUW` | `\mathcal{W}` |  |
| `\EUS` | `\mathcal{S}` |  |
| `\EUX` | `\mathcal{X}` |  |
| `\EUZ` | `\mathcal{Z}` |  |
| `\EUY` | `\mathcal{Y}` |  |
| `\EUQ` | `\mathcal{Q}` |  |
| `\euc` | `\mathcal{c}` |  |
| `\EUA` | `\mathcal{A}` |  |
| `\EUB` | `\mathcal{B}` |  |
| `\EUC` | `\mathcal{C}` |  |
| `\EUD` | `\mathcal{D}` |  |
| `\EUE` | `\mathcal{E}` |  |
| `\EUF` | `\mathcal{F}` |  |
| `\EUG` | `\mathcal{G}` |  |
| `\EUH` | `\mathcal{H}` |  |
| `\EUI` | `\mathcal{I}` |  |
| `\EUJ` | `\mathcal{J}` |  |
| `\EUK` | `\mathcal{K}` |  |
| `\EUL` | `\mathcal{L}` |  |
| `\EUM` | `\mathcal{M}` | 花体 $\mathcal{M}$（希格斯丛模空间等） |
| `\EUN` | `\mathcal{N}` |  |
| `\EUO` | `\mathcal{O}` |  |
| `\EUP` | `\mathcal{P}` |  |
| `\EUR` | `\mathcal{R}` |  |
| `\TT` | `{\mathbb{T}}` | $\mathbb{T}$，极大环面 |
| `\cA` | `{\mathcal A}` |  |
| `\cD` | `{\mathcal D}` |  |
| `\cF` | `{\mathcal F}` |  |
| `\cO` | `{\mathcal O}` |  |
| `\cK` | `{\mathcal K}` |  |
| `\ot` | `\otimes` |  |
| `\End` | `{\rm End}` |  |
| `\ra` | `\rightarrow` |  |
| `\hat` | `\widehat` |  |
| `\G` | `{\Gamma}` |  |
| `\M` | `{\EUM}` |  |
| `\MH` | `{{\EUM}_H}` | $\mathcal{M}_H$，带分歧希格斯丛模空间 |
| `\CZ` | `{\mathcal Z}` |  |
| `\MHAD` | `\MH(G_{\rm ad})` |  |
| `\tilde` | `\widetilde` |  |
| `\bar` | `\overline` |  |
| `\Gad` | `{G_{\rm ad}}` |  |
| `\ad` | `{\rm ad}` |  |
| `\EUBB` | `\bm{B}` |  |
| `\CMR` | `\bm{R}` |  |
| `\EUWW` | `\mathfrak{W}` |  |
| `\np` | `Nucl. Phys. {\bf B#1} (#2) #3` |  |
| `\pl` | `Phys. Lett. {\bf #1B} (#2) #3` |  |
| `\prl` | `Phys. Rev. Lett.{\bf #1} (#2) #3` |  |
| `\physrev` | `Phys. Rev. {\bf D#1} (#2) #3` |  |
| `\ap` | `Ann. Phys. {\bf #1} (#2) #3` |  |
| `\prep` | `Phys. Rep. {\bf #1} (#2) #3` |  |
| `\rmp` | `Rev. Mod. Phys. {\bf #1} (#2) #3` |  |
| `\cmp` | `Comm. Math. Phys. {\bf #1} (#2) #3` |  |
| `\mpl` | `Mod. Phys. Lett. {\bf #1} (#2) #3` |  |
| `\bz` | `{\bar z}` |  |
| `\by` | `{\bar y}` |  |
| `\bt` | `{\bar t}` |  |
| `\bsigma` | `{\bar\sigma}` |  |
| `\bpartial` | `{\bar\partial}` |  |
| `\Tr` | `{\rm Tr}` |  |
| `\eps` | `\epsilon` |  |
| `\RR` | `{\mathbb{R}}` |  |
| `\cL` | `{\mathcal L}` |  |
| `\CC` | `{\mathbb{C}}` |  |
| `\PP` | `{\mathbb{P}}` |  |
| `\LG` | `{^L\negthinspace G}` |  |
| `\cQ` | `{\mathcal Q}` |  |
| `\neg` | `\negthinspace` |  |
| `\Z` | `{\mathbb{Z}}` |  |
| `\R` | `{\mathbb{R}}` |  |
| `\C` | `{\mathbb{C}}` |  |
| `\Lam` | `\Lambda_{#1}` |  |
| `\pf` | `{\rm Pf ~}` |  |
| `\bigone` | `\mathbf{1}` |  |
| `\ZZ` | `\mathbb{Z}` |  |
| `\half` | `\frac{1}{2}` |  |
| `\mx` | `m_{#1}` |  |
| `\lamlam` | `\langle S_{#1}\rangle` |  |
| `\CM` | `{\EUM}` |  |
| `\Re` | `{\rm Re ~}` |  |
| `\Im` | `{\rm Im ~}` |  |
| `\lfm` | `\medskip\noindent\item{#1}` |  |
| `\cI` | `{\mathcal I}` |  |
| `\cJ` | `{\mathcal J}` |  |
| `\cM` | `{\EUM}` |  |
| `\cN` | `{\EUN}` |  |
| `\gog` | `{\mathfrak g}` |  |
| `\tI` | `{\tilde I}` |  |
| `\tg` | `{\mathfrak t}` |  |
| `\tpsi` | `{\tilde\psi}` |  |
| `\N` | `{\EUN}` |  |
| `\g` | `{\mathfrak g}` |  |
| `\BG` | `{\overline \Gamma}` |  |
| `\HG` | `{\widehat \Gamma}` |  |
| `\rr` | `r` |  |
| `\char` | `{\rm char}` |  |
| `\cochar` | `{\rm cochar}` |  |
| `\wt` | `{\rm wt}` |  |
| `\cowt` | `{\rm cowt}` |  |
| `\rt` | `{\rm rt}` |  |
| `\cort` | `{\rm cort}` |  |
| `\SS` | `{\mathcal S}` |  |
| `\CK` | `\bm{k}` |  |
| `\cv` | `\bm{v}` |  |
| `\cb` | ` b` |  |
| `\FF` | `{\mathcal F}` |  |
| `\CV` | `\bm{V}` |  |
| `\Weyl` | `{\mathcal W}` |  |
| `\AffWeyl` | `{\mathcal W}_{\rm aff}` |  |
| `\eurx` | `\mathfrak{X}` |  |
| `\CMF` | `{\bm{F}}` |  |
| `\CB` | `{\mathcal B}` |  |
| `\cc` | `{\rm c.c.}` |  |
| `\eury` | `{\mathfrak{Y}}` |  |
| `\eurz` | `\mathfrak{Z}` |  |
| `\eurq` | `{\mathfrak{Q}}` |  |
| `\EURV` | `\mathfrak{V}` |  |
| `\BAff` | `{B_{\rm aff}}` |  |
| `\eura` | `\mathfrak{A}` |  |
| `\eurr` | `\mathfrak{R}` |  |
| `\eurs` | `\mathfrak{S}` |  |
| `\eurb` | `\mathfrak{B}` |  |
| `\eurt` | `\mathfrak{T}` |  |
| `\eurme` | `\mathfrak{E}` |  |
| `\CA` | `{\mathcal A}` | $\mathcal{A}=A+i\phi$（复联络） |
| `\CO` | `{\mathcal O}` | $\mathcal{O}$ |
| `\CF` | `{\mathcal F}` | $\mathcal{F}$（曲率） |
