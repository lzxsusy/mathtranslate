// 02_校对workflow.js — SY01-26 全书逐单元校对（DSH workflow 脚本）
// 用法：把 script 内容交给 workflow 工具（meta 见下方注释），run_in_background: true。
// 约束：DSH 同时活跃子智能体上限 8，故必须 for 批次 + parallel，不能用 pipeline 全并行。
//
// meta = {
//   name: "mirror-proof-batched",
//   description: "Cox–Katz 中译本 153 单元分 8 批逐句对照校对",
//   phases: [{title: "校对", detail: "每批 8 单元"}]
// }
//
// args = { units: ["u01", ...], batch: 8 }

const BASE = "C:/Users/admin/Downloads/_mirror_review";
const BATCH = (args && args.batch) || 8;
const units = (args && args.units) || Array.from({ length: 153 }, (_, i) => "u" + String(i + 1).padStart(2, "0"));

const GLOSSARY = `
镜像对称 mirror symmetry｜量子上同调 quantum cohomology｜环面簇 toric variety｜
丰沛 ample｜单值性 monodromy｜轨形 orbifold｜翻转 flip｜翻越 flop｜万有族 universal family｜
线性系 linear system / pencil｜虚拟基本类 virtual fundamental class｜稳定映射 stable map｜
形变形变 deformation｜Hodge 结构变分 variation of Hodge structure｜消失圈 vanishing cycle｜
弱 Fröbenius 流形 Frobenius manifold｜Gromov–Witten 不变量｜Picard–Fuchs 方程｜
大复结构极限 large complex structure limit｜镜像映射 mirror map｜Yukawa 耦合｜
Batyrev 构造｜自反多胞形 reflexive polytope｜扇 fan｜多胞形 polytope｜
`;

function prompt(u) {
  return `你是数学文献校对员。逐句对照英文原文与中文译文，找出译文缺陷。

只读这两个文件（用 read/ops_inspect_local_file，禁止 glob/grep/bash）：
- ${BASE}/units/${u}.tex      （中文译文；首行是 % UNIT 注释，正文第 2 行对应 chapters 的起始行）
- ${BASE}/units/${u}.en.txt   （英文原文 OCR；[p.NNN] 标 PDF 物理页）

术语基准：${GLOSSARY}
（凡与上表冲突且属系统性者报「术语」类。）

输出：用 write 工具写 ${BASE}/review/${u}.json，结构：
{"unit":"${u}","issues":[{"line":N,"page":P,"type":"...","quote":"...","new":"...","problem":"...","confidence":"high|medium|low"}],
 "skipped":[{"line":N,"reason":"..."}],"notes":[{"page":P,"text":"..."}]}

规则：
1. type ∈ 错译/漏译/增译/术语/记号/数学/病句/指代。
2. quote 必须从 uXX.tex 逐字复制、不跨行、≤60 字；new 是替换后的文本（可含 LaTeX）。
3. line = uXX.tex 的行号（第 2 行 = chapters 起始行）；page = 该句所在 PDF 物理页。
4. 数学内容（公式、条件、取值范围、指数）错误优先级最高，必须给 confidence=high 的证据。
5. 英文 OCR 对公式糊掉的地方**不许臆断**，写进 skipped。
6. 每单元最多 2 条译注（作者跳步、记号冲突、原文笔误），写进 notes。
7. 宁缺勿滥：译文通顺且意思正确就不要报。0 条 issues 是合法结果。
8. 最后只回复 JSON：{"unit":"${u}","ok":true,"n":<issues 数>,"notes_n":<notes 数>}`;
}

phase("校对");
const counts = { total: units.length, ok: 0, bad: 0 };
for (let i = 0; i < units.length; i += BATCH) {
  const batch = units.slice(i, i + BATCH);
  const res = await parallel(batch.map((u) => () =>
    agent(prompt(u), {
      label: u,
      schema: {
        type: "object",
        properties: { unit: { type: "string" }, ok: { type: "boolean" }, n: { type: "number" }, notes_n: { type: "number" }, note: { type: "string" } },
        required: ["unit", "ok", "n", "notes_n"],
        additionalProperties: false,
      },
    })
  ));
  const good = res.filter((r) => r && r.ok).length;
  counts.ok += good;
  counts.bad += batch.length - good;
  log(`batch ${i / BATCH + 1}: ok ${good}/${batch.length}（累计 ${counts.ok}/${counts.total}）`);
}
return counts;
