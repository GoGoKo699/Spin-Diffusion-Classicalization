# Rank-two diffusion: a local cubic scale and a global gap

[Model](model.md) · [Positive anisotropy](anisotropic_diffusion.md) · [Nonlinear diffusion sister](https://github.com/GoGoKo699/Nonlinear-Diffusion-Entanglement)

Rank-two angular noise generates the missing rotation direction through commutators. Near a suitable coherent pole, a growing-excitation contraction turns this mechanism into the nonlinear oscillator channel studied in **Nonlinear-Diffusion-Entanglement**. This gives a stronger finite-spin obstruction to entanglement-breaking approximation. A separate global heat-kernel argument proves a weaker sufficient regime when the positive diffusion rates coincide. The two statements leave a genuine gap.

## 1. Model and established conclusions

Fix $`0<b\le c<\infty`$, independently of $`n=2j`$, on one irreducible spin carrier. Set

```math
\mathcal L_{b,c}=-b\,\mathrm{ad}_{J_y}^2-c\,\mathrm{ad}_{J_z}^2,
\qquad \Phi^{(j)}_{b,c,t}=e^{t\mathcal L_{b,c}},
\qquad e_{j;b,c}(t)=\inf_{\Psi\in\mathrm{EB}}
\tfrac12\|\Phi^{(j)}_{b,c,t}-\Psi\|_\diamond.
```

Thus $`D=\mathrm{diag}(0,b,c)`$ in the [anisotropic convention](anisotropic_diffusion.md). The distance includes arbitrary external references and all encodings into the carrier. No environment record, intermediate correction or noiseless quantum bypass is available.

**Local contraction and converse.** At $`t=s n^{-2/3}`$, a squeezed coherent-pole encoding converges on each fixed finite span of Schwartz oscillator vectors to the channel with generator

```math
\mathcal G=-\frac b2\,\mathrm{ad}_P^2
-c\,\mathrm{ad}_{Q^2/2}^2,\qquad [Q,P]=i.
```

For each fixed finite reference and bounded interval $`0\le s\le T`$, the output trace-norm error is $`O(n^{-2/3})`$, with constants depending on the input's Schwartz seminorms and on $`T,b,c`$. The encoded excitation moments grow as $`O(n^{r/3})`$. This is a controlled local statement, not convergence in the full spin diamond norm.

The limiting channel has an NPT output for a finite-energy input with a qubit reference at **every** fixed finite $`s>0`$. Its witness transfers to exact spin states, giving

```math
\boxed{\forall s\in(0,\infty):\quad
\liminf_{n\to\infty}e_{n/2;b,c}(s n^{-2/3})>0.}
```

Consequently, for any sequence of times,

```math
\boxed{e_{n/2;b,c}(t_n)\longrightarrow0
\quad\Longrightarrow\quad n^{2/3}t_n\longrightarrow\infty.}
```

**Global sufficient regime, equal rates.** For $`b=c`$, an actual coherent-state measurement comparator and a subelliptic heat-kernel estimate give, for sufficiently small $`t>0`$,

```math
\boxed{e_{n/2;b,b}(t)\le
\min\left\{1,\frac{C_b}{\sqrt n\,t}\right\}.}
```

In particular $`\sqrt n\,t_n\to\infty`$ is sufficient for global proximity to EB in this equal-rate family. There is no proved matching sufficiency at $`n^{2/3}t_n\to\infty`$, and this upper proof does not establish the fixed unequal-rate case.

The scale $`n^{-2/3}`$ is therefore a local cubic crossover and a necessary lower scale. It is **not** a proved sharp global classicalization scale, and no finite coefficient multiplying it makes the distance vanish in the large-spin limit.

## 2. Conditional covariance and inherited mechanisms

The horizontal Brownian coordinates of rank-two rotation noise have size $`\sqrt t`$; their bracket generates a coordinate of size $`t`$. At the $`z`$ pole, one noisy axis is longitudinal and rotates the remaining tangent-noise direction. The tangent displacement covariance has eigenvalue orders $`nt`$ and $`nt^2`$, giving a determinant of order $`n^2t^3`$.

This commutator mechanism is inherited. [Baudoin–Bonnefont](https://arxiv.org/abs/0802.3320v2), Sections 2 and 3.4, treat the rank-two SU(2) heat kernel and its Heisenberg contraction. [Schubert–Plastow](https://arxiv.org/abs/2307.08799v1), Theorem I.2 and Section III, identify delayed $`t^{2k+1}`$ decoherence in quadratic-Hamiltonian, linear-Lindblad models. Their Hilbert–Schmidt coherent-cross-term conclusions do not give diamond distance to EB. [Speed–Lyu–Schubert](https://arxiv.org/abs/2305.08467v1) introduce and solve the nonlinear oscillator model using Grushin and Mehler methods. A new notation for the cubic variable would not be a new hypoelliptic mechanism.

Exchanging $`Q,P`$ puts $`\mathcal G`$ into the nonlinear sister's convention with $`D=b/2`$, $`\kappa=c`$ and $`\eta=\omega=0`$. Its [conditional covariance](https://github.com/GoGoKo699/Nonlinear-Diffusion-Entanglement/blob/9c0ee02e018cf6940bcbb7916a666495331e8852/science/conditional_gaussian.md) has determinant

```math
\det V=8\Lambda Z,\qquad
\Lambda=\frac{b^2c}{4}s^3,
\qquad
Z=\int_0^1\left(B_u-\int_0^1B_v\,dv\right)^2du.
```

Here $`B`$ is standard Brownian motion and

```math
\mathbb E e^{-qZ}
=\left[\frac{\sqrt{2q}}{\sinh\sqrt{2q}}\right]^{1/2}.
```

On $`8\Lambda Z\ge1`$ the conditional additive Gaussian channel is EB by Holevo's Gaussian-channel criterion. Replacing exceptional paths by a preparation channel gives the **oscillator** distance bound

```math
e_{\mathrm{osc}}(s)\le
\min\left\{1,
\sqrt{\frac{8\Lambda}{1-e^{-8\Lambda}}}\,e^{-\Lambda}\right\}.
```

The [nonlinear distance proof](https://github.com/GoGoKo699/Nonlinear-Diffusion-Entanglement/blob/9c0ee02e018cf6940bcbb7916a666495331e8852/science/cubic_distance.md) owns this exceptional-path argument and its operational interpretation. It does not supply a finite-spin global EB approximant. At finite spin the conditional generators have operator-valued commutators; their time ordering is not merely a scalar phase.

## 3. A finite-spin reference witness before taking a contraction

There is a direct finite-dimensional check of the proposed scale. For any orthonormal spin states $`u_0,u_1`$, put

```math
|\Xi\rangle=\frac{|u_0\rangle|0\rangle+|u_1\rangle|1\rangle}{\sqrt2},
\qquad \rho_A=\tfrac12(|u_0\rangle\langle u_0|+|u_1\rangle\langle u_1|).
```

The Hilbert–Schmidt operator $`\mathcal C=b\,\mathrm{ad}_{J_y}^2+c\,\mathrm{ad}_{J_z}^2`$ is positive and self-adjoint, also after tensoring with the reference identity. The scalar inequality $`e^{-tx}\ge1-tx`$ and spectral calculus give the exact entanglement-fidelity bound

```math
F_\Xi(t)\ge1-2t\left[b\,\mathrm{Var}_{\rho_A}(J_y)
+c\,\mathrm{Var}_{\rho_A}(J_z)\right].
```

Every separable output has overlap at most $`1/2`$ with $`\Xi`$. Testing the rank-one effect $`|\Xi\rangle\langle\Xi|`$ therefore gives

```math
e_{j;b,c}(t)\ge
\left[\frac12-2t\left(b\,\mathrm{Var}_{\rho_A}(J_y)
+c\,\mathrm{Var}_{\rho_A}(J_z)\right)\right]_+.
```

### A code with growing excitation

Identify $`|k\rangle`$ with $`|j,j-k\rangle`$ for $`0\le k\le n`$. Let $`S(r)=e^{r(a^{\dagger2}-a^2)/2}`$, so $`S(r)^\dagger qS(r)=e^r q`$ and $`S(r)^\dagger pS(r)=e^{-r}p`$. Project $`S(r_n)|0\rangle`$ and $`S(r_n)|1\rangle`$ onto this ladder and normalize separately, with

```math
r_n=\frac{\log n}{6}+\log\zeta,\qquad \zeta>0\ \text{fixed}.
```

Parity makes the two projected states exactly orthogonal. The unprojected coefficients are

```math
\langle2k|S(r)|0\rangle
=\frac{\sqrt{(2k)!}\,\tanh^k r}{2^k k!\sqrt{\cosh r}},
\qquad
\langle2k+1|S(r)|1\rangle
=\frac{\sqrt{(2k+1)!}\,\tanh^k r}{2^k k!\cosh^{3/2}r}.
```

For their equal mixture, before projection,

```math
\langle N\rangle=\tfrac12+2\sinh^2r,
\qquad \langle p^2\rangle=e^{-2r},
\qquad \mathrm{Var}(N)=\tfrac14+5\sinh^2r\cosh^2r.
```

At $`r=r_n`$, the excitation is $`O(n^{1/3})`$, with $`r`$th moments $`O(n^{r/3})`$. Discarded polynomially weighted tails are exponentially small in $`n^{2/3}`$. Since $`J_z=j-N`$ exactly and the Holstein–Primakoff remainder in $`J_y=\sqrt{n/2}\,p+R_n`$ has norm $`O(1)`$ on these states,

```math
b\,\mathrm{Var}(J_y)+c\,\mathrm{Var}(J_z)
=\left(\frac b{2\zeta^2}+\frac{5c\zeta^4}{16}\right)n^{2/3}
+O(n^{1/3}).
```

The remainder bound follows from $`\sqrt n-\sqrt{n-k}\le k/\sqrt n`$ and the third excitation moment; it does not assume convergence of the noisy channel. Thus at $`t=s n^{-2/3}`$,

```math
\liminf_n e_{n/2;b,c}(s n^{-2/3})
\ge\left[\frac12-2s\left(\frac b{2\zeta^2}
+\frac{5c\zeta^4}{16}\right)\right]_+.
```

For $`b=c=\zeta=1`$ this is $`[1/2-13s/8]_+`$. Optimizing $`\zeta^6=4b/(5c)`$ replaces the parenthesis by $`K_*=(3/4)b^{2/3}(5c/4)^{1/3}`$. The direct witness alone proves a positive interval of scaled times and $`\liminf e_{n/2;b,c}(t_n)\ge1/2`$ when $`t_n=o(n^{-2/3})`$.

### Exact-channel numerical test

For the normalized projected code, compute

```math
D_{01}=\langle u_1|\Phi_t(|u_0\rangle\langle u_0|)|u_1\rangle,
\quad D_{10}=\langle u_0|\Phi_t(|u_1\rangle\langle u_1|)|u_0\rangle,
\quad C_{01}=\langle u_0|\Phi_t(|u_0\rangle\langle u_1|)|u_1\rangle.
```

An equal-Schmidt partial-transpose witness, with optimized phase, has expectation $`w=(D_{01}+D_{10}-2|C_{01}|)/4`$ and operator norm $`1/2`$. Every separable state has nonnegative expectation, so $`e_{j;b,c}(t)\ge[-w]_+`$ for the actual output. For $`b=c=\zeta=1`$, at $`t=s n^{-2/3}`$:

| $`n`$ | $`s=0.1`$ | $`s=0.5`$ | $`s=1`$ | $`s=2`$ |
|---:|---:|---:|---:|---:|
| 64 | −0.40266331 | −0.17185328 | −0.04553065 | +0.03655966 |
| 256 | −0.40186085 | −0.17061946 | −0.04535716 | +0.03475758 |
| 512 | −0.40162407 | −0.17022650 | −0.04523346 | +0.03436729 |

These are floating-point reference-entanglement tests, not interval certificates. A positive entry is a failure of this particular detector, not evidence of EB. The [verification route](../verification/README.md) explains the exact finite-spin tridiagonal algorithm, independent dense-generator controls and residuals. No oscillator evolution approximation is used in this table.

## 4. Controlled growing-excitation contraction

The direct witness is deliberately conservative. A controlled contraction transfers the nonlinear sister's finite-time converse to **every** finite scaled time.

### Exact extension and squeezing

On the oscillator ladder let $`\Pi_n=1_{N\le n}`$. The exact spin formulas on this subspace are

```math
J_+=\sqrt{n-N}\,a,\qquad
J_-=a^\dagger\sqrt{n-N},\qquad J_z=n/2-N.
```

Extend $`J_y`$ by zero outside $`\Pi_n\mathcal H`$ and keep the full oscillator $`N`$. Let $`S_n=S((\log n)/6)`$. In canonical variables $`Q,P`$,

```math
S_n^\dagger qS_n=n^{1/6}Q,\qquad
S_n^\dagger pS_n=n^{-1/6}P.
```

Set

```math
A_n=n^{-1/3}S_n^\dagger\Pi_nJ_y\Pi_nS_n,
\qquad
C_n=-n^{-1/3}S_n^\dagger(N+\tfrac12)S_n
=-\tfrac12(Q^2+n^{-2/3}P^2).
```

The squeezed spin subspace is invariant under both generators. On it, $`C_n`$ differs from $`n^{-1/3}S_n^\dagger J_zS_n`$ only by a scalar, which disappears from double commutators. The exact rescaled channel is therefore the restriction of $`e^{s\mathcal G_n}`$, where

```math
\mathcal G_n=-b\,\mathrm{ad}_{A_n}^2-c\,\mathrm{ad}_{C_n}^2.
```

### Vector estimates, including the squared generator

For a fixed Schwartz vector $`\psi`$ and every integer $`r\ge1`$,

```math
\|N^rS_n\psi\|\le C_{\psi,r}n^{r/3},\qquad
\|1_{N>n/2}S_n\psi\|\le C_{\psi,r}n^{-2r/3}.
```

Taylor expansion is controlled on $`N\le n/2`$ and the complementary tail is bounded by arbitrarily high moments. The cancellation in

```math
J_y=\frac{\{f(N),p\}}{2\sqrt2}
+\frac{[f(N),q]}{2i\sqrt2},\qquad f(N)=\sqrt{n-N},
```

gives, in vector norm on Schwartz vectors,

```math
A_n\psi=\frac P{\sqrt2}\psi
-\frac{n^{-2/3}}{8\sqrt2}\{Q^2,P\}\psi+O_\psi(n^{-1}).
```

This leading remainder cannot simply be multiplied by the growing full operator norm. To justify squaring, retain

```math
f_{n,2}(N)=\sqrt n\left(1-\frac N{2n}-\frac{N^2}{8n^2}\right)
```

and let $`B_n`$ be its squeezed, rescaled polynomial in place of $`A_n`$. On $`N\le n/2`$, the unsqueezed remainder is bounded by $`C n^{-5/2}N^3`$. Including the adjacent ladder operator and the $`n^{-1/3}`$ prefactor yields

```math
\|(A_n-B_n)\psi\|
\le Cn^{-17/6}\|(N+1)^{7/2}S_n\psi\|
+\text{complementary tails}
\le C_\psi n^{-5/3}.
```

The tails have any required inverse-power order. After cancellation, $`B_n`$ is a fixed-degree polynomial in $`Q,P`$ with uniformly bounded coefficients; every coefficient of $`B_n-P/\sqrt2`$ is $`O(n^{-2/3})`$. Thus its action preserves uniformly bounded Schwartz seminorms on each fixed vector. With $`A=P/\sqrt2`$ and $`\|A_n\|\le n^{2/3}/2`$,

```math
A_n^2-A^2=A_n(A_n-B_n)+(A_n-B_n)B_n+(B_n^2-A^2).
```

The three terms on a fixed Schwartz vector are respectively $`O(n^{-1})`$, $`O(n^{-5/3})`$ and $`O(n^{-2/3})`$. Hence

```math
\|(A_n^2-P^2/2)\psi\|\le C_\psi n^{-2/3}.
```

The exact expression for $`C_n`$ supplies the analogous estimates for $`C_n-C`$ and $`C_n^2-C^2`$, with $`C=-Q^2/2`$. Constants in these statements are bounded by finitely many Schwartz seminorms, not by an energy-independent operator norm.

### From generators to actual outputs

For $`\rho=|\psi\rangle\langle\phi|`$,

```math
\mathrm{ad}_A^2(\rho)
=|A^2\psi\rangle\langle\phi|
+|\psi\rangle\langle A^2\phi|
-2|A\psi\rangle\langle A\phi|.
```

The rank-one trace norm and the estimates above bound $`\|(\mathcal G_n-\mathcal G)\rho\|_1`$ by $`n^{-2/3}`$ times finitely many Schwartz seminorms. Finite matrix-valued sums cover each fixed finite reference.

The limiting random-unitary propagator consists of a quadratic shear and Weyl displacements. Its affine metaplectic coefficients have finite polynomial moments uniformly on bounded time intervals, by the conditional Brownian representation. It preserves Schwartz vectors pathwise, with integrable bounds on the required seminorms. For each $`n`$, the extended evolution is also well-defined: $`A_n`$ is bounded, and interaction with the quadratic self-adjoint $`C_n`$ gives a bounded stochastic perturbation. On these smooth trace-class inputs, variation of constants is valid:

```math
(e^{s\mathcal G_n}-e^{s\mathcal G})\rho
=\int_0^s e^{(s-u)\mathcal G_n}
(\mathcal G_n-\mathcal G)e^{u\mathcal G}\rho\,du.
```

CPTP trace-norm contraction and the integrable seminorm bounds prove the claimed $`O(n^{-2/3})`$ output estimate for fixed inputs and $`s\le T`$. Formal generator convergence alone is not used as a substitute for this step.

To obtain exact physical encodings, restrict $`\Pi_nS_n`$ to a fixed finite Schwartz span $`E`$. Its Gram matrix is $`I_E+O(n^{-K})`$ for every fixed $`K`$. Polar normalization gives an exact isometry $`V_n:E\to\mathcal H_j`$ differing by the same tail order. There is no postselection or loss of normalization. Mean excitation is $`O(n^{1/3})`$; mass above $`n^{1/3+\epsilon}`$ is smaller than any fixed inverse power for every $`\epsilon>0`$. This tail statement does not say that a hard growing cutoff is invariant under the channel.

## 5. All finite scaled times retain a reference witness

The nonlinear sister's [exact-threshold proof](https://github.com/GoGoKo699/Nonlinear-Diffusion-Entanglement/blob/9c0ee02e018cf6940bcbb7916a666495331e8852/science/exact_threshold.md), Sections 3–5, provides Gaussian packets and a qubit reference with a strictly negative partial-transpose expectation at each finite time when $`\eta=0`$. The packets are Schwartz, although their sufficient preparation parameters depend on time.

For fixed $`s,b,c`$, select those finite parameters once. Encode the fixed span containing both input packets and both test packets by $`V_n`$. The controlled output estimate preserves the strict negative witness margin for all sufficiently large $`n`$. The witness operator has a finite operator norm, so its negative expectation bounds the half trace distance from every separable output, and hence the half-diamond distance from every EB channel. This proves the all-finite-$`s`$ lower bound in Section 1. Its positive constant can be very small and is not a practical-memory guarantee.

If $`n^{2/3}t_n`$ had a bounded subsequence, it would be at most some finite $`S>0`$ there. Semigroup postprocessing makes the distance nonincreasing, so

```math
e_{n/2;b,c}(t_n)\ge e_{n/2;b,c}(S n^{-2/3}).
```

The right side has positive liminf. This proves the necessary divergence condition, rather than extrapolating a local noise determinant into a global threshold.

## 6. A separate global EB approximation for equal rates

Let $`\mathcal B_j`$ be the [coherent-state measurement-and-preparation channel](classicalization.md#1-an-established-measurement-channel), with exact random-rotation kernel $`k_n`$ from Aschieri–Ruba–Solovej, Lemma 13. If $`p_t`$ is the physical rank-two heat law on SO(3), then

```math
\Psi_{j,t}=\Phi^{(j)}_{b,b,t}\circ\mathcal B_j
```

is an actual EB channel on the entire spin carrier. The random-unitary transference bound gives

```math
\tfrac12\|\Phi^{(j)}_{b,b,t}-\Psi_{j,t}\|_\diamond
\le\mathrm{TV}(p_t,p_t*k_n).
```

This is uniform over input energy, encodings and reference dimension.

### Heat-kernel translation estimate

[Baudoin–Bonnefont, Theorem 4.3 and Remark 4.4](https://arxiv.org/abs/0802.3320v2) use $`L=X^2+Y^2`$ and $`[X,Y]=2Z`$. Write $`u`$ for their time and $`p_u^{\mathrm{BB}}`$ for the normalized SU(2) heat kernel. With their parameter $`\alpha=3`$, integrating the gradient estimate against $`p_u^{\mathrm{BB}}`$ removes the $`Lp/p`$ term and gives

```math
\int\Gamma(\log p_u^{\mathrm{BB}})p_u^{\mathrm{BB}}
+\frac u3\int(Z\log p_u^{\mathrm{BB}})^2p_u^{\mathrm{BB}}
\le\frac u3-4+\frac{64}u\le\frac{64}u,
\qquad 0<u\le1.
```

Cauchy–Schwarz therefore bounds the joint horizontal $`L^1`$ gradient by $`8/\sqrt u`$ and $`\|Zp_u^{\mathrm{BB}}\|_1`$ by $`8\sqrt3/u`$. For $`V=aX+dY+fZ`$, integrating along $`h\exp(-vV)`$, $`0\le v\le1`$, yields

```math
\|p_u^{\mathrm{BB}}(\,\cdot\,e^{-V})-p_u^{\mathrm{BB}}\|_1
\le\frac{8\sqrt{a^2+d^2}}{\sqrt u}
+\frac{8\sqrt3|f|}u
\le\frac{C\|V\|}u.
```

Translation preserves Haar measure. Choose the principal logarithm after passing to SO(3); its norm is proportional to the physical angle $`\theta\in[0,\pi]`$. Total variation contracts under this quotient, so no choice between the two central SU(2) representatives affects the estimate. The paper's fields are twice the physical spin-rotation fields, hence $`u=bt/4`$; constants absorb this fixed normalization.

The coherent kernel has the [proved radial domination](classicalization.md#the-coherent-measurement-kernel)

```math
\mathbb E_{k_n}\theta^2\le\frac{6A_n}{n},
\qquad A_n\le(1+1/n)e^{1/(6n)}.
```

Average the translation estimate against $`k_n`$ and use $`\mathbb E\theta\le\sqrt{\mathbb E\theta^2}`$. It follows that

```math
\mathrm{TV}(p_t,p_t*k_n)
\le\frac{C_b}{t}\mathbb E_{k_n}\theta
\le\frac{C'_b}{\sqrt n\,t}.
```

This proves the global upper bound. If a sequence with $`\sqrt n\,t_n\to\infty`$ does not tend to zero, monotonicity permits replacement by a smaller sequence tending to zero with the same divergence, so the sufficient condition still applies. The cited derivative theorem is for equal horizontal rates. Noncommuting Trotter factors do not by themselves extend this argument to arbitrary $`b\ne c`$.

## 7. What the remaining global question requires

At $`t=s n^{-2/3}`$, the missing group-coordinate width is $`t\asymp n^{-2/3}`$, while the coherent kernel adds isotropic angular width $`n^{-1/2}`$. The comparator above is not a small approximate identity in that missing direction; its proved upper estimate is then vacuous. Failure of this comparator is not an obstruction to every possible EB approximation.

A matching sufficient result would require globally CP and TP, input-independent EB maps $`\mathcal E_{j,t}`$ satisfying, in a specified regime,

```math
\tfrac12\|\Phi^{(j)}_{b,c,t}-\mathcal E_{j,t}\|_\diamond
\le\epsilon_{j,t}+\Pr(\text{exceptional paths}),
\qquad \epsilon_{j,t}\longrightarrow0.
```

All localization disturbance, path truncation and finite-spin errors must be included. A coherent-patch decomposition would itself need a valid quantum instrument and a uniform bound on entangled inputs. The local contraction and oscillator good-path EB replacements do not construct such an instrument or global channel.

The shared-result ownership is therefore precise: the nonlinear sister owns the conditional covariance, exceptional-path oscillator bound and finite-time oscillator NPT witness; this page owns their controlled growing-excitation transfer to rank-two spin diffusion, the finite-spin converse and the separate equal-rate global comparator. The inherited hypoelliptic and Gaussian mechanisms retain the attributions in Section 2. Neither project claims that local contraction closes the global gap.
