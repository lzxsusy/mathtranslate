# Fourier–Mukai 复合等于卷积

> `functoriality/deriv/fm-composition` ｜ track B ｜ draft

**目标**：重构命题 thm:3.5（[Huy06] 命题 5.10 / [Muk81] 命题 1.3）的推理：$\Phi_{\mathscr P}:D^b(X)\to D^b(Y)$ 与 $\Phi_{\mathscr Q}:D^b(Y)\to D^b(Z)$ 复合后仍是 Fourier–Mukai 变换，核由 $\mathscr R={\pi_{XZ}}_*\bigl(\pi_{XY}^*\mathscr P\otimes\pi_{YZ}^*\mathscr Q\bigr)$ 给出。

**自测**：为什么 Fourier–Mukai 变换的复合可以写成核的卷积，这一步在辛侧的对应物是什么？

## 前提

- $X,Y,Z$ 为光滑射影簇；$D^b(-)$ 取凝聚层有界导出范畴（dg 增强，以得到函子层面的复合）。
- $\mathscr P\in D^b(X\times Y)$、$\mathscr Q\in D^b(Y\times Z)$ 为 Fourier–Mukai 核；$p,q$ 分别表示到两个因子的投影。
- $\pi_{XY},\pi_{YZ},\pi_{XZ}$ 表示 $X\times Y\times Z$ 到相应二重乘积的投影。

## 步骤

1. **FM 变换的定义：$\Phi_{\mathscr P}(\mathscr E^\bullet)=p_*(q^*\mathscr E^\bullet\otimes\mathscr P)$，即先拉回、再与核作张量、最后推出。**  
   为什么：这三步正是「沿对应搬运层」的代数版本；辛侧的 $\Phi_{L_{12}}$ 对应「沿拉格朗日对应搬运拉格朗日」。  
   锚点：原书 p.20 §3.2（证据 A）

2. **把 $\Phi_{\mathscr Q}(\Phi_{\mathscr P}(\mathscr E^\bullet))$ 展开：先对 $\mathscr P$ 作 $q^*\otimes\mathscr P$ 再 $p_*$ 到 $Y$，随后对 $\mathscr Q$ 重复同一操作，得到先在 $X\times Y$ 上、再在 $Y\times Z$ 上的两次搬运。**  
   为什么：把两次搬运合并到三重乘积 $X\times Y\times Z$ 上，是把「复合」写成单一核的关键一步。  
   锚点：原书 p.20 §3.2（证据 B）

3. **用投影公式与平坦基变换把中间的 $Y$ 方向消去：先在 $X\times Y\times Z$ 上取 $\pi_{XY}^*\mathscr P\otimes\pi_{YZ}^*\mathscr Q$，再沿 $\pi_{XZ}$ 推出，即得 $\mathscr R$。**  
   为什么：这一步是标准 FM 复合计算：$p_*$ 与张量积交换（投影公式）使中间变量被纤维化掉。  
   锚点：原书 p.20 §3.2（证据 B）

4. **得到 $\Phi_{\mathscr Q}\circ\Phi_{\mathscr P}\cong\Phi_{\mathscr R}$，且 $\mathscr R$ 由上式给出；特别地复合的核只依赖两个核的卷积，不依赖具体的层。**  
   为什么：这正是命题 thm:3.5 的陈述；它说明 FM 变换在「核 = $X\times Y$ 上的对象」与「函子」之间是封闭的。  
   锚点：原书 p.20 §3.2（证据 A）

5. **与辛侧对照：MWW 的 (50) 说 $\Phi^\#_{L_{12}}\circ\Phi^\#_{L_{01}}\simeq\Phi^\#_{L_{01}\circ L_{12}}$，即「复合的函子 = 复合对应的函子」，形式上与 FM 复合定理同型。**  
   为什么：这是原文明确指出的类比（「与 thm:3.5 比较」）；但辛侧只到 $A_\infty$-同伦，且需要嵌入复合等假设，不能把代数侧的严格同构直接搬过来。  
   锚点：原书 p.21 §3.3（证据 C）

## 结果

$\Phi_{\mathscr Q}\circ\Phi_{\mathscr P}\cong\Phi_{\mathscr R}$，其中 $\mathscr R={\pi_{XZ}}_*\bigl(\pi_{XY}^*\mathscr P\otimes\pi_{YZ}^*\mathscr Q\bigr)$；复合对应核的卷积，是 MWW 复合定理 (50) 的代数原型。

## 缺口

- 原文只陈述命题并引用 [Huy06] 5.10 / [Muk81] 1.3，未给推导；步骤 2–3 的投影公式与基变换细节是按标准 FM 论证补出的（B）。
- 严格来说 $D^b$ 需要 dg 增强才能在函子层面谈复合与自然同构；原文在 §3.1 提到这一点但没有展开。
- 辛侧类比只是形式类比：代数侧是严格同构且无单调性假设，辛侧只得到 $A_\infty$-同伦且需嵌入复合与单调性。

## 易错点

- 把卷积核写成 $\mathscr P\otimes\mathscr Q$：两个核在不同的乘积空间上，必须先分别拉回到 $X\times Y\times Z$ 再张量，最后沿 $\pi_{XZ}$ 推出。
- 忘记 ${\pi_{XZ}}_*$ 是导出推出：在非光滑或非投影情形需要额外技术，不能当作普通层推前。
- 把「FM 复合 = 卷积」直接当成辛侧已证结论：辛侧 (50) 是 $A_\infty$-同伦，且需要膜结构、可容许、嵌入复合等假设。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§3.2，p.20–20（原书 p.20–20 §3.2）

关联：`functoriality/concept/fourier-mukai`、`functoriality/concept/derived-category-coherent`、`functoriality/deriv/mww-composition`、`functoriality/concept/orlov-theorem`

来源说明：原书 p.20 §3.2（FM 变换定义、复合命题）；推导骨架据 [Huy06] 5.10 的标准论证重写，公式取自中译本 chapter3.tex。
