# GLC 全量审计案例集（2026-11-26）

本目录是 `datasets/glc/cards` 154 张 concept 卡**全量双盲审计**中确认修复的案例归档。
与 `11_card_audit/casebook/`（上一批 100 卡审计的 32 例，已冻结）相互独立，不修改它。

## 目录

每张修过的卡一例，文件名 `<序号>-<slug>.md`，含七节：
错误版 / 正确版 / 为什么错 / 证据 / 审计轨迹 / 形式化提示 / 防再犯。
`../index.json` 是索引；`../README.md` 与 `../TRACE.md` 记录方法与时间线。

## 收录口径

只有同时满足以下条件的卡才有一例：

1. Pass A 与 Pass B 两名互盲审计员都判 issue（`both_issue`）；或单方判 issue 后
   第三名 arbiter 盲审也判 issue；
2. lead 逐条复核证据成立（E1 一手来源或卡内自相矛盾）；
3. 已按 `fix_log.json` 做字段级最小修复，且 md 镜像同步。

单方发现但未获第二判断认可的，不进本目录，只记入审计目录的 `report.md` 残余风险。

3 例例外（23–25）：原为单方发现、按协议未修，用户 m01466 授权后用 E1 英文原本＋E2
（nLab、CAG 2001、Casselman–Shalika 文献）补核，确认成立并修复；案例中把确认链标为
`lead+E1/E2`，与双盲确认的 22 例区分。

## 证据路径说明

每例「证据」节引用的 `tmp/pages/pNNN.txt`（PDF 逐页文本）只在本地工作副本
`datasets/_audit/glc_full_2026-11-26/` 中，**未入库**（含讲义正文，版权理由）；
发布件里对应的逐字引文已直接写进各例的证据节，`raw/EXTERNAL_VERIFICATION.md`
另有 56 处修改的完整对照与外部依据（51 处主核＋5 处 follow-up）。
