# group extension

url: https://ncatlab.org/nlab/show/group+extension
last_revised: 2026-02-23
---

#### Group Theory
+-- {: .hide}
[[!include group theory - contents]]

* table of contents

## Idea

A _group extension_ of a [[group]] $G$ by a group $A$ is third group $\hat G$ that sits in a [[short exact sequence]], that can usefully be thought of as a [[fiber sequence]], $A \to \hat G \to G$.

## Definition
 {#Definition}

+-- {: .num_defn #GroupExtension}
###### Definition

Two consecutive [[homomorphisms]] of  [[groups]]

\[\label{shortExtension} 
  A
  \overset{i}\hookrightarrow \hat G\overset{p}\to G
\]

are a **[[short exact sequence]]** if 

1. $i$ is [[monomorphism]], 

1. $p$ an [[epimorphism]] 

1. the [[image]] of $i$ is all of the [[kernel]] of $p$: $ker(p)\simeq im(i)$. 

We say that such a short exact sequence exhibits $\hat G$ as an **extension** of $G$ by $A$.

If $A \hookrightarrow \hat G$ factors through the [[center]] of $\hat G$ we say that this is a **[[central extension]]**.

Under the [[looping and delooping]]-equivalence, this is equivalently reformulated as follows. For $G \in$ [[Grp]] a [[group]], write $\mathbf{B}G \in $ [[Grpd]] for its [[delooping]] groupoid.

+-- {: .num_defn }
###### Definition

A sequence $A \to \hat G \to G$ is a [[short exact sequence]] of groups precisely if the [[delooping]]

$$
  \mathbf{B}A \to \mathbf{B}\hat G \to \mathbf{B}G
$$ 

is a [[fiber sequence]] in the [[(2,1)-category]] [[Grpd]].

+-- {: .num_prop }
###### Proposition

A morphism of extensions as in def. \ref{MorphismOfGroupExtensions} is necessarily an [[isomorphism]].

\[
  \label{equivExt}
  \array{
     1\to &A&\stackrel{i}\to &\hat G_1&\stackrel{p}\to &G&\to 1
     \\
    &\downarrow\mathrlap{=}&&\downarrow\mathrlap\epsilon&&\downarrow\mathrlap=&
    \\
    1\to &A&\stackrel{i'}\to &\hat G_2&\stackrel{p'}\to& G&\to 1
  }
  \,.
\]

## Properties

We discuss properties of group extensions in stages, 

* [General properties](#PropertiesGeneral)

* [Central group extensions](#PropertiesCentralGroupExtensions)

* [Abelian group extensions](#PropertiesAbelianGroupExtensions)

* [Schreier theory for nonabelian extensions](#SchreierTheory)

### General 
 {#PropertiesGeneral}

#### Fibers of extensions are normal subgroups

+-- {: .num_prop }
###### Proposition

For $A \hookrightarrow \hat G \to G$ a group extension, the inclusion $A \hookrightarrow \hat G$ is a [[normal subgroup]] inclusion.

#### Extensions as torsors / principal bundles
  {#Torsors}

+-- {: .num_prop}
###### Proposition

For $A \stackrel{i}{\to} \hat G \stackrel{p}{\to} G$ a group extension, we have that $p : \hat G \to G$ is an $A$-[[torsor]] over $G$ where  the [[action]] of $A$ on $\hat G$ is defined by

$$  
  \rho : A \times \hat G \stackrel{(i,Id)}{\to} \hat G \times_G \hat G \stackrel{\cdot}{\to} \hat G
  \,.
$$

For $A$ an [[abelian group]] we may understand the $A$-torsor/$A$-[[principal bundle]] $\hat G$ as the [[delooping]] of the $\mathbf{B}A$-[[principal 2-bundle]] $\mathbf{B} \hat G \to \mathbf{BG}$ that is classified by (is the [[homotopy fiber]] of) the 2-[[cocycle]] in [[group cohomology]]  $c : \mathbf{B}G \to \mathbf{B}^2 A$ that classifies the extension.

All this is then summarized by the statement that

$$
  A \to \hat G \to G \to \mathbf{B}A \to \mathbf{B}\hat G \to \mathbf{B}G \stackrel{c}{\to}
  \mathbf{B}^2 A
$$

is a [[fiber sequence]] in [[∞Grpd]] (or in [[LieGrpd]] if we have [[Lie group]] extensions, etc).

Here we may think of $\mathbf{B}\hat G$ as being the $\mathbf{B}A$-[[principal 2-bundle]] over $\mathbf{B}G$ classified by $c$. See the examples discussed at [[bundle gerbe]].

#### Split extensions and semidirect product groups
 {#SplitExtensionsAndSemidirectProductGroups}

+-- {: .num_defn #SplitExtension}
###### Definition

A group extension $A \to \hat G \stackrel{p}{\to} G$ is called **split** if there is a [[section]] [[homomorphism]] $\sigma \colon G \to \hat G$, hence a group homomorphism such that $p \circ \sigma = id_G$.

+-- {: .num_prop #SplitExtensionsAreSemidirectProducts}
###### Proposition

Split extensions $\hat G$ of $G$ by $A$, def. \ref{SplitExtension}, are equivalently [[semidirect product groups]] 

$$
  A \hookrightarrow \hat G \simeq A \rtimes_\rho G \to G
$$

for some [[action]] $\rho \colon G \times A  \to A$ of $G$ on $A$. 

+-- {: .num_prop}
###### Proposition

A split extension $A \to \hat G \to G$ is a [[central extension]] precisely if the [[action]] $\rho$ induced from it as in prop. \ref{SplitExtensionsAreSemidirectProducts} is trivial.

+-- {: .num_prop}
###### Remark

This means in particular that split central extensions are product groups $A \to G$. If all groups involved are [[abelian groups]], then these are equivalently the [[direct sums]] $A \oplus G$ of abelian groups. In this way the notion of split group extension reduces to that of [[split short exact sequences]] of abelian groups.

### Extensions by abelian groups
 {#ExtensionsByAbelianGroups}

Group extensions $A \hookrightarrow \widehat G \twoheadrightarrow G$ by [[abelian groups]] $A$ induce a [[linear map|linear]] [[group action]] of $G$ on $A$ making $A$ a *[[module]]* over the [[group ring]] of $G$, to be denoted $G \curvearrowright A$. The [[isomorphism classes]] of such extensions are classified by the second [[group cohomology]] $H^2_{grp}(G;\, G \curvearrowright A)$ of $G$ with [[coefficients]] in this [[module]] $A$ (cf. [Ho](#Ho)).

Beware that the action $G \curvearrowright A$ is often left notationally implicit in the literature but that the group cohomology sensitively depends on this action.

Precisely in the special case that the [[group action]] is [[trivial action|trivial]] these extensions are [[central extension]], classified by the group cohomology $H^2_{grp}(G;\, A)$ (cf. [Conrad p 1](#Conrad)). This is the case discussed in [the following](#PropertiesCentralGroupExtensions).

#### Central extensions
 {#PropertiesCentralGroupExtensions}

We discuss now properties of _central_ group extensions, those where $A \hookrightarrow \hat G$ factors through the [[

[... 正文截断于 6000 字符 ...]
