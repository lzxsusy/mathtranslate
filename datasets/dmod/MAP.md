# dmod 卡片依赖图（MAP）

边 = `related`（A → B 读作「A 的卡引用 B」）；只画同轨或相邻轨的边，避免线团。

```mermaid
graph LR
  artin-rees-lemma[artin-rees-lemma] --> krull-dimension-and-multiplicity[krull-dimension-and-multiplicity]
  artin-rees-lemma[artin-rees-lemma] --> good-filtration[good-filtration]
  artin-rees-lemma[artin-rees-lemma] --> dimension-theory-of-filtered-modules[dimension-theory-of-filtered-modules]
  associated-graded-ring[associated-graded-ring] --> good-filtration[good-filtration]
  associated-graded-ring[associated-graded-ring] --> hilbert-polynomial[hilbert-polynomial]
  base-change-for-d-modules[base-change-for-d-modules] --> kashiwara-base-change[kashiwara-base-change]
  base-change-for-d-modules[base-change-for-d-modules] --> non-characteristic-restriction[non-characteristic-restriction]
  base-change-for-d-modules[base-change-for-d-modules] --> local-cohomology-d-module[local-cohomology-d-module]
  bernstein-dimension-bound[bernstein-dimension-bound] --> bernstein-inequality[bernstein-inequality]
  bernstein-dimension-bound[bernstein-dimension-bound] --> holonomic-defect[holonomic-defect]
  bernstein-dimension-bound[bernstein-dimension-bound] --> kashiwara-theorem[kashiwara-theorem]
  bernstein-dimension[bernstein-dimension] --> characteristic-variety[characteristic-variety]
  bernstein-dimension[bernstein-dimension] --> holonomic-module[holonomic-module]
  bernstein-dimension[bernstein-dimension] --> characteristic-ideal[characteristic-ideal]
  bernstein-inequality[bernstein-inequality] --> holonomic-defect[holonomic-defect]
  bernstein-inequality[bernstein-inequality] --> bernstein-dimension-bound[bernstein-dimension-bound]
  bernstein-inequality[bernstein-inequality] --> kashiwara-theorem[kashiwara-theorem]
  bimodule-dx-to-y[bimodule-dx-to-y] --> relative-differential-operators[relative-differential-operators]
  bimodule-dx-to-y[bimodule-dx-to-y] --> inverse-image-functor[inverse-image-functor]
  bimodule-dx-to-y[bimodule-dx-to-y] --> direct-image-functor[direct-image-functor]
  characteristic-ideal[characteristic-ideal] --> characteristic-variety[characteristic-variety]
  characteristic-ideal[characteristic-ideal] --> bernstein-dimension[bernstein-dimension]
  characteristic-ideal[characteristic-ideal] --> holonomic-module[holonomic-module]
  characteristic-ideal[characteristic-ideal] --> weyl-algebra[weyl-algebra]
  characteristic-variety-sheaf[characteristic-variety-sheaf] --> coherent-d-module[coherent-d-module]
  characteristic-variety-sheaf[characteristic-variety-sheaf] --> support-and-irreducibility[support-and-irreducibility]
  characteristic-variety-sheaf[characteristic-variety-sheaf] --> graded-dz-on-smooth[graded-dz-on-smooth]
  characteristic-variety-sheaf[characteristic-variety-sheaf] --> characteristic-variety[characteristic-variety]
  characteristic-variety[characteristic-variety] --> characteristic-ideal[characteristic-ideal]
  characteristic-variety[characteristic-variety] --> bernstein-dimension[bernstein-dimension]
  characteristic-variety[characteristic-variety] --> holonomic-module[holonomic-module]
  characteristic-variety[characteristic-variety] --> singular-support[singular-support]
  characteristic-variety[characteristic-variety] --> characteristic-variety-sheaf[characteristic-variety-sheaf]
  coherator[coherator] --> coherent-d-module[coherent-d-module]
  coherator[coherator] --> quasi-coherent-d-module[quasi-coherent-d-module]
  coherent-d-module[coherent-d-module] --> quasi-coherent-d-module[quasi-coherent-d-module]
  coherent-d-module[coherent-d-module] --> characteristic-variety-sheaf[characteristic-variety-sheaf]
  coherent-d-module[coherent-d-module] --> coherator[coherator]
  cohomological-dimension-of-i-plus[cohomological-dimension-of-i-plus] --> inverse-image-functor[inverse-image-functor]
  cohomological-dimension-of-i-plus[cohomological-dimension-of-i-plus] --> derived-inverse-image[derived-inverse-image]
  d-module-on-affine-line[d-module-on-affine-line] --> irreducible-holonomic-classification[irreducible-holonomic-classification]
  d-module-on-affine-line[d-module-on-affine-line] --> flat-connection[flat-connection]
  d-module-on-affine-line[d-module-on-affine-line] --> deligne-regular-singular[deligne-regular-singular]
  d-module-on-affine-line[d-module-on-affine-line] --> example-euler-operator-on-a1[example-euler-operator-on-a1]
  d-module-on-projective-space[d-module-on-projective-space] --> quasi-coherent-d-module[quasi-coherent-d-module]
  d-module-on-projective-space[d-module-on-projective-space] --> coherent-d-module[coherent-d-module]
  d-module-on-projective-space[d-module-on-projective-space] --> coherator[coherator]
  deligne-regular-singular[deligne-regular-singular] --> riemann-hilbert-correspondence[riemann-hilbert-correspondence]
  deligne-regular-singular[deligne-regular-singular] --> local-system[local-system]
  deligne-regular-singular[deligne-regular-singular] --> d-module-on-affine-line[d-module-on-affine-line]
  derived-inverse-image[derived-inverse-image] --> inverse-image-functor[inverse-image-functor]
  derived-inverse-image[derived-inverse-image] --> six-operations[six-operations]
  derived-inverse-image[derived-inverse-image] --> cohomological-dimension-of-i-plus[cohomological-dimension-of-i-plus]
  dimension-theory-of-filtered-modules[dimension-theory-of-filtered-modules] --> good-filtration[good-filtration]
  dimension-theory-of-filtered-modules[dimension-theory-of-filtered-modules] --> associated-graded-ring[associated-graded-ring]
  direct-image-functor[direct-image-functor] --> bimodule-dx-to-y[bimodule-dx-to-y]
  direct-image-functor[direct-image-functor] --> projection-formula[projection-formula]
  direct-image-functor[direct-image-functor] --> direct-image-of-immersion[direct-image-of-immersion]
  direct-image-of-immersion[direct-image-of-immersion] --> direct-image-functor[direct-image-functor]
  direct-image-of-immersion[direct-image-of-immersion] --> standard-filtration-of-dx-to-y[standard-filtration-of-dx-to-y]
  dz-structure-sheaf[dz-structure-sheaf] --> smooth-point[smooth-point]
  dz-structure-sheaf[dz-structure-sheaf] --> relative-differential-operators[relative-differential-operators]
  dz-structure-sheaf[dz-structure-sheaf] --> module-over-algebraic-variety[module-over-algebraic-variety]
  external-tensor-product[external-tensor-product] --> direct-image-of-immersion[direct-image-of-immersion]
  finite-length-of-holonomic[finite-length-of-holonomic] --> holonomic-module[holonomic-module]
  finite-length-of-holonomic[finite-length-of-holonomic] --> bernstein-dimension[bernstein-dimension]
  finite-length-of-holonomic[finite-length-of-holonomic] --> characteristic-variety[characteristic-variety]
  finite-length-of-holonomic[finite-length-of-holonomic] --> kashiwara-theorem-statement[kashiwara-theorem-statement]
  finite-length-sheaf[finite-length-sheaf] --> coherent-d-module[coherent-d-module]
  finite-length-sheaf[finite-length-sheaf] --> support-and-irreducibility[support-and-irreducibility]
  flat-connection[flat-connection] --> local-system[local-system]
  flat-connection[flat-connection] --> riemann-hilbert-correspondence[riemann-hilbert-correspondence]
  flat-connection[flat-connection] --> d-module-on-affine-line[d-module-on-affine-line]
  good-filtration[good-filtration] --> associated-graded-ring[associated-graded-ring]
  good-filtration[good-filtration] --> dimension-theory-of-filtered-modules[dimension-theory-of-filtered-modules]
  good-filtration[good-filtration] --> artin-rees-lemma[artin-rees-lemma]
  graded-dz-on-smooth[graded-dz-on-smooth] --> dz-structure-sheaf[dz-structure-sheaf]
  graded-dz-on-smooth[graded-dz-on-smooth] --> smooth-point[smooth-point]
  graded-dz-on-smooth[graded-dz-on-smooth] --> characteristic-variety-sheaf[characteristic-variety-sheaf]
  grobner-basis-symbol[grobner-basis-symbol] --> symbol-and-principal-symbol[symbol-and-principal-symbol]
  grobner-basis-symbol[grobner-basis-symbol] --> characteristic-variety[characteristic-variety]
  grobner-basis-symbol[grobner-basis-symbol] --> order-filtration-of-dn[order-filtration-of-dn]
  grobner-basis-symbol[grobner-basis-symbol] --> holonomic-module[holonomic-module]
  hilbert-polynomial[hilbert-polynomial] --> krull-dimension-and-multiplicity[krull-dimension-and-multiplicity]
  hilbert-polynomial[hilbert-polynomial] --> associated-graded-ring[associated-graded-ring]
  hilbert-polynomial[hilbert-polynomial] --> dimension-theory-of-filtered-modules[dimension-theory-of-filtered-modules]
  holonomic-defect[holonomic-defect] --> bernstein-inequality[bernstein-inequality]
  holonomic-defect[holonomic-defect] --> kashiwara-theorem[kashiwara-theorem]
  holonomic-defect[holonomic-defect] --> holonomicity-preserved-by-direct-image[holonomicity-preserved-by-direct-image]
  holonomic-module[holonomic-module] --> characteristic-variety[characteristic-variety]
  holonomic-module[holonomic-module] --> bernstein-dimension[bernstein-dimension]
  holonomic-module[holonomic-module] --> finite-length-of-holonomic[finite-length-of-holonomic]
  holonomic-module[holonomic-module] --> holonomicity-under-tensor[holonomicity-under-tensor]
  holonomic-module[holonomic-module] --> kashiwara-theorem-statement[kashiwara-theorem-statement]
  holonomic-module[holonomic-module] --> preservation-of-holonomicity[preservation-of-holonomicity]
  holonomicity-preserved-by-direct-image[holonomicity-preserved-by-direct-image] --> kashiwara-theorem[kashiwara-theorem]
  holonomicity-preserved-by-direct-image[holonomicity-preserved-by-direct-image] --> local-cohomology-d-module[local-cohomology-d-module]
  holonomicity-preserved-by-direct-image[holonomicity-preserved-by-direct-image] --> bernstein-inequality[bernstein-inequality]
  holonomicity-under-tensor[holonomicity-under-tensor] --> holonomic-module[holonomic-module]
  holonomicity-under-tensor[holonomicity-under-tensor] --> characteristic-variety[characteristic-variety]
  holonomicity-under-tensor[holonomicity-under-tensor] --> bernstein-dimension[bernstein-dimension]
  holonomicity-under-tensor[holonomicity-under-tensor] --> preservation-of-holonomicity[preservation-of-holonomicity]
  inverse-image-functor[inverse-image-functor] --> bimodule-dx-to-y[bimodule-dx-to-y]
  inverse-image-functor[inverse-image-functor] --> derived-inverse-image[derived-inverse-image]
  inverse-image-functor[inverse-image-functor] --> cohomological-dimension-of-i-plus[cohomological-dimension-of-i-plus]
  irreducible-holonomic-classification[irreducible-holonomic-classification] --> d-module-on-affine-line[d-module-on-affine-line]
  irreducible-holonomic-classification[irreducible-holonomic-classification] --> riemann-hilbert-correspondence[riemann-hilbert-correspondence]
  kashiwara-base-change[kashiwara-base-change] --> base-change-for-d-modules[base-change-for-d-modules]
  kashiwara-base-change[kashiwara-base-change] --> kashiwara-theorem[kashiwara-theorem]
  kashiwara-base-change[kashiwara-base-change] --> local-cohomology-d-module[local-cohomology-d-module]
  kashiwara-theorem-statement[kashiwara-theorem-statement] --> holonomic-module[holonomic-module]
  kashiwara-theorem-statement[kashiwara-theorem-statement] --> preservation-of-holonomicity[preservation-of-holonomicity]
  kashiwara-theorem-statement[kashiwara-theorem-statement] --> finite-length-of-holonomic[finite-length-of-holonomic]
  kashiwara-theorem[kashiwara-theorem] --> holonomic-defect[holonomic-defect]
  kashiwara-theorem[kashiwara-theorem] --> local-cohomology-d-module[local-cohomology-d-module]
  kashiwara-theorem[kashiwara-theorem] --> support-localization[support-localization]
  krull-dimension-and-multiplicity[krull-dimension-and-multiplicity] --> hilbert-polynomial[hilbert-polynomial]
  krull-dimension-and-multiplicity[krull-dimension-and-multiplicity] --> artin-rees-lemma[artin-rees-lemma]
  krull-dimension-and-multiplicity[krull-dimension-and-multiplicity] --> associated-graded-ring[associated-graded-ring]
  krull-dimension-and-multiplicity[krull-dimension-and-multiplicity] --> good-filtration[good-filtration]
  local-cohomology-d-module[local-cohomology-d-module] --> support-localization[support-localization]
  local-cohomology-d-module[local-cohomology-d-module] --> kashiwara-theorem[kashiwara-theorem]
  local-cohomology-d-module[local-cohomology-d-module] --> kashiwara-base-change[kashiwara-base-change]
  local-system[local-system] --> flat-connection[flat-connection]
  local-system[local-system] --> riemann-hilbert-correspondence[riemann-hilbert-correspondence]
  local-system[local-system] --> deligne-regular-singular[deligne-regular-singular]
  module-over-algebraic-variety[module-over-algebraic-variety] --> quasi-coherent-d-module[quasi-coherent-d-module]
  module-over-algebraic-variety[module-over-algebraic-variety] --> dz-structure-sheaf[dz-structure-sheaf]
  noetherianity-of-dn[noetherianity-of-dn] --> weyl-algebra[weyl-algebra]
  noetherianity-of-dn[noetherianity-of-dn] --> order-filtration-of-dn[order-filtration-of-dn]
  noetherianity-of-dn[noetherianity-of-dn] --> holonomic-module[holonomic-module]
  non-characteristic-restriction[non-characteristic-restriction] --> holonomicity-preserved-by-direct-image[holonomicity-preserved-by-direct-image]
  non-characteristic-restriction[non-characteristic-restriction] --> base-change-for-d-modules[base-change-for-d-modules]
  non-characteristic-restriction[non-characteristic-restriction] --> kashiwara-theorem[kashiwara-theorem]
  order-filtration-of-dn[order-filtration-of-dn] --> weyl-algebra[weyl-algebra]
  order-filtration-of-dn[order-filtration-of-dn] --> symbol-and-principal-symbol[symbol-and-principal-symbol]
  order-filtration-of-dn[order-filtration-of-dn] --> grobner-basis-symbol[grobner-basis-symbol]
  preservation-of-holonomicity[preservation-of-holonomicity] --> holonomic-module[holonomic-module]
  preservation-of-holonomicity[preservation-of-holonomicity] --> kashiwara-theorem-statement[kashiwara-theorem-statement]
  preservation-of-holonomicity[preservation-of-holonomicity] --> holonomicity-under-tensor[holonomicity-under-tensor]
  preservation-of-holonomicity[preservation-of-holonomicity] --> finite-length-of-holonomic[finite-length-of-holonomic]
  projection-formula[projection-formula] --> direct-image-functor[direct-image-functor]
  projection-formula[projection-formula] --> six-operations[six-operations]
  projection-formula[projection-formula] --> derived-inverse-image[derived-inverse-image]
  quasi-coherent-d-module[quasi-coherent-d-module] --> coherent-d-module[coherent-d-module]
  quasi-coherent-d-module[quasi-coherent-d-module] --> module-over-algebraic-variety[module-over-algebraic-variety]
  relative-differential-operators[relative-differential-operators] --> dz-structure-sheaf[dz-structure-sheaf]
  relative-differential-operators[relative-differential-operators] --> module-over-algebraic-variety[module-over-algebraic-variety]
  riemann-hilbert-correspondence[riemann-hilbert-correspondence] --> flat-connection[flat-connection]
  riemann-hilbert-correspondence[riemann-hilbert-correspondence] --> local-system[local-system]
  riemann-hilbert-correspondence[riemann-hilbert-correspondence] --> deligne-regular-singular[deligne-regular-singular]
  riemann-hilbert-correspondence[riemann-hilbert-correspondence] --> irreducible-holonomic-classification[irreducible-holonomic-classification]
  ring-of-differential-operators-polynomial[ring-of-differential-operators-polynomial] --> weyl-algebra[weyl-algebra]
  ring-of-differential-operators-polynomial[ring-of-differential-operators-polynomial] --> order-filtration-of-dn[order-filtration-of-dn]
  ring-of-differential-operators-polynomial[ring-of-differential-operators-polynomial] --> symbol-and-principal-symbol[symbol-and-principal-symbol]
  singular-support[singular-support] --> characteristic-variety[characteristic-variety]
  singular-support[singular-support] --> characteristic-ideal[characteristic-ideal]
  singular-support[singular-support] --> holonomic-module[holonomic-module]
  six-operations[six-operations] --> direct-image-functor[direct-image-functor]
  six-operations[six-operations] --> inverse-image-functor[inverse-image-functor]
  six-operations[six-operations] --> projection-formula[projection-formula]
  smooth-point[smooth-point] --> graded-dz-on-smooth[graded-dz-on-smooth]
  smooth-point[smooth-point] --> dz-structure-sheaf[dz-structure-sheaf]
  standard-filtration-of-dx-to-y[standard-filtration-of-dx-to-y] --> bimodule-dx-to-y[bimodule-dx-to-y]
  standard-filtration-of-dx-to-y[standard-filtration-of-dx-to-y] --> direct-image-of-immersion[direct-image-of-immersion]
  support-and-irreducibility[support-and-irreducibility] --> coherent-d-module[coherent-d-module]
  support-and-irreducibility[support-and-irreducibility] --> finite-length-sheaf[finite-length-sheaf]
  support-and-irreducibility[support-and-irreducibility] --> characteristic-variety-sheaf[characteristic-variety-sheaf]
  support-localization[support-localization] --> local-cohomology-d-module[local-cohomology-d-module]
  support-localization[support-localization] --> kashiwara-theorem[kashiwara-theorem]
  support-localization[support-localization] --> base-change-for-d-modules[base-change-for-d-modules]
  symbol-and-principal-symbol[symbol-and-principal-symbol] --> order-filtration-of-dn[order-filtration-of-dn]
  symbol-and-principal-symbol[symbol-and-principal-symbol] --> grobner-basis-symbol[grobner-basis-symbol]
  symbol-and-principal-symbol[symbol-and-principal-symbol] --> characteristic-variety[characteristic-variety]
  weyl-algebra[weyl-algebra] --> ring-of-differential-operators-polynomial[ring-of-differential-operators-polynomial]
  weyl-algebra[weyl-algebra] --> order-filtration-of-dn[order-filtration-of-dn]
  weyl-algebra[weyl-algebra] --> symbol-and-principal-symbol[symbol-and-principal-symbol]
  weyl-algebra[weyl-algebra] --> noetherianity-of-dn[noetherianity-of-dn]
  example-d-module-on-projective-space[example-d-module-on-projective-space] --> d-module-on-affine-line[d-module-on-affine-line]
  example-d-module-on-projective-space[example-d-module-on-projective-space] --> flat-connection[flat-connection]
  example-d-module-on-projective-space[example-d-module-on-projective-space] --> example-euler-operator-on-a1[example-euler-operator-on-a1]
  example-euler-operator-on-a1[example-euler-operator-on-a1] --> d-module-on-affine-line[d-module-on-affine-line]
  example-euler-operator-on-a1[example-euler-operator-on-a1] --> irreducible-holonomic-classification[irreducible-holonomic-classification]
  example-euler-operator-on-a1[example-euler-operator-on-a1] --> example-d-module-on-projective-space[example-d-module-on-projective-space]
```

