# de Rham complex

url: https://ncatlab.org/nlab/show/de+Rham+complex
last_revised: 2026-09-26
---

#### Cohomology
+--{: .hide}
[[!include cohomology - contents]]

* table of contents 

## Idea

The _de Rham complex_  (named after [[Georges de Rham]]) $\Omega^\bullet(X)$ of a [[space]] $X$ is the [[cochain complex]] that in degree $n$ has the [[differential form]]s (which may mean: [[Kähler differential form]]s) of degree $n$, and whose [[differential]] is the **de Rham differential** or **exterior derivative**.

As $X$ varies this constitutes an [[abelian sheaf]] of complexes.

## Definition

### For smooth manifolds

The **de Rham complex** of a [[smooth manifold]] is the [[cochain complex]] which in degree $n \in \mathbb{N}$ has the [[vector space]] $\Omega^n(X)$ of degree-$n$ [[differential forms]] on $X$. The coboundary map is the de Rham _[[exterior derivative]]_.

Explicitly, given a differential $k$-form $\omega$, its de Rham differential $d\omega$ can be computed as
$$d\omega(v_0,\ldots,v_k)=\sum_i (-1)^i \mathcal{L}_{v_i} \omega(v_0,\ldots,v_{i-1},v_{i+1},\ldots,v_k)+\sum_{i\lt j}(-1)^{i+j}\omega([v_i,v_j],v_0,\ldots,v_{i-1},v_{i+1},\ldots,v_{j-1},v_{j+1},\ldots,v_k),$$
where $v_i$ are [[vector fields]] on $X$, $[-,-]$ is the [[Lie bracket of vector fields]], and $\mathcal{L}_{v}$ is the [[Lie derivative]] of a smooth function with respect to a vector field $v$.

The [[chain cohomology|cohomology]] of the de Rham complex (hence the [[quotient]] of [[closed differential forms]] by [[exact differential forms]]) is __de Rham cohomology__. Under the [[wedge product]], the deRham complex becomes a [[differential graded algebra]]. This may be regarded as the [[Chevalley-Eilenberg algebra]] of the [[tangent Lie algebroid]] $T X$ of $X$.

The corresponding [[abelian sheaf]] in this case defines a [[smooth spectrum]] via the [[stable Dold-Kan correspondence]], see at _[smooth spectrum -- Examples -- De Rham spectra](smooth+spectrum#ExamplesDeRhamSpectra)_.

### For algebraic objects

For [[smooth varieties]] $X$, algebraic de Rham cohomology is defined to be the [[hypercohomology]] of the de Rham complex $\Omega_X^\bullet$.

De Rham cohomology has a rather subtle generalization for possibly singular algebraic varieties due to ([Grothendieck](#Grothendieck)). 

For [[analytic spaces]]

* T. Bloom, M. Herrera, _De Rham cohomology of an analytic space_, Inv. Math. __7__ (1969), 275-296, [doi](http://dx.doi.org/10.1007/BF01425536)

### For cohesive homotopy types
 {#ForCohesiveHomotopyTypes}

In the general context of [[cohesive homotopy theory]] in a [[cohesive (∞,1)-topos]] $\mathbf{H}$, for $A \in \mathbf{H}$ a [[cohesive homotopy type]], then the [[homotopy fiber]] of the [[counit of a comonad|counit]] of the [[flat modality]]

$$
  \flat_{dR} A \coloneqq fib(\flat A \to A)
$$

may be interpreted as the de Rham complex with [[coefficients]] in $A$.

This is the [[codomain]] for the [[Maurer-Cartan form]] $\theta_{\Omega A}$ on $\Omega A$ in this generality. The [[shape modality|shape]] of $\theta_{\Omega A}$ is the general [[Chern character]] on $\Pi(\Omega A)$.

For more on this see at

* _[structures in a cohesive infinity-topos -- de Rham cohomology](cohesive+%28infinity%2C1%29-topos+--+structures#deRhamCohomology)_

More precisely, $\flat_{dR} \Sigma A$ and $\Pi_{dR} \Omega A$ play the role of the non-negative degree and negative degree part, respectively of the de Rham complex with coefficients in $\Pi \flat_{dR} \Sigma A$. For more on this see at 

* _[differential cohomology diagram -- de Rham coefficients](differential%20cohomology%20diagram#DeRhamCoefficients)_.

## Examples

### de Rham cohomology of spheres

+-- {: .num_prop }
###### Proposition

For positive $n$, the de Rham cohomology of the $n$-[[sphere]] $S^n$ is 

$$
  H^p(S^n)
  = 
  \left\{
    \array{
      \mathbb{R} & if\; p = 0,n  
      \\
      0 & otherwise
    }
  \right.
  \,.
$$

For $n=0$, we have

$$
  H^p(S^0)
  = 
  \left\{
    \array{
      \mathbb{R} \oplus \mathbb{R} & if\; p = 0
      \\
      0 & otherwise
    }
  \right.
  \,.
$$

## Properties

### Basic theorems

* [[Poincare lemma]] 

* [[de Rham theorem]]

* [[nonabelian de Rham cohomology]]

### Relation to PL de Rham complex
  {#RelaionToPLDeRhamComplex}

+-- {: .num_prop #PLdeRhamComplex} 
###### Proposition
**([[PL de Rham complex of smooth manifold is equivalent to de Rham complex]])**

Let $X$ be a [[smooth manifold]].

We have the following [[zig-zag]] of [[dgc-algebra]] [[quasi-isomorphisms]] between the [[PL de Rham complex]] of (the [[topological space]] underlying) $X$ and the smooth [[de Rham complex]] of $X$:

$$
  \array{
    &&
    \Omega^\bullet_{PLdR}
    \big(
      S(X)
    \big)    
    &&
    &&
    \Omega^\bullet_{dR}(X)
    \\
    &
      {}^{
        \mathllap{
          i^\ast
        }
      }
      \nearrow
    & &
      \searrow^{
        \mathrlap{
          i_{poly}
        }
      }
    & & 
      {}^{
        \mathllap{
          p^\ast
        }
      }
      \swarrow
    \\
    \mathllap{
      \Omega^\bullet_{PLdR}(X)
      \;=\;
    }
    \Omega^\bullet_{PLdR}
    \big(
      Sing(X)
    \big)
    && && 
    \Omega^\bullet_{PSdR}
    \big(
      S(X)
    \big)
  }
$$

Here $S(X)$ is the [[simplicial complex]] corresponding to any smooth [[triangulation]] of $X$.
