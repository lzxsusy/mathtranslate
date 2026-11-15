# 拉取本工程到发布仓 08_source_code/SY08-02_凝聚层的导出范畴
import io, os, shutil

SRC = r'<HOME>\Downloads\orlov_derived_work'
DST = r'<HOME>\Desktop\数译发布\gitee_shuyi\08_source_code\SY08-02_凝聚层的导出范畴'
META = r'<HOME>\Desktop\数译发布\gitee_shuyi\03_translations_meta\SY08-02'

def ensure(p):
    os.makedirs(p, exist_ok=True)

def copy_file(a, b):
    ensure(os.path.dirname(b))
    shutil.copy2(a, b)

def copy_tree(a, b, exts=None, skip_prefix=()):
    for root, dirs, files in os.walk(a):
        for f in files:
            if exts and not f.lower().endswith(exts):
                continue
            if f.startswith(skip_prefix):
                continue
            p = os.path.join(root, f)
            rel = os.path.relpath(p, a)
            copy_file(p, os.path.join(b, rel))

if os.path.isdir(DST):
    shutil.rmtree(DST)
ensure(DST)

# 源码
S = os.path.join(DST, '源码')
copy_file(os.path.join(SRC, 'src', 'main.tex'), os.path.join(S, 'main.tex'))
copy_file(os.path.join(SRC, 'src', 'preamble.tex'), os.path.join(S, 'preamble.tex'))
copy_tree(os.path.join(SRC, 'src', 'chunks'), os.path.join(S, 'chunks'), exts=('.tex',), skip_prefix=('_',))
copy_tree(os.path.join(SRC, 'src', 'frontmatter'), os.path.join(S, 'frontmatter'), exts=('.tex',))
ensure(os.path.join(S, 'figures'))
io.open(os.path.join(S, 'figures', 'README.txt'), 'w', encoding='utf-8').write(
    '本译本的全部交换图均在源码内用 TikZ（\\diag / tikzcd）重排，无外部图文件。\n')

# 工程文件
G = os.path.join(DST, '工程文件')
copy_file(os.path.join(SRC, '工程文件', 'STYLE_GUIDE.md'), os.path.join(G, 'STYLE_GUIDE.md'))
copy_file(os.path.join(SRC, '工程文件', 'BRIEF.md'), os.path.join(G, 'BRIEF.md'))
copy_file(os.path.join(SRC, '工程文件', 'build.ps1'), os.path.join(G, 'build.ps1'))
copy_file(os.path.join(SRC, '工程文件', 'deliverable', 'README.md'), os.path.join(G, 'README.md'))
copy_tree(os.path.join(SRC, '工程文件', 'deliverable'), os.path.join(G, 'deliverable'))
# 工作记录
W = os.path.join(G, 'work')
copy_file(os.path.join(SRC, 'work', '通读笔记.md'), os.path.join(W, '通读笔记.md'))
copy_file(os.path.join(SRC, 'work', '疑点清单.tsv'), os.path.join(W, '疑点清单.tsv'))
copy_file(os.path.join(SRC, 'work', 'glossary.tsv'), os.path.join(W, 'glossary.tsv'))
copy_file(os.path.join(SRC, 'work', 'chunks.tsv'), os.path.join(W, 'chunks.tsv'))
copy_tree(os.path.join(SRC, 'work', 'reports'), os.path.join(W, 'reports'), exts=('.md',))
copy_tree(os.path.join(SRC, 'work', 'proposals'), os.path.join(W, 'proposals'), exts=('.tsv',))
copy_tree(os.path.join(SRC, 'tools'), os.path.join(W, 'tools'), exts=('.py',), skip_prefix=('_',))

# 成品
copy_file(os.path.join(SRC, '成品', '凝聚层的导出范畴_中文译注本.pdf'),
          os.path.join(DST, '成品', '凝聚层的导出范畴_中文译注本.pdf'))
# 投稿信息
copy_file(os.path.join(SRC, '工程文件', 'deliverable', '投稿信息.md'), os.path.join(DST, '投稿信息.md'))
ensure(META)
copy_file(os.path.join(SRC, '工程文件', 'deliverable', '投稿信息.md'), os.path.join(META, '投稿信息.md'))

n = sum(len(f) for _, _, f in os.walk(DST))
sz = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(DST) for f in fs)
print('files', n, 'MB', round(sz / 1048576, 2))
