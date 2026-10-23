# From a noisy spin to an operational classical channel

[Learning route](README.md) · [Milestone map](MILESTONES.md) · [Educational anchor](ANCHOR.md) · [Scientific account](../science/README.md)

A growing spin carrier can retain its direction and almost all its classical communication capacity while its quantum communication rate tends to zero. This tutorial develops the objects and mechanism behind that statement. The crucial comparison concerns the entire noisy channel, including inputs entangled with an external reference.

The sections follow the settled M01–M30 map. Holevo's *Quantum Systems, Channels, Information* supplies the educational anchor: Chapters 3 and 6 for composite systems and channels, Chapters 7–8 for entropy and classical communication, Chapter 10 for quantum transmission, and Chapter 12 for a limited local Gaussian interpretation. These are the [verified chapter-level pointers](ANCHOR.md#verified-chapter-locations-and-their-role); the spin-specific claims and detailed proofs come from the linked scientific pages.

## 1. The carrier, its reference, and its channel — M01–M03

One irreducible spin $`j=n/2`$ has the basis $`|j,m\rangle`$, with $`m=-j,\ldots,j`$, and dimension $`d=n+1`$. Set $`\hbar=1`$. Its angular-momentum operators satisfy

```math
[J_a,J_b]=i\sum_c\epsilon_{abc}J_c,
\qquad
J_x^2+J_y^2+J_z^2=j(j+1)I.
```

A state is a positive matrix of trace one. Its three mean spin components describe only part of that matrix when $`j>1/2`$. Preserving those means therefore does not establish preservation of arbitrary superpositions or quantum encodings.

For example, a spin-one particle in $`|1,0\rangle`$ and an equal mixture of $`|1,1\rangle`$ and $`|1,-1\rangle`$ both have zero mean spin. A measurement of $`J_z`$ distinguishes their distributions immediately: the first always gives zero, while the second never does. The same three means can hide substantially different states, even before introducing entanglement.

An external reference makes this distinction operational. A joint state $`\rho_{RS}`$ can be entangled even though each reduced state is mixed. Separability means it can be expressed as a mixture of product states across the specified reference/spin split. Here the entire spin is one party. Entanglement between hypothetical constituent particles is a different bipartition.

A Bell pair illustrates why reduced states are insufficient. Each half is maximally mixed, just as for an equal classical mixture of $`|00\rangle`$ and $`|11\rangle`$. The Bell pair also has coherence between those alternatives. Testing a channel on one half asks whether it preserves the joint quantum correlations, beyond reproducing the local input state.

A quantum channel is completely positive and trace preserving, or CPTP. Complete positivity requires the extended operation $`\operatorname{id}_R\otimes\Phi`$ to preserve positivity for every reference. It ensures that the channel remains physically meaningful when its input belongs to an entangled system.

The channel studied here averages rotations:

```math
\Phi_t(\rho)=\int p_t(g)\,U_j(g)\rho U_j(g)^\dagger\,dg.
```

The density $`p_t`$ describes rotational Brownian motion. This channel preserves the identity and commutes with rotations: it is unital and rotation covariant. These are separate properties, and later anisotropic noise retains the first without the second. Independent Brownian increments give the semigroup relation $`\Phi_{t+s}=\Phi_t\circ\Phi_s`$.

Its complete positivity is visible directly: on a joint input, each integrand applies $`I_R\otimes U_j(g)`$ and its adjoint, preserving positivity and trace. Averaging preserves both properties. The loss of information comes from not retaining the random rotation label.

The resource assumptions matter. Encoders may use the whole irreducible carrier, with arbitrary final recovery and local implementation ancillas. An untouched reference tests entanglement; it is not an extra communication path. Intermediate error correction changes the channel. A symmetric sector of $`n`$ qubits realizes the carrier, but the full tensor product contains additional multiplicity subsystems protected from collective rotations. Those are outside this model. For capacities, $`m`$ independent uses mean $`\Phi_t^{\otimes m}`$; $`m`$ and the spin-size parameter $`n`$ play different roles. See the [model and resource scope](../science/model.md).

## 2. Directions, multipoles, and local fluctuations — M04–M06

A coherent spin state $`|\Omega\rangle`$ is a rotated highest-weight state $`|j,j\rangle`$, labeled by a direction on the unit sphere. These states are nonorthogonal and overcomplete. With normalized area measure,

```math
(n+1)\int_{S^2}|\Omega\rangle\langle\Omega|\,d\Omega=I.
```

