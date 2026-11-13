# ch06a 施工报告

- 负责页段：PDF 77–88（原书 p.68–79）
- 文件：src\chunks\ch06a.tex（25.4 KB，593 行）
- 节：第6章 完全可积系统（含本章引言）/ 6.1 Liouville–Arnold 定理 / 6.2 Lie 群的分解（6.2.1 Cartan 分解 / 6.2.2 Iwasawa 分解 / 6.2.3 Bruhat 分解）/ 6.3 Toda 格子（本节跨出本 chunk，续于 ch06b）；章末评注在 ch06b，本块**不写**
- 编译：file:line=0 fatal=0 undefined=0 missingchar=0 overfull=0 undefref=0（`build.ps1 -Chunk ch06a`，草稿 tmp_ch06a.pdf，11 页）
- 批注：共 14 条（背景 5 / 难点 4 / 校勘 5），平均 1.17 条/页
- 环境与编号：定义 6.1.1、6.1.3；定理 6.1.4；引理* 6.1.2、6.2.1；定理* 6.2.2、6.2.3、6.2.4、6.3.1；公式 (6.1.1)–(6.1.10)、(6.2.1)–(6.2.42)、(6.3.1)–(6.3.32) 共 84 个 `\tag`，号全部照抄原书；3 个 `\takeaway`（6.1 / 6.2 / 6.3 各一，置于各节首 1–2 段之后）
- 新增术语（原书→中译，正文首现括注西文）：
  - 関数的に独立＝函数独立（functionally independent）/ 频率ベクトル＝频率向量（frequency vector）
  - 準周期解＝准周期解（quasi-periodic solution）/ 角座標＝角坐标（angle coordinate）/ 作用座標＝作用坐标（action coordinate）
  - 極分解＝极分解（polar decomposition）/ 岩澤分解＝Iwasawa 分解（Iwasawa decomposition）/ QR 分解＝QR 分解
  - 掃き出し法＝消去法（Gaussian elimination）/ 上半三角可逆複素行列＝上半三角可逆复矩阵 / 置換行列＝置换矩阵
  - 旗多様体＝旗流形 / Schubert 胞体＝Schubert 胞体（Schubert cell）/ Bruhat 分解＝Bruhat 分解
  - 重心＝重心 / 相対運動＝相对运动 / Flaschka の従属変数＝Flaschka 因变量（Flaschka's dependent variables）
  - 三重対角行列＝三对角矩阵 / 対称三重対角行列＝对称三对角矩阵 / 反対称行列＝反对称矩阵
  - 直交化法＝正交化（Gram–Schmidt）
- 疑似原书笔误（均照录并加校勘批注）：
  1. p.76 证明末「すなわち $u\in B$ となる」：由 (6.2.38) 定义的是 $u'$，(6.2.39) 亦算 $u'_{ij}$，此处应为 $u'\in B$；照录并注明。
  2. p.76「Wely 群」：通行拼法为 Weyl 群；照录并注明。
  3. p.76 (6.2.20) 中 $w\in\mathfrak{S}_n$，而 (6.2.40) 起改用 Weyl 群 $W$（$W\cong\mathfrak{S}_n$）；照录并注明二者在 $GL(n,\C)$ 情形一致。
  4. 原书 6.2.2 节标题印作「岩澤分解」（=Iwasawa），OCR 反复误识为「岩津」；已回页面图放大确认，统一作 Iwasawa 分解并批注。
- 待核/未解：无。全部公式（含 (6.2.12) Gram–Schmidt、(6.2.14)–(6.2.17) 四个矩阵块、(6.3.13)(6.3.14) 三对角矩阵、(6.3.23)–(6.3.25)、(6.3.30)–(6.3.32)）已回 p081–p088 页面图逐符号核对；(6.2.15) 原为漏译，已补。
- 需要的宏：无新增。用到的 `\bm`、`\mathfrak`、`\bigsqcup`、`\xrightarrow`、`\Longrightarrow`、`\dot{w}` 均在 preamble 既有宏包范围内，未改 preamble。
- 边界说明 / 需 Lead 处理的一点：chunk 终点 p.79 末行正处于**定理 6.3.1 证明中途**（「在两边左乘 $-Q^{-1}$，便得到」）。为让本 chunk 独立编译（build.ps1 的 draft.tex 会直接 `\end{document}`），末尾暂时补了 `\end{proof}` 并留 `% __CONTINUE__` 标记。ch06b 开头直接从 (6.3.33) 续写、未开 proof 环境，因此**合并成书时 p.79 末会多出一个 ■**；建议 Lead 在 main.tex 合并版中删去 ch06a 末尾这一 `\end{proof}`（或给 ch06b 续写段补 `\begin{proof}`）。

