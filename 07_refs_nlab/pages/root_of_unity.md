# root of unity

url: https://ncatlab.org/nlab/show/root+of+unity
last_revised: 2025-03-23
---

#### Algebra
+--{: .hide}
[[!include algebra - contents]]

* table of contents

## Idea

An $n$th _root of unity_ in a [[ring]] $R$ is an element $x$ such that $x^n = 1$ in $R$, hence is a [[root]] of the [[equation]] $x^n-1 = 0$.

## Properties

### Over a field

\begin{proposition}\label{SumOfRootsOfUnity}
**(sum of roots of unity)**
\linebreak
For $k \in \mathbb{N}_{\gt 0}$, let $\zeta$ be a $k$th root of unity in a [[field]], $\zeta^k = 1$. Then

\[
  \label{SumOfPowersOfRootOfUnity}
  \tfrac{1}{k}
  \sum_{n=0}^{k-1}
  \zeta^n
  \;=\;
  \left\{
  \begin{array}{lcl}
    1 &\vert& \zeta = 1
    \\
    0 &\vert& otherwise
  \end{array}
  \right.
  \,.
\]
\end{proposition}
\begin{proof}
  The case $\zeta = 1$ is immediate.
  For the case $\zeta \neq 1$ observe that
  $$
    (1 - \zeta)
    \sum_{n=0}^{k-1}
    \zeta^n
    \;=\;
    1 - \zeta^{k}
    \;=\;
    0
    \,.
  $$
\end{proof}
This may be understood as expressing the [[discrete Fourier transform]] of the [[Kronecker delta]]. For more subtle variants of the expression (eq:SumOfPowersOfRootOfUnity) see at *[[Gauss sum]]*.

\linebreak

In a [[field]] $k$, a [[torsion subgroup|torsion]] element of the multiplicative group $k^\ast$ is a [[root of unity]] by definition. Moreover we have the following useful result:

+-- {: .num_theorem} 
###### Theorem 
Let $G$ be a [[finite group|finite]] [[subgroup]] of the [[multiplicative group]] $k^\ast$ of a field $k$. Then $G$ is [[cyclic group|cyclic]]. 

+-- {: .num_lemma}
###### Lemma 
If $m, n$ are relatively prime and $x$ has order $m$ and $y$ has order $n$ in an abelian group, then $x y$ has order $m n$. 

Clearly there is at most one subgroup $G$ of a given order $n$ in $k^\ast$, which will be the set of $n^{th}$ [[roots of unity]]. If $G$ is a finite subgroup of order $n$ in $k^\ast$, then a generator of $G$ is called a **primitive** $n^{th}$ [[root of unity]] in $k$. 

+-- {: .num_cor}
###### Corollary 

Every [[finite field]] has a [[cyclic group|cyclic]] [[multiplicative group]].
