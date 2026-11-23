/**
 * dsh-kb —— 数译知识库插件
 *
 * 把「带页码、带来源、带可信度」的数学文献资料卡接成 4 个 agent 工具：
 *   kb_search  全文检索（默认只返回已核卡片）
 *   kb_card    读单张卡（依赖、来源、证据引文、回源页码）
 *   kb_brief   阅读前置包：读一本新书之前，先把我们已知的端上来
 *   kb_stats   库统计 + 风险队列（被查得多但没复核的卡）
 *
 * 自包含：数据随包发布（data/cards/*.jsonl），检索在进程内完成，
 * 不需要 Python、不需要 SQLite、不需要配置任何路径。
 * 想挂到自己的仓库（数据更大/更新）时，配置 repo 指向含 kb/cards 的仓库根即可。
 */
import { existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import { buildIndex, cardById, crossBook, dataStamp, loadCards, search, worksOf, STATUS_W } from "./engine.js";
import {
  bestPageFor,
  buildSourceIndex,
  existsDir,
  loadSourceRows,
  pageContext,
  pkgList,
  searchSource,
  sourceStamp,
  sourceStats,
} from "./source.js";
import {
  bestPara,
  buildZhIndex,
  loadZhRows,
  paraContext,
  searchZh,
  snippet as zhSnippet,
  zhStats,
  zhStamp,
} from "./zh.js";

const HERE = dirname(fileURLToPath(import.meta.url));
const PKG_ROOT = resolve(HERE, "..");
const BUNDLED_DATA = join(PKG_ROOT, "data", "cards");
const BUNDLED_SRC = join(PKG_ROOT, "data", "src");

export const name = "dsh-kb";
export const inject = ["tools"];

const DEFAULT_CONFIG = {
  /** 含 kb/cards/*.jsonl 的仓库根；留空则用包内自带数据 */
  repo: "",
  /** 可选：work → 原文页图目录，用于回源核对 */
  pageRoots: {},
};

const CONTRACT =
  "知识库只给带证据的线索，不给没有出处的结论。" +
  "每条结果都带：可信度（已核/未复核）、原文页码、来源、以及 caveat。" +
  "默认只查已核卡片（checked/verified）；要未复核的必须显式 include_draft。" +
  "命中即“某部作品可能讲过”，引用前请用页码回原文核对。";

function normalizeConfig(raw) {
  const c = { ...DEFAULT_CONFIG, ...(raw && typeof raw === "object" ? raw : {}) };
  if (typeof c.repo !== "string") c.repo = "";
  c.repo = c.repo.trim();
  if (!c.pageRoots || typeof c.pageRoots !== "object") c.pageRoots = {};
  return c;
}

function dataDirOf(config) {
  if (config.repo) {
    const p = join(config.repo, "kb", "cards");
    if (existsSync(p)) return { dir: p, source: "repo", repo: config.repo };
  }
  if (existsSync(BUNDLED_DATA)) return { dir: BUNDLED_DATA, source: "bundled", repo: null };
  return { dir: null, source: "missing", repo: config.repo || null };
}

/** 索引缓存：按数据目录 mtime 失效（换库/更新数据后自动重建） */
let cache = { key: "", idx: null };

/** 原文层数据目录：外部仓库优先 01_corpus_src，否则用包内 data/src */
function srcDirOf(config) {
  if (config.repo) {
    const p = join(config.repo, "01_corpus_src");
    if (existsDir(p)) return { dir: p, source: "repo" };
  }
  if (existsDir(BUNDLED_SRC)) return { dir: BUNDLED_SRC, source: "bundled" };
  return { dir: null, source: "missing" };
}

let srcCache = { key: "", idx: null };

function getSourceIndex(config) {
  const { dir, source } = srcDirOf(config);
  if (!dir) return { idx: null, dir: null, source: "missing", stamp: null };
  const stamp = sourceStamp(dir);
  const key = `${dir}|${stamp?.mtime ?? 0}|${stamp?.files ?? 0}`;
  if (srcCache.key !== key) {
    srcCache = { key, idx: buildSourceIndex(loadSourceRows(dir)) };
  }
  return { idx: srcCache.idx, dir, source, stamp };
}

const BUNDLED_ZH = join(PKG_ROOT, "data", "zh");

/** 译文层数据目录：外部仓库优先 01_corpus_zh，否则用包内 data/zh */
function zhDirOf(config) {
  if (config.repo) {
    const p = join(config.repo, "01_corpus_zh");
    if (existsDir(p)) return { dir: p, source: "repo" };
  }
  if (existsDir(BUNDLED_ZH)) return { dir: BUNDLED_ZH, source: "bundled" };
  return { dir: null, source: "missing" };
}

let zhCache = { key: "", idx: null };

function getZhIndex(config) {
  const { dir, source } = zhDirOf(config);
  if (!dir) return { idx: null, dir: null, source: "missing", stamp: null };
  const stamp = zhStamp(dir);
  const key = `${dir}|${stamp?.mtime ?? 0}|${stamp?.files ?? 0}`;
  if (zhCache.key !== key) zhCache = { key, idx: buildZhIndex(loadZhRows(dir)) };
  return { idx: zhCache.idx, dir, source, stamp };
}
function getIndex(config) {
  const { dir, source, repo } = dataDirOf(config);
  if (!dir) {
    const err = new Error(
      "找不到卡片数据：包内 data/cards 缺失，且配置里的 repo 下没有 kb/cards。" +
        "请重新安装插件，或把 repo 指向含 kb/cards/*.jsonl 的仓库根。",
    );
    err.code = "NO_DATA";
    throw err;
  }
  const stamp = dataStamp(dir);
  const key = `${dir}|${stamp?.mtime ?? 0}|${stamp?.files ?? 0}`;
  if (cache.key !== key) {
    const cards = loadCards(dir);
    cache = { key, idx: buildIndex(cards) };
  }
  return { idx: cache.idx, dir, source, repo, stamp };
}

// ---------- 渲染 ----------

const pnum = (card) => {
  const p = Array.isArray(card.pages) ? card.pages : [];
  if (!p.length) return "无页码";
  return p.length === 1 ? `p.${p[0]}` : `p.${p[0]}–${p[p.length - 1]}`;
};

const srcLine = (card) => {
  const s = Array.isArray(card.sources) ? card.sources.filter(Boolean) : [];
  if (!s.length) return "";
  const first = s[0];
  const grade = first?.grade ? `[${first.grade}] ` : "";
  const text = String(first?.text ?? first ?? "").replace(/\s+/g, " ").slice(0, 140);
  return `\n   来源：${grade}${text}`;
};

const trustLabel = (st) =>
  st === "verified" ? "已核（≥2 轮）" : st === "checked" ? "已核（引文可核）" : st === "disputed" ? "有争议" : "未复核";

function renderHits(items) {
  if (!items.length) return "（没有命中已核卡片。可加 include_draft 试试，或换关键词。）";
  return items
    .map(({ card }, i) => {
      const body = String(card.summary ?? "").replace(/\s+/g, " ").slice(0, 260);
      return (
        `[${i + 1}] ${card.title}  (${card.id})\n` +
        `   ${trustLabel(card.status)} · ${card.kind}${card.level ? "/" + card.level : ""} · ${card.work} · ${pnum(card)}` +
        (body ? `\n   ${body}${body.length >= 260 ? "…" : ""}` : "") +
        srcLine(card) +
        (card.caveat ? `\n   ⚠ ${card.caveat}` : "")
      );
    })
    .join("\n\n");
}

const LANG_LABEL = { en: "英文", ja: "日文", zh: "中文", other: "其它" };

function renderSourceHits(items) {
  if (!items.length)
    return "（原文层没有命中。原文段落是底本逐字文本，换个更贴近原文的说法试试——比如把中文术语换成英文/日文写法。）";
  return items
    .map(({ row, snippet: sn }, i) => {
      const page = row.page != null ? `p.${row.page}` : "无页码";
      return (
        `[${i + 1}] ${row.pkg} · ${page} · 原文(${LANG_LABEL[row.lang] ?? row.lang})` +
        `\n   ${sn}` +
        `\n   → 读整页上下文：kb_source(pkg="${row.pkg}", page=${row.page ?? 1})`
      );
    })
    .join("\n\n");
}

function renderSourcePage(ctx, config) {
  if (!ctx) return "没有这一段（检查 pkg 与 page）。";
  const head = `# ${ctx.pkg} · p.${ctx.page} 原文`;
  const body = ctx.rows
    .map((r) => {
      const mark = r.page === ctx.page ? "▍" : " ";
      const page = r.page != null ? `p.${r.page}` : "—";
      const text = String(r.text).replace(/\s+\n/g, "\n").trim();
      return `${mark} [${page}] ${text}`;
    })
    .join("\n\n");
  const tail = [
    "",
    "—— 以上是底本原文（本库不发布原文 PDF，只放已公开的抽文）。",
    "卡片层对着同一件事可能有更省事的说法：kb_search(query=…, layer=\"cards\")。",
  ].join("\n");
  return `${head}\n\n${body}\n${tail}`;
}

function renderZhHits(items, q) {
  if (!items.length)
    return "（译文层没有命中。译文是逐段对照底本译的中文，换成更朴素的词、或只留一个关键词再试。）";
  return items
    .map(({ row }, i) => {
      const pg = row.page != null ? ` · 原书 p.${row.page}` : "";
      const tier = row.tier ? ` · ${row.tier} 级` : "";
      return (
        `[${i + 1}] ${row.pkg} · 段 ${row.para ?? "?"} · ${row.env}${pg}${tier}` +
        `\n   ${zhSnippet(row.text, q, 220)}` +
        `\n   → 读前后文：kb_zh(pkg="${row.pkg}", para=${row.para ?? 1})`
      );
    })
    .join("\n\n");
}
function renderCard(card, config) {
  const lines = [
    `${card.title}${card.title_en ? `  /  ${card.title_en}` : ""}`,
    `id: ${card.id}`,
    `作品: ${card.work}   类型: ${card.kind}${card.level ? `   层: ${card.level}` : ""}   可信度: ${trustLabel(card.status)}`,
    `页码: ${pnum(card)}`,
  ];
  if (Array.isArray(card.aliases) && card.aliases.length) lines.push(`别名: ${card.aliases.join(" / ")}`);
  if (Array.isArray(card.prereqs) && card.prereqs.length) lines.push(`前置: ${card.prereqs.join(", ")}`);
  if (Array.isArray(card.links) && card.links.length) {
    lines.push("关联:");
    for (const l of card.links.slice(0, 12)) {
      lines.push(`  · ${l.rel ?? "related"} → ${l.to ?? l.id ?? JSON.stringify(l)}`);
    }
  }
  if (card.summary) lines.push("", String(card.summary).trim());
  if (Array.isArray(card.sources) && card.sources.length) {
    lines.push("", "来源:");
    for (const s of card.sources.slice(0, 8)) {
      lines.push(`  · ${s?.grade ? `[${s.grade}] ` : ""}${String(s?.text ?? s).slice(0, 200)}`);
    }
  }
  if (card.evidence_quote) lines.push("", `证据引文：${String(card.evidence_quote).slice(0, 220)}`);
  if (card.terms) lines.push("", `术语：${JSON.stringify(card.terms).slice(0, 300)}`);
  if (card.review) lines.push("", `复核：${JSON.stringify(card.review).slice(0, 240)}`);
  if (card.caveat) lines.push("", `⚠ ${card.caveat}`);
  const root = config.pageRoots?.[card.work];
  if (root) lines.push("", `回源：${join(root, `p${String((card.pages ?? [0])[0] ?? 0).padStart(3, "0")}.png`)}`);

  return lines.join("\n");
}

// ---------- 插件 ----------

export function apply(ctx, rawConfig) {
  const config = normalizeConfig(rawConfig);
  const outSchema = {
    type: "object",
    additionalProperties: false,
    properties: { ok: { type: "boolean" }, error: { type: "string" }, text: { type: "string" } },
  };
  const renderText = (_args, value) => [{ type: "text", text: value?.text ?? "(无输出)" }];

  const guarded = async (fn) => {
    try {
      return { ok: true, text: await fn() };
    } catch (err) {
      if (err?.code === "NO_DATA") return { ok: false, text: err.message };
      return { ok: false, text: "知识库调用失败：" + (err?.message ?? err) };
    }
  };

  const searchTool = {
    name: "kb_search",
    description:
      "检索数译知识库：默认查资料卡（structure 化、带页码与可信度）；也可以查原文层（底本逐字文本，覆盖卡片还没做到的部分）。" +
      "layer=cards 只查卡片，layer=zh 只查中文译文，layer=source 只查原文，layer=both / all 三层都给。" +
      CONTRACT,
    parameters: {
      type: "object",
      properties: {
        query: { type: "string", description: '关键词或术语，可中英混写（例："Hecke 特征层"、"Gromov-Witten"、"仿射 Grassmann"）。按空白分词，全部词都要命中。' },
        layer: { type: "string", description: '查哪一层：cards（默认，资料卡）/ zh（中文译文）/ source（原文）/ both 或 all（三层都给）' },
        kind: { type: "string", description: "只查某一类卡：concept/theorem/proof/chain/example/term/errata/alignment/work/note" },
        work: { type: "string", description: "只查某一部作品，如 SY02-14 / glc / bdh" },
        level: { type: "string", description: "只查某一深度层：L0 名词 / L1 定义 / L2 定理 / L3 证明骨架 / L4 跨书论证链" },
        lang: { type: "string", description: "原文层限定语种：en / ja / zh / other" },
        env: { type: "string", description: "译文层限定段落类型：text/theorem/proof/definition/example/remark" },
        tier: { type: "string", description: "译文层限定等级：A / B" },
        include_draft: { type: "boolean", description: "卡片层是否包含未复核卡片（default false）。返回里会标“未复核”。" },
        limit: { type: "number", description: "每层返回条数上限，默认 6，最大 20" },
      },
      required: ["query"],
    },
    output: { schema: outSchema, render: renderText },
    timeoutMs: 15000,
    execute(args = {}) {
      const q = String(args.query ?? "").trim();
      if (!q) return { ok: false, text: "query 不能为空。" };
      const rawLayer = String(args.layer ?? "").trim();
      const layer = ["cards", "source", "zh", "both", "all"].includes(rawLayer) ? rawLayer : "cards";
      const limit = Math.min(Math.max(Number(args.limit) || 6, 1), 20);
      const wantCards = layer === "cards" || layer === "both" || layer === "all";
      const wantZh = layer === "zh" || layer === "both" || layer === "all";
      const wantSrc = layer === "source" || layer === "both" || layer === "all";
      const multi = (wantCards ? 1 : 0) + (wantZh ? 1 : 0) + (wantSrc ? 1 : 0) > 1;
      return guarded(() => {
        const parts = [];
        if (wantCards) {
          const { idx } = getIndex(config);
          const items = search(idx, q, {
            kind: args.kind,
            work: args.work,
            level: args.level,
            include_draft: !!args.include_draft,
            limit,
          });
          parts.push(
            multi ? `## 资料卡层（结构化结论，带页码与可信度）\n\n${renderHits(items)}` : renderHits(items),
          );
        }
        if (wantZh) {
          const { idx: zidx } = getZhIndex(config);
          if (!zidx) parts.push("译文层数据缺失（包内 data/zh 没有，也没找到 repo/01_corpus_zh）。");
          else {
            const items = searchZh(zidx, q, {
              pkg: args.work && zidx.byPkg.has(String(args.work)) ? String(args.work) : undefined,
              env: args.env,
              tier: args.tier,
              limit,
            });
            parts.push(
              multi
                ? `## 译文层（我们自己的中文译文，覆盖最全）\n\n${renderZhHits(items, q)}`
                : renderZhHits(items, q),
            );
          }
        }
        if (wantSrc) {
          const { idx: sidx } = getSourceIndex(config);
          if (!sidx) parts.push("原文层数据缺失（包内 data/src 没有，也没找到 repo/01_corpus_src）。");
          else {
            const items = searchSource(sidx, q, {
              lang: args.lang,
              pkg: args.work && sidx.byPkg.has(String(args.work)) ? String(args.work) : undefined,
              limit,
            });
            parts.push(
              multi
                ? `## 原文层（底本逐字文本，卡片没覆盖的地方看这里）\n\n${renderSourceHits(items)}`
                : renderSourceHits(items),
            );
          }
        }
        return parts.join("\n\n");
      });
    },
  };

  const sourceTool = {
    name: "kb_source",
    description:
      "读底本原文的整页上下文（默认前后各 2 段）。资料卡说“某书 p.12 讲了 X”时，用这个把那一页原文调出来自己核一遍；" +
      "也可以只给 pkg + query，会自动找最相关的一页。只覆盖仓库已公开的原文抽文（不是全书）。",
    parameters: {
      type: "object",
      properties: {
        pkg: { type: "string", description: "工程/作品编号，如 SY02-15、SEM-9407087（用 kb_search layer=source 找）" },
        page: { type: "number", description: "页码（底本 PDF 页）。省略时按 query 自动选页" },
        query: { type: "string", description: "只给 pkg 时用来定位最相关页面的关键词" },
        around: { type: "number", description: "上下文段数，默认 2，最大 6" },
      },
      required: ["pkg"],
    },
    output: { schema: outSchema, render: renderText },
    timeoutMs: 15000,
    execute(args = {}) {
      const pkg = String(args.pkg ?? "").trim();
      if (!pkg) return { ok: false, text: "pkg 不能为空。" };
      const around = Math.min(Math.max(Number(args.around) || 2, 0), 6);
      return guarded(() => {
        const { idx: sidx, source } = getSourceIndex(config);
        if (!sidx) return "原文层数据缺失（包内 data/src 没有，也没找到 repo/01_corpus_src）。";
        if (!sidx.byPkg.has(pkg)) {
          const have = pkgList(sidx);
          return `原文层没有工程 ${pkg}。目前有原文的 ${have.length} 个工程：${have.join(", ")}`;
        }
        const page = Number.isFinite(Number(args.page))
          ? Number(args.page)
          : bestPageFor(sidx, pkg, String(args.query ?? ""));
        const ctx = pageContext(sidx, pkg, page, around);
        if (!ctx) return `${pkg} 没有 p.${page} 这一段。`;
        return renderSourcePage(ctx, config);
      });
    },
  };

  const zhTool = {
    name: "kb_zh",
    description:
      "读中文译文的某一段及前后文（默认前后各 2 段）。只知道工程编号时可给 query，自动在这一部里找最相关的一段。" +
      "与 kb_source 的区别：kb_source 回到底本原文，kb_zh 看我们自己译成中文的对应段落。",
    parameters: {
      type: "object",
      properties: {
        pkg: { type: "string", description: "工程编号，如 SY01-07（用 kb_search layer=zh 找）" },
        para: { type: "number", description: "段号（zh_paragraphs.jsonl 里的 para）" },
        query: { type: "string", description: "不给 para 时，用它在这一部里找最相关的一段" },
        around: { type: "number", description: "前后各取几段，默认 2，最大 6" },
      },
      required: ["pkg"],
    },
    output: { schema: outSchema, render: renderText },
    timeoutMs: 15000,
    execute(args = {}) {
      const pkg = String(args.pkg ?? "").trim();
      if (!pkg) return { ok: false, text: "pkg 不能为空。" };
      const around = Math.min(Math.max(Number(args.around) || 2, 0), 6);
      return guarded(() => {
        const { idx } = getZhIndex(config);
        if (!idx) return "译文层数据缺失（包内 data/zh 没有，也没找到 repo/01_corpus_zh）。";
        if (!idx.byPkg.has(pkg)) return `没有这个工程的译文：${pkg}（用 kb_search(layer="zh") 找工程编号）`;
        let para = args.para != null && Number.isFinite(Number(args.para)) ? Number(args.para) : null;
        if (para == null) {
          const q2 = String(args.query ?? "").trim();
          if (!q2) return "要么给 para，要么给 query。";
          const best = bestPara(idx, pkg, q2);
          if (!best) return `${pkg} 里没有命中「${q2}」的段落。`;
          para = best.para;
        }
        const ctx = paraContext(idx, pkg, para, around);
        if (!ctx) return `没有这一段：${pkg} 段 ${para}`;
        const head = `# ${pkg} · 段 ${para} 中文译文（前后各 ${around} 段）`;
        const body = ctx.span
          .map((r) => {
            const mark = r.para === para ? "▍" : " ";
            const meta = `[段 ${r.para ?? "?"} · ${r.env}${r.tier ? ` · ${r.tier} 级` : ""}${
              r.page != null ? ` · 原书 p.${r.page}` : ""
            }]`;
            return `${mark} ${meta}\n${String(r.text).trim()}`;
          })
          .join("\n\n");
        const tail = [
          "",
          '—— 以上是本库自己的中文译文。想核对底本原话：kb_source(pkg, page)；想找结构化结论：kb_search(layer="cards")。',
        ].join("\n");
        return `${head}\n\n${body}\n${tail}`;
      });
    },
  };


  const cardTool = {
    name: "kb_card",
    description: "读一张资料卡的全文（依赖、来源、证据引文、caveat）以及它的回源信息。" + CONTRACT,
    parameters: {
      type: "object",
      properties: { id: { type: "string", description: "卡片 id，如 SY01-26.MS-05 或 glc.concept.hecke-eigensheaf-oper" } },
      required: ["id"],
    },
    output: { schema: outSchema, render: renderText },
    timeoutMs: 15000,
    execute(args = {}) {
      const id = String(args.id ?? "").trim();
      if (!id) return { ok: false, text: "id 不能为空。" };
      return guarded(() => {
        const { idx } = getIndex(config);
        const card = cardById(idx, id);
        return card ? renderCard(card, config) : `没有这张卡：${id}（用 kb_search 找 id）`;
      });
    },
  };

  const briefTool = {
    name: "kb_brief",
    description:
      "生成“阅读前置包”：动笔翻译/精读一部新书之前，先看我们已经入库的相关卡片（跨书线索）。" +
      "传 work=已入库作品编号，或 query=新书主题。结果仍是线索，不是结论。" + CONTRACT,
    parameters: {
      type: "object",
      properties: {
        work: { type: "string", description: "已入库作品编号，如 SY02-08 / glc" },
        query: { type: "string", description: "新书主题关键词（work 为空时用）" },
        limit: { type: "number", description: "最多列几张，默认 10" },
      },
      required: [],
    },
    output: { schema: outSchema, render: renderText },
    timeoutMs: 15000,
    execute(args = {}) {
      const limit = Math.min(Math.max(Number(args.limit) || 10, 1), 30);
      const work = String(args.work ?? "").trim();
      const query = String(args.query ?? "").trim();
      return guarded(() => {
        const { idx } = getIndex(config);
        if (work) {
          const own = idx.docs.filter((d) => String(d.card.work) === work).map((d) => d.card);
          if (!own.length) return `库里没有作品 ${work}。已有作品：${[...worksOf(idx).keys()].slice(0, 40).join(", ")}`;
          const ranked = own
            .slice()
            .sort(
              (a, b) =>
                (STATUS_W[b.status] ?? 0) - (STATUS_W[a.status] ?? 0) ||
                String(a.kind).localeCompare(String(b.kind)) ||
                String(a.title).localeCompare(String(b.title)),
            )
            .slice(0, limit);
          const cross = crossBook(idx, own.slice(0, 40), work, Math.max(6, Math.floor(limit / 2)));
          return [
            `# 阅读前置包：${work}（已入库作品）`,
            "",
            `本作品已入库 ${own.length} 张卡，按可信度排序取前 ${ranked.length} 张：`,
            "",
            renderHits(ranked.map((card) => ({ card }))),
            "",
            "## 跨书线索（别的作品里可能讲过同一件事）",
            "",
            cross.length ? renderHits(cross) : "_没有找到跨书线索。_",
          ].join("\n");
        }
        if (!query) return "请给 work 或 query 之一。";
        const hits = search(idx, query, { limit, include_draft: false });
        return [
          `# 阅读前置包：${query}`,
          "",
          hits.length
            ? renderHits(hits)
            : "_库里没有已核卡片覆盖这个主题。可以换关键词，或先补卡片（kb/cards）再把数据打进插件。_",
        ].join("\n");
      });
    },
  };

  const statsTool = {
    name: "kb_stats",
    description:
      "知识库现状：卡片数 / 可信度分布 / 各作品规模 / 带页码比例。用来判断某本书的卡是否可信、是否值得先补校。",
    parameters: { type: "object", properties: {}, required: [] },
    output: { schema: outSchema, render: renderText },
    timeoutMs: 15000,
    execute() {
      return guarded(() => {
        const { idx, dir, source, repo, stamp } = getIndex(config);
        const cards = idx.docs.map((d) => d.card);
        const by = (fn) => {
          const m = new Map();
          for (const c of cards) m.set(fn(c) ?? "?", (m.get(fn(c) ?? "?") ?? 0) + 1);
          return [...m.entries()].sort((a, b) => b[1] - a[1]);
        };
        const pages = cards.filter((c) => Array.isArray(c.pages) && c.pages.length).length;
        const withSrc = cards.filter((c) => Array.isArray(c.sources) && c.sources.length).length;
        const lines = [
          `库：${dir}`,
          `来源：${source === "bundled" ? "包内自带数据（data/cards）" : `外部仓库 ${repo}`}` +
            ` · ${stamp?.files ?? "?"} 个文件 · ${((stamp?.bytes ?? 0) / 1048576).toFixed(1)} MB`,
          "",
          `共 ${cards.length} 张卡 / ${worksOf(idx).size} 部作品`,
          "",
          "== 可信度 ==",
          ...by((c) => c.status).map(([k, v]) => `  ${String(k).padEnd(10)} ${v}   ${trustLabel(k)}`),
          "",
          "== 类型 ==",
          ...by((c) => c.kind).map(([k, v]) => `  ${String(k).padEnd(10)} ${v}`),
          "",
          `带页码（可回溯）：${pages}   带来源：${withSrc}`,
          "",
          "== 卡片最多的 12 部作品 ==",
          ...[...worksOf(idx).entries()]
            .sort((a, b) => b[1] - a[1])
            .slice(0, 12)
            .map(([w, n]) => `  ${String(w).padEnd(14)} ${n}`),
        ];
        const drafts = cards.filter((c) => c.status === "draft").length;
        if (drafts) lines.push("", `未复核（draft）：${drafts} 张 —— 默认不会被检索到，需 include_draft。`);

        // 原文层
        const { idx: sidx, dir: sdir, source: ssource } = getSourceIndex(config);
        if (sidx) {
          const st = sourceStats(sidx);
          const langs = [...st.langs.entries()]
            .sort((a, b) => b[1] - a[1])
            .map(([k, v]) => `${LANG_LABEL[k] ?? k} ${v}`)
            .join(" · ");
          lines.push(
            "",
            "== 原文层（底本逐字文本）==",
            `来源：${ssource === "bundled" ? "包内自带数据（data/src）" : `外部仓库 ${sdir}`}`,
            `共 ${st.total} 段 / ${st.pkgs.size} 个工程 / ${(st.chars / 1e6).toFixed(1)}M 字符 · ${langs}`,
            "检索：kb_search(layer=\"source\") / 读页：kb_source(pkg, page)",
            "",
            "原文段落最多的 10 个工程：",
            ...[...st.pkgs.entries()]
              .sort((a, b) => b[1].paras - a[1].paras)
              .slice(0, 10)
              .map(([p, e]) => `  ${String(p).padEnd(14)} ${String(e.paras).padStart(5)} 段 · ${e.pages.size} 页`),
          );
        } else {
          lines.push("", "== 原文层 ==", "未安装原文数据（包内 data/src 缺失）。卡片层不受影响。");
        }
        // 译文层
        const { idx: zidx, dir: zdir, source: zsource } = getZhIndex(config);
        if (zidx) {
          const zt = zhStats(zidx);
          const envs = [...zt.envs.entries()]
            .sort((a, b) => b[1] - a[1])
            .slice(0, 6)
            .map(([k, v]) => `${k} ${v}`)
            .join(" · ");
          lines.push(
            "",
            "== 译文层（我们自己的中文译文）==",
            `来源：${zsource === "bundled" ? "包内自带数据（data/zh）" : `外部仓库 ${zdir}`}`,
            `共 ${zt.paragraphs} 段 / ${zt.projects} 个工程 / ${(zt.chars / 1e4).toFixed(1)} 万汉字 · 带页码 ${zt.pages} 页`,
            `段落类型：${envs}`,
            '检索：kb_search(layer="zh") / 读前后文：kb_zh(pkg, para)',
          );
        } else {
          lines.push("", "== 译文层 ==", "未安装译文数据（包内 data/zh 缺失）。卡片层不受影响。");
        }

        return lines.join("\n");
      });
    },
  };

  ctx.effect(() => ctx.tools.register(searchTool), "dsh-kb: tool kb_search");
  ctx.effect(() => ctx.tools.register(sourceTool), "dsh-kb: tool kb_source");
  ctx.effect(() => ctx.tools.register(zhTool), "dsh-kb: tool kb_zh");
  ctx.effect(() => ctx.tools.register(cardTool), "dsh-kb: tool kb_card");
  ctx.effect(() => ctx.tools.register(briefTool), "dsh-kb: tool kb_brief");
  ctx.effect(() => ctx.tools.register(statsTool), "dsh-kb: tool kb_stats");
}
