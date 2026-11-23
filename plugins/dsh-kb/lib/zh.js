/**
 * 译文层检索（dsh-kb 0.3.1）
 *
 * 三层数据的分工：
 *   卡片层（data/cards）  —— 我们读出来的结构化结论（1,250 张，覆盖不全）
 *   原文层（data/src）    —— 底本自己说的话（7,644 段，只有公开了原文的 33 个工程）
 *   译文层（data/zh）     —— 我们自己的中文译文（49,035 段，覆盖 81 个工程，最全）
 *
 * 为什么必须有这一层：直接搜「几何内窥与镜像对称」时，卡片层 0 张、原文层也没收这个工程，
 * 但译文层里 SY01-07 就有 166 段在讲它。只查卡片会让人以为「库里没有」。
 *
 * 检索方式与原文层一致：线性扫描。49k 段 × 平均 150 字，单查询十几到几十毫秒，
 * 比建 bigram 倒排省几百 MB 内存。
 */
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";
import { gunzipSync } from "node:zlib";

const norm = (s) => String(s ?? "").toLowerCase();

/** 数据戳：目录里最新 mtime + 文件数，用来判断缓存是否失效 */
export function zhStamp(dir) {
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

export function existsDir(dir) {
  try {
    return !!dir && existsSync(dir) && statSync(dir).isDirectory();
  } catch {
    return false;
  }
}

/** 读行：支持 .jsonl 与 .jsonl.gz */
export function loadZhRows(dir) {
  const rows = [];
  const seen = new Set();
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
      // 语料里有重复行（同一段被两个文件各收一次）：按 pkg + para + 文本去重，
      // 否则同一个段落会在结果里占两三个位置。
      // 长段按文本去重（同一段常被两个文件各收一次），短段仍按 para 区分
      const t0 = r.text.trim();
      const key =
        t0.length >= 40
          ? `${r.pkg ?? "?"}#t#${t0}`
          : `${r.pkg ?? "?"}#p#${r.para ?? "?"}#${t0}`;
      if (seen.has(key)) continue;
      seen.add(key);
      rows.push({
        pkg: String(r.pkg ?? "?"),
        file: String(r.file ?? ""),
        para: r.para != null && Number.isFinite(Number(r.para)) ? Number(r.para) : null,
        paraId: String(r.para_id ?? ""),
        page: r.page_orig != null && Number.isFinite(Number(r.page_orig)) ? Number(r.page_orig) : null,
        env: String(r.env ?? "text"),
        tier: String(r.tier ?? "?"),
        text: r.text,
        chars: Number(r.zh_chars) || r.text.length,
        flags: Array.isArray(r.flags) ? r.flags : [],
      });
    }
  }
  return rows;
}

/** 建索引：只预存小写文本与按工程/段号的反查表 */
export function buildZhIndex(rows) {
  const low = rows.map((r) => norm(r.text));
  const byPkg = new Map();
  const byKey = new Map();
  rows.forEach((r, i) => {
    let arr = byPkg.get(r.pkg);
    if (!arr) byPkg.set(r.pkg, (arr = []));
    arr.push(i);
    if (r.para != null) byKey.set(`${r.pkg}#${r.para}`, i);
  });
  return { rows, low, byPkg, byKey };
}

/** 段落里命中的词数（上限 6 次/词），用于排序 */
function hitsOf(lowText, tokens) {
  let n = 0;
  for (const t of tokens) {
    if (!t) continue;
    let c = 1;
    let at = lowText.indexOf(t);
    while (at !== -1 && c < 6) {
      c++;
      at = lowText.indexOf(t, at + t.length);
    }
    n += c;
  }
  return n;
}

const ENV_BONUS = { theorem: 1.15, definition: 1.15, proof: 1.05, example: 1.05, remark: 1.0, text: 1.0 };

