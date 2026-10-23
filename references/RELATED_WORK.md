# Related work and source map

Sources and versions checked on 23 October 2026. Citation keys refer to `references.bib`. This record distinguishes established ingredients from the estimates and operational consequences developed in the accompanying analysis. It does not certify priority over all literature.

## Setting and scope

The channel acts on one irreducible spin-$`j`$ representation, with $`n=2j`$, $`d=n+1`$, and

```math
\Phi_{j,t}=\exp\!\left[-t\sum_{a=x,y,z}[J_a,[J_a,\cdot]]\right],
\qquad \nu=nt.
```

The question concerns preservation of entanglement with an external reference, uniformly over encodings into this single spin. Classical and quantum capacities concern independent uses of this channel. Intermediate error correction, extra noiseless storage, and multiplicity spaces in a reducible collective-spin representation are outside this setting. In particular, results for one irreducible spin do not rule out decoherence-free subsystems of a larger register.

## Established ingredients and the contribution of this analysis

| Ingredient or conclusion | Source and status | Distinction needed here |
|---|---|---|
| Isotropic spin diffusion and multipole decay $`e^{-t\ell(\ell+1)}`$ | Established; [DenisMartin2022], [Bardet2021], and the same generator in [Gross2021]. | The model and its inverse-spin semiclassical scale are not introduced here. |
| Coherent-state measurement followed by preparation is entanglement breaking | Standard measure-and-prepare characterization [HorodeckiShorRuskai2003]. | Entanglement breaking of the comparator is an imported fact. |
| Exact Berezin multipliers and a positive central random-rotation kernel for the comparator | Imported from [Aschieri2024], published Lemmas 12–13 and Eqs. (3.11)–(3.18). | The exact kernel identity must be cited, not presented as a new construction. |
| Berezin transform approximates heat flow | Uniform Sobolev-operator estimate already proved in [Ioos2020], Proposition 3.9, Eq. (3.30); spin measurement/diffusion comparison in [Brody2026]. | Neither the heat analogy nor norm approximation in general is new. The norm, domain, and ancillary-system uniformity matter. |
| Classical group kernels control quantum-channel distances | Established transference framework [Bardet2021], especially Sections III and IV.C. | The elementary total-variation-to-diamond transfer is not itself the new step. |
| At $`t=1/n`$, the spin diffusion channel is within $`O(n^{-1})`$ in diamond norm of the coherent measure-and-prepare channel | Estimate derived in the accompanying analysis, using the imported central kernel and a shrinking-time heat-kernel comparison. | The bound is uniform over input states and arbitrary reference systems despite growing spin dimension. |
| For every fixed $`0\leq\nu<1`$, distance from all entanglement-breaking channels remains bounded below | Derived from the two-level north-pole encoding and a partial-transpose witness in the accompanying analysis. | This supplies the lower side of the asymptotic channel-classicalization threshold; it does not establish a positive quantum-capacity threshold. |
| Bounds for every encoding and final recovery, and $`Q=O(\log n/n)`$ above threshold | Consequences of the uniform estimate, the standard entanglement-breaking fidelity bound, and capacity continuity [LeungSmith2009]. | The general continuity theorem is imported; its shrinking-time application to this spin family is derived. |
| $`C\geq\log_2(n+1)-g(\nu)`$, where $`g(x)=(x+1)\log_2(x+1)-x\log_2x`$ | Coherent-ensemble calculation in the accompanying analysis; uses covariance and the standard entropy bound at fixed mean occupation. | This retains nearly maximal classical information at the same scale where the quantum upper bound vanishes. |
| Singlet eigenvalue of the partially transposed heat-channel Choi state and its odd-$`n`$ asymptotics | Specialization derived in the accompanying analysis. The SU(2) partial-transpose multiplet method is established [Schliemann2003]. | This distinguishes exact residual entanglement from operational distance to entanglement breaking; it does not determine the full PPT or entanglement-breaking time. |

For rotations represented in $`SU(2)`$, the coherent comparator kernel has peaks at both central elements. A heat-kernel comparison must therefore use the corresponding $`SO(3)`$ kernel or the correctly symmetrized $`SU(2)`$ kernel. Conjugation is insensitive to the sign of the representing group element. This normalization issue is part of the estimate, not a change to the imported identity.