## 全图（含跨轨）

| 卡 | 指向 |
| --- | --- |
| `artin-rees-lemma` | krull-dimension-and-multiplicity、good-filtration、dimension-theory-of-filtered-modules |
| `associated-graded-ring` | good-filtration、symbol-and-principal-symbol、hilbert-polynomial、noetherianity-of-dn |
| `base-change-for-d-modules` | kashiwara-base-change、non-characteristic-restriction、local-cohomology-d-module |
| `bernstein-dimension-bound` | bernstein-inequality、holonomic-defect、kashiwara-theorem、bernstein-dimension |
| `bernstein-dimension` | characteristic-variety、holonomic-module、bernstein-inequality、characteristic-ideal、bernstein-dimension-bound |
| `bernstein-inequality` | holonomic-defect、bernstein-dimension-bound、kashiwara-theorem |
| `bimodule-dx-to-y` | relative-differential-operators、inverse-image-functor、direct-image-functor |
| `characteristic-ideal` | characteristic-variety、bernstein-dimension、holonomic-module、weyl-algebra |
| `characteristic-variety-sheaf` | coherent-d-module、support-and-irreducibility、graded-dz-on-smooth、characteristic-variety |
| `characteristic-variety` | characteristic-ideal、bernstein-dimension、holonomic-module、singular-support、characteristic-variety-sheaf |
| `coherator` | coherent-d-module、quasi-coherent-d-module |
| `coherent-d-module` | quasi-coherent-d-module、characteristic-variety-sheaf、coherator |
| `cohomological-dimension-of-i-plus` | inverse-image-functor、derived-inverse-image |
| `d-module-on-affine-line` | irreducible-holonomic-classification、flat-connection、deligne-regular-singular、example-euler-operator-on-a1 |
| `d-module-on-projective-space` | quasi-coherent-d-module、coherent-d-module、coherator、example-d-module-on-projective-space |
| `deligne-regular-singular` | riemann-hilbert-correspondence、local-system、d-module-on-affine-line |
| `derived-inverse-image` | inverse-image-functor、six-operations、cohomological-dimension-of-i-plus |
| `dimension-theory-of-filtered-modules` | good-filtration、associated-graded-ring、noetherianity-of-dn、holonomic-module |
| `direct-image-functor` | bimodule-dx-to-y、projection-formula、direct-image-of-immersion |
| `direct-image-of-immersion` | direct-image-functor、standard-filtration-of-dx-to-y、characteristic-variety |
| `dz-structure-sheaf` | smooth-point、relative-differential-operators、module-over-algebraic-variety |
| `external-tensor-product` | good-filtration、characteristic-variety、direct-image-of-immersion |
| `finite-length-of-holonomic` | holonomic-module、bernstein-dimension、characteristic-variety、kashiwara-theorem-statement |
| `finite-length-sheaf` | coherent-d-module、support-and-irreducibility |
| `flat-connection` | local-system、riemann-hilbert-correspondence、d-module-on-affine-line |
| `good-filtration` | associated-graded-ring、dimension-theory-of-filtered-modules、artin-rees-lemma、noetherianity-of-dn |
| `graded-dz-on-smooth` | dz-structure-sheaf、smooth-point、characteristic-variety-sheaf |
| `grobner-basis-symbol` | symbol-and-principal-symbol、characteristic-variety、order-filtration-of-dn、holonomic-module |
| `hilbert-polynomial` | krull-dimension-and-multiplicity、associated-graded-ring、dimension-theory-of-filtered-modules |
| `holonomic-defect` | bernstein-inequality、kashiwara-theorem、holonomicity-preserved-by-direct-image |
| `holonomic-module` | characteristic-variety、bernstein-dimension、finite-length-of-holonomic、holonomicity-under-tensor、kashiwara-theorem-statement、preservation-of-holonomicity |
| `holonomicity-preserved-by-direct-image` | kashiwara-theorem、local-cohomology-d-module、bernstein-inequality、preservation-of-holonomicity |
| `holonomicity-under-tensor` | holonomic-module、characteristic-variety、bernstein-dimension、preservation-of-holonomicity |
| `inverse-image-functor` | bimodule-dx-to-y、derived-inverse-image、cohomological-dimension-of-i-plus |
| `irreducible-holonomic-classification` | holonomicity-preserved-by-direct-image、d-module-on-affine-line、riemann-hilbert-correspondence |
| `kashiwara-base-change` | base-change-for-d-modules、kashiwara-theorem、local-cohomology-d-module |
| `kashiwara-theorem-statement` | holonomic-module、preservation-of-holonomicity、finite-length-of-holonomic、local-cohomology-d-module、kashiwara-theorem、kashiwara-base-change |
| `kashiwara-theorem` | holonomic-defect、local-cohomology-d-module、support-localization、kashiwara-theorem-statement |
| `krull-dimension-and-multiplicity` | hilbert-polynomial、artin-rees-lemma、associated-graded-ring、good-filtration |
| `local-cohomology-d-module` | support-localization、kashiwara-theorem、kashiwara-base-change |
| `local-system` | flat-connection、riemann-hilbert-correspondence、deligne-regular-singular |
| `module-over-algebraic-variety` | quasi-coherent-d-module、dz-structure-sheaf |
| `noetherianity-of-dn` | weyl-algebra、order-filtration-of-dn、associated-graded-ring、good-filtration、holonomic-module |
| `non-characteristic-restriction` | holonomicity-preserved-by-direct-image、base-change-for-d-modules、kashiwara-theorem |
| `order-filtration-of-dn` | weyl-algebra、symbol-and-principal-symbol、associated-graded-ring、grobner-basis-symbol |
| `preservation-of-holonomicity` | holonomic-module、kashiwara-theorem-statement、holonomicity-under-tensor、finite-length-of-holonomic、holonomicity-preserved-by-direct-image |
| `projection-formula` | direct-image-functor、six-operations、derived-inverse-image |
| `quasi-coherent-d-module` | coherent-d-module、module-over-algebraic-variety |
| `relative-differential-operators` | dz-structure-sheaf、module-over-algebraic-variety |
| `riemann-hilbert-correspondence` | flat-connection、local-system、deligne-regular-singular、irreducible-holonomic-classification |
| `ring-of-differential-operators-polynomial` | weyl-algebra、order-filtration-of-dn、symbol-and-principal-symbol、associated-graded-ring |
| `singular-support` | characteristic-variety、characteristic-ideal、holonomic-module |
| `six-operations` | direct-image-functor、inverse-image-functor、projection-formula |
| `smooth-point` | graded-dz-on-smooth、dz-structure-sheaf |
| `standard-filtration-of-dx-to-y` | order-filtration-of-dn、bimodule-dx-to-y、direct-image-of-immersion |
| `support-and-irreducibility` | coherent-d-module、finite-length-sheaf、characteristic-variety-sheaf |
| `support-localization` | local-cohomology-d-module、kashiwara-theorem、base-change-for-d-modules |
| `symbol-and-principal-symbol` | order-filtration-of-dn、associated-graded-ring、grobner-basis-symbol、characteristic-variety |
| `weyl-algebra` | ring-of-differential-operators-polynomial、order-filtration-of-dn、symbol-and-principal-symbol、noetherianity-of-dn |
| `example-d-module-on-projective-space` | d-module-on-affine-line、flat-connection、holonomicity-preserved-by-direct-image、example-euler-operator-on-a1、d-module-on-projective-space |
| `example-euler-operator-on-a1` | d-module-on-affine-line、irreducible-holonomic-classification、example-d-module-on-projective-space |
