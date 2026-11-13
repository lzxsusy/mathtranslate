# 源片段 tr04b（底本：SYZ Mirror Symmetry for Toric Fano Varieties）

<<B140 env>>
[ENV] **Lemma.** The summation $$\sum_{\mu(\beta)=2k}\int_{\left[\mathcal{M}_1 (\beta)\right]^{vir}}\ev^{\ast}\alpha\cdot T^{\omega (\beta)}$$ for any $\alpha\in\Omega^{\ast} (X_{\Sigma})$ is $0$ for $k\geq 2$.

<<B141 p>>
So only disks of Maslov index $2$ contribute non-trivially to the curvature $\mathfrak{m}^0$. Note that they correspond to holomorphic disks with a single intersection with one of the toric boundary components, and we can in fact determine all such holomorphic disks.

<<B142 env>>
[ENV] **Lemma.** Holomorphic disks with Maslov index $2$ are all projections of holomorphic disks $\tilde{u}\colon (\mathbb{D}^2,\partial\mathbb{D}^2)\to (\mathbb{C}^N\setminus Z(\Sigma),\tilde{L})$ of the form $$\tilde{u} (z)=(c_1,\dotsc, c_{i-1}, c_i z, c_{i+1},\dotsc, c_N)$$ for $c_j\in\mathbb{C}^{\ast}$ and some $1\leq i\leq N$. We write homotopy classes of such disks as $D(v_i)$.

<<B143 p>>
As all such counts are weighted by the area of the holomorphic disks, we also need to determine the symplectic area of these Maslov index $2$ holomorphic disks.

<<B144 env>>
[ENV] **Lemma.** Let $b\in\mathbb{R}^n$ be a vector, then the symplectic area of the holomorphic disk $D(v_i)$ with boundary on $L_b$ is given by $$\omega (D(v_i))=2\pi (\langle b,v_i\rangle -\lambda_i),$$ where $\lambda_i$ is the constant appearing in the definition of the moment polytope.

<<B145 p>>
With all these preparations, we are able to write down $\mathfrak{m}^0$ explicitly as follows: note that $\mathfrak{m}^0$ counts only holomorphic disks with one output, and therefore representing an element in $CF^{\ast} (L_b,\nabla;L_b,\nabla)$ of the form $$\mathfrak{m}^0 (L_b,\nabla)=\sum_{i=1}^N T^{\omega (D(v_i))}PD\left(\ev_{\ast}\left[\mathcal{M}_1 (D(v_i))\right]^{vir}\right)\hol_{\nabla} (\partial D(v_i))=\sum_{i=1}^N T^{2\pi(\langle b,v_i\rangle -\lambda_i)}\hol_{\nabla} (\partial D(v_i)),$$ and the function $z_i(L_b,\nabla)\colon =\exp\left(-\int_{D(v_i)}\omega\right)\hol_{\nabla} (\partial D(v_i))$ for $1\leq i\leq N$ can be shown to be holomorphic.

<<B146 p>>
Choose a basis $\{w_i\}_{i=1}^w$ of the torus $\left(\mathbb{C}^{\ast}\right)^n$, the curvature term then defines a Laurent polynomial on $\left(\mathbb{C}^{\ast}\right)^n$ which we call the _Hori-Vafa superpotential_. The other part of Homological Mirror Symmetry states that

<<B147 env>>
[ENV] **Statement.** There is an equivalence of triangulated categories $$D^{\pi}\mathcal{F} (X_{\Sigma},\omega_{\Sigma})\simeq HMF(\left(\mathbb{C}^{\ast}\right)^n,W_{\Sigma})$$ where $W_{\Sigma}\colon =\sum_{i=1}^N w_i^{v_i}$ is the Hori-Vafa superpotential.

<<B148 p>>
Going back to the computation of Fukaya $A_{\infty}$-algebra $CF^{\ast}(L_b,L_b)$, we want to firstly verify that the Floer cohomology is well-defined, i.e. $\left(\mathfrak{m}^1\right)^2=0$. This can be achieved by the following Proposition:

<<B149 env>>
[ENV] **Proposition.** Assume that $L_b$ does not bound any holomorphic disk of Maslov index $\leq 0$, then we have the following:

<<B150 li>>
- $\mathfrak{m}^0$ is a multiple of the point class $[\mathrm{pt}]$;

<<B151 li>>
- the Floer cohomology $HF^{\ast} (L,L)$ is well-defined with $[\mathrm{pt}]$ as a cocycle;

<<B152 li>>
- the chain-level product $\mathfrak{m}^2$ determines a well-defined associate product on $HF(L,L)$, for which $[\mathrm{pt}]$ is a unit.

<<B153 p>>
In particular, we have $\left(\mathfrak{m}^1\right)^2=\mathfrak{m}^2 (\mathfrak{m}^0,x)+(-1)^{\deg (x)+1}\mathfrak{m}^2 (x,\mathfrak{m}^0)=((-1)^{\deg (x)}+(-1)^{\deg (x)+1})C=0$.

<<B154 p>>
Therefore $HF^{\ast} ((L_b,\nabla),(L_b,\nabla))$ for all Lagrangian brane $(L_b,\nabla)$ is well-defined.
