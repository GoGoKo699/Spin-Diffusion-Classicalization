# The sharp operational threshold

[Model and claims](model.md) · [Communication](communication.md) · [Anisotropic diffusion](anisotropic_diffusion.md)

The proof has two parts. A coherent-state measurement supplies an explicit entanglement-breaking comparator at $`\nu=1`$. A two-level encoded Bell state supplies the converse at every fixed $`\nu<1`$.

## 1. An established measurement channel

Write $`|\Omega\rangle`$ for a spin coherent state and use normalized area measure $`d\Omega`$ on the unit sphere. Define

```math
\mathcal B_j(X)
=(n+1)\int_{S^2}
\langle\Omega|X|\Omega\rangle
|\Omega\rangle\langle\Omega|\,d\Omega.
```

The identity resolution $`(n+1)\int|\Omega\rangle\langle\Omega|\,d\Omega=I`$ makes this a channel. Its displayed measurement-and-preparation form makes it EB.

Its tensor-rank multipliers and exact random-rotation representation are **imported identities** from [Aschieri–Ruba–Solovej, Lemmas 12–13](../references/RELATED_WORK.md#exact-coherent-channel-kernel-aschieri-ruba-and-solovej):

```math
b_{n,\ell}
=\frac{n!(n+1)!}{(n-\ell)!(n+\ell+1)!},
\qquad
\mathcal B_j(X)
=\int_{\mathrm{SO}(3)}k_n(g)U_j(g)XU_j(g)^\dagger\,dg,
```

```math
k_n(\theta)=C_n\cos^{2n}(\theta/2),
\qquad
C_n=\frac{4^n n!(n+1)!}{(2n)!}.
```

Here $`\theta\in[0,\pi]`$ is the physical rotation angle and $`dg`$ is normalized Haar measure. In the SU(2) description the density has equal peaks at $`I`$ and $`-I`$. The adjoint channel identifies these two rotations, so the comparison below takes place on SO(3).

For a direct normalization check, SO(3)'s radial Haar density and integer-spin characters are

```math
w(\theta)=\frac2\pi\sin^2(\theta/2),
\qquad
\chi_\ell(\theta)=
\frac{\sin((\ell+\tfrac12)\theta)}{\sin(\theta/2)}.
```

The identity

```math
\sin^2(\theta/2)\chi_\ell(\theta)
=\tfrac12[\cos(\ell\theta)-\cos((\ell+1)\theta)]
```

and the finite cosine expansion of $`\cos^{2n}(\theta/2)`$ give
$`\int k_n\chi_\ell\,dg/(2\ell+1)=b_{n,\ell}`$.
The case $`\ell=0`$ proves normalization. The multiplicity-free decomposition of the adjoint spin representation then verifies the channel identity.

## 2. Classical probability controls the complete channel norm

The heat-kernel representation is

```math
\Phi_t^{(j)}(X)
=\int_{\mathrm{SO}(3)}p_t(g)U_j(g)XU_j(g)^\dagger\,dg,
\qquad
p_t(\theta)=\sum_{\ell=0}^{\infty}
(2\ell+1)e^{-t\ell(\ell+1)}\chi_\ell(\theta).
```

Conjugation by a unitary has diamond norm one, independently of the representation dimension. Therefore

```math
\frac12\|\Phi_t^{(j)}-\mathcal B_j\|_\diamond
\le\frac12\int|p_t(g)-k_n(g)|\,dg
=\mathrm{TV}(p_t,k_n).
```

This elementary transfer is part of the broader method developed by [Bardet and collaborators](../references/RELATED_WORK.md#group-transference-collective-decoherence-and-capacities-bardet-et-al). The required estimate here compares two sharply localized kernels at time $`1/n`$, rather than comparing the heat kernel with its uniform stationary law.

## 3. A uniform finite-size bound

We compare both radial probability distributions with the Maxwell density

```math
m_t(\theta)
=\frac{\theta^2}{2\sqrt{\pi}\,t^{3/2}}
e^{-\theta^2/(4t)},
\qquad
\theta\ge0,
\qquad
\mathbb E_{m_t}\theta^2=6t.
```

Densities on $`[0,\pi]`$ are extended by zero to the positive half-line. Since the group kernels are central, their total variation equals that of their radial distributions.

### The coherent-measurement kernel

Let $`r_n(\theta)=w(\theta)k_n(\theta)`$. At $`t=1/n`$,

```math
\frac{r_n(\theta)}{m_{1/n}(\theta)}
=A_n\mathrm{sinc}^2(\theta/2)
e^{n\theta^2/4}\cos^{2n}(\theta/2)
\le A_n,
\qquad
A_n=\frac{C_n}{\sqrt{\pi}n^{3/2}}.
```

Here $`\mathrm{sinc}x=\sin x/x`$. The inequality follows from
$`\log\cos x\le-x^2/2`$ for $`0\le x<\pi/2`$.

Both densities integrate to one. If $`r\le A m`$ for normalized densities, then
$`\mathrm{TV}(r,m)=\int(r-m)_+\le A-1`$.
Stirling's bounds give

```math
A_n\le(1+1/n)e^{1/(6n)},
\qquad
\mathrm{TV}(r_n,m_{1/n})
\le\frac{(7/6)e^{1/6}}n.
```

For completeness, write
$`n!=\sqrt{2\pi n}(n/e)^n e^{s_n}`$ with $`0<s_n<1/(12n)`$.
Then $`A_n=(1+1/n)e^{2s_n-s_{2n}}`$.
Finally $`(1+x)e^{x/6}-1\le(7/6)e^{1/6}x`$ for $`0\le x\le1`$.

### The heat kernel

Multiplying the character expansion by $`w`$ and applying Poisson summation to half-integer frequencies yields

```math
h_t(\theta):=w(\theta)p_t(\theta)
=\frac{e^{t/4}}{\sqrt{\pi}t^{3/2}}\sin(\theta/2)
\sum_{q\in\mathbb Z}(-1)^q(\theta-2\pi q)
e^{-(\theta-2\pi q)^2/(4t)}.
```

One can obtain the constants directly from

```math
\sum_{k\in\mathbb Z+1/2}e^{-tk^2}e^{ik\theta}
=\sqrt{\pi/t}\sum_{q\in\mathbb Z}(-1)^q
e^{-(\theta-2\pi q)^2/(4t)}
```

by taking minus its $`\theta`$ derivative and multiplying by
$`2e^{t/4}\sin(\theta/2)/\pi`$.

The zero-image term is
$`h_t^0=m_t e^{t/4}\mathrm{sinc}(\theta/2)`$.
For nonzero images, put $`x=\theta-2\pi q`$.
The absolute-radius intervals from $`q\ge1`$ are
$`[(2q-1)\pi,2q\pi]`$; those from $`q=-p\le-1`$ are
$`[2p\pi,(2p+1)\pi]`$. They partition $`[\pi,\infty)`$ once.
Because $`\sin(\theta/2)=(-1)^q\sin(x/2)`$,

```math
\int_0^\pi|h_t-h_t^0|\,d\theta
\le e^{t/4}\int_\pi^\infty
m_t(x)|\mathrm{sinc}(x/2)|\,dx
\le e^{t/4}\Pr_{m_t}\{\theta\ge\pi\}.
```

On $`[0,\pi]`$,
$`0\le1-\mathrm{sinc}(\theta/2)\le\theta^2/24`$.
For $`t\le1`$, the zero-image discrepancy has integral at most
$`(e^{t/4}-1)+e^{t/4}t/4\le e^{1/4}t/2`$.
Adding the image error and the missing Maxwell tail, dividing by two, and using
$`\Pr\{\theta\ge\pi\}\le6t/\pi^2`$ gives

```math
\mathrm{TV}(h_t,m_t)
\le
\left[\frac{e^{1/4}}4+
\frac{3(1+e^{1/4})}{\pi^2}\right]t.
```

Combining the two comparisons at $`t=1/n`$ establishes

```math
\mathrm{TV}(p_{1/n},k_n)
\le \frac{K_0}{n},
\qquad
K_0=
\frac76e^{1/6}+\frac14e^{1/4}
+\frac{3(1+e^{1/4})}{\pi^2}
=2.393520645\ldots<2.4.
```

This is a conservative bound, valid for every positive integer $`n`$.
For small $`n`$, use the trivial bound one if it is stronger.
No dimension-dependent conversion from Hilbert–Schmidt norm is used.

### Later times

For $`t\ge1/n`$, choose the explicit EB channel

```math
\mathcal E_{j,t}
=\Phi_{t-1/n}^{(j)}\circ\mathcal B_j.
```

Postprocessing preserves EB and contracts diamond distance. The semigroup property therefore gives

```math
\frac12\|\Phi_t^{(j)}-\mathcal E_{j,t}\|_\diamond
\le \min\{1,K_0/n\}.
```

This proves the upper half of Theorem 1, uniformly over all later times.

## 4. A two-level converse below the boundary

Choose $`|0\rangle=|j,j\rangle`$ and $`|1\rangle=|j,j-1\rangle`$.
Entangle these two levels with a reference qubit:

```math
|\beta_j\rangle
=\frac{|0\rangle_R|0\rangle_S+|1\rangle_R|1\rangle_S}{\sqrt2}.
```

Write a fundamental SU(2) rotation as

```math
u=\begin{pmatrix}a&b\\-\overline b&\overline a\end{pmatrix},
\qquad |a|^2+|b|^2=1.
```

The spin-$`j`$ representation is its $`n`$th symmetric power. Its highest-weight matrix elements obey

```math
U_{00}=a^n,\quad
|U_{10}|^2=|U_{01}|^2=n|b|^2|a|^{2n-2},
\quad
U_{11}=a^{n-2}(1-n|b|^2).
```

The last expression is used for $`n\ge2`$; its apparent singularity at $`n=1`$ is removable.

Let $`\rho_{RS}=(\mathrm{id}\otimes\Phi_{\nu/n}^{(j)})(|\beta_j\rangle\langle\beta_j|)`$.
The principal block of $`\rho_{RS}^{\Gamma_R}`$ on
$`|0\rangle_R|1\rangle_S,|1\rangle_R|0\rangle_S`$ is

```math
\frac12
\begin{pmatrix} A_n&B_n\\B_n&A_n\end{pmatrix},
\quad
A_n=\mathbb E[n|b|^2(1-|b|^2)^{n-1}],
\quad
B_n=\mathbb E[U_{11}\overline{U_{00}}].
```

The expectation is over the heat-kernel rotation. Inversion symmetry makes $`B_n`$ real.

For each fixed $`\nu>0`$, the exponential coordinates
$`X=\sqrt n\,\theta\,\widehat u`$ converge in total variation to
$`N(0,2\nu I_3)`$. This follows from the radial Maxwell comparison above and the uniform direction of a central kernel. Thus

```math
n|b|^2\longrightarrow
Z=\tfrac14(X_x^2+X_y^2),
\qquad
Z\sim\mathrm{Exp}(\text{mean }\nu).
```

The longitudinal phase that could oscillate in $`a^n`$ cancels in the relevant product:

```math
U_{11}\overline{U_{00}}
=\overline a^{\,2}|a|^{2n-4}(1-n|b|^2)
\longrightarrow e^{-Z}(1-Z).
```

The matrix elements are bounded, and their scaled-coordinate limits are uniform on compact sets. Gaussian tail truncation therefore justifies convergence of their expectations:

```math
A_n\longrightarrow\mathbb E[Ze^{-Z}]
=\frac{\nu}{(1+\nu)^2},
\qquad
B_n\longrightarrow\mathbb E[(1-Z)e^{-Z}]
=\frac1{(1+\nu)^2}.
```

For $`\nu<1`$, the antisymmetric unit vector $`|v\rangle`$ in this block has limiting negative expectation

```math
\langle v|\rho_{RS}^{\Gamma_R}|v\rangle
\longrightarrow-\frac{1-\nu}{2(1+\nu)^2}.
```

Set $`W=(|v\rangle\langle v|)^{\Gamma_R}`$. This witness has
$`\|W\|_\infty=1/2`$ and nonnegative expectation on every separable state $`\sigma`$. Hence

```math
-\mathrm{Tr}(W\rho_{RS})
\le|\mathrm{Tr}[W(\rho_{RS}-\sigma)]|
\le\tfrac12\|\rho_{RS}-\sigma\|_1.
```

Every EB channel produces such a separable $`\sigma`$ from the input Bell state. Taking the infimum over EB channels proves

```math
\liminf_{n\to\infty}e_{n/2}(\nu/n)
\ge \frac{1-\nu}{2(1+\nu)^2}.
```

At $`\nu=0`$, the input Bell state is unchanged and the same witness gives the stated lower bound directly. The vector $`v`$ only needs a negative expectation; it need not be an eigenvector of the entire partial transpose.

## 5. What makes the result uniform

The upper argument compares probability laws on the rotation group before choosing a representation. Its error therefore controls the complete spin channel even as the Hilbert space grows. The lower argument requires only two physical spin levels and a qubit reference. Together they avoid assuming that every possible encoding is confined to a semiclassical patch.

The lower witness and upper comparator have the same time normalization and distance convention. Their meeting point establishes the exact fixed-$`\nu`$ boundary. Their numerical prefactors need not match away from that boundary.

[Verification](../verification/README.md) compares the analytic kernel identity with quadrature and computes finite-spin witnesses from invariant Lindblad sectors. Those checks illustrate and check the formulas; the general norm and asymptotic statements follow from the proof above.

