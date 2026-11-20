const BASE = "C:/Users/admin/Desktop/数译发布/gitee_shuyi/08_source_code/SY01-26_镜像对称与代数几何（Cox–Katz）/资料卡";
const OUT = BASE + "/_核验";

const CARDS = [
  "MS-01-mirror-symmetry", "MS-02-mirror-map", "MS-03-quintic-threefold",
  "MS-04-quantum-cohomology", "MS-05-gromov-witten-invariant", "MS-06-picard-fuchs",
  "MS-07-toric-variety", "MS-08-fan-and-polytope", "MS-09-reflexive-polytope",
  "MS-10-hodge-structure", "MS-11-variation-of-hodge-structure", "MS-12-monodromy-maximally-unipotent",
  "MS-13-monodromy-theorem-lim", "MS-14-vanishing-cycle", "MS-15-stable-maps-vfc",
  "MS-16-prestable-curves", "MS-17-localization-equivariant", "MS-18-frobenius-manifold",
  "MS-19-quantum-hyperplane-section", "MS-20-nlsm-scft", "MS-21-glsm-phases",
  "MS-22-extremal-conifold-transition", "MS-23-nef-partition-batyrev", "MS-24-berglund-hubsch",
];

function promptFor(id) {
  return `你是数学资料卡的核验员。只处理这一张卡：${BASE}/${id}.md

任务：核验这张卡里的**可核验断言**，不要重写卡片、不要改卡片文件。

步骤：
1. 读卡片，挑出 6–10 条最值得核验的断言，优先选：数值（Hodge 数、Betti 数、Euler 数、GW 不变量 n_d、维数、指数）、定理归属（谁在什么文献证明）、公式常数与符号约定、定义的标准性、历史事实（年份/人名/期刊）。
2. 逐条核验：
   - 优先外部权威来源：arXiv、AMS(MathSciNet 摘要页)、nLab、Springer、知名大学讲义、原始论文 PDF。用 web_search 检索、必要时 web_fetch 读原文。
   - 能通过算术或最小例子自证的（如 χ=2(h^{1,1}-h^{2,1})、b_3=2+2h^{2,1}、Σ n_d d³ q^d/(1-q^d) 的系数、K=5Y 之类），自己算并写明算式。
   - 判定只能是 ok / wrong / unverified 三种之一。**不确定就写 unverified，不要猜**。
3. 把结果写到 ${OUT}/${id}.json，UTF-8，格式：
{"id":"${id}","claims":[{"claim":"卡片原话或紧贴原意的摘要","verdict":"ok|wrong|unverified","evidence":"一句话证据（含关键数字/原文措辞）","source":"URL 或 自算：算式"}],"wrong_count":N,"unverified_count":N,"notes":"其他发现（可空）"}

要求：
- claims 里的 claim 尽量保留卡片原措辞的关键术语（便于回查）。
- source 必须是真实 URL 或「自算：…」；不要编造 DOI。
- 只用 write 写这一个 JSON 文件；不要读写其他卡。
- 最后只回复 JSON：{"id":"${id}","ok":<ok 条数>,"wrong":<wrong 条数>,"unverified":<unverified 条数>}`;
}

const schema = {
  type: "object",
  additionalProperties: false,
  required: ["id", "ok", "wrong", "unverified"],
  properties: {
    id: { type: "string" },
    ok: { type: "number" },
    wrong: { type: "number" },
    unverified: { type: "number" },
  },
};

const BATCH = 8;
const results = [];
for (let i = 0; i < CARDS.length; i += BATCH) {
  const chunk = CARDS.slice(i, i + BATCH);
  const out = await parallel(
    chunk.map((id) => () => agent(promptFor(id), { schema, label: "verify " + id })),
  );
  for (const r of out) if (r) results.push(r);
  log(`batch ${i / BATCH + 1}: ${results.length}/${CARDS.length} 张卡核验完成`);
}

const wrong = results.reduce((s, r) => s + (r.wrong || 0), 0);
const unv = results.reduce((s, r) => s + (r.unverified || 0), 0);
const ok = results.reduce((s, r) => s + (r.ok || 0), 0);
return { cards: results.length, ok, wrong, unverified: unv, details: results };
