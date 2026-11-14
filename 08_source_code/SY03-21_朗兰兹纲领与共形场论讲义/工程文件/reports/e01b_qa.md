# e01b QA（§1.5–1.7 非阿贝尔推广、$GL_2$ 自守表示与模形式、椭圆曲线与 Galois 表示）

- 规模：en 31,083 字符 → 译文 15,417 字符；段落 59/59；`$$` 44/44、equation 4/4、subsection 3/3、label 9/9、eqref 10/10、secref 2/2、cite 10/10、index 13/13、footnote 7/7。
- 数学：显示公式 27/27、行内公式 397/397 归一化后逐字符一致（`check_math.py e01b` 全 [OK]）。
- 结构：三个 `\subsection` 译作「非阿贝尔推广？」（`\label{frob}`）、「$GL_2(\AD_\Q)$的自守表示与模形式」（`\label{modularforms}`）、「椭圆曲线与 Galois 表示」（`\label{ellipticcurves}`）；标题前的四空格、`\label` 位置照抄。
- 数学环境内英文未译：两个 `\boxed{\begin{matrix}1\text{-dimensional representations}...}` 示意图依 Lead m00057 逐字符保留（含 `\text{}` 内英文）。
- 术语：自守表示、尖点自守表示、尖形式、模形式（权/水平）、Hecke 算符、球 Hecke 代数、Hecke 本征值、Frobenius 共轭类、分解群、惯性子群、非分歧、Casimir 算符、Verma 模、Harish-Chandra 对、新形式、Tate 模、导子、好约化、同源类、伴随（adjoint 未出现）、动机（motive）；`automorphic` 等按 TERMS，人名一律保留原文。
- 存疑（照录原文，未改）：① `\begin{align}` 第二行 `\rho_p(g) \cdot\rho_p` 疑应为 `\cdot v_p`；② 脚注 `$d \equiv \, \on{mod} p^{n_p} \Z_p$` 中 `\equiv` 后疑脱 `1`；③ 行文 `$GL_1(Q_p)$` 中 `Q_p` 疑脱反斜杠（应为 `\Q_p`）；④ `(growth) $f$ is bounded on $GL_n(\AD)$` 疑应为 `GL_2`；⑤ `it can shown`（脱 be）、`the definition the Hecke operators`（脱 of）；⑥ `\on{Gal}(\ol{F}_v,F_v)` 用逗号，与 `\on{Gal}(\ol{k}_v/k_v)` 的斜杠不一致。
- 自检：无 `\section`/`\begin{document}`；UTF-8；中文全角标点、中文与公式间无空格；正文无裸露 `& % # _`；无 `% ZHU-CAND`。
