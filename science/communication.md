# Quantum transmission and classical communication

[Model](model.md) · [Threshold proof](classicalization.md) · [Physical interpretation](interpretation.md)

A channel can preserve an accurate classical direction and still be unable to carry reliable quantum information. The uniform EB approximation turns that distinction into bounds on encoding, recovery and asymptotic communication rates.

All logarithms in this page are base two. A use means one irreducible spin carrier subjected to one noise interval. Capacities use arbitrarily many independent copies of that channel.

## 1. Every encoding and final recovery

Let $`\mathcal V:\mathcal B(\mathbb C^k)\to\mathcal B(\mathcal H_j)`$ and
$`\mathcal R:\mathcal B(\mathcal H_j)\to\mathcal B(\mathbb C^k)`$ be arbitrary CPTP maps. Define the entanglement fidelity of their effective channel by

```math
F_e=
\langle\Omega_k|
(\mathrm{id}\otimes\mathcal R\circ\Phi_t^{(j)}\circ\mathcal V)
(|\Omega_k\rangle\langle\Omega_k|)
|\Omega_k\rangle,
\qquad
|\Omega_k\rangle=k^{-1/2}\sum_{r=1}^k|r,r\rangle.
```

If $`\mathcal E`$ is EB, then $`\mathcal R\circ\mathcal E\circ\mathcal V`$ is EB. Every separable state has overlap at most $`1/k`$ with $`|\Omega_k\rangle`$. Indeed, this bound holds for product pure states by Cauchy–Schwarz and extends by convexity.

The threshold proof supplies an EB comparator within half-diamond distance
$`\delta_n=\min\{1,2.4/n\}`$ at every $`t\ge1/n`$. Encoding and recovery contract the distance. A projector's expectation changes by at most trace distance, so

```math
F_e\le\min\{1,1/k+2.4/n\},
\qquad t\ge1/n.
```

For any fixed logical dimension $`k\ge2`$, the limiting upper bound is the corresponding EB fidelity ceiling. This covers unrestricted encodings within the carrier and arbitrary final recovery. It does not assume a particular spin code or an efficient recovery circuit.

## 2. Almost all classical bits survive

Consider the uniform ensemble of coherent states
$`\{d\Omega,|\Omega\rangle\langle\Omega|\}`$.
Its average state is $`I/d`$. Unitality preserves this average, and rotation covariance makes all individual output entropies equal. Its Holevo information is therefore

```math
\chi=\log_2 d
-S\!\left(\Phi_t^{(j)}(|j,j\rangle\langle j,j|)\right).
```

The Holevo–Schumacher–Westmoreland coding theorem makes this an achievable lower bound on ordinary classical capacity. The channel need not have an additive optimized Holevo information, and the coherent ensemble need not be optimal.

For north-pole input, use the nonnegative excitation observable
$`N=j-J_z`$, with eigenvalues $`0,\ldots,n`$. The rank-one decay law gives the exact mean

```math
\mu_j(t)=\mathrm{Tr}[N\Phi_t^{(j)}(|j,j\rangle\langle j,j|)]
=j(1-e^{-2t}).
```

Any state supported on nonnegative integer levels with mean at most $`\mu`$ has entropy at most

```math
g(\mu)=(\mu+1)\log_2(\mu+1)-\mu\log_2\mu,
\qquad g(0)=0.
```

To see this without a Gaussian-state assumption, embed the finite ladder in the infinite nonnegative ladder and compare with the geometric Gibbs distribution
$`q_r=(1+\mu)^{-1}(\mu/(1+\mu))^r`$.
Nonnegativity of quantum relative entropy gives $`S(\rho)\le-\mathrm{Tr}\rho\log_2 q=g(\mu)`$ when the mean is $`\mu`$; monotonicity of $`g`$ handles an upper bound on the mean. Off-diagonal matrix elements do not invalidate this argument.

