# 审校记录：第 5 章下（5.3–5.5，原书 p.120–p.140 / PDF p.128–p.148）

译者：ch05b-floer。对应源码：`qsg/tex/ch05b-s01.tex`（5.3）、`ch05b-s02.tex`（5.4）、
`ch05b-s03.tex`（5.5）。

体例：**原文照译、不改动**，疑点一律在译文中以 `% [Tutor Note: 原文疑误——…]` 标注；
下表汇总，供教授定夺。页码为**印刷页码**（括号内为 PDF 页码）。

---

## 一、实质性疑误（建议再版时修正）

| # | 位置 | 原文 | 疑点 | 建议改法 |
|---|---|---|---|---|
| 1 | p.120（PDF p.128）例 5.3.1 | `H : [0,1] × S^1 → ℝ` | 本例题的底流形是 $S^2$（标准 2-球面），定义域不应是 $S^1$；上下文（球面上沿 $z$ 轴的旋转、$S^2$ 的 Betti 数 2）都指向 $S^2$ | 改为 `H : [0,1] × S^2 → ℝ` |
| 2 | p.120（PDF p.128）开头 | `#Crit(F) ⩾ Σ_i b_i(X; k)` | $X$ 全文未定义，此处应为底流形 $M$（同页猜想 5.3.1 用的是 $M$） | 改为 `b_i(M; k)` |
| 3 | p.132（PDF p.140）定理 5.4.1 末句 | `HF_*(M,ω,H,J) ≅ H_*(M;k), the classical homology groups of X` | $X$ 未定义，应为 $M$ | 改为 `of M` |
| 4 | p.133（PDF p.141）§5.5 第 2 段 | `... and co-vector p in the fiber over x` | 讨论的是秩 $n$ 的 $\mathbf{k}$-向量丛 $E\to M$，纤维为 $\mathbf{k}^n$，$p$ 是纤维中的**向量**而非余向量 | 改为 `vector p` |
| 5 | p.128（PDF p.136）命题 5.4.1 证明 | “第一项等于”后的链式等式 | 求导式第一项带负号 $-\int_{\mathbb{D}^2}\frac{d}{ds}(\cdots)^*\omega$，而“第一项等于”一行把外层负号丢掉了；链式等式其余各项与最终结论 (5.18) 均正确 | 在“第一项等于”一行前补负号：$-\int_{\mathbb{D}^2}\frac{d}{ds}(\tilde w(s,\cdot))^*\omega\big|_{s=0}=\cdots=-\int_0^1\omega(\xi,\dot x)\,dt$（或不改，但需读者自行补号） |
| 6 | p.136（PDF p.144）$S(t)^{\mathrm T}=S(t)$ 的链式等式 | 中间两行 $(A^{-1})^{\mathrm T}(\Omega A^{-1})'$、$(A^{-1})^{\mathrm T}\Omega\dot A^{-1}$、$\Omega A\dot A^{-1}$ | 按原样逐符号验算，中间两步难以成立（疑为排版/跳步）。结论 $S(t)^{\mathrm T}=S(t)$ 正确 | 建议改用一行式：对 $A^{\mathrm T}\Omega A=\Omega$ 求导得 $\dot A^{\mathrm T}\Omega A+A^{\mathrm T}\Omega\dot A=0$，故 $S^{\mathrm T}=-(A^{-1})^{\mathrm T}A^{\mathrm T}\Omega\dot AA^{-1}=S$ |
| 7 | p.139（PDF p.147）注 5.5.4 | 置于练习 5.5.1 **之前**，却使用参数 $\alpha$ | 该注的 $\alpha$ 是紧接着的练习 5.5.1 中 $H=\pi\alpha(x^2+y^2)$ 的参数；注在前、练习在后，阅读顺序倒置 | 建议把注 5.5.4 移到练习 5.5.1 之后（或改写为“见下题”） |

## 二、文字/拼写小误（不影响数学内容）

