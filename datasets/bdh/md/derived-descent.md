# 导出范畴的下降

- **id**：`bdh/concept/derived-descent`
- **类型**：concept
- **位置**：§7.4
- **问题**：为什么不能直接取 $\mathcal{M}(\mathcal{Y})$ 的普通导出范畴，而要在超覆叠上做同伦逆向极限？

> 把光滑栈的超覆叠看作 $(\Delta)$ 上的范畴族，用余笛卡儿截面与 $c_{\pm}$ 的伴随等价造出以 $\mathcal{M}(\mathcal{Y})$ 为核心的 t-范畴 $D(\mathcal{Y})$，使 $\mathcal{D}$-模导出范畴不依赖覆盖。

## 定义

设 $(\Delta)$ 是非空有限全序集 $\Delta_{n}=[0,n]$ 与递增单射构成的范畴。$(\Delta)$ 上的一族余纤维化阿贝尔范畴 $\mathcal{M}_{\cdot}$（每个 $\alpha_{\cdot}:\mathcal{M}_{n}\to\mathcal{M}_{m}$ 正合）的余笛卡儿截面是资料 $M=\{M_{n},\alpha^{*}\}$，其中 $\alpha^{*}:\alpha_{\cdot}M_{n}\xrightarrow{\sim}M_{m}$ 是同构且满足 $(\alpha\beta)^{*}=\alpha^{*}\alpha_{\cdot}(\beta^{*})$；这些截面构成阿贝尔范畴 $\mathcal{M}_{\mathrm{tot}}$（7.4.1）。目标是造出以 $\mathcal{M}_{\mathrm{tot}}$ 为核心的 t-范畴 $D_{\mathrm{tot}}(\mathcal{M}_{\cdot})$，并使 (312) 成立：对 $M,N\in\mathcal{M}_{\mathrm{tot}}$ 存在收敛到 $\operatorname{Ext}^{p+q}_{D_{\mathrm{tot}}(\mathcal{M}_{\cdot})}(N,M)$ 的典范谱序列，$E^{p,q}_{1}=\operatorname{Ext}^{q}_{\mathcal{M}_{p}}(N_{p},M_{p})$。构造先放宽同构要求：$\sec_{+}$ 的对象 $M=(M_{n},\alpha^{*})$ 只要求 $\alpha^{*}:\alpha_{\cdot}M_{n}\to M_{m}$ 满足粘合条件，$\sec_{-}$ 用对偶定义；在复形范畴 $C\sec_{\pm}$ 上有一对伴随 DG 函子 $c_{+}:C\sec_{-}\to C\sec_{+}$、$c_{-}:C\sec_{+}\to C\sec_{-}$（313），其中 $c_{-}$ 把 $M$ 送到单纯形 $\Delta_{m}$ 上的全上链复形 $C^{\cdot}(\Delta_{m},\widetilde{M}_{m})$，伴随性由 (314) 给出。引理 7.4.4 说 $c_{\pm}$ 保持拟同构且两个伴随态射都是拟同构，故 $D\sec_{+}\cong D\sec_{-}=D\sec$。再取所有 $\alpha^{*}$ 都是拟同构的对象，得到三角子范畴 $D_{\mathrm{tot}\pm}\subset D\sec$；引理 7.4.6 与 7.4.7 证明两者在 $D\sec$ 中重合，记公共范畴为 $D_{\mathrm{tot}}$，其核心正是 $\mathcal{M}_{\mathrm{tot}}$，并带非退化 t-结构。几何上的输入是 7.5.1：对任意光滑栈 $\mathcal{Y}$ 取容许超覆叠 $U_{\cdot}$（各 $U_{n}$ 是光滑拟紧分离代数空间的无交并），$\mathcal{M}(U_{\cdot})$ 是 $(\Delta)$-族且 $\mathcal{M}_{\mathrm{tot}}=\mathcal{M}(\mathcal{Y})$，而 $\Omega$ 给出范畴等价 $\Omega:D_{\mathrm{tot}}(U_{\cdot},\mathcal{D})\to D_{\mathrm{tot}}(U_{\cdot},\Omega)$（315）；7.5.2 与 7.5.3 再把 $D_{\mathrm{tot}}(U_{\cdot},\Omega)$ 与整体定义的 $D(\mathcal{Y},\Omega)$ 等同，于是 $D(\mathcal{Y})$ 不依赖超覆叠的选取。

