# 交付②：工程文件与源代码

> 用户 2026-11-13 定：交付“一个工程文件，然后还要有源代码这些东西”，与笔记一并上传公开仓库，供他人阅读和使用。

## 目标

别人 clone 仓库后，**一条命令重建笔记 PDF**，并能核查“笔记里每条断言确实能在原文找到”。

## 计划内容

```
deliverables/engineering/
├── README.md            本文件
├── manifest.json        论文/译本/锚点/产物的机器可读索引
├── Makefile 或 build.ps1  一条命令：编译笔记 + 校验锚点 + 导出数据
└── scripts/
    ├── check_claims.py   校验 claims.jsonl 字段与锚点格式
    ├── check_anchors.py  把笔记里的 [src p.N]/[eq x.y] 与 claims.jsonl、原文页图对照
    ├── make_manifest.py  扫描 materials/、sessions/、deliverables/ 生成 manifest.json
    └── export_html.py    把笔记导出为单页 HTML（可选）
```

## 依赖

- TeX Live / MiKTeX（xelatex + ctex + tikz + amsthm）
- Python 3（仅标准库 + pypdf，用于页数与锚点核对）
- 无需网络：所有材料随仓库分发（译本页图受版权限制的，见下）

## 版权分层（必须遵守）

- **L0 自产**：笔记、脚本、manifest、claims/questions —— 可公开，CC BY 4.0。
- **L1 译本**：我们自己的 Witten 中译 —— 随仓库公开需注明“非官方译本，仅供学习”，不再分发英文原刊页图。
- **L2 第三方**：英文原刊 PDF、教材扫描件 —— **不上传**，只在 manifest 里记“本地路径 + 获取方式”。

## 一条命令

```powershell
pwsh deliverables/engineering/build.ps1
# 1) python scripts/check_claims.py
# 2) xelatex -interaction=nonstopmode reading_note/main.tex（3 遍）
# 3) python scripts/check_anchors.py
# 4) python scripts/make_manifest.py
```

## 状态

- [ ] manifest.json 字段定稿
- [ ] check_claims.py 可跑（S1 的 13 条 claims 先过）
- [ ] build.ps1 可跑（笔记骨架能编译出空 PDF 即算通过）
- [ ] check_anchors.py 接原文页图
- [ ] README（仓库根）5 分钟上手一节
