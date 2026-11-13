# 核验报告 · ch03g（原书 p.91–p.102）

核验人：tr-yi（译者乙）　作者：tr-bing（译者丙）　日期：2026-11-09

## 结论

需修改。正文与公式整体可靠，逐页核对未见实质误译；问题集中在两处 `example*` 的 □ 处理、一处上下标笔误，以及三处页标记位置违反 lead 新裁决（m00859）。

## 必须改（影响正确性）

1. 第 121 行 `\begin{example*}{1}`（原书 p.93–94，Bockstein 同态）：原书该例末尾有 □（p.94「……order $p^k$. □」），按体例应印 □，现带星版不印。改 `\begin{example*}{1}` → `\begin{example}{1}`。
2. 第 143 行 `\begin{example*}{2}`（原书 p.94，Massey 括号）：原书该例末尾有 □（「……natural cohomology operations. □」），同上。改 `\begin{example*}{2}` → `\begin{example}{2}`。
3. 第 144 行「$z_j\in H^{n_j}(X;k)$（$i=1,2,3$）」：下标 $j$ 与括注的 $i$ 不一致，原书作 $z_i\in H^{n_i}(X;k)\ (i=1,2,3)$。改 `$z_j\in H^{n_j}(X;k)$（$i=1,2,3$）` → `$z_i\in H^{n_i}(X;k)$（$i=1,2,3$）`。
4. 第 161 行 `\begin{example*}`（原书 p.94–95，Steenrod 平方的应用）：该例无编号，但原书末尾有 □（p.95 第 4 条推论末「……only if $n=2,4,8$. □」），现带星版不印 □。修法二选一：末行补 `\hfill$\square$`，或按 ch03d 既定做法改成 `\para{例}` 并手写 □。

## 必须改（体例 · 页标记位置，lead 裁决 m00859 第 ② 条）

页标记必须独占一行且落在段落/句子边界，现下列三处插在句中（LaTeX 会把换行当空格，排出来多一个空格）：

- 第 171 行 `% [原文 p.95]`：前一行以「……实、复、四元数以及」结尾，句中。应移到「Cayley 射影平面。」之后。
- 第 202 行 `% [原文 p.96]`：前一行以「设 $w$ 是」结尾，句中。应移到该句结束之后。
- 第 297 行 `% [原文 p.99]`：前一行以「……并按它的次数分次，即令」结尾，句中。应移到该句结束之后。

## 建议改（可读性/文风）

1. 第 315 行 `$E_m=\bigoplus_{q,l}E_m^{q,l}$`、第 322 行 `$\bigoplus\limits_{q-l=t}E_\infty^{q,l}$`：原书此处用的是一般的求和号 $\sum$，不是直和号 $\bigoplus$（同页别处的直和号则确为 $\bigoplus$）。建议照原书作 `\sum_{q,l}`、`\sum_{q-l=t}`。
2. 第 85 行（原书 p.92）$\deg a=\sum_i(2\omega'_i+1)+\sum_j(2\omega''_j+1)=2(\sum\omega'_i+\sum\omega''_j)+s$ 与原书逐字一致，但按该式自身的逻辑右端应为 $+s+q$（$q$ 为 $\omega'$ 的长度）。原书如此，正文不动，可加一条 Tutor Note 提示，免读者卡住。
3. 第 130 行「对 $\Ker\beta_{k-1}$（$k\ge 2$，$\beta_1=\beta$）类似地定义一个运算 $\beta_k$」：原句主语是元素 $z\in\Ker\beta_{k-1}$，译作「对……定义」略顺；可改为「对 $z\in\Ker\beta_{k-1}$……类似地定义运算 $\beta_k$」。

## 抽查记录

