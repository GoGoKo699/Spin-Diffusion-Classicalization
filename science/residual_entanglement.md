# Residual entanglement beyond the operational boundary

[Model](model.md) · [Threshold proof](classicalization.md) · [Communication](communication.md)

## Result and conventions

Let $n=2j\in\mathbb N$, $d=n+1$, and let $J_x,J_y,J_z$ act in one irreducible spin-$j$ representation. Consider

```math
\Phi_t=\exp\!\left[-t\sum_{a=x,y,z}[J_a,[J_a,\cdot]]\right],
\qquad \nu=nt.
```

Rank-$\ell$ tensor operators have channel eigenvalue $e^{-t\ell(\ell+1)}$. Define the **normalized** Choi state and its partial transpose by

```math
\rho_{n,t}=(\Phi_t\otimes\operatorname{id})(|\Omega_d\rangle\langle\Omega_d|),
\quad |\Omega_d\rangle=d^{-1/2}\sum_{m=-j}^{j}|m,m\rangle,
\quad \rho_{n,t}^{\Gamma}=({\rm id}\otimes T)(\rho_{n,t}).
```

The basis for the transpose is the displayed $J_z$ basis. Let

```math
|s_j\rangle=d^{-1/2}\sum_{m=-j}^{j}(-1)^{j-m}|m,-m\rangle
```

be the total-spin-zero vector.

**Theorem.** The singlet is an eigenvector of $\rho_{n,t}^{\Gamma}$, with exact eigenvalue

```math
\boxed{\lambda_{0,n}(t)=\frac1{(n+1)^2}
\sum_{\ell=0}^{n}(-1)^\ell(2\ell+1)e^{-t\ell(\ell+1)}.}
\tag{1}
```

For every fixed $0<\nu<\pi/2$, along odd $n\to\infty$,

```math
\boxed{\lambda_{0,n}(\nu/n)
\sim-\frac{e^{-2\nu}}{\cosh\nu}\frac{e^{-\nu n}}n<0.}
\tag{2}
```

Consequently the channel has an NPT Choi state, and is not entanglement breaking, for all sufficiently large half-integer spins at each such fixed $\nu$. At $\nu=1$, the stronger finite statement holds: **every odd $n\ge5$** has a negative singlet eigenvalue.

This is compatible with the independent channel-level bound

```math
\inf_{\Psi\in\mathrm{EB}}\frac12\|\Phi_{\nu/n}-\Psi\|_\diamond
\le\frac{2.4}{n},\qquad \nu\ge1.
```

Thus, for $1\le\nu<\pi/2$, arbitrarily good approximation by entanglement-breaking channels coexists with exact Choi NPT along half-integer spins. Equation (2) describes **one identified partial-transpose eigenvalue**. It is not an upper bound on all residual entanglement, nor a determination of the exact PPT or EB time.

## 1. Exact singlet eigenvalue

The diffusion channel is a random rotation with the normalized SO(3) heat distribution $p_t(g)$. For half-integer spin, conjugation by $U_j(g)$ is independent of the choice of SU(2) lift. Since

```math
(|\Omega_d\rangle\langle\Omega_d|)^\Gamma=F/d,
```

where $F$ swaps the two spin factors,

```math
\rho_{n,t}^{\Gamma}
=\frac1d\int p_t(g)(U_j(g)\otimes I)F(U_j(g)^\dagger\otimes I)\,dg
=\frac1d\int p_t(g)(U_j(g)\otimes U_j(g)^\dagger)F\,dg.
\tag{3}
```

Covariance implies that $\rho_{n,t}^{\Gamma}$ commutes with every $U_j(h)\otimes U_j(h)$. The decomposition into total spins $0,1,\ldots,n$ is multiplicity free, so the singlet is an eigenvector. Its swap parity is

```math
F|s_j\rangle=(-1)^n|s_j\rangle.
```

Singlet invariance also gives

```math
(I\otimes U_j(g)^\dagger)|s_j\rangle=(U_j(g)\otimes I)|s_j\rangle.
```

Because each singlet marginal is $I/d$,

```math
\lambda_{0,n}(t)
=\frac{(-1)^n}{d^2}\int p_t(g)\operatorname{tr}[U_j(g)^2]\,dg.
\tag{4}
```

The SU(2) character identity

```math
(-1)^n\chi_j(g^2)=\sum_{\ell=0}^{n}(-1)^\ell\chi_\ell(g)
\tag{5}
```

