# 对偶扭层 $\mathcal D^\circ$

> `mloc/concept/dual-twisted-sheaf` · type=concept · track=A · status=draft · verification=source-only

**别名**：opposite twisted sheaf、$\mathcal D^\circ$、反代数层、典范层扭

## 摘要

对偶：$\mathcal D_X^\circ\cong\mathcal D_{\omega_X}$，$t(\mathcal D^\circ)=-t(\mathcal D)+H^1(d\log)i(\omega_X)$。

## 问题

把乘法取反之后还是扭层吗，对偶层的扭化不变量与原来的 $t(\mathcal D)$ 有什么关系？

## 定义

对 $X$ 上的 $k$-代数层 $A$，记 $A^\circ$ 为与之反同构的 $k$-代数层（乘法 $a\cdot^\circ b=ba$），称反代数层。$(\mathcal D^\circ,i)$ 指同一个 $i$ 视为 $\mathcal O_X\to\mathcal D^\circ$。$\omega_X$ 是 $n$ 次微分形式层（$n=\dim X$），是可逆层；$\mathcal D_{\omega_X}$ 是按「用线丛扭」构造得到的层。第 1 章命题 1.11 断言 $(\mathcal D^\circ,i)$ 仍是扭层，第 1 章引理 1.12 把它认成 $\mathcal D_{\omega_X}$，第 1 章命题 1.13 计算其 $t$。

记号：$A^\circ$：反代数层；$\omega_X=\Omega_X^n$：典范层；$L_\xi$：Lie 导数；$\lambda(\xi)=-L_\xi$；$i(\omega_X)\in H^1(X,\mathcal O_X^*)$。

## 要点

- 第 1 章命题 1.11：$(\mathcal D^\circ,i)$ 仍是扭层——这不是废话：反代数层的局部模型是 $\mathcal D_X^\circ$，需要一条同构把它认成 $\mathcal D_{\omega_X}$。
- 关键映射是 $\lambda(\xi)=-L_\xi$：$L_\xi$ 是 $\omega_X$ 上的一阶微分算子，$L_{f\xi}=L_\xi f$（右乘 $f$）说明 $\lambda$ 关于右乘 $\mathcal O_X$-线性；且 $\lambda([\xi,\eta])=[\lambda(\eta),\lambda(\xi)]$，这正是反代数所需的符号反转。
- 第 1 章引理 1.12：$(\mathcal D_X^\circ,i_X)\cong(\mathcal D_{\omega_X},i_{\omega_X})$，即反代数层的局部模型恰是「被典范层扭过的 $\mathcal D_X$」。
- 第 1 章命题 1.13：$t(\mathcal D^\circ)=-t(\mathcal D)+H^1(d\log)(i(\omega_X))$；负号来自反代数，$\omega_X$ 项来自第 1 章引理 1.12。
- 当 $\omega_X\cong\mathcal O_X$（如 $\mathbb A^n$）时 $t(\mathcal D^\circ)=-t(\mathcal D)$：对偶把扭化类取反。

## 公式

$$a\cdot^\circ b=ba$$

$$\lambda(\xi)=-L_\xi,\qquad \lambda([\xi,\eta])=[\lambda(\eta),\lambda(\xi)]$$

$$(\mathcal D_X^\circ,i_X)\cong(\mathcal D_{\omega_X},i_{\omega_X})$$

$$t(\mathcal D^\circ)=-t(\mathcal D)+H^1(d\log)(i(\omega_X))$$

## 相关定理

### 第 1 章命题 1.11（反代数层仍是扭层）

设 $(\mathcal D,i)$ 是光滑代数簇 $X$ 上的扭微分算子层。则 $(\mathcal D^\circ,i)$ 也是 $X$ 上的扭微分算子层。

证明状态：`complete`

1. 断言是局部的，可设 $(\mathcal D,i)=(\mathcal D_X,i_X)$。
   - 为什么：扭层的定义是局部同构于 $(\mathcal D_X,i_X)$，故只需验证模型本身。
