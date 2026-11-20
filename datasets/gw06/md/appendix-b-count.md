# 记号表条目数误抄成参考文献数（91→70）

- **id**：`gw06/correction/appendix-b-count`
- **类型**：correction
- **位置**：附录B
- **问题**：为什么附录 B 的「91 条」是笔误而不是版本差异？

> 附录 B 开头说「原文共 91 条」，实测原文与中译各 70 条；91 是参考文献的条数，串了行。

## 位置

附录 B 开头，sB-notation.tex:11

## 原文片段

```latex
原文 Appendix B 共 91 条
```

## 改为

```latex
原文 Appendix B 共 70 条
```

## 依据

逐条清点：原文 ramified.tex 第 7618–7705 行的记号表共 70 个条目，中译 sB-notation.tex 的表格也恰为 70 行；而参考文献恰为 91 条（`\ref\key` 54 + `\nref\key` 37）。两处数字相同纯属巧合，抄写时把参考文献的计数写进了附录 B 的开场说明。读者若据此核对「有没有漏译」，会以为漏了 21 条。

## 说明

只改数字，未动表格；70 条已逐条与英文对照，符号与释义一致。

## 批注

### 易错预警：「共 N 条」要数一遍

凡是译文里出现「共 N 条／节／式」的元陈述，都要回到原文实际清点。这类句子不承载数学，校对时最容易被跳过，却是读者最先拿来当核对清单的东西。

## 出处

- S. Gukov & E. Witten, Gauge Theory, Ramification, And The Geometric Langlands Program（arXiv:hep-th/0612073v2）中译校订本 附录B；印刷页 [152] / PDF 页 [153]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/sB-notation.tex:9-13`
- 附录 B 自印刷第 152 页起（PDF 第 153 页）。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