follows directly by summing weights: in the alternating sum on the right, the surviving weights are $-n,-n+2,\ldots,n$, each with coefficient $(-1)^n$. Finally,

```math
\int p_t(g)\chi_\ell(g)\,dg=(2\ell+1)e^{-t\ell(\ell+1)}.
```

Substitution proves (1). As a normalization check, at $t=0$ it gives $\lambda_{0,n}(0)=(-1)^n/d$, exactly the singlet eigenvalue of $F/d$. For $n=1$, it gives the familiar qubit expression $(1-3e^{-2t})/4$.

## 2. Separate the antipodal heat kernel from a representation tail

Write

```math
S_n(t)=\sum_{\ell=0}^{n}(-1)^\ell(2\ell+1)e^{-t\ell(\ell+1)},
\quad H(t)=\sum_{\ell=0}^{\infty}(-1)^\ell(2\ell+1)e^{-t\ell(\ell+1)}.
```

Since $\chi_\ell(\pi)=(-1)^\ell$, $H(t)=p_t(\pi)>0$ is the SO(3) heat kernel at rotation angle $\pi$, relative to normalized Haar measure. For odd $n$, define the omitted tail

```math
R_n(t)=\sum_{\ell=n+1}^{\infty}(-1)^\ell(2\ell+1)e^{-t\ell(\ell+1)}.
```

Then

```math
S_n(t)=H(t)-R_n(t).
\tag{6}
```

The parity assumption is essential: when $n$ is odd, the first omitted term is positive. The argument below therefore produces a negative singlet eigenvalue for odd $n$. It makes no corresponding all-sector assertion for even $n$.

### 2.1 Exact heat-kernel image formula and its asymptotics

Poisson summation of the half-integer character series, evaluated at $\theta=\pi$, gives

```math
H(t)=\pi^{3/2}t^{-3/2}e^{t/4}
\sum_{k=0}^{\infty}(-1)^k(2k+1)
e^{-\pi^2(2k+1)^2/(4t)}.
\tag{7}
```

The coefficient contains both equally short images at angular displacements $+\pi$ and $-\pi$. Equivalently, start from the exact radial heat density

```math
h_t(\theta)=\frac{e^{t/4}}{\sqrt\pi t^{3/2}}\sin(\theta/2)
\sum_{q\in\mathbb Z}(-1)^q(\theta-2\pi q)e^{-(\theta-2\pi q)^2/(4t)}
```

and use $p_t(\pi)=\pi h_t(\pi)/2$. Pairing $q=0,1$, then $q=-1,2$, and so on gives (7).

For $0<t\le\pi^2/2$, the positive magnitudes in (7) decrease, so alternating-series bounds yield

```math
K(t)\bigl(1-3e^{-2\pi^2/t}\bigr)\le H(t)\le K(t),
\quad K(t)=\pi^{3/2}t^{-3/2}e^{t/4-\pi^2/(4t)}.
\tag{8}
```

In particular, for fixed $\nu>0$,

```math
H(\nu/n)
\sim \pi^{3/2}\nu^{-3/2}n^{3/2}
e^{-\pi^2 n/(4\nu)}.
\tag{9}
```

### 2.2 Dominated convergence for the omitted tail

Set $\ell=n+1+k$. For odd $n$,

```math
\frac{R_n(\nu/n)}{n e^{-\nu n}}
=\sum_{k=0}^{\infty}(-1)^k
\left(2+\frac{3+2k}{n}\right)
e^{-\nu(3+2k)}e^{-\nu(k+1)(k+2)/n}.
\tag{10}
```

For every fixed $\nu>0$ and every $n\ge1$, the absolute value of the summand is at most

```math
(5+2k)e^{-\nu(3+2k)}.
```

This is an absolutely summable, $n$-independent majorant. Dominated convergence applies to the series despite its alternating signs, giving

```math
\lim_{n\to\infty,\ n\ {\mathrm{odd}}}
\frac{R_n(\nu/n)}{n e^{-\nu n}}
=2e^{-3\nu}\sum_{k=0}^{\infty}(-e^{-2\nu})^k
=\frac{2e^{-3\nu}}{1+e^{-2\nu}}
=:\beta(\nu)=\frac{e^{-2\nu}}{\cosh\nu}>0.
\tag{11}
```

For a quantitative bound, put $q=e^{-2\nu}$ and define

```math
D(\nu)=e^{-3\nu}\left[
\frac{3+4\nu}{1-q}
+\frac{(2+6\nu)q}{(1-q)^2}
+\frac{2\nu q(1+q)}{(1-q)^3}\right].
\tag{12}
```