## Closest analytical and physical predecessors

### Exact coherent-channel kernel: Aschieri, Ruba, and Solovej

[Aschieri2024] gives quantitative semiclassical analysis of $`SU(2)`$-equivariant channels. Published Lemma 12 gives the Berezin eigenvalues. Lemma 13 gives the exact random-rotation representation of $`\operatorname{Op}_J H_J`$, with central density proportional to $`\cos^{4J}\alpha`$ when the eigenvalues of the group element are $`e^{\pm i\alpha}`$. Equations (3.14)–(3.18), including the normalization and character expansion, are the source of the comparator kernel used here. Theorem 5 also supplies quantitative Schatten-norm semiclassical estimates for channels with input/output spins $`J,K`$; its generic $`J^2/K`$ scale must not be represented as the equal-spin diamond estimate used here.

The additional analysis compares this known central probability density with heat flow at $`t=1/(2j)`$, with a dimension-uniform total-variation remainder. The operational coding bound then follows from that estimate. The published paper, rather than only its preprint, should be cited for lemma numbering.

Primary text: <https://link.springer.com/article/10.1007/s00220-024-05178-1>. Preprint record: <https://arxiv.org/abs/2404.04133> (v1, 5 April 2024); publication: 23 November 2024.

### Uniform Berezin–heat comparison: Ioos, Kaminker, Polterovich, and Shmoish

[Ioos2020], Proposition 3.9, Eq. (3.30), proves on its compact geometric quantization setting that, for each Sobolev order $`m`$,

```math
\big\|\big(e^{-\Delta/(4\pi p)}-B_p\big)f\big\|_{H^m}
\leq \frac{C_m}{p}\,\|f\|_{H^m}.
```

This is a uniform operator-norm estimate on functions, not merely convergence for each fixed multipole or smooth observable. Its proof directly compares the relevant kernels. It is therefore a substantial analytical predecessor to the shrinking-time comparison. The present operational statement requires a quantum-channel diamond estimate uniform in arbitrary reference systems. A Sobolev norm on scalar phase-space functions does not by itself identify that norm or provide a dimension-independent conversion to it. The exact central group representation supplies the direct route used here.

Primary published text: <https://www.numdam.org/item/10.5802/ahl.63.pdf>, pp. 1357–1358 for Proposition 3.9 and its proof. DOI: <https://doi.org/10.5802/ahl.63>.

### Group transference, collective decoherence, and capacities: Bardet et al.

[Bardet2021] develops transference from classical group Markov kernels to quantum semigroups, including norms with ancillary systems, entropies, capacities, and entanglement-breaking times. Section IV.C identifies strong collective decoherence of qubits with heat flow on $`SU(2)`$, subject to its generator convention. Section V bounds capacities by comparison with the limiting conditional expectation. Theorem V.4 bounds the exact entanglement-breaking time of a primitive transferred semigroup by $`t(d^{-1})`$, using convergence toward the fully depolarizing channel and a separable neighborhood of its Choi state. Section V.F also discusses the remaining capacity of decoherence-free subsystems.

Here the comparator at the shrinking time is a spin-dependent coherent measure-and-prepare channel, which retains substantial classical information. It is not the long-time fully depolarizing channel. The new calculation therefore needs its own localized kernel estimate and matching lower witness. Neither group-to-channel transference nor capacity bounds for collective decoherence should be claimed as new.

Primary author text: <https://arxiv.org/html/1904.11043v2>. Version record: <https://arxiv.org/abs/1904.11043> (v2, 4 June 2021, close to the published version). DOI: <https://doi.org/10.1109/TIT.2021.3065452>.

### Spin phase-space measurements and diffusion: Brody, Graefe, and Melanathuru

[Brody2026] directly compares isotropic angular-momentum Lindblad dynamics with repeated coherent-state phase-space measurements. It gives both spectra and explains their fixed-multipole large-spin agreement, while distinguishing their finite-spin dynamics. Its discussion also distinguishes density-matrix decoherence from positivity of a spin quasiprobability distribution. Equations (27)–(32) and Section IV are especially close to the comparator and scaling used here.

