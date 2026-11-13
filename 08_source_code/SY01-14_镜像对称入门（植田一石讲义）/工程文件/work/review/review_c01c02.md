# c01/c02 交叉校对报告

校对对象：`src/chunks/c01.tex`（p002–p005，23 条：(1.2)–(1.23)、(2.1)）、`src/chunks/c02.tex`（p006–p008，13 条：(2.2)–(2.10)、(3.1)–(3.4)）。
方法：逐页对照 `work/pages/p002.png`–`p008.png`（公式唯一真值），密集区另做 500 dpi 裁图（`work/review/tmp_c12_p4.png`、`tmp_c12_p5.png`、`tmp_c12_p7.png`）；并在临时目录用 preamble + c00 + c01 + c02 做了一次**局部**编译（非整书编译）以核对编号与跨文件环境。未修改任何 .tex。

**结论：必须改 2 条，可选改 5 条（其中 1 条含 6 处句末标点）**

## 必须改

### 1. c02 第 118 行（p008）／「Hamilton 系」→「Hamilton 系统」（glossary 冻结术语）

- 原文：「時間発展が Hamilton ベクトル場によって与えられるような力学系を Hamilton 系と呼ぶ。演習 2.7 から、Hamilton 系を考える舞台は局所的にはシンプレクティック多様体だと考えて良い。」
- 现状：「时间演化由 Hamilton 向量场给出的动力系统称为 Hamilton 系。由习题2.7 可知，考虑 Hamilton 系的舞台局部上可以认为是辛流形。」
- 建议改为（整段替换）：

```
时间演化由 Hamilton 向量场给出的动力系统称为 Hamilton 系统。由习题2.7 可知，考虑 Hamilton 系统的舞台局部上可以认为是辛流形。
```

- 依据：`glossary.tsv` 冻结「Hamilton 系 → Hamilton 系统」。同块第 112、115 行的「Hamilton 向量场」属另一词条，不必动。

### 2. c01 第 5–15 行（p002–p003）／习题1.3 句子缺「当……的……给定时」框架

- 原文：「多様体 N に対し、接束 TN 上の完全列 (1.2) の分裂 (splitting) が与えられた時、J_TN := … (1.3) と表示される J_TN によって概複素構造が入ることを示せ。」
- 现状：「对流形 $N$，切丛 $TN$ 上的正合列〔(1.2)〕给定该正合列的分裂（splitting）时，证明：由〔(1.3)〕所表示的 $J_{TN}$ 给出近复结构。」
  ——「正合列」与「给定……时」之间无连接（既无「当」也无「的分裂」），句子读不通。
- 建议改为（整块替换，仅两处改动：加「当」；把「给定该正合列的分裂……时」改为「的分裂……给定时」；两条 `\tag` 不动）：

```
\begin{exercise}
对流形 $N$，当切丛 $TN$ 上的正合列
\begin{equation}
    0 \to \pi^*TN \to T(TN) \xrightarrow{\pi_*} \pi^*TN \to 0 \tag{1.2}
\end{equation}
的分裂（splitting）给定时，证明：由
\begin{equation}
    J_{TN} := \begin{pmatrix} 0 & -\mathrm{id}_{TN} \\ \mathrm{id}_{TN} & 0 \end{pmatrix} \tag{1.3}
\end{equation}
所表示的 $J_{TN}$ 给出近复结构。这里 $\pi\colon TN\to N$ 是自然投影，映射 $\pi^*TN\to T(TN)$ 是纤维方向上切空间的自然嵌入。
\end{exercise}
```

## 可选改

### 1. 句末标点：display 结束句子时缺「。」（共 6 处）

编译后会出现「……[公式] T′M 称为……」这类粘连。建议统一在 `\tag` 前补 `.`（与 c01 对 (1.8) 的既有处理一致），位置：

