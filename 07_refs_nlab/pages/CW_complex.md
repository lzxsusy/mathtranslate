# CW complex

url: https://ncatlab.org/nlab/show/CW+complex
last_revised: 2026-07-29
---

#### Topology
+--{: .hide}
[[!include topology - contents]]

* table of contents

## Idea

A **CW-complex** is a [[nice topological space|nice]] [[topological space]] which is, or can be, built up inductively, by a process of [[attaching space|attaching]] [[n-disks]] $D^n$ along their [[boundary]] [[n-spheres|(n-1)-spheres]] $S^{n-1}$ for all $n \in \mathbb{N}$: a [[cell complex]] built from the basic topological cells $S^{n-1} \hookrightarrow D^n$. 

Being, therefore,  essentially combinatorial objects, CW complexes are the principal objects of interest in [[algebraic topology]]; in fact, most spaces of interest to algebraic topologists are [[homotopy equivalence|homotopy equivalent]] to CW-complexes. Notably the [[geometric realization]] of every [[simplicial set]], hence also of every [[groupoid]], [[2-groupoid]], etc., is a CW complex. 

Milnor has argued that the category of spaces which are homotopy equivalent to CW-complexes, also called [[m-cofibrant spaces]], is a [[nice category of spaces|convenient category of spaces]] for [[algebraic topology]].

Also, CW complexes are among the [[cofibrant objects]] in the [[classical model structure on topological spaces]]. 
In fact, _every_  topological space is _[[weak homotopy equivalence|weakly homotopy equivalent]]_ to a CW-complex (but need not be [[homotopy equivalence|strongly homotopy equivalent]] to one). See also at _[[CW-approximation]]_.  Since every topological space is a [[fibrant object]] in this [[model category]] structure, this means that the [[full subcategory]] of [[Top]] on the CW-complexes is a category of "homotopically very good representatives" of [[homotopy types]]. See at _[[homotopy theory]]_ and _[[homotopy hypothesis]]_ for more on this.

+-- {: .num_remark}
###### Remark
**(origin of the "CW" terminology)**

The terminology "CW-complex" goes back to [[John Henry Constantine Whitehead]] (and see the discussion in [Hatcher, "Topology of cell complexes", p. 520](#HatcherTopologyOfCellComplexes)). 

To quote from the original paper, which was "an address delivered before the Princeton Meeting of the (American Mathematical) Society on November
2, 1946", Whitehead states:

>In this presentation we abandon [[simplicial complexes]] in favor of [[cell complexes]]. This first part consists of geometrical preliminaries, including some elementary propositions concerning what we call closure finite complexes with weak topology, abbreviated to CW-complexes, ...

Thus the "CW" stands for the following two properties shared by any CW-complex:

* **C** = "closure finiteness": a [[compact subset]] of a CW-complex intersects the [[interior]] of only finitely many cells ([prop.](classical+model+structure+on+topological+spaces#CompactSubsetsAreSmallInCellComplexes)), hence in particular so does the closure of any cell.

* **W** = "weak topology": Since a CW-complex is a [[colimit]] in [[Top]] over its cells, and as such equipped with the [[final topology]] of the cell inclusion maps, a subset of a CW-complex is open or closed precisely if its restriction to (the closure of) each cell is open or closed, respectively.

(Whitehead called the [[interior]] of the [[n-disks]] the "cells", so that their closure of each cell is the corresponding $n$-disk.)

+-- {: .num_defn #SingleCellAttachment}
###### Definition
**(single cell attachment)**

For $X$ any [[topological space]] and for $n \in \mathbb{N}$, then an **$n$-cell [[attaching space|attachment]]** to $X$ is the result of gluing an [[n-disk]] to $X$, along a prescribed image of its bounding [[n-sphere|(n-1)-sphere]] (def. \ref{SpheresAndDisks}):

Let

$$
  \phi \;\colon\; S^{n-1} \longrightarrow X
$$

be a [[continuous function]], then the _[[attaching space]]_

$$
  X \cup_\phi D^n \,\in Top
$$

is the topological space which is the [[pushout]] of the boundary inclusion of the $n$-sphere along $\phi$, hence the universal space that makes the following [[commuting diagram|diagram commute]]

$$
  \array{
    S^{n-1} &\stackrel{\phi}{\longrightarrow}& X
    \\
    {}^{\mathllap{\iota_n}}\downarrow &(po)& \downarrow
    \\
    D^n &\longrightarrow& X \cup_\phi D^n
  }
  \,.
$$

+-- {: .num_example }
###### Example

A single cell [[attaching space|attachment]] of a 0-cell, according to def. \ref{SingleCellAttachment} is the same as forming the [[disjoint union space]] $X \sqcup \ast$ with the [[point]] space $\ast$:

$$
  \array{
     (S^{-1} = \emptyset) &\overset{\exists !}{\longrightarrow}&  X
     \\
     \downarrow &(po)& \downarrow
     \\
     (D^0 = \ast) &\longrightarrow& X \sqcup \ast
  }
  \,.
$$

In particular if we start with the [[empty topological space]] $X = \emptyset$ itself, then by [[attaching space|attaching]] 0-cells we obtain a [[discrete topological space]]. To this then we may attach higher dimensional cells.

Apart from attaching a set of cells all at once to a fixed base space, we may "attach cells to cells" in that after forming a given cell attachment, then we further attach cells to the resulting attaching space, and ever so on:

+-- {: .num_defn #RelativeCellComplexes}
###### Definition
**([[relative cell complexes]])

Let $X$ be a topological space, then 
a _topological [[relative cell complex]]_ of countable height based on $X$ is a [[continuous function]]

$$
  f \colon X \longrightarrow Y
$$

and a [[sequential diagram]] of [[topological space]] of the form

$$
  X = X_{-1} \hookrightarrow X_0 \hookrightarrow X_1 \hookrightarrow X_2 \hookrightarrow \cdots
$$

such that 

1. each $X_k \hookrightarrow X_{k+1}$ is exhibited as a cell attachment according to def. \ref{CellAttachments}, hence presented by a [[pushout]] diagram of the form

   $$
     \array{
       \underset{i \in I}{\sqcup} S^{n_i - 1}
         &\overset{(\phi_i)_{i \in I}}{\longrightarrow}&
       X_k
       \\
       \downarrow
         &(po)&
       \downarrow
       \\
       \underset{i \in I}{\sqcup} D^{n_i}
         &\longrightarrow&
      X_{k+1}
     }
     \,.
   $$

1. $Y = \u

[... 正文截断于 6000 字符 ...]
