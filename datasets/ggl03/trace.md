# 决策记录（trace）

| 判断点 | 依据 | 结论与理由 | 事后确认 |
| --- | --- | --- | --- |
| 页码基准取 PDF 页还是印刷页 | p003 页脚 2、p045 页脚 44，二者都差 1 | 一律用 PDF 页序填 sources.pages，anchor 写「A p.N eq (x.y)」；印刷页只在 notes 换算表里出现 | verify_pages 按 PDF 页命中，audit_locators 的 p.N 也按 PDF 页解析，均通过 |
| B 源锚点选哪一页 | KW06 PDF p.6 的 (2.1)、(2.2) 与本文 (2.1)、(2.4) 逐字一致；KW06 p.30 给出 (α,β,γ,η)→(η,β,γ,−α) | 参数卡锚 B p.6 与 B p.30，理由是这两页正是本文 §2.1、§2.6 的出处 | 卡片 related/sources 未被 lint 报缺字段；KW06 引用可回查原文 |
| 弯路一：用正则扫全篇式号找编号笔误 | 对 90 页跑 `\((\d+\.\d+)\)`，得 256 个匹配，大量重复与回退，但多数是正文交叉引用 | 无法区分「式号标签」与「引用」，该法不可用，放弃；改为人工核关键式号并用 audit_locators 机检 | 最终 audit_locators 在 03 目录通过，说明关键 locator 的式号都真实存在于所标页 |
| 弯路二：E2 先判为 (7.7) 的单处笔误 | 按 (7.6) 读 ^Lα=η，则 (7.7) 应为 +^Lα，看似只错一个符号 | 进一步按 (2.8) 复算对偶单值性，发现 (7.7) 恰与 (7.5) 自洽，而与 (7.4) 冲突；三式不能同时成立，改为「η 符号约定」的 low/open 结论 | errata E2 记 low、open，卡片保留原文并在 D4 加 corrections，未擅改 (7.4)/(7.5) |
| E1 的矩阵要不要在卡片里改 | 渲染 p039 得 300 dpi 图（external/p039_render.png），原文确为 [[0,i],[−i,0]]；det=−1 | 判定为真笔误：正确提升是 ±iσ_x=[[0,i],[i,0]]；卡片公式用订正形式并加 corrections，同时在 pitfalls 提醒原文印法 | lint 校验 corrections.id 存在于 errata，通过；结论（不刚性）不受影响，故记 medium 而非 high |
| 概念卡写几张、写哪些 | TASK 要求 8±2；主线为定义、半 BPS 参数、两类强刚性轨道、指纹、极多项式、中心/拓扑、对偶群、sigma model、minimal | 写 10 张：覆盖上述主线且每张都能迁移到别的篇（KW06、bdh、ggl12）；不写「special 轨道」单卡，因为它更适合放进指纹卡的关键点 | lint 概念卡计数与字段检查通过；related 指向的 id 全部存在 |
| 推导卡选哪三条主线 | TASK 点名 α,β,γ→0、指纹由幂零轨道决定、S-对偶主链 | 写 4 条：刚性极限、指纹、形变判据、量子化中心特征；前三条是原文核心推导，第四条承载 E2 | 每条 steps≥3 且 locator 全部带 p.N 与式号，audit_locators 通过 |
| 是否把 (2.28) 形变链单独成卡 | (2.28)–(2.30) 是「无间隙必要」的唯一构造性证明，且容易在别处复用 | 单写 rigid-orbit-deformation，而不是塞进强刚性幂零概念卡 | 5 步 locator 分别落在 p.20 与 p.21，audit 无 mismatch |
| D4 是否引入 E2 | §7 的猜想 (7.5) 依赖 (7.4)、(7.6)、(7.7) 三式；不写 E2 就无法诚实处理符号 | 写 D4，steps 3–5 用 provenance C 标自算，并加 corrections E2；result 明确保留原文 | errata「影响卡片」列出的 id 存在；lint 未报 high 缺依据2（E2 是 low） |
| terms 的首见页怎么取 | 用 grep -il 逐词扫 txt/03，取第一次出现的 PDF 页 | 25 条，含既定译名（twist、eigenbrane 等本篇未用的不收）；polar polynomial 与 fingerprint 取摘要页 2 而非 §4 正文页，因为摘要先出现 | term_index.py check 通过（术语与卡片用词一致） |
| excerpts 选哪四段 | 需要覆盖「刚性定义」「对数奇异」「中心/拓扑」「量子化」四个不可替代的论证点 | 4 段，每段 150–400 汉字，段前标 [p.N]；只译不评，公式按原文符号 | 逐段数字数均在区间内；内容与 notes 的骨架条目对应 |
| 审计脚本的参数怎么传 | audit_locators.py 内部 txt=root/"txt"/argv[2]，实际目录是 txt/03 | 按任务书传 3 会找不到 txt/3；先用 3 复现该失败，再用 03 实跑作为正式结果，不新建 txt/3（禁改 txt/） | 03 跑出 OK；把该坑写进 workflow「最易错」一节 |
