# 译文修订 section-12-ef.tex:106

> `seidel/correction/a07-section-12-ef-106` ｜ 原书 p.183 ｜ draft

**一句话**：初版「$c_u$ 的末项 $\longrightarrow\R.$」改为「$\longrightarrow\K.$」：原书 p183 作 → K，同段链映射已取值于 K，$c_u$ 正是把 $|c|_\K$ 逐项求和的对象。

**自测**：初版这里错在哪，为什么必须改？

## 初版

```
c_u:o(\Lambda_{y,0}^\#,\Lambda_{y,1}^\#\otimes\lambda^{\mathrm{top}}(\Lambda_{y,1}))\longrightarrow\R.
```

## 改后

```
末项改为 `\longrightarrow\K.`
```

## 为什么改

原书 p183 作 `cu: o(Λ#_{y,0}, Λ#_{y,1}⊗λtop(Λ_{y,1})) → K`。同段上文链映射已取值于 $\K$，$c_u$ 正是用来把 $|c|_\K$ 逐项求和的对象；若取值于 $\R$，规范化和与 $\mu^d$ 的 $\pm1$ 系数都无从谈起，与全段自相矛盾。

## 补注

见分章报告 A07 修订表第 1 行（report-A07.md 第 32 行）；修订总表第 14 条（section-12-ef.tex:106，印刷页 183）。修订总表该行 reason 末尾被截断（止于「用来把」三字），why 据报告补全；original/corrected 与 TSV 逐字一致（含末项的反引号）。

## 易错点

- 只看改后的句子不足以判断对错；须对照原书同一页的公式与上下文。
- 术语改动要全书统一，不能只改这一处。

## 参考与关联

- Seidel, Fukaya categories and Picard–Lefschetz theory，校订，p.183–183（原书 p.183）

关联：`seidel/concept/fukaya-category`、`seidel/concept/a-infinity-category`

来源说明：据修订总表、分章报告与原书印刷页图逐条核对（PDF 页 = 印刷页 + 8）；页码已回页确认。
