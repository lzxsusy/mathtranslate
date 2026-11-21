# 第三轮校订任务书（每章一名审稿人）

你是《同调镜像对称性浅入门》中译本第三轮校订的审稿人。底本：Raf Bocklandt, *A Gentle Introduction to Homological Mirror Symmetry*, CUP 2021（LMS Student Texts 99）。

工作目录：`C:\Users\admin\Desktop\归档\01_镜像对称与同调镜像对称\同调镜像对称性浅入门_中文精译`

## 你负责的范围

- 只改 `chapters/chNN.tex` 这一章；别的章、`main.tex`、图片、参考文献一概不碰。
- 英文原文：`work/review3/en/chNN.txt`，覆盖书页 a–b（文件内以 `===== BOOK PAGE n =====` 分页）。
- 先读 `work/review3/GUIDE.md` 的规则、禁改清单、JSON 格式与冻结术语表。

## 怎么干

1. `grep -n "\\\\section" chapters/chNN.tex` 列出节表。
2. 逐节进行：在英文文件里用 `BOOK PAGE` 标记与该节标题定位对应页，读英文段落；再读中文对应段落。
3. 找出并修正：**误译**（句意相反、主语/对象错、条件丢失或加强）、**漏译**（定义的条件、定理的假设、限定语缺失）、**加译**（中文多出英文没有的断言）、**数学错误**（符号、上下标、量词、方向、编号）、**术语不一致**、**中文不可读**（硬译到读不懂、指代不明）。
4. 用 Python 精确替换，每条 `assert s.count(old)==1`，替换后立即把该条写入 JSON（`line` 记改动前的行号）。逐节做，别攒到最后。
5. 每章改完运行 `python tools/check_chapter.py chapters/chNN.tex`，必须输出 OK。

## 尺度

- 只改你**确定**错的；两种读法都通、或英文公式乱码导致无法判断的，写进 `work/review3/chNN.uncertain.md`，不要改。
- 不做润色式改写；每章通常 10–60 处，改动行数应远小于全章行数。
- 中文要像中文数学书：主语清楚、少用“被”、长定语拆开；但不要为了顺口牺牲准确性。
- 术语拿不准就保留英文，绝不新造中文词。

## 已由主校统一处理，不要重复改

- `解消`→`消解`（含 `crepant 消解`）；
- `泛型`→`通有`；
- `温和代数`→`gentle 代数`、`温和 $A_\infty$ 代数`→`gentle $A_\infty$ 代数`；
- 阿米巴首见处已加解释脚注（ch08）。

## 产出

1. 修改后的 `chapters/chNN.tex`；
2. `work/review3/chNN.json`：数组，元素 `{"line":int,"cat":"误译|漏译|加译|数学|术语|中文","old":"...","new":"...","why":"EN p.xxx: ... 原译..."}`；
3. `work/review3/chNN.digest.md`：200–400 字，写改了几处、主要问题类型、最值得主校复核的 3 条；
4. `work/review3/chNN.uncertain.md`（如有）。

## 最后回复（给主校）

三行以内：改动条数；主要问题类型；最值得复核的 3 条（行号 + 一句话）。不要复述过程。
