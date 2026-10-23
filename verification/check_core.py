"""Numerical verification of the isotropic spin-diffusion core.

Convention: n=2j, Phi_t=exp[-t sum_a [J_a,[J_a,.]]], nu=n*t.
All angle densities use normalized SO(3) Haar measure and theta in [0, pi].

Public plotting helpers:
    berezin_radial_density(theta, n)
    heat_radial_poisson(theta, t)
    heat_radial_character(theta, t)
    berezin_scaled_radial(u, n)
    heat_scaled_radial(u, t, method="poisson")
    berezin_multiplier(n, ell)
    bell_block_entries(n, nu)
    bell_block_eigenvalue(n, nu)

The scaled radius is u=theta/(2*sqrt(t)); for the Berezin kernel t=1/n.
The script checks independent formulas and exact finite-spin evolution.
Numerical quadrature is validation, not a replacement for the analytic proof.
Dependencies: Python standard library, NumPy, SciPy.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import json
import math
from pathlib import Path
import warnings

import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.special import erfc, gammaln
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply


K0 = ((7.0 / 6.0) * math.exp(1.0 / 6.0)
      + math.exp(1.0 / 4.0) / 4.0
      + 3.0 * (1.0 + math.exp(1.0 / 4.0)) / math.pi**2)
KERNEL_NS = (1, 2, 5, 10, 50, 200, 1000)
FOURIER_NS = (1, 2, 3, 4, 10, 30)
BELL_NS = (2, 10, 50, 200, 1000)
BELL_NUS = (0.25, 0.5, 0.9, 1.0, 1.2)
MAX_SCALED_RADIUS = 12.0


def _positive_integer(n: int) -> int:
    if int(n) != n or n < 1:
        raise ValueError("n must be a positive integer")
    return int(n)


def _positive_time(t: float) -> float:
    t = float(t)
    if not math.isfinite(t) or t <= 0:
        raise ValueError("a radial heat density requires finite t > 0")
    return t


def _scalar_or_array(value):
    value = np.asarray(value)
    return float(value) if value.ndim == 0 else value


@lru_cache(maxsize=None)
def berezin_log_normalizer(n: int) -> float:
    """Log C_n, using the equivalent gamma ratio to reduce cancellation."""
    n = _positive_integer(n)
    return float(0.5 * math.log(math.pi)
                 + gammaln(n + 2.0) - gammaln(n + 0.5))


def haar_radial_density(theta):
    theta = np.asarray(theta, dtype=float)
    result = (2.0 / math.pi) * np.sin(theta / 2.0)**2
    return _scalar_or_array(np.where((theta >= 0) & (theta <= math.pi),
                                    result, 0.0))


def berezin_class_density(theta, n: int):
    """Central density C_n cos(theta/2)^(2n), relative to normalized Haar."""
    n = _positive_integer(n)
    theta = np.asarray(theta, dtype=float)
    inside = (theta >= 0) & (theta <= math.pi)
    clipped = np.clip(theta, 0.0, math.pi)
    sin_squared = np.clip(np.sin(clipped / 2.0)**2, 0.0, 1.0)
    with np.errstate(divide="ignore"):
        log_density = berezin_log_normalizer(n) + n * np.log1p(-sin_squared)
    return _scalar_or_array(np.where(inside, np.exp(log_density), 0.0))


def berezin_radial_density(theta, n: int):
    return _scalar_or_array(np.asarray(haar_radial_density(theta))
                            * np.asarray(berezin_class_density(theta, n)))


def heat_radial_poisson(theta, t: float):
    """SO(3) heat radial density from the alternating image sum."""
    t = _positive_time(t)
    theta = np.asarray(theta, dtype=float)
    inside = (theta >= 0) & (theta <= math.pi)
    clipped = np.clip(theta, 0.0, math.pi)
    # The first omitted image lies beyond an exponent of at least 50.
    # All verification times satisfy t<=1; this also works for larger t,
    # although the character representation is preferable there.
    q_max = max(1, int(math.ceil(0.5 + math.sqrt(50.0*t)/math.pi)))
    q = np.arange(-q_max, q_max+1)
    x = clipped[..., None] - 2.0*math.pi*q
    signs = np.where(q % 2 == 0, 1.0, -1.0)
    image_sum = np.sum(signs*x*np.exp(-x*x/(4.0*t)), axis=-1)
    result = (math.exp(t/4.0) / (math.sqrt(math.pi)*t**1.5)
              * np.sin(clipped/2.0) * image_sum)
    return _scalar_or_array(np.where(inside, result, 0.0))


@lru_cache(maxsize=32)
def _heat_character_terms(t: float):
    t = _positive_time(t)
    # Include a power-of-t allowance for the polynomial character weights.
    exponent = 50.0 + 4.0*max(0.0, math.log(1.0/t))
    l_max = int(math.ceil(math.sqrt(exponent/t))) + 2
    ell = np.arange(l_max+1, dtype=float)
    weights = (2.0*ell+1.0)**2 * np.exp(-t*ell*(ell+1.0))
    return ell, weights


def heat_radial_character(theta, t: float):
    """Independent SO(3) heat formula from its integer-spin character sum."""
    t = _positive_time(t)
    theta = np.asarray(theta, dtype=float)
    inside = (theta >= 0) & (theta <= math.pi)
    clipped = np.clip(theta, 0.0, math.pi)
    ell, weights = _heat_character_terms(t)
    normalized_character = (
        np.sinc(clipped[..., None]*(ell+0.5)/math.pi)
        / np.sinc(clipped[..., None]/(2.0*math.pi)))
    class_density = np.sum(normalized_character*weights, axis=-1)
    result = (2.0/math.pi)*np.sin(clipped/2.0)**2*class_density
    return _scalar_or_array(np.where(inside, result, 0.0))


def berezin_scaled_radial(u, n: int):
    """Density in u=sqrt(n)*theta/2, including its change-of-variable factor."""
    n = _positive_integer(n)
    factor = 2.0/math.sqrt(n)
    return _scalar_or_array(factor*np.asarray(
        berezin_radial_density(factor*np.asarray(u), n)))


def heat_scaled_radial(u, t: float, method: str = "poisson"):
    """Density in u=theta/(2sqrt(t)), including its Jacobian."""
    t = _positive_time(t)
    factor = 2.0*math.sqrt(t)
    theta = factor*np.asarray(u)
    if method == "poisson":
        result = heat_radial_poisson(theta, t)
    elif method == "character":
        result = heat_radial_character(theta, t)
    else:
        raise ValueError("method must be 'poisson' or 'character'")
    return _scalar_or_array(factor*np.asarray(result))


def maxwell_scaled_density(u):
    u = np.asarray(u, dtype=float)
    result = 4.0/math.sqrt(math.pi)*u*u*np.exp(-u*u)
    return _scalar_or_array(np.where(u >= 0, result, 0.0))


def maxwell_scaled_tail(u: float) -> float:
    return float(erfc(u) + 2.0/math.sqrt(math.pi)*u*math.exp(-u*u))


def scaled_integration_interval(n: int):
    n = _positive_integer(n)
    physical_upper = math.pi*math.sqrt(n)/2.0
    return min(physical_upper, MAX_SCALED_RADIUS), physical_upper


def _integrate_scaled(function, upper: float):
    points = [x for x in (0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0)
              if x < upper]
    with warnings.catch_warnings():
        warnings.simplefilter("error", IntegrationWarning)
        value, error = quad(function, 0.0, upper, points=points,
                            epsabs=3e-12, epsrel=3e-11, limit=250)
    return float(value), float(error)


def berezin_multiplier(n: int, ell: int) -> float:
    n = _positive_integer(n)
    if int(ell) != ell or ell < 0:
        raise ValueError("ell must be a nonnegative integer")
    ell = int(ell)
    if ell == 0:
        return 1.0
    if ell > n:
        return 0.0
    return float(math.exp(gammaln(n+1)+gammaln(n+2)
                         - gammaln(n-ell+1)-gammaln(n+ell+2)))


def berezin_fourier_integral(n: int, ell: int):
    """Integral of chi_ell/(2ell+1) against the exact rotation density."""
    n = _positive_integer(n)
    if int(ell) != ell or ell < 0:
        raise ValueError("ell must be a nonnegative integer")
    ell = int(ell)
    upper, _ = scaled_integration_interval(n)

    def integrand(u):
        theta = 2.0*u/math.sqrt(n)
        normalized_character = (np.sinc((ell+0.5)*theta/math.pi)
                                / np.sinc(theta/(2.0*math.pi)))
        return berezin_scaled_radial(u, n)*normalized_character

    return _integrate_scaled(integrand, upper)


@lru_cache(maxsize=None)
def _bell_generators(n: int):
    n = _positive_integer(n)
    r = np.arange(n+1, dtype=float)
    birth = (n-r)*(r+1)
    death = r*(n-r+1)
    population = diags([birth[:-1], -(birth+death), death[1:]],
                       [-1, 0, 1], format="csr")
    r = np.arange(n, dtype=float)
    off = np.sqrt((n-r[:-1]-1)*(n-r[:-1])*(r[:-1]+1)*(r[:-1]+2))
    coherence = diags([off, -2.0*(r+1)*(n-r), off],
                      [-1, 0, 1], format="csr")
    return population, coherence


@lru_cache(maxsize=None)
def bell_block_entries(n: int, nu: float):
    """Exact finite-n Bell block via invariant population/coherence sectors.

    A=<1|Phi(|0><0|)|1>, B=<1|Phi(|1><0|)|0>.
    The selected partial-transpose block is [[A,B],[B,A]]/2.
    """
    n = _positive_integer(n)
    nu = float(nu)
    if not math.isfinite(nu) or nu < 0:
        raise ValueError("nu must be finite and nonnegative")
    population, coherence = _bell_generators(n)
    initial_population = np.zeros(n+1)
    initial_population[0] = 1.0
    initial_coherence = np.zeros(n)
    initial_coherence[0] = 1.0
    t = nu/n
    probabilities = expm_multiply(t*population, initial_population)
    coherences = expm_multiply(t*coherence, initial_coherence)
    a = float(probabilities[1])
    b = float(coherences[0])
    return {
        "n": n, "nu": nu, "A": a, "B": b,
        "lambda_minus": (a-b)/2.0,
        "limiting_eigenvalue": (nu-1.0)/(2.0*(1.0+nu)**2),
        "population_trace": float(probabilities.sum()),
        "minimum_population": float(probabilities.min()),
        "minimum_coherence_sector_entry": float(coherences.min()),
    }


def bell_block_eigenvalue(n: int, nu: float) -> float:
    return float(bell_block_entries(n, nu)["lambda_minus"])


def check_scaled_kernel(n: int):
    t = 1.0/n
    upper, physical_upper = scaled_integration_interval(n)
    berezin_norm, berezin_error = _integrate_scaled(
        lambda u: berezin_scaled_radial(u, n), upper)
    heat_norm, heat_error = _integrate_scaled(
        lambda u: heat_scaled_radial(u, t), upper)
    character_norm, character_error = _integrate_scaled(
        lambda u: heat_scaled_radial(u, t, "character"), upper)
    twice_tv, tv_error = _integrate_scaled(
        lambda u: abs(heat_scaled_radial(u, t)
                      - berezin_scaled_radial(u, n)), upper)
    tv = twice_tv/2.0

    # For a truncated scaled interval, bound the omitted probability by the
    # Maxwell domination from the analytic proof, rather than assuming zero.
    if upper < physical_upper:
        maxwell_tail = maxwell_scaled_tail(upper)
        a_n = math.exp(berezin_log_normalizer(n)
                       - 0.5*math.log(math.pi)-1.5*math.log(n))
        berezin_tail_bound = a_n*maxwell_tail
        heat_tail_bound = 2.0*math.exp(t/4.0)*maxwell_tail
    else:
        berezin_tail_bound = heat_tail_bound = 0.0
    tv_tail_bound = (berezin_tail_bound+heat_tail_bound)/2.0

    probes = np.array(sorted(set(
        [u for u in (0., .07, .2, .5, 1., 1.358, 2., 3., 5., 8.)
         if u <= physical_upper] + [physical_upper])))
    poisson_values = np.asarray(heat_scaled_radial(probes, t))
    character_values = np.asarray(heat_scaled_radial(probes, t, "character"))
    heat_formula_error = float(np.max(np.abs(poisson_values-character_values)))

    assert abs(berezin_norm-1.0) <= 2e-9 + berezin_tail_bound, (n, berezin_norm)
    assert abs(heat_norm-1.0) <= 2e-9 + heat_tail_bound, (n, heat_norm)
    assert abs(character_norm-1.0) <= 2e-9 + heat_tail_bound, (n, character_norm)
    assert heat_formula_error < 2e-10, (n, heat_formula_error)
    assert poisson_values.min() >= -2e-12, (n, poisson_values.min())
    assert 0.0 <= tv <= 1.0 + 2e-10, (n, tv)
    assert tv + tv_error/2.0 + tv_tail_bound < K0/n, (n, tv, K0/n)

    return {
        "n": n, "t": t, "scaled_upper_integrated": upper,
        "scaled_physical_upper": physical_upper,
        "berezin_normalization": berezin_norm,
        "heat_poisson_normalization": heat_norm,
        "heat_character_normalization": character_norm,
        "normalization_quad_error_estimates": {
            "berezin": berezin_error, "poisson": heat_error,
            "character": character_error},
        "heat_formula_max_scaled_density_difference": heat_formula_error,
        "heat_formula_probe_u": probes.tolist(),
        "tv": tv, "n_times_tv": n*tv,
        "tv_quad_error_estimate": tv_error/2.0,
        "tv_omitted_tail_bound": tv_tail_bound,
        "theorem_tv_upper_bound": K0/n,
        "theorem_margin_including_numerical_error":
            K0/n-tv-tv_error/2.0-tv_tail_bound,
    }


def run_checks():
    assert K0 < 2.4
    kernel_rows = [check_scaled_kernel(n) for n in KERNEL_NS]

    fourier_rows = []
    for n in FOURIER_NS:
        entries = []
        for ell in range(n+1):
            numerical, error = berezin_fourier_integral(n, ell)
            exact = berezin_multiplier(n, ell)
            discrepancy = abs(numerical-exact)
            assert discrepancy < 2e-10, (n, ell, numerical, exact)
            entries.append({"ell": ell, "integral": numerical,
                            "factorial_multiplier": exact,
                            "absolute_error": discrepancy,
                            "quad_error_estimate": error})
        fourier_rows.append({"n": n, "max_absolute_error": max(
            item["absolute_error"] for item in entries), "entries": entries})

    # The exactly solvable spin-1/2 channel independently fixes sector
    # indexing and the factor of two in physical time.
    qubit_rows = []
    for nu in (0.0, 0.25, 0.5, 1.0):
        row = dict(bell_block_entries(1, nu))
        expected_a = (1.0-math.exp(-2.0*nu))/2.0
        expected_b = math.exp(-2.0*nu)
        assert abs(row["A"]-expected_a) < 2e-12
        assert abs(row["B"]-expected_b) < 2e-12
        qubit_rows.append(row)

    bell_rows = []
    for nu in BELL_NUS:
        for n in BELL_NS:
            row = dict(bell_block_entries(n, nu))
            assert abs(row["population_trace"]-1.0) < 2e-9, row
            assert row["minimum_population"] >= -2e-12, row
            assert row["minimum_coherence_sector_entry"] >= -2e-12, row
            assert -2e-12 <= row["A"] <= 1.0+2e-12, row
            assert abs(row["B"]) <= 1.0+2e-12, row
            if nu >= 1.0:
                # This normalized witness cannot exceed the proven
                # half-diamond distance to the explicit EB comparator.
                assert max(0.0, -row["lambda_minus"]) <= K0/n + 2e-10, row
            if n == 1000 and nu < 1.0:
                assert row["lambda_minus"] < 0.0, row
            row["difference_from_limiting_eigenvalue"] = (
                row["lambda_minus"]-row["limiting_eigenvalue"])
            bell_rows.append(row)

    return {
        "convention": "n=2j; Phi_t=exp(-t sum_a [J_a,[J_a,.]]); nu=n*t",
        "group_measure": "normalized SO(3) Haar; radial density (2/pi)sin²(theta/2)",
        "K0": K0,
        "scaled_radius": "u=theta/(2sqrt(t)); Berezin comparison uses t=1/n",
        "interpretation": "Numerical validation of analytic claims; quadrature errors are estimates.",
        "kernel_checks": kernel_rows,
        "berezin_fourier_checks": fourier_rows,
        "qubit_exact_checks": qubit_rows,
        "bell_sector_checks": bell_rows,
        "summary": {
            "kernel_cases": len(kernel_rows),
            "fourier_multipliers": sum(len(row["entries"]) for row in fourier_rows),
            "bell_sector_cases": len(bell_rows),
            "max_kernel_normalization_error": max(
                abs(row[key]-1.0) for row in kernel_rows for key in
                ("berezin_normalization", "heat_poisson_normalization",
                 "heat_character_normalization")),
            "max_heat_formula_scaled_density_difference": max(
                row["heat_formula_max_scaled_density_difference"] for row in kernel_rows),
            "max_fourier_multiplier_error": max(
                row["max_absolute_error"] for row in fourier_rows),
            "max_bell_population_trace_error": max(
                abs(row["population_trace"]-1.0) for row in bell_rows),
            "all_assertions_passed": True,
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).parent / "local_results" / "core.json",
                        help="JSON output path (default: verification/local_results/core.json)")
    args = parser.parse_args(argv)
    results = run_checks()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, allow_nan=False)+"\n")
    print(json.dumps(results["summary"], indent=2))
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()
