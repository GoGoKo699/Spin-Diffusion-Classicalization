# Physical meaning and boundaries

[Scientific route](README.md) · [Precise model](model.md) · [Communication bounds](communication.md)

## A good classical carrier can be a poor quantum carrier

A coherent spin state occupies an angular region whose width is proportional to $j^{-1/2}$. At time $t=1/(2j)$, rotational Brownian motion has a typical angle of the same order. The mean direction changes only by a relative factor $1-e^{-1/j}$, yet the entire channel can be simulated, to vanishing error, by a coherent-state measurement followed by preparation.

The quantitative reason is the comparison of two probability distributions on the rotation group. The known random-rotation distribution for coherent measurement and the shrinking-time heat kernel differ by $O(1/j)$ in total variation. This comparison is independent of the size of the representation and therefore includes highly nonclassical input states.

A fixed collection of low multipoles would miss the question of whether an unusual encoding hides quantum information in the rest of the growing Hilbert space. The diamond-norm theorem settles that question under the stated carrier and control model.

## Why the classical rate stays high

The sphere contains an increasing number of distinguishable coherent-state directions. Diffusion at the boundary adds only a bounded mean number of excitations relative to the input direction. The output entropy of each coherent message is therefore bounded by two bits, whereas the entropy of the average message grows as $\log_2(2j+1)$.

This is the source of the capacity separation. High polarization alone would not prove it; the entropy and coding argument is essential.

## Why exact entanglement can survive

Being close to an EB channel and belonging exactly to the EB set are different properties. The [finite-spin Choi analysis](residual_entanglement.md) identifies a negative partial-transpose eigenvalue for sufficiently large half-integer spins at every fixed $1\le\nu<\pi/2$. Its magnitude is exponentially small in $n=2j$.

This result concerns one identified eigenvalue. It does not establish that every entanglement measure, every negative eigenvalue, or the exact distance to the EB set is exponentially small. The uniform theorem bounds the latter distance by $O(1/n)$.

The coexistence explains why a search for the exact finite-dimensional EB time would answer a different question from an operational approximation theorem.

## Imperfect isotropy

The [anisotropic analysis](anisotropic_diffusion.md) retains a uniform upper bound after extracting the smallest isotropic noise component. A local encoded witness gives a complementary lower bound.

When the two smallest diffusion strengths agree, both sides meet. Noise about the remaining axis may be stronger, so exact equality of all three strengths is unnecessary. For three distinct positive strengths the proven bounds form a bracket; an exact coefficient is not asserted.

The model still assumes Markovian rotational diffusion with fixed diffusion strengths. The results do not automatically transfer to ballistic static disorder, non-Markovian fluctuations, a joint unknown rotation shared across all uses, or arbitrary control during the storage interval.

## Where another encoding can escape

One irreducible spin is the relevant resource. In a reducible collection of spins, collective rotations act on representation factors while leaving multiplicity factors unchanged. Encoding into those factors is outside the theorem and can preserve quantum information.

Likewise, a protected ancillary memory, an extra quantum communication path, or intermediate error correction changes the resource model. The one-carrier fidelity converse permits arbitrary preparation and final recovery, but does not grant free protection during the interval.

These boundaries determine the claim's application to large-spin memories. A spin-code construction in the same passive-storage model is constrained regardless of its codeword geometry. A code that uses a different noise model or additional protected resources requires its own comparison.

## Established ingredients and the contribution

The coherent-measurement identity, semiclassical Berezin/heat correspondence, transfer of classical kernel estimates to complete quantum norms, and capacity-continuity theorem come from existing literature. The inverse-spin timescale also has precedents in studies of internal spin-state entanglement.

The result established here is the sharp operational boundary for a growing irreducible carrier, with a matching finite-level witness and a simultaneous communication separation. The anisotropic bracket and residual-NPT result delimit that statement. [The related-work account](../references/RELATED_WORK.md) compares the actual models and theorem scopes.

The analytical proofs establish the general statements. Numerical examples check normalization, finite-size behavior, and representation-theory identities; they do not certify priority or replace those proofs.