2. 由第 1 章引理 1.12，$(\mathcal D_X^\circ,i_X)\cong(\mathcal D_{\omega_X},i_{\omega_X})$，而后者按「用线丛扭」的构造是扭层。
   - 为什么：第 1 章引理 1.12 给出与典范层扭层的同构；第 1 章命题 1.8 之前已说明用可逆层扭得到的是扭层（第 1 章引理 1.7 的构造）。
3. 故 $(\mathcal D_X^\circ,i_X)$ 局部同构于 $(\mathcal D_X,i_X)$，一般 $(\mathcal D^\circ,i)$ 逐块同理。
   - 为什么：局部同构的传递性：先在局部把 $\mathcal D$ 平凡化，再对反代数层用模型情形。

### 第 1 章引理 1.12（$\mathcal D_X^\circ\cong\mathcal D_{\omega_X}$）

设 $X$ 是维数为 $n$ 的光滑代数簇，$\omega_X$ 是 $X$ 上 $n$ 次微分形式构成的可逆 $\mathcal O_X$-模。则二元组 $(\mathcal D_X^\circ,i_X)$ 自然同构于 $(\mathcal D_{\omega_X},i_{\omega_X})$。

证明状态：`complete`

1. 向量场经 Lie 导数 $L_\xi$ 作用在 $\omega_X$ 上；$L_\xi$ 是一阶微分算子，因为 $L_\xi(f\omega)=fL_\xi\omega+\xi(f)\omega$，即 $[L_\xi,f]=\xi(f)$。
   - 为什么：Cartan 公式展开给出 Leibniz 规则；$[L_\xi,f]=\xi(f)$ 正是「一阶微分算子」的定义。
2. $[L_\xi,L_\eta]=L_{[\xi,\eta]}$，且 $L_{f\xi}=L_\xi f$（右乘 $f$）；故 $\lambda(\xi)=-L_\xi$ 是 $\mathcal O_X$-模态射（关于右乘），并满足 $\lambda([\xi,\eta])=[\lambda(\eta),\lambda(\xi)]$。
   - 为什么：$L_{f\xi}=fL_\xi+\xi(f)$ 与 $L_\xi f=fL_\xi+\xi(f)$ 相差 $fL_\xi$，整理即 $L_{f\xi}=L_\xi f$；反交换性来自 $[L_\xi,L_\eta]=L_{[\xi,\eta]}$ 与负号。
3. 由 $\mathcal D_X$ 由 $\mathcal O_X$ 与 $T_X$ 生成，$\lambda$ 延拓为 $k$-代数层态射 $\mathcal D_X\to\mathcal D_{\omega_X}^\circ$，且在 $\mathcal O_X$ 上恒等。
   - 为什么：$\lambda$ 关于右乘 $\mathcal O_X$-线性且保持反交换子，故与 $\mathcal D_X$ 的泛性质相容。
4. $\operatorname{Gr}\lambda=\mathrm{id}$（两边分次都同构于 $S(T_X)$，$\lambda$ 在 $T_X$ 上是恒等），故 $\lambda$ 是同构。
   - 为什么：$\operatorname{Gr}\lambda$ 在 $\operatorname{Gr}_1$ 上是恒等，而 $\operatorname{Gr}_1$ 生成分次环；再由第 1 章引理 1.1 的论证得可逆。
5. 于是 $(\mathcal D_X^\circ,i_X)\cong(\mathcal D_{\omega_X},i_{\omega_X})$。
   - 为什么：把 $\lambda$ 视为 $\mathcal D_X$ 与 $\mathcal D_{\omega_X}^\circ$ 之间的同构，再取反代数回到原陈述。

### 第 1 章命题 1.13（$t(\mathcal D^\circ)$）

设 $X$ 是光滑代数簇，$\mathcal D$ 是 $X$ 上的扭微分算子层。则 $t(\mathcal D^\circ)=-t(\mathcal D)+H^1(d\log)(i(\omega_X))$。

证明状态：`complete`

