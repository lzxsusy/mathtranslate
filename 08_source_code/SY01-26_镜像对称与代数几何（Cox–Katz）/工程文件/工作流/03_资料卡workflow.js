// 03_资料卡workflow.js — SY01-26 概念资料卡（24 张，playbook 13 号十一节硬模板）
// 用法：workflow 工具，meta 见注释，run_in_background: true。
// 约束：同时活跃子智能体 ≤ 8 → for 批次 + parallel。
//
// meta = {
//   name: "mirror-cards",
//   description: "Cox–Katz 中译本 24 张概念资料卡（十一节模板 + 跨项目冲突标记）",
//   phases: [{title: "立卡", detail: "每批 8 张"}]
// }
//
// args = { batch: 8 }

const REPO = "C:/Users/admin/Desktop/数译发布/gitee_shuyi/08_source_code";
const PROJ = `${REPO}/SY01-26_镜像对称与代数几何（Cox–Katz）`;
const WORK = "C:/Users/admin/Downloads/_mirror_review";
const BATCH = (args && args.batch) || 8;

const CARDS = [
  ["MS-03", "五次三维簇", "quintic-threefold", "L0"],
  ["MS-07", "环面簇", "toric-variety", "L0"],
  ["MS-08", "扇与多胞形", "fan-and-polytope", "L0"],
  ["MS-10", "Hodge 结构与滤过", "hodge-structure", "L0"],
  ["MS-16", "预稳定曲线与模空间", "prestable-curves", "L0"],
  ["MS-04", "量子上同调", "quantum-cohomology", "L1"],
  ["MS-05", "Gromov–Witten 不变量", "gromov-witten-invariant", "L1"],
  ["MS-06", "Picard–Fuchs 方程", "picard-fuchs", "L1"],
  ["MS-09", "自反多胞形", "reflexive-polytope", "L1"],
  ["MS-11", "Hodge 结构变分", "variation-of-hodge-structure", "L1"],
  ["MS-12", "单值性与最大幺幂", "monodromy-maximally-unipotent", "L1"],
  ["MS-13", "单值性定理与极限混合 Hodge 结构", "monodromy-theorem-lim", "L1"],
  ["MS-14", "消失圈", "vanishing-cycle", "L1"],
  ["MS-15", "稳定映射与虚拟基本类", "stable-maps-vfc", "L1"],
  ["MS-17", "局部化与等变上同调", "localization-equivariant", "L1"],
  ["MS-18", "Frobenius 流形与 Dubrovin 联络", "frobenius-manifold", "L1"],
  ["MS-19", "量子超平面截面原理", "quantum-hyperplane-section", "L1"],
  ["MS-01", "镜像对称", "mirror-symmetry", "L2"],
  ["MS-02", "镜像映射", "mirror-map", "L2"],
  ["MS-20", "非线性 σ 模型与超共形场论", "nlsm-scft", "L2"],
  ["MS-21", "规范线性 σ 模型与相", "glsm-phases", "L2"],
  ["MS-22", "极端跃迁与锥形奇点跃迁", "extremal-conifold-transition", "L2"],
  ["MS-23", "nef 分拆与 Batyrev 镜像构造", "nef-partition-batyrev", "L2"],
  ["MS-24", "Berglund–Hübsch 转置与轨形镜像", "berglund-hubsch", "L2"],
];

function prompt([id, zh, slug, layer]) {
  return `你是数学文献资料卡撰写员。为 Cox–Katz《镜像对称与代数几何》中译本写一张概念资料卡：${id}「${zh}」（层 ${layer}）。

## 先读这些（用 read / ops_inspect_local_file / grep，禁止改写任何既有文件）

1. 模板：${PROJ}/资料卡/_模板.md（十一节硬模板，**必须逐节写满**，不许增删节标题）
2. 队列与位置提示：${PROJ}/资料卡/_queue.md（找 ${id} 那一行：书内位置、可算最小例子、前置）
3. 本书英文 OCR（按页取）：${WORK}/ocr2/pNNN.txt（pNNN = PDF 物理页，如 p024.txt）
4. 本书中译：${WORK}/chapters/*.tex（用 grep 找中文关键词，`\\SourcePage{N}` 标页）
5. 对照资料（**必须读**，用于第 8 节与第 11 节）：
   - SY01-24 术语表：${REPO}/SY01-24_镜像对称（Siebert 讲义中译本）/成品/SY01-24_术语表.md
   - SY01-25 术语/勘误卡：${REPO}/SY01-25_同调镜像对称与环面纤维化/资料卡/04-术语文献勘误.md
   - 本项目冲突清单：${PROJ}/资料卡/_冲突表.md

## 写作要求

- 第 1 节一句话 ≤40 字；第 3 节定义必须写全假设；第 4 节**最小例子必须能算出具体数字**（给出计算过程与结果，不许只举「例如 P^2」）；第 6 节推导链每步写依据（书页/引理号）；第 7 节至少 2 个常见误解或反例；第 8 节文献坐标表至少 4 行（Cox–Katz 页、SY01-24、SY01-25、至少一部原始文献）。
- 书内页码一律用**本书 PDF 物理页**（= \SourcePage{N}，印刷页 + 23）；外部文献用原书页码或定理号。
- **冲突标记**：若 SY01-24 术语表 / SY01-25 资料卡的说法与本书定义、适用范围或术语不一致，在 §8 表格对应行写「冲突：……」并在 §11 待核清单登记；不得擅自判定谁对，只陈述差异与依据。
- 术语按本书口径：单值性（monodromy，不写单值化/单值变换）、消失圈、代数叠、虚拟基本类、多胞形、自反多胞形。
- 来源分级：A 级 = 能落到定理号/页码的原书或论文；B 级 = 教材/nLab/Stacks 索引；不许引知乎、博客、二手转述。
- 不确定的数字宁可写「待核」也不要编。YAML 头 status 一律 draft。

## 输出

用 write 写到：${PROJ}/资料卡/${id}-${slug}.md
长度 120–220 行。写完后只回复 JSON：{"id":"${id}","ok":true,"lines":<行数>,"conflicts":<冲突条数>}`;
}

phase("立卡");
const res = { total: CARDS.length, ok: 0, bad: 0, details: [] };
for (let i = 0; i < CARDS.length; i += BATCH) {
  const batch = CARDS.slice(i, i + BATCH);
  const out = await parallel(batch.map((c) => () =>
    agent(prompt(c), {
      label: c[0],
      schema: {
        type: "object",
        properties: { id: { type: "string" }, ok: { type: "boolean" }, lines: { type: "number" }, conflicts: { type: "number" }, note: { type: "string" } },
        required: ["id", "ok"],
        additionalProperties: false,
      },
    })
  ));
  out.forEach((r) => { if (r && r.ok) { res.ok++; res.details.push(r); } else res.bad++; });
  log(`cards batch ${i / BATCH + 1}: 累计 ok ${res.ok}/${res.total}`);
}
return res;
