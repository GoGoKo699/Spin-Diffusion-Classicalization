# Common map: 30 milestones for spin-diffusion classicalization

[Learning route](README.md) · [Source bridge](ANCHOR.md) · [Tutorial](TUTORIAL.md)

This map describes the project's common understanding targets. Its stable IDs are M01–M30. The first **12 milestones form the background/preliminaries phase**: they connect a physical spin, reference entanglement, noisy channels, probability, and communication into the question the research answers. The remaining **18 milestones form the narrative/innovation phase**: they assemble the comparator and converse, derive communication consequences, and integrate robustness, residual entanglement, and attribution. M12 and M30 synthesize their respective phases.

The selected educational anchor is Alexander S. Holevo, *Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition (2019), [DOI: 10.1515/9783110642490](https://www.degruyterbrill.com/document/doi/10.1515/9783110642490/html). Chapter pointers below are deliberately at chapter level: Chapter 3 supports composite systems, Chapter 6 evolutions and channels, Chapter 7 entropy, Chapter 8 classical capacity, Chapter 10 quantum transmission, and Chapter 12 the Gaussian setting. The Gaussian chapter supplies a useful comparison, not a derivation of compact-group Brownian motion or a claim that the entire spin channel is a Gaussian channel.

The [scientific account](../science/README.md) supplies the spin-specific definitions and proofs. The [source map](../references/RELATED_WORK.md) identifies imported research ingredients separately from the estimates derived here. Holevo supplies foundations; the book is not a source for this project's threshold, anisotropic bounds, or residual-NPT asymptotics. The milestones select the arguments needed for global understanding, with specialist calculations retained in the canonical science pages.

## Phase I — Background and preliminaries

### M01 — One irreducible spin as a growing carrier

**Phase:** Background/preliminaries.

**Central question:** What physical information carrier grows when the spin quantum number increases?

**Understanding target:** Identify the state space $`\mathcal H_j`$, the dimension $`d=2j+1=n+1`$, the angular-momentum observables, and the distinction between a state and its mean spin. Distinguish one irreducible spin from the full tensor product of $`n`$ distinguishable qubits, even when its symmetric sector realizes the same representation.

**Dependencies and story role:** No earlier milestone is required. This fixes the local physical object before adding noise, references, or coding resources.

**Conceptual connection:** A growing Hilbert space offers more possible encodings than a classical direction alone describes. The irreducibility assumption later determines which encodings the converse actually covers.

**Sources and anchor:** [Model: one irreducible carrier](../science/model.md#one-irreducible-carrier) and [covered resources](../science/model.md#which-resources-are-covered). Holevo, Chapter 3, supports the distinction between a system and a composite; the spin representation and its resource restriction are specified locally.

### M02 — An external reference makes quantum preservation observable

**Phase:** Background/preliminaries.

**Central question:** Why ask whether the entire spin remains entangled with another system?

**Understanding target:** Explain joint states, reduced states, separable states, and entangled states for a carrier and a reference. Distinguish spin–reference entanglement from entanglement among constituent qubits in a symmetric-spin representation. Recognize the reference as a way to test what the channel preserves, without granting a noiseless path from encoder to decoder.

**Dependencies and story role:** Builds on M01. It enlarges the description from one carrier to the correlations that a quantum transmission task must preserve.

**Conceptual connection:** The same spin marginal can occur in joint states with different correlations. Looking only at that marginal, or at its polarization, cannot establish preservation of quantum information.

**Sources and anchor:** [Model: a channel distance that includes every encoding](../science/model.md#a-channel-distance-that-includes-every-encoding), [resource conventions](../science/model.md#which-resources-are-covered), and [the comparison with internal spin entanglement](../references/RELATED_WORK.md#depolarization-and-internal-symmetric-qubit-entanglement-denis-and-martin). Holevo, Chapter 3, supplies the composite-system foundation.

### M03 — Physical channels, random rotations, and composition

**Phase:** Background/preliminaries.

**Central question:** What makes a mathematical evolution a valid noise channel, including on entangled inputs?

**Understanding target:** Explain complete positivity and trace preservation, the role of the untouched reference, and why an average of unitary conjugations is a channel. Distinguish unitality from covariance. Understand sequential channel composition and the semigroup property as the mathematical expression of accumulated Markovian noise.

**Dependencies and story role:** Uses M01–M02. It supplies the operations that later represent diffusion, measurement, encoding, and recovery within one framework.

**Conceptual connection:** A classical probability distribution over rotations defines a quantum channel. Composition will both extend a comparison to later times and transfer it through arbitrary encoders and decoders.

**Sources and anchor:** [Model: the diffusion channel](../science/model.md#one-irreducible-carrier) and [the complete-channel comparison](../science/classicalization.md#2-classical-probability-controls-the-complete-channel-norm). Holevo, Chapter 6, provides the evolution and channel framework; Chapter 3 supplies the reference-system setting.

### M04 — Coherent spin directions and their measurement

**Phase:** Background/preliminaries.

**Central question:** How can a quantum spin encode and measure a continuous classical direction?

**Understanding target:** Identify a coherent spin state as a rotated highest-weight state. Explain why coherent directions form an overcomplete family rather than an orthogonal basis, why their normalized orbit average is $`I/d`$, and how their resolution of the identity defines a POVM. Relate the angular width of a coherent state to the scale $`j^{-1/2}`$.

**Dependencies and story role:** Uses M01 and M03. It introduces the concrete states and measurement needed for both the comparator and the classical communication ensemble.

**Conceptual connection:** The same coherent-state orbit can serve as an alphabet, a measurement, and a preparation rule. Those different operational roles will connect classical information retention to entanglement breaking.

**Sources and anchor:** [Coherent-state measurement and identity resolution](../science/classicalization.md#1-an-established-measurement-channel) and [the physical angular scale](../science/interpretation.md#a-good-classical-carrier-can-be-a-poor-quantum-carrier). Holevo, Chapter 6, supports channels built from measurement and preparation; the spin-coherent construction is supplied by the project and its cited primary source.

### M05 — Diffusion acts differently on different multipoles

**Phase:** Background/preliminaries.

**Central question:** Why does preserving a spin's mean direction leave open the fate of other information?

**Understanding target:** Explain the double-commutator generator and the decomposition of operators into ranks $`\ell=0,\ldots,n`$. Interpret the decay factor $`e^{-t\ell(\ell+1)}`$, including identity preservation at $`\ell=0`$ and polarization retention $`e^{-2t}`$ at $`\ell=1`$. Keep the dimensionless time $`t`$ separate from physical time and its diffusion rate.

**Dependencies and story role:** Uses M01, M03, and M04. It connects the noise mechanism to observable decay and identifies why low-rank information is an incomplete diagnostic.

**Conceptual connection:** Higher tensor ranks become available as the carrier grows. Agreement on each fixed rank therefore need not control encodings whose structure changes with $`j`$.

**Sources and anchor:** [Model: generator, time convention, and tensor spectrum](../science/model.md#one-irreducible-carrier) and [spin measurement/diffusion predecessors](../references/RELATED_WORK.md#spin-phase-space-measurements-and-diffusion-brody-graefe-and-melanathuru). Holevo, Chapter 6, supplies the evolution framework; the angular-momentum spectrum is an established spin-specific ingredient.

### M06 — Rotation probability and the local Gaussian scale

**Phase:** Background/preliminaries.

**Central question:** How does diffusion on a compact rotation group acquire a Gaussian description at short times?

**Understanding target:** Distinguish a density relative to normalized Haar measure from its radial probability density. Understand central distributions, physical rotation angles, and the $`\sqrt t`$ width of Brownian motion. Recognize the Maxwell law as the radial law of a three-dimensional isotropic Gaussian, and distinguish a local limit from a uniform estimate on an entire probability distribution.

**Dependencies and story role:** Uses M03 and M05. It supplies the classical probability language needed before comparing the heat and coherent-measurement kernels.

**Conceptual connection:** At $`t\sim1/n`$, Brownian angular fluctuations and coherent-state angular width are comparable. This motivates the candidate scale without establishing a channel theorem.

**Sources and anchor:** [Heat-kernel representation](../science/classicalization.md#2-classical-probability-controls-the-complete-channel-norm), [Maxwell reference distribution](../science/classicalization.md#3-a-uniform-finite-size-bound), and [local Brownian contraction](../science/anisotropic_diffusion.md#21-brownian-representation-and-its-short-time-contraction). Holevo, Chapter 12, offers the Gaussian comparison; the rotation-group probability argument is supplied locally.

### M07 — Entanglement breaking and what a witness establishes

**Phase:** Background/preliminaries.

**Central question:** What does it mean for a channel to admit a purely measurement-and-preparation implementation?

**Understanding target:** Connect the measure-and-prepare form with destruction of all output–reference entanglement and with separability of the normalized Choi state. Explain why a negative partial transpose certifies entanglement, while a positive partial transpose need not certify separability in the dimensions used here. Distinguish an exact property of a channel from a small distance to channels with that property.

**Dependencies and story role:** Uses M02–M04. It establishes the comparison set and the logic of lower witnesses before introducing quantitative distances.

**Conceptual connection:** An explicit EB comparator proves an approximation upper bound; one entangled output can disprove exact EB. These are complementary tasks with different quantifiers.

**Sources and anchor:** [Model: EB characterization](../science/model.md#a-channel-distance-that-includes-every-encoding), [standard equivalences and their primary attribution](../references/RELATED_WORK.md#entanglement-breaking-continuity-and-the-limits-of-the-conclusion), and [the limits of a partial-transpose sector](../science/residual_entanglement.md#4-the-endpoint-and-the-interpretation-of-the-scale-pi2). Holevo, Chapters 3 and 6, provide the entanglement and channel foundations; the source map identifies the imported characterization.

### M08 — Complete distinguishability and dimension-uniform comparison

**Phase:** Background/preliminaries.

**Central question:** Which notion of closeness can constrain every input, reference, and encoding at once?

**Understanding target:** Interpret trace distance, total variation, and half-diamond distance as distinguishability measures in their respective settings. Explain the optimization over reference-assisted inputs, the half-norm convention, and contraction under channel pre- and postprocessing. Understand why a norm estimate whose conversion cost grows with $`d`$ may fail in a large-spin limit.

**Dependencies and story role:** Uses M02, M03, M06, and M07. It fixes the operational strength that an upper bound must have and the units in which the upper and lower arguments will meet.

**Conceptual connection:** A bound on rotation probability laws can remain independent of representation dimension. This is the route from a classical kernel calculation to an unrestricted quantum-channel statement.

**Sources and anchor:** [Model: half-diamond distance](../science/model.md#a-channel-distance-that-includes-every-encoding), [probability-to-channel transfer](../science/classicalization.md#2-classical-probability-controls-the-complete-channel-norm), and [the comparison with Sobolev estimates](../references/RELATED_WORK.md#uniform-berezinheat-comparison-ioos-kaminker-polterovich-and-shmoish). Holevo, Chapters 3 and 6, supply the channel-with-reference framework; the complete-norm estimate is given in the canonical project proof.

### M09 — Entropy under a mean-excitation constraint

**Phase:** Background/preliminaries.

**Central question:** Why can a bound on one mean excitation control the whole output entropy?

**Understanding target:** Explain von Neumann entropy, nonnegative relative entropy, and the maximum-entropy role of the geometric Gibbs distribution on nonnegative integer levels. Interpret $`g(\mu)=(\mu+1)\log_2(\mu+1)-\mu\log_2\mu`$ and its monotonicity and concavity. Understand why embedding a finite ladder in the infinite ladder gives an upper bound without assuming that the original density matrix is diagonal or Gaussian.

**Dependencies and story role:** Uses M01 and M03. It provides the entropy tool before applying it to the noisy coherent-state alphabet.

**Conceptual connection:** The ladder observable $`j-J_z`$ measures deviations from a chosen coherent pole. A bounded mean on that ladder can coexist with a carrier dimension that grows without bound.

**Sources and anchor:** [Communication: entropy at fixed mean excitation](../science/communication.md#2-almost-all-classical-bits-survive). Holevo, Chapter 7, supplies entropy and relative-entropy foundations; Chapter 12 provides related oscillator language, while the finite-spin embedding is explained locally.

### M10 — Classical messages, ensembles, and achievable rates

**Phase:** Background/preliminaries.

**Central question:** How does an ensemble of quantum outputs yield a classical communication rate?

**Understanding target:** Explain the difference between entropy of the average output and average output entropy in the Holevo information. Relate an achievable ensemble rate to ordinary classical capacity over independent uses. Distinguish that rate from a single-shot direction estimate, and distinguish a lower bound from a proof that an ensemble is optimal or that optimized Holevo information is additive.

**Dependencies and story role:** Uses M03, M04, and M09. It connects individual noisy states to a global communication task.

**Conceptual connection:** The coherent ensemble has average $`I/d`$. If each individual output has bounded entropy, most of the dimensional information budget $`\log_2d`$ remains available for classical messages.

**Sources and anchor:** [Communication: coherent ensemble and coding argument](../science/communication.md#2-almost-all-classical-bits-survive) and [independent-use conventions](../science/model.md#which-resources-are-covered). Holevo, Chapter 8, is the anchor for classical capacity, supported by Chapter 7 for the entropy quantities.

### M11 — Quantum transmission and the meaning of a converse

**Phase:** Background/preliminaries.

**Central question:** How do one-carrier entanglement fidelity and asymptotic quantum capacity ask different questions?

**Understanding target:** Describe arbitrary CPTP encoders and final recovery maps, the maximally entangled input used to define entanglement fidelity, and quantum capacity for arbitrarily long blocks of independent channel uses. Understand the EB overlap ceiling $`1/k`$ for a $`k`$-dimensional logical system. Keep a surviving entangled output distinct from a positive unassisted quantum transmission rate.

**Dependencies and story role:** Uses M02, M03, M07, M08, and M10. It completes the operational background by distinguishing the several quantum tasks that the project will constrain.

**Conceptual connection:** A complete-channel approximation can survive every fixed encoder and decoder; a capacity-continuity theorem is needed to control regularized rates over arbitrary blocks.

**Sources and anchor:** [Communication: arbitrary encoding and recovery](../science/communication.md#1-every-encoding-and-final-recovery), [quantum capacity](../science/communication.md#3-vanishing-quantum-capacity), and [distinct conclusions](../science/communication.md#5-what-remains-distinct). Holevo, Chapter 10, anchors quantum transmission; Chapter 3 supports the entangled-reference description.

### M12 — Background synthesis: formulate the operational question

**Phase:** Background/preliminaries.

**Central question:** What precise problem joins large-spin diffusion, reference entanglement, and retained classical information?

**Understanding target:** Formulate $`e_j(t)=\inf_{\mathcal E\in\mathrm{EB}}\frac12\|\Phi_t^{(j)}-\mathcal E\|_\diamond`$ and the scaled time $`\nu=nt`$. Explain why almost unchanged polarization does not decide whether $`e_j`$ vanishes. State the carrier, time convention, independent-use assumption, and exclusion of protected bypasses and intermediate correction. Separate exact finite-spin EB, asymptotic proximity to EB, and a quantum-capacity threshold before examining the proposed theorem.

**Dependencies and story role:** Integrates M01–M11. This closes the background phase by turning its local objects and tools into one well-posed research question.

**Conceptual connection:** The unresolved issue is whether a measurement-like description can hold uniformly over a growing quantum state space while classical messages remain abundant.

**Sources and anchor:** [Model and central statements](../science/model.md), [physical interpretation](../science/interpretation.md), and [the scope recorded in the source map](../references/RELATED_WORK.md#setting-and-scope). Holevo, Chapters 3, 6, 7, 8, and 10, provide the assembled foundations; the project defines the specific limiting question.

## Phase II — Narrative and innovation

### M13 — Build the coherent measure-and-prepare comparator

**Phase:** Narrative/innovation.

**Central question:** Which explicit classical implementation should approximate short-time spin diffusion?

**Understanding target:** Explain how the coherent POVM followed by preparation of the measured direction defines $`\mathcal B_j`$. Use the resolution of the identity to understand trace preservation and the displayed construction to understand EB. Identify its exact rank-$`\ell`$ multipliers as imported identities, while leaving open whether their agreement with heat multipliers suffices for a complete-channel bound.

**Dependencies and story role:** Uses M04, M05, M07, and M12. This opens the research phase with a concrete comparator that can be independently checked.

**Conceptual connection:** The comparator preserves a useful classical direction while removing quantum correlations with a reference. It therefore matches the physical task more closely than comparison with the fully depolarizing channel.

**Sources and anchor:** [Classicalization, Section 1](../science/classicalization.md#1-an-established-measurement-channel) and [Aschieri–Ruba–Solovej attribution](../references/RELATED_WORK.md#exact-coherent-channel-kernel-aschieri-ruba-and-solovej), published Lemmas 12–13. Holevo, Chapter 6, supplies the channel framework; the exact spin comparator identities come from the cited primary work.

### M14 — Represent the comparator by central rotations on SO(3)

**Phase:** Narrative/innovation.

**Central question:** How can the same EB channel be written as an average of unitary rotations?

**Understanding target:** Explain the positive central density $`k_n(\theta)=C_n\cos^{2n}(\theta/2)`$, its Haar normalization, and verification through integer-spin characters. Resolve the two SU(2) peaks at $`I`$ and $`-I`$ by working on SO(3), where conjugation is unambiguous even for half-integer spin. Connect the common random-rotation representation to the total-variation upper bound on half-diamond distance.

**Dependencies and story role:** Uses M05, M06, M08, and M13. It converts a quantum comparison problem into comparison of two classical probability laws with the correct group convention.

**Conceptual connection:** EB and random-unitary are compatible channel descriptions. Their coexistence here supplies both a known classical comparator and a representation-independent route to error control.

**Sources and anchor:** [Exact comparator representation](../science/classicalization.md#1-an-established-measurement-channel), [complete-norm transfer](../science/classicalization.md#2-classical-probability-controls-the-complete-channel-norm), and [Bardet et al.'s transference framework](../references/RELATED_WORK.md#group-transference-collective-decoherence-and-capacities-bardet-et-al). Holevo, Chapter 6, supplies channel foundations; the central-kernel identity is attributed to Aschieri–Ruba–Solovej.

### M15 — Control the Berezin kernel by a Maxwell law

**Phase:** Narrative/innovation.

**Central question:** How does a local Gaussian shape become a uniform finite-size probability bound?

**Understanding target:** Distinguish the group density $`k_n`$ from its radial density $`r_n`$. Explain the domination $`r_n/m_{1/n}\le A_n`$, why normalization converts this into total variation at most $`A_n-1`$, and how Stirling bounds make that error $`O(1/n)`$ for every positive integer $`n`$. Keep the missing radial tail in the common probability space by extending the compactly supported density by zero.

**Dependencies and story role:** Uses M06 and M14. It establishes the first quantitative half of the kernel comparison rather than relying on a pointwise Taylor expansion near the identity.

**Conceptual connection:** The Maxwell law is a shared reference distribution. Its usefulness lies in an integrated error bound that remains valid as the probability peak shrinks.

**Sources and anchor:** [Classicalization: the coherent-measurement kernel](../science/classicalization.md#the-coherent-measurement-kernel). Holevo, Chapter 12, provides the Gaussian comparison already introduced in M06; the domination and finite-size estimate are local project derivations.

### M16 — Control heat-kernel images and the compact-group tail

**Phase:** Narrative/innovation.

**Central question:** What must be added to the Euclidean Gaussian term to control diffusion on the whole rotation group?

**Understanding target:** Explain why Poisson summation of half-integer frequencies produces the heat-kernel image formula and its alternating signs. Identify the zero-image Maxwell term with its curvature factor. Understand how the nonzero image intervals cover the outer radial tail, and why the image error, curvature error, and missing Maxwell mass must all be bounded.

**Dependencies and story role:** Uses M05, M06, M14, and M15. It establishes the second half of the uniform probability comparison with the normalization appropriate to SO(3).

**Conceptual connection:** Short-time diffusion is locally Gaussian, but the theorem requires accounting for the global compact geometry. The same image representation will later explain the antipodal contribution in the residual-entanglement calculation.

**Sources and anchor:** [Classicalization: the heat kernel](../science/classicalization.md#the-heat-kernel). Holevo, Chapter 6, supplies the evolution context; the Poisson formula, image accounting, and tail estimate are supplied in the project proof.

### M17 — Obtain the uniform finite-size channel bound

**Phase:** Narrative/innovation.

**Central question:** Why does the kernel estimate control the full spin channel as its dimension grows?

**Understanding target:** Combine the two Maxwell comparisons with the probability-to-channel inequality to obtain $`\frac12\|\Phi_{1/n}^{(j)}-\mathcal B_j\|_\diamond\le K_0/n`$, with $`K_0<2.4`$. Explain the absence of a dimension-dependent norm-conversion factor and the resulting uniformity over arbitrary input states and references. Distinguish this upper bound from either equality with total variation or an optimized exact distance to the EB set.

**Dependencies and story role:** Uses M08 and M14–M16. This turns the component estimates into the first channel-level conclusion of the narrative.

**Conceptual connection:** The rotation distributions are compared before choosing a spin representation. That order of argument is what protects the bound against hidden encodings in the growing Hilbert space.

**Sources and anchor:** [Finite-size bound and its explicit constant](../science/classicalization.md#3-a-uniform-finite-size-bound), [uniformity of the argument](../science/classicalization.md#5-what-makes-the-result-uniform), and [related norm comparisons](../references/RELATED_WORK.md#uniform-berezinheat-comparison-ioos-kaminker-polterovich-and-shmoish). Holevo, Chapters 3 and 6, supply the operational channel setting; the uniform estimate is established locally.

### M18 — Extend the comparator to every later time

**Phase:** Narrative/innovation.

**Central question:** Why is a bound at one shrinking time sufficient for all subsequent diffusion times?

**Understanding target:** Construct $`\mathcal E_{j,t}=\Phi_{t-1/n}^{(j)}\circ\mathcal B_j`$ for $`t\ge1/n`$. Explain why this channel remains EB and why the semigroup property and diamond-norm contraction preserve the same $`O(1/n)`$ error. Distinguish a uniform upper bound at later times from a determination of the exact EB time or an assertion that the error stays constant.

**Dependencies and story role:** Uses M03, M07, M08, and M17. It completes the upper side before the narrative turns to a separate lower witness.

**Conceptual connection:** Once the channel is well approximated by a measurement-and-preparation process, further noise cannot invalidate that approximation bound. No second kernel calculation is required.

**Sources and anchor:** [Classicalization: later times](../science/classicalization.md#later-times). Holevo, Chapter 6, supplies the composition and evolution framework; the explicit comparator and its uniform error are the project application.

### M19 — Isolate an exact two-level Bell witness

**Phase:** Narrative/innovation.

**Central question:** Can two physical spin levels expose a failure of every EB approximation below the proposed boundary?

**Understanding target:** Identify the code spanned by $`|j,j\rangle`$ and $`|j,j-1\rangle`$ and its entanglement with a reference qubit. Understand how exact symmetric-power matrix elements determine a $`2\times2`$ principal block after partial transposition. Explain why a negative expectation in that block is sufficient, without requiring its vector to be an eigenvector of the full partial transpose. Track the witness norm $`1/2`$ that converts negativity to half-trace distance.

**Dependencies and story role:** Uses M01, M02, M07, M08, and M12. It starts an independent converse construction after the upper bound has been established.

**Conceptual connection:** A universal upper bound must work for every input, but a universal obstruction to EB approximation can be proved with one carefully chosen reference-entangled input.

**Sources and anchor:** [Classicalization, Section 4: exact encoding and witness](../science/classicalization.md#4-a-two-level-converse-below-the-boundary). Holevo, Chapter 3, supplies the composite-state setting and Chapter 10 the quantum-transmission viewpoint; the matrix elements and witness calculation are supplied locally.

### M20 — Evaluate the witness through the local Gaussian limit

**Phase:** Narrative/innovation.

**Central question:** Which short-time fluctuations determine the asymptotic sign of the two-level witness?

**Understanding target:** Explain the scaled Gaussian rotation coordinates at fixed $`\nu>0`$ and the exponential variable $`Z`$ with mean $`\nu`$ obtained from the two transverse coordinates. Identify the exact cancellation of the longitudinal phase in the relevant coherence product. Connect bounded matrix elements and tail truncation to convergence of expectations, leading to the negative expectation $`-(1-\nu)/[2(1+\nu)^2]`$ when $`0<\nu<1`$, with $`\nu=0`$ treated directly.

**Dependencies and story role:** Uses M06, M16, and M19. It supplies the nonzero limiting obstruction needed to match the upper bound's time scale.

**Conceptual connection:** A local limit suffices for the chosen finite-level witness. This does not require replacing every possible spin encoding by an oscillator code or establishing a Gaussian approximation on the whole Hilbert space.

**Sources and anchor:** [Classicalization, Section 4: Gaussian limit and expectation bounds](../science/classicalization.md#4-a-two-level-converse-below-the-boundary). Holevo, Chapter 12, provides the Gaussian comparison; the compact-spin limit and its witness application are proved in the project.

### M21 — Synthesize the sharp operational threshold

**Phase:** Narrative/innovation.

**Central question:** In exactly what sense do the upper comparator and lower witness locate a sharp boundary?

**Understanding target:** Combine $`e_{n/2}(\nu/n)=O(1/n)`$ for $`\nu\ge1`$ with a strictly positive limiting lower bound at each fixed $`0\le\nu<1`$. Explain why their meeting point is $`\nu=1`$, even though their numerical bounds need not agree away from it. State the order of limits and distinguish this distance-to-EB boundary from finite-$`n`$ exact EB and from a proven boundary for positive quantum capacity.

**Dependencies and story role:** Integrates M17–M20 with the definitions in M12. It completes the central channel theorem before turning to its consequences and extensions.

**Conceptual connection:** The upper proof is global over states and references; the lower proof is local in a two-level encoding. Their shared normalization makes these different forms of evidence meet at one operational scale.

**Sources and anchor:** [Model: Theorem 1](../science/model.md#central-statements), [interpretation of sharpness](../science/model.md#interpretation-of-sharpness), and [proof synthesis](../science/classicalization.md#5-what-makes-the-result-uniform). Holevo, Chapters 6 and 10, support the distinction between a channel property and a transmission task; the threshold itself is the local result.

### M22 — Constrain arbitrary encoding and final recovery

**Phase:** Narrative/innovation.

**Central question:** What does the complete-channel theorem say about a code whose structure was never examined?

**Understanding target:** Derive the entanglement-fidelity ceiling $`F_e\le\min\{1,1/k+2.4/n\}`$ for arbitrary CPTP encoding into the spin and final recovery when $`t\ge1/n`$. Explain the roles of the EB overlap bound, pre- and postprocessing contraction, and trace-distance control of a projector expectation. Keep unrestricted code design distinct from granting a protected quantum bypass or correction during the interval.

**Dependencies and story role:** Uses M08, M11, and M18–M21. It turns the channel-level result into an operational converse for each carrier without optimizing over codes.

**Conceptual connection:** Uniformity removes the need to inspect codeword geometry or recovery complexity. The bound constrains passive storage under the specified noise while leaving other resources and noise models as separate problems.

**Sources and anchor:** [Communication, Section 1](../science/communication.md#1-every-encoding-and-final-recovery), [resource boundary](../science/model.md#which-resources-are-covered), and [relation to spin codes](../references/RELATED_WORK.md#relation-to-spin-error-correcting-codes). Holevo, Chapter 10, supplies the quantum-transmission framework.

### M23 — Retain nearly all classical bits

**Phase:** Narrative/innovation.

**Central question:** How can the same noisy carrier retain a classical rate close to its dimensional maximum?

**Understanding target:** Combine the uniform coherent ensemble, its maximally mixed average, covariance of individual output entropies, and the exact mean excitation $`\mu_j(t)=j(1-e^{-2t})`$. Use the entropy bound to obtain $`C\ge\log_2(n+1)-g(nt)`$, hence $`C\ge\log_2(n+1)-g(\nu)`$ at fixed scaled time. Explain the two-bit deficit bound at $`\nu=1`$ without claiming that the chosen ensemble is optimal or the capacity is exactly known.

**Dependencies and story role:** Uses M04, M05, M09, M10, and M21. It establishes the retained classical resource against which quantum loss becomes physically informative.

**Conceptual connection:** Individual outputs acquire only bounded excitation entropy while the ensemble average has entropy growing as $`\log_2d`$. The capacity statement therefore needs more than the observation that polarization remains high.

**Sources and anchor:** [Communication, Section 2](../science/communication.md#2-almost-all-classical-bits-survive) and [physical explanation of the retained rate](../science/interpretation.md#why-the-classical-rate-stays-high). Holevo, Chapters 7 and 8, supply the entropy and coding foundations; the spin-specific bound is derived locally.

### M24 — Control quantum capacity with the growing dimension retained

**Phase:** Narrative/innovation.

**Central question:** Why does an $`O(1/n)`$ channel approximation force the regularized quantum rate to vanish?

**Understanding target:** Apply the imported Leung–Smith continuity theorem with full diamond error $`\epsilon\le4.8/n`$ and output dimension $`d=n+1`$. Track the factor of two from the project's half-diamond convention and the dimension term in $`8\epsilon\log_2d+4h_2(\epsilon)`$. Conclude $`Q=O(\log n/n)`$ for independent uses, understanding that the continuity theorem already controls regularized capacity and that its finite-size constants are conservative.

**Dependencies and story role:** Uses M08, M11, M18, and M21–M23. It completes the simultaneous classical/quantum communication separation.

**Conceptual connection:** Nearness to an EB channel alone is qualitative until the dimension dependence is retained. The continuity estimate makes the shrinking error win against the growing Hilbert space.

**Sources and anchor:** [Communication, Section 3](../science/communication.md#3-vanishing-quantum-capacity) and [continuity attribution and scope](../references/RELATED_WORK.md#entanglement-breaking-continuity-and-the-limits-of-the-conclusion), especially Leung–Smith, Corollary 14, equation (29). Holevo, Chapter 10, anchors quantum capacity; the cited primary theorem supplies the quantitative continuity bound.

### M25 — Extend the separation across shrinking time scales

**Phase:** Narrative/innovation.

**Central question:** Is the communication separation confined to one finely chosen time?

**Understanding target:** Use the exact finite bounds at $`t_n=n^{-\alpha}`$, with fixed $`0<\alpha<1`$, to obtain $`C\ge\alpha\log_2n-\log_2e+o(1)`$ while $`Q=O(\log n/n)`$ and polarization tends to one. Explain why $`nt_n`$ now grows rather than remaining fixed, and why the later-time upper bound and entropy estimate still apply without another channel approximation.

**Dependencies and story role:** Uses M18, M23, and M24. It broadens the fixed-$`\nu`$ conclusion into a range of experimentally interpretable shrinking diffusion times.

**Conceptual connection:** The channel can support a diverging number of classical bits after the quantum converse already applies. The two information types are separated over a time interval, rather than only at a single comparison point.

**Sources and anchor:** [Communication, Section 4](../science/communication.md#4-a-broad-interval-of-communication-separation). Holevo, Chapters 8 and 10, supply the meanings of the two rates; this scaling corollary follows from the project's finite bounds.

### M26 — Understand what survives unequal diffusion strengths

**Phase:** Narrative/innovation.

**Central question:** Which parts of classicalization require isotropy, and when can the anisotropic boundary still be located exactly?

**Understanding target:** For fixed $`D>0`$ with eigenvalues $`a\le b\le c`$, explain extraction of the isotropic component $`aI`$ through the central adjoint Casimir. Connect the tangent-plane witness to $`ab`$ at the pole along the strongest axis, giving $`1/\sqrt{ab}\le\tau_{\mathrm{op}}(D)\le1/a`$ for $`\tau=nt`$. Identify the exact case $`a=b\le c`$ and the unresolved gap when $`a<b`$. Explain why unitality and entropy averaging retain the classical bound without full rotation covariance.

**Dependencies and story role:** Uses M05, M18, M20, M23, and M24. It tests the structural robustness of the completed isotropic argument.

**Conceptual connection:** A global isotropic component controls the upper bound, while two local transverse rates control the witness. Their agreement in an axisymmetric family explains both the robust exact case and the limitation of the general bracket.

**Sources and anchor:** [Anisotropic Casimir factorization](../science/anisotropic_diffusion.md#1-upper-bound-from-the-adjoint-casimir), [optimal pole and bracket](../science/anisotropic_diffusion.md#24-optimal-pole-for-this-witness-and-the-sandwich), and [capacity without covariance](../science/anisotropic_diffusion.md#3-classical-capacity-without-covariance). Holevo, Chapter 6, supports the channel evolution and Chapters 7–8 the entropy and classical-capacity framework; the anisotropic coefficients are derived locally.

### M27 — Locate the limits of deterministic rotations and missing noise axes

**Phase:** Narrative/innovation.

**Central question:** Which changes to the dynamics preserve the argument, and which change its inverse-spin conclusion?

**Understanding target:** Explain the integrated minimum diffusion strength $`\kappa(T)=\int_0^T\lambda_{\min}(D(s))\,ds`$ and the upper condition $`n\kappa(T)\ge1`$ in the presence of deterministic linear spin Hamiltonians. Distinguish this upper statement, which permits strong rotations, from the unchanged lower limit proved for rotation rates bounded independently of $`n`$. Recognize the integrated-trace entropy bound for classical communication and the positive lower witness at every fixed inverse-spin time when a fixed diffusion matrix is rank deficient and rotation rates remain bounded. Keep nonlinear Hamiltonians and spin-dependent degenerating rates outside the stated fixed-rate conclusion.

**Dependencies and story role:** Uses M03, M09, M20, and M26. It turns robustness into explicit conditions on dynamics and resources, rather than a generic claim about control.

**Conceptual connection:** Centrality of the Casimir protects the upper factorization; transverse fluctuations determine the local converse. These mechanisms have different assumptions and must remain separate.

**Sources and anchor:** [Deterministic rotations and time-dependent rates](../science/anisotropic_diffusion.md#5-deterministic-hamiltonian-rotations-and-time-dependent-rates) and [limits of robustness](../science/anisotropic_diffusion.md#6-limits-of-the-robustness-claim). Holevo, Chapter 6, supplies the evolution framework and Chapter 7 the entropy foundation; the control and rank-deficiency statements are local results.

### M28 — Resolve the normalized Choi partial transpose in the singlet sector

**Phase:** Narrative/innovation.

**Central question:** How can rotational symmetry turn a finite-spin entanglement question into one exact scalar expression?

**Understanding target:** Define the normalized Choi state and identify the transpose basis. Explain why covariance makes its partial transpose scalar on total-spin sectors, why the singlet is an eigenvector, and how its swap parity depends on $`n`$. Connect the character identity to $`\lambda_{0,n}(t)=(n+1)^{-2}\sum_{\ell=0}^{n}(-1)^\ell(2\ell+1)e^{-t\ell(\ell+1)}`$. Use the zero-time swap value to understand the normalization.

**Dependencies and story role:** Uses M01, M02, M05, M07, and M14. It opens the final distinction between asymptotic operational classicalization and exact finite-spin entanglement.

**Conceptual connection:** The Choi input probes the channel through a maximally entangled state, while representation symmetry isolates one diagnostic sector. A scalar calculation can certify non-EB without determining every sector.

**Sources and anchor:** [Residual entanglement: conventions](../science/residual_entanglement.md#result-and-conventions), [exact singlet eigenvalue](../science/residual_entanglement.md#1-exact-singlet-eigenvalue), and [Schliemann's representation-theoretic background](../references/RELATED_WORK.md#partial-transpose-and-residual-choi-entanglement). Holevo, Chapters 3 and 6, supply composite-state and channel foundations; the singlet specialization is derived locally.

### M29 — Explain residual NPT beyond the operational boundary

**Phase:** Narrative/innovation.

**Central question:** How can a channel approach the EB set while an exact entanglement witness remains negative?

**Understanding target:** Separate the finite character sum into the positive antipodal heat term and the omitted representation tail. Compare their exponential rates to obtain $`\lambda_{0,n}(\nu/n)\sim-[e^{-2\nu}/\cosh\nu]e^{-\nu n}/n`$ for fixed $`0<\nu<\pi/2`$ along odd $`n`$. Explain the stronger certificate at $`\nu=1`$ for every odd $`n\ge5`$, the change in this sector's sign at the fixed-$`\nu`$ endpoint, and the coexistence of an exponentially small distance lower bound with the independent $`O(1/n)`$ upper bound. Do not identify this single eigenvalue with total residual entanglement or the exact PPT/EB time.

**Dependencies and story role:** Uses M07, M16, M21, M24, and M28. It reconciles the project's operational conclusion with exact surviving entanglement.

**Conceptual connection:** An approximation can be operationally strong without erasing every exact signature. Parity, distinct exponential scales, and the meaning of a one-sector witness explain why the two statements coexist.

**Sources and anchor:** [Heat term and representation tail](../science/residual_entanglement.md#2-separate-the-antipodal-heat-kernel-from-a-representation-tail), [finite-spin certificates](../science/residual_entanglement.md#3-explicit-finite-spin-npt-certificates), and [channel-distance consequence](../science/residual_entanglement.md#5-a-channel-distance-consequence). Holevo, Chapters 3, 6, and 10, supply the distinctions between entanglement, channel structure, and quantum transmission; the parity-dependent asymptotics are local results.

### M30 — Whole-project synthesis: contribution, mechanism, and scope

**Phase:** Narrative/innovation.

**Central question:** What has the combined analysis established, why does it matter, and which claims remain separate?

**Understanding target:** Explain the complete chain from a known coherent-measurement kernel, through a uniform shrinking-time comparison and matching two-level witness, to the sharp distance-to-EB boundary and simultaneous communication separation. Integrate the anisotropic bracket, its exact axisymmetric case, deterministic-rotation scope, and residual Choi NPT. State the irreducible-carrier and independent-use assumptions. Distinguish imported representation and continuity results from the estimates derived here, analytical proofs from finite numerical checks, and established conclusions from the open general anisotropic coefficient, exact EB/PPT times, and quantum-capacity boundary below $`\nu=1`$.

**Dependencies and story role:** Integrates M13–M29 using the problem formulation in M12. This closes the narrative phase by connecting the mechanism, consequences, robustness, and limits into one scientific contribution.

**Conceptual connection:** A large spin can remain a high-capacity classical carrier while every encoding in that same irreducible carrier faces a quantum-transmission converse. Operational approximation, exact entanglement, and communication capacity remain distinct quantities throughout that statement.

**Sources and anchor:** [Scientific account](../science/README.md), [physical interpretation and boundaries](../science/interpretation.md), [attribution and closest predecessors](../references/RELATED_WORK.md#established-ingredients-and-the-contribution-of-this-analysis), and [the scope of numerical verification](../verification/README.md). Holevo, Chapters 3, 6, 7, 8, and 10, provide the integrated quantum-information foundation, with Chapter 12 as a limited Gaussian comparison; the canonical project pages supply the actual research claims.
