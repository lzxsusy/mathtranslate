# -*- coding: utf-8 -*-
"""把原文 ZhiweiYunPCMI.tex 按行号切块，落到 工程文件/work/orig/chNN.tex。
行号表见 CHUNKS；行号为源文件绝对行（含两端）。"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # 工程文件/
SRC = os.path.join(ROOT, 'work', 'src', 'ZhiweiYunPCMI.tex')
OUT = os.path.join(ROOT, 'work', 'orig')

CHUNKS = [
    ('ch00', 850, 909),    # 摘要 + Introduction §0.1 §0.2 致谢
    ('ch01', 910, 952),    # Lecture I §1.1 + §1.2 前半
    ('ch02', 953, 1008),   # §1.3 Examples
    ('ch03', 1009, 1035),  # §1.4 Geometric properties
    ('ch04', 1036, 1082),  # §1.5 前半（Springer 对应、两个定理）
    ('ch05', 1083, 1145),  # §1.5 后半（Fourier、单值、证明、A 型、次正则）
    ('ch06', 1146, 1241),  # §1.6 Comments + §1.7 Exercises
    ('ch07', 1242, 1330),  # Lecture II §2.1
    ('ch08', 1331, 1440),  # §2.2 + §2.3
    ('ch09', 1441, 1529),  # §2.4 Further examples
    ('ch10', 1530, 1654),  # §2.5 Geometric properties
    ('ch11', 1655, 1765),  # §2.6 + §2.7 + §2.8
    ('ch12', 1766, 1883),  # Lecture III §3.1 + §3.2
    ('ch13', 1884, 2020),  # §3.3 + §3.4
    ('ch14', 2021, 2173),  # §3.5 + §3.6 + §3.7
    ('ch15', 2174, 2306),  # Lecture IV §4.1 + §4.2
    ('ch16', 2307, 2401),  # §4.3 + §4.4
    ('ch17', 2402, 2444),  # §4.5 + §4.6
    ('ch18', 2445, 3279),  # 参考文献（amsrefs biblist）
]


def main():
    os.makedirs(OUT, exist_ok=True)
    with open(SRC, encoding='utf-8') as f:
        lines = f.readlines()
    for name, a, b in CHUNKS:
        body = ''.join(lines[a - 1:b])
        with open(os.path.join(OUT, name + '.tex'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(body)
        print(name, a, b, len(body.splitlines()), 'lines', len(body), 'chars')


if __name__ == '__main__':
    main()
