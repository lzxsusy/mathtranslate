# -*- coding: utf-8 -*-
"""把 SY05-28 登记进 RELEASE_REGISTER.csv（R5 门禁要求），并让底本 PDF 不入库。"""
import io, os, subprocess

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
os.chdir(ROOT)

ROW = ("SY05-28,曲线的镜像及其 Fukaya 范畴,"
       "08_source_code/SY05-28_曲线的镜像及其Fukaya范畴,"
       "作者手稿（会议报告手写笔记 + 报告幻灯片；未刊）,"
       "Auroux《Mirrors of curves and their Fukaya categories》（Miami 2020-01-27/29；手写笔记 17 页）+"
       "《An invitation to homological mirror symmetry》（IMSA 2019-09-06；幻灯片 14 页）,"
       "演绎作品；底本权利归原作者,中,"
       "L2 公开·受限（可撤下）,申请获取（暂无外链）,否,,L4 禁入,auto,合规,2026-11-20,"
       "底本 31 页（手写 17 + 幻灯片 14）不入库；中译注本 32 页；批注 14 条、疑点 17 条（未解 0）、"
       "术语 90 行、文献 12 条；0 error/0 Overfull；成品待上传\n")

path = 'RELEASE_REGISTER.csv'
s = io.open(path, encoding='utf-8-sig').read()
if 'SY05-28' not in s:
    if not s.endswith('\n'):
        s += '\n'
    s += ROW
    io.open(path, 'w', encoding='utf-8', newline='\n').write(s)
    print('register: appended')
else:
    print('register: already present')

# 底本 PDF 不入库（L4）
gi = '08_source_code/SY05-28_曲线的镜像及其Fukaya范畴/源码/.gitignore'
t = io.open(gi, encoding='utf-8').read()
t = t.replace('original/pages/', 'original/')
io.open(gi, 'w', encoding='utf-8', newline='\n').write(t)
print(subprocess.run(['git', 'rm', '-r', '--cached', '-q',
                      '08_source_code/SY05-28_曲线的镜像及其Fukaya范畴/源码/original'],
                     capture_output=True, text=True).stdout)
print('done')
