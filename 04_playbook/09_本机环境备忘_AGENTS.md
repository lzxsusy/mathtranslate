# 本机 / 本工作目录备忘（给 DSH agent 看的）

主人的电脑是 Windows 11（2560×1440，缩放 150%），DSH 桌面端，工作目录通常是 `<本地路径>`。

## 交流偏好

- 说中文。结论先行，少绕弯；能干就干，不要反复确认小事。
- 气氛轻松时主动甩表情包（`send_meme`），干活时克制。

## 可以直接用的事实（省得每次重查）

- Python（含 Pillow / numpy / pandas / openpyxl / python-docx / python-pptx / lxml）：
  `<本地路径>`
  `load_workspace_dependencies` 也能拿到路径。
- Node：`<本地路径> Harness\resources\runtime\primary-runtime\dependencies\node\bin\node.exe`
  （`runtime\bin\node.cmd` 依赖 `%DSH_DESKTOP_NODE_EXECUTABLE%`，直接调用会失败。）
- **PowerShell 里没有 heredoc**：`& $py - <<'EOF'` 会报解析错误。要多行脚本就先用 write 工具落一个 `.py`，再 `& $py file.py`。
- PowerShell 输出中文容易乱码：读文件用 read 工具，别用 `Get-Content` 判断内容；
  写文件用 write 工具（UTF-8），避免 `Set-Content`/`Out-File` 的编码坑。
- DSH 的 UI 覆盖样式：`<本地路径>`（见同目录 `Downloads\DSH-美化改动说明.md`），改完 Ctrl+R 生效。
- 桌面控制插件可用：`desktop_windows / desktop_capture / desktop_click / desktop_type` 等。
  窗口标题含中文时先 `desktop_windows` 确认 hwnd。
- DevTools（Electron 的 `dsh-app://app/`）里敲命令必须 `desktop_type` 传 `mode:"unicode"` 逐字键入：
  先输入 `allow pasting` 回车解锁，之后才能粘贴/执行代码；剪贴板方式会被 Chrome 的粘贴防护拦掉。
- 抓屏截图存全分辨率 PNG（`desktop_capture` 传 `maxDim:0` 和 `path`），再用 Pillow 取像素点验证配色，比肉眼可靠。
- 余额 / 花费看侧栏底部，或 `dsh-cost-meter` 的存储：`<本地路径>`。

## 别乱动

- `<本地路径> Mascot\` 是华硕自带壁纸，恢复壁纸用 `<本地路径>`。
- 改 `~/.dsh/profiles/desktop/cordis.patch.yml` 或 `package.json` 里的 bundles 前，先备份；插件改动需要重启 DSH 才生效。
