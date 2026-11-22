# 离散谱与尖点谱

> `lbook04/concept/ch8-discrete-spectrum` · 轨 T Tate 与迹公式 · 状态 reviewed · 核验 source-only

**问题：** 为什么尖点条件恰好把连续谱剔除，只留下离散的特征值？

**一句话：** $L^2(\Gamma\backslash G)$ 分解为尖点谱 $L_0^2$ 与 Eisenstein 连续谱；$L_0^2$ 由尖点形式张成，$T_\varphi$ 在其上紧，故有离散特征基（Gelfand–Graev–Piatetski-Shapiro）。

**别名：** `discrete spectrum`、`cuspidal spectrum`、`$L_0^2$`

## 定义

尖点条件 $(40)$：$\int_0^1f\bigl((\begin{smallmatrix}1&x\\0&1\end{smallmatrix})g\bigr)dx=0$ 对一切 $g$。$L_0^2(\Gamma\backslash G)$ 为满足此条件的 $L^2$ 函数闭子空间。定理 37：$T_\varphi$ 在 $L_0^2$ 上紧；定理 38：(i) $L_0^2(\Gamma\backslash\mathfrak H)$ 有 $\Delta$ 的特征基；(ii) $L_0^2(\Gamma\backslash G)$ 分解为不可约表示，$K$-有限向量速降。连续谱部分由 Eisenstein 级数张成（§8），两者在 §9 的谱展开中合成 $L^2$ 的全分解。

**记号：** $L_0^2(\Gamma\backslash G)$：尖点谱；$T_\varphi$：积分算子；$\Delta$：双曲 Laplacian；$E$：Eisenstein 边界值。

## 要点

- 尖点条件消去常数项，使紧算子论证可用；没有它，平移算子只有连续谱（$\mathbb R$ 上平移的例子）。
- 定理 37 的紧性来自 $\Gamma\backslash G$ 尖点处体积有限与 $\varphi$ 的紧支性。
- 谱分解：$L^2=L_0^2\oplus L^2_{\mathrm{Eis}}$；$L_0^2$ 的谱离散（特征值 $\lambda_j$），$L^2_{\mathrm{Eis}}$ 的谱是 $[1/4,\infty)$ 的绝对连续部分。
- 例外特征值 $\lambda\in(0,1/4)$ 对应主系列外的特征函数（定理 17），Selberg 猜想说它们不存在（算术群情形仍未完全解决）。

## 公式

$$
\int_0^1 f\bigl((\begin{smallmatrix}1&x\\0&1\end{smallmatrix})g\bigr)\,dx=0
$$

$$
L^2(\Gamma\backslash G)=L_0^2(\Gamma\backslash G)\oplus L_{\mathrm{Eis}}^2(\Gamma\backslash G)
$$

## 易错点

- 尖点形式与 $L_0^2$ 的元素：前者全纯/实解析，后者只是 $L^2$；定理 38(i) 的特征基在 $L_0^2$ 中，不一定是全纯形式。
- 例外特征值区间是 $(0,1/4)$，不是 $[0,1/4)$：$\lambda=0$ 是常数函数，不属于尖点谱。

## 批注

**〔背景直觉〕紧算子为什么给离散谱**　紧自伴算子的谱由特征值 $0$ 及收敛到 $0$ 的特征值组成，每个特征值有限重；$L_0^2$ 上 $T_\varphi$ 紧，故谱离散。反之连续谱来自非紧的平移部分。

**〔含糊点拨〕两种谱的记号**　书中用 $L_0^2$ 记尖点谱、$L^2$ 记全谱；$(55)$ 把离散和写成 $\sum_j\langle\psi,\eta_j\rangle\eta_j+\sum_i\langle\psi,\xi_i\rangle\xi_i$，连续部分写成 $\frac1{4\pi}\int\langle\psi,E(-,1/2+it)\rangle E(g,1/2+it)dt$，注意 $j=0$ 的常数函数项。

## 相关

[[ch8-eisenstein]]、[[ch8-selberg-trace]]、[[ch8-arthur-selberg]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§1，原书 pp. 153–154（PDF pp. 156–157）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch08.tex:12-109`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§8，原书 pp. 180–181（PDF pp. 183–184）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch08.tex:1397-1460`
