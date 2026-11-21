# Hitchin 纤维化与完全可积系统

- **id**：`bdh/concept/hitchin-fibration`
- **类型**：concept
- **位置**：§2.2
- **问题**：为什么 Hitchin 纤维化 $p:T^{*}\operatorname{Bun}_G\to\operatorname{Hitch}(X)$ 的纤维能是阿贝尔簇，且 $\dim\operatorname{Hitch}(X)=\dim\operatorname{Bun}_G$？

> 把 $\omega_X$-扭的 Casimir 不变量按 $X$ 的整体截面取值，得到 Hitchin 底 $\operatorname{Hitch}(X)$；余切栈 $T^{*}\operatorname{Bun}_G$ 沿每个态射的截面为 $\Gamma(X,\mathfrak{g}^{*}_{\mathcal{F}}\otimes\omega_X)$，由此得到 Hitchin 纤维化，其纤维在 $\gamma$ 分支上阿贝尔簇，且维数等于 $\dim\operatorname{Bun}_G$。

## 定义

设 $G$ 是约化群，$\mathfrak{g}=\operatorname{Lie}G$，$g=\dim X$。令 $\mathcal{C}=\mathcal{C}_{\mathfrak{g}}:=\operatorname{Spec}(\operatorname{Sym}\mathfrak{g})^{G}$，齐次生成元 $p_i$ 的次数记作 $d_i$。把 $(\operatorname{Sym}^{\cdot}\mathfrak{g})^{G}$ 扭成 $\omega_X$-扭的形式 $\mathcal{C}_{\omega_X}$，定义 Hitchin 底：$\operatorname{Hitch}(X)=\operatorname{Hitch}_{\mathfrak{g}}(X):=\Gamma(X,\mathcal{C}_{\omega_X})\simeq\prod_{i}\Gamma(X,\omega_X^{\otimes d_i})$。其上的函数环记作 $\mathfrak{z}^{cl}(X)=\mathfrak{z}^{cl}_{\mathfrak{g}}(X)$。对 $\operatorname{Bun}_G$ 上的 $G$-torsor $\mathcal{F}$，余切栈是 $T^{*}_{\mathcal{F}}\operatorname{Bun}_G=\Gamma(X,\mathfrak{g}^{*}_{\mathcal{F}}\otimes\omega_X)$；把 $\mathcal{C}_{\omega_X}$ 的不变量作用在每个截面上，就得到 $p:T^{*}\operatorname{Bun}_G\to\operatorname{Hitch}(X)$，称为 Hitchin 纤维化。相应地有 $h_X^{cl}:\mathfrak{z}^{cl}(X)\to\Gamma(T^{*}\operatorname{Bun}_G,\mathcal{O})=\Gamma(\operatorname{Bun}_G,P)$，它是 $^{\cdot}$-代数同态。

**记号**：$\mathcal{C}:=\operatorname{Spec}(\operatorname{Sym}\mathfrak{g})^{G}$：Casimir 不变量谱；$d_i$：齐次生成元的次数、$\operatorname{Hitch}(X)=\Gamma(X,\mathcal{C}_{\omega_X})$：Hitchin 底、$\mathfrak{z}^{cl}(X)$：$\operatorname{Hitch}(X)$ 上的函数环、$p:T^{*}\operatorname{Bun}_G\to\operatorname{Hitch}(X)$：Hitchin 纤维化

## 关键点

