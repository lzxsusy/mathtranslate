# SYZ 猜想：综述与讲义资料包

<!-- TRANSLATION-STANDARD:v2.0.1 -->
## 施工标准（必读，每次按此执行）

本项目（含后续补译、校订、译注重写）一律按《数学文献翻译纪律》**v2.0** 执行——**它是硬标准，不是参考资料**：

1. **先通读后落笔**（§1.0）：译前先通读全文并产出《通读笔记》《疑点清单》，疑点清单「未解」= 0 才准译第一句。
2. **译注必须有可追溯来源**（§2.5）：先查本库既有译法（corpus / 既往术语表），再查 nLab / Stacks Project / EMS / DLMF 交叉验证，最后落到 A 级原始文献；每条解释性译注带 `[来源：…]` 或 `[译者按（无外部依据）]`，禁止编造来源。
3. **来源黑名单与语料卫生**（§2.5.9）：知乎、百度百科/知道、CSDN、简书、公众号、博客、视频课笔记等一律不看、不引、不缓存；语料使用口径以 DATASHEET 与 LICENSE 为准：译文与语料是第三方底本的演绎作品，本库不代原作者授权、也不另设限制（检索、研究、教学、训练均可），权利人通知即撤；自产元数据、术语、工程文档与工作流为 CC BY 4.0。

全文：《数学文献翻译纪律》v2.0 —— `playbook/01_数学文献翻译纪律.md`（开发仓）· `04_playbook/01_数学文献翻译纪律.md`（发布仓）· https://atomgit.com/lzxSUSUY/mathtranslate/blob/main/04_playbook/01_数学文献翻译纪律.md ｜文件库总入口：`playbook/README.md`

下载时间：2026-11-04　|　文件数：13　|　合计约 4.1 MB

SYZ 猜想（Strominger–Yau–Zaslow conjecture, 1996）：镜像对称的 Calabi–Yau 流形 $X,\check X$ 之间，
在**大复结构极限**附近，应存在由**特殊拉格朗日子流形**构成的**仿射环面纤维化** $X\to B$、$\check X\to B$，
且互为对偶（T-对偶）。它把"镜像"从同调/量子上同调的对应，还原成一个可几何化的图景。
以下按"先易后难、先综述后专题"排序。

---

## 目录结构

```
SYZ-conjecture/
├─ 01_surveys/         综述（6 篇，按推荐阅读顺序排列）
├─ 02_lecture-notes/   讲义（MIT 18.969 的 SYZ 五讲 + 入门速览）
├─ 03_original-paper/  原始论文（SYZ 1996）
└─ README.md
```

## 一、综述（01_surveys）

| 顺序 | 文件 | 作者 / 年 | 页数 | 说明 |
|---|---|---|---|---|
| ① | `Chan-2014_SYZ-conjecture-and-its-impact_arXiv1408.6062.pdf` | Kwokwai Chan, 2014 | 22 | **入门首选**。从 SYZ 1996 之后的完整脉络讲起：拓扑 T-对偶、特殊拉格朗日纤维化、到镜像对称几何的现代理解。篇幅短、框架清楚。 |
| ② | `Glimpse-of-the-SYZ-conjecture-and-related-developments_ICCM2016.pdf` | Kwokwai Chan, 2016 | 22 | ICCM 2016 会议报告。开头用"SYZ 之前的镜像对称"作铺垫，适合打通前史再进入 SYZ 主线，可与 ① 对照读。 |
| ③ | `Gross-2008_SYZ-conjecture_torus-fibrations-to-degenerations_arXiv0802.3407.pdf` | Mark Gross, 2008 | 44 | 经典综述。从环面纤维化讲到**退化（degenerations）与对数结构**，即 Gross–Siebert 纲领的起点。 |
| ④ | `Gross-2013_Mirror-symmetry-and-SYZ-conjecture_arXiv1212.4220.pdf` | Mark Gross, 2013 | 68 | **核心综述**：③ 的全面升级版（Current Developments in Mathematics 2012），把 2008–2013 的进展纳入同一叙事，篇幅最长、最系统。若只读一篇大综述，读这篇。 |
| ⑤ | `YangLi-2022_Survey-metric-SYZ-conjecture-non-archimedean-geometry_arXiv2204.11363.pdf` | Yang Li, 2022 | 48 | **现代前沿（度量侧）**。讲大复结构极限下特殊拉格朗日纤维化的度量存在性，核心工具是**多复变势理论 + 非阿基米德几何**，附开放问题清单。想碰研究前沿就读它。 |
| ⑥ | `Collins-Lin-2022_Recent-progress-SYZ-noncompact-CY-surfaces_arXiv2208.14485.pdf` | T. C. Collins, Yu-Shen Lin, 2022 | 29 | **专题综述**：非紧 Calabi–Yau 曲面（有理椭圆曲面、del Pezzo 曲面）上的 SYZ 镜像对称，及其对 $ALH^*$ 引力瞬子分类的应用（与 Hein–Sun–Viaclovsky–Zhang 的结果呼应）。 |