The physical connection between angular diffusion and coherent-state measurement is therefore explicit prior work. The distinction addressed here is operational uniformity over all states, references, and encodings, together with a matching below-threshold witness and a classical/quantum capacity separation. Fixed-multipole agreement cannot alone control encodings whose structure changes with spin. A diamond approximation also does not assert equality of the two finite-spin dynamics or equivalence of their quasiprobability criteria.

Primary text: <https://arxiv.org/html/2605.02696v1>. Record: <https://arxiv.org/abs/2605.02696>. As checked on 23 October 2026, the record lists only v1, submitted 4 May 2026, with no journal reference. Its preceding flat-phase-space study is [Brody2025].

### Depolarization and internal symmetric-qubit entanglement: Denis and Martin

[DenisMartin2022] studies isotropic and anisotropic depolarization of a spin and uses the equivalent symmetric sector of $`N=2j`$ qubits to analyze entanglement decay. Equation (55) gives the isotropic multipole dynamics. Section IV.E and the relevant figures investigate nonpositive-partial-transpose survival and positive-$`P`$ times, including inverse-spin scaling for studied families.

The timescale $`1/j`$, anisotropic spin diffusion, and fast loss of spin-state nonclassicality are established context. The bipartition must nevertheless be kept explicit. Entanglement among constituent qubits in the symmetric representation is different from entanglement between the entire physical spin and an external reference. The latter is the criterion needed for entanglement-breaking channels and arbitrary-code communication bounds.

Primary published text: <https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.4.013178>. Publication: 4 March 2022.

## Relation to spin error-correcting codes

[Gross2021] encodes a logical qubit in a single large spin. Its Eq. (9) uses

```math
\frac{d\rho}{ds}=\gamma\sum_a\left(J_a\rho J_a-\tfrac12\{J_a^2,\rho\}\right)
=-\frac{\gamma}{2}\sum_a[J_a,[J_a,\rho]],
```

so its physical time $`s`$ corresponds exactly to $`t=\gamma s/2`$ in the convention above. Its leading Kraus operators describe the small-rotation error set corrected by the designed codes. This supplies a direct motivation for asking when *any* code followed by a final recovery is limited under accumulated noise of this form. The result here does not prohibit correction of sufficiently small errors or repeated active recovery during the interval.

Primary author copy: <https://jarthurgross.name/docs/papers/gross_designing_2021.pdf>. Published title and metadata: <https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.010504>. The 21 May 2020 preprint, arXiv:2005.10910v1, has the earlier title *Encoding a qubit in a spin*; use the published title in the bibliography.

[OmanakuttanVolkoff2023] constructs spin analogues of Gottesman–Kitaev–Preskill codes through a quantum central-limit correspondence and compares optimal recovery under stochastic relaxation and isotropic ballistic dephasing. Its Eq. (21) averages a Gaussian-distributed rotation angle and a uniform rotation axis. That distribution is not the compact-group Brownian heat kernel. Its numerical code comparisons therefore motivate the broader spin-code question without being an identical noise-model theorem.

Primary text: <https://arxiv.org/pdf/2211.05181>. Version record: <https://arxiv.org/abs/2211.05181> (v2, 19 June 2023); publication: <https://journals.aps.org/pra/abstract/10.1103/PhysRevA.108.022428>, 28 August 2023.

## Entanglement breaking, continuity, and the limits of the conclusion

The equivalence between a measure-and-prepare representation, entanglement breaking, and separability of the channel's Choi state is standard [HorodeckiShorRuskai2003, Theorem 4]. General results on eventual entanglement breaking for Markovian dynamics are given in [Hanson2020]. These results concern exact entanglement breaking and characteristic-time estimates; the approximation studied here need not coincide with the exact finite-spin entanglement-breaking time.

