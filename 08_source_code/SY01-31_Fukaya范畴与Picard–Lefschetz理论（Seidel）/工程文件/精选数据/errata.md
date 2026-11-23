# 原书笔误与内部不一致登记

本表只登记**原书**（Seidel, *Fukaya categories and Picard–Lefschetz theory*, EMS 2008）中可确认的笔误或前后不一致；译文处理方式另列。每条给出原书印刷页与依据。

| # | 原书页 | 原文 | 问题 | 处理 | 依据 |
|---|---|---|---|---|---|
| 1 | p.4 / p.5 | Theorem A: “$n \ge 1$”；p.5: “$n > 1$ excludes the lowest nontrivial dimension, where $X^1$ is a Riemann surface” | 同一条件前后不一致；按 p.5 的解释与 Theorem B 后文，应为 $n > 1$ | 译文统一作 $n>1$，并在 Theorem A 处加译者注说明原书不一致 | 原书 p.4–5 对读；无外部勘误 |
| 2 | p.4 | “combinational data” | 拼写错误，应为 “combinatorial data” | 译文作“组合数据”，不加注 | 英语拼写；同页下文 “combinatorial data” 亦见于 p.5 |
| 3 | p.106 | §8g 曲率公式 | 作者已发布勘误，$R_K$ 的公式应为 $(\partial_t K(\partial_s)-\partial_s K(\partial_t)+\{K(\partial_s),K(\partial_t)\})ds\wedge dt$ | 已核对 `section-8.tex:144-146`，译文与勘误一致，无需改 | Seidel, “Erratum to Section 8g”, https://math.mit.edu/~seidel/errata/book-curvature-erratum.pdf |
| 4 | p.24 | Lemma 2.1: “Let $\mathcal A$ be a cohomologically unital $A_\infty$-category. Then…” | 陈述漏掉“每个对象的 endomorphism 复形上同调非零，或该对象与一切对象双向 hom 为零”的条件；含零对象时严格单位元不存在，命题为假 | 译文保留补上的条件，并在引理处加注说明这是对原书陈述的必要修补 | 反例由 A∞ 范畴定义直接验证（零对象的 $\hom(X,X)$ 无上同调，$e_X=0$ 与严格含幺方程矛盾） |
| 5 | p.52 | Lemma 3.30（英文） | 中文译本引作“引理 3.31”；从上下文看，3.31 才是从 $H(\Tw\mathcal B)$ 回到 $H(\mathcal B)$ 的桥接引理，原书编号疑误 | 译文保留 3.31，不加注 | 原书 §3 引理编号与证明结构对读 |
