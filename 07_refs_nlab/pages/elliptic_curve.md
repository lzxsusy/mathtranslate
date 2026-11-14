# elliptic curve

url: https://ncatlab.org/nlab/show/elliptic+curve
last_revised: 2025-05-11
---

#### Complex geometry
+--{: .hide}
[[!include complex geometry - contents]]
#### Elliptic cohomology
+-- {: .hide}
[[!include elliptic cohomology -- contents]]

+-- {: .num_defn}
###### Definition

An elliptic curve over a [[field]] of [[positive characteristic]] whose [[formal group law]] has [[height of a formal group|height]] equal to 2 is called a _[[supersingular elliptic curve]]_. Otherwise the height equals 1 and the elliptic curve is called _ordinary_.

+-- {: .num_remark}
###### Remark

Much of the literature on elliptic curves considers def. \ref{GeneralWeierstrassCubic} for the case that $R$ is an [[algebraically closed field]], in which case there is no need to pass to a cover. But for the true global discussion necessary for the [[moduli stack of elliptic curves]] one needs the full generality.

+-- {: .num_remark #RelationBetweenDiscriminantAndTheModularInvariants}
###### Remark

In def. \ref{DiscriminantAndJInvariant} the discriminant satisfies the relation

$$
  1728 \Delta = c_4^3 - c_6^2
  \,.
$$

##### Elliptic curves, Nodal curves, Cuspidal curves
 {#EllipticCurvesNodalCurvesCuspidalCurves}

The following is a definition if one takes the coordinate-description as fundamental. If one takes the more abstract characterization of def. \ref{EllipticCurve} as fundamental then the following is a proposition.

+-- {: .num_defn}
###### Definition/Proposition

A solution to the Weierstrass cubic, def. \ref{GeneralWeierstrassCubic}, with modular invariants $c_4$, $c_6$ and discriminant $\Delta$ according to def. \ref{DiscriminantAndJInvariant} is

1. an _elliptic curve_ iff $\Delta \neq 0$;

1. a _[[nodal curve]]_ or _[[cubic curve]] with nodal [[singular point of an algebraic variety|singularity]]_  iff $\Delta = 0$ and $c_4 \neq 0$;

1. a _[[cuspidal curve]]_ or _[[cubic curve]] with [[cusp]] [[singular point of an algebraic variety|singularity]]_  iff $\Delta = 0$ and $c_4 = 0$ (which by remark \ref{RelationBetweenDiscriminantAndTheModularInvariants} is equivalent to $c_4 = 0$ and $c_6 = 0$)

##### Localization at 2 and 3

+-- {: .num_prop #WeierstrassEquationLocalAt2And3}
###### Proposition

If $2$ is invertible in $R$ (is a [[unit]] ), and hence generally over the [[localization of a ring|localization]] $R[\frac{1}{2}]$ of $R$ at 2, the general [[Weierstrass equation]], def. \ref{GeneralWeierstrassCubic}, is equivalent, to the equation

$$
  y^2  = 4 x^3  + b_2 x^2 + 2 b_4 x + b_6
$$

with the [[coefficients]] identified as in def. \ref{DiscriminantAndJInvariant}.

If moreover $3$ is also invertible in $R$, hence generally over $R[\frac{1}{2}, \frac{1}{3}]$ then this equation is equivalent to just

$$
  y^2 = x^3 - 27 c_4 x - 54 c_6
 \,.
$$

See e.g. ([Hain 08, section 5](#Hain08)) on how complex elliptic curves are expressed in this algebraic geometric fashion.

#### In terms of complex geometry
 {#InTermsOfCpomplexGeometry}

+-- {: .num_prop #CharacterizationOverC}
###### Proposition

An [[elliptic curve]], def. \ref{EllipticCurve}, over the [[complex numbers]] $\mathbb{C}$ is equivalently

* a [[Riemann surface]] $X$ of [[genus]] 1 with a base point $P \in X$ (e.g.[Hain 08, def. 1.1](#Hain08))

* a quotient $\mathbb{C}/\Lambda$ where $\Lambda$ is a [[lattice]] in $\mathbb{C}$;

* a compact complex [[Lie group]] of dimension 1.

* a [[smooth scheme|smooth]] [[algebraic curve]] of degree 3 in $\mathcal{P}$.

+-- {: .num_defn}
###### Definition

A **[[framed elliptic curve]]** is an elliptic curve $(X,P)$ in the sense of the first item in prop. \ref{CharacterizationOverC}, together with an [[ordering|ordered]] [[basis]] $(a,b)$ of $H_1(X, \mathbb{Z})$ with $(a \cdot b) = 1 $

For $n$ a natural number, a **[[level n-structure on an elliptic curve]]** over the complex numbers is similar data but with [[coefficients]] only in the [[cyclic group]] $\mathbb{Z}/n\mathbb{Z}$.

A **framed lattice** in $\mathbb{C}$ is a lattice $\Lambda$ together with an ordered basis $(\lambda_1, \lambda_2)$ of $\Lambda$ such that $Im(\lambda_2/\lambda_1) \gt 0$.

+-- {: .num_example}
###### Example

**(Jacobi quartics)**

$$
  y^2 = 1- 2 \delta x^2 + \epsilon x^4
$$

defines $E$ over $R = \mathbb{Z}[Y_Z,\epsilon, \delta]$.

The corresponding [[formal group law]] is **Euler's formal group law**

\[
  \label{EulerFormalGroupLaw}
  f(x,y) 
    \;=\; 
  \frac{
x{\sqrt{1- 2 \delta y^2 + \epsilon y^4}} + y{\sqrt{1- 2 \delta x^2 + \epsilon x^4}}
  }
  {1- \epsilon x^2 y^2}
\]

if $\Delta \coloneqq \epsilon(\delta^2 - \epsilon)^2 \neq 0$ then this is a non-trivial elliptic curve.
