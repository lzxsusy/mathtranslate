import io, os
root = r"C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code\SY02-21_范畴表示论与局部几何朗兰兹导论\源码\chunks"

edits = {
    "ch08.tex": [
        # E4：M/N 互换
        (r"""\zy{原文此处把 $\sM$ 与 $\sN$ 的位置写颠倒了：按上例的样式，应为 $\pi_X^! \sM \overset{!}{\otimes} \pi_Y^! \sN$，而原文写作 $\pi_X^! \sN \overset{!}{\otimes} \pi_Y^! \sM$。本译本照原文排印，读者按此理解即可。}""",
         r"""\zy{[译者按（上下文推断，无外部依据）：原文此处把 $\sM$ 与 $\sN$ 的位置写颠倒了。按上例的样式，应为 $\pi_X^! \sM \overset{!}{\otimes} \pi_Y^! \sN$，而原文写作 $\pi_X^! \sN \overset{!}{\otimes} \pi_Y^! \sM$。本译本照原文排印，读者按此理解即可。]}"""),
        # E6：漏写花体 N
        (r"""\zy{下式第二项中的 $N$，按全式其余各项的写法应作花体的 $\sN$。原文此处漏写花体，本译本照原文排印。}""",
         r"""\zy{[译者按（上下文推断，无外部依据）：下式第二项中的 $N$，按全式其余各项的写法应作花体的 $\sN$。原文此处漏写花体，本译本照原文排印。]}"""),
    ],
    "ch11.tex": [
        # fk ⊕ fk mod 的读法
        (r"""\zy{按上面最后的计算，此行应读作 $(\fk \oplus \fk)\mod$，即 $\fk \oplus \fk$ 的模范畴；原文把它印作 $\fk \oplus \fk\mod$，本译本照原文排印。}""",
         r"""\zy{[译者按（上下文推断，无外部依据）：按上面最后的计算，此行应读作 $(\fk \oplus \fk)\mod$，即 $\fk \oplus \fk$ 的模范畴；原文把它印作 $\fk \oplus \fk\mod$，本译本照原文排印。]}"""),
    ],
    "ch16.tex": [
        # E7：G_q(F_q) 应为 F_q
        (r"""\zy{原文此处作 $\mathbb{G}_q(\Fq)$，按上下文应为 $\Fq$；本译本照原文排印。}""",
         r"""\zy{[译者按（上下文推断，无外部依据）：原文此处作 $\mathbb{G}_q(\Fq)$，按上下文应为 $\Fq$；本译本照原文排印。]}"""),
    ],
}

for name, pairs in edits.items():
    p = os.path.join(root, name)
    s = io.open(p, encoding="utf-8").read()
    for a, b in pairs:
        if a not in s:
            print("MISS", name, a[:40]); continue
        s = s.replace(a, b)
    io.open(p, "w", encoding="utf-8").write(s)
print("done")
