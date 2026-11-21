# symbol 译作「符号」应为「象征」

- **id**：`bdh/correction/symbol-not-sign`
- **类型**：correction
- **位置**：§3
- **问题**：为什么这里必须译「象征」而不能译「符号」？

> 微分算子的 symbol 在 Sturm–Liouville 段被译成「符号」，与本章其余各处的「象征」不一致。

## 位置

§3.1 ch03.tex:56

## 原文片段

```latex
即符号 $\sigma(\partial)$ 无处为零
```

## 改为

```latex
即象征 $\sigma(\partial)$ 无处为零
```

## 依据

术语表把 symbol（微分算子的主象征）冻结为「象征」，并明确标注「不是符号」；本章 3.1 节其余各处（ch03.tex:50 的「其象征 $\sigma(\partial)\in\Gamma(X,\mathcal{B}\otimes\mathcal{A}^{\otimes(-1)}\otimes\Theta_X^{\otimes n})$ 无处为零」，以及后面几处）都作「象征」。$\sigma(\partial)$ 是主象征层里的截面，不是正负号；译作「符号」会与 sign 混淆，也会让本节把 SL_2-oper 与二阶自伴算子对应起来的构造失去「最高阶项」这层几何含义。

## 说明

译本改译：只改 ch03.tex:56 的「符号」为「象征」；同段 ch03.tex:50 原本已作「象征」，未动。依据是术语表与本章内部一致性。

## 批注

### 易错预警：symbol 不是 sign

微分算子的 symbol 是最高阶项对应的截面 $\sigma(\partial)\in\Gamma(X,\mathcal{B}\otimes\mathcal{A}^{\otimes(-1)}\otimes\Theta_X^{\otimes n})$，住在层里；sign 才是正负号。中文口语把两者都叫「符号」，所以数学文本里必须用「象征」把对象钉死，否则读者会把椭圆性条件读成「正负号处处非零」。

### 背景直觉：为什么这个译名值得较真

「象征无处为零」是椭圆性的定义性条件，也是 3.1 节把 $\mathrm{SL}_2$-oper 与二阶自伴算子对应起来的关键：$\partial$ 的象征就是 oper 的最高阶项。若读成「符号无处为零」，这条对应就只剩形式上的算子等式，看不出它为什么与 $\Theta_X$、$\omega_X$ 的幂次挂钩。

## 出处

- A. Beilinson & V. Drinfeld, Quantization of Hitchin's Integrable System and Hecke Eigensheaves（中译校订本） §3.1；印刷页 [63] / PDF 页 [63]；锚点 `08_source_code/SY02-14_Hitchin可积系统的量子化与Hecke特征层/源码/chapters/ch03.tex:54-58`
- 印刷页=PDF 页；页标记 $\SourcePage{64}$ 在 ch03.tex:62，故 54–58 行整段属 p.63。

---

权利：`rewritten`；核验：`source-only`（2026-11-21）。