1. 取覆盖与 $\psi_i:(\mathcal D,i)|_{U_i}\to(\mathcal D_{U_i},i_{U_i})$，$\varphi_{jk}$ 对应 $\omega_{jk}$；复合 $\lambda$ 得 $\tau_i:(\mathcal D^\circ,i)|_{U_i}\to(\mathcal D_{\omega_X},i_{\omega_X})|_{U_i}$。
   - 为什么：反代数层上的乘法取反，$\psi_i$ 仍是同构；再与第 1 章引理 1.12 的 $\lambda$ 复合即得平凡化。
2. 自同构 $\sigma_{jk}=\lambda\circ\varphi_{jk}\circ\lambda^{-1}$ 满足 $\sigma_{jk}(\lambda(\xi))=\lambda(\xi)-\omega_{jk}(\xi)$，且 $\tau_j=\sigma_{jk}\circ\tau_k$。
   - 为什么：$\lambda$ 是 $\mathcal O_X$-线性的（关于右乘），故把 $\varphi_{jk}$ 的修正项原样搬运。
3. 再用 $\alpha_i:\omega_{U_i}\to\mathcal O_{U_i}$ 把 $\mathcal D_{\omega_X}$ 平凡化为 $\mathcal D_X$：$\beta_i(\eta)=\alpha_i\eta\alpha_i^{-1}$，$s_{jk}=\alpha_j\alpha_k^{-1}(1)$，得 $\delta_{jk}=\beta_j\sigma_{jk}\beta_k^{-1}$。
   - 为什么：与第 1 章命题 1.4 的证明同法：可逆层 $\omega_X$ 的过渡函数是 $s_{jk}=d\log$ 的上闭链。
4. 计算 $\delta_{jk}(\xi)=\xi+\omega_{jk}(\xi)-s_{jk}^{-1}ds_{jk}(\xi)=\xi-(-\omega_{jk}+s_{jk}^{-1}ds_{jk})(\xi)$。
   - 为什么：把 $\beta_i^{-1}(\xi)=-\lambda(\xi)+\beta_i(\lambda(\xi))(1)$ 代入并用 $\beta_j(\lambda(\xi))=s_{jk}\beta_k(\lambda(\xi))s_{jk}^{-1}$。
5. 故 $t(\mathcal D^\circ)$ 的上闭链是 $-\omega_{jk}+d\log s_{jk}$，即 $-t(\mathcal D)+H^1(d\log)(i(\omega_X))$。
   - 为什么：逐项相加：$-\omega$ 贡献 $-t(\mathcal D)$，$d\log s$ 贡献典范层的类。

## 易错点

- $(\mathcal D^\circ,i)$ 里的 $i$ 不变，变的是乘法；不要把它与「用 $\omega_X$ 扭」混为一谈——两者只差一个同构（第 1 章引理 1.12）。
- 第 1 章命题 1.13 的两项符号相反：$-t(\mathcal D)$ 与 $+H^1(d\log)(i(\omega_X))$；在 $\omega_X\cong\mathcal O_X$ 时只剩 $-t(\mathcal D)$。
- $\lambda(\xi)=-L_\xi$ 是**右** $\mathcal O_X$-线性的（$L_{f\xi}=L_\xi f$），这正是它给出反代数同构而不是同构的原因；把 $f$ 放错边会丢掉反交换性。

## 相关卡

- `mloc/concept/twisted-sheaf-of-differential-operators`
- `mloc/concept/twisting-invariant-t`
- `mloc/concept/twist-by-line-bundle`
- `dmod/concept/dz-structure-sheaf`

## 出处

- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[8]（PDF [12]） · `源码/chapters/ch01.tex:276-280（反代数层与第 1 章命题 1.11）`
- Miličić, Localization and Representation Theory of Reductive Lie Groups · 第 1 章 §1 扭微分算子层 · p.[9]（PDF [13]） · `源码/chapters/ch01.tex:282-368（第 1 章引理 1.12 与第 1 章命题 1.13）`
