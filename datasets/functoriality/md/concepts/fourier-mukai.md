# Fourier–Mukai 变换

> `functoriality/concept/fourier-mukai` ｜ track B ｜ draft

**一句话**：以乘积上的对象 P 为核，先沿第一投影拉回、再与核张量、最后沿第二投影推出，得到 D^b(X) 到 D^b(Y) 的函子。

**自测**：Fourier–Mukai 变换为什么必须按「拉回—张量—推出」这三步组合，核又怎样编码复合？

## 定义

对 $X\times Y$ 上的凝聚层 $\mathscr P$，Fourier–Mukai 变换定义为 $\Phi_{\mathscr P}(\mathscr E^\bullet)=p_*(q^*\mathscr E^\bullet\otimes\mathscr P)$：先沿第一因子的投影把 $X$ 上的层拉回到乘积 $X\times Y$，把结果与核 $\mathscr P$ 作张量积，最后沿第二投影推出到 $Y$。复合由核的卷积描述：若 $\mathscr P\in D^b(X\times Y)$、$\mathscr Q\in D^b(Y\times Z)$，取 $\mathscr R:={\pi_{XZ}}_*(\pi_{XY}^*\mathscr P\otimes\pi_{YZ}^*\mathscr Q)$，则 $\Phi_{\mathscr Q}\circ\Phi_{\mathscr P}$ 自然同构于 $\Phi_{\mathscr R}$（命题 3.5）。

记号：$p:X\times Y\to Y$ 与 $q:X\times Y\to X$ 是两个投影；$\pi_{XY},\pi_{YZ},\pi_{XZ}$ 是三重积上的投影；核 $\mathscr P$ 是乘积上的对象。

## 要点

- 核编码整个函子：Orlov 定理说（带伴随的）函子都由某个核给出，因此「函子」与「乘积上的对象」是同一件事。
- 三步缺一不可：必须在乘积上才能把层与核张量；先拉回再张量最后推出，方向由两个投影决定。
- 复合是核的卷积 (48)，不是张量 $\mathscr P\otimes\mathscr Q$，也不是某个映射的复合。
- 这是辛侧 $\Phi_\Lambda$ 的模板：拉格朗日对应 $\Lambda$ 替代核 $\mathscr P$，拼接曲面上的计数替代张量与推出。

## 公式

$\Phi_{\mathscr P}:D^b(X)\longrightarrow D^b(Y),\qquad \mathscr E^\bullet\longmapsto p_*(q^*\mathscr E^\bullet\otimes\mathscr P),$
$\mathscr R:={\pi_{XZ}}_*\bigl(\pi_{XY}^*\mathscr P\otimes\pi_{YZ}^*\mathscr Q\bigr).$

## 定理与证明

### Fourier–Mukai 变换的复合

设 P∈D^b(X×Y)、Q∈D^b(Y×Z)，并令 R 为核的卷积（48）。则复合 Φ_Q∘Φ_P 自然同构于 Φ_R。

（none；来源：原书 p.20 §3.2）


缺口：原文只陈述命题并引 Huybrechts 命题 5.10 与 Mukai 的原始表述，未给投影公式的推导；证明需在乘积上反复用投影公式与平坦基变换。

### 核表示函子

在 Orlov 定理的假设下，每个有左右伴随的全忠实正合函子 F 都同构于某个 Φ_P，且 P 在同构意义下唯一。

（none；来源：原书 p.20 §3.2）


缺口：原文引 Orlov 定理 2.2；本卡只记录结论，核的构造在 Orlov 原文。

## 易错点

- 把核写成 X 或 Y 上的层：核是乘积 X×Y 上的对象，它同时携带两侧的几何。
- 把 FM 的复合写成普通函子复合或核的张量：正确公式是卷积 (48)，含三个投影与一次推出。
- 把拉回与推出的投影写反：$q$ 是到 $X$ 的投影、$p$ 是到 $Y$ 的投影，写反会得到反方向的函子。
- 以为 FM 变换总是等价：只有核满足额外条件（如核为 Poincaré 丛且维数匹配）时才是等价，Orlov 定理讲的是函子的表示而非可逆性。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§3.2，p.20–20（原书 p.20 §3.2）

关联：`functoriality/concept/orlov-theorem`、`functoriality/concept/derived-category-coherent`、`functoriality/deriv/fm-composition`、`functoriality/concept/mww-functor`

来源说明：原书 p.20 §3.2；公式 (46)(48) 逐字取自中译本 chapter3.tex。
