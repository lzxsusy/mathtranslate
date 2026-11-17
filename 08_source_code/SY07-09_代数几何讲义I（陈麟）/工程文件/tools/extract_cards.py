# -*- coding: utf-8 -*-
"""从译注本 sec*.tex 抽出定义/定理类条目（带节/小节/原书页），生成 cards.json。"""
import glob, io, json, os, re

SRC = r"C:\Users\admin\Downloads\陈麟_代数几何1_译注工程\源码"
OUT = r"C:\Users\admin\Downloads\陈麟_代数几何1_译注工程\资料卡"
os.makedirs(OUT, exist_ok=True)

CORE = {"definition": "定义", "theorem": "定理", "proposition": "命题", "lemma": "引理",
        "corollary": "推论", "claim": "断言", "predefinition": "预备定义", "propdef": "命题—定义"}
EXTRA = {"example": "例", "remark": "注记", "notation": "记号", "construction": "构造",
         "warning": "警告", "exercise": "习题", "question": "问题", "convention": "约定"}
TYPE_CN = dict(CORE, **EXTRA)

SEC_PAGE = {"0": 5, "1": 9, "2": 14, "3": 19, "4": 27, "5": 33, "6": 37, "7": 42, "8": 44, "9": 47, "10": 52,
            "11": 56, "12": 61, "13": 67, "14": 72, "15": 77, "16": 78, "17": 83, "18": 85, "19": 95,
            "20": 98, "21": 105, "22": 108, "23": 111, "24": 114, "25": 119, "26": 124, "27": 133,
            "28": 141, "29": 157, "30": 161, "A": 164}

files = sorted([f for f in glob.glob(os.path.join(SRC, "sec*.tex"))
                if re.search(r"sec\d\d\.tex$", f)])
files.append(os.path.join(SRC, "appendixA.tex"))


def read(p):
    return io.open(p, encoding="utf-8").read()


label_num = {}
for p in files:
    for m in re.finditer(r"\\label\{([^}]+)\}", read(p)):
        key = m.group(1)
        if ":" in key:
            label_num[key] = key.split(":", 1)[1]

REF_RE = re.compile(r"\\([cC]ref|eqref|ref|secref)\{([^}]*)\}")


def fix_refs(s):
    def rep(m):
        kind, key = m.group(1), m.group(2)
        num = label_num.get(key)
        if num is None:
            return m.group(0)
        if kind == "eqref":
            return "(" + num + ")"
        if kind in ("cref", "Cref"):
            cn = TYPE_CN.get(key.split(":", 1)[0], "")
            return (cn + " " + num) if cn else num
        if kind == "secref":
            return "第 " + num + " 节"
        return num
    return REF_RE.sub(rep, s)


def brace_block(s, i):
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


cards = []
sec_titles = {}
sec_order = []
for path in files:
    raw = read(path)
    events = []
    for m in re.finditer(r"\\section\*?\{", raw):
        t, _ = brace_block(raw, m.end() - 1)
        t = re.sub(r"\\label\{[^}]*\}", "", t).strip()
        lab = re.search(r"\\label\{sec:([^}]+)\}", raw[m.end():m.end() + 200])
        events.append((m.start(), "sec", (fix_refs(t), lab.group(1) if lab else "")))
    for m in re.finditer(r"\\subsection\*?\{", raw):
        t, _ = brace_block(raw, m.end() - 1)
        t = re.sub(r"\\label\{[^}]*\}", "", t).strip()
        events.append((m.start(), "sub", fix_refs(t)))
    for m in re.finditer(r"%[^\n]*?\bp\.(\d{3})", raw):
        events.append((m.start(), "page", int(m.group(1))))
    env_re = re.compile(r"\\begin\{(" + "|".join(TYPE_CN) + r")\}")
    for m in env_re.finditer(raw):
        events.append((m.start(), "env", m.group(1)))
    events.sort(key=lambda e: e[0])

    cur_sec_no, cur_sec_t = "", ""
    cur_sub, cur_page = "", None
    for pos, kind, val in events:
        if kind == "sec":
            cur_sec_t, cur_sec_no = val
            cur_sub = ""
            cur_page = SEC_PAGE.get(cur_sec_no, cur_page)
            if cur_sec_no not in sec_titles:
                sec_titles[cur_sec_no] = cur_sec_t
                sec_order.append(cur_sec_no)
        elif kind == "sub":
            cur_sub = val
        elif kind == "page":
            cur_page = val
        else:
            env = val
            bstart = pos + len("\\begin{%s}" % env)
            j = bstart
            while j < len(raw) and raw[j] in " \t\n":
                j += 1
            if j < len(raw) and raw[j] == "[":
                depth = 0
                while j < len(raw):
                    if raw[j] == "[":
                        depth += 1
                    elif raw[j] == "]":
                        depth -= 1
                        if depth == 0:
                            j += 1
                            break
                    j += 1
                bstart = j
            endtok = "\\end{%s}" % env
            e = raw.find(endtok, bstart)
            if e < 0:
                continue
            body = raw[bstart:e]
            lab = re.search(r"\\label\{([^}]+)\}", body)
            key = lab.group(1) if lab else ""
            num = key.split(":", 1)[1] if ":" in key else ""
            body = re.sub(r"\\label\{[^}]*\}", "", body)
            k = e + len(endtok)
            yizhu = ""
            if re.match(r"\s*\\begin\{yizhu\}", raw[k:k + 200]):
                zs = raw.find("\\begin{yizhu}", k) + len("\\begin{yizhu}")
                ze = raw.find("\\end{yizhu}", zs)
                yizhu = raw[zs:ze]
            cards.append(dict(env=env, cn=TYPE_CN[env], num=num, key=key,
                              body=fix_refs(body).strip(), yizhu=fix_refs(yizhu).strip(),
                              section=cur_sec_no, section_title=cur_sec_t,
                              subsection=cur_sub, page=cur_page))

core = [c for c in cards if c["env"] in CORE]
print("all cards:", len(cards), "core:", len(core))
print("sections:", len(sec_order), sec_order[:5], sec_order[-3:])
io.open(os.path.join(OUT, "cards.json"), "w", encoding="utf-8").write(
    json.dumps(cards, ensure_ascii=False, indent=1))
io.open(os.path.join(OUT, "sections.json"), "w", encoding="utf-8").write(
    json.dumps([{"no": n, "title": sec_titles[n]} for n in sec_order], ensure_ascii=False, indent=1))
