# 07 Frobenius 扭曲的迹与谱分解

- 卡片：`glc/concept/frobenius-twisted-trace`
- 失效模式：页码范围遗漏
- 严重度：minor
- 确认链：A(A6)+arbiter-t1a
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`、`theorems[0].source`

## 错误版

- `sources[0].pages`：[63]
- `sources[0].pdf_pages`：[63]
- `theorems[0].source`：命题（§12.7，讲义无编号） / 原书 p.63

## 正确版

- `sources[0].pages`：[63, 64]
- `sources[0].pdf_pages`：[63, 64]
- `theorems[0].source`：命题（§12.7，讲义无编号） / 原书 p.63–64

## 为什么错

命题后半句（取全局截面恢复自守迹空间）在 p.64 首段；`ch12.tex` 无 `\srcpage{64}`，卡只写 [63]。

## 证据

- E1 glc.pdf p.64 首段: `whose points are restricted Weil Ĝ-local systems. Taking global sections recovers the automorphic trace space above.`
- ch12.tex 无 \srcpage{64}

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 3 处，JSON 变更 8 行；md 镜像同步 2 处

## 形式化提示

该卡是 git 基线里已有的未提交改动（游走→巡游），修 pages 不碰那处措辞。

## 防再犯

修卡前先 `git diff` 看该卡是否已有他人未提交改动，避免覆盖。
