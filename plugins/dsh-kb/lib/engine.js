/**
 * dsh-kb 搜索引擎（纯 JS，无外部依赖、无 Python、无 SQLite）
 *
 * 为什么不用 SQLite FTS5：
 *   插件要能被别人一条命令装上就用，就必须零外部依赖。1–3 万张卡这个量级，
 *   内存倒排索引比 SQLite 更快也更省事，而且中文分词按「bigram」做，
 *   连「顶点」这种两个字的中文词也能查（FTS5 的 trigram 做不到）。
 *
 * 检索语义（与仓库里 kb/q.py 对齐）：
 *   - 查询按空白切词，多个词之间是 AND；
 *   - 中文词：bigram 倒排取候选 → 再用整词 substring 校验；
 *   - 拉丁词：词表精确命中，≥4 字符时允许前缀命中（Grassmann → Grassmannian）；
 *   - 打分 = Σ(词 × 字段权重) × 可信度权重；title 4 / aliases 2.5 / terms 1.6 / summary 1。
 */
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

export { norm as normalizeText };
export const STATUS_W = { verified: 1.0, checked: 0.85, disputed: 0.7, draft: 0.55 };
const FIELD_W = { title: 4, title_en: 2, aliases: 2.5, terms: 1.6, symbols: 1.2, summary: 1 };

