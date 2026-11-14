# stack

url: https://ncatlab.org/nlab/show/stack
last_revised: 2025-11-04
---

#### $(\infty,1)$-Topos Theory
+--{: .hide}
[[!include (infinity,1)-topos - contents]]

* table of contents

## Idea

The term _stack_ is a traditional synonym for _[[2-sheaf]]_ (typically specifically on a [[category]] rather than a [[2-category]]) or often, more restrictively, a synonym for _[[(2,1)-sheaf]]_ (see there for more details).

This is part of a whole hierarchy of [[higher category theory|higher categorical]] generalizations of the notion of a _[[sheaf]]_. A [[(2,1)-sheaf]] / stack is equivalently a [[1-truncated]] [[(∞,1)-sheaf]]/[[∞-stack]].

Generally, the term _[[n-stack]]_ is a synonym for _[[n-sheaf|(n+1)-sheaf]]_, or more restrictively for _[[(n,1)-sheaf|(n+1,1)-sheaf]]_.

More concretely, this means that a 1-stack on a [[site]] $S$ (or more generally [[(2,1)-site]] or even [[(2,2)-site]] $S$) is 

* a ([[pseudofunctor|pseudo]]-)[[functor]] from  $S^{op}$ to the 2-category [[Cat]] of categories

* that satisfies [[descent]] for all covers.

If the pseudofunctor takes values in the 2-subcategory [[Grpd]]$\subseteq Cat$ of groupoids, the stack is sometimes referred to as a _stack of groupoids_. This is the more commonly occurring case, so the term "stack" has come to mean "stack of groupoids" in much of the literature. 

In some circles, the notion of a stack as a generalized [[groupoid]] is almost more familiar than the notion of a sheaf as a [[space and quantity|generalized space]]. For instance, [[differentiable stacks]] have attracted much attention in the study of [[Lie groupoids]] and [[orbifolds]], while [[diffeological space|diffeological spaces]] are only beginning to be investigated more in [[Lie theory]]. Groupoid stacks are closely related to internal groupoids (see [this MO post](https://mathoverflow.net/questions/93948/link-between-internal-groupoids-and-stacks-on-a-topos)).

An [[algebraic stack]], [[differentiable stack]], etc. is a stack over a site of schemes or differentiable manifolds with additional representability conditions. 

## Provisional discussion

The following is "provisional" material on stacks that [[Todd Trimble]] wrote in the course of a discussion with [[Urs Schreiber|Urs]]. Somebody should turn this here into a coherent entry on stacks.

***

(Todd speaking.) I don't really speak "stacks", but in an effort to build a bridge between sheaves and stacks, I'll write down what I thought I understood, and ask someone such as Urs to come in and check. (Warning: I'm treating this edit box almost as a sandbox, in that what I say below is all a bit provisional until we get some discussion going.) 

+--{.query}
 Hi Todd, thanks for this. I started making some remarks on the relation between descent $\infty$-categories and pseudofunctors from [[covers]] regarded as [[sieves]] (hence as presheaves) at [[descent and codescent]] in the section titled _Descent in terms of pseudo-functors_.