- p.91（PDF 98）：Steenrod 平方性质 (iii)–(v)、乘性公式；Steenrod 幂性质 (i)–(v)、(6.9) $St_p^{2j(p-1)+1}=\beta\mathcal{P}^j$、(6.10) 两行——正确。
- p.92（PDF 99）：(6.11) $Sq^\omega$、$u_\omega$、$\omega_j=2^{h_j}-1$、$S_{k,\omega}$、$S_{(\omega',\omega'')}$ 与乘法公式——正确；$\deg a$ 式照原书（见建议改 2）。
- p.93（PDF 100）：$\tau$-Cartan 型 $s(a)$、双分次 $a\mapsto[s(a),\deg a-s(a)]$、Milnor 运算 $\theta_k$、$s(\theta_k)=1$、$\theta_k\theta_j=-\theta_j\theta_k$——正确。
- p.94（PDF 101）：全部上同调运算分类段、(6.12) $\beta_k$ 及其定义域余域、(6.13) Massey 括号与歧义项——内容正确；两个编号例的 □ 见必须改 1、2，$z_i$ 上下标见必须改 3。
- p.95（PDF 102）：$Sq^nu_n=u_{2n}$、$n=2^s$ 的论证、Adams 分解、四条推论（实可除代数、稳定切丛、Hopf 不变量、Hopf 纤维化）、脚注（Hopf 不变量定义见第 4 章 §3）——正确。
- p.96（PDF 103）：$(z^2)_i=\Delta_1^*(w_i)$、$Sq^{n-i}(z)=(z^2)_i$、$Sq^{n+i}(z)=0$、$Sq^n(z)=z^2$、Hopf 代数与增广 $\varepsilon$、张量积代数——正确。
- p.97（PDF 104）：扭映射 $\sigma$、对角同态 $\Delta^*$ 公理、对称 Hopf 代数、(6.14) $St_p^i$、$St_p^0=\alpha^*$（Frobenius-Adams）——正确。
- p.98（PDF 105）：(6.15)(6.16)(6.17)、$A^+$ 的定义、$n$-链与 $\deg\sigma^n=\sum_{j=1}^n n_j+n$、脚注 8、9（含 Novikov 与 Translator's Note）——正确。
- p.99（PDF 106）：边缘同态公式、$E_m$、$d_m$、$E_2^{q,l}\cong\Ext$、$\sum_{q-l=t}E_\infty^{q,l}\cong G\pi_t^s(K)$、$G\pi=\oplus_jG_j\pi$、$K=S^n$ 时乘性微分——内容正确，$\sum/\bigoplus$ 见建议改 1。
- p.100（PDF 107）：$\pi^s_*=\oplus_k\pi^s_k$、$E_2^{\ast,\ast}=\Ext$、$h_0\in E_2^{1,1}$、Example 1 起与 (6.18)、$d_m(x)=0$——正确。
- p.101（PDF 108）：Example 1 收尾（其 □ 在 p.101 顶端，故用非星版正确）、Example 2、$h_i\in\Ext^{1,2^i}$、$d_2(h_i)=h_0h_{i-1}^2$、$h_3=\sigma$、$h_0h_3^2=dz$、(6.19) 原书确印作 $\Ext^{1,2^i+2^j}$（批注说明应为 $2^{i}+2^{j}$ 的次数，处理得当）、脚注 10——正确。
- p.102（PDF 109）：(6.20) $\pi_t^s(K)\otimes\Q\cong H_t(K;\Q)$、Hopf 代数模型 $B$、$C\subset A$、$\Ker f=AC^+=C^+A$、item (i)；末尾 enumerate 已闭合，与 ch03h 第 7 行 `start=2` 的 item (ii) 衔接正确——正确。

---

---

---

## 作者修回后的复核（第二轮，核验人 tr-yi）

- ch03f 必须改 1（块首重复跨页句）：已修。现从「此外，若 $p>2$，则 $n-r$ 为偶数」起，重复片段与随之失效的 Tutor Note 已删改；p.78 末句归属 ch03e 正确。
- ch03f 必须改 2（例 3 环境）：已修。`example{3}` 现包住整段（含「如前所述，对于 $K(\pi,1)$ 型……」），□ 落在例末，与原书 p.89 一致。
- ch03f 页标记 p.88、p.90 两处已下移到句末。
- ch03g 必须改 1（末尾 enumerate 未闭合）：已修，已补 `\end{enumerate}`。
- ch03g 必须改 2、3（例 1 与例 2 去星）：已修，改为 `example{1}` 与 `example{2}`，□ 由环境自动印出。
- ch03g 必须改 4（无编号例补 □）：已修，仍用 `example*`，末条推论后加 `\hfill$\square$`。
- ch03g 撤回两条（作者以 450–600 dpi 裁图复核，原书原貌如此）：① p.94 例 2 原书即印 $z_j\in H^{n_j}(X;k)$ 而括注 $i=1,2,3$，按「笔误照排」保留混用，不改为 $z_i$；② p.103 第 1 条原书为三星号（三阶分次谱序列），非两星号。
- ch03g 页标记 p.95、p.99 已下移；p.96 前句以「：」结尾，按新规属句边界，保留合规。
- ch03h 必须改 1（例 2 环境提前收尾）：已修，`\end{example}` 移至纤维化清单 `\end{enumerate}` 之后，□ 落在第 7 条末，与原书 p.107 一致。
- ch03h 必须改 2、3、4（p.109 三例加星）：已修，均为 `example*{1}`、`example*{2}`、`example*{3}`（原书无 □）。
- ch03h 页标记 p.108、p.110、p.111 三处已下移到句末。
- ch03i 必须改（K 理论开头实复并列）：已修，ch03i:15 现为「群 $K_\R^0(K,L)$ 与 $K_\C^0(K,L)$（分别为实与复情形）」，后文泛用写法 $K_\Lambda^0$ 保留，与原书 p.113 一致。
- ch03i 页标记 p.114、p.117、p.122 三处已下移到句末。

复跑结果（四块均）：check_chunk 0 error——ch03f 页 79..90、tag 8、陈述 9、Tutor Note 6；ch03g 页 91..102、tag 12、陈述 4、Tutor Note 5；ch03h 页 103..112、tag 16、陈述 6、Tutor Note 4；ch03i 页 113..124、tag 26、陈述 1、Tutor Note 5。check_glyphs 0 blocking。环境配对（example*/example 等）逐块计数一致。

**结论：四块均通过（tr-bing 已按清单修完，tr-yi 复验）。**