Thus the following bound is exact at finite $`j`$:

```math
C(\Phi_t^{(j)})
\ge\log_2(n+1)-g(\mu_j(t))
\ge\log_2(n+1)-g(nt).
```

The second inequality uses $`1-e^{-2t}\le2t`$. At $`t=\nu/n`$,

```math
C(\Phi_{\nu/n}^{(j)})
\ge\log_2(n+1)-g(\nu).
```

In particular, $`g(1)=2`$. At the operational boundary the loss from the dimensional maximum $`\log_2(n+1)`$ is at most two bits per use.

This is an achievable rate statement based on collective decoding over independent uses. It is stronger than preserving one spin moment and different from the precision of a single-shot direction estimate.

## 3. Vanishing quantum capacity

For an EB comparator $`\mathcal E`$, $`Q(\mathcal E)=0`$.
[Leung–Smith, Corollary 14, Eq. (29)](../references/RELATED_WORK.md#entanglement-breaking-continuity-and-the-limits-of-the-conclusion) prove that channels with common finite output dimension $`d`$ and full diamond distance at most $`\epsilon`$ obey

```math
|Q(\mathcal N)-Q(\mathcal M)|
\le8\epsilon\log_2 d+4h_2(\epsilon),
```

where $`h_2(x)=-x\log_2x-(1-x)\log_2(1-x)`$.
We use the bound with $`\epsilon=4.8/n\le0.48`$ for $`n\ge10`$.
The factor two converts our half-diamond convention to theirs.

For every $`t\ge1/n`$ and $`n\ge10`$,

```math
0\le Q(\Phi_t^{(j)})
\le
\min\left\{
\log_2(n+1),
\frac{38.4\log_2(n+1)}n+4h_2(4.8/n)
\right\}.
```

Since $`h_2(c/n)=O(\log n/n)`$ for fixed $`c`$, this is
$`Q=O(\log n/n)`$.
The theorem controls the regularized capacity, so the conclusion permits arbitrary block encodings and decodings over independent uses. It is not restricted to a one-use coherent-information calculation.

The constants are deliberately conservative. For moderate $`n`$, the displayed bound may supply only the dimensional upper bound. Its role is an explicit vanishing asymptotic converse, not a tight finite-size capacity estimate.

## 4. A broad interval of communication separation

At any fixed $`\nu\ge1`$ the classical deficit is bounded while the quantum rate vanishes. The same exact bounds also describe intermediate time scales.

Let $`t_n=n^{-\alpha}`$ with fixed $`0<\alpha<1`$. Then $`nt_n=n^{1-\alpha}\ge1`$, and
$`g(x)=\log_2x+\log_2e+o(1)`$ as $`x\to\infty`$. Consequently

```math
C(\Phi_{t_n}^{(n/2)})
\ge\alpha\log_2n-\log_2e+o(1),
\qquad
Q(\Phi_{t_n}^{(n/2)})
=O(\log n/n).
```

Meanwhile $`e^{-2t_n}\to1`$. Thus a diverging number of classical bits survives throughout a range of shrinking diffusion times after the quantum-transmission converse already applies.

This corollary follows from the finite bounds above; it does not require an additional approximation of the channel.

## 5. What remains distinct

The negative witness expectation for every fixed $`\nu<1`$ establishes a sharp distance-to-EB boundary. It does not prove positive unassisted quantum capacity at every such $`\nu`$. A quantum-capacity phase boundary is a different question.

The [residual-entanglement calculation](residual_entanglement.md) shows that some finite carriers can remain NPT beyond $`\nu=1`$ while the capacity upper bound tends to zero. Detecting an entangled Choi state, transmitting one state with high fidelity, and having a nonzero asymptotic quantum rate are different operational statements.

The same classical/quantum separation survives the [anisotropic bounds](anisotropic_diffusion.md). Classical capacity uses unitality and an entropy bound there, without assuming rotation covariance.