| # | 位置 | 原文 | 说明 |
|---|---|---|---|
| 8 | p.120（PDF p.128）猜想 5.3.1 显示式 | `#{fix points of the time-1 map φ_H^1}` | `fix` 应为 `fixed`（漏字）。译文按“不动点”处理 |
| 9 | p.120（PDF p.128） | `the full version this theory is built up in ...` | 漏 `of`：应为 `the full version of this theory` |
| 10 | p.125（PDF p.133）猜想 5.3.7 前 | `Hofer-Wyoscki-Zehnder` | `Wyoscki` 应为 `Wysocki`（P. Wysocki） |
| 11 | p.138（PDF p.146）例 5.5.7 | `It is a Morse function with the only critical point of H is 0` | 语法重复（`with the only critical point ... is 0`）；译文按“唯一临界点是 0”处理 |
| 12 | p.127（PDF p.135）命题 5.4.1 陈述 | `Crit(A_H) = {contractible closed Hamiltonian orbits of {φ_H^t}}` | 严格说 $\mathrm{Crit}(\mathcal{A}_H)\subset\Lambda_0M$ 是**环路**的集合，不是“轨道”的集合；二者在闭轨道意义下可对应，但 $\mathcal{A}_H$ 原本定义在 $(x,w)$ 上。译文照原文，已在 (5.17) 后与命题处加注说明良定义性 |
| 13 | p.132（PDF p.140）(5.22)/(5.23) | (5.22) 用系数域 $\mathbf{k}$，(5.23) 用 $\#_{\mathbb{Z}_2}$ | 两处系数约定不统一（(5.23) 的模 2 计数对应 $\mathbb{Z}_2$ 系数；一般 $\mathbf{k}$/$\mathbb{Z}$ 系数需相干定向）。已在译文批注中指出 |
| 14 | p.126（PDF p.134） | `for any smooth function f : S^2 → M` | $f^*\omega$ 需要的是映射；原文用 `function`，译文按“光滑映射”处理（不视为错误） |

## 三、记号/约定提醒（非疑误，已写入 Tutor Note）

1. **符号约定**：本书取 $\iota_{X_F}\omega=-\dd F$（即 $\omega(X_F,\cdot)=-\dd F$），与不少教材的
   $\iota_{X_H}\omega=\dd H$ 差一符号；(5.17)–(5.21) 的符号均与此配套。核对时以 (5.18)、(5.20)、
   (5.21) 三式为锚点整体核对。
2. **辛非球面条件**：$c_1(\pi_2(M))=0$ 是简写，准确含义是 $c_1$ 在 Hurewicz 像
   $\operatorname{im}(h_2\colon\pi_2(M)\to H_2(M;\mathbb{Z}))$ 上为零。
3. **Conley–Zehnder 与 Robin–Salamon**：$\mu_{\mathrm{CZ}}$ 依赖哈密顿函数（经由 $(\varphi_H^t)_*$），
   沿轨道作定常扰动时只平移一个常数；$\mu_{\mathrm{CZ}}$ 一般不等于 Morse 指标（例 5.5.7：3 对 0）。
4. **谱不变量**：本节只用 Floer 同调的秩，未涉及作用量过滤；谱不变量（Viterbo–Oh）与持续模/条形码
   是保留过滤信息后的定量化对象，不可与 $\mu_{\mathrm{CZ}}$ 混淆（已在定理 5.4.1 后批注）。
5. **Robin–Salamon 指标与 $c_1$ 的系数 2**：更换界定圆盘时
   $\mu_{\mathrm{CZ}}((x,w))-\mu_{\mathrm{CZ}}((x,w'))=2c_1(\overline{w}\#w')$，系数 2 源于
   Maslov 类与第一 Chern 类的换算；不同文献对 $\mu_{\mathrm{CZ}}$ 的规范化不同，引用时须核对。

---

## 四、译名与体例处理

- 5.5 节 "crossing" 译「交点」，"regular crossing" 译「正则交点」，"prime" 译「素的」。
- "Fact 5.5.1" 沿用全书体例写作 `\whead{事实}{5.5.1}`（preamble 无 Fact 环境）。
- 原文例末的 `//` 记号按全书体例排为 `\hfill$\square$`。
- p.120 页首（5.2 节末尾两段）由 ch05a 译者负责（已协调），本文件不重复。
- **待统一的术语**：GLOSSARY 规定 Morse theory 作「莫尔斯理论」，但 ch05a 与本章下半一致使用
  「Morse」（如「Morse 函数」「Morse 同调」「无穷维 Morse 理论」），而 ch06 一律用「莫尔斯」。
  本译者与 ch05a 保持章内一致，取「Morse」；全书统一时建议由 lead 决定后全局替换。

## 五、自检结果

```
python qsg/tools/check.py ch05b
  === ch05b  PDF p128-p148  文件 3 个 ===
  覆盖 21/21 页 | 节 3 | 要点 3 | 批注 35 | 图 11 | 公式编号 14
  结论：无问题
```

另用 TeX Live 2026 对三节做过独立试编译（`qsg/build/test_ch05b.tex`，17 页）：
无 `!` 错误、无缺字（Missing character）、无 >30pt 的 overfull hbox。
