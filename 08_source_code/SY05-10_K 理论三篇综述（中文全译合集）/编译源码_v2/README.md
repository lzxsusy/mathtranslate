# SY05-10 v2.0 编译源码

本目录是《K 理论三篇综述》v2.0 的 LaTeX 源码、清理后的中文 Markdown、矢量图与构建脚本，供复现与校订使用。

## 目录

| 目录 | 内容 |
|---|---|
| `witten/` | Witten 分册：`witten.tex`（主文件）、`witten_body.tex`（正文）、`witten_clean.md`（去 front matter 的底稿）、三件套 |
| `moore/` | Moore 分册：`moore.tex`、`moore_clean.md`、`fig01–fig12.pdf`（从原文 PDF 矢量裁切）、三件套 |
| `olsen_szabo/` | Olsen–Szabo 分册：`olsen.tex`、`olsen_clean.md`、`fig01.pdf`、三件套 |
| `tools/` | `build_moore.py`、`build_olsen.py`、`crop_figs.py`、`fix_witten_v2.py`（脚本内路径为本机绝对路径，复现时需改） |

## 编译

```bash
cd witten && xelatex -interaction=nonstopmode witten.tex && xelatex -interaction=nonstopmode witten.tex
cd moore && xelatex -interaction=nonstopmode moore.tex && xelatex -interaction=nonstopmode moore.tex
cd olsen_szabo && xelatex -interaction=nonstopmode olsen.tex && xelatex -interaction=nonstopmode olsen.tex
```

需要 `ctex`（XeLaTeX）、`amsmath`、`graphicx`、`float`、`caption`、`fancyhdr`、`enumitem`、`longtable`、`booktabs`、`array`、`calc`。图均为矢量 PDF，不依赖 Ghostscript。

## 说明

- 中文底稿沿用旧版 Markdown（在投稿包内，未随本目录分发），逐段对照原文校订后转 LaTeX；不是从零重译。
- 旧版 123 页 PDF 已撤下，不随本目录提供。
- Olsen–Szabo 分册的公式未逐式编号，见该目录 `疑点清单.tsv` 第 7 条。
