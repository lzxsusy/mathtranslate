# plugins/ — dsh-kb 插件分发

`dsh-kb` 是本仓库的配套插件：**把 kb/ 里的资料卡变成 agent 能直接检索的工具**。
包内自带三层数据：`data/cards/*.jsonl`（2,782 张卡 / 46 部作品）、
`data/zh/zh_paragraphs.jsonl.gz`（47,802 段中文译文 / 82 个工程）与
`data/src/src_paragraphs.jsonl.gz`（7,644 段底本原文抽文 / 33 个工程）。装好即查，
不需要 clone 本仓库，不需要 Python、不需要 SQLite、不需要配置任何路径。

## 安装（三种方式，任选其一）

**① 直接给 DSH 一条命令（推荐，最快）**

```powershell
dsh plugin --profile desktop add https://atomgit.com/api/v5/repos/lzxSUSUY/mathtranslate/raw/plugins/dsh-kb-0.3.3.tgz
```

或在 DSH 会话里让我装：

```
plugin_manager({ action: "install_bundle",
                 target: "https://atomgit.com/api/v5/repos/lzxSUSUY/mathtranslate/raw/plugins/dsh-kb-0.3.3.tgz" })
```

**② 从本地 tarball 装**（已下载 `dsh-kb-0.3.3.tgz` 时）

```
plugin_manager({ action: "install_bundle", target: "file:C:/path/to/dsh-kb-0.3.3.tgz" })
```

**③ 从源码目录装**（想改代码）

```
plugin_manager({ action: "install_bundle", target: "file:C:/path/to/dsh-kb" })
```

装完重启 DSH 桌面端，会话里会出现 6 个工具：
`kb_search`（`layer=cards|zh|source|both|all`）/ `kb_zh` / `kb_source` / `kb_card` / `kb_brief` / `kb_stats`。

## 挂到自己的数据（可选）

插件默认读包内数据。想用更新/更大的库，在 profile 插件配置里指到任意含 `kb/cards/*.jsonl` 的仓库根：

```yaml
- id: dsh-kb
  name: dsh-kb
  config:
    repo: "C:\\Users\\admin\\Desktop\\数译发布\\gitee_shuyi"
    pageRoots:
      glc: "C:\\path\\to\\pages"     # 可选：回源页码对应的页图目录
```

## 自带一个市场目录（DSHM_REGISTRY_URL）

`plugins.json` 是一份最小可用的市场目录（只有一个条目）。把它挂成镜像：

```powershell
$env:DSHM_REGISTRY_URL = "https://atomgit.com/api/v5/repos/lzxSUSUY/mathtranslate/raw/plugins/plugins.json"
```

市场客户端会按同一份结构展示条目（图标/截图字段在本镜像里为空是正常的：市场只从 GitHub 图床加载图片）。

## 版本

| 版本 | 变化 |
|---|---|
| 0.3.1 | 补 bug（无命中查询不再拿全库兜底）+ 新增**译文层**：`kb_search(layer=zh/all)` + `kb_zh`，随包 47,802 段中文译文（8.1 MB gz） |
| 0.3.2 | 2026-11-23 | 资料卡 1,250 → 2,782；gen2 解析（论证链/结果清单/论证地图/术语勘误）；降级检索最长连续子串 |
| 0.3.0 | 新增**原文层**：`kb_search(layer=source/both)` + `kb_source(pkg,page)`，随包 7,644 段原文抽文（33 个工程，2.2 MB gz） |
| 0.2.1 | 数据随包（1,250 卡）、纯 JS 检索、零配置；新增中文 bigram 检索（两个字的中文词也能查） |
| 0.1.0 | 首个版本：调用仓库里的 Python + SQLite FTS5 |

## 已知限制

- 中文检索按 bigram 切分，**单个汉字**查询会退化为全库扫描（能查，但慢）。
- 卡片复核对数不一：`draft` 默认不返回；`pages` 多为启发式抽取，卡上 `caveat` 会说明。
- 没有向量检索：1–3 万卡规模下，倒排 + 术语归一已经够用；需要语义检索时再上。
- 原文层只有 33 个工程（仓库里公开了原文文本的那些），592 段无页码；不是全书全文。
