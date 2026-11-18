# 匹配圈

> `seidel/concept/matching-cycle` ｜ track C ｜ draft

**一句话**：连接两个临界值的匹配路径在纤维中给出的 Lagrangian 球面，是相应 thimble 的边界。

**自测**：两个消失圈如何沿一条路径「匹配」成一个球面？

## 定义

设 $\gamma$ 是复平面中连接两个临界值（或一个临界值与正则值）的道路，且 $\gamma$ 在 $(n+1)$ 维全空间中提升为一族消失盘。沿 $\gamma$ 的两侧取消失圈 $V_{\gamma_1},V_{\gamma_2}$，其并（在交点处粘合）称为匹配圈
$$M_\gamma=V_{\gamma_1}\cup V_{\gamma_2}.$$
当 $\gamma$ 是匹配路径时，$M_\gamma$ 是光滑纤维中的 Lagrangian 球面。

记号：匹配路径要求两个临界值在 $\pi$ 下的像由一条道路连接，且道路避开其他临界值。

## 要点

- 匹配圈是纤维中的 Lagrangian 球面，维数 $n-1$。
- 匹配圈的 thimble 以它为边界；这是把 Lefschetz 纤维化的几何变成纤维中球面的组合数据的桥梁。
- 不同的匹配路径给出不同的匹配圈，彼此相差 Dehn twist 与哈密顿同痕。

## 公式

$$M_\gamma=V_{\gamma_1}\cup V_{\gamma_2}\cong S^{n-1}$$
$$\partial T_\gamma=M_\gamma$$

## 定理与证明

### 匹配圈是 Lagrangian 球面

沿匹配路径 $\gamma$ 的匹配圈 $M_\gamma$ 是光滑纤维中的 Lagrangian 球面。

（sketch；来源：原书 p.224–228 §16）

1. 在 $\gamma$ 的每个正则点处，两侧消失圈平行移动后光滑粘合。  
   为什么：匹配条件保证粘合处切空间一致。
2. 粘合后的子流形同胚于 $S^{n-1}$，且每点的切空间是 Lagrangian。  
   为什么：两个 Lagrangian 半球的并，粘合边界处切空间相同。
3. 故 $M_\gamma$ 是 Lagrangian 球面。  
   为什么：局部性质逐点成立。

缺口：细节见原书 §16c–16d。

## 易错点

- 匹配路径不是任意道路：它必须与消失圈的平行移动相容，否则粘合不光滑。
- 匹配圈的定向依赖两侧消失圈的定向，换定向会改变符号。
- 不要把匹配圈与 thimble 混同：前者在纤维中，后者在全空间中。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§16，p.224–228（原书 p.224 §16）

关联：`seidel/concept/vanishing-cycle`、`seidel/concept/thimble`、`seidel/deriv/mutation`

来源说明：据原书 §16（p.224–228）转述；译者注 A09-xx。