- 构造的要点是 $\omega_X$-扭：$\mathcal{C}_{\omega_X}$ 的截面给出 $\operatorname{Hitch}(X)=\Gamma(X,\mathcal{C}_{\omega_X})\simeq\prod_{i}\Gamma(X,\omega_X^{\otimes d_i})$，这与 $(\operatorname{Sym}^{\cdot}\mathfrak{g})^{G}$ 的 $G_m$-分次（$p_i$ 的次数 $d_i$）严格对应（ch02.tex:28-32）。
- $T^{*}\operatorname{Bun}_G$ 的纤维是 $\Gamma(X,\mathfrak{g}^{*}_{\mathcal{F}}\otimes\omega_X)$：切层纤维是 $H^{1}(X,\mathfrak{g}_{\mathcal{F}})$，对偶后扭以 $\omega_X$，于是整个余切栈由 $p$ 映到 Hitchin 底（ch02.tex:34-38）。
- 定理 2.2.4 [Hit87][Fal93][Gi97]：(i) $h_X^{cl}$ 的像由两两泊松交换的函数组成；(ii) $\dim\operatorname{Hitch}(X)=\dim\operatorname{Bun}_G=(g-1)\cdot\dim\mathfrak{g}$；(iii) $p$ 平坦、纤维纯维数 $\dim\operatorname{Bun}_G$、$p^{\gamma}$ 满；(iv) 存在非空开 $U$，使 $(p^{\gamma})^{-1}(U)\to U$ 固有光滑、纤维连通，且纤维同构于阿贝尔簇 $A_u$ 与中心 $Z\subset G$ 的分类栈之积；(v) $\mathfrak{z}^{cl}(X)\to\Gamma(\operatorname{Bun}_G^{\gamma},P)$ 是同构（ch02.tex:48-56）。
- (i) 蕴涵 $p$ 是 Lagrange 纤维化，即 $(T^{*}\operatorname{Bun}_G,p)$ 是完全可积系统：$\dim\operatorname{Bun}_G$ 个泊松交换的函数足以把每根纤维的辛方向全部零化（ch02.tex:61-62）。
- (ii) 的算法：$\dim\Gamma(X,\omega_X^{\otimes d})=(g-1)(2d-1)$，故 $\dim\operatorname{Hitch}(X)=\sum_{i}(g-1)(2d_i-1)=(g-1)\dim\mathfrak{g}$，与 $\dim\operatorname{Bun}_G$ 相等（ch02.tex:64-66）。
- 可靠度：$\operatorname{Bun}_G$ 极良（2.1.2，证明在 2.10.5），所以 $T^{*}\operatorname{Bun}_G$ 有开稠密的 DM 子栈 $T^{*}\operatorname{Bun}_G^{0}$ 且是辛的，定理中的 Lagrange 说法才有意义（ch02.tex:61）。
- 2.2.4(v) 是 2.2.5 量子化问题的起点：它给出 $\mathfrak{z}^{cl}(X)$ 与 $\Gamma(\operatorname{Bun}_G^{\gamma},P)$ 的同构，从而在 $\gamma$ 分支上 $h_X^{\gamma}$ 是整体截面的同构。

## 公式

```latex
\mathcal{C}=\mathcal{C}_{\mathfrak{g}}:=\operatorname{Spec}(\operatorname{Sym}\mathfrak{g})^{G}
```
```latex
\operatorname{Hitch}(X)=\operatorname{Hitch}_{\mathfrak{g}}(X):=\Gamma(X,\mathcal{C}_{\omega_X})\simeq\prod_{i}\Gamma(X,\omega_X^{\otimes d_i})
```
```latex
T^{*}_{\mathcal{F}}\operatorname{Bun}_G=\Gamma(X,\mathfrak{g}^{*}_{\mathcal{F}}\otimes\omega_X)
```
```latex
p:T^{*}\operatorname{Bun}_G\to\operatorname{Hitch}(X),\qquad h_X^{cl}:\mathfrak{z}^{cl}(X)\to\Gamma(T^{*}\operatorname{Bun}_G,\mathcal{O})=\Gamma(\operatorname{Bun}_G,P)
```
```latex
\dim\operatorname{Hitch}(X)=\dim\operatorname{Bun}_G=(g-1)\cdot\dim\mathfrak{g}
```

## 定理

定理 2.2.4 [Hit87, Fal93, Gi97]：$h_X^{cl}$ 的像由泊松交换的函数组成；$\dim\operatorname{Hitch}(X)=\dim\operatorname{Bun}_G$；$p$ 平坦、纤维纯维数 $\dim\operatorname{Bun}_G$，且存在非空开 $U$ 使 $(p^{\gamma})^{-1}(U)\to U$ 固有光滑、纤维连通，同构于阿贝尔簇 $A_u$ 与中心 $Z$ 的分类栈之积；最后 $\mathfrak{z}^{cl}(X)\to\Gamma(\operatorname{Bun}_G^{\gamma},P)$ 是同构（ch02.tex:48-56，pp.16-18）。

