# ch09.tex 待注点（第 9 章，原 PDF p48–p53）

## 待注 ch09.tex:9（原 PDF p48）
- 原文：Let L^d_E ∈ D(Tor^d) be Laumon's sheaf: on the preimage of the multiplicity-free locus X^{(d),∘} ⊂ X^{(d)} under the support map Tor^d → X^{(d)} it is the symmetric descent E^{(d)} of E^{⊠d}, and globally it is its Goresky–MacPherson extension to Tor^d.
- 概念：Laumon 层（修改核 L^d_E）、无重数轨迹 X^{(d),∘}、E^{⊠d} 的对称下降 E^{(d)}、Goresky–MacPherson（中间）延拓。
- 读者缺什么：一句话里压了三个未解释的操作——为何要在无重数轨迹上取 E^{⊠d} 的 S_d-对称下降、为何要把这个局部定义整体延拓到 Tor^d（取 Goresky–MacPherson 延拓）、这个层与 §9.4 Cauchy 分解中的 Schur 函子 S_μ 是什么关系。
- 建议来源：nLab “Laumon sheaf”；原书文献 [Gai16b]

## 待注 ch09.tex:46（原 PDF p49）
- 原文：It is understood as the colimit of the powers X^I along surjections. The factorization category Rep(Ǧ)_Ran has fiber ⊗_{x∈I} Rep(Ǧ) over a finite set I ⊂ X, with fusion when points collide.
- 概念：Ran 空间 Ran(X)、沿满射的余极限、因子化范畴 Rep(Ǧ)_Ran、碰撞点处的融合（fusion）。
- 读者缺什么：为何取“沿满射”的余极限而不是通常的 X^I、纤维写成张量积 ⊗ 而非积 ∏、“融合”具体是什么相容同构；不弄清这三点，§9.3 的幺半作用和定理 9.3.2 都读不下去。
- 建议来源：nLab “Ran space”；nLab “factorization algebra”

## 待注 ch09.tex:74（原 PDF p50）
- 原文：Sym^d(St_m ⊗ E_x) ≃ ⊕_{μ⊢d, ℓ(μ)≤min(m,r)} S_μ(St_m) ⊗ S_μ(E_x)
- 概念：Cauchy 分解（Cauchy 恒等式）、Schur 函子 S_μ（μ⊢d 对应 S_d 的不可约表示）、分拆长度 ℓ(μ) 与截断 ℓ(μ)≤min(m,r)。
- 读者缺什么：不知道 S_μ 是 Schur 函子、μ⊢d 与 ℓ(μ) 的含义，也不清楚截断 min(m,r) 为何出现（m 与 rank r 都限制分拆长度）；随后一句“不变空间”的说法因此也读不懂。
- 建议来源：nLab “Schur functor”

## 待注 ch09.tex:105（原 PDF p51）
- 原文：Up to the standard shifts, Av^{-d}_{E*} is both the left and the right adjoint of Av^d_E, and Verdier duality gives 𝔻 ∘ Av^{-d}_{E*} ≃ Av^d_E ∘ 𝔻.
- 概念：下修改函子 Av^{-d}_{E*}、左右伴随、Verdier 对偶 𝔻、自伴随性。
- 读者缺什么：作者用“同时是左、右伴随”一步推出 $F=0$（见 ch09.tex:109 的 Hom 计算），读者若不知道伴随函子的 Hom 刻画与 𝔻 在 D 模上的具体作用，会觉得这一步是循环论证。
- 建议来源：nLab “Verdier duality”；nLab “adjoint functor”

## 待注 ch09.tex:144（原 PDF p53）
- 原文：This is a Springer-type replacement for the false exactness of Av^1_E.
- 概念：Springer 型（Springer 解消/对应式的类比）、用 Verdier 商替换错误的 t-正合性。
- 读者缺什么：“Springer 型”只出现在这一句，原文也没展开；读者会误以为是 Springer 对应本身，而这里只是借 Springer 解消作类比（用另一个范畴替代坏的像）。
- 建议来源：nLab “Springer resolution”

## 待注 ch09.tex:148（原 PDF p53）
- 原文：The geometric Ramanujan theorem says that cuspidal objects are tempered [Ber21]
- 概念：几何 Ramanujan 定理（尖点对象都是温和的）、尖点对象与温和子范畴的关系。
- 读者缺什么：只报名不讲内容——读者不知道它对应经典 Ramanujan 猜想的哪一面（自守表示的 L 函数没有极点/在临界带的位置），也不知道在本书里“温和”的确切定义（要到 §9.8 与 ch10.tex:111 才给出）。
- 建议来源：原书文献 [Ber21]；nLab “Langlands program”
