# loop group

url: https://ncatlab.org/nlab/show/loop+group
last_revised: 2026-03-21
---

#### Group Theory
+-- {: .hide}
[[!include group theory - contents]]

### Based loop group extension

\begin{proposition}
  For $G$ a [[topological group]], the free loop space of its [[underlying]] [[topological space]] is [[homeomorphism|homeomorphic]] to the [[product space]] of $G$ with its [[based loop space]]:
$$
  \mathcal{L}G
  \simeq
  G \times \Omega G
  \mathrlap{\,,}
$$
where the [[base point]] of $G$ is taken to be the [[neutral element]].

Moreover, this [[homeomorphism]] is also a [[group homomorphism]] with respect to the pointwise group operation on $\mathcal{L}G$ and the following [[semidirect product group]] [[structure]] on $G \times \Omega G$:

$$
  (g_1,\ell_1) (g_2, \ell_2)
  \coloneqq
  \Big(
    g_1 g_2,
    \big(
      t \mapsto
      g_2^{-1} \ell_1(t) g_2 \ell_2(t)
    \big)
  \Big)
  \mathrlap{\,.}
$$
\end{proposition}
\begin{proof}
  Let the loops be parameterized over $[0,1]$.
  Consider the maps
$$
  \begin{array}{ccc}
    \mathcal{L} G
      &\xrightarrow{\phantom{--} \Phi \phantom{--}}& 
    G \times \Omega G
    \\
    \gamma 
      &\mapsto& 
    \Big( 
      \gamma(0),  
      \big(
        t \mapsto \gamma(0)^{-1}\gamma(t)
      \big)
   \Big)
  \end{array}
$$
and
$$
  \begin{array}{ccc}
    G \times \Omega G
      &\xrightarrow{\phantom{--} \overline{\Phi} \phantom{--}}& 
    \mathcal{L} G
    \\
    (g, \ell) 
      &\mapsto&
    \big(
      t \mapsto g \ell(t)
    \big)
  \end{array}
$$
These maps are both [[continuous map|continuous]] since the operations of forming [[binary map|products]] and [[inverses]] in $G$ are continuous, by assumption on $G$. So it remains to check that the maps are [[inverses]] of each other. Indeed, unwinding the definitions, we have:
$$
  \begin{aligned}
    \overline{\Phi}\big(\Phi(\gamma)\big)
    & =
    \overline{\Phi}\Big(
      \gamma(0), 
      \big( t \mapsto \gamma(0)^{-1}\gamma(t) \big)
    \Big)
    \\
    & =
    \big(
      t \mapsto \gamma(0) \gamma(0)^{-1}\gamma(t)
    \big)
    \\
    & =
    \gamma
  \end{aligned}
$$
and
$$
  \begin{aligned}
    \Phi\big(\overline{\Phi}(g,\ell)\big)
    & =
    \Phi\big(
      t \mapsto g \ell(t)
    \big)
    \\
    & =
    \bigg(
      g \ell(0), 
      \Big(
        t \mapsto \big(g \ell(0)\big)^{-1} g \ell(t)
      \Big)
    \bigg)
    \\
    & =
    \Big(
      g , 
      \big(
        t \mapsto \ell(t)
      \big)
    \Big)
    \\
    & = 
    (g, \ell)
    \mathrlap{\,.}
  \end{aligned}
$$

Similarly, it is immediate to check that $\overline{\Phi}$ is a group homomorphism as claimed:
$$
  \begin{aligned}
    \overline{\Phi}\big(
      (g_1,\ell_1) (g_2, \ell_2)
    \big)
    & =
    \overline{\Phi}\bigg(
      \Big(
        g_1 g_2, 
        \big(
          t \mapsto g_2^{-1} \ell_1(t) g_2 \ell_2(t)
        \big)
      \Big)
    \bigg)
    \\
    & =
    \big(
      t \mapsto
        g_1 g_2 g_2^{-1} \ell_1(t) g_2 \ell_2(t)
    \big)
    \\
    & =
    \big(
      t \mapsto
        g_1 \ell_1(t) g_2 \ell_2(t)
    \big)
    \\
    & =
    \overline{\Phi}(
      g_1, \ell_1
    )
    \overline{\Phi}(
      g_2, \ell_2
    )
    \mathrlap{\,.}
  \end{aligned}
$$

\end{proof}

### Complexification

Let $G$ be a [[compact Lie group]].

+-- {: .num_prop }
###### Proposition

The [[complexification of a Lie group|complexification]] of $L G$ is the loop group of the complexification of $G$

$$
  (L G)_{\mathbb{C}}
  \simeq
  L (G_\mathbb{C})
  \,.
$$

#### By geometric quantization (looped orbit method)
 {#ByGeometricQuantization}

We discuss the [[quantization of loop groups]] in the sense of [[geometric quantization]] of their canonical [[prequantum bundle]].

Let $G$ be a [[compact Lie group]].
Let $T \hookrightarrow G$ be the inclusion of a [[maximal torus]]. There is a [[fiber sequence]]

$$
  \array{
    G/T &\to& L G / T
    \\
    && \downarrow
    \\
    && L G / G & \simeq \Omega G
  }
  \,.
$$

+-- {: .num_remark }
###### Remark

By the discussion at _[[orbit method]]_, if $G$ is a [[semisimple Lie group]], then $G/T$ is isomorphic to the [[coadjoint orbit]] of an element $\langle \lambda , -\rangle \in \mathfrak{g}^*$ for which $T \simeq G_\lambda$ is the [[stabilizer subgroup]].

If moreover $G$ is [[simply connected topological space|simply connected]], then the [[weight lattice]] $\Gamma_{wt} \subset \mathfrak{t}^* \simeq \mathfrak{t}$ of the Lie group $G$ is [[isomorphism|isomorphic]] to the group of [[group characters]]

$$
  \Gamma_{wt} \stackrel{\simeq}{\to} Hom_{LieGrp}(G,U(1))
  \,.
$$

This appears for instance as ([Segal, prop. 4.2](#Segal)).

### Relation to equivariant elliptic cohomology
 {#RelationToEquivariantEllipticCohomology}

Under mild conditions (but over the complex numbers) the representation ring of a loop group $L G$ is equivalent to the $G$-[[equivariant elliptic cohomology]] (see there for more) of the point ([Ando 00, theorem 10.10](#Ando00)).

This is a higher analog of how $G$-[[equivariant K-theory]] of the point gives the [[representation ring]] of $G$.

## Related concepts

* [[Kac-Moody group]]

* [[Verlinde ring]]

* [[string group]]

* [[caloron correspondence]]

* [[equivariant elliptic cohomology]]

* [[Kac character formula]]

* [[Kac-Weyl character]]

* [[double loop group]]

## References

The standard textbook on loop groups is

* {#PressleySegal} [[Andrew Pressley]], [[Graeme Segal]], _Loop groups_, Oxford University Press (1988) &lbrack;[ISBN:9780198535614](https://global.oup.com/academic/product/loop-groups-9780198535614)&rbrack;
  

A review talk is 

* {#Segal} [[Graeme Segal]], _Loop groups_ ([pdf](http://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BFb0084581/chapter08.pdf))
 

A review of some aspects with an eye towards loop groups as part of the [[crossed module]] of groups representing a [[string 2-group]] is in

* {#BCSS05} [[John Baez]], [[Alissa Crans]], [[Urs Schreiber]], [[Danny Stevenson]], _From loop groups to 2-groups_, Homology Homotopy Appl. Volume 9, Number 2 (2007), 101-135. ([arXiv:math/0

[... 正文截断于 6000 字符 ...]
