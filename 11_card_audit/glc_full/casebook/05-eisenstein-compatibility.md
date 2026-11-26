# 05 Eisenstein 函子的 Langlands 相容性

- 卡片：`glc/concept/eisenstein-compatibility`
- 失效模式：页码/出处定位漂移
- 严重度：minor
- 确认链：A(A8)+B(B3)
- 修复字段：`theorems[0].source`、`key_points[3]`

## 错误版

- `theorems[0].source`：§16.2 图表 (16.1) / 原书 p.76
- `key_points[3]`：在几何 Casselman–Schalika 等价 $\operatorname{Whit}(H)_x\simeq\operatorname{Rep}(\check H)_x$ 下，这一比较变为 Whittaker 系数的抛物限制与表示上相应 Chevalley 函子之间的相容性。

## 正确版

- `theorems[0].source`：§16.2 图表 (16.1) / 原书 p.77
- `key_points[3]`：在几何 Casselman–Shalika 等价 $\operatorname{Whit}(H)_x\simeq\operatorname{Rep}(\check H)_x$ 下，这一比较变为 Whittaker 系数的抛物限制与表示上相应 Chevalley 函子之间的相容性。

## 为什么错

图表 (16.1) 整幅在 p.77；p.76 §16.2 只有文字，卡把 theorem.source 写成 p.76。

## 证据

- E1 glc.pdf p.77 L8: 图表 (16.1)
- E1 glc.pdf p.76 L31: `Here CS denotes the geometric Casselman–Shalika equivalence.`；ch16.tex:38/96/168 同

## 审计轨迹

- Pass A 独立判 issue（查 `datasets/_audit/glc_full_2026-11-26/passA/`）
- Pass B 盲审独立判 issue（查 `passB/`；只拿卡路径，未见 A 结论）
- lead 逐条复核证据：`tmp/lead_verdicts.md`；修复记录：`fix_log.json`
- 本卡修复 2 处，JSON 变更 4 行；md 镜像同步 2 处

## 形式化提示

图表类对象的页码取整幅所在页；sources.pages 已含 76,77，只需改 theorem.source。

## 防再犯

theorem.source 指向图表时，页码取图表所在页而非小节起页。
