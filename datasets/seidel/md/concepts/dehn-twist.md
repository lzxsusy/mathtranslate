# Dehn 扭转

> `seidel/concept/dehn-twist` ｜ track C ｜ draft

**一句话**：沿 Lagrangian 球面 V 的余切邻域把纤维方向扭转一圈所得的 exact 辛自同构；它实现绕临界值的单值，并在同调上给出反射公式。

**自测**：绕消失圈走一圈的单值，为什么正好是一个 Dehn 扭转？

## 定义

设 $V\subset M$ 是带框架（framed）的 exact Lagrangian 球面，$\xi:B^*_sV\to V$ 是其半径 $s$ 的余切邻域。取光滑函数 $b:[-s,s]\to\R$ 满足
$$b(r)=0\ (r\ge s),\qquad b(r)-b(-r)=-r,$$
并令 $H(x)=b(|\xi^{-1}(x)|)$（邻域外取 $H=0$）。$H$ 的时间 $2\pi$ 流
$$\tau_V=\phi^{2\pi}_H$$
称为沿 $V$ 的 symplectic Dehn twist。$\tau_V$ 支在 $B^*_sV$ 内、在 $V$ 外为恒等，且是 exact 辛自同构；其同痕类 $[\tau_V]\in\pi_0\mathrm{Aut}(M,\partial M)$ 不依赖 $V$ 的定向。

记号：$r=|\xi|$ 是余切纤维的半径；$\phi^t_H$ 是哈密顿向量场 $X_H$ 的时间 $t$ 流；$\mathrm{Aut}(M,\partial M)$ 是保持边界（若 $M$ 有边界）的辛自同构群。

## 要点

