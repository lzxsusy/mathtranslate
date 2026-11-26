# 18 奇异支撑受控的层范畴 $\operatorname{Shv}^{\mathrm{all}}_N(S)$

- 卡片：`glc/concept/shv-nilpotent-support`
- 失效模式：页码范围遗漏
- 严重度：minor
- 确认链：A(A6)+arbiter-t1a
- 修复字段：`sources[0].pages`、`sources[0].pdf_pages`、`theorems[0].source`、`theorems[0].proof.gap_note`

## 错误版

- `sources[0].pages`：[58, 59]
- `sources[0].pdf_pages`：[58, 59]
- `theorems[0].source`：定义（§11.4，讲义无编号） / 原书 p.58；§11.6 末段 p.59
- `theorems[0].proof.gap_note`：两条断言讲义都只陈述、未证明；分层控制一段出现在 §11.6 末（p.59），讲义称其为「幂零支撑恢复有限性性质的微局部原因」，未给论证。

## 正确版

- `sources[0].pages`：[58, 60]
- `sources[0].pdf_pages`：[58, 60]
- `theorems[0].source`：定义（§11.4，讲义无编号） / 原书 p.58；§11.6 末段 p.60
- `theorems[0].proof.gap_note`：两条断言讲义都只陈述、未证明；分层控制一段出现在 §11.6 末（p.60），讲义称其为「幂零支撑恢复有限性性质的微局部原因」，未给论证。

## 为什么错

§11.6 末段（分层控制）在 p.60 页眉后首段；p.59 以「Third, it is not too large…」结束，而 `ch11.tex` 全文没有 `\srcpage{60}`，卡只写到 [58,59]。

## 证据

- E1 glc.pdf p.59 末行: `Third, it is not too large: … whereas Shv^all(BunG) is generally not.`
- E1 glc.pdf p.60 页眉后首段: `More generally, for a smooth scheme S and conical subset N … controlled by a stratification adapted to N`
- ch11.tex 全文无 \srcpage{60}

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 4 处，JSON 变更 8 行；md 镜像同步 3 处

## 形式化提示

中译 ch11 缺 p.60 标记属源码缺陷；页码应以 PDF p.60 正文为准补上。

## 防再犯

`\srcpage` 缺页时以 PDF 页眉为准；末段/首段跨页要读下一页首行。
