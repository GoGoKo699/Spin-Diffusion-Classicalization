# Anisotropic diffusion and deterministic rotations

[Model](model.md) · [Threshold proof](classicalization.md) · [Communication](communication.md)

Unequal rotation-noise strengths preserve an inverse-spin operational boundary. Two-sided bounds locate it exactly when the two smallest diffusion strengths coincide, even if the third is arbitrarily stronger and fixed.

## Model, conventions, and conclusions

Let $`n=2j`$ be a positive integer, let $`\mathcal H_j`$ be one irreducible spin-$`j`$ representation, and let $`d=n+1`$. For a real symmetric positive semidefinite $`3\times3`$ matrix $`D`$, define

```math
\mathcal L_D(X)=-\sum_{a,b=x,y,z}D_{ab}[J_a,[J_b,X]],
\qquad \Phi_{D,t}=e^{t\mathcal L_D}.
```

The eigenvalues of $`D`$ are physical angular diffusion rates. Our normalization is that $`D=\gamma I`$ gives tensor multipliers $`e^{-\gamma t\ell(\ell+1)}`$ and mean-spin retention $`e^{-2\gamma t}`$. The short-time variable for a fixed $`D`$ is $`\tau=nt`$; the products of $`\tau`$ with the diffusion rates are dimensionless, whereas $`\tau`$ retains time units if those units have not been fixed. This is anisotropic random rotation noise with a real symmetric diffusion matrix, not a general nonunital spin-relaxation model.

Write

```math
0<a\le b\le c
```

for the eigenvalues of a positive definite $`D`$, and define

```math
e_{j,D}(t)=\inf_{\Psi\in\mathrm{EB}}
\frac12\|\Phi_{D,t}-\Psi\|_\diamond.
```

The following bounds hold.

**Upper bound, exact at finite $`n`$.** For every $`t`$ with $`nat\ge1`$,

```math
e_{j,D}(t)\le\min\{1,K_0/n\}.
\tag{1}
```

