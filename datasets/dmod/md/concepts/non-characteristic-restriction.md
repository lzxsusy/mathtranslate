---
id: dmod/concept/non-characteristic-restriction
type: concept
track: F
---

# 非特征限制（逆像的完整性）

> 沿光滑态射的逆像 $Lf^+$ 把有界完整 $\mathcal D_Y$-复形映为有界完整 $\mathcal D_X$-复形，这是「限制不破坏完整」的讲义表述。

**问题**：把完整模限制到光滑子簇上，结果还完整吗？

## 定义

设 $f:X\to Y$ 是光滑代数簇的态射，$Lf^+$ 是逆像函子。讲义 §6 把 §5 的结果综合为：$Lf^+$ 把 $\mathcal D_Y$-模的有界完整复形映为 $\mathcal D_X$-模的有界完整复形（定理 5.6.3）。两条中间结果是：闭浸入 $i:Y\to X$ 上 $Li_+(\mathcal V^\cdot)$ 有界完整（引理 5.6.1）；投影 $p:X\times Y\to Y$ 上 $p_+(\mathcal V^\cdot)=\mathcal O_X\boxtimes\mathcal V^\cdot$ 正合且保持有界完整（引理 5.6.2）。

*记号*：$Lf^+$：光滑态射 $f$ 的逆像函子；$L^p\varphi_+$：直像的左导出；$\mathcal O_X\boxtimes\mathcal V^\cdot$：外积；$i^!$、$i_+$：闭浸入的伴随对；$D^b_{hol}$：有界完整复形的三角子范畴。

## 要点

- 讲义 §5.6 只陈述逆像形式，既不使用「非特征」这一术语，也不给出「特征簇与余法丛横截」形式的判据；本卡标题沿用通行叫法，陈述严格限于讲义内容。
- 论证链：$R\Gamma_Y=i_+\circ Ri^!$（定理 4.9.3）$\Rightarrow$ $Ri^!$ 保持有界完整（用引理 5.5.1）$\Rightarrow$ 闭浸入情形得引理 5.6.1。
- 投影情形：$p_+=\mathcal O_X\boxtimes(-)$ 正合，故逐项保持完整（引理 5.6.2）。
- 一般 $f$ 用图构造分解为闭浸入 $X\to X\times Y$ 与投影 $X\times Y\to Y$；两种情形都保持有界完整，故 $Lf^+$ 也保持。
- 完整模理论在此收束：局部上同调 $R\Gamma_Y$（引理 5.5.1）、直像（定理 5.3.4）、逆像（定理 5.6.3）三种运算都不破坏完整性。

## 关键公式

- $Lf^+\bigl(D^b_{hol}(\mathcal D_Y)\bigr)\subset D^b_{hol}(\mathcal D_X)$
- $R\Gamma_Y(\mathcal V^\cdot)=i_+\bigl(Ri^!(\mathcal V^\cdot)\bigr)$
- $p_+(\mathcal V^\cdot)=\mathcal O_X\boxtimes\mathcal V^\cdot$

## 定理与证明

### 引理 5.6.1（闭浸入下 $Ri^!$ 保持有界完整）（完整）

设 $\mathcal V^\cdot$ 是有界完整 $\mathcal D_X$-模复形。则 $Li_+(\mathcal V^\cdot)$ 是有界完整 $\mathcal D_Y$-模复形。

1. 由 §9 的结果有 $R\Gamma_Y(\mathcal V^\cdot)=i_+(Ri^!(\mathcal V^\cdot))$（定理 4.9.3 的复形形式）。  
   *为什么*：把待证的 $Ri^!$ 与已知保持完整的 $R\Gamma_Y$ 用直像联系起来。
2. $R\Gamma_Y(\mathcal V^\cdot)$ 是有界完整 $\mathcal D_X$-模复形（引理 5.5.1）。  
   *为什么*：$\mathcal V^\cdot|_U$ 完整、$j_+(\mathcal V^\cdot|_U)=Rj_\bullet(\mathcal V^\cdot|_U)$ 完整，再由可区别三角得 $R\Gamma_Y$ 完整。
3. 由 Kashiwara 定理，$i_+$ 与 $i^!$ 在支集受限于 $Y$ 的子范畴上互为拟逆，故 $Ri^!(\mathcal V^\cdot)$ 也有界完整，进而 $Li_+(\mathcal V^\cdot)$ 有界完整。  
   *为什么*：完整性沿这对拟逆双向传递，这就是闭浸入情形。

*出处*：引理 5.6.1 / 原书 §6, p.141

### 定理 5.6.3（光滑态射的逆像保持有界完整）（完整）

设 $f:X\to Y$ 是光滑代数簇的态射。则逆像函子 $Lf^+$ 把 $\mathcal D_Y$-模的有界完整复形映为 $\mathcal D_X$-模的有界完整复形。

1. 把 $f$ 用图构造分解为 $f=p\circ i$：$i:X\to X\times Y$ 是图嵌入（闭浸入），$p:X\times Y\to Y$ 是投影。  
   *为什么*：光滑态射的逆像于是分解为闭浸入的 $Ri^!$ 与投影的平坦拉回，两种情形都已单独处理。
2. 闭浸入情形：由引理 5.6.1 与 $i^!$ 是 $i_+$ 的拟逆（Kashiwara 定理），$Ri^!$ 保持有界完整。  
   *为什么*：完整性可沿直像与 $i^!$ 双向传递，这一步是引理 5.6.1 的推论。
3. 投影情形：由引理 5.6.2，$p_+=\mathcal O_X\boxtimes(-)$ 正合且逐项保持完整；复合两步即得 $Lf^+$ 保持有界完整。  
   *为什么*：讲义此处只写「把这些结果与图构造相结合并使用前述」，未写出 $Lf^+=Li^!\circ Lp^+$ 的合成与平移核对，本卡按两步复原。

*出处*：定理 5.6.3 / 原书 §6, p.141


## 易错点

- 讲义没有定义「非特征子簇」，也没有把结论写成特征簇与余法丛的交条件；引用时不能声称讲义给出了非特征判据。
- 定理 5.6.3 的对象是**有界**完整复形；无界复形不在陈述范围内。
- 引理 5.6.1 在讲义里写作 $Li_+$，与 $i_+$ 的导出不要混同；记号相近但含义不同。
- 投影情形的正合性来自 $p_+=\mathcal O_X\boxtimes(-)$；一般的 $f$ 没有正合性，只能有逐项（导出）断言。
- 「限制到子簇」在讲义中是逆像 $Lf^+$，不是取截面；把两者混同会得到错误的方向。

## 出处

- Miličić《Lectures on the Algebraic Theory of D-Modules》（中译本，校订批注本），§6 完整性与逆像，p.140–141（PDF p.146–147），`源码/chapters/chap5.tex:297-319（引理 5.6.1、定理 5.6.3）`

## 核验

状态：`source-only`（2026-11-19）

## 关联

- `dmod/concept/holonomicity-preserved-by-direct-image`
- `dmod/concept/base-change-for-d-modules`
- `dmod/concept/kashiwara-theorem`