**记号**：$(\Delta)$：非空有限全序集 $\Delta_{n}=[0,n]$ 与递增单射构成的范畴、$\mathcal{M}_{\mathrm{tot}}$：余笛卡儿截面范畴，即把所有 $\alpha_{\cdot}M_{n}$ 沿 $\alpha^{*}$ 粘起来的对象、$\sec_{\pm}$：$\alpha^{*}$ 只要求为态射（$\sec_{+}$）或对偶形式（$\sec_{-}$）的截面范畴；$\mathcal{M}_{\mathrm{tot}}\subset\sec_{+}$、$D^{\mathrm{fake}}_{\mathrm{tot}}$：逐项导出范畴 $D(\mathcal{M}_{n})$ 的余笛卡儿截面，原文强调它不是三角范畴、$D(\mathcal{Y})$：$D_{\mathrm{tot}}(U_{\cdot},\mathcal{D})\cong D_{\mathrm{tot}}(U_{\cdot},\Omega)$ 对容许覆盖的公共值

## 关键点

- 式 (312) 就是 $D_{\mathrm{tot}}$ 的定义性质：$E^{p,q}_{1}=\operatorname{Ext}^{q}_{\mathcal{M}_{p}}(N_{p},M_{p})\Rightarrow\operatorname{Ext}^{p+q}_{D_{\mathrm{tot}}}(N,M)$；7.4.8 把它实现为 $Hom(N,M)$ 上滤链的谱序列，其分次片满足 $gr^{n}_{F}RHom(N,M)\to RHom(N_{n},M_{n})[-n]$ 是拟同构。
- $c_{-}$ 有显式公式 $(c_{-}M)^{\cdot}_{m}=\bigoplus_{\alpha:\Delta_{n}\to\Delta_{m}}\alpha_{\cdot}M_{n}^{\cdot-n}$，伴随性由同态复形 (314) 的显然等同 $Hom(c_{+}N,M)\cong Hom(N,M)\cong Hom(N,c_{-}M)$ 给出；引理 7.4.4 保证 $c_{\pm}$ 在导出范畴上互逆。
- 7.4.7：$D_{\mathrm{tot}+}$ 与 $D_{\mathrm{tot}-}$ 在 $D\sec$ 中重合，$D_{\mathrm{tot}}$ 以 $\mathcal{M}_{\mathrm{tot}}$ 为核心带非退化 t-结构，嵌入 $D_{\mathrm{tot}}\to D\sec$ 对两个 t-结构都 t-正合，且核心等于 $\sec_{+}\cap\sec_{-}$。
- 7.5.1：对任意光滑栈都有容许超覆叠，$\mathcal{M}(U_{\cdot})$ 的余笛卡儿截面就是 $\mathcal{M}(\mathcal{Y})$；$\Omega_{n}(M_{n}):=\Omega M_{n}[-\dim U_{n}/\mathcal{Y}]$ 给出 (315) 的正合函子，虽然 $\mathcal{D}$ 不与纤维范畴结构相容，它仍给出逆函子。
- 7.5.2 与 7.5.3：不同容许覆盖给出的 $D_{\mathrm{tot}}$ 典范等同，且 $r:D(\mathcal{Y},\Omega)\to D_{\mathrm{tot}}(U_{\cdot},\Omega)$ 是范畴等价（逆函子用 Čech 全复形 $\pi_{\cdot}F$，投影仿射性来自条件 (310)）；7.5.4 说明当 $\mathcal{Y}$ 对角仿射时这与 7.3.12 的 $D(\mathcal{Y})$ 一致。

## 公式

```latex
E^{p,q}_{1}=\operatorname{Ext}^{q}_{\mathcal{M}_{p}}(N_{p},M_{p})\ \Rightarrow\ \operatorname{Ext}^{p+q}_{D_{\mathrm{tot}}(\mathcal{M}_{\cdot})}(N,M)
```
```latex
(c_{-}M)^{\cdot}_{m}=\bigoplus_{\alpha:\Delta_{n}\to\Delta_{m}}\alpha_{\cdot}M_{n}^{\cdot-n}
```
```latex
Hom(c_{+}N,M)\xrightarrow{\ \sim\ }Hom(N,M)\xleftarrow{\ \sim\ }Hom(N,c_{-}M)
```
```latex
gr^{n}_{F}RHom(N,M)\xrightarrow{\ \sim\ }RHom(N_{n},M_{n})[-n]
```