- $\tau_V$ 只改动 $V$ 的余切邻域：在 $B^*_sV$ 外是恒等，故 $[\tau_V]$ 只依赖 $V$ 的框架与同痕类，不依赖定向。
- 在实二维纤维（$n=2$，消失圈是简单闭曲线）的常用约定下，$\tau_L$ 在同调上的作用是 $\tau_L(S)=S+\langle S,L\rangle L$，即沿 $L$ 的反射（transvection）。
- 匹配路径拼接给出 $\Sigma_{\tau_1\#\tau_0}\simeq\tau_{\Sigma_{\tau_1}}(\Sigma_{\tau_0})$（引理 16.13）：Dehn 扭转把不同的匹配圈联系起来。
- 代数侧有「$T=\tau$」：在 $DF(M)$ 中 $T_{L\#_0}(L\#_1)\cong\tau_{L_0}(L\#_1)$（推论 17.17），即扭曲函子在链层次实现几何 Dehn 扭转。
- Lefschetz 纤维化中绕各临界值的单值是 $h_k\simeq\tau_{V_k}$，其复合 $\tau=\tau_{V_1}\cdots\tau_{V_m}$ 给出单值；辫群元素 $\delta^{1/2}\in\mathrm{Br}_m$（见 (5.25)）几何上对应沿边界平行圆的负 Dehn 扭转的平方根（§18l，p.289）。

## 公式

$$\tau_V=\phi^{2\pi}_H,\qquad H(x)=b(|\xi^{-1}(x)|)$$
$$b(r)=0\ (r\ge s),\qquad b(r)-b(-r)=-r$$
$$\tau_L(S)=S+\langle S,L\rangle L$$
$$h_\gamma\simeq\tau_{V_\gamma},\qquad \Sigma_{\tau_1\#\tau_0}\simeq\tau_{\Sigma_{\tau_1}}(\Sigma_{\tau_0})$$

## 定理与证明

### Symplectic Picard–Lefschetz 定理（式 16.6）

设 $\gamma$ 是一条消失路径，$V_\gamma$ 为相应的消失圈。则绕 $\gamma$ 端点临界值的单值 $h_\gamma$ 与 Dehn 扭转 $\tau_{V_\gamma}$ 同痕。

（sketch；来源：原书 p.223–224 §16c）

1. 把环路收缩到临界值附近的小圆盘，单值只由绕临界值一圈的局部模型决定。  
   为什么：临界值之外单值是局部常值的，同痕不改变它。
2. 在局部模型 $z_0^2+\cdots+z_n^2$ 中，沿小圆平行移动使消失圈回到自身，而法向坐标经历一次整圈旋转。  
   为什么：单值的定义就是沿环路平行移动；局部模型把几何化成显式坐标变换。
3. 该法向旋转恰是 $\tau_{V_\gamma}$ 在余切邻域上的作用：$b(r)-b(-r)=-r$ 保证法向翻转一次。  
   为什么：$\tau_V$ 的构造正是「沿 $V$ 的余切纤维转一圈」，两者在局部模型上逐点相同。
4. 故 $h_\gamma$ 与 $\tau_{V_\gamma}$ 同痕。  
   为什么：两个辛自同构在局部模型上相同，模型外又都是恒等。

缺口：原书明确不给证明（p.224：「We will not give the proof here」），只勾画策略：先把纤维化形变到便于计算的位置。

### 引理 16.13：匹配圈与 Dehn 扭转的相容性

设 $\tau=\tau_1\#\tau_0$ 是两条匹配路径的拼接，$\Sigma_\tau$ 为对应的匹配圈。则存在 framed Lagrangian 球面在总空间 $E$ 中的同痕 $\Sigma_{\tau,I}\simeq\tau_{\Sigma_{\tau_1,I_1}}(\Sigma_{\tau_0,I_0})$（式 16.10）。

（complete；来源：原书 p.232 §16h Lemma 16.13）

1. 在拼接点附近，$\Sigma_\tau$ 的两半分别由 $\Sigma_{\tau_0}$ 与 $\Sigma_{\tau_1}$ 平行移动得到。  
   为什么：匹配路径的拼接在纤维中对应的正是两个匹配圈沿公共消失圈粘合。
2. 把 $\Sigma_{\tau_0}$ 沿 $\Sigma_{\tau_1}$ 的余切邻域扭转一圈，恰好把它移动到与 $\Sigma_{\tau_1}$ 粘合的位置。  
   为什么：这正是 $\tau_{\Sigma_{\tau_1}}$ 的局部定义：绕 $\Sigma_{\tau_1}$ 转一圈。
3. 粘合所得球面与 $\Sigma_\tau$ 同痕。  
   为什么：粘合数据与拼接路径的数据一致，同痕保持 Lagrange 性。

缺口：原书把证明放在 §16h（p.232–233），用 (16.9) 的两半消失圈同痕与 framed isotopy 拼出；此处只给结论。

## 易错点

- 同调公式 $\tau_L(S)=S+\langle S,L\rangle L$ 只在纤维实维数 $n=2$、消失圈为曲线时用这个符号；高维情形要带 $\pm$ 号，且 $S$ 是 $n-1$ 维闭链，不能照抄。
- 不要混淆几何 Dehn 扭转 $\tau_V$ 与代数 twist 函子 $T$：前者是 $M$ 的辛自同构，后者是 $\mathrm{Tw}\,F(M)$ 里的函子；推论 17.17 说的才是二者在对象上一致。
- $\tau_V$ 的分次提升依赖 $V$ 的定向：换定向不改变 $[\tau_V]$，却会改变其分次提升的次数，分次公式里差一个平移。
- 辫群 $\Delta$ 的指数约定：$\Delta$ 是正元素、几何上却是负 Dehn 扭转的平方根（§18l），符号取反会得到 $\Delta^{-1}$。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，§16c，p.223–224（原书 p.223–224 §16c）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§16h Lemma 16.13，p.232–232（原书 p.232 Lemma 16.13）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§16c Remark 16.6 / §17 推论 17.17，p.224–261（原书 p.224 Remark 16.6、p.261 推论 17.17）
- Seidel, Fukaya categories and Picard–Lefschetz theory，§18g–§18l，p.283–289（原书 p.283–289 §18g–§18l）

关联：`seidel/concept/exact-lagrangian`、`seidel/concept/vanishing-cycle`、`seidel/concept/matching-cycle`、`seidel/concept/lefschetz-fibration`

来源说明：据原书 §16c（p.223–224）与 §18g（p.283–284）转述；译者注 A11-10、A11-16；外部参考 nLab「Dehn twist」与 Seidel–Thomas（arXiv:math/0001043）。