[LeungSmith2009] provides the finite-output-dimension continuity theorem used to turn a diamond-distance estimate into an upper bound on unassisted quantum capacity. The dimension factor must be retained as the spin grows. An $`O(1/n)`$ estimate therefore yields the stated $`O(\log n/n)`$ conclusion. This argument alone does not establish an analogous continuity-at-zero result for two-way assisted quantum capacity, or identify a sharp quantum-capacity threshold below $`\nu=1`$.

Primary records: <https://arxiv.org/abs/quant-ph/0302031> (v2, 4 June 2003; arXiv record title differs from the PDF/published title), <https://link.springer.com/article/10.1007/s00023-020-00906-4>, and <https://arxiv.org/abs/0810.4931> (v2, 18 February 2009).

## SU(2)-covariant Choi structure: Rudnicki et al.

[Rudnicki2026] develops the covariant Choi and Kraus structure. Equations (13)–(19) use partial time reversal and angular-momentum sectors; the method explicitly follows Breuer, *Physical Review A* **71**, 062330 (2005). Equation (38) connects Choi-sector coefficients with multipole attenuation through a $`6j`$ transform. Equations (50)–(51) give the same isotropic Lindbladian and its multipole decay, in the convention $`-(\gamma/2)\sum_a[J_a,[J_a,\cdot]]`$.

Sections 3–7 were inspected in a public copy explicitly supplied by MDPI on ResearchGate. Their conclusions concern representation structure, state-survival fidelity, and Wigner-function smoothing. This inspected text does not state the shrinking-time singlet-sign asymptotic, a uniform diamond approximation to an entanglement-breaking channel, or the classical/quantum capacity separation developed here. General partial-transpose and Choi-sector methods are nevertheless established background.

Publisher and MPG endpoints remained unavailable. Publisher notes list first publication on 5 July 2026 and file updates on 9 July; the accessible copy's exact update stamp could not be independently matched. Initial full-text access limitations were thus resolved for the substantive comparison, with that version qualification.

Publisher-provided text: <https://www.researchgate.net/publication/408495460_SU2-Covariant_Quantum_Channels>. Publisher: <https://www.mdpi.com/2073-8994/18/7/1146>. Version notes: <https://www.mdpi.com/2073-8994/18/7/1146/notes>. DOI: <https://doi.org/10.3390/sym18071146>.

## Partial transpose and residual Choi entanglement

[Schliemann2003], Section II, explains the multiplet structure of partial transposes of SU(2)-invariant bipartite spin states. Equations (1)–(2) and the following argument identify the conjugate representation and show that the partial transpose acts as a scalar on its irreducible sectors. This is established representation-theoretic background for resolving Choi partial-transpose sectors, rather than a method introduced here.

For the normalized heat-channel Choi state, the accompanying analysis derives the singlet specialization

```math
\lambda_0(j,t)=\frac{1}{(n+1)^2}
\sum_{\ell=0}^{n}(-1)^\ell(2\ell+1)e^{-t\ell(\ell+1)}.
```

Along odd $`n`$, at fixed $`0<\nu<\pi/2`$ and $`t=\nu/n`$, the derived asymptotic is

```math
\lambda_0(j,\nu/n)\sim
-\frac{e^{-2\nu}}{\cosh\nu}\frac{e^{-\nu n}}{n}.
```

Thus, for fixed $`1\leq\nu<\pi/2`$ and sufficiently large odd $`n`$, an exact nonpositive-partial-transpose witness coexists with a vanishing operational distance to the entanglement-breaking set. The negative eigenvalue is exponentially small. This is not an exact PPT/entanglement-breaking-time determination or a lower bound on quantum communication capacity. The structural comparison with [Rudnicki2026] is given above.

Primary author text: <https://arxiv.org/html/quant-ph/0212114v3>. Version record: <https://arxiv.org/abs/quant-ph/0212114> (v3, 12 July 2003); publication: <https://journals.aps.org/pra/abstract/10.1103/PhysRevA.68.012309>, 11 July 2003. The generated HTML date is not the paper's publication or revision date.

Anisotropic thresholds are another separate statement. Anisotropic spin dynamics already appears in [DenisMartin2022]; any sharp coefficient or general sandwich bound must be justified by its own derivation and its exact ordering assumptions on the diffusion coefficients.