The elementary inequality $1-e^{-x}\le x$ gives, term by term,

```math
\left|\left(2+\frac{3+2k}{n}\right)e^{-\nu(k+1)(k+2)/n}-2\right|
\le\frac{3+2k+2\nu(k+1)(k+2)}n.
```

Summing the resulting geometric moments proves the explicit estimate

```math
\boxed{\left|\frac{R_n(\nu/n)}{n e^{-\nu n}}-\beta(\nu)\right|
\le\frac{D(\nu)}n.}
\tag{13}
```

### 2.3 Exponential comparison

For fixed $0<\nu<\pi/2$,

```math
\Delta(\nu)=\frac{\pi^2}{4\nu}-\nu>0.
```

Equations (8) and (13) yield the finite bound

```math
\left|\frac{S_n(\nu/n)}{n e^{-\nu n}}+\beta(\nu)\right|
\le\frac{D(\nu)}n
+\pi^{3/2}\nu^{-3/2}\sqrt n\,
e^{\nu/(4n)}e^{-n\Delta(\nu)}.
\tag{14}
```

Both terms on the right vanish. Since $\beta(\nu)>0$, $S_n(\nu/n)<0$ for all sufficiently large odd $n$, and

```math
\lambda_{0,n}(\nu/n)
=-\beta(\nu)\frac{e^{-\nu n}}n
\left[1+O_\nu\!\left(n^{-1}+\sqrt n\,e^{-n\Delta(\nu)}\right)\right].
\tag{15}
```

This proves (2). The estimate is for fixed $\nu$; it is not uniform as $\nu\uparrow\pi/2$.

## 3. Explicit finite-spin NPT certificates

Let $a_\ell(t)=(2\ell+1)e^{-t\ell(\ell+1)}$. If

```math
t(2n+3)^2\ge2,
\tag{16}
```

then $a_\ell(t)$ decreases for all real $\ell\ge n+1$, since the derivative of its logarithm is $2/(2\ell+1)-t(2\ell+1)$. For odd $n$, alternating-series bounds imply

```math
R_n(t)\ge a_{n+1}(t)-a_{n+2}(t).
```

Consequently the following fully explicit conditions certify a negative singlet eigenvalue:

```math
\begin{gathered}
0<t\le\pi^2/2,\qquad t(2n+3)^2\ge2,\qquad n\ {\mathrm{odd}},\\
(2n+3)e^{-t(n+1)(n+2)}
\left[1-\frac{2n+5}{2n+3}e^{-2t(n+2)}\right]
>\pi^{3/2}t^{-3/2}e^{t/4-\pi^2/(4t)}.
\end{gathered}
\tag{17}
```

The certificate uses an upper bound on the full heat contribution and a lower bound on the omitted tail. It therefore does not depend on resolving a small difference between large floating-point terms.

### At the operational threshold: all odd $n\ge5$

Set $t=1/n$. For $n\ge5$, (16) holds and

```math
R_n(1/n)\ge
2n e^{-n-17/5}\left(1-\frac{15}{13}e^{-2}\right),
```

whereas

```math
H(1/n)\le\pi^{3/2}n^{3/2}e^{1/20-\pi^2 n/4}.
```

Their lower ratio bound is

```math
\frac{R_n(1/n)}{H(1/n)}
\ge
\frac{2e^{-69/20}(1-15e^{-2}/13)}{\pi^{3/2}}
\frac{e^{(\pi^2/4-1)n}}{\sqrt n}.
\tag{18}
```

The right-hand side is increasing for $n\ge5$. At $n=5$, the elementary inequalities $\pi>3$, $\pi^{3/2}<6$, $\sqrt5<9/4$, $e^2>7$, and $\sqrt e>3/2$ already lower-bound it by $1064/819>1$. Thus $R_n>H$ for every odd $n\ge5$, proving the stated finite-spin result. For example,

```math
\lambda_{0,5}(1/5)=-6.77854310143684068\times10^{-5}.
```

## 4. The endpoint and the interpretation of the scale $\pi/2$

At $\nu=\pi/2$, the two exponential rates agree. Their polynomial prefactors do not: the heat term scales as $n^{3/2}$, and the omitted tail as $n$. Therefore

```math
\lambda_{0,n}\!\left(\frac\pi{2n}\right)
\sim 2\sqrt2\,n^{-1/2}e^{-\pi n/2}>0.
\tag{19}
```

