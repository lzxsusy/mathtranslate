# ch10.tex 待注点（第 10 章，原 PDF p53–p56）

## 待注 ch10.tex:7（原 PDF p53）
- 原文：Ignoring the customary half-twist, the expected equivalence is the Arinkin–Gaitsgory/Gaitsgory–Raskin formulation [AG15, GR24a]
- 概念：半扭转（half-twist）、Tate 扭转的归一化、Arinkin–Gaitsgory 与 Gaitsgory–Raskin 两种表述。
- 读者缺什么：作者一句“忽略惯常的半扭转”就过去了，读者不知道被忽略的是什么（Hecke 特征层与 Eisenstein 函子上各差一个 Tate 扭转），也不知道两种表述为何等价；后面 §10.4、§10.5 的函子都要按此归一化才对得上。
- 建议来源：原书文献 [AG15]、[GR24a]；nLab “Tate twist”

## 待注 ch10.tex:28（原 PDF p53）
- 原文：Equivalently, this is the classical stack underlying the (−1)-shifted cotangent stack. If Y is smooth, Sing(Y) is the zero vector bundle over Y, i.e. the zero section.
- 概念：奇异概形 Sing(Y) := Spec_{Y^cl} Sym(H^1(T_Y))、(−1)-移位余切叠、准光滑（quasi-smooth）导出概形。
- 读者缺什么：不知道 (−1)-移位余切叠怎么定义、“底层经典叠”指取何种截断，也不清楚为何用 H^1(T_Y) 而不是 H^0；“Y 光滑时 Sing(Y) 是零截面”这句因此只能死记。
- 建议来源：nLab “shifted cotangent bundle”；原书文献 [AG15]

## 待注 ch10.tex:59（原 PDF p54）
- 原文：For X = P1, the underived stack of de Rham local systems is essentially pt/Ǧ, but the derived stack is the derived zero fiber LocSys_Ǧ(P1) ≃ pt/Ǧ ×_{ǧ/Ǧ} pt/Ǧ.
- 概念：导出零纤维/导出纤维积、非导出叠与导出叠的差别、导出结构保留的 Ext 数据。
- 读者缺什么：为何 P^1 上 de Rham 局部系统非导出地都平凡、导出版本多出来的到底是什么（Ext 群），以及导出纤维积 pt/Ǧ ×_{ǧ/Ǧ} pt/Ǧ 为何就是零纤维。
- 建议来源：nLab “derived algebraic geometry”；nLab “de Rham stack”

## 待注 ch10.tex:72（原 PDF p54）
- 原文：The derived Satake theorem identifies Sph_{G,x} ≃ IndCoh_{Nilp(ǧ*)/Ǧ}(Hecke^spec).
- 概念：导出 Satake 等价、谱 Hecke 叠 Hecke^spec、幂零锥 Nilp(ǧ*)/Ǧ 作为允许的奇异支撑。
- 读者缺什么：只报名“导出 Satake 定理”，未说它是把几何 Satake 的心范畴等价提升到导出层；读者不知道 Hecke^spec 的几何、也不知道为何右端要在 Nilp(ǧ*)/Ǧ 上取 IndCoh。
- 建议来源：原书文献 [AG15]；nLab “geometric Satake correspondence”

## 待注 ch10.tex:91（原 PDF p55）
- 原文：Eis^spec_{P̌} := (p̌)^{IndCoh}_* ∘ q̌^!
- 概念：IndCoh 推前 (p̌)^{IndCoh}_*、反常/!-拉回 q̌^!、连续右伴随。
- 读者缺什么：上一条只说普通 p̌_* 不行，没说 (p̌)^{IndCoh}_* 是什么（AG 的 IndCoh 六函子形式化）；q̌^! 与 q̌^* 的区别、为何组合起来才有正确的连续右伴随，读者无法自行补出。
- 建议来源：nLab “ind-coherent sheaves”；原书文献 [AG15]

## 待注 ch10.tex:127（原 PDF p56）
- 原文：its singular support is a closed conical subset SS(F) ⊂ T*Y, defined by microlocal analysis, equivalently by the vanishing of nearby cycles in non-characteristic directions
- 概念：微局部奇异支撑 SS(F)、非特征方向、邻近圈（nearby cycles）消失的判据。
- 读者缺什么：两种定义（微局部分析/非特征方向上邻近圈消失）为何等价，Betti 与 de Rham 情形下 SS 的差别，以及“局部系统 ⇔ SS 为零截面”的证明思路。
- 建议来源：原书文献 [BZN16]、[NY19]；nLab “singular support”
