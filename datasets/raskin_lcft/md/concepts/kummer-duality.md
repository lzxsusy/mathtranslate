# Kummer 理论与范数群的存在定理

> `raskin_lcft/concept/kummer-duality` ｜ track D ｜ reviewed

**一句话**：当 μ_n ⊆ K 时，(K^×)^n 是范数群，K^×/(K^×)^n 与 n 挠群对偶；这条对偶是存在定理（18.2）的引擎。

**自测**：为什么「μ_n 在 K 里」能让 (K^×)^n 一定是范数群？没有 μ_n 时缺的是什么？

## 定义

设 $K$ 含 $n$ 次单位根群 $\mu_n$（且 $\mathrm{char}\,K\nmid n$）。Kummer 理论给出配对 $K^\times/(K^\times)^n\times\mu_n\to\mu_n$（由 $\sqrt[n]{x}$ 的作用）；由此证明 $(K^\times)^n$ 是范数群（推论 18.7），并在无 $\mu_n$ 的一般情形用「有限层 + 逆向极限」把存在定理补全（18.2）。

记号：$K^\times/(K^\times)^n\ \leftrightarrow\ \operatorname{Hom}(\mu_n,\mu_n)$。

## 要点

- $\mu_n\subseteq K$ 时，$n$ 次幂群恰是「Kummer 扩张」的范数群，这一步是纯代数（Kummer 配对 + 90）。
- 无 $\mu_n$ 时不能直接做：要先取 $L=K(\zeta_n)$，在 $L$ 上做，再用 $G$-模的范数下降。
- 断言 18.6 的「$n$ 挠群对偶计数」是把有限群对偶搬到 $K^\times/(K^\times)^n$ 上的技术前提。
- 存在定理（18.2）由此完成：任给闭有限指数 $\Gamma$，取 $n$ 使其含 $K^{\times n}$，再用 Kummer 判定它落在范数群里。

## 公式

K^\times/(K^\times)^n\ \cong\ \operatorname{Hom}(\mu_n,\mu_n)\quad(\mu_n\subseteq K)
\mu_n\subseteq K\implies (K^\times)^n\ \text{是范数群}

## 定理与证明

### 推论 18.7（(K^×)^n 是范数群）

若 $\mu_n\subseteq K$，则 $(K^\times)^n$ 是某有限阿贝尔扩张的范数群（即 $K^\times/(K^\times)^n$ 的 Kummer 对偶扩张）。

（sketch；来源：原书 p.78）


缺口：用 Kummer 配对把 $(K^	imes)^n$ 识别成 $\operatorname{Hom}$ 的核，再对偶回范数群。

### 断言 18.6（n 挠群的对偶计数）

若 $A$ 是 $n$-挠有限阿贝尔群，则 $\#A=\#\operatorname{Hom}(A,\mathbb Z/n\mathbb Z)$。

（complete；来源：原书 p.78）

1. 把 $A$ 拆成 $\mathbb Z/d\mathbb Z$ 的直和（$d\mid n$）。  
   为什么：有限阿贝尔群的基本定理，且 Hom 与直和交换。
2. 对 $A=\mathbb Z/d\mathbb Z$ 算 $\operatorname{Hom}(\mathbb Z/d\mathbb Z,\mathbb Z/n\mathbb Z)=(\mathbb Z/n\mathbb Z)[d]$，阶为 $d$。  
   为什么：同态由 $1$ 的像决定，像必须被 $d$ 杀掉。
3. 两边都乘性，故一般情形成立。  
   为什么：直和分解与阶的乘性。

## 易错点

- 把 μ_n ⊆ K 当成自动成立：p 进域在 n=p 时会失效
- 把 (K^×)^n 与 K^×/K^{×n} 弄混：前者是「n 次幂」，后者是「模 n 次幂」
- 在无限扩张上直接引用有限群的对偶：要先用投射有限上同调

## 参考与关联

- Raskin, Lectures on Cohomological Class Field Theory (MIT 18.786, Spring 2016; notes by Oron Propp)，第 18 讲 范数群与 Kummer 理论，p.76–80（原书 p.76）

关联：`raskin_lcft/concept/norm-group`、`raskin_lcft/concept/hilbert-theorem-90`、`raskin_lcft/concept/vanishing-theorem`

来源说明：卡由中译本的数学内容改写，不含底本原文；页码为底本印刷页。
