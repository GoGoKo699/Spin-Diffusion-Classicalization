# Learning spin-diffusion classicalization

[Project overview](../README.md) · [Scientific account](../science/README.md) · [Verification](../verification/README.md)

A large spin can retain an accurate direction while its ability to preserve quantum information changes substantially. The learning route explains how to make that statement precise for every encoding in one irreducible spin, why the threshold occurs on an inverse-spin time scale, and how classical communication survives it.

The single educational anchor is **Alexander S. Holevo, _Quantum Systems, Channels, Information: A Mathematical Introduction_, second revised and expanded edition (2019)**. The [source bridge](ANCHOR.md) identifies the verified chapter locations, fixes the project's conventions, and connects the textbook topics to the spin-specific arguments. The tutorial supplies the explanations needed to enter the project; reading the entire book is not a prerequisite.

## Choose a reading route

| Aim | Route |
|---|---|
| Follow the physical story with equations and a complete small example | [Tutorial](TUTORIAL.md), from the carrier and its reference to the threshold and communication consequences. |
| See the project's full set of understanding targets | [30-milestone map](MILESTONES.md), including dependencies and scientific source pointers. |
| Connect the selected book to the project | [Holevo bridge](ANCHOR.md), with chapter-level source verification and notation, normalization, and assumption translations. |
| Inspect exact claims and proof details | [Scientific account](../science/README.md), beginning with the [model](../science/model.md). |
| Separate established ingredients from the contribution | [Related work](../references/RELATED_WORK.md) and the [structured bibliography](../references/references.bib). |
| Compare the analytical reasoning with finite-spin computations | [Verification](../verification/README.md), including the recorded outputs and reproducible figures. |

## How the 30 milestones fit together

The allocation follows the scientific dependencies. **Twelve background milestones** connect the spin carrier, entanglement, channels, probability, entropy, and coding into the operational question. **Eighteen narrative milestones** assemble the two sides of the theorem, derive its consequences, and test its scope. Each phase moves from individual objects and arguments toward a synthesis.

| Milestones | Part of the story |
|---|---|
| M01–M06 | Carrier, external reference, channels, coherent directions, multipole diffusion, and local probability. |
| M07–M11 | Entanglement breaking, complete channel distance, excitation entropy, and classical and quantum communication. |
| M12 | Background synthesis: state the channel question with its resources and limits. |
| M13–M18 | Build the EB comparator, compare rotation kernels uniformly, and extend the bound to later times. |
| M19–M21 | Construct the two-level witness, evaluate its local limit, and establish the sharp boundary. |
| M22–M25 | Constrain arbitrary recovery, retain classical bits, bound quantum capacity, and extend the separation across time scales. |
| M26–M27 | Unequal diffusion strengths, deterministic rotations, and missing noise directions. |
| M28–M29 | Exact Choi partial transpose and the residual entanglement that can coexist with operational classicality. |
| M30 | Whole-project synthesis: mechanism, contribution, attribution, and resource scope. |

The map selects what is needed to understand the project as a whole. The canonical science pages retain the specialist lemmas and calculations behind each target. The tutorial follows this settled map and uses the exactly solvable qubit channel to connect physical preparation, noisy output, measurement, entanglement, and channel distance in one example.

## Three quantities to keep in view

The central boundary concerns **distance to the set of entanglement-breaking channels as the spin grows**. Exact EB at a fixed spin, the survival of an entangled output, and an unassisted quantum communication rate are related but distinct questions. The tutorial carries their definitions through the arguments so that the upper comparator, lower witness, capacity bounds, and residual Choi eigenvalue can be read together.

The book supplies a common quantum-information language. The repository's proofs and primary research references supply the spin-specific results, with the source-access limits stated in the bridge.
