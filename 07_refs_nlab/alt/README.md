# 替代来源库（work/nlab/alt/）——给施工员与后续核查员看的说明

nLab 缓存（`../`）里 123 个候选条目有 31 个 NOTFOUND。本目录就是这 31 个概念的替代来源库：
每个概念一个 `<概念英文小写下划线>.md`，**六字段固定格式**，`citation_zh` 可直接粘进 `\znote{…}`。

- `INDEX.tsv`：概念英文 / 概念中文 / 文件名 / level / 状态（ok | partial | none）
- `_BIB.tsv`：`lecture02..lecture23.tex` 各讲 `references` 环境里 `\refitem` 条目的机械抽取（60 条，6 列）。
  **教材类引用只许引这张表里出现过的书，章号只许用表里给的那个，不许自己补。**
- 重建：`cd work; python build_bib.py`（_BIB.tsv + _TARGETS.tsv）、`python mk_alt1.py` / `mk_alt2.py` / `mk_alt3.py`；
  校验：`python check_alt.py`（31 条齐全、六字段非空、level 合法）；写 md 与重建 INDEX 的逻辑在 `../altlib.py`。

## 硬规矩（踩过的坑，2026-11-14 实测）

1. **encyclopediaofmath.org 全站 502**（`/wiki/…` 与 `/index.php/…` 同样 502，2026-11-14 实测两次）。
   别再试这个站，改用 MathWorld / nLab / Stacks Project / 本讲参考文献里的教材。
2. **Stacks Project 对不存在的 Tag 也返回 HTTP 200**（例：`0ABC` 打开是 Lemma 40.14.4，不是空页）。
   所以引 Tag 时**必须抓正文、抄下定义原文来核**，不许只凭状态码，也不许凭搜索结果标题猜 Tag。
3. **B 级源一律要打开正文读一眼定义**：标题、摘要或搜索结果里出现该词**不算命中**——标题对 ≠ 含义对。
   反例：MathWorld `Eigenform` 讲的是微分算子的本征形式，不是模形式的 Hecke 特征形式，已弃用；
   `IdeleGroup`、`InertiaGroup`、`RootDatum`、`DualTorus`、`Newform`、`QExpansion`、`Categorification` 等 slug 均 404。
4. **nLab 重定向页不是条目**。`place+at+infinity` 只有一句 stub（"see Arakelov geometry"），
   不可作为 archimedean place 的引证；`symmetric+power` 重定向到 symmetric algebra，
   `categorification` 重定向到 vertical categorification——后两者内容可用，但引文写重定向后的真实标题。
5. **访问日期统一写 2026-11-14**，只在该日真正抓取成功的页面才写这个日期；单纯据书目推的教材引用，
   `verified` 写「书目核对（未逐页翻原文）：……」，不谎称抓过页面。
6. 抓不到的宁可标 `none` 并让正文改用 `\znoteplain`，**绝不编造 URL、Tag 号、章号、定理号、日期**。
7. 教材类（level A）引用只写「作者《书名》（版次/丛书号或卷号），第 N 章（本讲参考文献）」：
   **不写页码、不写定理号**；`verified` 统一写「书目核对（未逐页翻原文）」。补定理号是红线。

## 黑名单与废案（不要再用，抽查时按这个判）

| 来源 | 原因 | 日期 |
|---|---|---|
| encyclopediaofmath.org 全站 | 全站 502（`/wiki/`、`/index.php/` 都试过） | 2026-11-14 |
| MathWorld `Eigenform` | 讲微分算子本征形式，非模形式 Hecke 特征形式 | 2026-11-14 |
| nLab `place+at+infinity` | 仅一句 stub（"see Arakelov geometry"），无定义 | 2026-11-14 |
| MathWorld `IdeleGroup` / `InertiaGroup` / `RayClassGroup` / `RootDatum` / `DualTorus` / `Newform` / `QExpansion` / `Categorification` / `StrongApproximation` / `PrincipalSeries` / `AutomorphicRepresentation` / `AdmissibleRepresentation` / `RayClassField` | 404，页面不存在 | 2026-11-14 |
| Stacks `Tag 0ABC` | 该 Tag 实际指向 Lemma 40.14.4，与想引的内容无关（假 Tag 也 200 的实例） | 2026-11-14 |
