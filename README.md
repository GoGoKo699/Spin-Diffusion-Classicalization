# Spin-Diffusion-Classicalization

**When does a noisy large spin become operationally classical, even though it remains a good classical information carrier?**

For isotropic rotational diffusion on one irreducible spin, this account proves a sharp large-spin threshold for proximity to entanglement-breaking channels. At the threshold, every encoding and final recovery is constrained, quantum capacity tends to zero, and classical capacity remains within two bits of its dimensional maximum. The result concerns the complete channel, including arbitrary external reference systems.

## Principal result

Write $`n=2j`$, $`d=n+1`$, and use the dimensionless noise convention

```math
\Phi_t=\exp\!\left[-t\sum_{a=x,y,z}[J_a,[J_a,\cdot]]\right],
\qquad \nu=nt.
```

Let $`e_j(t)`$ be the infimum of the half-diamond distance from $`\Phi_t`$ to all entanglement-breaking (EB) channels with the same input and output spaces. Then

```math
\begin{aligned}
\nu\ge1:&\qquad e_{n/2}(\nu/n)\le\min\{1,2.4/n\},\\
0\le\nu<1:&\qquad
\liminf_{n\to\infty}e_{n/2}(\nu/n)
\ge\frac{1-\nu}{2(1+\nu)^2}>0.
\end{aligned}
```

The second line holds at every fixed subthreshold $`\nu`$. Thus **$`\nu=1`$ is the exact asymptotic boundary for vanishing distance to the EB set**. The proof uses the established random-rotation representation of coherent-state measurement, a uniform heat-kernel comparison, and a two-level encoded entanglement witness. [Read the theorem and proof](science/classicalization.md).

| Operational consequence | Result and domain |
|---|---|
| Any encoding and final recovery of a logical $`k`$-level system | $`F_e\le\min\{1,1/k+2.4/n\}`$ for $`t\ge1/n`$. |
| Unassisted quantum capacity per independent use | $`Q=O(\log n/n)`$ for $`t\ge1/n`$. An explicit finite-size bound is provided. |
| Classical capacity at fixed scaled time | $`C\ge\log_2(n+1)-g(\nu)`$, where $`g(x)=(x+1)\log_2(x+1)-x\log_2x`$. |
| At the boundary $`\nu=1`$ | The classical deficit is at most two bits; mean polarization is retained by the factor $`e^{-2/n}`$. |

These capacity statements allow arbitrary block codes over independent uses. The sharp boundary above is a channel-distance result; positive quantum capacity throughout $`\nu<1`$ is not established. [Communication bounds and proofs](science/communication.md).

![Kernel comparison and encoded witness for spin diffusion](figures/operational_threshold.svg)

*Left: the computed total variation between the heat law and the coherent-measurement rotation law, alongside the analytical upper bound. Total variation is an upper bound on channel distance, not an exact diamond-distance calculation. Right: the negative expectation of the two-level Bell witness, clipped at zero, gives a lower bound on distance to EB. The curve is its proved large-spin limit; markers are exact finite-spin evolution. [Data and reproduction](verification/README.md).*

## Robustness and residual entanglement

For a fixed positive diffusion matrix with eigenvalues $`0<a\le b\le c`$, the onset of vanishing distance to EB obeys

```math
\frac1{\sqrt{ab}}\le\tau_{\mathrm{op}}\le\frac1a,
\qquad t=\tau/n.
```

When **the two smallest rates agree**, $`a=b\le c`$, both bounds meet at $`\tau_{\mathrm{op}}=1/a`$. The third-axis rate may be arbitrarily stronger and fixed. Classical capacity still grows as $`\log_2(n+1)`$ with a bounded deficit. Deterministic linear spin rotations preserve the upper bound through an exact Casimir factorization. [Anisotropic theorem](science/anisotropic_diffusion.md).

Operational classicality also differs from exact entanglement death. For every fixed $`1\le\nu<\pi/2`$ and sufficiently large odd $`n`$, the normalized Choi state still has a negative partial-transpose eigenvalue:

```math
\lambda_{0,n}(\nu/n)
\sim-\frac{e^{-2\nu}}{\cosh\nu}\frac{e^{-\nu n}}n.
```

At $`\nu=1`$, this singlet eigenvalue is negative for every odd $`n\ge5`$. The exponentially small eigenvalue coexists with an $`O(1/n)`$ upper bound on distance to EB. This does not determine the decay of all entanglement measures or the exact finite-spin EB time. [Residual-entanglement proof](science/residual_entanglement.md).

## Reading routes

| Question | Start here |
|---|---|
| What is the physical mechanism? | [Interpretation](science/interpretation.md) |
| How can I build an understanding of the whole project? | [Tutorial](learning/TUTORIAL.md), [30-milestone map](learning/MILESTONES.md), and [Holevo source bridge](learning/ANCHOR.md) |
| What exactly is assumed and proved? | [Model, conventions and claims](science/model.md) |
| How does the complete argument fit together? | [Scientific account](science/README.md) |
| Why does the result constrain every spin code? | [Uniform threshold proof](science/classicalization.md) and [recovery converse](science/communication.md#1-every-encoding-and-final-recovery) |
| Which ingredients are established prior work? | [Related work and source map](references/RELATED_WORK.md), with [BibTeX bibliography](references/references.bib) |
| How can I reproduce the finite checks and figures? | [Verification](verification/README.md) |

The [learning route](learning/README.md) uses **Holevo, _Quantum Systems, Channels, Information_, second revised and expanded edition (2019)** as its single educational anchor. Twelve background milestones and eighteen narrative milestones connect the physical carrier to the theorem, its communication consequences, and its limits. The tutorial includes an exactly solved qubit example; the source bridge records the verified chapter locations and the additional spin-specific steps supplied here.

## Reproduce

From the repository root, with Python 3.11 or newer:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
python verification/make_figures.py
```

The checks compare independent analytical and matrix constructions, including high-precision arithmetic for the exponentially small Choi eigenvalue. Their defaults write fresh numerical results under `verification/local_results/`; the committed reference run is under `verification/results/`. The analytical proofs establish the general statements; sampled numerics verify conventions and finite-size behavior.

## Physical scope

The carrier is **one irreducible spin**, with arbitrary encoding before the noise and recovery afterward. Intermediate active error correction, a protected quantum bypass, and noiseless multiplicity spaces in a reducible collection of spins are additional resources. The capacity claims assume independent noise between channel uses. The anisotropic sharp case fixes its diffusion rates as spin grows; three distinct rates retain the stated bracket.

For the physical master equation $`d\rho/ds=\gamma\sum_a\mathcal D[J_a](\rho)`$, our time is $`t=\gamma s/2`$, so the isotropic boundary corresponds to $`s=1/(\gamma j)`$. [Full resource accounting](science/model.md#which-resources-are-covered).

The [source map](references/RELATED_WORK.md) distinguishes imported identities and theorems from the estimates developed here. It compares directly relevant earlier results without claiming an exhaustive priority certification.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