## 二、讲义（02_lecture-notes）

**MIT 18.969 Topics in Geometry: Mirror Symmetry（Denis Auroux, 2009 春）—— SYZ 专题五讲**，笔记由 Kartik Venkatram 整理，取自 MIT OpenCourseWare（CC BY-NC-SA）：

| 文件 | 讲次 | 页数 | 内容 |
|---|---|---|---|
| `MIT18.969-Auroux_Lec20_HMS-elliptic-curve-motivation-for-SYZ.pdf` | Lec 20 | 4 | 椭圆曲线的同调镜像对称、Massey 积 → 引出 SYZ 猜想 |
| `MIT18.969-Auroux_Lec21_The-SYZ-conjecture-special-Lagrangians.pdf` | Lec 21 | 4 | SYZ 猜想本体；特殊拉格朗日子流形及其形变 |
| `MIT18.969-Auroux_Lec22_Moduli-of-special-Lagrangians-affine-structures.pdf` | Lec 22 | 5 | 特殊拉格朗日模空间、仿射结构；镜像的复结构与 Kähler 形式 |
| `MIT18.969-Auroux_Lec23_SYZ-continued-elliptic-curves-K3.pdf` | Lec 23 | 3 | SYZ 续讲；椭圆曲线与 K3 两个可算的例子 |
| `MIT18.969-Auroux_Lec24_SYZ-from-toric-degenerations-LG-models.pdf` | Lec 24 | 4 | 从环面退化看 SYZ（K3 情形）；Landau–Ginzburg 模型、超势 |

> 这套讲义的价值在于"**能算**"：先看综述建立图景，再用这五讲把椭圆曲线、K3 的纤维化与对偶亲手过一遍。
> 完整课程（Lec 1–25）在 MIT OCW 可免费获取，如需要可再补全。

另附：`Brief-introduction-to-the-SYZ-conjecture_slides.pdf`（Ju Tan，6 页）—— 网络上的极简速览笔记（非正式出版，适合 10 分钟建立直觉，严谨性以正式综述为准）。

## 三、原始论文（03_original-paper）

`SYZ-1996_Mirror-symmetry-is-T-duality_hep-th-9606040.pdf` — A. Strominger, S.-T. Yau, E. Zaslow, *Mirror Symmetry is T-Duality*, Nucl. Phys. B479 (1996) 243–259，21 页。（arXiv: hep-th/9606040）

建议在读综述 ① 之后回头读原文：篇幅短，但"镜像 = T-对偶"的原始论证很值得看一遍。

---

## 推荐阅读路线

1. **建立直觉**（约 1 天）：Ju Tan 6 页速览 → Chan 2014（①）。
2. **补前史与全局**（约 2–3 天）：Chan 2016（②）→ Gross 2008（③）。
3. **系统化**（约 1–2 周）：Gross 2013（④）精读，重点看 Gross–Siebert 退化纲领如何从 SYZ 生长出来。
4. **动手**（约 1 周）：Auroux Lec 20–24，配合椭圆曲线、K3 的例子做计算。
5. **进前沿**（按方向选读）：度量侧 → Yang Li 2022（⑤）；非紧曲面/引力瞬子 → Collins–Lin 2022（⑥）。
6. **溯源**：原始论文。

## 延伸阅读（未下载，需要可再补）

- Gross–Siebert 纲领的系统材料（log Calabi–Yau、scattering diagram、theta functions）
- Kontsevich–Soibelman 关于 SYZ 与affine结构/坍缩的系列工作
- 特殊拉格朗日几何的系统讲义（如 Joyce 的 SL 几何综述）—— ⑤ 的度量侧会直接用到
- 更偏物理的镜像对称教材（Hori 等 *Mirror Symmetry*，Clay 讲义）

## 下载来源（便于溯源与版本核对）

均取自作者主页 / arXiv / MIT OCW / 会议论文集官方存档，均为公开可获取的预印本或开放讲义：

- arXiv:0802.3407, 1212.4220, 1408.6062, 2204.11363, 2208.14485, hep-th/9606040
- ICCM 2016 存档: archive.ymsc.tsinghua.edu.cn
- MIT OCW 18.969（Spring 2009）Lecture Notes
- GitHub 用户 Ju-Tan/Slide（速览笔记）

> 说明：检索时也见到若干中文"专著/讲义"类的自出版 PDF（如 zenodo 上的若干条目），来源与同行评议状态无法核实，未纳入本资料包。
