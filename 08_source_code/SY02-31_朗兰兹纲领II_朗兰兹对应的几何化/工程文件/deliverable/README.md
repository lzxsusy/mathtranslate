# deliverable 说明

按仓库上传规范（`04_playbook/17_仓库理念与上传规范.md` §3.3）与 R3 判定，本工程**不入库成品 PDF**：

- 底本 *The Langlands Program II: Geometrization of the Langlands Correspondence*（AMS，Proc. Sympos. Pure Math. 112.2）为在版图书，权利归作者与 AMS；
- 译本是演绎作品，仓库只保存**源码、工程文件、术语与资料卡**；
- 需要 PDF 时由使用者自行编译：

```
cd ../源码
xelatex main.tex && xelatex main.tex && xelatex main.tex
```

产物 `main.pdf` 约 495 页（A4）。编译环境与审计结果见 `../工程文件/reports/U04_编译与审计.md`。