Here $`K_0\approx2.393520645246<2.4`$ is the constant defined exactly in the [isotropic kernel comparison](classicalization.md#3-a-uniform-finite-size-bound).

**Lower bound, fixed anisotropy and fixed $`\tau`$.** For every finite $`\tau\ge0`$,

```math
\liminf_{n\to\infty}e_{j,D}(\tau/n)
\ge
\left[
\frac{1-\tau^2ab}{2[(1+\tau a)(1+\tau b)]^{3/2}}
\right]_+.
\tag{2}
```

In particular, the distance remains bounded away from zero when $`\tau<1/\sqrt{ab}`$, while it is $`O(1/n)`$ when $`\tau\ge1/a`$. These bounds give an interval for the boundary; they do not establish a universal equality.

**A nontrivial exactly located family.** If the two smallest rates coincide, $`a=b\le c`$, then the onset of asymptotic proximity to EB channels is exactly

```math
\tau_{\mathrm{op}}(D)=\frac1a,\qquad \tau=nt.
\tag{3}
```

This remains true for an arbitrarily stronger fixed third-axis rate $`c`$. The lower witness uses the coherent pole along that third axis. Its limiting lower bound is

```math
\frac{1-a\tau}{2(1+a\tau)^2},\qquad a\tau<1.
```

**Classical capacity, exact finite-$`n`$ bound.** Let $`g(x)=(x+1)\log_2(x+1)-x\log_2x`$, with $`g(0)=0`$. Then

```math
C(\Phi_{D,\tau/n})\ge
\log_2(n+1)-g\!\left(\frac{\tau\operatorname{Tr}D}{3}\right).
\tag{4}
```

Here $`C`$ denotes unassisted classical capacity for independent channel uses. When $`\tau\ge1/a`$ is fixed and $`D`$ is fixed, (1) and finite-dimensional quantum-capacity continuity give

```math
Q(\Phi_{D,\tau/n})=O\!\left(\frac{\log n}{n}\right),
\quad
C(\Phi_{D,\tau/n})\ge\log_2(n+1)-O_D(1).
\tag{5}
```

At the same times every coherent input retains mean spin along its original direction by at least $`e^{-(b+c)\tau/n}=1-O_D(1/n)`$. All these conclusions are for the growing irreducible carrier, with no noiseless quantum side channel and no active correction during the noisy interval.

## 1. Upper bound from the adjoint Casimir

Let $`A_a=[J_a,\cdot]`$ and $`C_{\mathrm{ad}}=\sum_a A_a^2`$. The operators $`A_a`$ form the adjoint $`\mathfrak{su}(2)`$ representation, so $`C_{\mathrm{ad}}`$ commutes with every $`A_b`$, hence with every quadratic $`A_aA_b`$. Set $`D=aI+R`$, where $`R`$ is positive semidefinite. Then

```math
\mathcal L_D=-a C_{\mathrm{ad}}+\mathcal L_R,
\qquad [C_{\mathrm{ad}},\mathcal L_R]=0,
```

and both summands generate CPTP semigroups. Consequently

```math
\Phi_{D,t}=\Phi_{I,at}\circ\Phi_{R,t}
=\Phi_{R,t}\circ\Phi_{I,at}.
\tag{6}
```

The isotropic core supplies an explicitly EB channel $`\mathcal B_j`$, the coherent POVM followed by coherent-state preparation, such that

```math
\tfrac12\|\Phi_{I,1/n}-\mathcal B_j\|_\diamond\le K_0/n.
\tag{7}
```

If $`at\ge1/n`$, replace the isotropic factor in (6) by $`\Phi_{I,at-1/n}\circ\mathcal B_j`$. The resulting full channel is EB, because an EB map remains EB under arbitrary CPTP pre- and postprocessing. Diamond distance is contractive under those operations. This proves (1), without perturbation theory in the anisotropy and without a condition-number prefactor.

The constant $`K_0`$ in (7) is the [isotropic kernel-comparison constant](classicalization.md#3-a-uniform-finite-size-bound). The exact random-rotation representation of $`\mathcal B_j`$ is prior work of [Aschieri, Ruba, and Solovej](../references/RELATED_WORK.md#exact-coherent-channel-kernel-aschieri-ruba-and-solovej), *Communications in Mathematical Physics* **405**, 298 (2024), Lemma 13; the short-time total-variation comparison is proved in the threshold account.

## 2. Local Gaussian limit for arbitrary orientation

Fix a unit vector $`v`$ and choose orthonormal axes $`e_1,e_2`$ in $`v^\perp`$. Let $`D_v`$ be the $`2\times2`$ tangent restriction, with entries $`(D_v)_{kl}=e_k^TDe_l`$. Its eigenvalues are denoted $`\mu_1,\mu_2`$. Rotate the spin basis so that $`v`$ is the north pole, and use the two states

```math
|0\rangle=|j,j\rangle_v,\qquad |1\rangle=|j,j-1\rangle_v.
```

The same Bell-pair witness used in the isotropic proof yields the orientation-dependent bound

```math
\liminf_{n\to\infty}e_{j,D}(\tau/n)
\ge
\left[
\frac{1-\tau^2\det D_v}{2\det(I_2+\tau D_v)^{3/2}}
\right]_+.
\tag{8}
```

There is no squeezing operation or oscillator code hidden in this bound.

### 2.1 Brownian representation and its short-time contraction

Let $`B_t`$ be a three-dimensional Brownian motion with covariance $`\mathbb E[B_tB_t^T]=2tD`$. On the fundamental representation of $`\mathrm{SU}(2)`$, solve the Stratonovich equation

```math
dU_t=-\frac{i}{2}\sum_a\sigma_a U_t\circ dB_{a,t},\qquad U_0=I.
```

The spin-$`j`$ representation gives a random-unitary realization of $`\Phi_{D,t}`$; its Itô generator on density matrices is exactly $`\mathcal L_D`$. The use of the $`\mathrm{SU}(2)`$ cover is harmless because conjugation is unchanged by its center.

A first-order stochastic expansion at $`t=\tau/n`$ gives

```math
U_{\tau/n}=I-\frac{i}{2}\boldsymbol\sigma\cdot B_{\tau/n}
+O_{L^2}(n^{-1}).
\tag{9}
```

For completeness, the Itô drift is bounded and contributes $`O(t)`$ in $`L^2`$. In the stochastic remainder, replace $`U_s`$ by $`U_s-I`$; Itô isometry and $`\mathbb E\|U_s-I\|^2=O(s)`$ give a squared $`L^2`$ remainder of order $`\int_0^t s\,ds=O(t^2)`$. This proves (9). Thus $`\sqrt n\,B_{\tau/n}`$ has the limiting Gaussian law $`N(0,2\tau D)`$, and $`\sqrt n\,(U-I)`$ has the corresponding linearized law. Only this finite-dimensional Brownian limit is used; a uniform approximation of the entire spin Hilbert space is unnecessary for the lower bound.

Write the fundamental matrix in the chosen pole basis as

```math
U=\begin{pmatrix}\alpha&\beta\\-\overline\beta&\overline\alpha\end{pmatrix},
\qquad |\alpha|^2+|\beta|^2=1.
```

Then $`q=|\beta|^2`$ satisfies

```math
nq\ \Longrightarrow\ Z=\frac{X_1^2+X_2^2}{4},
\qquad (X_1,X_2)\sim N(0,2\tau D_v),
\tag{10}
```

while $`\alpha`$ tends in probability to one. Correlations with the longitudinal component do not affect this marginal law.

### 2.2 Exact finite-spin matrix elements

The spin-$`j`$ representation is the symmetric power of order $`n`$ of the fundamental one. Its top two matrix elements satisfy

```math
U_{00}=\alpha^n,\quad
|U_{10}|^2=|U_{01}|^2=nq(1-q)^{n-1},\quad
U_{11}=\alpha^{n-2}(1-nq).
\tag{11}
```

Use the input $`(|0,0\rangle+|1,1\rangle)/\sqrt2`$, with a qubit reference. The partial transpose of its output has the principal block on $`|1,0\rangle`$, $`|0,1\rangle`$

```math
\frac12\begin{pmatrix}A_n&B_n\\\overline B_n&A_n\end{pmatrix},
\quad
A_n=\mathbb E[nq(1-q)^{n-1}],\quad
B_n=\mathbb E[U_{11}\overline U_{00}].
\tag{12}
```

The dangerous longitudinal phase cancels exactly in the product:

```math
U_{11}\overline U_{00}
=\overline\alpha^{\,2}(1-q)^{n-2}(1-nq).
```

Equations (9)–(11) therefore imply

```math
A_n\to\mathbb E[Ze^{-Z}],\qquad
B_n\to\mathbb E[(1-Z)e^{-Z}].
\tag{13}
```

These expectation limits are rigorous: both finite-spin integrands have absolute value at most one, $`nq`$ is tight, and the elementary powers converge uniformly on each compact range of $`nq`$. Truncating that range and then taking its size to infinity justifies the passage to expectations.

### 2.3 The unsqueezed Bell witness detects the geometric mean

For $`s\ge0`$, the Laplace transform of $`Z`$ is

```math
M(s)=\mathbb E[e^{-sZ}]=\det(I_2+s\tau D_v)^{-1/2}
=[(1+s\tau\mu_1)(1+s\tau\mu_2)]^{-1/2}.
```

The limiting $`A`$ and $`B`$ are $`-M'(1)`$ and $`M(1)+M'(1)`$. Hence

```math
B-A=M(1)+2M'(1)
=\frac{1-\tau^2\mu_1\mu_2}
{[(1+\tau\mu_1)(1+\tau\mu_2)]^{3/2}}.
\tag{14}
```

When $`\tau\sqrt{\mu_1\mu_2}<1`$, $`B>A\ge0`$ and the block has limiting negative eigenvalue $`-(B-A)/2`$. Let $`w=(|1,0\rangle-|0,1\rangle)/\sqrt2`$ and $`W=(|w\rangle\langle w|)^{\Gamma_R}`$. Its operator norm is $`1/2`$ and its expectation is nonnegative on every separable state. Thus the output's half trace-norm distance from separable states is at least $`(B-A)/2`$ in the limit. Every EB comparator sends this input to a separable state, proving (8).

### 2.4 Optimal pole for this witness and the sandwich

For positive definite $`D`$,

```math
\det D_v=v^T\operatorname{adj}(D)v
=(\det D)v^TD^{-1}v.
```

Its minimum is $`ab`$, attained when $`v`$ is an eigenvector for the largest rate $`c`$. At that pole, the tangent eigenvalues are $`a,b`$, proving (2). More generally, eigenvalue interlacing gives $`\mu_1\ge a`$ and $`\mu_2\ge b`$; the positive expression in (8) decreases as either tangent rate increases. Thus this pole also maximizes the positive bound among this particular family of witnesses.

A precise definition avoiding unproved intermediate limits is

```math
\tau_{\mathrm{op}}(D)=\inf\left\{\tau\ge0:
\limsup_{n\to\infty}e_{j,D}(\tau/n)=0\right\}.
```

Semigroup postprocessing makes $`e_{j,D}(t)`$ nonincreasing in $`t`$, and the proved bounds imply

```math
\frac1{\sqrt{ab}}\le\tau_{\mathrm{op}}(D)\le\frac1a.
\tag{15}
```

Equality of the two rates $`a=b`$ closes this interval and proves (3). For $`a<b`$, the interval is an unresolved gap. The local Gaussian threshold suggests a sharper possible coefficient, but the upper bound does not prove it and no universal formula is asserted.

## 3. Classical capacity without covariance

The coherent-state orbit obeys $`\int|v\rangle\langle v|\,d\Omega=I/d`$. The channel $`\Phi_{D,t}`$ is unital, so the average output of the uniform coherent ensemble remains $`I/d`$ even though individual output entropies depend on $`v`$. Its Holevo information is therefore

```math
\chi=\log_2d-\int S(\Phi_{D,t}(|v\rangle\langle v|))\,d\Omega.
```

The Heisenberg generator on the spin vector is

```math
\mathcal L_D^\dagger(\boldsymbol J)=-A\boldsymbol J,
\qquad A=(\operatorname{Tr}D)I_3-D.
```

For the coherent state at $`v`$, the nonnegative integer-valued excitation operator $`N_v=j-v\cdot\boldsymbol J`$ has output mean

```math
m_v=j[1-v^Te^{-tA}v]
\le jt\,v^TAv
=\frac{\tau}{2}[\operatorname{Tr}D-v^TDv].
\tag{16}
```

The entropy of any state on the finite ladder $`0,\ldots,n`$ with mean excitation $`m`$ is at most $`g(m)`$: embed it in the oscillator number ladder and apply the Gibbs variational bound, or dephase in that basis and maximize the resulting distribution entropy. No diagonality of the original output is needed.

Since $`g`$ is increasing and concave,

```math
\int S(\Phi_{D,t}(|v\rangle\langle v|))\,d\Omega
\le g\!\left(j\left[1-\tfrac13\operatorname{Tr}(e^{-tA})\right]\right)
\le g\!\left(\frac{nt\operatorname{Tr}D}{3}\right).
\tag{17}
```

Here the average of $`v^TDv`$ is $`\operatorname{Tr}D/3`$. Combining (17) with $`\chi`$ proves (4), because the Holevo information of any fixed ensemble is achievable in independent-use classical communication. The sharper first expression in (17) is also an exact finite-$`n`$ bound.

A simpler uniform bound,

```math
C\ge\log_2d-g[\tau(b+c)/2],
```

is valid as well. Averaging before applying $`g`$ yields (4), which is at least as strong because $`\operatorname{Tr}D/3\le(b+c)/2`$.

The smallest eigenvalue of $`e^{-tA}`$ is $`e^{-(b+c)t}`$, so (16) also gives the stated polarization retention. At fixed $`\tau`$ and fixed $`D`$, nearly maximal classical communication and nearly unchanged mean polarization coexist with the channel's $`O(1/n)`$ proximity to EB.

## 4. Logical encoding and quantum-capacity consequences

Let $`E:\mathcal B(\mathbb C^k)\to\mathcal B(\mathcal H_j)`$ and $`R:\mathcal B(\mathcal H_j)\to\mathcal B(\mathbb C^k)`$ be arbitrary CPTP encoding and recovery maps, with no noiseless quantum bypass. When $`nat\ge1`$, replace $`\Phi_{D,t}`$ by the EB comparator from Section 1. Composing $`R`$ with that comparator and $`E`$ gives an EB channel, and its maximally entangled overlap is at most $`1/k`$. Contractivity of half-diamond distance therefore gives

```math
F_e(R\circ\Phi_{D,t}\circ E)\le\frac1k+\frac{K_0}{n}.
\tag{18}
```

For independent uses, [Leung–Smith's finite-output-dimension continuity bound](../references/RELATED_WORK.md#entanglement-breaking-continuity-and-the-limits-of-the-conclusion) applies to the full diamond error $`\epsilon\le2K_0/n<4.8/n`$. Their Corollary 14, equation (29), bounds the quantum-capacity difference by $`8\epsilon\log_2d+4h_2(\epsilon)`$. For sufficiently large $`n`$, this proves (5). No interchange of the regularization in the number of channel uses with the limit $`n\to\infty`$ is required.

Primary continuity source: [Leung and Smith, *Continuity of quantum channel capacities*](https://arxiv.org/html/0810.4931v2).

The lower bound in Section 2 is a statement about distance from EB and surviving reference entanglement. It does not prove positive unassisted quantum capacity for every $`\tau`$ below the boundary. Exact EB at finite $`n`$ is also not asserted.

## 5. Deterministic Hamiltonian rotations and time-dependent rates

Let

```math
H(t)=\boldsymbol h(t)\cdot\boldsymbol J,
\qquad
\mathcal G_t=-i[H(t),\cdot]+\mathcal L_{D(t)},
```

with deterministic, locally integrable coefficients. The adjoint Casimir commutes with every linear Hamiltonian rotation as well as every quadratic diffusion generator. Write $`\alpha(t)=\lambda_{\min}(D(t))`$ and

```math
\kappa(T)=\int_0^T\alpha(s)\,ds.
```

Factoring the central Casimir out of the time-ordered propagator gives exactly

```math
\Phi_{[0,T]}=\Phi_{I,\kappa(T)}\circ\Psi_{[0,T]},
\tag{19}
```

where $`\Psi`$ is the CPTP propagator generated by the same Hamiltonian plus the diffusion matrix $`D(t)-\alpha(t)I`$. Thus

```math
n\kappa(T)\ge1
\quad\Longrightarrow\quad
\inf_{\Psi_{\mathrm{EB}}}\tfrac12\|\Phi_{[0,T]}-\Psi_{\mathrm{EB}}\|_\diamond
\le K_0/n.
\tag{20}
```

This upper statement allows arbitrarily strong deterministic rotations, including strengths depending on $`n`$, provided the time evolution is well-defined. It does not extend by this proof to nonlinear spin Hamiltonians, because those need not commute with the adjoint Casimir.

### Lower bound with bounded rotation rates

For fixed constant $`D`$ and a Hamiltonian vector $`\boldsymbol h(t)`$ bounded near $`t=0`$ independently of $`n`$, remove its deterministic unitary by an interaction picture. On $`T=\tau/n`$, the corresponding three-dimensional rotation is $`I+O(1/n)`$, so the rotated noise matrix has the same local Gaussian limit $`\tau D`$. Output unitary conjugation leaves distance to EB unchanged. Therefore the lower bound (2) remains valid, and the sharp $`a=b`$ family remains sharp in the presence of such rotations.

### Classical capacity during deterministic rotations

The classical lower bound also survives time-dependent deterministic rotations. Remove the final known unitary. Let $`R_H(t)`$ be the three-dimensional rotation generated by the deterministic Hamiltonian. The interaction-frame diffusion matrix is $`\widetilde D(t)=R_H(t)^T D(t)R_H(t)`$; this rotation preserves its trace and positive semidefiniteness. Let $`M(t)`$ be the real matrix that evolves mean spin in that frame:

```math
\dot M=-A(t)M,\qquad M(0)=I,
\qquad A(t)=(\operatorname{Tr}D(t))I-\widetilde D(t)\ge0.
```

Euclidean contraction gives $`\|M(t)\|_{\mathrm{op}}\le1`$. The average coherent-state excitation relative to its initial pole is $`j[1-\operatorname{Tr}M(T)/3]`$. Since

```math
3-\operatorname{Tr}M(T)
=\int_0^T\operatorname{Tr}[A(s)M(s)]\,ds
\le\int_0^T\operatorname{Tr}A(s)\,ds
=2\int_0^T\operatorname{Tr}D(s)\,ds,
```

the same uniform ensemble and Jensen argument prove

```math
C(\Phi_{[0,T]})\ge\log_2(n+1)
-g\!\left(\frac n3\int_0^T\operatorname{Tr}D(s)\,ds\right).
\tag{21}
```

The trace inequality uses $`|\operatorname{Tr}(AM)|\le\operatorname{Tr}(A)\|M\|_{\mathrm{op}}`$ for $`A\ge0`$; $`M`$ need not be symmetric. Therefore the capacity proof does not assume commuting instantaneous anisotropies.

## 6. Limits of the robustness claim

1. **Fixed positive anisotropy matters.** For a fixed $`D>0`$, the EB upper bound has no condition-number prefactor, and the classical deficit at $`\tau=1/a`$ remains the finite constant $`g(\operatorname{Tr}D/(3a))`$. If $`a`$ depends on $`n`$ and tends to zero, that deficit can grow, and the advertised fixed-anisotropy separation must be reassessed.
2. **Rank-deficient noise has a different limit.** The lower-bound proof remains valid for $`D\ge0`$. If $`a=0`$, the pole along the largest-eigenvalue axis has tangent rates $`0,b`$ and gives the strictly positive lower bound $`1/[2(1+\tau b)^{3/2}]`$ for every finite $`\tau`$. Thus bounded-rate rotations do not produce asymptotic EB proximity at any fixed inverse-spin time under rank-deficient $`D`$. No claim about its longer timescale is made here.
3. **Irreducibility is essential.** Collective noise on the full tensor product of distinguishable spins has noiseless multiplicity spaces. They are absent from $`\mathcal H_j`$ and are outside this theorem.
4. **Uses must be independent for capacities.** A common rotation applied jointly to many carriers is a different communication channel. Equations (5) and (18) do not rule out relational or multiplicity encodings in that model.
5. **No active intermediate correction.** Encoding and recovery at the two ends are unrestricted, but intervention with noiseless ancillas during the interval is not part of this channel model.
6. **No universal anisotropic coefficient is proved.** For $`a<b`$ the gap in (15) is open. Closing it would require a stronger global EB approximation than the isotropic Casimir factorization, not simply the local Gaussian argument.

## 7. Focused finite-spin check

[The anisotropic verification](../verification/README.md) builds the exact finite-spin double-commutator generator as a sparse superoperator and exponentiates it on the four matrix units needed for the Bell partial-transpose block. This supplies a finite-size check of the anisotropic lower formula using an independent formula for the exact channel, including a diffusion matrix with longitudinal–transverse cross terms. It does not attempt to compute the diamond distance or certify an unproved threshold. The analytic arguments above establish the theorem.

The completed run gives the following smallest eigenvalues of that $`2\times2`$ partial-transpose block:

| Diffusion and $`\tau`$ | $`n=16`$ | $`n=32`$ | $`n=64`$ | Proved limit |
|---|---:|---:|---:|---:|
| $`\operatorname{diag}(1,2,5)`$, $`\tau=0.5`$ | $`-0.0248990`$ | $`-0.0361314`$ | $`-0.0420206`$ | $`-0.0481125`$ |
| $`\operatorname{diag}(1,1,5)`$, $`\tau=0.8`$ | $`0.0015970`$ | $`-0.0138792`$ | $`-0.0221729`$ | $`-0.0308642`$ |
| $`D`$ with cross terms, $`\tau=0.5`$ | $`-0.0275724`$ | $`-0.0388456`$ | $`-0.0447486`$ | $`-0.0508486`$ |
| $`\operatorname{diag}(0,1,3)`$, $`\tau=2`$ | $`-0.0079839`$ | $`-0.0426074`$ | $`-0.0657619`$ | $`-0.0962250`$ |

The cross-term matrix has rows $`(1,0.3,0.4)`$, $`(0.3,2,0.2)`$, $`(0.4,0.2,5)`$, with pole along the third coordinate. All four sequences approach the predicted constants. The positive $`n=16`$ value in the axial example is an expected finite-size limitation of this witness; the theorem is a lower bound at fixed rates as $`n\to\infty`$ and does not claim that the witness detects entanglement for every finite $`n`$. Full values, commands and numerical residuals are available in the [verification record](../verification/README.md).