Their overlap at angular separation $`\theta`$ is $`|\langle\Omega|\Omega'\rangle|^2=\cos^{2n}(\theta/2)`$. Thus their angular width is of order $`n^{-1/2}`$. The identity resolution both supplies a measurement and makes the uniform ensemble's average state $`I/d`$.

The diffusion generator and its multipole spectrum are

```math
\Phi_t=\exp(-t\mathcal C_j),\qquad
\mathcal C_j(X)=\sum_a[J_a,[J_a,X]],
\qquad
\Phi_t(T_{\ell m})=e^{-t\ell(\ell+1)}T_{\ell m},
\quad \ell=0,\ldots,n.
```

Rank zero is the identity; rank one contains the spin components. Polarization therefore decays by $`e^{-2t}`$. If the physical master equation is $`d\rho/ds=\gamma\sum_a\mathcal D[J_a](\rho)`$, the convention here is $`t=\gamma s/2`$.

The relevant scaled time is $`\nu=nt`$. Brownian angular width is of order $`\sqrt t`$, so at $`t=\nu/n`$ it competes with the coherent state's shrinking width. Every fixed multipole approaches its noiseless value in this limit. That observation alone cannot control a channel whose available ranks extend to $`n`$.

For a central distribution, the density relative to normalized Haar measure differs from the density of the physical rotation angle. On SO(3),

```math
w(\theta)=\frac2\pi\sin^2(\theta/2),\qquad 0\le\theta\le\pi.
```

The radial density is $`w(\theta)p_t(\theta)`$. Its small-time comparison is the Maxwell radius of a three-dimensional Gaussian. Locally around the north pole, $`Q_j=J_x/\sqrt j`$ and $`P_j=J_y/\sqrt j`$ obey

```math
[Q_j,P_j]=i(1-N/j),\qquad N=j-J_z.
```

