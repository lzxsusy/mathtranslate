# 匹配圈

> `seidel/concept/matching-cycle` ｜ track C ｜ draft

**一句话**：连接两个临界值的匹配路径给出总空间中的 Lagrangian 球面：两个 thimble 沿公共消失圈粘合。

**自测**：匹配路径两侧的消失圈何时能拼成总空间中的 Lagrangian 球面？

## 定义

设 $\gamma:[-1,1]\to\operatorname{int}(S)$ 是嵌入道路，$\gamma^{-1}(\operatorname{Critv})=\{-1,1\}$。把它拆成两条同起点的消失路径 $\gamma_\pm(t)=\gamma(\pm t)$，得到纤维 $M=E_{\gamma(0)}$ 中两个消失圈 $V_\pm$。若 $V_\pm$ 作为带 framing 的正合 Lagrangian 球面同痕，称 $\gamma$ 为匹配路径，相应同痕为匹配同痕。
此时两个 thimble $\Delta^-_\gamma,\Delta^+_\gamma$ 沿公共边界 $V_\pm$ 粘合，
$$\Sigma_\gamma=\Delta^-_\gamma\cup\Delta^+_\gamma\subset E$$
是总空间 $E$ 中的光滑 Lagrangian 球面（naive matching cycle）。一般情形先用形变把 $V_-$ 移到 $V_+$，再拉回，得匹配圈 $\Sigma_{\gamma,I}\subset E$。

记号：$n=\dim_\C E-1$；$\Sigma_\gamma\cong S^{n+1}$，在总空间而非纤维中。$I$ 为匹配同痕。

## 要点

- 匹配圈是总空间 $E$ 中的 Lagrangian 球面，维数 $n+1$。
- 它是两个 thimble 沿公共消失圈 $V_\pm$ 粘成的，不是两个消失圈在纤维中的并。
- 不同匹配路径/同痕给出的匹配圈相差 Dehn twist 与 Lagrangian 同痕；$n=1$ 时与同痕 $I$ 无关（Remark 16.11）。

## 公式

$$\Sigma_\gamma=\Delta^-_\gamma\cup\Delta^+_\gamma\cong S^{n+1}\subset E$$
$$\partial\Delta^\pm_\gamma=V_\pm$$

## 定理与证明

### 匹配圈是 Lagrangian 球面

沿匹配路径 $\gamma$ 的匹配圈 $\Sigma_\gamma$ 是总空间 $E$ 中的光滑 Lagrangian 球面 $S^{n+1}$。

（sketch；来源：原书 p.230–231 §16g）

1. 两条消失路径给出纤维中的消失圈 $V_\pm$；匹配条件保证 $V_+=V_-$（或经同痕）。  
   为什么：匹配路径按定义要求两个消失圈作为 framed exact Lagrangian spheres 同痕。
2. 平行移动把两个 thimble 沿公共边界 $V_\pm$ 粘合，局部为 $(t-1,t+1)\times V_\pm$。  
   为什么：两球沿公共边界粘合，粘合处切空间一致。
3. 粘合结果为总空间中的光滑 Lagrangian 子流形，同胚于 $S^{n+1}$。  
   为什么：两个 $(n+1)$-球沿公共 $S^n$ 粘合。

缺口：细节见原书 §16g（p.230–231）；一般情形需先作形变（Lemma 15.3）。

## 易错点

- 匹配路径不是任意道路：它要求两侧消失圈作为 framed exact Lagrangian spheres 同痕。
- 匹配圈在总空间 $E$ 中，不在纤维中；不要把它写成两个消失圈的并。
- 匹配圈的定向依赖两侧 thimble 的定向；换定向会改变符号。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§16，p.230–231（原书 p.230 §16g）

关联：`seidel/concept/vanishing-cycle`、`seidel/concept/thimble`、`seidel/deriv/mutation`

来源说明：据原书 §16g（p.230–231）转述；译者注 A09-xx。
