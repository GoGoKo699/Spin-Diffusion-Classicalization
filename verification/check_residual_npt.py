"""Independent checks of the residual-NPT theorem for spin diffusion.

Run from the repository root: python verification/check_residual_npt.py
Optional: --output PATH (default: verification/local_results/residual_npt.json).
Import run_checks() to obtain the report without writing a file.

Two independent calculations are compared:
  1. A dense Lindblad-generator exponential and its full normalized Choi matrix.
  2. The alternating scalar formula for the Choi partial-transpose singlet.

Larger-n scalar checks use Python's Decimal arithmetic, including Decimal.exp,
to avoid catastrophic cancellation. No arbitrary-precision package is needed.
The larger-n checks also compare a direct finite sum against the independent
Poisson heat-kernel representation minus the omitted representation tail.
Numerics validate formulas and conventions; the asymptotic theorem is proved
in science/residual_entanglement.md.
"""

from __future__ import annotations

import argparse
import json
import math
from decimal import Decimal, localcontext
from functools import lru_cache
from pathlib import Path

import numpy as np
from scipy.linalg import eigh


@lru_cache(maxsize=None)
def decimal_pi(precision: int) -> Decimal:
    """Gauss-Legendre iteration, with guard digits."""
    with localcontext() as context:
        context.prec = precision + 15
        one = Decimal(1)
        a, b, tau, multiplier = one, one / Decimal(2).sqrt(), one / 4, one
        for _ in range(math.ceil(math.log2(precision)) + 2):
            new_a = (a + b) / 2
            b = (a * b).sqrt()
            tau -= multiplier * (a - new_a) ** 2
            a = new_a
            multiplier *= 2
        value = (a + b) ** 2 / (4 * tau)
        context.prec = precision
        return +value


def spin_matrices(n: int) -> tuple[np.ndarray, ...]:
    d = n + 1
    raising = np.zeros((d, d), dtype=complex)
    for r in range(1, d):
        raising[r - 1, r] = math.sqrt(r * (n - r + 1))
    lowering = raising.conj().T
    return (
        (raising + lowering) / 2,
        (raising - lowering) / (2j),
        np.diag(n / 2 - np.arange(d)),
    )


