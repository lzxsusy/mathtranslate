# ERRATA.md — 底本疑误与译注登记（SY05-24）

> 施工中发现原文疑似笔误，**照译**，在此登记并给出建议的正确形式；不擅自改原文数学。
> 状态：`候选`（施工者提出，Lead 复核）→ `确认`（已核页面图，确为原文如此）→ `已注`（译文中已加批注）。

## 登记表

| # | 页 | 位置 | 原文 | 疑点 | 建议 | 状态 |
|---|---|---|---|---|---|---|
| 1 | p4 | §1 | "compute the partition function it so easily" | `it` 疑为衍字 | 删去 `it`："compute the partition function so easily" | 候选 |
| 2 | p5 | §1 | "It is seems like" | 系动词重复 | "It seems like" | 候选 |
| 3 | p7 | §1，(1.25) 上段 | "the fundamental representation of SO(N)" | 与 (1.25) 的展开不符：该展开 $a_1+a_1^{-1}+\cdots+a_n+a_n^{-1}$ 是 $\SO(2N)$ 矢量表示的特征标 | 应为 $\SO(2N)$ | 候选 |
| 4 | p4 | 式 (1.12) | 引入 $\mathbf{f}$ 记号后全文未再使用 | 记号悬置 | 可删 $\mathbf{f}$，或后文补用 | 候选 |
| 5 | p11 | §2.2 | "the index it studied" | 缺系动词 | "the index it is studied" 或 "the index studied" | 候选 |
| 6 | p12 | §2.2 | "the this superpotential" | 冠词重复 | "this superpotential" | 候选 |
| 7 | p10、p13 | 表 1、表 2 第三组四个导数行 | $\delta$ 列印作 $0,0,2,2$、$\mathcal{I}$ 列印作 $p,q$（$q$ 在 $\partial_{-\dot+}$ 行） | 按 $\delta=\Delta-2j_1+\frac32r$ 应为 $2,2,0,0$；即 $\delta$ 列相当于误用 $j_2$ 代替 $j_1$ 计算。等价地 $q$ 应跟在 $\delta=0$ 的 $\partial_{+\dot-}$ 行 | $\delta$ 列改为 $2,2,0,0$，$\mathcal{I}$ 列 $p$ 随 $\partial_{+\dot+}$、$q$ 随 $\partial_{+\dot-}$ | 候选 |
| 8 | p14 | 式 (2.20) | 被积函数只有单个 $\Gamma(pqa^\alpha)$，测度无 $\prod_i$ | 按 (2.18) 的 Weyl 投影积分，应有 $\frac1{|W|}\prod_i\oint\frac{\dd a_i}{2\pi\ii}$ 与 $\prod_\alpha\Gamma(pqa^\alpha)$ | 补 $\prod_i$（测度）与 $\prod_\alpha$（被积函数） | 候选 |
| 9 | p16 | 式 (2.24) 正文 | 正文写 $\{|\chi\rangle\}$，方程写 $Q|\varphi\rangle=0$ | 短多重态符号 $\chi$ 与 $\varphi$ 混用 | 统一为 $|\chi\rangle$ 或 $|\varphi\rangle$ | 候选 |
| 10 | p16 | 式 (2.26) 及其下段 | 重组链末项印 $r-2j-2$，下段印 $r-2j-3$，并有 $\Delta+j$ | $j$ 疑为 $j_1$ 的漏下标 | 各处 $j\to j_1$：$r-2j_1-2$、$r-2j_1-3$、$\Delta+j_1$ | 候选 |
| 11 | p22 | §3.2 | "the a puncture" | 冠词衍余 | "a puncture" 或 "the puncture" | 候选 |
| 12 | p25 | §3.3 | "Ruijsenaars-Schnider" | 人名拼写 | 应为 Ruijsenaars–Schneider | 候选 |
| 13 | p26 | 式 (4.4) 第二行 | $V(\theta)=-\sum\frac1n(1-i(p^n,q^n,x^n,s^n)\cos(n\theta).$ | 括号不平衡；且 $\cos(n\theta)$ 应在因子 $(1-i(\cdots))$ 之外 | $V(\theta)=-\sum_{n\ge1}\frac1n\big(1-i(p^n,q^n,x^n,s^n)\big)\cos(n\theta)$ | 候选 |
| 14 | p27 | 式 (4.5) 第二行 | $V_n=\frac{2\pi}{n}(1-i(p^n,q^n,x^n,s^n).$ | 缺右括号 | $V_n=\frac{2\pi}{n}\big(1-i(p^n,q^n,x^n,s^n)\big)$ | 候选 |
| 15 | p30 | 文献 [15] | "Advances in Mathematics 156 (2000) 4476" | 页码疑为 44–76 的粘连 | 44–76 | 候选 |
| 16 | p32 | 文献 [41] | "AdS(5) x T**1,1" | 记号疑为 $T^{1,1}$ 的排版残留 | $AdS_5\times T^{1,1}$ | 候选 |
| 17 | p31 | 文献 [27] | "I. Garca-Etxebarria" | 姓氏疑缺重音 | García-Etxebarria | 候选 |

## 说明

- 原文为讲义，符号约定与常见文献可能不同（如 $(-1)^F$ 的分配、$\Tr$ 的定义域），这类**不算笔误**，只在批注里说明约定。
- 表格若与正文公式不一致，以正文推导为准并注明。
- 参考文献条目不校对（照抄），仅登记明显排版异常（#15–#17）。
- 上述 17 条均已在上文各块中以 `% [Tutor Note: …]` 或正文括注指出；译文一律照录原文形式。
