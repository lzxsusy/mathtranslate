# -*- coding: utf-8 -*-
"""按 check_bib.py 的报告修补 ch21.tex 的参考文献条目。

每条 = (行号, 该行必含的旧片段, 新行全文)。带 guard，行内容不符即报错退出，不写入。
用法：cd 工程文件/scripts && python fix_bib.py
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CH21 = os.path.normpath(os.path.join(HERE, "..", "..", "源码", "chunks", "ch21.tex"))

FIXES = [
    # —— 会议/文集条目：补丛书名，出版年取书的年份而非会议年份 ——
    (15, r"\bibitem{BBD}",
     r"\bibitem{BBD} A. A. Be{\u\i}linson, J. Bernstein and P. Deligne, \emph{Faisceaux pervers}, Ast\'erisque \textbf{100} (1982), 5--171."),
    (17, r"\bibitem{Be}",
     r"\bibitem{Be} A. A. Be{\u\i}linson, \emph{How to glue perverse sheaves}, Lecture Notes in Math. \textbf{1289} (1987), 42--51."),
    (41, r"\bibitem{SGA4.5}",
     r"\bibitem{SGA4.5} Pierre Deligne, \emph{Th\'eor\`emes de finitude en cohomologie $\ell$-adique}, in \emph{Cohomologie \'etale}, Lecture Notes in Math. \textbf{569} (1977), 233--261."),
    (43, r"\bibitem{DM}",
     r"\bibitem{DM} Pierre Deligne and James S. Milne, \emph{Tannakian categories}, in \emph{Hodge cycles, motives, and Shimura varieties}, Lecture Notes in Math. \textbf{900} (1982), 101--228."),
    (47, r"\bibitem{Dr}",
     r"\bibitem{Dr} Vladimir Drinfeld, \emph{Infinite-dimensional vector bundles in algebraic geometry: an introduction}, Progr. Math. \textbf{244} (2006), 263--304."),
    (69, r"\bibitem{Gortz}",
     r"\bibitem{Gortz} Ulrich G{\"o}rtz, \emph{Affine Springer fibers and affine Deligne-Lusztig varieties}, Trends Math. (2010), 1--50."),
    (71, r"\bibitem{Gr}",
     r"\bibitem{Gr} Benedict H. Gross, \emph{On the Satake isomorphism}, London Math. Soc. Lecture Note Ser. \textbf{254} (1998), 223--237."),
    (85, r"\bibitem{KL}",
     r"\bibitem{KL} David Kazhdan and George Lusztig, \emph{Schubert varieties and Poincar\'e duality}, Proc. Sympos. Pure Math., XXXVI (1980), 185--203."),
    (101, r"\bibitem{Lu}",
     r"\bibitem{Lu} George Lusztig, \emph{Singularities, character formulas, and a $q$-analog of weight multiplicities}, Ast\'erisque \textbf{101} (1983), 208--229."),
    (105, r"\bibitem{MS}",
     r"\bibitem{MS} James S. Milne and Kuang-yen Shih, \emph{Conjugates of Shimura varieties}, in \emph{Hodge cycles, motives, and Shimura varieties}, Lecture Notes in Math. \textbf{900} (1982), 280--356."),
    (145, r"\bibitem{So}",
     r"\bibitem{So} Christoph Sorger, \emph{Lectures on moduli of principal $G$-bundles over algebraic curves}, ICTP Lect. Notes \textbf{1} (2000), 1--57."),
    (147, r"\bibitem{Sp}",
     r"\bibitem{Sp} T. A. Springer, \emph{Reductive groups}, Proc. Sympos. Pure Math., XXXIII (1979), 3--27."),
    (151, r"\bibitem{Ti}",
     r"\bibitem{Ti} J. Tits, \emph{Reductive groups over local fields}, Proc. Sympos. Pure Math., XXXIII (1979), 29--69."),
    # —— 预印本条目：补 eprint / note / 出处 ——
    (109, r"\bibitem{MVy}",
     r"\bibitem{MVy} I. Mirkovi\'c and M. Vybornov, \emph{Quiver varieties and Beilinson-Drinfeld Grassmannians of type $A$}, available at http://arxiv.org/abs/0712.4160."),
    (135, r"\bibitem{RZ}",
     r"\bibitem{RZ} Timo Richarz and Xinwen Zhu, \emph{Construction of the full Langlands dual group via the geometric Satake correspondence}, appendix to \cite{Z11}."),
    (139, r"\bibitem{Sch}",
     r"\bibitem{Sch} Peter Scholze and Jared Weinstein, \emph{$p$-adic geometry}, available at https://math.berkeley.edu/~jared/Math274/ScholzeLectures.pdf."),
    (149, r"\bibitem{St}",
     r"\bibitem{St} Stack project authors, \emph{Stack project}, available at http://stacks.math.columbia.edu (2016)."),
    (157, r"\bibitem{Yu}",
     r"\bibitem{Yu} Zhiwei Yun, \emph{Lectures on Springer theories and orbital integrals}, in \emph{These Proceedings}."),
    # —— 版次写法 ——
    (81, r"\bibitem{Kac}",
     r"\bibitem{Kac} Victor G. Kac, \emph{Infinite-dimensional Lie algebras}, 3rd ed., Cambridge University Press, Cambridge, 1990."),
]


def main():
    with io.open(CH21, encoding="utf-8") as f:
        lines = f.read().split("\n")

    bad = []
    for ln, must, new in FIXES:
        cur = lines[ln - 1]
        if must not in cur:
            bad.append("line %d: 期望含 %r，实为 %r" % (ln, must, cur[:80]))
        if cur.strip() == new.strip():
            bad.append("line %d: 已是目标内容" % ln)
    if bad:
        sys.stderr.write("未写入，先修正：\n" + "\n".join(bad) + "\n")
        return 1

    for ln, must, new in FIXES:
        lines[ln - 1] = new

    with io.open(CH21, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    sys.stdout.write("fixed %d entries in %s\n" % (len(FIXES), CH21))
    return 0


if __name__ == "__main__":
    sys.exit(main())
