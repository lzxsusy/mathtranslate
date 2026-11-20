# GNO 对偶

- **id**：`gw06/concept/gno-duality`
- **类型**：concept
- **位置**：附录A
- **问题**：为什么把磁荷放进余根格、电荷放进权格，就得到另一个紧李群，并使电磁对偶成为群的对偶？

> GNO 对偶把规范群 G 的电荷格与磁荷格互换，得到对偶群 ^LG；两群共享外尔群，中心与基本群互换。

## 定义

GNO 对偶断言：对每个紧李群 $G$（根系 $\Phi$、根格 $\Lambda_\rt$、权格 $\Lambda_\wt$），存在紧李群 $^LG$，其根系为 $\Phi^\vee=\{\mu^\vee=2\mu/(\mu,\mu)\}$，且 $\Lambda_\rt({}^LG)=\Lambda_\cort(G)$、$\Lambda_\wt({}^LG)=\Lambda_\cowt(G)$。出发点是狄拉克量子化：电、磁荷的配对必须取整，即对一切根 $\nu$ 与余根 $\mu^\vee$ 有 $\langle\nu,\mu^\vee\rangle=\mu^\vee(\nu)=2(\nu,\mu)/(\mu,\mu)\in\mathbb{Z}$（式 (A.1)、(A.4)）。因此磁荷自然取值于 $\Lambda_\cort$，电荷取值于 $\Lambda_\wt$；把这两个格互换、再把 $\Phi$ 换成 $\Phi^\vee$，就得到 $^LG$，并在群层面完成 $S$-对偶。两群的李代数未必同构，但外尔群相同，因为余根只是根的正倍数；同一个对偶群也可以对应多个 $G$，它们由 $\Lambda_\char$ 的中间取值区分。物理上，$G$ 规范理论中的 't Hooft 磁单极荷正是 $\Lambda_\cort$ 的元素，而 Wilson 线按 $\Lambda_\wt$ 标号；$S$-对偶交换两者，在群论上就是把 $G$ 换成 $^LG$。

**记号**：$\Phi$：根系；$\mu^\vee=2\mu/(\mu,\mu)$：余根；$\Lambda_\rt$：根格；$\Lambda_\cort$：余根格；$\Lambda_\wt$：权格；$\Lambda_\cowt$：余权格；$^LG$：GNO 对偶群；$\langle\nu,\mu\rangle$：与度规归一化无关的配对。

## 关键点

- 狄拉克量子化就是式 (A.1) 的整性 $\langle\nu,\mu\rangle\in\mathbb{Z}$；它只依赖配对 $\langle~,~\rangle$，不依赖度规的归一化（式 (A.4)）。
- 两群共享外尔群：$\mu\langle\nu,\mu\rangle=\mu^\vee\langle\nu,\mu^\vee\rangle$，故关于 $\mu$ 与关于 $\mu^\vee$ 的反射相同，$\mathcal{W}(G)=\mathcal{W}({}^LG)$。
- 中心与基本群互换：$\pi_1({}^LG)=\mathcal{Z}(G)^\vee$、$\mathcal{Z}({}^LG)=\pi_1(G)^\vee$（式 (A.15)）；故单连通 $G$ 的对偶是伴随型。
- 对偶群只由特征格 $\Lambda_\char$ 决定：$\Lambda_\char=\Lambda_\wt$ 给出单连通 $G$，$\Lambda_\char=\Lambda_\rt$ 给出伴随型，中间取值给出其余有限商（式 (A.6)）。
- 对偶是自反的：$\Phi^\vee$ 的根系就是 $\Phi$，两对格再换一次即回到原处，故 $({}^LG)^L\neg G=G$（式 (A.6)、(A.7) 的对偶性）。

## 公式

```latex
\langle\nu,\mu\rangle ={2(\nu,\mu)\over (\mu,\mu)}
```
```latex
\mu^\vee={2\mu\over (\mu,\mu)}
```
```latex
\Lambda_\cochar={\rm Hom}({}^L\neg\TT,U(1))={\rm Hom}(U(1),\mathbb{T})
```

## 定理

**对偶根系统仍是根系**：对任意根系 $\Phi$，向量集 $\Phi^\vee=\{\mu^\vee=2\mu/(\mu,\mu)\}$ 满足与 $\Phi$ 相同的三条公理，因此可作为某个紧李群的根系——这就是 GNO 对偶群的存在性依据。

