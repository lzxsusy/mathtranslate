import io, os
root = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论"
sha = "390d5aecaead9f8e37f2702ded89da0882f4a4143ce85137f507197750fe6493"

p = os.path.join(root, "投稿信息.md")
s = io.open(p, encoding="utf-8").read()
a = "| 第 9 批 | §A 附录、参考文献、全部资料卡 | 6906–7937 | 105 | 见末次提交 |"
b = "| 第 9 批 | §A 附录、参考文献、全部资料卡 | 6906–7937 | 105 | `820a88b6` |"
assert a in s
s = s.replace(a, b)
s += ("\n## 七、成品指纹\n\n"
      "- 成品：`成品/范畴表示论与局部几何朗兰兹导论_arXiv-2205.14578_v1.0.pdf`，105 页，"
      "SHA256 `%s`。\n"
      "- PDF 不入库（`.gitignore` 的 `成品/*.pdf`），只随 Release 外链发布；本指纹供下载后核对。\n" % sha)
io.open(p, "w", encoding="utf-8").write(s)

p = os.path.join(root, "工程文件", "reports", "03-终检与交付.md")
s = io.open(p, encoding="utf-8").read()
a = "- `源码/main.pdf` → `成品/范畴表示论与局部几何朗兰兹导论_arXiv-2205.14578_v1.0.pdf`，105 页，SHA256 记录于提交信息之外（PDF 不入库，故只在本地保留）。"
b = ("- `源码/main.pdf` → `成品/范畴表示论与局部几何朗兰兹导论_arXiv-2205.14578_v1.0.pdf`，105 页，\n"
     "  SHA256 `%s`（PDF 不入库，指纹记在 `投稿信息.md` §七）。\n"
     "- 最终提交：`820a88b6`「SY02-21 第 9 批（§A 附录与参考文献）译完，整书 105 页，0 error/0 Overfull；资料卡 5 件与精选片段齐备」，\n"
     "  推送 `atomgit master:main` 与 `origin master:master` 均为 `0aa36f4f..820a88b6`。" % sha)
assert a in s
s = s.replace(a, b)
io.open(p, "w", encoding="utf-8").write(s)
print("ok")