- p003 c01 (1.9)：`TM\otimes_\R\C = T'M\oplus T''M` → `TM\otimes_\R\C = T'M\oplus T''M.`（否则下句「$T'M$ 称为……」粘连）
- p004 c01 (1.12)：`\bigwedge^q(T''M)^*` → `\bigwedge^q(T''M)^* .`（该段以公式收尾）
- p007 c02 (2.8)：`+ \{g,\{f,h\}\}` → `+ \{g,\{f,h\}\}.`（注意2.7 以公式收尾）
- p007 c02 (2.9)：`f\mapsto X_f:=\{f,-\}` → `f\mapsto X_f:=\{f,-\}.`（否则下句「把这一点与……」粘连）
- p008 c02 (3.1)：`\nabla V=\left(\frac{\partial V}{\partial x},\frac{\partial V}{\partial y},\frac{\partial V}{\partial z}\right)` → 末尾补 `.`
- p008 c02 (3.3)：`i=1,2,3` → `i=1,2,3.`

（若不愿改动公式内部，替代做法：把 (3.1) 前改为「则 Newton 运动方程为下式：」等引导句。）

### 2. p004 习题1.11 句式：陈述句 +「证明之」混杂

- 现状：「则 $N$ 是 $(T^*M)^{\otimes 2}\otimes TM$ 的截面，证明之。」
- 建议：「证明：$N$ 是 $(T^*M)^{\otimes 2}\otimes TM$ 的截面。」（与全书习题「证明：……」体例一致；提示文字不动。）

### 3. p005 习题1.17 语序：「不 $E_1$ 退化」→「不是 $E_1$ 退化的」

- 现状：「举出 Frölicher 谱序列不 $E_1$ 退化的紧复流形的例子。」
- 建议：「举出 Frölicher 谱序列不是 $E_1$ 退化的紧复流形的例子。」

### 4. p007 定义2.5 句末冗余（「……双线性映射……的映射」）

- 现状：「是指 $\R$ 上的双线性映射〔(2.4)〕且满足反对称性〔(2.5)〕Jacobi 恒等式〔(2.6)〕以及 Leibniz 法则〔(2.7)〕的映射。」
- 建议：「是指 $\R$ 上的双线性映射〔(2.4)〕，且满足反对称性〔(2.5)〕、Jacobi 恒等式〔(2.6)〕以及 Leibniz 法则〔(2.7)〕的映射。」（补一个逗号、一个顿号即可；四条 `\tag` 不动。）

### 5. p006 近辛形式的 Nijenhuis 类比句

- 原文：「概シンプレクティック形式に対する Nijenhuis テンソルの類似は 3 次微分形式 dω であり……」
- 现状：「近辛形式所对应的 Nijenhuis 张量的类比是 3 次微分形式 $d\omega$……」
- 建议：「对近辛形式而言，Nijenhuis 张量的类比物是 3 次微分形式 $d\omega$，而 Newlander–Nirenberg 定理的类比则是 Darboux 定理。」（语义更贴原文；「对应」易被读成「近辛形式所对应的 Nijenhuis 张量」。）

## 核验通过（无须改动）

