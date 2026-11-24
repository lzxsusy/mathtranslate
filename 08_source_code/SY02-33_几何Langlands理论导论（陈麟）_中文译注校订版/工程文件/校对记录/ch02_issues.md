# ch02（Hecke 特征性质）审读：问题清单

范围：`src/chapters/ch02.tex` 全 256 行（原 PDF p12–p19；p11 下半的章首与 p19 末句也在本文件）。审读期间该文件于 23:48 被另一进程改动过一次（行尾由 CRLF 改为 LF，且第 138、155 行的“相对 Schubert 层”已改为“相对 Schubert 分层”），下列行号按改动后的当前文件。
逐句对照 `work/en/ch02_en.txt` 第 1–410 行，公式按 p012–p019 的整页 PNG 复核（Def 2.1.1/2.1.2、Thm 2.2.1、Thm 2.2.4、Def 2.3.1、Thm 2.4.1、Hecke≃Bun^∞×^{L^+G}Gr、Def 2.6.1、(2.1)、d_i 与归一化函子、闭包序、det 展开、IC^{⋆i}、Mod^{-i}_n、H^{i,+}_n、Springer 解消、Claim 2.13.1、投影公式链）。

结论：P1 0 条；P2 3 条（80、94、209 行：1 条公式、2 条术语）。未发现整句漏译/增译、逻辑反转或定理/命题编号错误；#2.14 的整条投影公式计算与原文逐项一致。

## ch02.tex:80（原 PDF p13）
- 原文：β : P|_{X×S−Γ_x} ≅ P^0|_{X×S−Γ_x}, where P^0 is the trivial G-torsor.
- 原译：$\beta:P|_{X\times S-\Gamma_x}\xrightarrow{\sim}P_0|_{X\times S-\Gamma_x}$，其中 $P_0$ 是平凡 $G$ 挠子。
- 类型：公式
- 改法：$\beta:P|_{X\times S-\Gamma_x}\xrightarrow{\sim}P^{0}|_{X\times S-\Gamma_x}$，其中 $P^{0}$ 是平凡 $G$ 挠子。
- 理由：原书（p013、p014 PNG）平凡挠子记作上标 $P^0$，译稿一律改成下标 $P_0$（第 80、83、95 行）；虽不致误解，但属可核的上下标偏差，也与书里 $P'$、$\Bun_G^\lambda$ 一类上标记号不统一。原文用花体 $\mathcal P$、译稿改用斜体 $P$，同属记号层面的改动，建议照原文一并统一。

## ch02.tex:94（原 PDF p14）
- 原文：To pass from this local model to global modifications, introduce the infinite-level bundle Bun^∞_G(S) = {(x, P, α) | x: S → X, P ∈ Bun_G(S), α: P|_{D_x} ≅ P^0|_{D_x}}.
- 原译：为了从这个局部模型过渡到整体修改，引入无限层丛
- 类型：术语
- 改法：为了从这个局部模型过渡到整体修改，引入无限级丛
- 理由：infinite-level 应译“无限级”（即在形式圆盘 $D_x$ 上平凡化到无穷阶），译作“层”与本书 sheaf 的“层”同字撞车，读者会把 $\Bun_G^\infty$ 误当某个层；第 167 行“无限层 $L^+G$ 挠子”同误。

## ch02.tex:209（原 PDF p17）
- 原文：The stratum where V/V′ ≃ k(x)^{⊕i} is precisely Hecke^i_n.
- 原译：满足 $\mathcal V/\mathcal V'\simeq k(x)^{\oplus i}$ 的层正是 $\Hecke_n^i$。
- 类型：术语
- 改法：满足 $\mathcal V/\mathcal V'\simeq k(x)^{\oplus i}$ 的分层正是 $\Hecke_n^i$。
- 理由：stratum 是“分层”（相对版的轨道/子叠），“的层”会被读成“满足该条件的层”（sheaf），与全章“层”的含义直接冲突；同类还须改第 169 行“相应的相对层 $\Gr_{G,X}^\lambda$”（第 138、155 行已改为“分层”，请照此统一；若全书改用“分片”，则一并对齐）。