Bounded excitation makes this approach the oscillator commutator. The local noise corresponds to random quadrature shifts with covariance $`\nu I_2`$, in the convention with vacuum variance $`1/2`$. This helps interpret the scale; it does not replace the whole spin by an oscillator. The [anchor's local-fluctuation discussion](ANCHOR.md#local-fluctuations-near-a-coherent-pole) explains that restriction.

## 3. Entanglement breaking and complete distance — M07–M08

A channel is entanglement breaking, abbreviated EB, if every joint input becomes separable across output/reference. Equivalently, it has a measurement-and-preparation implementation:

```math
\mathcal E(\rho)=\sum_x\operatorname{Tr}(M_x\rho)\,\sigma_x,
\qquad M_x\ge0,\qquad \sum_xM_x=I.
```

The measurement outcome may carry useful classical information. EB therefore permits substantial classical capacity.

Another equivalent characterization uses the normalized Choi state

```math
\rho_\Phi=(\Phi\otimes\operatorname{id})
(|\Omega_d\rangle\langle\Omega_d|),
\qquad
|\Omega_d\rangle=d^{-1/2}\sum_{r=1}^d|r,r\rangle.
```

The channel is EB exactly when this state is separable. Partial transposition on one factor preserves positivity of separable states, so a negative partial-transpose eigenvalue certifies entanglement. In general dimensions, a positive partial transpose does not establish separability.

Trace distance is $`\frac12\|\rho-\sigma\|_1`$. It bounds the difference in probabilities of every measurement event. The corresponding complete channel distance maximizes over joint inputs with a reference:

```math
\frac12\|\Phi-\Psi\|_\diamond
=\sup_{\rho_{RS}}\frac12
\|(\operatorname{id}_R\otimes(\Phi-\Psi))(\rho_{RS})\|_1.
```

A reference of input dimension suffices. Preprocessing and postprocessing by channels contract this distance. Thus one estimate controls all encoders and final decoders, including entangled tests.

The factor of one half has a statistical meaning. For two equally likely channels at half-diamond distance $`\delta`$, the best single-use discrimination success is $`(1+\delta)/2`$, allowing a reference and a final joint measurement. A small complete distance therefore limits every such operational distinction, rather than only comparisons in a selected basis.

The central quantity is

```math
e_j(t)=\inf_{\mathcal E\in\mathrm{EB}}
\frac12\|\Phi_t^{(j)}-\mathcal E\|_\diamond.
```

The infimum includes every EB comparator on these spaces. Exact EB means $`e_j(t)=0`$ at a given finite spin. Approximate EB in the growing-spin problem means this distance tends to zero along a specified sequence. The [model](../science/model.md#a-channel-distance-that-includes-every-encoding) fixes these conventions; the EB characterizations are attributed to Horodecki–Shor–Ruskai in the [source map](../references/RELATED_WORK.md#entanglement-breaking-continuity-and-the-limits-of-the-conclusion).

## 4. Entropy, coding, and the research question — M09–M12

All entropies use base-two logarithms. The von Neumann entropy is $`S(\rho)=-\operatorname{Tr}\rho\log_2\rho`$. A useful bound controls it using the mean of the nonnegative excitation observable $`N`$:

```math
S(\rho)\le g(\mu),\qquad
g(\mu)=(\mu+1)\log_2(\mu+1)-\mu\log_2\mu,
\quad g(0)=0,\quad \operatorname{Tr}(N\rho)\le\mu.
```

To justify this for the finite spin ladder when $`\mu>0`$, embed it in the nonnegative integer ladder and compare with the geometric distribution $`q_r=(1+\mu)^{-1}[\mu/(1+\mu)]^r`$. Nonnegative quantum relative entropy gives $`S(\rho)\le-\operatorname{Tr}\rho\log_2q`$. The logarithm is affine in excitation, producing $`g(\mu)`$. At $`\mu=0`$, only the ground level can be occupied and the entropy is zero. Coherences cause no difficulty; the actual state need not be thermal or Gaussian.

The function is increasing and concave: for positive $`\mu`$, its first derivative is $`\log_2(1+1/\mu)`$ and its second is $`-1/[\ln2\,\mu(1+\mu)]`$. Increasingness permits an upper estimate on mean excitation. Concavity later permits averaging over coherent directions when the output entropy depends on orientation. The bound controls uncertainty through excitation, independently of how many high levels exist.

For an input ensemble, the Holevo information is

```math
\chi=S\!\left(\sum_xp_x\Phi(\rho_x)\right)
-\sum_xp_xS(\Phi(\rho_x)).
```

The classical coding theorem makes this an achievable rate over independent uses with collective decoding. It gives a lower bound on ordinary classical capacity $`C`$ without requiring that the chosen ensemble be optimal.

Quantum capacity $`Q`$ instead concerns reliable quantum transmission using arbitrarily long block codes. Entanglement fidelity tests whether an encoded system can preserve a maximally entangled state with its reference. For an effective EB channel on a logical system of dimension $`k`$, this fidelity is at most $`1/k`$: every separable state has at most that overlap with $`|\Omega_k\rangle`$.

More explicitly, a rate $`R`$ is quantum-achievable when codes over $`m`$ uses can transmit logical dimensions growing like $`2^{mR}`$ with entanglement fidelity approaching one. Classical achievability instead requires that many distinguishable messages with error approaching zero. These coding limits are taken at each fixed channel, before comparing different spin sizes. They allow joint encoding and decoding across independent uses; a one-use witness or a one-use success probability alone does not determine either capacity.

The research question is therefore precise: at fixed $`\nu=nt`$, does proximity to EB vanish as the carrier grows, and what follows simultaneously for $`C`$, $`Q`$, and arbitrary recovery? Surviving entanglement, nonzero quantum capacity, and exact finite-spin EB times remain distinct questions. Their coding meanings are developed in [communication](../science/communication.md), with textbook chapter pointers in [ANCHOR](ANCHOR.md#references-resources-and-capacities).

## 5. A complete qubit example

For $`n=1`$, set $`J_a=\sigma_a/2`$. The double commutator fixes the identity and has eigenvalue two on each Pauli matrix. With $`\lambda=e^{-2t}`$,

```math
\rho=\frac12
\begin{pmatrix}
1+r_z&r_x-ir_y\\r_x+ir_y&1-r_z
\end{pmatrix}
\quad\longmapsto\quad
\Phi_t(\rho)=\lambda\rho+(1-\lambda)\frac I2.
```

The state condition is $`|r|\le1`$, and the Bloch vector contracts from $`r`$ to $`\lambda r`$. Encode an equally likely classical bit as $`|0\rangle`$ or $`|1\rangle`$ and measure in that basis. The two outputs are

```math
\Phi_t(|0\rangle\langle0|)
=\begin{pmatrix}(1+\lambda)/2&0\\0&(1-\lambda)/2\end{pmatrix},
\qquad
\Phi_t(|1\rangle\langle1|)
=\begin{pmatrix}(1-\lambda)/2&0\\0&(1+\lambda)/2\end{pmatrix}.
```

The success probability is $`(1+\lambda)/2`$, also the optimal discrimination probability for these two outputs. This is a one-use message experiment, separate from a capacity calculation.

Now send half of $`|\Omega_2\rangle=(|00\rangle+|11\rangle)/\sqrt2`$. In the basis $`00,01,10,11`$, the normalized Choi state is

```math
\rho_{\Phi_t}
=\lambda|\Omega_2\rangle\langle\Omega_2|+(1-\lambda)\frac{I_4}{4}
=\frac14
\begin{pmatrix}
1+\lambda&0&0&2\lambda\\
0&1-\lambda&0&0\\
0&0&1-\lambda&0\\
2\lambda&0&0&1+\lambda
\end{pmatrix}.
```

Partial transposition moves the off-diagonal entries into the middle block,

```math
\frac14\begin{pmatrix}1-\lambda&2\lambda\\2\lambda&1-\lambda\end{pmatrix}.
```

Its antisymmetric vector has eigenvalue $`(1-3\lambda)/4`$; the other three eigenvalues are $`(1+\lambda)/4`$. Hence $`\lambda>1/3`$ certifies that the channel is not EB.

Sufficiency at $`\lambda\le1/3`$ has a constructive proof. Measure the uniformly distributed coherent-state POVM and prepare the measured direction. Write that direction as the unit vector $`\mathbf s`$, so its projector is $`(I+\mathbf s\cdot\boldsymbol\sigma)/2`$. Normalized sphere measure satisfies $`\int\mathbf s\,d\mathbf s=0`$ and $`\int s_as_b\,d\mathbf s=\delta_{ab}/3`$. The outcome density is $`1+\mathbf r\cdot\mathbf s`$, giving

```math
\mathcal B(\rho)
=\int_{S^2}(1+\mathbf r\cdot\mathbf s)
\frac{I+\mathbf s\cdot\boldsymbol\sigma}{2}\,d\mathbf s
=\frac{I+(\mathbf r/3)\cdot\boldsymbol\sigma}{2}.
```

Thus this EB channel contracts the Bloch vector by $`1/3`$. Mixing it with the completely depolarizing channel realizes every contraction between zero and $`1/3`$. Consequently,

```math
t_{\mathrm{EB}}=\frac{\ln3}{2}\approx0.549306.
```

At this exact EB boundary, the classical readout still succeeds with probability $`2/3`$.

The distance to the entire EB set is also exact:

```math
e_{1/2}(t)=\max\left\{0,\frac{3\lambda-1}{4}\right\}.
```

For the lower bound, every separable Choi state has Bell overlap at most $`1/2`$, whereas the displayed state has overlap $`(1+3\lambda)/4`$. Their difference bounds trace distance and therefore half-diamond distance. This applies to every EB comparator.

For the matching upper bound when $`\lambda>1/3`$, choose the depolarizing channel with contraction $`1/3`$. A depolarizing channel is a mixture of Pauli conjugations with probabilities $`p_0=(1+3\lambda)/4`$ and $`p_x=p_y=p_z=(1-\lambda)/4`$. The triangle inequality bounds the full diamond difference by the sum of the absolute probability differences; a Bell input attains it because the four Pauli outputs are orthogonal. Half that sum is $`(3\lambda-1)/4`$.

Here $`\nu=t`$ because $`n=1`$. This finite-spin EB boundary need not equal the large-spin operational boundary derived below. The [normalized-Choi calculation](../science/residual_entanglement.md#1-exact-singlet-eigenvalue) recovers the same qubit eigenvalue.

## 6. A global measurement comparator — M13–M18

For general spin, use the coherent measurement-and-preparation channel

```math
\mathcal B_j(X)=(n+1)\int
\langle\Omega|X|\Omega\rangle
|\Omega\rangle\langle\Omega|\,d\Omega.
```

The identity resolution makes it trace preserving, and the displayed implementation makes it EB. Its exact multipliers and random-rotation representation are imported from [Aschieri–Ruba–Solovej](../references/RELATED_WORK.md#exact-coherent-channel-kernel-aschieri-ruba-and-solovej):

```math
b_{n,\ell}=\frac{n!(n+1)!}{(n-\ell)!(n+\ell+1)!},
\qquad
\mathcal B_j(X)=\int k_n(g)U_j(g)XU_j(g)^\dagger\,dg,
```

```math
k_n(\theta)=C_n\cos^{2n}(\theta/2),
\qquad C_n=\frac{4^n n!(n+1)!}{(2n)!}.
```

Integer-spin characters $`\chi_\ell(\theta)=\sin((\ell+1/2)\theta)/\sin(\theta/2)`$ verify the identity: $`\int k_n\chi_\ell\,dg=(2\ell+1)b_{n,\ell}`$. A character is the trace of the corresponding rotation matrix. For a central distribution, averaging is scalar on each irreducible tensor sector, and the trace determines that scalar. On SU(2), the kernel has peaks at both identity lifts. Conjugation identifies them, so SO(3) supplies the appropriate single-angle comparison.

For any fixed rank, the multiplier satisfies $`\ln b_{n,\ell}=-\ell(\ell+1)/n+O(n^{-2})`$, matching diffusion at time $`1/n`$. This explains the semiclassical resemblance. It leaves a serious uniformity issue: the rank can increase with the spin, and reference-assisted inputs can probe combinations of all ranks. A separate global estimate is required to control every allowed input.

The decisive step controls classical probability distributions before choosing the representation:

```math
\frac12\|\Phi_t-\mathcal B_j\|_\diamond
\le\frac12\int|p_t(g)-k_n(g)|\,dg
=\operatorname{TV}(p_t,k_n).
```

Every unitary conjugation has diamond norm one, whatever the spin dimension. This is why the bound survives a growing carrier and an arbitrary reference.

At $`t=1/n`$, compare both radial densities with

```math
m_t(\theta)=\frac{\theta^2}{2\sqrt\pi\,t^{3/2}}
e^{-\theta^2/(4t)},\qquad \theta\ge0,\qquad
\mathbb E_{m_t}\theta^2=6t.
```

Extend the group densities by zero beyond $`\pi`$. For $`r_n=w k_n`$, the inequality $`\log\cos x\le-x^2/2`$ gives

```math
r_n(\theta)\le A_nm_{1/n}(\theta),
\qquad A_n=\frac{C_n}{\sqrt\pi\,n^{3/2}}
\le(1+1/n)e^{1/(6n)}.
```

Normalization turns pointwise domination into $`\operatorname{TV}(r_n,m_{1/n})\le A_n-1=O(1/n)`$. Stirling bounds control the normalization uniformly, rather than merely identifying its limiting value.

The Maxwell density is normalized on the whole positive half-line. Its second moment is $`6t`$ because it is the radius of three independent Gaussian coordinates, each of variance $`2t`$. Keeping the radial measure explicit is essential: comparing the central densities while forgetting the Haar volume factor would give the wrong probability law and normalization.

For the heat kernel, Poisson summation gives the exact radial image formula

```math
h_t(\theta)=
\frac{e^{t/4}\sin(\theta/2)}{\sqrt\pi\,t^{3/2}}
\sum_{q\in\mathbb Z}(-1)^q(\theta-2\pi q)
e^{-(\theta-2\pi q)^2/(4t)}.
```

The zero image is $`m_t(\theta)e^{t/4}\operatorname{sinc}(\theta/2)`$. Its curvature correction has integrated size $`O(t)`$, since $`1-\operatorname{sinc}(\theta/2)\le\theta^2/24`$. The absolute-radius intervals of the remaining images partition $`[\pi,\infty)`$ once. Their total contribution is bounded by a Maxwell tail, as is the missing mass beyond the group interval. Thus the estimate includes curvature, wrapping images, and tails.

Combining the two explicit bounds gives

```math
\operatorname{TV}(p_{1/n},k_n)\le\frac{K_0}{n},
\qquad K_0=2.393520645\ldots<2.4.
```

This is a conservative uniform estimate, not the optimized diamond distance. For later times, the comparator $`\Phi_{t-1/n}\circ\mathcal B_j`$ remains EB. Semigroup composition and contraction therefore yield

```math
e_{n/2}(\nu/n)\le\min\{1,2.4/n\},
\qquad \nu\ge1.
```

The [full upper proof](../science/classicalization.md#3-a-uniform-finite-size-bound) records every constant. Its load-bearing feature is the dimension-independent conversion from total variation to complete channel distance.

## 7. A two-level witness below the boundary — M19–M21

The converse uses only the two highest spin levels, $`|0\rangle=|j,j\rangle`$ and $`|1\rangle=|j,j-1\rangle`$, entangled with a reference qubit. For a fundamental rotation

```math
u=\begin{pmatrix}a&b\\-\overline b&\overline a\end{pmatrix},
```

the symmetric-power representation gives exact entries

```math
U_{00}=a^n,\qquad
|U_{10}|^2=|U_{01}|^2=n|b|^2|a|^{2n-2},
\qquad U_{11}=a^{n-2}(1-n|b|^2).
```

The last expression is used for $`n\ge2`$. After the noise, a principal block of the partially transposed Bell output is

```math
\frac12\begin{pmatrix}A_n&B_n\\B_n&A_n\end{pmatrix},
\qquad
A_n=\mathbb E[n|b|^2(1-|b|^2)^{n-1}],
\quad B_n=\mathbb E[U_{11}\overline{U_{00}}].
```

Inversion symmetry makes $`B_n`$ real. At fixed $`\nu>0`$, scaled rotation coordinates $`X=\sqrt n\,\theta\widehat u`$ converge to $`N(0,2\nu I_3)`$. The transverse variable $`Z=(X_x^2+X_y^2)/4`$ is exponential with mean $`\nu`$. Consequently,

```math
A_n\longrightarrow\mathbb E[Ze^{-Z}]
=\frac{\nu}{(1+\nu)^2},
\qquad
B_n\longrightarrow\mathbb E[(1-Z)e^{-Z}]
=\frac1{(1+\nu)^2}.
```

The potentially rapid longitudinal phase cancels in the product defining $`B_n`$. Bounded matrix entries and Gaussian-tail control justify passage to the limit. This proves exactly the matrix-element statement needed, without assuming a global oscillator-channel approximation.

The limiting expectations are elementary Laplace transforms. The exponential variable has $`\mathbb E e^{-sZ}=1/(1+\nu s)`$; differentiating in $`s`$ gives $`\mathbb E[Ze^{-sZ}]=\nu/(1+\nu s)^2`$. In the finite-spin entries, $`n|b|^2`$ approaches $`Z`$ while $`(1-|b|^2)^n`$ approaches $`e^{-Z}`$. The witness thus balances noise-induced population transfer against surviving coherence in the same two levels.

The antisymmetric vector in this block has limiting partial-transpose expectation $`-(1-\nu)/[2(1+\nu)^2]`$. Transposing its projector gives a separability witness with operator norm $`1/2`$. Norm duality therefore turns the negative expectation into

```math
\liminf_{n\to\infty}e_{n/2}(\nu/n)
\ge\frac{1-\nu}{2(1+\nu)^2},
\qquad 0\le\nu<1.
```

For example, $`\nu=1/2`$ gives the nonzero lower bound $`1/9`$. At $`\nu=0`$, the Bell state is unchanged.

Together with the upper bound, this places the sharp boundary for vanishing distance to EB at $`\nu=1`$. The [converse proof](../science/classicalization.md#4-a-two-level-converse-below-the-boundary) establishes that operational statement; it does not locate a positive-quantum-capacity boundary.

The lower formula is a bound obtained from one chosen input and measurement. It need not equal the limiting channel distance. Sharpness here refers to its strictly positive sign at every fixed $`\nu<1`$, together with a uniform upper bound that vanishes at and above one.

## 8. Fidelity and the communication separation — M22–M25

Let arbitrary CPTP maps encode a logical $`k`$-dimensional system into the spin and recover it afterward. Replacing the noisy channel by its EB comparator makes the effective logical channel EB. Contraction preserves the error bound, and a Bell-projector probability changes by at most trace distance. Hence

```math
F_e\le\min\{1,1/k+2.4/n\},\qquad t\ge1/n.
```

No particular code or recovery circuit is assumed.

Classical communication has a different behavior. The uniform coherent ensemble has average output $`I/d`$, and covariance makes every individual output entropy equal. For north-pole input the exact mean excitation is

```math
\mu_j(t)=j(1-e^{-2t})\le nt.
```

The entropy bound and classical coding theorem give the finite-spin result

```math
C(\Phi_t)\ge\log_2(n+1)-g(\mu_j(t))
\ge\log_2(n+1)-g(nt).
```

At $`\nu=1`$, $`g(1)=2`$: at most two bits are lost from the dimensional maximum, while polarization retention is $`e^{-2/n}`$. This achievable rate permits collective decoding and is stronger than a statement about a single direction measurement.

For quantum capacity, the imported [Leung–Smith continuity theorem](../references/RELATED_WORK.md#entanglement-breaking-continuity-and-the-limits-of-the-conclusion) controls the regularized rate:

```math
|Q(\Phi)-Q(\Psi)|
\le8\epsilon\log_2d+4h_2(\epsilon),
\qquad \|\Phi-\Psi\|_\diamond\le\epsilon.
```

Here $`h_2`$ is binary entropy. Their error is the full diamond norm, so use $`\epsilon=4.8/n`$. For $`n\ge10`$ this is at most $`0.48`$. Since the EB comparator has zero quantum capacity,

```math
Q(\Phi_t)\le
\min\left\{\log_2(n+1),
\frac{38.4\log_2(n+1)}n+4h_2(4.8/n)\right\}
=O(\log n/n),
\quad t\ge1/n.
```

The dimension factor is essential, and the theorem already accounts for arbitrary block lengths at each fixed spin. Its conservative constants need not give a useful finite-size improvement at moderate $`n`$.

The separation also holds for $`t_n=n^{-\alpha}`$, with fixed $`0<\alpha<1`$. Now $`nt_n`$ grows, but the later-time comparison still applies. Using $`g(x)=\log_2x+\log_2e+o(1)`$,

```math
C(\Phi_{t_n})\ge\alpha\log_2n-\log_2e+o(1),
\qquad Q(\Phi_{t_n})=O(\log n/n),
\qquad e^{-2t_n}\longrightarrow1.
```

Thus the classical rate diverges across a range of shrinking times. The [communication proof](../science/communication.md) supplies the coding attribution, continuity theorem, and resource qualifications.

## 9. Unequal noise strengths and deterministic rotations — M26–M27

Replace isotropy by a fixed real symmetric positive-definite matrix $`D`$, with eigenvalues $`0<a\le b\le c`$:

```math
\mathcal L_D=-\sum_{r,s}D_{rs}[J_r,[J_s,\cdot]],
\qquad t=\tau/n.
```

Write $`D=aI+(D-aI)`$. The adjoint Casimir commutes with the remaining generator, so the channel factors into isotropic diffusion of time $`at`$ and another CPTP channel. The upper bound consequently applies for $`\tau a\ge1`$.

Write $`e_{j,D}`$ for the same distance to EB with this anisotropic channel. The lower witness sees the two tangent-plane noise strengths. At a pole whose transverse restriction is $`D_v`$, its limiting distance bound is

```math
\liminf_{n\to\infty}e_{n/2,D}(\tau/n)
\ge
\frac{(1-\tau^2\det D_v)_+}
{2\det(I+\tau D_v)^{3/2}}.
```

Choosing the pole along the strongest axis gives transverse strengths $`a,b`$. The operational boundary is therefore bracketed by

```math
\frac1{\sqrt{ab}}\le\tau_{\mathrm{op}}(D)\le\frac1a.
```

The bounds coincide when $`a=b\le c`$. For $`a<b`$, the exact coefficient remains unresolved. Unitality still preserves the ensemble average; averaging the output entropy bounds and using concavity of $`g`$ yields $`C\ge\log_2d-g(\tau\operatorname{Tr}D/3)`$ without assuming covariance.

The two rates enter through a Gaussian determinant. The isotropic Laplace transform becomes $`\mathbb E e^{-sZ}=\det(I+s\tau D_v)^{-1/2}`$; the same population/coherence combination produces the displayed numerator. By contrast, the global upper bound can extract only the guaranteed isotropic strength $`a`$. For classical entropy, averaging directions uses $`\int v^TDv\,d\Omega=\operatorname{Tr}D/3`$. These are three different uses of the noise matrix, explaining the bracket and the averaged rate.

Deterministic linear spin Hamiltonians $`H(s)=h(s)\cdot J`$ permit a stronger upper statement. With time-dependent positive-semidefinite diffusion matrices,

```math
\kappa(T)=\int_0^T\lambda_{\min}(D(s))\,ds,
\qquad n\kappa(T)\ge1
```

is sufficient for the same $`2.4/n`$ EB approximation. Casimir centrality makes the factorization survive strong prescribed rotations. The unchanged local lower limit has a narrower assumption: rotation rates bounded independently of $`n`$. Fast spin-dependent rotations may change the transverse noise seen by the witness.

The corresponding classical entropy bound uses $`(n/3)\int_0^T\operatorname{Tr}D(s)\,ds`$ as its argument of $`g`$. For fixed rank-deficient diffusion and bounded rotation rates, a transverse determinant vanishes and the lower witness remains positive at every fixed inverse-spin time. Nonlinear Hamiltonians and spin-dependent degenerating diffusion rates require separate analysis. The [anisotropic proof](../science/anisotropic_diffusion.md) gives the factorization, Gaussian integral, entropy averaging, and precise control scope.

## 10. Exact residual entanglement — M28–M29

Approximation by EB channels can coexist with an exactly negative Choi partial-transpose eigenvalue. Use the normalized Choi state defined above, with transpose on its second factor in the $`J_z`$ basis. Covariance makes its partial transpose commute with $`U_j\otimes U_j`$. The total-spin decomposition is multiplicity free, so the singlet

```math
|s_j\rangle=d^{-1/2}\sum_{m=-j}^j(-1)^{j-m}|m,-m\rangle
```

is an eigenvector. Its exact eigenvalue is

```math
\lambda_{0,n}(t)=\frac1{(n+1)^2}
\sum_{\ell=0}^{n}(-1)^\ell(2\ell+1)e^{-t\ell(\ell+1)}.
```

The proof uses the swap identity $`(|\Omega_d\rangle\langle\Omega_d|)^\Gamma=F/d`$, the singlet's swap parity $`(-1)^n`$, and the character identity $`(-1)^n\chi_j(g^2)=\sum_{\ell=0}^n(-1)^\ell\chi_\ell(g)`$. At zero time the formula gives $`(-1)^n/d`$, fixing the normalization. At $`n=1`$ it reproduces the qubit result.

For odd $`n`$, separate the finite alternating sum into the infinite heat sum $`H`$ minus its omitted tail $`R_n`$. The infinite sum is the positive heat kernel at angle $`\pi`$. At fixed positive $`\nu`$,

```math
H(\nu/n)\sim
\pi^{3/2}\nu^{-3/2}n^{3/2}e^{-\pi^2n/(4\nu)},
\qquad
R_n(\nu/n)\sim
\frac{e^{-2\nu}}{\cosh\nu}\,n e^{-\nu n}.
```

When $`0<\nu<\pi/2`$, the tail decays more slowly and dominates. Division by $`(n+1)^2`$ gives

```math
\lambda_{0,n}(\nu/n)\sim
-\frac{e^{-2\nu}}{\cosh\nu}\frac{e^{-\nu n}}n.
```

Thus fixed $`1\le\nu<\pi/2`$ supports both vanishing distance to EB and an NPT Choi state along sufficiently large odd $`n`$, corresponding to half-integer spins. At $`\nu=1`$, a finite certificate proves negativity for every odd $`n\ge5`$. At the endpoint $`\nu=\pi/2`$, the heat term's larger polynomial prefactor makes this particular eigenvalue eventually positive.

Parity determines the tail's first sign: odd $`n`$ makes the first omitted rank even and its contribution positive. The asymptotic argument controls the whole tail by an absolutely summable majorant after writing its ranks as $`n+1+k`$. It therefore requires fixed positive $`\nu`$ and compares complete sums, not just two individual terms. The endpoint changes because the exponential rates agree there and the polynomial prefactors become decisive.

The singlet witness also yields $`e_j(t)\ge-d\lambda_{0,n}(t)/2`$ when the eigenvalue is negative. This exponentially small lower bound is compatible with the independent $`O(1/n)`$ upper bound. Neither bound identifies the total residual entanglement, the exact PPT or EB time, or a positive quantum rate. The [residual-entanglement proof](../science/residual_entanglement.md) establishes the tail estimates and finite certificates.

## 11. The combined mechanism and its attribution — M30

The global and local arguments do different jobs. Comparing rotation distributions gives a uniform channel approximation that protects the conclusion against every encoding within the irreducible carrier. A two-level reference witness prevents that approximation below the limiting boundary. Entropy then quantifies the surviving classical messages, while capacity continuity constrains quantum transmission. Anisotropy tests which parts rely on isotropy; the singlet calculation exposes the difference between operational approximation and exact entanglement death.

Several ingredients are established prior work. Aschieri–Ruba–Solovej supply the coherent-channel identities. Berezin–heat comparisons, group-to-channel norm transfer, and spin diffusion have substantial precedents, including Ioos and collaborators, Bardet and collaborators, and Brody–Graefe–Melanathuru. EB characterizations, classical coding, and quantum-capacity continuity are imported tools. The [source map](../references/RELATED_WORK.md#established-ingredients-and-the-contribution-of-this-analysis) records these dependencies and the closest overlaps.

The analysis here combines the explicit shrinking-time, dimension-uniform comparison with the matching reference witness, communication consequences, qualified robustness results, and odd-spin residual asymptotics. The [verification record](../verification/README.md) provides reproducible finite checks; analytical estimates establish the asymptotic claims. Remaining questions include the general anisotropic coefficient, exact finite-spin PPT and EB times, and the quantum-capacity boundary below $`\nu=1`$.

The common result is a separation within one specified physical carrier: almost maximal classical communication can persist while every encoding faces a quantum-transmission converse. The [milestone map](MILESTONES.md), [educational anchor](ANCHOR.md), and [scientific route](../science/README.md) provide complementary paths through the definitions, background, and complete proofs.
