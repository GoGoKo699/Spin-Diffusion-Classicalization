# Bounded scientific and navigation review

Review date: 2 November 2026. [Reproduction](README.md) · [Scientific report manifest](results/manifest.json) · [Rank-two account](../science/rank_two_diffusion.md)

This review covers the local scientific computations, their stated scope and authored file navigation. Actual GitHub mathematical rendering, final integrated revision identity, merge status and preservation are separate checks. A successful local run alone establishes none of those statuses.

## Scientific checks performed

The following commands completed successfully with Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8:

```bash
OPENBLAS_NUM_THREADS=1 python verification/run_all.py --output-dir verification/results
OPENBLAS_NUM_THREADS=1 python verification/check_rank_two.py --full --output verification/results/rank_two_full.json
python verification/check_navigation.py --sister-root ../Nonlinear-Diffusion-Entanglement
```

The runner's manifest records all four scientific modules passing, including the three existing isotropic, anisotropic and residual-entanglement modules. The additional rank-two calculations retain their inputs, residuals and results in [the bounded report](results/rank_two.json) and [the optional larger grid](results/rank_two_full.json).

| Evidence | Observed result | Practical limit |
|---|---|---|
| Exact coherence-order evolution versus independent full Kronecker double commutator | 15 controls through $`n=7`$; largest matrix discrepancy $`1.65\times10^{-15}`$ | Floating-point checks at registered sizes; not an interval certificate |
| Encoded Bell state at zero time | Partial-transpose block minimum $`-1/2`$ and entanglement fidelity one | Fixes the code, reference and transpose normalization |
| Original finite-spin channel on squeezed reference inputs | 16 bounded cases through $`n=128`$; optional grid adds $`n=256,512`$ | A selected witness, not optimization over every input |
| Population output normalization and positivity | Full-grid trace errors below $`1.3\times10^{-13}`$; Hermiticity and positivity tolerances pass | Numerical evolution diagnostics |
| Independent finite-spin fidelity inequality | Evolved fidelity exceeds its exact semigroup tangent lower bound in every registered case | Conservative bound; it can become uninformative before the NPT test does |
| Growing-excitation first and squared generators | Seven sizes $`n=64,\ldots,4096`$; scaled errors about $`0.147\ldots0.160`$ and $`0.292\ldots0.309`$ | Vector/generator tests, not an output-convergence or full-diamond proof |

At $`t=n^{-2/3}`$, the optional $`n=512`$ witness expectation is approximately $`-0.04523346`$. At $`t=2n^{-2/3}`$ it is approximately $`+0.03436729`$. The positive value is recorded as failure of that particular detector; no EB conclusion is drawn from it.

## Scope and attribution review

The [rank-two account](../science/rank_two_diffusion.md) retains these distinctions:

- The direct finite-spin fidelity witness gives the lower bound $`[1/2-13s/8]_+`$ for the unit-rate, unit-squeeze example at $`t=s n^{-2/3}`$. It uses exact finite-dimensional spectral calculus and squeezed-state moments.
- The controlled contraction concerns fixed finite Schwartz input spans, fixed finite references and bounded intervals of scaled time. Its constants depend on the selected inputs and interval. The growing excitation is $`O(n^{1/3})`$; a hard growing cutoff is not claimed invariant.
- The all-finite-$`s`$ converse transfers the sister account's finite-energy oscillator witnesses using the local output estimate. The particular two-state numerical detector is not claimed to detect every such time.
- The exceptional-path covariance estimate bounds the oscillator channel. It supplies no global finite-spin EB comparator. The separately established equal-rate global upper regime is $`\sqrt n\,t\to\infty`$, leaving the stronger $`n^{2/3}t\to\infty`$ sufficiency question open.
- Hörmander/Grushin noise spreading, the rank-two SU(2) heat kernel and contraction, the nonlinear model and Mehler methods, and the Gaussian EB criterion retain their cited antecedents. The shared contribution is the controlled finite-spin transfer and its operational converse, with explicit ownership of the inherited oscillator results.

The numerical checks support normalization, finite examples and the generator estimates. The analytical output-convergence argument and global derivative estimate are assessed in the scientific account; the program does not turn those proofs into automatic certificates.

## Navigation and learning consistency

[The navigation report](results/navigation.json) records local file-target checks, exactly one heading for every milestone M01–M30, the sister README link and, in the joint-checkout run, reciprocity and directly linked counterpart files. Both learning routes identify the selected Holevo book DOI. The checker excludes mathematical/code expressions from link parsing and reports its scope explicitly.

External URLs, section-fragment targets and hosted mathematical rendering require separate inspection. A navigation pass is not a scientific correctness or release-readiness verdict.