def lindblad_spectrum(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Column-vectorization convention: vec([J,X])=(I kron J-J.T kron I)vec(X)."""
    identity = np.eye(n + 1)
    generator = np.zeros(((n + 1) ** 2,) * 2, dtype=complex)
    for operator in spin_matrices(n):
        commutator = np.kron(identity, operator) - np.kron(operator.T, identity)
        generator -= commutator @ commutator
    return eigh(generator)


def full_choi_check(n: int, nu: float, spectrum: tuple[np.ndarray, np.ndarray]) -> dict:
    d = n + 1
    eigenvalues, eigenvectors = spectrum
    channel = (eigenvectors * np.exp((nu / n) * eigenvalues)) @ eigenvectors.conj().T
    # Superoperator indices (a,b,c,e) become Choi indices (a,c,b,e).
    choi = channel.reshape((d, d, d, d), order="F").transpose(0, 2, 1, 3)
    choi = choi.reshape((d * d, d * d)) / d
    partial_transpose = choi.reshape((d, d, d, d)).transpose(0, 3, 2, 1)
    partial_transpose = partial_transpose.reshape((d * d, d * d))
    singlet = np.zeros(d * d, dtype=complex)
    for r in range(d):
        singlet[r * d + (n - r)] = (-1) ** r / math.sqrt(d)
    expected = math.fsum(
        (-1) ** ell * (2 * ell + 1) * math.exp(-(nu / n) * ell * (ell + 1))
        for ell in range(n + 1)
    ) / d ** 2
    actual = float(np.vdot(singlet, partial_transpose @ singlet).real)
    residual = float(np.linalg.norm(partial_transpose @ singlet - expected * singlet))
    result = {
        "n": n,
        "nu": nu,
        "singlet_from_full_choi": actual,
        "singlet_from_finite_sum": expected,
        "singlet_eigenvector_residual": residual,
        "choi_trace_error": float(abs(np.trace(choi) - 1)),
        "choi_min_eigenvalue": float(np.linalg.eigvalsh(choi)[0]),
        "partial_transpose_min_eigenvalue": float(np.linalg.eigvalsh(partial_transpose)[0]),
    }
    assert abs(actual - expected) < 5e-13, result
    assert residual < 5e-13, result
    assert result["choi_trace_error"] < 5e-13, result
    assert result["choi_min_eigenvalue"] > -5e-13, result
    return result


def scalar_check(n: int, nu_label: str) -> dict:
    # All chosen nu are below 2; this safely resolves sums as small as exp(-nu*n).
    precision = 90 + math.ceil(2 * n / math.log(10))
    with localcontext() as context:
        context.prec = precision
        pi = decimal_pi(precision)
        nu = pi / 2 if nu_label == "pi/2" else Decimal(nu_label)
        dn = Decimal(n)
        t = nu / dn
        finite_sum = sum(
            (Decimal((-1) ** ell * (2 * ell + 1))
             * (-t * ell * (ell + 1)).exp()
             for ell in range(n + 1)),
            Decimal(0),
        )
        scaling = dn * (-nu * dn).exp()
        scaled_finite_sum = finite_sum / scaling

        # Omitted tail, divided by n*exp(-nu*n); n is odd in these checks.
        tail = Decimal(0)
        cutoff = Decimal("1e-70")
        for k in range(10000):
            term = (2 + Decimal(3 + 2 * k) / dn) * (
                -nu * (3 + 2 * k) - nu * (k + 1) * (k + 2) / dn
            ).exp()
            tail += (-1) ** k * term
            if term < cutoff:
                break
        else:
            raise AssertionError("Tail cutoff not reached")

        # Heat kernel at angle pi, divided by n*exp(-nu*n).
        action = pi ** 2 * dn / (4 * nu)
        image_factor = Decimal(0)
        for k in range(1000):
            term = Decimal(2 * k + 1) * (-action * ((2 * k + 1) ** 2 - 1)).exp()
            image_factor += (-1) ** k * term
            if k and term < cutoff:
                break
        else:
            raise AssertionError("Image cutoff not reached")
        delta = pi ** 2 / (4 * nu) - nu
        scaled_heat = (pi / nu) ** Decimal("1.5") * dn.sqrt() * (
            nu / (4 * dn) - dn * delta
        ).exp() * image_factor
        reconstruction_error = abs(scaled_finite_sum - (scaled_heat - tail))

        q = (-2 * nu).exp()
        beta = 2 * (-3 * nu).exp() / (1 + q)
        error_coefficient = (-3 * nu).exp() * (
            (3 + 4 * nu) / (1 - q)
            + (2 + 6 * nu) * q / (1 - q) ** 2
            + 2 * nu * q * (1 + q) / (1 - q) ** 3
        )
        tail_limit_error = abs(tail - beta)
        assert reconstruction_error < Decimal("1e-55"), (n, nu_label, reconstruction_error)
        assert tail_limit_error <= error_coefficient / dn + Decimal("1e-60")

        # Alternating-series lower bound on the tail and upper bound on heat.
        first_tail = Decimal(2 * n + 3) * (-t * (n + 1) * (n + 2)).exp()
        tail_ratio = Decimal(2 * n + 5) / Decimal(2 * n + 3) * (-2 * t * (n + 2)).exp()
        heat_upper = (pi / t) ** Decimal("1.5") * (t / 4 - pi ** 2 / (4 * t)).exp()
        tail_lower = first_tail * (1 - tail_ratio)
        monotone_tail = t * (2 * n + 3) ** 2 >= 2
        certificate = bool(monotone_tail and t <= pi ** 2 / 2 and tail_lower > heat_upper)
        if certificate:
            assert finite_sum < 0

        def compact(value: Decimal) -> str:
            return format(value, ".24E")

        return {
            "n": n,
            "nu": nu_label,
            "decimal_precision": precision,
            "singlet_eigenvalue": compact(finite_sum / (dn + 1) ** 2),
            "scaled_finite_sum": compact(scaled_finite_sum),
            "scaled_tail": compact(tail),
            "tail_limit_beta": compact(beta),
            "scaled_heat": compact(scaled_heat),
            "heat_minus_tail_reconstruction_error": compact(reconstruction_error),
            "tail_limit_error": compact(tail_limit_error),
            "proved_tail_error_bound": compact(error_coefficient / dn),
            "negative_asymptotic_ratio": compact(-scaled_finite_sum / beta),
            "elementary_npt_certificate": certificate,
        }


def run_checks() -> dict:
    """Run the sampled full-Choi and high-precision checks; return a JSON-ready report."""
    dense = []
    for n in (1, 2, 3, 4, 5, 7, 9):
        spectrum = lindblad_spectrum(n)
        for nu in (0.0, 0.5, 1.0, 1.4, 1.7):
            dense.append(full_choi_check(n, nu, spectrum))
    scalar = [scalar_check(n, nu) for nu in ("1", "1.5", "1.55", "pi/2")
              for n in (11, 51, 151, 401)]
    # The first simple half-integer example at the operational threshold.
    scalar.append(scalar_check(5, "1"))
    return {
        "passed": True,
        "model": "Phi_t=exp[-t sum_a [J_a,[J_a,.]]], n=2j, nu=n*t; normalized Choi",
        "scope": "Singlet PT sector only; no claim about all-sector PPT or exact EB threshold",
        "proof": "science/residual_entanglement.md",
        "max_full_choi_formula_error": max(abs(x["singlet_from_full_choi"] - x["singlet_from_finite_sum"]) for x in dense),
        "max_singlet_eigenvector_residual": max(x["singlet_eigenvector_residual"] for x in dense),
        "full_choi_checks": dense,
        "high_precision_scalar_checks": scalar,
    }
def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parent / "local_results" / "residual_npt.json",
        help="JSON report path; parent directories are created if necessary.",
    )
    arguments = parser.parse_args(argv)
    report = run_checks()
    destination = arguments.output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "passed": True,
        "full_choi_cases": len(report["full_choi_checks"]),
        "high_precision_cases": len(report["high_precision_scalar_checks"]),
        "max_full_choi_formula_error": report["max_full_choi_formula_error"],
        "max_singlet_eigenvector_residual": report["max_singlet_eigenvector_residual"],
        "report": str(destination),
    }, indent=2))


if __name__ == "__main__":
    main()
