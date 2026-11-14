# 第 9 章上半 审校记录（review_ch09a.md）

范围：原书第 9 章 *Hard Stories on Lagrangians* 前半（9.1--9.3），印刷页 231–249，
扫描 PDF 第 239–257 页。9.4--9.7 由另一译者续写（ch09b）。

处理原则：译文**保留原文写法**并就地加 `% [Tutor Note: ...]` 说明；下表列出原文、
页码、疑点与建议改法。标记「确信」者为可确定之笔误，「待核」者需对照作者原稿确认。

| # | 位置（印刷页 / PDF 页） | 原文 | 疑点 | 建议改法 | 把握 |
|---|---|---|---|---|---|
| 1 | p.231 / p.239，章首导语 | "Often this provides surprisingly results" | 副词误作形容词 | "surprising results" | 确信 |
| 2 | p.235 / p.243，(ii) | "via the stereographic projection define by" | 语法笔误 | "defined by" | 确信 |
| 3 | p.235 / p.243，(i)--(ii) | "disk $B^2(2)$ ... with radius $\sqrt2$"，随后又写 $B^2(\sqrt2)$ | 同一对象两种记号 | 统一为半径 $\sqrt2$ 的圆盘记号（并据 (1.13) 核对 $B^2(r)$ 的确切定义） | 待核 |
| 4 | p.238 / p.246，例 9.2.2 | "It can be viewed it as an $A_\infty$-algebra" | 多一个 it | "It can be viewed as" | 确信 |
| 5 | p.239 / p.247，(9.15) | $\sum_{l_0,\cdots,l_k\geqslant0} m_{\cdots}(b^{\otimes l_1}\otimes x_1\otimes\cdots\otimes x_k\otimes b^{\otimes l_k})$ | 求和指标 $l_0,\cdots,l_k$ 共 $k+1$ 个，但单项式中只出现 $b^{\otimes l_1},\cdots,b^{\otimes l_k}$ 共 $k$ 个，$l_0$ 未出现 | 写成 $b^{\otimes l_0}\otimes x_1\otimes b^{\otimes l_1}\otimes\cdots\otimes x_k\otimes b^{\otimes l_k}$（或把指标改为 $l_1,\cdots,l_{k+1}$） | 待核 |
| 6 | p.239 与 p.240 / p.247 与 p.248，(9.16) | 两处均编号 (9.16) | 公式编号重复（p.239 末的展开式与 p.240 的 Maurer--Cartan 方程） | 其一改为 (9.17)，其后编号顺延；或在重印时修正 | 确信 |
| 7 | p.239 / p.247，(9.16) | 展开式末两行均含 $m_2(m_2(b\otimes x)\otimes b)$ | 同一项重复出现，且缺少按 $\hat m_1^b$ 展开应出现的 $m_2(b\otimes m_2(x\otimes b))$ | 核对 $m_2(b\otimes m_2(x\otimes b))$ 与 $m_2(m_2(b\otimes x)\otimes b)$ 两项 | 待核 |
| 8 | p.240 / p.248，(9.16) 的改写式 | 改写式与 (9.16) 逐项对照 | 改写式似漏掉 $m_2(m_2(b\otimes x)\otimes b)$、$m_2(b\otimes m_2(x\otimes b))$ 型项，且 $m_2(m_1(x)\otimes b)$ 只出现一次 | 逐项重算（建议按 $m_1(m_2(b\otimes x)+m_2(x\otimes b))$ 的 Leibniz 展开重排） | 待核 |
| 9 | p.240 / p.248，注 9.2.3 | $m_0(1)+m_1(b)+m_2(b,b)+\cdots$ | $m_2$ 的定义域是 $C\otimes C$，应写 $m_2(b\otimes b)$ | 改为 $m_2(b\otimes b)$ | 确信 |
| 10 | p.246 / p.254，(iv) 的开头 | "define the the following subset" | 多一个 the | "the following subset" | 确信 |
| 11 | p.246 / p.254，(9.23) | $\operatorname{supp}(H)\in[0,1]\times M\setminus R_L$ | 支撑集是集合，不能用 $\in$ | 改为 $\operatorname{supp}(H)\subset[0,1]\times M\setminus R_L$ | 确信 |
| 12 | p.248 / p.256，定理 9.3.1 的证明 | "the map $\widehat\Phi:\R^{2n}\to R_L$ defined by $\widehat\Phi(t_1,\cdots,t_n):=\cdots$" | 自变量只有 $n$ 个，定义域应为 $\R^n$；像落在 $R_L\subset L$ | 改为 $\widehat\Phi:\R^n\to R_L$（或 $\R^n\to M$） | 确信 |
| 13 | p.248 / p.256，定理 9.3.1 的证明 | "choose local coordinates $(x_1,\cdots,x_{2n})$ around $x$ such that $x_i\notin L^n$ for $i=1,\cdots,n$" | 字面不通：$x_i$ 是坐标函数，不能与子流形 $L^n$ 作「属于/不属于」比较。按图 9.7 与证明用途，应指这 $n$ 个坐标方向在 $x$ 处横截于 $L$ | 建议改为「使 $\partial/\partial x_1,\cdots,\partial/\partial x_n$ 与 $T_xL$ 一起张成 $T_xM$」或等价的横截性条件 | 待核 |
| 14 | p.248 / p.256，定理 9.3.1 的证明末 | "is non-degenerate.." | 双句点 | 删去多余句点 | 确信 |