## 批注清单

| 原书页 | 类型 | 内容 |
|---|---|---|
| p.68 | 背景 | 角动量三分量之和并非 Poisson 可交换，故三者不能同时取作 Darboux 坐标的一部分；可积性要求的正是「函数独立 + 两两 Poisson 可交换」，交换性一项的来源即在此。 |
| p.69 | 难点 | (6.1.1) 第二个等号用 Leibniz 法则并代入 $\{f_j,f_i\}=0$；因此复合函数 $F(f_1,\dots,f_k)$ 不提供新的独立守恒量。 |
| p.70 | 背景 | 不变环面上的运动经作用–角变量线性化，「线性化」正是完全可积系统可解的含义；频率向量 $\omega=\partial H/\partial I$ 的算术性质决定轨道是周期还是稠密。 |
| p.71 | 校勘 | 原书 6.2.2 节标题与正文作「岩澤分解」（读作 Iwasawa），OCR 常误识为「岩津」；本译本统一作 Iwasawa 分解。 |
| p.72 | 背景 | 极分解 $g=ue^X$ 正是 $GL(n,\C)$ 的 Cartan 分解；$K=U(n)$ 与 Hermite 矩阵空间 $\mathfrak{p}$ 分别是极大紧子群与其正交补（对称空间 $GL(n,\C)/U(n)$ 的切空间）。 |
| p.73 | 难点 | (6.2.12) 中内积 $(v_i,u_j)$ 是 $\C^n$ 上的 Hermite 内积（对第二变量共轭线性）；因 $u_j$ 已正交归一，$w_i$ 与 $u_1,\dots,u_{i-1}$ 正交。 |
| p.74 | 背景 | Iwasawa 分解 $G=KAN$ 是极分解的「非对称」加强版；实矩阵情形 $K=O(n)$、$A$ 为正对角、$N$ 为单位上三角，恰是数值线性代数中的 QR 分解。 |
| p.76 | 校勘 | 原书作「$u\in B$」，据 (6.2.38) 定义的 $u'$ 及其下标运算应为「$u'\in B$」，照录并注明。 |
| p.76 | 校勘 | 原书 (6.2.20) 中 $w$ 取自 $\mathfrak{S}_n$，此处起改用 Weyl 群 $W$；$GL(n,\C)$ 情形二者一致（$W\cong\mathfrak{S}_n$），不影响结论。 |
| p.76 | 校勘 | 原书作「Wely 群」，通行拼法为 Weyl 群（Hermann Weyl），照录并注明。 |
| p.76 | 背景 | $G/B$ 即旗流形；Schubert 胞体 $Bw$ 的闭包给出 Schubert 簇，其维数等于置换 $w$ 的长度，这一胞体分解是 Schubert 演算与相交上同调的出发点。 |
| p.77 | 背景 | Flaschka 因变量把非线性方程 (6.3.4) 化为 $a_i,b_i$ 的二次方程组，从而可写成矩阵的 Lax 形式；这是 Toda 格子完全可积性的关键一步。 |
| p.78 | 难点 | Lax 形式意味着 $L(t)$ 与 $L_0$ 相似，故特征值全不随时间变化；Toda 格子的 $n$ 个独立守恒量即由 $L$ 的特征多项式给出。 |
| p.79 | 难点 | (6.3.25) 的等式是把第一项写成 $-Q^{-1}\dot{Q}\cdot L$、第二项写成 $L\cdot(-Q^{-1}\dot{Q})$，其中用到 $Q^{-1}L_0\dot{Q}=Q^{-1}L_0QQ^{-1}\dot{Q}$。 |

## 排版说明

- (6.2.16)(6.2.17) 原书是 (6.2.15) 的续行式（均以「$=$」起头），按原书分号各自成式，用 `equation` + `aligned` 前置 `&=`。
- (6.2.30)–(6.2.33) 原书每行各有一号，用 `gather` + 逐行 `\tag`；(6.3.9)–(6.3.12)、(6.3.23)–(6.3.25)、(6.3.30)–(6.3.32) 用 `align` + 逐行 `\tag`；(6.3.19) 原书三行共一号，用 `equation` + `aligned`。
- 每页页首均有 `% [原文 p.N]` 标记（p.68–p.79 共 12 处，同页续段不重复）。
