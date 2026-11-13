# DSH 桌面端 · 外观与环境改动说明（2026-11-12）

> 本文档记录这次「装插件 + 美化界面/桌面」改了哪些东西、怎么改回去、以后怎么维护。

## 一、外观主题：深海墨蓝 Dark Ocean

**入口文件**：`<本地路径>`（由已安装的 `dsh-ui-overrides` 插件在每次页面加载时注入）

- 改完保存后，在 DSH 里按 **Ctrl+R** 生效；删掉这个文件即 100% 还原成默认外观。
- 改的是设计令牌（`--dsw-alias-*` / `--dsw-specific-*` / 圆角 / 阴影），所以所有插件（侧栏、气泡、输入框、任务看板、表情包、指挥台…）都会跟着变，不用逐个改。
- 追加的结构化规则用「类名片段」选择器（如 `[class*="_sessionRow"]`、`[class*="_tabActive"]`、`[class*="_composerStack"]`），这样 DSH 升级、哈希类名变化后依然命中。

**配色速查**

| 用途 | 值 |
| --- | --- |
| 底色 bg-base | `#0b0f15` |
| 侧栏 | `linear-gradient(#101620 → #0c1119)`，右侧 1px 冷色描边 |
| 浮层 layer-1/2/3 | `#131a24` / `#171f2b` / `#1d2733` |
| 品牌海蓝 | `#4d7cfe`（悬停 `#6f97ff`） |
| 点缀青 | `#3ddad0` |
| 正文/次级/三级文字 | `#e8eef8` / `#a6b6cc` / `#8497ae` |
| 圆角 | 6 / 10 / 14 / 18 / 22 / 18 |

**改动清单（人话版）**

1. 底色从「中性灰 #151517」换成带蓝调的深海墨色，主背景叠两团极淡的蓝/青光晕，避免大片死黑。
2. 侧栏做成独立玻璃板：竖向渐变 + 右侧冷色描边；会话行悬停发亮，**选中的会话是海蓝渐变 + 左侧亮条**。
3. 顶部标签（对话/轨迹/文件转换…）选中项改成白字 + 2px 海蓝下划线。
4. 输入卡片浮起：深色卡面 + 1px 冷色描边 + 圆角 20px，聚焦时套一圈蓝色光晕。
5. 「新会话」按钮做成整屏唯一的品牌色实心渐变按钮，当视觉锚点。
6. 用户气泡偏海蓝（`#1b2942 → #16202e`）；思考块左侧加一根青色细导线，长对话更好扫读。
7. 次级/三级文字整体提亮一档（原来的灰在长文里糊成一片）。
8. 弹窗/菜单统一圆角 14px + 毛玻璃；滚动条更细、半透明；选中文字与焦点环统一成品牌蓝。

**已知的小补丁**：`<本地路径>`
被改成注入 `/dsh-ui-overrides/user.css`（去掉了上游的 `?v=` 查询串，桌面端 `dsh-app://` 转发层对它不友好）。
原始版本备份在 `client.js.bak`。**重装/升级这个插件会覆盖此文件**，届时若 CSS 不再生效，照同样方式再改一次，或改用 DevTools 强制刷新：
```js
document.getElementById('dsh-ui-overrides').href='/dsh-ui-overrides/user.css?t='+Date.now()
```

**DevTools 小技巧**：Console 会拦粘贴代码。先手动输入 `allow pasting` 回车解锁，之后才允许粘贴（本会话里则是用真实按键逐字敲的）。

## 二、桌面壁纸

- 新壁纸：`<本地路径>`（与主题同色系，纯本地生成）
- 生成脚本：`<本地路径>`（改颜色/字标后重跑即可）
- 一键还原原壁纸（ASUS TX Mascot 动态壁纸）：`<本地路径>`

## 三、新装的插件（需要重启 DSH 才会加载）

| 插件 | 作用 |
| --- | --- |
| `@deepseek-ai/dsh-experimental-session-titles-bundle` | 会话标题随每轮提问自动刷新，侧栏标题更准确 |
| `@deepseek-ai/dsh-experimental-voice-input-bundle` | 语音输入（SenseVoice，首次使用才下载运行时，全本地） |
| `@deepseek-ai/dsh-experimental-inspector-profile` | 原始会话日志 / 节点检查器，排查 agent 行为时用 |
| `@deepseek-ai/dsh-experimental-plugin-market-bundle` | 插件市场「发现」页：从自定义插件索引浏览安装 |

安装方式（命令行等价物）：DSH 左侧「插件」页，或 `plugin_manager` 工具 `install_bundle`。
本次全部通过 profile 的 `package.json` → `dsh.profile.bundles` 注册，配置在
`<本地路径>`。

**回滚**：`plugin_manager` 里对对应 bundle 执行 disable/remove，或从 `package.json` 的 `dsh.profile.bundles` 里删掉那一行。

## 四、环境体检（当前可用）

- Node `v24.21.0`、Python（含 Pillow / numpy / pandas / python-docx / python-pptx / openpyxl）
- 已装并启用的效率插件：`billion-context`（长会话压缩，命中率 99%）、`dsh-cost-meter`（计费）、
  `dsh-perf-boost`（实测省 18% 主线程时间）、`dsh-keep-awake`（长任务期间不休眠）、
  `dsh-archive-manager`（会话归档）、`latex-look`、`dsh-file-convert`、任务看板、桌宠、桌面控制。
- 新增 `<本地路径>`：把本机 Python/Node 路径、PowerShell 没有 heredoc、
  DevTools 要先 `allow pasting` 这类踩过的坑写成了常驻备忘，以后新会话不用重新摸一遍。
- 想再补齐的（需你同意才下载）：`ffmpeg`（视频转换/压缩，约 56MB）、Tesseract OCR 语言包（扫描版 PDF 识别，10–30MB）。

## 五、如何验证没搞坏东西

1. 重启 DSH（插件需要重启才生效）。
2. 外观不对 → 删 `<本地路径>` 后 Ctrl+R，恢复原样。
3. 插件报错 → 左栏「插件」页把新装的那四个先关掉。
