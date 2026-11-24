# ch03（Whittaker）审读：问题清单

范围：`src/chapters/ch03.tex` 全 196 行（原 PDF p19–p26；p19 的章首与 §3.1 在 `work/en/ch02_en.txt` 末尾）。
逐句对照 `work/en/ch03_en.txt`，公式全部按 p019–p026 的 PNG 复核。

结论：P1 1 条（38 行，公式符号错）；P2 0 条。其余章节（3.1–3.10）未发现误译、漏译、增译、逻辑反转或公式/编号错误。

## ch03.tex:38（原 PDF p20）
- 原文：In the Tate-twist convention this is denoted γx = σ((n−1)/2)(Frx).
- 原译：采用 Tate 扭转的约定时，记为 $\gamma_x=\sigma(-(n-1)/2)(\Fr_x)$。
- 类型：公式
- 改法：采用 Tate 扭转的约定时，记为 $\gamma_x=\sigma((n-1)/2)(\Fr_x)$。
- 理由：p020 PNG 上指数为正的 $(n-1)/2$，负号是多出来的；代入上一行刻画式会得到 $\Tr(\bigwedge^d\gamma_x)=q_x^{-d(n-1)/2}\Tr(\bigwedge^d\sigma(\Fr_x))$，与原式 $q_x^{d(n-1)/2}$ 自相矛盾，也与下一行"同一特征值为 $q_x^{-d(d-1)/2}\Tr(\bigwedge^d\gamma_x)$"对不上。