1. **公式逐符号**：c01 的 23 条、c02 的 13 条全部逐条与 p2–p8 图像核对，**无一处与原文不符**。重点核过：
   - (1.6)–(1.9)：`T'_pM` / `T''_pM` 的上标撇与下标位置、`\otimes_\R\C`、`J_pX=\pm\sqrt{-1}X` 的符号、(1.8) 句末句点。
   - (1.10)–(1.12)：`\partial/\partial z_i` 与 `\partial/\partial\bar z_i` 的 ± 号；`\Omega^{p,q}_M:=\bigwedge^p(T'M)^*\otimes\bigwedge^q(T''M)^*`。
   - (1.13)–(1.16)：`\Gamma(\bigwedge^rT^*M)\otimes\C`（原文为 ⊗ℂ，未误作 ⊗_ℝℂ）；`\Pi^{p,q}` 的指标；`\partial:=\Pi^{p+1,q}\circ d`、`\bar\partial:=\Pi^{p,q+1}\circ d`。
   - (1.17)(1.18)：`[JX,JY]-[X,Y]-J[X,JY]-J[JX,Y]` 四项及其符号，提示式 `N(fX,Y)=N(X,fY)=fN(X,Y)`。
   - (1.19)：Ker/Im 分式、`\Omega^{p,q-1}_M` 与 `\Omega^{p,q+1}_M` 的上下限。
   - (1.21)(1.22)：`H^q(\Omega^p_M)\Rightarrow H^{p+q}(M)`；`0\to\C\to\Omega_M\to\Omega^1_M\to\cdots\to\Omega^{\dim M}_M\to0`。
   - (1.23)：Hopf 曲面 Hodge 菱形的 5 列 array 与原倒三角**逐位一致**（1 ／ 0 1 ／ 0 0 0 ／ 1 0 ／ 1）。
   - (2.2)(2.3)：`\omega\in\bigwedge^2V^*\subset V^*\otimes V^*`；块矩阵 `\begin{pmatrix}0&-I\\I&0\end{pmatrix}`。
   - (2.4)–(2.10)：三条公理、注意2.7 的 (2.8)、`X_f:=\{f,-\}`、`\beta\in\Gamma(\bigwedge^2TM)` 全部无误。
   - (3.1)–(3.4)：`\nabla V` 三个分量、`S=\int L(\bm q,\dot{\bm q})dt`、Euler–Lagrange 式、`p_i=\partial L/\partial\dot q_i` 与 `H=\sum_i\dot q_ip_i-L.` 的句点。
2. **tag 完整性**：c01 = 23 条（(1.2)–(1.23)、(2.1)），c02 = 13 条（(2.2)–(2.10)、(3.1)–(3.4)）；与 `tags_bypage.txt` 的 p002–p008 清单完全一致，不缺不重不跳。
3. **环境类型与编号**：局部编译结果——定义1.3–1.9、习题1.3–1.18、定义2.1–2.8、注2.6／注2.7、习题2.1–2.7，与原文及 STYLE_GUIDE 的计数器规则（definition/example/remark/problem 共用、exercise 独立）完全吻合。
4. **跨文件环境**：c01 末尾 `\begin{definition}`（含 (2.1)）未闭合、由 c02 首行「为单射（从而为同构）时，称 $\omega$ 非退化」闭合——编译正常，编号正确为**定义2.1**；两文件头部注释都写明了这一点，属可接受的跨块处理。
5. **接缝**：c02 首行与 c01 末 (2.1) 衔接自然无重复；c02 末 (3.4) 与 c03 首「Legendre 变换之前的 $(q,\dot q)$……」顺序衔接（对应 p9 首行），无漏译、无溢出。
6. **结构/体例**：`\section` 仅 c01「辛流形」（p5）、c02「分析力学」（p8）各一次，与 BRIEF 一致；无 `\ref`/`\cite`/markdown 粗体/脚注遗漏；引号「」保留。
7. **术语**：除「Hamilton 系」外全部与 `glossary.tsv` 一致（近复结构、近全纯映射、可积、全纯切丛、反全纯切丛、正合列、截面、对偶丛、辛同胚、近辛形式、Poisson 双向量、叶状结构、位形空间、广义坐标/速度/动量、Legendre 变换等）；「近辛流形」为 glossary 未收词，作者按「近辛形式」类推，可接受。
8. **批注**：c02 对原文 p8「Euler–Langrange 方程式」的 `% [Tutor Note: …]` 正确（原书确作 Langrange），译文写 Euler–Lagrange 并加注，处理得当，无需改动。
9. **漏译/增译**：p2（行 47 起）–p8 逐句比对，未发现漏译、误译或凭空增补；p8「例として」为行文，未误立 `example` 环境，正确。
