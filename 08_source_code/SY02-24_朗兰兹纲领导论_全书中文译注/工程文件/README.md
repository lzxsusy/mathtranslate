# 《朗兰兹纲领导论》全书中文译注（SY02-24）

J. Bernstein、S. Gelbart 编 *An Introduction to the Langlands Program*（Birkhäuser, 2004，ISBN 0-8176-3211-5）十二个章节的完整中文译注本。译文逐章编译，章节、公式、定理编号一律沿用原书；每章附通读笔记、疑点清单与带来源的详细译注。

## 交付物

| 文件 | 说明 |
|---|---|
| `SY02-24_朗兰兹纲领导论_全书中文译注.pdf` | 全书成品，234 页，2026-11-23 编译 |
| `译注汇总.md` | 12 章共 154 条译注，含 A/B/I 来源分级 |
| `术语表.tsv` | 126 条术语（英文 / 中文 / 来源） |
| `工程总结.md` | 底本、页次映射、流程、质量数据、遗留问题 |
| `README.md` | 本文件 |

## 底本与页次

底本 PDF 共 283 页，与印刷本相比缺 6 页，故 PDF 页 = 印刷页 + k，k 从 8 逐段递减到 2（第 12 章为 2）。译文引用页码一律用印刷页码；逐章对应见工程文件 `work/PAGE_MAP.md`。

## 编译

```bash
cd src
xelatex main.tex   # 三遍
```

`main.tex` 以 `\InputIfFileExists{chapters/chNN}{}{}` 逐章挂载，缺章不影响编译；`\setcounter{chapter}{N-1}` 保证章号与原书一致。

## 质量

- 2026-11-23 全量编译：**234 页，0 error、0 undefined、0 overfull、0 缺字**（`PunctStyle=kaiming`，`emergencystretch=3.5em`）。
- 12 章、10,878 行 TeX、154 条译注、126 条术语。
- 全部公式逐符号对照 150 dpi 页图核对，未使用文字提取件的公式。

## 权利

底本为在版图书。本工程只作内部译校与语料生产使用，成品 PDF 不入公开仓库（见发布仓 `RELEASE_REGISTER.csv` 与 `COMPLIANCE.md` R3）。
