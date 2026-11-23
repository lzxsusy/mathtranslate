# dsh-kb 上架记录（awesome-dsh-plugin）

插件市场（dshmarket）本身不是目录：条目来自 [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)
的 `data/plugins/*.yml`，站点与 `plugins.json` 由那里的脚本生成。**上架 = 在那个仓库加一个 yml 文件。**

## 一、当前状态

| 项 | 状态 |
|---|---|
| GitHub 仓库（`url` 指向的子目录） | ✅ https://github.com/lzxsusy/mathtranslate/tree/main/plugins/dsh-kb |
| 包清单 `dsh.bundle` + `cordis.patch.yml` | ✅ `plugins/dsh-kb/package.json` 与同目录 `cordis.patch.yml` |
| 图标（市场只从 GitHub 图床加载） | ✅ `assets/icon-180.png`（180×180 PNG，由 `assets/icon.svg` 渲染） |
| 可安装地址 | ✅ `github:lzxsusy/mathtranslate#path:/plugins/dsh-kb`；另保留 AtomGit raw tarball |
| 投稿 PR | ✅ [#18102](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/pull/18102)（分支 `lzxsusy:add-dsh-kb`） |

PR 建好后 CI 显示 `action_required`（0 个 job）——这是 GitHub 对**首次贡献者**的
「维护者批准后才运行工作流」闸门，不是检查失败；维护者批准后 `PR check` 会自动跑。

## 二、投稿文件内容（`data/plugins/lzxsusy__mathtranslate--plugins-dsh-kb.yml`）

```yaml
url: https://github.com/lzxsusy/mathtranslate/tree/main/plugins/dsh-kb
name: lzxsusy/mathtranslate#dsh-kb
category: docs
description:
  en: '…（一行，说明它做什么：1,250 张带页码/来源等级/caveat 的数学文献卡，随包自带，纯 JS 无网络）'
  zh: '…'
icon: https://raw.githubusercontent.com/lzxsusy/mathtranslate/main/plugins/dsh-kb/assets/icon-180.png
```

文件名规则来自其 `contributing.md`：`<owner>__<repo>.yml`，monorepo 子包用
`owner__repo--<路径用短横线连接>.yml`。

## 三、安装方式（不依赖市场也能装）

1. **GitHub 子目录**（市场条目就是这个）：
   ```
   dsh plugin --profile desktop add "github:lzxsusy/mathtranslate#path:/plugins/dsh-kb"
   ```
2. **预打包 tarball（AtomGit 源）**：
   ```
   dsh plugin --profile desktop add https://atomgit.com/api/v5/repos/lzxSUSUY/mathtranslate/raw/plugins/dsh-kb-0.2.1.tgz
   ```
3. **本地包**：`dsh plugin --profile desktop add ./plugins/dsh-kb-0.2.1.tgz`

## 四、上架后还能补的

- **screenshots**：市场仓库的 `data/screenshots.json` 按仓库名收图（GitHub 图床），可另提 PR 补 2 张
  （`kb_search` 命中卡、`kb_stats` 输出）。
- **npm 发布**：`npm installs are prebuilt and skip the allowBuilds approval`——发到 npm 后市场会给
  一条 `npm i` 式安装命令，更适合普通用户。需要 npm 账号与 token。
- **更新**：改代码后 bump `package.json` 版本号重新打 tarball；市场按 `package.json` 版本或
  pinned commit 判断更新。
