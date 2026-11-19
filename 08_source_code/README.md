# 08_source_code —— 译本的完整工程（源码 + 工程文件）

每部译本一个目录，保留翻译工程**可重建的全部内容**，**不含任何 PDF（原文与成品都在别处/未发布）**。

```
08_source_code/<编号>_<中文名>/
  投稿信息.md          原书信息、译者、版本、分类
  工程文件/            BRIEF、STYLE_GUIDE、构建脚本（build.ps1/check.py/pack.py）、
                      deliverable/（交付清单、工程总结、术语表、译注汇总、校对记录）、
                      reports/（逐章报告、图表审计）
  源码/                LaTeX 工程：main.tex、preamble.tex、chunks/*.tex、figures/*.png
```

- 只要装了 TeX Live / MiKTeX，进 `源码/` 执行 `xelatex main.tex` 就能重建中文译注本。
- 图（`源码/figures/*.png`）是从原书页面裁切/复算得到的，随源码一起提供以保证可编译。
- **用途**：学习、研究、改进翻译流程；**禁止任何商业用途**。译文版权归译者，原始文献版权归原作者与出版方。

## 统计

- 工程数：**87**
- 文件数：**4360**
- 体积：**191.7 MB**