const CJK_CHAR = /[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]/;
const CJK_RUN = /[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+/g;
const LATIN_RE = /[a-z0-9][a-z0-9.+#_-]*/g;

/** 归一化：NFKC（全角→半角）+ 各类破折号统一成 ASCII 连字符，避免「Gromov–Witten」查不到 */
const norm = (s) => String(s ?? "").normalize("NFKC").replace(/[\u2010-\u2015\u2212]/g, "-");
const lower = (s) => norm(s).toLowerCase();

function fieldText(card, key) {
  const v = card[key];
  if (Array.isArray(v)) {
    return v
      .map((x) => (x && typeof x === "object" ? x.text ?? x.name ?? x.label ?? JSON.stringify(x) : x))
      .join(" ");
  }
  if (v && typeof v === "object") return JSON.stringify(v);
  return v ? String(v) : "";
}

/** 从目录读所有 *.jsonl（每行一张卡） */
export function loadCards(dir) {
  const files = readdirSync(dir).filter((f) => f.endsWith(".jsonl")).sort();
  const cards = [];
  for (const f of files) {
    const raw = readFileSync(join(dir, f), "utf8");
    for (const line of raw.split("\n")) {
      const t = line.trim();
      if (!t) continue;
      try {
        cards.push(JSON.parse(t));
      } catch {
        /* 单行坏了不拖垮整个库 */
      }
    }
  }
  return cards;
}

export function dataStamp(dir) {
  try {
    const files = readdirSync(dir).filter((f) => f.endsWith(".jsonl"));
    let mtime = 0;
    let bytes = 0;
    for (const f of files) {
      const st = statSync(join(dir, f));
      mtime = Math.max(mtime, st.mtimeMs);
      bytes += st.size;
    }
    return { files: files.length, mtime, bytes };
  } catch {
    return null;
  }
}

/** 建索引：bigram（中文）+ 词表（拉丁） */
/** 整卡文本（含 definition/key_points 等未进索引的字段），只用于判断题「库里到底有没有这个词」 */
function flatAll(card) {
  const parts = [];
  const walk = (v) => {
    if (v == null) return;
    if (typeof v === "string") parts.push(v);
    else if (Array.isArray(v)) v.forEach(walk);
    else if (typeof v === "object") Object.values(v).forEach(walk);
  };
  walk(card);
  return parts.join("\n").toLowerCase();
}

export function buildIndex(cards) {
  const byId = new Map();
  const bigram = new Map();
  const lex = new Map();
  const docs = [];

  const push = (map, key, i) => {
    let arr = map.get(key);
    if (!arr) map.set(key, (arr = []));
    if (arr[arr.length - 1] !== i) arr.push(i);
  };

  cards.forEach((card, i) => {
    const fields = {};
    for (const k of Object.keys(FIELD_W)) fields[k] = lower(fieldText(card, k));
    const blob = lower(Object.values(fields).join("\n"));

    for (const m of blob.matchAll(LATIN_RE)) push(lex, m[0].replace(/[.+#_-]+$/, ""), i);
    for (const m of blob.matchAll(CJK_RUN)) {
      const run = m[0];
      for (let p = 0; p + 1 < run.length; p++) push(bigram, run.slice(p, p + 2), i);
    }

    byId.set(card.id, i);
    // flat：去掉 LaTeX 结构字符，让「Bun_G」「$\operatorname{Bun}$」这类标识符也能子串命中
    const flat = blob.replace(/[\\{}$^_]/g, "");
    docs.push({ card, fields, blob, flat, blobAll: flatAll(card) });
  });

  return { docs, byId, bigram, lex };
}

function bigramCandidates(idx, token) {
  const grams = [];
  for (let p = 0; p + 1 < token.length; p++) grams.push(token.slice(p, p + 2));
  if (!grams.length) return null;
  let acc = null;
  for (const g of grams) {
    const list = idx.bigram.get(g);
    if (!list) return [];
    const set = new Set(list);
    acc = acc === null ? set : new Set([...acc].filter((x) => set.has(x)));
    if (!acc.size) return [];
  }
  return [...acc];
}

function latinCandidates(idx, token) {
  const hit = idx.lex.get(token);
  if (hit) return [...hit];
  if (token.length >= 4) {
    const out = [];
    for (const [k, v] of idx.lex) if (k.startsWith(token)) out.push(...v);
    if (out.length) return out;
  }
  // 复合词退路：「Gromov-Witten」库里若只写了「Gromov」，拆成两个词求交而不是直接判死
  if (/[-_.\/]/.test(token)) {
    const parts = token.split(/[-_.\/]+/).filter((x) => x.length >= 3);
    if (parts.length >= 2) {
      let acc = null;
      for (const pt of parts) {
        const l = idx.lex.get(pt);
        if (!l) return [];
        const set = new Set(l);
        acc = acc === null ? set : new Set([...acc].filter((x) => set.has(x)));
        if (!acc.size) return [];
      }
      return acc ? [...acc] : [];
    }
  }
  return [];
}

function scoreDoc(idx, i, tokens) {
  const d = idx.docs[i];
  let s = 0;
  for (const t of tokens) {
    for (const [field, w] of Object.entries(FIELD_W)) {
      const text = d.fields[field] || "";
      if (!text) continue;
      let c = 0;
      let at = text.indexOf(t);
      while (at !== -1 && c < 5) {
        c++;
        at = text.indexOf(t, at + t.length);
      }
      s += c * w;
    }
  }
  const st = d.card.status ?? "draft";
  s *= STATUS_W[st] ?? 0.55;
  if (d.card.kind === "work") s *= 0.5; // 书级条目只是指针，别抢前排
  return s;
}

/** 检索主函数 */
export function search(idx, query, opts = {}) {
  const q = String(query ?? "").trim();
  if (!q) return [];
  const includeDraft = !!opts.include_draft;
  const limit = Math.min(Math.max(Number(opts.limit) || 6, 1), 50);
  const tokens = q
    .split(/\s+/)
    .map((t) => t.trim())
    .filter(Boolean)
    .map((t) => lower(t.replace(/^["'“”]+|["'“”]+$/g, "")).trim())
    .filter(Boolean);
  if (!tokens.length) return [];

  let cand = null;
  for (const t of tokens) {
    let set = null;
    if (CJK_CHAR.test(t)) {
      const c = bigramCandidates(idx, t);
      if (c !== null && c.length) set = new Set(c);
      else {
        // 中文词但 bigram 颗粒对不上（如「d-模」这种拉丁+中文混写）→ 退回原文子串匹配
        const sub = idx.docs.flatMap((d, i) => (d.blob.includes(t) ? [i] : []));
        if (sub.length) set = new Set(sub);
      }
    } else {
      const c = latinCandidates(idx, t);
      if (c.length) set = new Set(c);
      // 标识符兜底：Bun_G / det^{1/2} / g-oper 这类，扁平文本子串命中要并进候选集，
      // 否则词表里恰好存了同形的其它卡时，交集会被错误清空。
      if (/[_.+^{}\\/]/.test(t)) {
        const ft = t.replace(/[\\{}$^_]/g, "");
        if (ft.length >= 3) {
          const fh = idx.docs.flatMap((d, i) => (d.flat.includes(ft) ? [i] : []));
          set = set ? new Set([...set, ...fh]) : (fh.length ? new Set(fh) : null);
        }
      }
    }
    if (set === null) {
      // 词表与 bigram 都没命中：先确认整卡文本里到底有没有这个词。
      // 有 → 只是它落在没建索引的字段里（definition/key_points…），忽略该词继续；
      // 没有 → 这就是真没命中，不能拿全库兜底（否则乱码查询也会返回一堆卡）。
      if (!idx.docs.some((d) => d.blobAll.includes(t))) return [];
      continue;
    }        // 这个词无法约束（单字/无命中）→ 忽略，不判死整条查询
    cand = cand === null ? set : new Set([...cand].filter((x) => set.has(x)));
    if (!cand.size) return [];
  }
  if (cand === null) cand = new Set(idx.docs.map((_, i) => i));

  const cjkTokens = tokens.filter((t) => CJK_CHAR.test(t));
  const out = [];
  for (const i of cand) {
    const card = idx.docs[i].card;
    if (!includeDraft && (card.status ?? "draft") === "draft") continue;
    if (opts.kind && card.kind !== opts.kind) continue;
    if (opts.work && String(card.work ?? "") !== String(opts.work)) continue;
    if (opts.level && card.level !== opts.level) continue;
    if (cjkTokens.some((t) => !idx.docs[i].blob.includes(t))) continue; // bigram 只是粗筛
    out.push({ card, score: scoreDoc(idx, i, tokens) });
  }
  out.sort((a, b) => b.score - a.score || String(a.card.id).localeCompare(String(b.card.id)));
  return out.slice(0, limit);
}

export function cardById(idx, id) {
  const i = idx.byId.get(String(id ?? "").trim());
  return i === undefined ? null : idx.docs[i].card;
}

export function worksOf(idx) {
  const m = new Map();
  for (const d of idx.docs) {
    const w = d.card.work ?? "?";
    m.set(w, (m.get(w) ?? 0) + 1);
  }
  return m;
}

/** 跨书线索：拿一批卡的术语/别名去别的作品里找已核卡 */
export function crossBook(idx, seeds, excludeWork, limit = 8) {
  const keep = new Set();
  for (const c of seeds) {
    for (const f of ["aliases", "terms", "title", "title_en"]) {
      const v = c[f];
      if (Array.isArray(v)) for (const x of v) if (x && String(x).length >= 2) keep.add(String(x));
      else if (v) keep.add(String(v));
    }
  }
  const hits = [];
  for (const d of idx.docs) {
    if (d.card.work === excludeWork) continue;
    if ((d.card.status ?? "draft") === "draft") continue;
    if (d.card.kind === "work") continue;
    let s = 0;
    for (const term of keep) {
      const t = lower(term);
      if (t.length < 2) continue;
      if (d.blob.includes(t)) s += t.length >= 4 ? 2 : 1;
    }
    if (s > 0) hits.push({ card: d.card, score: s * (STATUS_W[d.card.status] ?? 0.55) });
  }
  hits.sort((a, b) => b.score - a.score);
  return hits.slice(0, limit);
}
