# ch13 待注点（Whittaker 系数的保守性，原 PDF p64–p67）

## 待注 ch13.tex:4（原 PDF p64）
- 原文：In the de Rham form of categorical Langlands one expects DMod(Bun_G) ≃ IndCoh_Nilp(LocSys_Ǧ), and DMod(Bun_G)_temp ≃ QCoh(LocSys_Ǧ).
- 概念：IndCoh（ind-凝聚层）与“幂零奇异支撑”子范畴；谱叠 LocSys_Ǧ 上的全局幂零锥；“温和 ↔ 拟凝聚”这条对应。
- 读者缺什么：全书没有定义 IndCoh_Nilp（谱侧 ind-凝聚层中支撑落在全局幂零锥内的部分），也没说清为什么 de Rham 侧用 IndCoh 而温和部分退化为 QCoh；读者会卡在“Nilp 是哪个锥、为什么 tempered 就该是拟凝聚层”。
- 建议来源：nLab “geometric Langlands correspondence”、“ind-coherent sheaf”；原书文献 [Gai18]、[FR25]。

## 待注 ch13.tex:31（原 PDF p64）
- 原文：For c = coeff this is Coeff^ren. Its counit, or global-sections, shadow recovers the scalar coefficient:
- 概念：重整化 Whittaker 系数——把标量泛函沿谱作用经余作用 coact 提升为 QCoh(LocSys_Ǧ)-值泛函，余单位 Γ(LocSys_Ǧ,−) 再回到标量。
- 读者缺什么：“重整化”在此首次出现且无一字解释：为何要把标量系数换成 QCoh-值对象、coact 从何而来、刚性假设下“标量函子 ↔ QCoh-线性函子”为何等价，读者只能靠猜。
- 建议来源：nLab “geometric Langlands correspondence”；原书文献 [Gai18]、[FR25]。

## 待注 ch13.tex:52（原 PDF p65）
- 原文：For a G(K)-category C, the expected reconstruction map is Wh(DMod(G(K))) ⊗_BiWhit(G) Wh(C) → C.
- 概念：双 Whittaker 范畴 BiWhit(G) 作为张量“基环”、Wh(C) 作为其模，以及重构映射；“C 温和 ⟺ 重构映射的像是整个 C”。
- 读者缺什么：讲义只给公式，未说明 BiWhit(G) 为何能充当基环、⊗_{BiWhit(G)} 是什么张量积、全忠实性来自何处（[Gai18] 的定理），也没交代这个“温和”与 13.1 中谱定义的对应。
- 建议来源：nLab “geometric Langlands correspondence”；原书文献 [Gai18]、[FR23]。

## 待注 ch13.tex:90（原 PDF p66）
- 原文：A key microlocal theorem in the nilpotent sheaf setting [FR25, NT25] says Shv_{Nilp_irreg}(Bun_G) = Shv_Nilp(Bun_G)_{anti-temp} as full subcategories.
- 概念：反温和子范畴 anti-temp 及其微局部刻画——奇异支撑不撞一般正则幂零轨迹。
- 读者缺什么：anti-tempered 没有定义（由谱 Hecke 作用的负向部分给出），读者无法理解为何“支撑落在 Nilp_irreg 内”就等价于“反温和”，也看不出这条定理随后如何把 SS(F) ⊂ Nilp_irreg 直接读成 F 反温和、从而与温和子范畴交为零。
- 建议来源：nLab “perverse sheaf”、“singular support”；原书文献 [FR25]、[NT25]。

## 待注 ch13.tex:104（原 PDF p67）
- 原文：The Færgeman–Raskin microlocal index theorem gives [FR25] χ(coeff(F)) = (−1)^{dim Bun_G} c_{Nilp_Kos}(F).
- 概念：微局部指标定理——Whittaker 系数的 Euler 特征等于特征圈在 Kostant 分支上的重数；以及 13.5 所说“Nilp_Kos 是指数 Whittaker 核的影子”（Lagrange 图像 dψ 与 Lagrange 对应复合）。
- 读者缺什么：特征圈、微茎与重数的定义都没给，读者不知道右边为何是一个整数重数、dim Bun_G 的符号从何而来；“核的影子”更像比喻，缺了“微支撑沿对应复合”这一步。
- 建议来源：nLab “characteristic cycle”、“microsupport”；原书文献 [FR25]、[NT25]。

## 待注 ch13.tex:112（原 PDF p67）
- 原文：The geometric Casselman–Shalika formula says coeff_D(F) ≃ coeff(V^D ⋆ F).
- 概念：几何 Casselman–Shalika 公式（Whittaker 系数与 Hecke 平移的关系）；V^D ∈ Rep(Ǧ)_Ran 的因子化延拓；D-移位 Whittaker 叠。
- 读者缺什么：V^D 在 Ran 空间上如何因子化延拓、⋆ 是什么卷积都未交代；经典 Casselman–Shalika 公式（Whittaker 函数 = 常数项乘 L 因子）这一对照也缺席，读者只能记住一个符号等式。
- 建议来源：nLab “Casselman-Shalika formula”；原书文献 [FR25]、[Gai18]。
