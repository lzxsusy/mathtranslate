# -*- coding: utf-8 -*-
"""给 08_source_code 下每个工程的 工程文件/ 生成统一的「00_开工必读.md」。

只覆盖带生成标记的文件，人工改过的（去掉标记的）不动。
"""
import os, re, sys

ROOT = r'C:\Users\admin\Desktop\数译发布\gitee_shuyi\08_source_code'
MARK = '<!-- generated-by: tools/gen_start_here.py from 04_playbook/17 -->'

TPL = """{mark}
# 开工必读 · {pid}

> 本文件是 [`04_playbook/17_仓库理念与上传规范.md`](../../../04_playbook/17_仓库理念与上传规范.md) 的摘要。
> **每次开工先读这一页**，再读本工程 `BRIEF.md` 与 `STYLE_GUIDE.md`；与全文冲突时以全文为准。

## 1. 这个仓为什么存在（60 秒版）

译本只是原料。真正的产出是**可对齐的中文数学底稿**：每一段译文能对回原文页码，每一个术语、记号
有唯一登记，每一条定理陈述都有同一句的自然语言版本与 Lean 4 版本，而且这些都由脚本检查。

目标不是「让模型做更多数学题」，而是**让模型学会把模糊的话逼成精确的话**——数学是目前反馈最干净的训练场。
所以：**页数是库存，对齐才是产能。**

## 2. 这个工程是什么

{what}

## 3. 上传什么、不传什么（三句话）

- **传**：BRIEF、STYLE_GUIDE、术语表、能独立编译的译文源、成品 PDF、资料卡五件套、登记行（`RELEASE_REGISTER.csv` + `03_translations_meta/`）。
- **传但要标状态**：草稿放 `work/` 并在 BRIEF 里写"未复核"；页面图像单页 ≤ 400 KB；> 50 MB 的文件走 Release 附件，不放进 git。
- **不传**：在版图书的全文扫描件、未脱敏会话分片、密钥/token、`__pycache__`/`*.aux`/`*.synctex.gz`、本机绝对路径、`CON` 之类设备文件。

判定口诀：**能被人复核的留下；只能被自己相信的别留；能重跑的不要存结果，存命令。**

## 4. 开工五件事

1. 读 `04_playbook/17` §1（理念）与 §4（检查清单）；
2. 读本工程 `BRIEF.md`（底本/页数/已有决定）与 `STYLE_GUIDE.md`（文体/术语/公式约定）；
3. 整书翻译读 `04_playbook/01_数学文献翻译纪律.md` v2.1 的 §0–§4；只做卡片读 `datasets/README.md` §4–§5；
4. `git status` + `python make_stats.py --check`，确认数字没漂、没有上一轮遗留；
5. 写 `work/TASK-YYYYMMDD.md`：这次改哪些文件、什么算做完、要不要更新 BRIEF 状态。

## 5. 收工五件事

跑 `make_stats.py --check`、`tools/check_numbers.py`、`tools/build_norm.py --check`（按 `17` §5 加跑对应闸门）→
更新 BRIEF 状态 → 更新 CHANGELOG → 若动了实物跑 `make_stats.py --write` → 提交（写清改了什么、为什么）。
"""


def split_id(pid):
    m = re.match(r'^([A-Z]{2}\d{2}-\d{2})_(.*)$', pid)
    return (m.group(1), m.group(2)) if m else (pid, pid)


def build_what(pid, has_brief, has_cards, n_tex):
    lines = []
    code, t = split_id(pid)
    lines.append(f'- 编号：`{code}`；题名：**《{t}》**。')
    if has_brief:
        lines.append('- 本工程有 `BRIEF.md`：底本、页数、结构页表、翻译决定都在那里，开工前必须读完。')
    else:
        lines.append('- 本工程**没有 `BRIEF.md`**：若这次要做实质工作，先补一份（模板见 `SY01-30` 或 `SY01-25`）。')
    if n_tex:
        lines.append(f'- `源码/` 下有 {n_tex} 个 `.tex`，成品与源必须同步；改动译文后重编译再提交。')
    else:
        lines.append('- `源码/` 下没有 `.tex`（可能只有成品 PDF 或尚未建源），交付时不要伪称有源码。')
    if has_cards:
        lines.append('- 本工程有 `资料卡/`：01 结果清单与 03 条款索引是对齐卡 L2 陈述层的首选来源，改定理陈述时同步改卡。')
    else:
        lines.append('- 本工程**没有 `资料卡/`**：先做五件套（00 速览/01 结果清单/02 论证地图/03 条款索引/04 术语文献勘误），再做对齐卡。')
    return '\n'.join(lines)


def main():
    made = skipped = 0
    for pid in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, pid, '工程文件')
        if not os.path.isdir(d):
            continue
        has_brief = os.path.exists(os.path.join(d, 'BRIEF.md'))
        has_cards = os.path.isdir(os.path.join(ROOT, pid, '资料卡'))
        src = os.path.join(ROOT, pid, '源码')
        n_tex = 0
        if os.path.isdir(src):
            for root, _, files in os.walk(src):
                n_tex += sum(1 for f in files if f.endswith('.tex'))
        out = os.path.join(d, '00_开工必读.md')
        if os.path.exists(out):
            old = open(out, encoding='utf-8').read()
            if old.strip() and MARK not in old:
                skipped += 1
                continue
        open(out, 'w', encoding='utf-8', newline='\n').write(
            TPL.format(mark=MARK, pid=pid, what=build_what(pid, has_brief, has_cards, n_tex)))
        made += 1
    print('written', made, 'skipped(hand-edited)', skipped)


if __name__ == '__main__':
    main()