## 常见错误

- 把 $\operatorname{Hitch}(X)$ 当成 $(\operatorname{Sym}^{\cdot}\mathfrak{g})^{G}$ 的整体截面：$\mathcal{C}$ 是仿射概形，底是由它扭以 $\omega_X$ 后的整体截面给的，两种取法一般不同；维数 $\sum(g-1)(2d_i-1)$ 的算法只对扭曲版本成立（ch02.tex:28-32、64）。
- 把定理 2.2.4(iv) 的纤维说成「阿贝尔簇」而不提中心：纤维是阿贝尔簇 $A_u$ 与中心 $Z\subset G$ 的分类栈之积，中心的贡献是栈性的，忘记它会以为纤维都是概形。
- 以为 $p$ 的平坦与纤维纯维数只对 $\gamma$ 分支成立：2.2.4(iii) 对 $p$ 整体成立，$p^{\gamma}$ 只是限制到分支；而 (iv) 的光滑、连通性只保证在某个非空开 $U$ 上。
- 把 $\gamma$ 与 $X$ 的某个量混淆：$\gamma\in\pi_1(G)$（原书 2.2.4 与 2.2.3 附近印作 $\pi_1(X)$，按上下文应为 $\pi_1(G)$，中译校订本底本如此保留并在 Tutor Note 中说明，见 ch02.tex:53、73）。
- 把完全可积系统理解为「纤维都是环面」：这里纤维可以是阿贝尔簇（复环面），且 (iv) 只说在开 $U$ 上；奇异纤维（例如 $0$ 纤维 $\operatorname{Nilp}$）需要单独处理，见 2.10。

## 批注

### 背景直觉：为什么底空间的维数正好等于总空间的维数的一半

对完全可积系统，底空间与纤维同维：总数是 $2\dim\operatorname{Bun}_G$，定理 2.2.4(ii) 说 $\dim\operatorname{Hitch}(X)=\dim\operatorname{Bun}_G$，恰好一半。算 $\dim\Gamma(X,\omega^{\otimes d})=(g-1)(2d-1)$ 时，$2d-1$ 中多出的 $2d$ 来自 $\omega$ 的成对抵消，$-1$ 是 $g-1$ 的 Euler 示性数效应；把所有 $d_i$ 加起来得到 $(g-1)\dim\mathfrak{g}$，与 $\dim\operatorname{Bun}_G$ 一致。

### 含糊点拨：为什么纤维能是阿贝尔簇

纤维是「固定所有 Casimir 不变量值的 Higgs 场」的模空间。在好的开集上，这样的 Higgs 丛 $(\mathcal{F},\eta)$ 给出一条谱曲线 $\Sigma\to X$——$\eta$ 在 $\Sigma$ 上成为取值于 $\omega_X$ 的截面——而 $\operatorname{Pic}$ 的部分（固定典范部分后）正是阿贝尔簇：基是曲线的雅可比，逐纤维看就是 Prym 型环面。中心 $Z$ 的部分不改变谱曲线，只留下分类栈的方向，故纤维是 $A_u\times BZ$。

### 易错预警：两个「维数相等」不是一回事

定理 2.2.4(ii) 的 $\dim\operatorname{Hitch}(X)=\dim\operatorname{Bun}_G$ 是底空间与总空间一半的关系；2.10.1 里出现的 $\dim T^{*}\operatorname{Bun}_G\le 2\dim\operatorname{Bun}_G$ 是余切栈维数与上界的关系。前者说明底空间「足够大」，后者说明 $\operatorname{Bun}_G$ 良。引用维数等式时需注明是哪一个，否则在论证 $\operatorname{Bun}_G$ 极良时会循环。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §2.2；印刷页 [16, 17, 18] / PDF 页 [16, 17, 18]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch02.tex:26-76`
- 2.2.1–2.2.3 在 p.16（`\SourcePage{16}` 在 ch02.tex:24）；定理 2.2.4 在 p.17（`\SourcePage{17}` 在 ch02.tex:44）；`\SourcePage{18}` 在 ch02.tex:63，故 2.2.5 的量子化问题在 p.18。印刷页与 PDF 页同为 16、17、18。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
