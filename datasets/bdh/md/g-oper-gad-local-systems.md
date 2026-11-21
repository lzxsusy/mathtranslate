# g-oper、伴随群 G_ad 与局部系统

- **id**：`bdh/concept/g-oper-gad-local-systems`
- **类型**：concept
- **位置**：§3.4
- **问题**：为什么 $G$-oper 到 $\mathfrak g$-oper 的投影没有典范截面，而非要选一个 $\omega_X$ 的平方根 $\mathcal L$，选完之后多出来的自由度又恰好是中心 $Z$ 的 torsor？

> $\mathfrak g$-oper 就是伴随群 $G_{ad}$ 的 oper；从 $G$-oper 到 $\mathfrak g$-oper 的投影要选 $\omega_X$ 的平方根才有截面，而固定平方根后 $\operatorname{Op}_G(X)$ 恰是 $\operatorname{Op}_{\mathfrak g}(X)$ 再乘上中心 $Z$ 的 torsor 群胚。

## 定义

设 $G$ 半单，对每个单负根 $\alpha$ 固定非零元 $y_{\alpha}\in\mathfrak g^{\alpha}$，令 $G_{ad}:=G/Z$、$B_{ad}:=B/Z$、$H_{ad}:=H/Z$（$Z$ 为 $G$ 的中心）。置 $\operatorname{Op}_{\mathfrak g}(X):=\operatorname{Op}_{G_{ad}}(X)$，于是有显然的投影 $\operatorname{Op}_G(X)\to\operatorname{Op}_{\mathfrak g}(X)$（§3.4.1）。要把 $\mathfrak g$-oper $(\mathfrak{F}_{B_{ad}},\nabla)$ 提升为 $G$-oper，等价于把 $\mathfrak{F}_{B_{ad}}$ 提升为 $B$-丛，又等价于把 $\mathfrak{F}_{H_{ad}}$ 提升为 $H$-丛（$\mathfrak{F}_{H_{ad}}$ 是沿 $B_{ad}\to H_{ad}$ 的前推）。一般情形有典范同构 $\mathfrak{F}_{H_{ad}}\xrightarrow{\sim}\lambda\omega_X$，其中 $\lambda\omega_X$ 是 $\omega_X$ 沿 $\lambda:\mathbb G_m\to H_{ad}$ 的前推，$\lambda(t)$ 在每个 $\mathfrak g^{\alpha}$（$\alpha$ 单正根）上乘以 $t$；构造用到固定的 $y_{\alpha}$。存在唯一同态 $\lambda^{\#}:\mathbb G_m\to H$ 使 $\lambda^{\#}(t)\bmod Z=\lambda(t)^2$（式 (54)）——因为 $\lambda$ 对应余权 $\check\rho$（基本余权之和），而 $2\check\rho$ 属于余根格。取 $\omega_X$ 的平方根 $\mathcal L$（即 $\mathcal L^{\otimes2}\cong\omega_X$），把 $\mathfrak{F}_{H_{ad}}=\lambda\omega_X$ 提升为 $H$-丛 $\lambda^{\#}\mathcal L$，就得到截面。固定 $\mathcal L\in\omega^{1/2}(X)$ 后，有等价 $\Phi_{\mathcal L}:\operatorname{Op}_{\mathfrak g}(X)\times Z\operatorname{tors}(X)\xrightarrow{\sim}\operatorname{Op}_G(X)$（式 (55)）：先用 $\mathcal L$ 把 $\mathfrak F$ 提升为 $G$-oper，再用 $Z$-torsor $\mathcal E$ 扭它。对 $\mathcal L$ 的依赖为 $\Phi_{\mathcal L\otimes\mathcal A}(\mathfrak F,\mathcal E)=\Phi_{\mathcal L}(\mathfrak F,\mathcal E\cdot\alpha\mathcal A)$，其中 $\mathcal A$ 是 $\mathcal O_X$ 的平方根（即 $\mu_2$-torsor），$\alpha:\mu_2\to Z$ 是 $\lambda^{\#}$ 在 $\mu_2$ 上的限制（式 (56)）。§3.1.11 另给出 $\mathfrak g$-oper 与局部系统的关系：$X$ 完备时 $\operatorname{Op}_{\mathfrak g}(X)$ 是概形，经 (43) 同构于仿射空间，且 $i:\operatorname{Op}_{\mathfrak g}(X)\to\operatorname{LocSys}_G$ 是闭嵌入，像是开子栈 $U$（不能约化到非平凡抛物子群、无非平凡自同构的局部系统）的 Lagrange 子簇。

**记号**：$G_{ad}=G/Z$：伴随群；$B_{ad}=B/Z$，$H_{ad}=H/Z$：相应的 Borel 与嘉当群、$\mathfrak g^{\alpha}$：单负根 $\alpha$ 的根空间（一维）；$y_{\alpha}\in\mathfrak g^{\alpha}$ 是固定非零元、$\lambda:\mathbb G_m\to H_{ad}$：在每个 $\mathfrak g^{\alpha}$（$\alpha$ 单正根）上乘 $t$ 的同态，对应余权 $\check\rho$、$\lambda^{\#}:\mathbb G_m\to H$：$\lambda$ 的提升，满足 $\lambda^{\#}\bmod Z=\lambda^2$（对应 $2\check\rho\in$ 余根格）、$\omega^{1/2}(X)$：$\omega_X$ 的平方根构成的群胚；$\mathcal L^{\otimes2}\cong\omega_X$、$Z\operatorname{tors}(X)$：$X$ 上 $Z$-torsor 的群胚；$Z\operatorname{tors}_{\theta}(X)$ 是带 $\theta$-结构（$\omega_X$ 的平方根）的版本

## 关键点

- 定义是「忘记中心」：$\mathfrak g$-oper 就是伴随群的 oper，因此 §3.1.3 的条件里不再出现 $Z$；反过来要从 $\mathfrak g$-oper 恢复 $G$-oper，必须补上中心的数据。
- 投影 $\operatorname{Op}_G(X)\to\operatorname{Op}_\mathfrak g(X)$ 没有典范截面：提升 $B_{ad}$-丛到 $B$-丛等价于提升 $H_{ad}$-丛到 $H$-丛，而 $\mathfrak F_{H_{ad}}$ 只典范同构于 $\lambda\omega_X$，要把它抬成 $H$-丛必须先把 $\omega_X$ 开平方。
- 式 (54) 的平方不可省：$\lambda$ 只到 $H_{ad}$，而 $H$-丛需要 $\lambda^{\#}$；$\lambda^{\#}\bmod Z=\lambda^2$ 可行的原因是 $\lambda$ 对应 $\check\rho$、$2\check\rho$ 落在余根格内，于是 $\lambda^2$ 才能被 $H$ 的整值权看见。
- 固定 $\mathcal L$ 之后，$\Phi_{\mathcal L}$ 是代数栈的同构 $\operatorname{Op}_\mathfrak g(X)\times Z\operatorname{tors}(X)\cong\operatorname{Op}_G(X)$：第一个因子给「oper 的骨架」，第二个因子给「中心 torsor 的扭」，两者独立。
- 换 $\mathcal L$ 的代价由 $\alpha:\mu_2\to Z$ 度量：$\mathcal L\mapsto\mathcal L\otimes\mathcal A$ 时截面变号（扭一个 $\alpha\mathcal A$），故 $\Phi$ 的选取只在 $\mu_2$ 的层面上不确定。注 (ii) 指出 $\alpha$ 恰是主同态 $\mathrm{SL}_2\to G$ 限制到中心 $\mu_2\subset\mathrm{SL}_2$。
- 与局部系统的接口在 §3.1.11：$i:\operatorname{Op}_{\mathfrak g}(X)\to\operatorname{LocSys}_G$ 是闭嵌入、像为 $U$ 的 Lagrange 子簇；$G$-oper 相对 $\mathfrak g$-oper 多出的 $Z\operatorname{tors}$ 正是「忘掉旗与中心」的自由度。

## 公式

```latex
\lambda^{\#}(t)\ \operatorname{mod}Z=\lambda(t)^{2}
```
```latex
\Phi_{\mathcal{L}} : \operatorname{Op}_{\mathfrak{g}}(X)\times Z\operatorname{tors}(X)\xrightarrow{\ \sim\ }\operatorname{Op}_{G}(X)
```
```latex
\Phi_{\mathcal{L}\otimes\mathcal{A}}(\mathfrak{F},\mathcal{E})=\Phi_{\mathcal{L}}(\mathfrak{F},\mathcal{E}\cdot\alpha\mathcal{A})
```
```latex
\alpha : \mu_{2}\longrightarrow Z,\qquad \alpha:=\lambda^{\#}|_{\mu_{2}}
```
```latex
i:\operatorname{Op}_{\mathfrak{g}}(X)\longrightarrow\operatorname{LocSys}_G
```

## 常见错误

- 把 $G$-oper 与 $\mathfrak g$-oper 当成同一个模空间：$\operatorname{Op}_\mathfrak g(X)$ 是概形（仿射空间），$\operatorname{Op}_G(X)$ 是代数栈；二者相差整个 $Z\operatorname{tors}(X)$ 因子。把 $Z$ 当平凡就会在 §4.0 中读不懂 $\operatorname{Op}_{{}^{L}G}(X)=\operatorname{Op}_{{}^{L}\mathfrak g}(X)\times Z\operatorname{tors}_\theta(X)$ 为何需要 torsor 因子。
- 把 (54) 写成 $\lambda^{\#}\bmod Z=\lambda$：少了平方就无法把 $\lambda$ 的 $H_{ad}$-值抬到 $H$；源码特别说明 $\lambda$ 对应 $\check\rho$、$2\check\rho$ 属余根格，平方正是整性所在。写成一次方会得到不存在的同态。
- 以为截面与 $\mathcal L$ 无关：$\Phi_{\mathcal L}$ 显式依赖 $\mathcal L$，换 $\mathcal L$ 要扭 $\alpha\mathcal A$；把截面当成典范的，就会把 $\mu_2$-层面的不确定当成零，从而漏掉 (56) 与注 (ii)。
- 在 $\omega_X$ 没有平方根时仍套用 (55)：该式对固定的 $\mathcal L\in\omega^{1/2}(X)$ 陈述，群胚为空时无对象可谈；这时应改用 §3.4.3 的 $Z\operatorname{tors}_\theta(X)$ 表述（$\theta$ 就是 $\omega_X$ 的平方根），它把 $\mathcal L$ 纳入对象。
- 把注 (iii) 忽略：$G$ 约化非半单时不能直接对 $G$ 用 (55)，要先复合 $\operatorname{Op}_\mathfrak g(X)\to\operatorname{Op}_{[G,G]}(X)\to\operatorname{Op}_G(X)$，并把 $Z\operatorname{tors}$ 换成带联络的 $Z^{\nabla}\operatorname{tors}$。

## 批注

### 易错预警：平方根是几何数据，不是符号游戏

$\omega^{1/2}(X)$ 是一个群胚：对象是满足 $\mathcal L^{\otimes2}\cong\omega_X$ 的线丛，态射是保持同构的同构。它可能为空（例如 $\omega_X$ 在 $\operatorname{Pic}$ 中不是平方元时），此时 (55) 作为「固定 $\mathcal L$ 的等价」没有对象可谈，但投影 $\operatorname{Op}_G\to\operatorname{Op}_\mathfrak g$ 仍然存在——只是没有截面。§3.4.3 用 $Z\operatorname{tors}_\theta(X)$（对象写成 $\mathcal E\cdot\mathcal L$）正是为了把 $\mathcal L$ 与 $\mathcal E$ 打包，使陈述在 $\omega_X$ 无平方根时依然有意义。

### 含糊点拨：为什么多出来的恰是 Z-torsor 而不是别的

提升链是 $B_{ad}$-丛 $\rightsquigarrow$ $B$-丛 $\rightsquigarrow$ $H$-丛；前一步的障碍与后一步相同，而 $H$-丛相对 $H_{ad}$-丛的差异由核 $Z$ 控制：两个 $H$-丛若前推到 $H_{ad}$ 后同构，它们相差一个 $Z$-torsor 的扭。因此「所有提升」构成一个 $Z\operatorname{tors}(X)$-torsor，而不是 $H$-丛的模空间。这也解释了 (55) 为何是「乘以」一个群胚而不是「纤维化」：$\operatorname{Op}_\mathfrak g$ 是底，$Z\operatorname{tors}$ 是纤维。

### 背景直觉：局部系统的 Lagrange 像

§3.1.11 注 iii 把 $\operatorname{Op}_{\mathfrak g}(X)$ 通过 $i$ 闭嵌入 $\operatorname{LocSys}_G$，像落在开子栈 $U$（不可约化、无自同构）里，且是 $U$ 的 Lagrange 子簇，$i(\operatorname{Op}_\mathfrak g)=\pi^{-1}(S)$ 其中 $\pi$ 忘掉联络、$S$ 是 $\mathrm{Bun}_G$ 中与 $\mathfrak F_G^0$ 同构的局部闭子栈。这条几何图像说明：oper 是「联络方向上的一半」，而 $G$-oper 相对 $\mathfrak g$-oper 的中心 torsor 只影响 $\mathrm{Bun}_G$ 一侧的 $S$，不影响辛结构。§4.0 给 ${}^{L}G$-oper 配线丛 $\lambda_{\mathfrak F}$ 时正是沿这条分解走的。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §3.4.1–§3.4.2；印刷页 [73, 75] / PDF 页 [73, 75]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch03.tex:251-283`
- $G_{ad}$ 设定在 p.73，式 (54) 与 (55) 在 p.74，注 (iii) 跨到 p.75；本书 PDF 页 = 印刷页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §3.1.11；印刷页 [66, 67] / PDF 页 [66, 67]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch03.tex:95-104`
- Op_G 作为光滑代数栈一句在 p.66，闭嵌入与 Lagrange 子簇的断言跨到 p.67（\SourcePage{67} 在注 iii 行内）；本书 PDF 页 = 印刷页。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
