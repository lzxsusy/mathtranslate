# SY02-33 陈麟《几何 Langlands 理论导论》中文译注 · 校订版

把 Lin Chen（陈麟）*Introduction to Geometric Langlands Theory*（2023 年秋清华大学课程讲义，Wenhan Dai 记录，2025-08-08 修订，85 页，16 章 119 节）整本译为中文，
附 59 条带来源的译注、八路逐章审读记录与 55 处正文校订。

**成品**（底本为公开课程讲义（未出版），经译者决定随仓公开；`RELEASE_REGISTER.csv` 记 `成品级别=随仓公开`）

- `成品/几何Langlands理论导论（陈麟）_中文译注校订版.pdf`（110 页，含书末「译注一览」附录）
- 源码在 `源码/`，`xelatex → biber → makeindex → xelatex ×2` 可原样重出（见下「编译」）
- `工程文件/校订报告.md`（依据、流程、改动分类、译注来源、未做事项、交付清单）
- `工程文件/校对记录/`（ch01–ch16 各 `_issues.md` 与 `_notes.md`、`改动对照.md` 55 处原译／校订并列、`notes.tsv` 59 条译注台账、`final_audit.txt`）

## 底本

- Lin Chen, *Introduction to Geometric Langlands Theory*，2023 年秋清华课程（2023-09-19 至 12-07），
  记录者 Wenhan Dai，2025-08-08 修订版；85 页，16 章 119 节，参考文献 33 条。
- 底本 PDF **不入仓**（`原文级别=L4 禁入`），仓外路径 `C:/Users/admin/Desktop/LinChenGLC2023_中文译注_校订版/原文/LinChenGLC2023.pdf`。
  原工作目录里的 `源码/references/original.pdf` 已按此规则移出；正文未使用指向它的 `\origref` 宏，编译与页数不受影响。
- 章→页映射（原书 p5–p83）：ch01 p5–11 … ch16 p76–83，逐章锚点见各章 `\srcpage{N}`。

## 内容与规模

| 项 | 数 |
| --- | ---: |
| 成品页数 | 110 |
| 翻译章数 | 16（119 节） |
| 正文校订 | 55 处（数学错误、增译漏译、术语统一、翻译腔） |
| 译注 | 59 条（含糊点拨 44／易错预警 9／背景直觉 6） |
| `\label` | 141（与初版集合完全一致） |
| 未定义引用／Overfull／缺字 | 0／0／0 |

资料卡：`datasets/glc/` 有据本译本产出的 154 张结构卡（66 张 external-confirmed、88 张 source-only），按 O–H 九条轨道组织。

## 结构

```
源码/
  main.tex            装配：封面 → 前言 → 目录 → ch01–ch16 → 译注一览 → 参考文献
  chapters/ch01–ch16  每章一个文件（\srcpage{N} 记原书页）
  chapters/notes-index.tex  59 条译注附录（由 work/gen_index.py 生成）
  references/         参考文献（biber）
  images/             图
  elegantbook.cls     ElegantBook 模板（GPL，见 ElegantBook-License）
  build.ps1           一键编译
  audit/              审计脚本与结果（结构检查、字体、评审 JSON）
工程文件/
  校订报告.md         校订依据与改动统计
  校对记录/           八路审读记录、改动对照、译注台账、自动审计
成品/
  几何Langlands理论导论（陈麟）_中文译注校订版.pdf
```

## 编译

```powershell
cd 源码
powershell -NoProfile -ExecutionPolicy Bypass -File build.ps1
```

产物在 `源码/build/main.pdf`；已在干净目录验证：110 页、0 error。

## 权利与撤下

- 底本为作者公开课程讲义（未出版），无排他分发限制；译本为演绎作品，权利归原作者，`RELEASE_REGISTER.csv` 记 `源码级别=L2 公开·受限（可撤下）`、`成品级别=随仓公开`。
- 原作者或记录者如有异议，按登记表约定即行撤下（`L2 公开·受限（可撤下）`）。
- 与 `SY02-27_无穷范畴讲义`、`SY07-09_代数几何讲义I（陈麟）` 同为陈麟课程讲义的中译注本，术语与版式互相参照。
