# -*- coding: utf-8 -*-
"""打印第 NN 章的精读任务书（Lead 填好后直接发给 subagent）。

用法：
    python tools\\chapter_task.py 3            # 打到 stdout
    python tools\\chapter_task.py 3 -o tmp\\task-ch03.md
    python tools\\chapter_task.py all -o tmp   # 9 份都生成到 tmp\\task-chNN.md

数据源：BRIEF.md §5 的九章任务卡（改这里要同步改 BRIEF）。
"""
import sys
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

CH = {
    1: dict(nn="01", author="Andersen & Gammelgaard",
            title="Hitchin 射影平坦联络、Toeplitz 算子与 TQFT 曲线算子的渐近展开",
            zh=(7, 29), en=(10, 33), book=(1, 24), size="76,698", notes=8,
            quota="概念 8 / 例子 2",
            points="Hitchin 联络、射影平坦性、模空间 M 与紧化 M̄、曲线算子（TQFT）、Toeplitz 算子、"
                   "Berezin–Toeplitz 形变量子化、星积 ⋆^BT、Bohr–Sommerfeld 层、几何量子化、半经典（h→0）渐近展开",
            hard="微分几何与辛几何前置多（联络、曲率、复结构形变）；Toeplitz 算子的符号计算密集；"
                 "(3) 式与 Theorem 7 的一阶项符号分歧（已有译注 7、8）。定理环境为 i* 独立编号（Theorem 1–13）"),
    2: dict(nn="02", author="Aprodu & Farkas", title="Koszul 上同调及其在模空间中的应用",
            zh=(30, 54), en=(34, 59), book=(25, 50), size="89,032", notes=14,
            quota="概念 12 / 例子 3",
            points="Koszul 上同调 K_{p,q}(X;L)、合冲 syzygy、极小自由分解、核丛、Hilbert 概形、"
                   "Brill–Noether 闭链、Koszul 闭链、小斜率除子、Green 猜想、棱性（gonality）猜想、"
                   "强极大秩猜想、极小合冲猜想",
            hard="Eagon–Northcott 复形与 Koszul 复形的具体构造；各猜想之间的关系网（谁强谁弱、哪些情形已知）。"
                 "25 个 theorem、7 个 conjecture，是全书概念密度最高的一章"),
    3: dict(nn="03", author="Arcara & Bertram", title="重访 Reider 定理与 Thaddeus 对",
            zh=(55, 71), en=(60, 77), book=(51, 68), size="56,962", notes=5,
            quota="概念 7 / 例子 2",
            points="Reider 定理、Thaddeus 对、Bridge 与翻转（flip）、例外对象/正交基、Bogomolov 型稳定性、"
                   "曲面上的模空间、射影对偶、导出范畴视角（若正文出现）",
            hard="曲面上向量丛的 moduli 与稳定性理论；本章 §3 是重写版，要抓「重访」相比原版改了什么。"
                 "编号混合：application/proposition/corollary 按节共享，iquestion 独立 1–5"),
    4: dict(nn="04", author="Jeffrey", title="奇异向量丛模空间中的相交配对",
            zh=(72, 81), en=(78, 89), book=(69, 80), size="32,374", notes=3,
            quota="概念 6 / 例子 1",
            points="部分消奇异（partial desingularization）、相交上同调、等变上同调、Kiem 定理、"
                   "M(n,d) 与 M(2,0)、相交配对、Kirwan 消奇异、局部化公式",
            hard="相交上同调的层论定义与 de Rham 版本对照；等变上同调在奇点上的行为。"
                 "原书 p.80 是空白背面页。编号混合（iremark 独立 1–3）"),
    5: dict(nn="05", author="Kamnitzer", title="Beilinson–Drinfeld 格拉斯曼流形与辛纽结同调",
            zh=(82, 93), en=(90, 103), book=(81, 94), size="49,385", notes=7,
            quota="概念 8 / 例子 2",
            points="仿射格拉斯曼流形 Gr、Beilinson–Drinfeld 格拉斯曼流形、Hecke 修正、卷积（convolution）积、"
                   "整体奇异格拉斯曼、半局部几何、切片（slice）与切片解消、比较定理、辛纽结同调、"
                   "Khovanov 同调/量子群",
            hard="卷积格拉斯曼的因子化结构；「奇异」与「卷积」两种版本的差异；与 knot homology 的桥在哪一句"),
    6: dict(nn="06", author="Lieblich", title="曲线上层模空间的算术方面",
            zh=(94, 115), en=(104, 129), book=(95, 120), size="92,033", notes=13,
            quota="概念 8 / 例子 2",
            points="模叠 Bun_{n,d}、Gerbe（带 band）、扭曲层（twisted sheaf）、Brauer 群 Br(X)、周期-指标定理、"
                   "抛物丛、分裂分歧（ramified splitting）、Torelli 定理、有理点、形变-障碍理论",
            hard="非交换几何术语（gerbe/band/中立化）与层论上同调的对应；附录 A–C 是自足的技术摘要，"
                 "值得单独导读。编号：§1–4 按节、§5 按小节、附录混合"),
    7: dict(nn="07", author="Newstead", title="代数曲线上 α-稳定凝聚系的存在性",
            zh=(116, 134), en=(130, 149), book=(121, 140), size="58,639", notes=6,
            quota="概念 8 / 例子 2",
            points="凝聚系 (E,V)、α-半稳定/稳定、模空间、存在性定理、边界情形 k=n+1 与 k≥n+2、"
                   "Brill–Noether 型方法、特殊曲线、奇异曲线",
            hard="α 的阈值与稳定性判据；不同 (n,d,k) 区域的证明策略差异（这是本章的组织逻辑，笔记里要画成表）。"
                 "12 个 question，「开放问题」节是全书最有价值的部分之一。原书 p.140 空白背面页"),
    8: dict(nn="08", author="Pareschi & Popa", title="阿贝尔簇上的正则性 III：与一般消没的关系及应用",
            zh=(135, 159), en=(150, 177), book=(141, 168), size="92,371", notes=18,
            quota="概念 9 / 例子 2",
            points="GV-层（generic vanishing）、M-正则层、Ishida 复形、Fourier–Mukai 变换、nef、多典范映射、"
                   "Seshadri 常数、Picard 丛、对称积、半齐次向量丛",
            hard="一般消没理论的前置（GV 猜想的背景）；Fourier–Mukai 与「M-正则 ⇒ 生成」的推理链。"
                 "11 theorem + 11 remark，remark 里常藏反例与比较，批注要抓。已有译注 18 处（全书最多）。"
                 "原书 p.168 空白背面页"),
    9: dict(nn="09", author="Teixidor i Bigas", title="可约曲线上的向量丛及应用",
            zh=(160, 170), en=(178, 189), book=(169, 179), size="37,545", notes=7,
            quota="概念 6 / 例子 1",
            points="可约曲线、斜率稳定无挠层、Hilbert 紧化（Hilbert 多项式）、极限线性系、子丛、Brill–Noether",
            hard="曲线可约/带奇点时稳定性的定义与紧化的比较（Gieseker vs 斜率）；短小但结论密度高。"
                 "英文 PDF p.190 是封底，不译"),
}

