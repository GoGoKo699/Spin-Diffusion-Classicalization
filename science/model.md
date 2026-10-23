# Spin diffusion and operational classicality

[Scientific route](README.md) · [Sharp threshold](classicalization.md) · [Communication](communication.md)

## The physical question

A large spin can serve as a compass: different directions encode distinguishable classical messages. Its Hilbert space also permits superpositions and quantum encodings. Rotational noise need not erase these two forms of information on the same timescale.

The question here is whether an encoding anywhere in that growing Hilbert space can avoid classicalization. Looking only at a spin's average direction or a fixed collection of multipole moments cannot answer it. We therefore compare entire channels, including their action on states entangled with an arbitrary external reference.

## One irreducible carrier

Let $`j=n/2`$, where $`n`$ is a positive integer, and let $`\mathcal H_j`$ be the single irreducible spin-$`j`$ representation of dimension $`d=n+1`$. Set $`\hbar=1`$. The angular-momentum operators satisfy

```math
[J_a,J_b]=i\sum_c\epsilon_{abc}J_c,
\qquad
J_x^2+J_y^2+J_z^2=j(j+1)I.
```

The noise channel is

```math
\Phi_t^{(j)}=\exp(-t\mathcal C_j),
\qquad
\mathcal C_j(X)=\sum_{a=x,y,z}[J_a,[J_a,X]],
\qquad t\ge0.
```

The map is completely positive, trace preserving, unital and rotation covariant. Equivalently, it averages conjugation by random rotations whose distribution is the heat kernel on $`\mathrm{SO}(3)`$. For half-integer $`j`$, the representation on $`\mathrm{SO}(3)`$ is projective, but conjugation by it is well-defined.

For a physical master equation

```math
\frac{d\rho}{ds}=\gamma\sum_a\mathcal D[J_a](\rho),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\},
```

the dimensionless time used throughout this account is $`t=\gamma s/2`$. The operational boundary $`t=1/(2j)`$ therefore corresponds to $`s=1/(\gamma j)`$. A different generator normalization changes that conversion, not the statements in dimensionless time.

Under conjugation, the operator space decomposes into integer tensor ranks $`\ell=0,\ldots,n`$. On any rank-$`\ell`$ tensor $`T_{\ell m}`$,

```math
\Phi_t^{(j)}(T_{\ell m})
=e^{-t\ell(\ell+1)}T_{\ell m}.
```

In particular, the first moment decays by $`e^{-2t}`$. This spectrum is established spin-diffusion theory; see [Denis–Martin and Brody–Graefe–Melanathuru](../references/RELATED_WORK.md).

## A channel distance that includes every encoding

A channel $`\mathcal E`$ is **entanglement breaking** (EB) when applying it to either part of any bipartite state produces a separable state across the output/reference split. Equivalently, it can be implemented by a measurement followed by state preparation. The equivalence is an imported characterization from [Horodecki–Shor–Ruskai](../references/RELATED_WORK.md#entanglement-breaking-continuity-and-the-limits-of-the-conclusion).

For a difference of channels, the diamond norm is

```math
\|\mathcal N-\mathcal M\|_\diamond
=\sup_{\rho_{RA}}
\|(\operatorname{id}_R\otimes(\mathcal N-\mathcal M))(\rho_{RA})\|_1.
```

A reference of dimension equal to the input dimension suffices. Our distance uses one half of this norm:

```math
e_j(t)=\inf_{\mathcal E\in\mathrm{EB}}
\frac12\|\Phi_t^{(j)}-\mathcal E\|_\diamond,
\qquad
\nu=nt=2jt.
```

The factor of one half agrees with trace distance and total variation. Thus $`0\le e_j(t)\le1`$. The infimum ranges over all EB channels with the same input and output spaces, without a covariance restriction.

This norm controls every initial state, every external reference, and every encoding and final recovery applied before and after the noise interval. It is stronger than convergence of each fixed multipole or the separability of particular spin states.

## Central statements

**Theorem 1 — Sharp operational threshold.** For every $`n\ge1`$ and every $`\nu\ge1`$,

```math
e_{n/2}(\nu/n)\le \min\{1,2.4/n\}.
```

For each fixed $`0\le\nu<1`$,

```math
\liminf_{n\to\infty}e_{n/2}(\nu/n)
\ge\frac{1-\nu}{2(1+\nu)^2}>0.
```

Consequently $`\nu=1`$ is the exact boundary between fixed scaled times where proximity to the EB set vanishes and fixed scaled times where it stays bounded away from zero. [The full proof](classicalization.md) includes an explicit EB comparator and a two-level encoded witness.

**Theorem 2 — Communication separation.** At fixed $`\nu\ge1`$,

```math
Q(\Phi_{\nu/n}^{(j)})
=O\!\left(\frac{\log n}{n}\right),
\qquad
C(\Phi_{\nu/n}^{(j)})
\ge\log_2(n+1)-g(\nu),
```

where $`g(x)=(x+1)\log_2(x+1)-x\log_2x`$, with $`g(0)=0`$. At $`\nu=1`$, the classical deficit is at most two bits, while polarization retention is $`e^{-2/n}`$. These are the ordinary unassisted capacities per independent channel use. [The communication proof](communication.md) also gives finite-size bounds and a one-carrier recovery converse.

The [anisotropic result](anisotropic_diffusion.md) extends these conclusions to unequal diffusion strengths, with a sharp boundary when the two smallest strengths coincide. The [residual-entanglement result](residual_entanglement.md) shows why approximate EB and exact entanglement death differ.

## Which resources are covered

An encoding is a CPTP map from a logical system to $`\mathcal H_j`$; a recovery is a CPTP map from $`\mathcal H_j`$ back to that system. Local ancillary systems used to implement those maps are permitted. A quantum system that carries information untouched from the encoder to the decoder is an additional channel and is outside this model. Arbitrary quantum states of an external reference are permitted in testing the channel.

Encoding and recovery occur before and after the diffusion interval. Continuous active error correction during that interval changes the effective channel and is a separate control problem.

A symmetric sector of $`n`$ spin-$`1/2`$ particles realizes $`\mathcal H_j`$. The full tensor-product space is reducible and has multiplicity subsystems on which a collective rotation acts trivially. Those subsystems are genuine ways of preserving quantum information, and are excluded by the irreducible-carrier assumption.

For capacities, different uses undergo independent draws of the channel. A common unknown rotation applied to an entire block of carriers is correlated noise and permits different relational encodings.

## Interpretation of sharpness

The theorem is sharp for the stated distance-to-EB criterion. For each fixed $`\nu<1`$, the subthreshold witness proves that entanglement survives for sufficiently large $`n`$; it does not determine the unassisted quantum capacity throughout that interval. Likewise, an $`O(1/n)`$ EB approximation does not make a finite-$`n`$ channel exactly EB. The residual-entanglement theorem makes this distinction quantitative.

All asymptotic statements specify which parameters are fixed. No result assumes that an approximate equality in a weak phase-space norm automatically holds in diamond norm.

