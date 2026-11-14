import re

# ---------------- README ----------------
p = "README.md"
t = open(p, encoding="utf-8").read()

t = t.replace("| 源码 | `CS and Knots.tex`（单文件，1,792 行，约 199 KB，UTF-8）+ `figures/` 5 张 PNG |",
              "| 源码 | `CS and Knots.tex`（单文件，1,793 行，约 199 KB，UTF-8）+ `figures/` 5 张 PNG |\n"
              "| 成品 PDF | `CS and Knots_中文译注本.pdf`（**43 页**，XeLaTeX 两遍实测编译，0 error、0 缺字） |")

t = t.replace("## 8. 校验记录（重要：编译验证未完成）", "## 8. 校验记录（已实测编译）")

old_start = t.index("**本机没有安装任何 TeX 发行版**")
old_end = t.index("已完成的静态审计")
new_para = (
    "**已实测编译**：本机原先没有 TeX 发行版，为出 PDF，我下载并解压了一份便携 **TinyTeX**（TeX Live 2026 内核，"
    "XeTeX 3.141592653-2.6-0.999998），从 CTAN 镜像补齐了 ctex / xecjk / zhnumber / fandol / tcolorbox / pgf / caption / cite / "
    "enumitem / mathtools 等宏包，然后在 TinyTeX 下用 `xelatex` **连跑两遍**编译本交付源码：\n\n"
    "- 编译结果：**43 页**，**0 error**，**0 missing character**，无 undefined reference、无 overfull box；\n"
    "  仅 9 处 underfull hbox（badness 1442–10000），全部出现在参考文献的英文长行断行处，不影响可读性。\n"
    "- 用的是交付文件 `CS and Knots.tex` 本身（未改内容、未替换宏包选项），字体为 `fontset=fandol`；"
    "故这份 PDF 即该源码的真实排版产物。\n"
    "- 排版微调：译注方框改为 `breakable` + `fontupper=\\small`（避免整框跳页留下大片空白），"
    "目录另起一页。这些只影响 preamble，正文、公式编号、图表均未动。\n\n"
    "**若教授在本机编译**：装 TeX Live 2022 及以上完整版，`xelatex` 两遍即可；若用精简发行版，缺哪个宏包就 `tlmgr install` 补哪个"
    "（清单见上）。附：本机为编译临时安装的 TinyTeX 不在交付目录内，可删。\n\n"
)
t = t[:old_start] + new_para + t[old_end:]

t = t.replace("## 9. 工作量与协作", "## 9. 工作量与协作")
open(p, "w", encoding="utf-8").write(t)
print("README updated")

# ---------------- 审校报告 ----------------
p = "审校报告.md"
t = open(p, encoding="utf-8").read()
old = t[t.index("1. **编译验证未做**"):t.index("2. **建议人工复核的 3 处**")]
new = ("1. **编译验证已完成**：为出 PDF，临时安装了便携 TinyTeX（TeX Live 2026 内核）并补齐 ctex/fandol/tcolorbox 等宏包，"
       "用 `xelatex` 两遍编译交付源码：**43 页，0 error，0 缺字**，仅参考文献处 9 个 underfull hbox（纯排版警告）。"
       "成品 PDF 见 `CS and Knots_中文译注本.pdf`。此前静态审计（`tools/qa_all.py`，`RESULT: OK`）继续有效。\n")
t = t.replace(old, new)
t = t.replace("| `CS and Knots.tex` | 单文件完整源码，1,792 行，74 个锁定编号公式，5 图，84 条译注，32 条文献 |",
              "| `CS and Knots.tex` | 单文件完整源码，1,793 行，74 个锁定编号公式，5 图，84 条译注，32 条文献 |\n"
              "| `CS and Knots_中文译注本.pdf` | 成品 PDF，43 页，XeLaTeX 两遍实测编译（0 error / 0 缺字） |")
open(p, "w", encoding="utf-8").write(t)
print("report updated")