TEMPLATE = """你是《Grassmannians, Moduli Spaces and Vector Bundles》中译精读工程的第 {nn} 章读者。
工程根：C:\\Users\\admin\\Downloads\\Grassmannians-精读
你的章：ch{nn} · {author} · 《{title}》
       中译 p.{za}–{zb}（{zp} 页）= 英文 PDF p.{ea}–{eb} = 原书 p.{ba}–{bb}

## 先读（按顺序）
1. `BRIEF.md` 全文（尤其 §1 页表、§7 质量门、§8 文件格式）与 `STATUS.md`。
2. `产出\\汇总\\existing-notes.tsv` 里你这一章的已有译注（{notes} 条）——**这些不要重复登记**；
   若认为某条登记有误，另立 `type=existing-note-wrong` 并说明理由。
3. `source\\TERMINOLOGY.md`（术语权威，只读）。全书 81 处译注的原始清单在 `source\\PROGRESS.md`
   的 `## 原书错误（译注清单）` 里，需要原话时去查你那一篇的表。
4. 你的中文源：`source\\chapters\\ch{nn}.tex`（{size} 字节，全章）。
5. 英文对照：`python tools\\pdf_pages.py text en {ea}-{eb} -o tmp\\en_ch{nn}.txt`，然后逐页读。
6. 版面核对：`python tools\\pdf_pages.py png zh {za} --out 产出\\_pages`，只渲真正需要的页。

## 本章提示（来自 BRIEF §5，是提示不是清单，以正文为准）
- 必抓对象：{points}
- 难点：{hard}
- 卡片配额：{quota}

## 产出（6 个文件，格式见 BRIEF §8）
1. `产出\\导读\\ch{nn}-导读.md`      1200–2000 字，五节：位置 / 前置知识 / 阅读路线 / 核心结果 / 术语对照
2. `产出\\批注\\ch{nn}-批注.md`      ≥12 条，编号连续；五种类型都要有（数学-难点 / 数学-补证 / 译注-核对 /
                                    译文-问题 / 联系-他章），可另加 背景-补充
3. `产出\\批注\\ch{nn}-errata.tsv`   对读发现的问题：chapter,loc_book,loc_zh,loc_tex,type,severity,original,problem,suggestion,evidence
4. `产出\\笔记\\ch{nn}-笔记.md`      1500–2500 字，五节：主线 / 关键构造 / 我的补全 / 疑问 / 延伸
5. `产出\\汇总\\cards-ch{nn}.tsv`    ≥6 概念卡 + ≥1 例子卡候选：local_id,type,title_en,title_zh,track,one_line,anchor
6. `产出\\汇总\\ch{nn}-report.md`    做了什么 / 统计 / 存疑 / 给 Lead 的 TODO

## 硬规则
- 只写上面 6 个路径（以及 `tmp\\` 下你自己的临时文件）；不改 `source\\`、`original\\`、别的章的文件。
- 中文数学以 .tex 为准；公式不要从 PDF 文字层抄（会被拆碎，如 `DV f = V [f] + ˜D(V )(f)`）。
- 页码三种写法别混：`原书 p.N` / `中译 p.N` / `英文 PDF p.N`。
- 术语照 `TERMINOLOGY.md`；新术语记在 `cards-ch{nn}.tsv` 的 note 里或在 report 里列，不改术语表。
- 卡片候选的 `anchor` 必须是 `chapters/ch{nn}.tex:行号`，且行号真指向该内容（写完回查一次）。
- 不编造：读不懂的地方写进笔记「疑问」节并在 report 里点出来，不许假装读懂。
- 文件 UTF-8 无 BOM、LF；用 write 工具写，不要用 shell 重定向写中文。
- 交前自检：6 个文件都在、字数达标、批注编号连续、tsv 每个字段数与表头一致（正文里不许出现裸 tab）。
"""


def render(n):
    d = CH[n]
    return TEMPLATE.format(
        nn=d["nn"], author=d["author"], title=d["title"],
        za=d["zh"][0], zb=d["zh"][1], zp=d["zh"][1] - d["zh"][0] + 1,
        ea=d["en"][0], eb=d["en"][1], ba=d["book"][0], bb=d["book"][1],
        size=d["size"], notes=d["notes"], quota=d["quota"],
        points=d["points"], hard=d["hard"],
    )


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    out = None
    if "-o" in sys.argv:
        out = sys.argv[sys.argv.index("-o") + 1]
    if not args:
        print("用法: python tools/chapter_task.py 3 [-o tmp/task-ch03.md] | all -o tmp")
        return 2
    which = args[0].lower()
    if which == "all":
        base = out or os.path.join(ROOT, "tmp")
        os.makedirs(base, exist_ok=True)
        for n in CH:
            p = os.path.join(base, "task-ch%s.md" % CH[n]["nn"])
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(render(n))
            print("wrote", p)
        return 0
    n = int(which)
    if n not in CH:
        print("章号必须是 1-9")
        return 2
    text = render(n)
    if out:
        os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("wrote", os.path.abspath(out))
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