For fixed $\nu>\pi/2$, the heat contribution also wins exponentially, and the singlet eigenvalue is eventually positive. Thus $\pi/2$ is the boundary for the fixed-$\nu$ sign behavior of **this singlet eigenvalue**. Positivity of one sector says nothing sufficient about the other partial-transpose sectors. Even positivity of all sectors would only establish PPT, not automatically separability or the entanglement-breaking property in these dimensions.

## 5. A channel-distance consequence

Let $W=(|s_j\rangle\langle s_j|)^\Gamma$. Since the singlet is maximally entangled,

```math
\|W\|_\infty=1/d.
```

For every separable state $\sigma$, $\operatorname{tr}(W\sigma)\ge0$. When $\lambda_{0,n}<0$, Hölder's inequality gives

```math
\frac12\|\rho_{n,t}-\sigma\|_1\ge-\frac d2\lambda_{0,n}(t).
```

Applying this to normalized Choi states of EB channels yields

```math
\inf_{\Psi\in\mathrm{EB}}\frac12\|\Phi_t-\Psi\|_\diamond
\ge-\frac{n+1}{2}\lambda_{0,n}(t).
\tag{20}
```

In particular, for fixed $1\le\nu<\pi/2$, along odd $n$,

```math
\liminf e^{\nu n}
\inf_{\Psi\in\mathrm{EB}}\frac12\|\Phi_{\nu/n}-\Psi\|_\diamond
\ge\frac{e^{-2\nu}}{2\cosh\nu}>0.
\tag{21}
```

This is an exponentially small **lower** bound, alongside the independent $O(1/n)$ upper bound. It does not establish the decay rate of the optimized channel distance, total negativity, distillable entanglement, or quantum capacity.

## 6. Reproducible validation

[The residual-entanglement verification](../verification/README.md) compares two independently constructed representations and includes the finite-spin checks below.

1. It constructs spin matrices, forms the full double-commutator generator, exponentiates it, builds the normalized Choi matrix, and partially transposes it. Across 35 cases with $n=1,2,3,4,5,7,9$ and $\nu=0,0.5,1,1.4,1.7$, the singlet formula agrees to at most $3.68\times10^{-16}$; the largest singlet eigenvector residual is $1.22\times10^{-15}$. Choi normalization and positivity are also checked.
2. Seventeen scalar cases use Python `Decimal.exp`, with precision chosen to resolve the exponentially small sum. Values through $n=401$ agree with the Poisson heat term minus the independently summed tail to less than $10^{-55}$ after dividing by $n e^{-\nu n}$. The explicit tail bound (13) passes in every case. The tests include $\nu=1,1.5,1.55,\pi/2$, so they check both negative residual NPT and the positive endpoint prefactor.

For $n=401$, the ratio $-S_n(\nu/n)/[\beta(\nu)n e^{-\nu n}]$ is approximately $0.999567$ at $\nu=1$, $0.996829$ at $\nu=1.5$, and $0.996390$ at $\nu=1.55$. The corresponding eigenvalue at $\nu=\pi/2$ is positive. These checks test conventions and finite-size behavior; the asymptotic statement follows from the analytic bounds above.

## Related primary literature and scope

The representation-theoretic simplification of partial transposition for rotationally invariant spin states is established background; see J. Schliemann, *Entanglement in SU(2)-invariant quantum spin systems*, Physical Review A **68**, 012309 (2003), [arXiv:quant-ph/0212114](https://arxiv.org/abs/quant-ph/0212114), [DOI](https://doi.org/10.1103/PhysRevA.68.012309). Equations (1)–(21) provide a self-contained specialization and asymptotic analysis for the diffusion channel, rather than relying on an unverified generic PPT formula.

The operational EB-approximation theorem uses the coherent-state channel identity from Aschieri, Ruba and Solovej, *SU(2)-Equivariant Quantum Channels: Semiclassical Analysis*, Communications in Mathematical Physics **405**, 298 (2024), [DOI](https://doi.org/10.1007/s00220-024-05178-1). Qualitative large-spin agreement of coherent measurement and diffusion is discussed by Brody, Graefe and Melanathuru, *Phase-space measurements and decoherence for angular momentum systems*, [arXiv:2605.02696](https://arxiv.org/abs/2605.02696). The [related-work account](../references/RELATED_WORK.md) distinguishes the imported representation methods from the diffusion-specific operational and asymptotic statements.
