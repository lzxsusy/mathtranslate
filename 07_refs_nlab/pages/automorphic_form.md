# automorphic form

url: https://ncatlab.org/nlab/show/automorphic+form
last_revised: 2026-09-09
---

### Context
#### Theta functions
+--{: .hide}
[[!include theta functions - contents]]

* table of contents

## Idea
 {#Idea}

Quite generally, _automorphic forms_ are suitably well-behaved [[functions]] on a [[quotient]] space $K\backslash X$ where $K$ is typically a [[discrete group]], hence suitable functions on $X$ which are [[invariant]] under the [[action]] of a discrete group. The precise definition has evolved a good bit through time.

[[Henri Poincaré]] considered [[analytic functions]] invariant under a discrete infinite group of [[fractional linear transformations]] and called them _[[Fuchsian functions]]_ (after his advisor [[Lazarus Fuchs]]). 

More generally, automorphic forms in the modern sense are suitable functions on a [[coset space]] $K \backslash G$, hence functions on [[groups]] $G$ which are [[invariant]] with respect to the [[action]] of the [[subgroup]] $K \hookrightarrow G$. The archetypical example here are [[modular forms]] regarded as functions on $K\backslash PSL(2,\mathbb{R})$ where $K$ is a [[congruence subgroup]], and for some time the terms "modular form" and "automorphic form" were used essentially synonymously, see [below](#ModularForms). Based on the fact that a [[modular form]] is a [[section]] of some [[line bundle]] on the [[moduli stack of elliptic curves]], [[Pierre Deligne]] defined an automorphic form to be a section of a line bundle on a [[Shimura variety]].

By pullback of functions the linear space of such functions hence constitutes a [[representation]] of $G$ and such representations are then called _automorphic representations_ (e.g. [Martin 13, p. 9](#Martin13)) , specifically so if $G = GL_n(\mathbb{A}_K)$ is the [[general linear group]] with [[coefficients]] in a [[ring of adeles]] of some [[global field]] and $K = GL_n(K)$. This is the subject of the _[[Langlands program]]_. There one also considers [[unramified]] such representations, which are constituted by functions that in addition are invariant under the action of $GL_n$ with coefficients in the [[integral adeles]], see [below](#InNumberTheory). 

### Modular forms as classical automorphic forms on $PSL(2,\mathbb{R})$
 {#ModularForms}

By a standard definition, a _[[modular form]]_ is a [[holomorphic function]] on the [[upper half plane]] $\mathfrak{H}$ satisfying a specified transformation property under the [[action]] of a given [[congruence subgroup]] $\Gamma$ of the [[modular group]] $G = PSL(2,\mathbb{Z})$ (e.g. [Martin 13, definition 1](#Martin13), [Litt, def. 1](#Litt)).

But the [[upper half plane]] is itself the [[coset]] of the [[projective linear group]] $G = PSL(\mathbb{R})$ by the subgroup $K = Stab_G(\{i\}) \simeq SO(2)/\{\pm I\}$

$$
  f\colon \mathfrak{H} \simeq PSL(2,\mathbb{R})/K
  \,.
$$

In view of this, one finds that every modular function $f \colon \mathfrak{H} \to \mathbb{C}$ lifts to a function 

$$
  \tilde f \colon \Gamma\backslash PSL(2,\mathbb{R})
  \longrightarrow \mathbb{C}
  \,,
$$

hence to a function on $G$ which is actually _invariant_ with respect to the $\Gamma$-action ("automorphy"), but which instead now satisfies some transformation property with respect to the action of $K$, as well as some well-behavedness property

This $\tilde f$ is the incarnation as an _automorphic function_ of the modular function $f$ (e.g. [Martin 13, around def. 3](#Martin13), [Litt, section 2](#Litt)). For emphasis these automorphic forms on $PSL(2,\mathbb{R})$ equivalent to modular forms are called _classical modular forms_.

This is where the concept of automorphic forms originates (for more on the history see e.g. [this MO comment](http://mathoverflow.net/a/124785/381) for the history of terminology) [and this one](http://mathoverflow.net/a/21556/381).

### Modular forms as adelic automorphic forms on $GL(2,\mathbb{A})$
 {#ModularFormsAdAdelicAutomorphicForms}

Where by the [above](#ModularForms) an ordinary [[modular form]] is equivalently a suitably periodic function on $SL(2,\mathbb{R})$, one may observe that the [[real numbers]] $\mathbb{R}$ appearing as [[coefficients]] in the latter are but one of many [[p-adic number]] completions of the [[rational numbers]]. Hence it is natural to consider suitably periodic functions on $SL(2,\mathbb{Q}_p)$ of all these completions at once. This means to consider functions on $SL(2,\mathbb{A})$, for $\mathbb{A}$ the [[ring of adeles]]. These are the _adelic automorphic forms_. They may be thought of as subsuming ordinary modular forms for all [[level structures]]. 
(e.g. [Martin 13, p. 8](#Martin13), also [Goldfeld-Hundley 11, lemma 5.5.10](#GoldfeldHundley11), [Bump, section 3.6](#Bump), [Gelbhart 84, p. 22](#Gelbhart84)): we have

$$
  \Gamma \backslash PSL(2,\mathbb{R})
  \simeq
  Z(\mathbb{A}) GL_2(\mathbb{Q})\backslash GL_2(\mathbb{A})/ GL_2(\mathbb{A}_{\mathbb{Z}})
  \,,
$$

where $\mathbb{A}_{\mathbb{Z}}$ are the [[integral adeles]]. (The [[double coset]] on the right is analogous to that which appears in the [[Weil uniformization theorem]], see the discussion there and at _[[geometric Langlands correspondence]]_ for more on this analogy.)

This leads to the more general concept of _adelic automorphic forms_ [below](#InNumberTheory).

### General adelic automorphic forms
 {#InNumberTheory}

More generally, for the [[general linear group]] $G = GL_n(\mathbb{A}_F)$, for any $n$ and with [[coefficients]] in a [[ring of adeles]] $\mathbb{A}_F$ of some [[number field]] $F$, and for the subgroup $GL_n(F)$, then sufficiently well-behaved functions on $GL_n(F)\backslash GL_n(\mathbb{A}_F)$ form [[representations]] of $GL_n(\mathbb{A}_{F})$ which are called _[[automorphic representations]]_. Here "well-behaved" typically means

1. **finiteness** -- the functions [[invariant]] under the [[action]] of the [[maximal compact subgroup]] [[span]] a [[finite number|finite]] [[dimension|dimensional]] [[vector space]];

1. **central character** -- the action by the [[center of a group|center]] is is controled by (...something...);

[... 正文截断于 6000 字符 ...]
