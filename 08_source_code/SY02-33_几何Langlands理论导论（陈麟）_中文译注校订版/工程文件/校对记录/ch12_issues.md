# ch12（谱分解与 LocSys^restr）审读：问题清单

范围：`src/chapters/ch12.tex` 全 144 行（原 PDF p60–p63）。
逐句对照 `work/en/ch12_en.txt`，公式按 p060–p063 的 PNG 复核（p61 相容方块在译稿中是图片 `\origdiagram{p061-square.pdf}`）。

结论：P1 2 条（23、51 行，无限 Jordan 块被改成“无限维局部系统”）；P2 4 条（51 行定理编号、65、118、139）。其余 §12.1–§12.7 未发现误译、漏译、增译或公式错误。

## ch12.tex:23（原 PDF p60）

- 原文：The functor $f_!$ is already subtle topologically: for instance, for $\mathrm{pt}\to S^1$, the result corresponds to a local system with an infinite Jordan block.
- 原译：函子 $f_!$ 即使在拓扑上也已经相当微妙：例如，对 $\mathrm{pt}\to S^1$，将一维常值对象作 $!$-推前，得到的是基本群 $\mathbb Z$ 的正则表示所对应的无限维局部系统。
- 类型：误译
- 改法：函子 $f_!$ 即使在拓扑上也已经相当微妙：例如，对 $\mathrm{pt}\to S^1$，所得结果对应一个具有无限 Jordan 块的局部系统。
- 理由：原文的要点是“infinite Jordan block（无限 Jordan 块）”，译文换成“无限维局部系统”并补出“基本群 $\mathbb Z$ 的正则表示”；正则表示可分解为特征标，不会给出 Jordan 块，数学内容被改。

## ch12.tex:51（原 PDF p61）

- 原文：…already maps such as $\mathrm{pt}\to S^1$ can create infinite Jordan-block local systems.
- 原译：…甚至像 $\mathrm{pt}\to S^1$ 这样的映射，也会产生无限维局部系统，例如基本群的正则表示。
- 类型：误译
- 改法：…甚至像 $\mathrm{pt}\to S^1$ 这样的映射，也会产生具有无限 Jordan 块的局部系统。
- 理由：同 ch12.tex:23，“infinite Jordan-block”被改成“无限维”，又增出“基本群的正则表示”，丢掉了单值化为单个无限 Jordan 块这一关键结构。

## ch12.tex:51（原 PDF p61）

- 原文：The local-to-global theorem, Theorem 9.3.1, says that the correct monoidal object is nevertheless $\mathrm{Perf}(\mathrm{Maps}(Y,B\check G))$, or its $\mathrm{QCoh}$-completion.
- 原译：\secref{12.2}的 Betti 局部到整体定理说明，正确的幺半对象仍然是 $\operatorname{Perf}(\operatorname{Maps}(Y,B\checkG))$，或它的 $\QCoh$-完备化。
- 类型：漏译
- 改法：\thref{9.3.1}（局部到整体定理）说明，正确的幺半对象仍然是 $\operatorname{Perf}(\operatorname{Maps}(Y,B\checkG))$，或它的 $\QCoh$-完备化。
- 理由：原文明引定理 9.3.1（译稿 ch09.tex:53 正是“Gaitsgory–Lurie，局部到整体”定理），译文把这一跨章编号换成“§12.2”，丢掉了原书的定理指向。

## ch12.tex:65（原 PDF p61）

- 原文：The Betti local-to-global theorem in Subsection 12.2 shows the nilpotent-support condition implies the Hecke-lisse property [NY19], and the form used in AGKRRV upgrades this to the equivalence [AGK$^+$20a].
- 原译：\secref{12.2}中讨论的 Betti 局部到整体定理及其 Hecke 输入说明，幂零支撑条件蕴涵 Hecke 光滑性质\cite{NY19}，而 AGKRRV 使用的形式将这一结论加强为等价\cite{AGK20a}
- 类型：增译
- 改法：\secref{12.2}中讨论的 Betti 局部到整体定理说明，幂零支撑条件蕴涵 Hecke 光滑性质\cite{NY19}，而 AGKRRV 使用的形式将这一结论加强为等价\cite{AGK20a}
- 理由：原文只说该定理本身给出这一蕴涵，并未提“Hecke 输入”；增出的短语把论证主体改成“定理及其 Hecke 输入”。

## ch12.tex:118（原 PDF p63）

- 原文：The expected sheaf-function statement is the categorical trace identity … , up to the usual choices of completions, finiteness conditions, and stacky automorphism weights on automorphic functions.
- 原译：预期的层与函数对应陈述是范畴迹恒等式 …，这里须按通常约定选择完备化、有限性条件，以及自守函数中来自叠自同构群的权重。
- 类型：误译
- 改法：预期的层与函数对应陈述是范畴迹恒等式 …，它只在通常的完备化选择、有限性条件以及自守函数上来自叠自同构的权重的意义下成立。
- 理由：“up to”表示恒等式差这些标准选择而成立，译文改写成“须按通常约定选择”，把限定条件读成了操作要求，削弱了“仅在 up to 意义下成立”的限定。

## ch12.tex:139（原 PDF p63）

- 原文：Thus the categorical trace formalism geometrizes the passage from geometric to function-theoretic Langlands and V. Lafforgue's excursion operators.
- 原译：因此，范畴迹形式体系将从几何 Langlands 到函数论 Langlands 的过渡，以及 V. Lafforgue 的游走算子几何化。
- 类型：逻辑
- 改法：因此，范畴迹形式体系把从几何 Langlands 到函数论 Langlands 的过渡、以及 V. Lafforgue 的游走算子都几何化了。
- 理由：谓语“几何化”被两个长宾语推到句末，“将…过渡”会先被读成“将要过渡”，句意要读到最后一个词才落定，影响理解。