## 定理

**命题 7.5.2（下降不依赖覆盖）**：对光滑栈 $\mathcal{Y}$ 的任意两个容许超覆叠 $U_{\cdot}$、$U'_{\cdot}$，t-范畴 $D_{\mathrm{tot}}(U_{\cdot})$ 与 $D_{\mathrm{tot}}(U'_{\cdot})$ 之间存在典范等同。

证明：略证（§7.5.2、§7.5.5，原书 p.257–260）

- 取 $\mathcal{Y}$ 上的 $(\Delta)^{\circ}\times(\Delta)^{\circ}$-代数空间 $V_{\cdot\cdot}$，连同光滑 $\pi:V_{mn}\to U_{m}$ 与仿射 $\pi':V_{mn}\to U'_{n}$，使 $\pi'_{\cdot n}:V_{\cdot n}\to U'_{n}$ 是超覆叠
- 对 $F\in K_{\mathrm{tot}+}(U_{\cdot},\Omega)$ 置 $\Phi_{V_{n}}F:=\pi'_{\cdot}F_{V_{n}}$，得到 t-正合函子 $\Phi_{V}:D_{\mathrm{tot}}(U_{\cdot},\Omega)\to D_{\mathrm{tot}}(U'_{\cdot},\Omega)$，它在核心 $\mathcal{M}(\mathcal{Y})$ 上诱导恒等
- 用公共加细 $V\supset V_{1},V_{2}$ 的拟同构 $\Phi_{V}F\to\Phi_{V_{i}}F$ 证明 $\Phi_{V}$ 不依赖 $V$，得 $\Phi_{UU'}$；再用 $\Phi_{UU''}=\Phi_{U'U''}\Phi_{UU'}$ 与 $\Phi_{UU}=\mathrm{id}$ 得典范等同

缺口：原文把不依赖辅助数据 $V$ 与三角函子相容性的验证留给读者。

**引理 7.5.3（超覆叠上的限制是等价）**：设各 $U_{n}$ 为仿射概形，则限制函子 $r:D(\mathcal{Y},\Omega)\to D_{\mathrm{tot}}(U_{\cdot},\Omega)$ 是范畴等价。

证明：略证（§7.5.3，原书 p.258）

- 对 $F\in K_{\mathrm{tot}+}(\Omega)$ 取各项为 $\pi_{\cdot}F^{ab}:=\pi_{b}(F^{a})$ 的 Čech 双复形的全复形 $\pi_{\cdot}F$，得到正合函子 $\pi_{\cdot}:K_{\mathrm{tot}+}(\Omega)\to K(\mathcal{Y},\Omega)$
- 由 (310)，投影 $\pi_{b}$ 仿射，故 $\pi_{\cdot}$ 保持 $\mathcal{D}$-拟同构，下降为 $D_{\mathrm{tot}}(U_{\cdot},\Omega)\to D(\mathcal{Y},\Omega)$
- 用 $C\sec_{-}(U_{\cdot},\Omega)$ 中的典范态射 $\pi'_{\Omega}\pi_{\cdot}F\to c_{-}F$ 验证它是 $r$ 的逆

缺口：逆函子的验证原文留给读者。

## 常见错误

- 把 $D_{\mathrm{tot}}$ 误当成 $D(\mathcal{M}_{\mathrm{tot}})$ 的普通导出范畴：普通导出范畴只记得 $\mathcal{M}_{\mathrm{tot}}$ 的复形，丢掉了 $\alpha^{*}$ 的同伦信息，因而得不到 (312) 的谱序列；7.4.5 的 $D^{\mathrm{fake}}_{\mathrm{tot}}$（逐项导出范畴的余笛卡儿截面）正是这种「假的」对象，原文强调它不是三角范畴。
- 在 $\sec_{+}$ 里提前要求 $\alpha^{*}$ 是同构：那样 $\sec_{+}$ 就退化成 $\mathcal{M}_{\mathrm{tot}}$，$c_{\pm}$ 的伴随等价（7.4.4）与 $D_{\mathrm{tot}\pm}$ 的重合（7.4.6–7.4.7）全部失效，因为证明恰靠「任意态射先经 $c_{-}$ 变成同构型对象」这一自由性。
- 在 $\Omega$ 与 $\mathcal{D}$ 的方向上出错：7.5.1 中与纤维结构相容、能给出 (315) 逆函子的是 $\mathcal{D}$（带平移 $\dim U_{n}/\mathcal{Y}$），而 $\Omega$ 只在导出层面与它互逆；若在 $C(U_{\cdot},\Omega)$ 层就断言二者等价，就与「$\mathcal{D}$ 不与纤维范畴结构相容」直接矛盾，也会把 (315) 的等价性证成循环论证。

## 批注

### 背景直觉：为什么必须是同伦逆向极限

超覆叠上的 Čech 描述只有在 $\mathcal{D}$-拟同构的意义下才有意义：把一个层复形「限制到覆盖再粘回去」时，各层之间的过渡同构只在导出范畴中才是数据。若只在 $\mathcal{M}_{\mathrm{tot}}$ 层面粘，就得到 7.4.5 的 $D^{\mathrm{fake}}_{\mathrm{tot}}$——它甚至不是三角范畴，因为三角结构需要同伦、而逐项截面的余笛卡儿条件与同伦不相容。7.4.5 的 $D^{\mathrm{fake}}_{\mathrm{tot}}$ 与 7.4.7 的 $D_{\mathrm{tot}}$ 的区别正好说明：下降的正确形状是 $\operatorname{holim}$，不是 $\lim$。

### 易错预警：$\epsilon:D_{\mathrm{tot}}\to D^{\mathrm{fake}}_{\mathrm{tot}}$ 只是比较函子

7.4.7 引入 $\epsilon$ 之后紧接着说 $H_{\pm}=H\epsilon$，$H$ 是 $D^{\mathrm{fake}}_{\mathrm{tot}}\to\mathcal{M}_{\mathrm{tot}}$ 的上同调函子；此处容易顺手把 $\epsilon$ 当成等价。它不是：$D^{\mathrm{fake}}_{\mathrm{tot}}$ 没有三角结构，$\epsilon$ 只保留逐项资料 $(M_{n},\alpha_{*})$，而同伦极限额外携带 $c_{-}$ 造出的高阶同伦（见 7.4.3 的 $\nu_{i}$ 彼此同伦并带高阶同伦）。把 $\epsilon$ 当等价，就会得出 $D_{\mathrm{tot}}$ 的 t-结构可以搬到逐项截面上，从而误判 7.4.7 的非退化性。

### 含糊点拨：谱序列里的 $p$ 是单纯形次数，不是几何维数

(312) 的 $E^{p,q}_{1}=\operatorname{Ext}^{q}_{\mathcal{M}_{p}}(N_{p},M_{p})$ 中，$p$ 标号的是 $(\Delta)$ 的对象 $\Delta_{p}=[0,p]$，即超覆叠的 $p$ 重纤维积，不是栈的几何维数；$q$ 才是 $\mathcal{M}_{p}$ 内部的内射维数方向。这一点在 7.4.8 的滤链证明中最清楚：$gr^{n}_{F}=Hom(N_{n},M_{n})[-n]$，位移 $-n$ 直接来自单纯形次数，而不是来自 $\dim U_{n}/\mathcal{Y}$ 的平移（那个平移只出现在 7.5.1 的上同调函子 $H_{\mathcal{D}n}$ 里）。混淆两者会把 (312) 的收敛次数算错一位。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.4.1–7.4.4；印刷页 [251, 252] / PDF 页 [251, 252]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:515-547`
- 原书 p.251–252：\SourcePage{252} 在第 519 行，故 515–518 属 p.251，519–547 属 p.252。本书 PDF 页 = 印刷页。
- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §7.5.1；印刷页 [257, 258] / PDF 页 [257, 258]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch07.tex:630-644`
- 原书 p.257–258：\SourcePage{258} 在第 641 行，630–640 属 p.257，641–644 属 p.258。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
