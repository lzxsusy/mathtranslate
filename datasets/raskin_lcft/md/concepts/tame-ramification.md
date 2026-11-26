# 驯分歧与单位群的范数满射

> `raskin_lcft/concept/tame-ramification` ｜ track A ｜ reviewed

**一句话**：驯分歧扩张里，单位群的范数映射是满射，因此范数判定完全落到剩余域上；这是第 3 讲能算清范数群的钥匙。

**自测**：为什么驯分歧时 O_L^× 的范数像刚好是整个 O_K^×，而不驯分歧时就不行？

## 定义

扩张 $L/K$ 称为驯分歧，若其分歧指数 $e$ 与剩余特征 $p$ 互素（$p\nmid e$）。此时 $\mathcal O_L^\times\cong\mu_{q^2-1}\times(1+\mathfrak p_L)$，范数映射 $\mathcal O_L^\times\to\mathcal O_K^\times$ 满射（断言 3.5），迹映射 $\mathcal O_L\to\mathcal O_K$ 也满射（断言 3.6）。

记号：$e=v_L(\varpi_K)$；$\mathfrak p_L$ 为极大理想；$q=\\#k$。

## 要点

- 满射性来自「$1+\mathfrak p_K$ 中的元素都能被范数打到」：$N(1+\mathfrak p_L^s)=1+\mathfrak p_K^s$（驯分歧时）。
- 一旦 $N(\mathcal O_L^\times)=\mathcal O_K^\times$，范数条件就只剩赋值条件：$x$ 是范数 ⟺ $v(x)$ 偶且单位部分是范数。
- 驯分歧是可算的边界：不驯分歧的范数群要用 Lubin–Tate 理论（第 21 讲）而不是初等分解。
- 第 3 讲的计数（$\#\ker N=q+1$）同时给出定理 3.3 与 $\chi(L^\times)=n$ 的雏形。

## 公式

N(\mathcal O_L^\times)=\mathcal O_K^\times\quad(\text{驯分歧})
\#\ker N=q+1

## 定理与证明

### 断言 3.4（范数判据的赋值化）

$x\\in K^\\times$ 是范数，当且仅当 $v_K(x)$ 为偶数且 $x$ 的单位部分属于 $N(\\mathcal O_L^\\times)=\\mathcal O_K^\\times$。

（sketch；来源：原书 p.11）


缺口：先对赋值取 $v$，再对单位部分用 3.5 的满射性。

### 断言 3.5（单位群的范数满射）

$L/K$ 驯分歧（二次）时，$N:\\mathcal O_L^\\times\\to\\mathcal O_K^\\times$ 是满射。

（sketch；来源：原书 p.12）


缺口：用 $\mu_{q^2-1}$ 与 $1+\mathfrak p_L$ 的分解分别验证。

## 易错点

- 把「驯分歧」当成「非分歧」：驯分歧允许分歧指数与剩余特征互素
- 在 $p$ 分歧（不驯）情形照搬 $1+\mathfrak p$ 的逐项计算：此时 $1+\mathfrak p_L$ 的范数像会缩小
- 把迹满射（3.6）与范数满射（3.5）混为一谈

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 3 讲 带驯分歧的范数群，p.10–13（原书 p.10）

关联：`raskin_lcft/concept/norm-group`、`raskin_lcft/concept/hilbert-symbol`、`raskin_lcft/concept/lcft-main-theorem`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
