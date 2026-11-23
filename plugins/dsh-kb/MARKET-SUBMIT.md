# dsh-kb 上架材料（awesome-dsh-plugin 条目）

插件市场（dshmarket）本身**不是目录**：条目来自 awesome-dsh-plugin 列表，站点与市场从那里生成
`plugins.json`。所以「上架」= 在那个仓库的列表里加一条。

## 一、还缺什么（不能直接提 PR 的原因）

| 需要 | 现状 |
|---|---|
| GitHub 仓库 URL（`url` 字段） | ❌ 当前网络 `github.com:443` 不通，账号也没建成；代码暂在 AtomGit |
| 图标（`icon`，市场只从 GitHub 图床加载） | ✅ 已有 `assets/icon.svg`，需放进 GitHub 仓库 |
| 截图（`screenshots`，同样只从 GitHub 图床） | ✅ 可现生成：`kb_search` 命中卡片、`kb_stats` 输出 |
| 可安装地址（`install`） | ✅ 已可用：AtomGit raw tarball，实测 `install_bundle` 成功 |

**结论**：插件已经可用（一条命令能装、装好自带数据），只是「进市场列表」这一步卡在 GitHub 可达性。
下面的内容准备好，等 GitHub 能用（或换台机器/手机热点）10 分钟就能提 PR。

## 二、要在 awesome-dsh-plugin 里加的一条

在列表里（按其 README 的格式）新增：

```markdown
- [dsh-kb](https://github.com/<OWNER>/dsh-kb) — 数译知识库：带页码/来源/可信度的数学文献资料卡检索，
  自带 1,250 张卡（45 部已译数学文献），纯 JS 零依赖。`kb_search` / `kb_card` / `kb_brief` / `kb_stats`。
  `install: dsh plugin --profile desktop add <tarball URL>`
```

## 三、生成后的 registry 条目长这样（与 plugins.json 字段一致）

```json
{
  "name": "dsh-kb",
  "owner": "<OWNER>",
  "url": "https://github.com/<OWNER>/dsh-kb",
  "category": "knowledge",
  "description": {
    "en": "Math-literature knowledge base with page numbers, sources and verification status: 1,250 structured cards from 45 translated works, bundled so it works right after install. Pure-JS search, zero config. Every hit carries a page, a source grade and a caveat — leads with provenance, not answers.",
    "zh": "带页码、带来源、带可信度的数学文献知识库：随包自带 1,250 张结构化卡片（45 部已译文献），装好即查；纯 JS 检索、零配置。每条结果都带原文页码、来源等级与 caveat —— 给的是带出处的线索，不是结论。"
  },
  "capabilities": [],
  "install": "dsh plugin --profile desktop add <tarball URL>",
  "icon": "https://raw.githubusercontent.com/<OWNER>/dsh-kb/main/assets/icon.svg",
  "screenshots": [
    "https://raw.githubusercontent.com/<OWNER>/dsh-kb/HEAD/docs/preview-search.png",
    "https://raw.githubusercontent.com/<OWNER>/dsh-kb/HEAD/docs/preview-stats.png"
  ]
}
```

> `capabilities: []` 是我们的卖点：不跑 shell、不写文件、不发网络请求——只读包内 JSON 再检索。

## 四、今天就能做的分发（不依赖市场）

1. **AtomGit raw 一条命令安装**（已验证）：
   ```
   dsh plugin --profile desktop add https://atomgit.com/api/v5/repos/lzxSUSUY/mathtranslate/raw/plugins/dsh-kb-0.2.0.tgz
   ```
2. **自建市场镜像**：把 `plugins/plugins.json` 挂上 `DSHM_REGISTRY_URL`，市场客户端就能列出本插件
   （图标/截图会空，因为市场只从 GitHub 图床取图）。

## 五、下次打包清单（发版时照做）

```powershell
# 1) 从上游仓库重建卡片数据
python kb/ingest.py all
python kb/build_kb.py
# 2) 把数据同步进插件包
Copy-Item gitee_shuyi\kb\cards\*.jsonl dsh-kb\data\cards\ -Force
# 3) 改版本号 → 打包
node <pnpm.cjs> pack --pack-destination .
# 4) 放到仓库 plugins/ 并推送
Copy-Item dsh-kb-*.tgz gitee_shuyi\plugins\ -Force
# 5) 更新 plugins/plugins.json 与 plugins/README.md 里的版本号/URL
```
