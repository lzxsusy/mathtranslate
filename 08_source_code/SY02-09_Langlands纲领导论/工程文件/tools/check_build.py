# -*- coding: utf-8 -*-
"""单章编译自检。

  python check_build.py 05        # 只编译 chapters/lecture05.tex
  python check_build.py 05 --keep # 保留 checks/ 中间文件

做法：读 src/main.tex 的导言区，把正文里的 \\input{chapters/...} 换成只留目标章，
生成 checks/checkNN.tex，用 xelatex 编译两遍到 checks/outNN/，然后解析日志。

输出：PASS / FAIL + 错误行 + 未定义引用 + Overfull + 缺字。
"""
import os, re, sys, subprocess, shutil

WORK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(WORK)
SRC = os.path.join(ROOT, 'src')
XELATEX = r'<本地路径>'


def build_tex(nn):
    main = open(os.path.join(SRC, 'main.tex'), encoding='utf-8').read()
    target = 'chapters/lecture%s' % nn
    if target not in main:
        raise SystemExit('main.tex 里没有 %s' % target)
    out = []
    for line in main.split('\n'):
        m = re.match(r'\s*\\input\{(chapters/[^}]+)\}', line)
        if m:
            if m.group(1) == target:
                out.append('\\input{%s}' % target)
            continue
        out.append(line)
    tex = '\n'.join(out)
    # 单章不需要目录/索引，避免空文件告警
    tex = tex.replace('\\tableofcontents', '')
    tex = tex.replace('\\printindex', '')
    os.makedirs(os.path.join(SRC, 'checks'), exist_ok=True)
    p = os.path.join(SRC, 'checks', 'check%s.tex' % nn)
    open(p, 'w', encoding='utf-8').write(tex)
    return p


def run(tex, nn):
    outdir = os.path.join(SRC, 'checks', 'out%s' % nn)
    os.makedirs(outdir, exist_ok=True)
    for i in (1, 2):
        cmd = [XELATEX, '-interaction=nonstopmode', '-halt-on-error=0',
               '-file-line-error', '-output-directory=' + outdir, tex]
        p = subprocess.run(cmd, cwd=SRC, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = p.stdout.decode('utf-8', 'replace')
        if 'Fatal error occurred' in log:
            break
    logp = os.path.join(outdir, 'check%s.log' % nn)
    return logp


def analyse(logp, nn):
    t = open(logp, encoding='utf-8', errors='replace').read()
    errs = re.findall(r'^(?:\./|.*?)([^\s:]+\.tex):(\d+): (.*)$', t, re.M)
    errs = [e for e in errs if 'check%s' % nn in e[0] or 'chapters' in e[0]]
    undef = re.findall(r"Reference `([^']+)' on page", t)
    undef2 = re.findall(r"Citation `([^']+)'", t)
    # 单章隔离编译时，跨讲引用（label 形如 L12S3O4）必然未定义，属预期，不计失败
    def cross(lbl):
        m = re.match(r'L(\d+)', lbl)
        return bool(m) and m.group(1).zfill(2) != nn
    undef_real = [u for u in sorted(set(undef)) if not cross(u)]
    undef_expected = [u for u in sorted(set(undef)) if cross(u)]
    overfull = re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\) in paragraph at lines (\d+)--(\d+)', t)
    missing = re.findall(r'Missing character: There is no (.)', t)
    overfull_any = t.count('Overfull \\hbox')
    print('--- check%s ---' % nn)
    print('errors   :', len(errs))
    for e in errs[:12]:
        print('   %s:%s %s' % e)
    print('undef ref:', len(undef_real), undef_real[:8], '(预期跨讲:', len(undef_expected), ')')
    print('undef cite:', len(undef2), sorted(set(undef2))[:8])
    print('overfull :', overfull_any, [(a, b) for a, b, c in overfull][:8])
    print('missing char:', len(missing), sorted(set(missing))[:8])
    ok = not errs and not undef_real and not undef2 and not overfull_any and not missing
    print('RESULT   :', 'PASS' if ok else 'FAIL')
    return ok


if __name__ == '__main__':
    nn = sys.argv[1].zfill(2)
    tex = build_tex(nn)
    logp = run(tex, nn)
    ok = analyse(logp, nn)
    sys.exit(0 if ok else 1)