/** 检索译文层：所有词都要命中（AND），按命中密度与段落性质排序 */
export function searchZh(idx, query, opts = {}) {
  const q = String(query ?? "").trim();
  if (!q) return [];
  const limit = Math.min(Math.max(Number(opts.limit) || 6, 1), 20);
  const tokens = q
    .toLowerCase()
    .split(/\s+/)
    .map((t) => t.trim())
    .filter(Boolean);
  if (!tokens.length) return [];

  let pool = null;
  if (opts.pkg && idx.byPkg.has(String(opts.pkg))) pool = idx.byPkg.get(String(opts.pkg));
  const scan = pool ?? idx.rows.map((_, i) => i);

  const out = [];
  for (const i of scan) {
    const r = idx.rows[i];
    if (opts.env && r.env !== String(opts.env)) continue;
    if (opts.tier && r.tier !== String(opts.tier)) continue;
    const lowText = idx.low[i];
    let ok = true;
    for (const t of tokens) {
      if (!lowText.includes(t)) {
        ok = false;
        break;
      }
    }
    if (!ok) continue;
    const h = hitsOf(lowText, tokens);
    const bonus = ENV_BONUS[r.env] ?? 1.0;
    const score = (h * bonus) / Math.sqrt(Math.max(r.chars, 40) / 200);
    out.push({ row: r, score });
  }
  out.sort((a, b) => {
    if (b.score !== a.score) return b.score - a.score;
    const pk = a.row.pkg.localeCompare(b.row.pkg);
    if (pk !== 0) return pk;
    return (a.row.para ?? 0) - (b.row.para ?? 0);
  });
  return out.slice(0, limit);
}

/** 抽命中片段 */
export function snippet(text, query, width = 190) {
  const t = String(query ?? "")
    .toLowerCase()
    .split(/\s+/)
    .filter(Boolean);
  const low = norm(text);
  let at = -1;
  for (const tok of t) {
    at = low.indexOf(tok);
    if (at !== -1) break;
  }
  if (at === -1) return text.length > width ? text.slice(0, width) + "…" : text;
  const start = Math.max(0, at - Math.floor(width / 3));
  const end = Math.min(text.length, start + width);
  return (start > 0 ? "…" : "") + text.slice(start, end) + (end < text.length ? "…" : "");
}

export function zhStats(idx) {
  const rows = idx.rows;
  const chars = rows.reduce((a, r) => a + r.chars, 0);
  const byPkg = new Map();
  const envs = new Map();
  const tiers = new Map();
  const pages = new Set();
  for (const r of rows) {
    byPkg.set(r.pkg, (byPkg.get(r.pkg) ?? 0) + 1);
    envs.set(r.env, (envs.get(r.env) ?? 0) + 1);
    tiers.set(r.tier, (tiers.get(r.tier) ?? 0) + 1);
    if (r.page != null) pages.add(`${r.pkg}#${r.page}`);
  }
  const top = [...byPkg.entries()].sort((a, b) => b[1] - a[1]);
  return { paragraphs: rows.length, projects: byPkg.size, chars, pages: pages.size, envs, tiers, top };
}

/** 取某段的中文译文 + 前后文 */
export function paraContext(idx, pkg, para, around = 2) {
  const key = `${pkg}#${para}`;
  let i = idx.byKey.get(key);
  if (i == null) {
    // 该工程所有段里挑最接近的段号
    const pool = idx.byPkg.get(String(pkg)) ?? [];
    let best = -1;
    for (const j of pool) {
      const p = idx.rows[j].para;
      if (p == null) continue;
      if (best === -1 || Math.abs(p - para) < Math.abs(idx.rows[best].para - para)) best = j;
    }
    if (best === -1) return null;
    i = best;
  }
  const lo = Math.max(0, i - around);
  const hi = Math.min(idx.rows.length, i + around + 1);
  return { center: i, span: idx.rows.slice(lo, hi), lo, hi };
}

/** 只给 pkg + query：在这一部里找最相关的一段 */
export function bestPara(idx, pkg, query) {
  const hits = searchZh(idx, query, { pkg, limit: 1 });
  return hits.length ? hits[0].row : null;
}

export function pkgList(idx) {
  return [...idx.byPkg.keys()].sort();
}