证明：sketch（式 (A.3) 后的“简短计算”，见锚点区间；展开见该处 [含糊点拨] 译注。）

1. $\mu^\vee$ 是 $\mu$ 的正倍数，故 $\Phi^\vee$ 中 $\mu^\vee$ 的倍数恰为 $\pm\mu^\vee$。 —— 由 $\mu^\vee=2\mu/(\mu,\mu)$ 直接得到，正实数的缩放不改变倍数关系（式 (A.3) 后一句）。
2. $\langle\nu^\vee,\mu^\vee\rangle=\langle\mu,\nu\rangle\in\mathbb{Z}$。 —— 代入定义并用 $(\nu^\vee,\mu^\vee)=4(\nu,\mu)/((\nu,\nu)(\mu,\mu))$，得 $2(\nu,\mu)/(\nu,\nu)$，即交换变元后的整性。
3. $\nu^\vee-\langle\nu^\vee,\mu^\vee\rangle\mu^\vee=(\nu-\langle\nu,\mu\rangle\mu)^\vee$，故 $\Phi^\vee$ 在自身反射下封闭。 —— 同一代入即得，说明反射公式在 $\Phi$ 与 $\Phi^\vee$ 中形式一致。

## 常见错误

- 把磁荷放进 $\Lambda_\wt$（或把电荷放进 $\Lambda_\cort$）：'t Hooft 荷与 $\pi_1(G)$ 的扭结被漏掉，$SU(N)$ 的对偶会被算成 $SU(N)$ 而不是 $PSU(N)$。
- 以为对偶只依赖李代数：$\Lambda_\char$ 不同则群不同（$SU(N)$ 与 $PSU(N)$ 同李代数不同群），忽略这点会把两个不同的对偶群混为一谈。
- 把 $\mu^\vee$ 当成 $\eurme$ 里的根：$\mu^\vee$ 落在 $\eurme^\vee$，只有单根系取 $(\mu,\mu)=2$ 时才与 $\mu$ 重合；否则像 $\mu\to\mu^*$ 这一步不能省。

## 批注

### 易错预警：单连通不等于自对偶

$SU(N)$ 单连通，但它的对偶是 $PSU(N)$，并不自对偶；判据是 $\pi_1({}^LG)=\mathcal{Z}(G)^\vee$（式 (A.15)）。把“单连通”误当成“自对偶”，就会以为 $SU(N)$ 的 't Hooft 荷与 Wilson 荷标号相同，从而把 $S$-对偶错写成 $G\to G$。正确的读法是先取 $\mathcal{Z}(G)^\vee$ 再回读 $\pi_1({}^LG)$；两群阶相同并不等于群相同；阶相同只说明有限群大小相同，配对结构可能不同。

### 含糊点拨：配对的次序

式 (A.1) 的 $\langle\nu,\mu\rangle$ 只对第一个变量线性，第二个位置是“根”。检验 $\Phi^\vee$ 的公理时须以 $\mu^\vee$ 为根，两个变元角色互换，得到 $\langle\nu^\vee,\mu^\vee\rangle=\langle\mu,\nu\rangle$；次序记反会把整性条件写成非整数。注意式 (A.1) 中第二个变元已被缩放，故 $\langle\nu,\mu\rangle$ 一般不是对称双线性型，整性命题都要按这个次序读。

### 背景直觉：朗兰兹对偶的群论骨架

几何朗兰兹把 $G$ 的希格斯丛与 $^LG$ 的局部系统对应起来，其群论基础正是这里的 $\Phi\leftrightarrow\Phi^\vee$：根与余根互换、权格与余权格互换。若不把 GNO 对偶的格对应先搞清楚，就无法解释对偶侧为什么出现 $\Lambda_\cowt$ 而不是 $\Lambda_\wt$；若把这两个格对调，希格斯场与局部系统的层级也会颠倒。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 附录 A；印刷页 [145, 147] / PDF 页 [146, 148]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/sA-duality.tex:11-110`
- 式 (A.1)–(A.9)：狄拉克量子化、对偶根系统与两对格；印刷页 145–147，原文 PDF 第 146–148 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
