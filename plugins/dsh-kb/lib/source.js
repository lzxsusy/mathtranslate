/**
 * 原文层检索（dsh-kb 0.3.0）
 *
 * 卡片层是「我们读出来的结构化结论」，原文层是「底本自己说的话」。
 * 卡片只有 1,250 张，覆盖不到全部段落，所以这里把仓库里【已经公开】的原文文本
 * 抽成段落（01_corpus_src/src_paragraphs.jsonl），随包发布一份 gz，进程内检索。
 *
 * 为什么不做倒排：5.5M 字符全量建中文 bigram 索引要吃几百 MB 内存，
 * 而 8,226 段线性扫描单查询只要十几毫秒 —— 用内存换那 10ms 不划算。
 */
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";
import { gunzipSync } from "node:zlib";

const norm = (s) => String(s ?? "").toLowerCase();

/** 数据戳：目录里最新 mtime + 文件数，用来判断缓存是否失效 */
export function sourceStamp(dir) {
  try {
    const files = readdirSync(dir).filter((f) => /\.jsonl(\.gz)?$/.test(f));
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

/** 读行：支持 .jsonl 与 .jsonl.gz */
export function loadSourceRows(dir) {
  const rows = [];
  const files = readdirSync(dir).filter((f) => /\.jsonl(\.gz)?$/.test(f));
  for (const f of files) {
    const p = join(dir, f);
    const buf = readFileSync(p);
    const text = f.endsWith(".gz") ? gunzipSync(buf).toString("utf8") : buf.toString("utf8");
    for (const line of text.split("\n")) {
      const s = line.trim();
      if (!s) continue;
      let r;
      try {
        r = JSON.parse(s);
      } catch {
        continue;
      }
      if (!r || typeof r.text !== "string" || !r.text) continue;
      rows.push({
        pkg: String(r.pkg ?? "?"),
        file: String(r.file ?? ""),
        page: r.page != null && Number.isFinite(Number(r.page)) ? Number(r.page) : null,
        seg: r.seg != null && Number.isFinite(Number(r.seg)) ? Number(r.seg) : null,
        lang: String(r.lang ?? "?"),
        text: r.text,
        chars: Number(r.chars) || r.text.length,
      });
    }
  }
  return rows;
}

/** 建原文索引：预计算小写文本 + (pkg) / (pkg,page) 反查表 */
export function buildSourceIndex(rows) {
  const low = new Array(rows.length);
  const byPkg = new Map();
  const byPkgPage = new Map();
  rows.forEach((r, i) => {
    low[i] = norm(r.text).replace(/\s+/g, " ");
    if (!byPkg.has(r.pkg)) byPkg.set(r.pkg, []);
    byPkg.get(r.pkg).push(i);
    const k = `${r.pkg}|${r.page ?? "?"}`;
    if (!byPkgPage.has(k)) byPkgPage.set(k, []);
    byPkgPage.get(k).push(i);
  });
  return { rows, low, byPkg, byPkgPage };
}

function countOf(hay, needle, cap = 12) {
  let c = 0;
  let at = hay.indexOf(needle);
  while (at !== -1 && c < cap) {
    c++;
    at = hay.indexOf(needle, at + needle.length);
  }
  return c;
}

/** 命中片段：以第一个命中的词为中心截一段 */
function snippet(text, tokens, width = 200) {
  const low = norm(text);
  let at = -1;
  for (const t of tokens) {
    const i = low.indexOf(t);
    if (i !== -1 && (at === -1 || i < at)) at = i;
  }
  if (at === -1) return text.slice(0, width * 2).replace(/\s+/g, " ");
  const start = Math.max(0, at - Math.floor(width / 2));
  const end = Math.min(text.length, start + width * 2);
  return (start > 0 ? "…" : "") + text.slice(start, end).replace(/\s+/g, " ") + (end < text.length ? "…" : "");
}

/**
 * 原文层检索：所有词都要命中（AND），按词频与词长加权。
 * opts: { pkg, lang, page, limit }
 */
export function searchSource(idx, query, opts = {}) {
  const q = String(query ?? "").trim();
  if (!q) return [];
  const limit = Math.min(Math.max(Number(opts.limit) || 6, 1), 20);
  const tokens = q
    .split(/\s+/)
    .map((t) => norm(t).replace(/^["'“”]+|["'“”]+$/g, "").trim())
    .filter((t) => t.length >= 2);
  if (!tokens.length) return [];

  let cands = null;
  if (opts.pkg) cands = new Set(idx.byPkg.get(String(opts.pkg)) ?? []);
  if (opts.page != null && opts.pkg) {
    const k = `${opts.pkg}|${Number(opts.page)}`;
    cands = new Set(idx.byPkgPage.get(k) ?? []);
  }

  const out = [];
  const n = idx.rows.length;
  const iter = cands ?? null;
  const visit = iter ? [...iter] : null;
  const total = iter ? visit.length : n;
  for (let j = 0; j < total; j++) {
    const i = visit ? visit[j] : j;
    const r = idx.rows[i];
    if (opts.lang && r.lang !== opts.lang) continue;
    const hay = idx.low[i];
    let score = 0;
    let ok = true;
    for (const t of tokens) {
      const c = countOf(hay, t);
      if (!c) {
        ok = false;
        break;
      }
      // 词越长越可信；短词（2–3 字符）容易遍地都是，压一点权重
      score += c * (1 + Math.min(t.length, 8) * 0.18) * (t.length <= 3 ? 0.55 : 1);
    }
    if (!ok) continue;
    // 段落越短、命中越密，越可能是"就是这一段"
    score *= 1 + Math.min(r.text.length, 1200) / 2400;
    out.push({ row: r, score, snippet: snippet(r.text, tokens) });
  }
  out.sort((a, b) => b.score - a.score || String(a.row.pkg).localeCompare(String(b.row.pkg)) || (a.row.page ?? 0) - (b.row.page ?? 0));
  return out.slice(0, limit);
}

/** 某工程原文规模（给 stats 和"这本书有没有原文"用） */
export function sourceStats(idx) {
  const pkgs = new Map();
  for (const r of idx.rows) {
    const e = pkgs.get(r.pkg) ?? { paras: 0, pages: new Set(), chars: 0, langs: new Set() };
    e.paras++;
    e.chars += r.chars;
    if (r.page != null) e.pages.add(r.page);
    e.langs.add(r.lang);
    pkgs.set(r.pkg, e);
  }
  const langs = new Map();
  for (const r of idx.rows) langs.set(r.lang, (langs.get(r.lang) ?? 0) + 1);
  return { pkgs, langs, total: idx.rows.length, chars: idx.rows.reduce((s, r) => s + r.chars, 0) };
}

/** 取某页（或某段）上下文：前后 around 段，返回渲染块 */
export function pageContext(idx, pkg, page, around = 2) {
  const key = `${pkg}|${page}`;
  const ids = idx.byPkgPage.get(key);
  if (!ids || !ids.length) return null;
  const all = idx.byPkg.get(pkg) ?? [];
  const first = ids[0];
  const last = ids[ids.length - 1];
  const from = Math.max(0, all.indexOf(first) - around);
  const to = Math.min(all.length - 1, all.indexOf(last) + around);
  const rows = all.slice(from, to + 1).map((i) => idx.rows[i]);
  return { pkg, page, rows, before: all.indexOf(first) - from, after: to - all.indexOf(last) };
}

/** 找某工程里离关键词最近的一页（kb_source 只给 pkg 时用） */
export function bestPageFor(idx, pkg, query) {
  const ids = idx.byPkg.get(pkg);
  if (!ids || !ids.length) return null;
  const tokens = norm(query)
    .split(/\s+/)
    .filter((t) => t.length >= 2);
  if (!tokens.length) {
    const r = idx.rows[ids[0]];
    return r.page;
  }
  let best = null;
  for (const i of ids) {
    const hay = idx.low[i];
    let s = 0;
    for (const t of tokens) s += countOf(hay, t);
    if (s > 0 && (!best || s > best.s)) best = { s, page: idx.rows[i].page };
  }
  return best ? best.page : idx.rows[ids[0]].page;
}

export function pkgList(idx) {
  return [...idx.byPkg.keys()].sort();
}

export function existsDir(p) {
  try {
    return existsSync(p) && statSync(p).isDirectory();
  } catch {
    return false;
  }
}