## 已核对但判为无误的易混点

- (9.9) 中第二个矩阵为 $\operatorname{diag}(-1,-1,1)$，与 $R_{-s}$ 的关系
  $D R_s=R_{-s}D$ 成立（因 $d_3=-d_2$），故 (9.9) 无误。
- (9.3) 的 $\omega_{S^2}(v,w)=\langle p,v\times w\rangle$ 是单位球面标准面积形式；
  $B^2(2)$（半径 $\sqrt2$）的面积 $2\pi$ 与 $(S^2,\tfrac12\omega_{S^2})$ 的总面积一致，
  (ii) 的嵌入确为等面积同构（二维时等面积即辛同胚）。
- 事实 9.2.1 的包含方向为 $\mathcal M_{\mathrm{weak}}(\mu^{-1}(x))\supset H^1(\cdots)$，
  不是 $\subset$（弱界定上链的集合更大），原文无误。
- (9.18) 中 $v_i$ 为内法向量，故 $l_i(x)\geqslant0$（$x\in\Omega$），$T^{l_i(x)}$ 属于
  $\Lambda^{\mathbf{k},\Gamma_\omega}_{\geqslant0}$，与例 9.2.4 的显式计算一致。
- 例 9.2.4 中 $(0.5,0.5)$ 处四个超平面给出 $l_i=1/2$，故势函数四项均带 $T^{1/2}$，
  与原文一致。

## 体例说明（非原文疑误）

例 9.2.3（相对 Gromov–Witten 不变量）在原文中从 p.240 延续到 p.242，其间夹有
定理 9.2.1 与「Roughly speaking……」一段，段末以 `//` 结束。若把定理 9.2.1 置于例内
将造成环境嵌套上的混乱，故译文把例 9.2.3 收在 p.241 末「……在 $L$ 本身上进行的」处，
其后「为借助 $^{\mathrm{rel}}\mathrm{GW}_{\beta,k}$ 构造 $A_\infty$-代数……」一段
按正文处理，段末的 `//` 以 $\square$ 呈现。此系排版取舍，不影响文字内容。

## 编号核对- 公式编号 (9.1)–(9.25) 齐全；其中 (9.16) 在原文出现两次（见上表 #6）。译文中
  p.239 末的展开式用 `\tag{9.16}`，p.240 的 Maurer–Cartan 方程用 `\tag*{(9.16)}`
  以忠实呈现原文编号、同时避免 LaTeX 标签重复。
- 定理类编号：9.1 节 7 项、9.2 节 15 项（含事实 9.2.1、9.2.2）、9.3 节 16 项，
  共 38 项，均按原文标号。

## 图目录（300 dpi 裁自扫描页，置于 qsg/figures/）

| 文件 | 原书位置 | 说明 |
|---|---|---|
| `fig_p243_1.png` | p.235 | 图 9.1 $\{\varphi_G^t(p)\}$ 在 $S^2\times S^2$ 中的轨道 |
| `fig_p243_2.png` | p.235 | 图 9.2 半圆盘内的闭曲线 $\Gamma$ |
| `fig_p249_1.png` | p.241 | 图 9.3 带 $k$ 个标记点的 $J$-全纯圆盘 |
| `fig_p251_1.png` | p.243 | 图 9.4 由方程确定的超平面 |
| `fig_p252_1.png` | p.244 | 图 9.5 $(S^2\times S^2,\omega_{\mathrm{prod}})$ 矩像中的超平面 |
| `fig_p254_1.png` | p.246 | 图 9.6 经 $\varphi^{-1}$ 作用 |
| `fig_p256_1.png` | p.248 | 图 9.7 $M^{2n}$ 上的坐标与 $L^n\subset M^{2n}$ |
