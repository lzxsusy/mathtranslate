# 磁本征膜的赫克本征值（$U(1)$ 与 $SU(N)$）

> `gtgl15/deriv/magnetic-hecke-eigenvalue` · 轨道 E · 行列式线丛与本征值 · 状态 dev · 5 步

> **要回答的问题**：为什么磁本征膜在 't Hooft 算符下的本征值与电本征膜在 Wilson 线下的本征值恰好相同？

## 一句话

由对偶把 $F$ 型膜的 Chan–Paton 丛写成 $\langle L,M\rangle$，'t Hooft 作用对应的赫克变换 $M\mapsto M\otimes\mathcal O(p)^{d}$ 给出 $\prod T^{(d_i)}\hat B=\hat B\otimes(\otimes_i L|_{p_i}^{d_i})$；非阿贝尔情形逐本征空间得到同一形式。

## 目标

计算 $U(1)$ 与 $SU(N)$ 磁本征膜在 't Hooft 算符作用下的本征值，验证与电侧一致。

## 前提

- $U(1)$：$B$ 是电侧零维膜，对偶的 $F$ 型膜 $\hat B$ 支撑在 $F\cong\mathrm{Jac}(C)$ 上，Chan–Paton 丛由 §6.4 的对偶给出 $\langle L,M\rangle$。
- 't Hooft 算符 $\prod_i T^{(d_i)}(y_i,p_i)$ 对应纤维上的赫克变换 $\Phi:M\mapsto M\otimes\otimes_i\mathcal O(p_i)^{d_i}$（由 §5.2 的 eq (5.3)）。
- 配对公式 eq (6.17)：$\langle L,M\rangle=\otimes_i L|_{q_i}^{n_i}$。

## 推导链

| # | 步骤 | 为什么 | 出处 | 可信度 |
|---|---|---|---|---|
| 1 | 由 §6.5 的对偶重述：$\mathrm{Jac}(C)$ 上零维膜（线丛 $L\to C$）的对偶 $F$ 型膜，其 Chan–Paton 丛为 $\langle L,M\rangle$（$M$ 参数化 $\mathrm{Jac}(C)$）。 | 这是 §6 配对的对偶解释。 | `A p.70` | A·原文明确写了 |
| 2 | 't Hooft 算符作用后 Chan–Paton 丛变成 $\Phi^*(\langle L,M\rangle)=\langle L,M\rangle\otimes\langle L,\otimes_i\mathcal O(p_i)^{d_i}\rangle$（eq (7.5)）。 | 赫克变换对 $M$ 是张量，配对对 $M$ 双线性。 | `A p.70 eq (7.5)` | A·原文明确写了 |
| 3 | 用 eq (6.17) 得 $\langle L,\otimes_i\mathcal O(p_i)^{d_i}\rangle=\otimes_i L\|_{p_i}^{d_i}$，故 $\prod_i T^{(d_i)}(y_i,p_i)\hat B=\hat B\otimes(\otimes_i L\|_{p_i}^{d_i})$（eq (7.6)）。 | 这给出磁本征值。 | `A p.71 eq (7.6)` | A·原文明确写了 |
| 4 | 非阿贝尔：取 ${}^Lw$ 的 $N$ 维表示，$E_{H,V}\|_{p\times x}=\bigoplus_i M\|_{q_i}$（eq (7.8)）；磁侧赫克变换 $\Phi_i(L)=L(q_i)$ 给 $\langle L(q_i),M\rangle=\langle L,M\rangle\otimes M\|_{q_i}$，求和得 $T\hat B=\hat B\otimes(\bigoplus_i M\|_{q_i})$（eq (7.10)），与电侧 eq (7.9) 相同。 | 逐本征空间的相同计算。 | `A p.73 eq (7.10)` | A·原文明确写了 |
| 5 | 更高 minuscule 权 ${}^Lw(k)$：电侧给 $\bigoplus_\alpha M\|_\alpha$（eq (7.12)），磁侧对应 $\Phi_\alpha:L\mapsto L\otimes\otimes_{i\in\alpha}\mathcal O(q_i)$，得同一形式（eq (7.13)）。 | 对偶在所有 minuscule 权上一致。 | `A p.74 eq (7.13)` | A·原文明确写了 |

## 结论

$U(1)$：$\prod_i T^{(d_i)}(y_i,p_i)\hat B=\hat B\otimes(\otimes_i L|_{p_i}^{d_i})$，与电侧 eq (7.2) 相同；非阿贝尔：$T({}^Lw;y,p)\hat B=\hat B\otimes(\bigoplus_i M|_{q_i})$，与 Wilson 侧 eq (7.9) 相同。

## 缺口

- $U(1)$ 的 $d=\sum d_i\ne0$ 情形不在 $\MH$ 内（$c_1(L)\ne0$），原文 §7.1.2 只作现象学讨论，未给完整膜范畴描述。
- 非阿贝尔的权和 $k+rN$ 可正可负；$\Delta\ne0$ 时本征值依赖 $M$ 的选择，原文 §7.2.2 承认此限制并建议取 ${}^LG=SU(N)$ 回避。

## 最容易讲错的地方

- $U(1)$ 与电侧“同一本征值”是计算结论，不是定义：两侧的膜与算符都不同，对偶才使结果一致。
- $\langle L,M\rangle$ 的配对是线丛，只有在平凡化后才能说“相等”；本征值本身的定义到同构。
- 非阿贝尔的 $E_{H,V}|_{p\times x}=\bigoplus_i M|_{q_i}$ 只在 $\varphi(p)$ 正则半单、$p$ 非分歧时成立。
- $\Delta=\sum(k_\sigma+Nr_\sigma)\ne0$ 时 Wilson 乘积的本征值不是规范不变的（原文 §7.2.2），不要忽略这个警告。

## 相关卡

[磁本征膜](../concepts/magnetic-eigenbranes.md) · [行列式线丛与配对 $\langle\mathcal L,\mathcal M\rangle$](../concepts/determinant-line-pairing.md) · [赫克修正与赫克变换](../concepts/hecke-modification.md) · [电本征膜](../concepts/electric-eigenbranes.md) · [Gerbe 与 $B$-场（离散电/磁荷）](../concepts/gerbe-bfield.md)

## 出处（印刷页）

- A p.68–71（A p.71 eq (7.6)）
- A p.73–74（A p.73 eq (7.10)）
- A p.71–73（A p.72）

> 说明：A5：eq (7.5)(7.6)(7.9)(7.10)(7.13) 均在原文 §7；B=把 $U(1)$ 与 $SU(N)$ 的计算并成同一条推导链。最没把握处：§7.1.2 的 $d\ne0$ 膜类与 §7.2.2 的 $\Delta\ne0$ 限制原文是现象学讨论，严格性未定。
