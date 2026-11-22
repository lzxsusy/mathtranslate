# Eisenstein 级数与尖点形式

> `lbook04/concept/ch3-eisenstein-cusp` · 轨 M 模形式与自守表示 · 状态 reviewed · 核验 source-only

**问题：** Eisenstein 级数与尖点形式在模形式空间里各自扮演什么角色，为什么必须分开？

**一句话：** Eisenstein 级数是对 $\Gamma$ 的陪集求平均得到的「连续谱」；尖点形式在 Fourier 展开中无常数项。两者构成 $M_k=S_k\oplus E_k$。

**别名：** `Eisenstein series`、`cusp form`、`尖点`

## 定义

例 3.4 说明：若函数已在子群 $G_1<G$ 下不变，只需对 $G_1$ 在 $G$ 中的陪集求平均。由此得到 Poincaré 级数 $P_m$ 与 Eisenstein 级数 $E_k(z)=\sum_{(a,b)=1}(az+b)^{-k}$；当 $m=0$ 时 $P_0$ 就是 Eisenstein 级数，$m\ne0$ 时 $P_m$ 是尖点形式。Eisenstein 级数的 Fourier 展开（例 4.2）含 $\zeta(1-k)$ 的常数项，一般不为零；尖点形式的常数项为零。于是 $M_k=S_k\oplus E_k$（尖点部分与 Eisenstein 部分直和），Petersson 内积下两部分正交。Hecke 理论在 $S_k$ 上给出正交特征基（推论 5.5），这是「离散谱」；Eisenstein 级数则对应「连续谱」，在 Rankin–Selberg 积分中作为核出现。

**记号：** $\Gamma_\infty$：$\mathrm{SL}(2,\mathbb Z)$ 的抛物子群；$P_m$：第 $m$ 个 Poincaré 级数；$E_k$：权 $k$ Eisenstein 级数；$S_k$：尖点形式空间；$M_k$：模形式空间；$\Delta$：权 $12$ 尖点形式。

## 要点

- Eisenstein 级数 = 由抛物子群诱导的表示对应的「连续谱」；它的 Fourier 常数项不为零，反映极点/常数项。
- 尖点形式 = 在所有尖点处衰减的部分；它们构成有限维空间，Hecke 算子在其上有正交特征基（推论 5.5）。
- 「尖点」不是几何点而是 $\Gamma\backslash\mathrm{H}$ 的边界点；在尖点处消失等价于该尖点处 Fourier 展开的常数项为 $0$。

## 公式

$$
E_k(z)=\sum_{(a,b)=1}\frac{1}{(az+b)^{k}}=\sum_{\gamma\in\Gamma_\infty\backslash\Gamma}\gamma\cdot z^{-k}
$$

$$
\Delta(z)=q\prod_{n\ge1}(1-q^{n})^{24}=\sum_{n\ge1}\tau(n)q^{n},\qquad q=e^{2\pi iz}
$$

$$
M_k=S_k\oplus E_k
$$

## 易错点

- 把「尖点形式」等同于「在 $\infty$ 处消失」：必须在所有尖点处消失；对 $\Gamma_0(q)$，各尖点的宽度不同，Fourier 展开要按伸缩矩阵 $\sigma_a$ 逐点写。
- 把 Eisenstein 级数的常数项当成 $0$：它含 $\zeta(1-k)$（例 4.2），一般非零；这正是 Eisenstein 部分与尖点部分的判别标志。

## 批注

**〔易错预警〕两种 q**　模形式里的 $q=e^{2\pi iz}$（局部坐标）与 level 的 $q$ 是同一个字母，书中专门出注提醒；读公式时先看 $q$ 出现在 $e(\cdot)$ 里还是 $\Gamma_0(q)$ 里。这个混淆在第 3 章反复出现。

**〔背景直觉〕Eisenstein = 诱导表示**　例 3.4 把 Eisenstein 级数写成对陪集 $\Gamma_\infty\backslash\Gamma$ 的平均；表示论上这就是从抛物子群的平凡表示诱导。尖点形式则是「离散谱」，与 Eisenstein 的连续谱在 Petersson 内积下正交——这正是谱分解 $L^2(\Gamma\backslash\mathrm{H})=L^2_{\mathrm{cusp}}\oplus L^2_{\mathrm{Eis}}$ 的经典情形。

## 相关

[[ch3-three-motives]]、[[ch3-hecke-operators]]、[[ch3-modular-l]]

## 来源

- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§3，原书 pp. 43–45（PDF pp. 50–52）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch03.tex:300-330`
- Bernstein–Gelbart 编《朗兰兹纲领导论》（An Introduction to the Langlands Program），Birkhäuser 2004，§4.2，原书 pp. 52–54（PDF pp. 59–61）
  - 锚点：`08_source_code/SY02-24_朗兰兹纲领导论_全书中文译注/源码/chapters/ch03.tex:455-495`
