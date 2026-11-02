"""Exact finite-spin reference witnesses and local generator checks.

These bounded checks do not compute an optimized diamond distance or a global
entanglement-breaking approximation.  See science/rank_two_diffusion.md.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal, expm
from scipy.sparse import diags
from scipy.special import gammaln


def spin_operators(n):
    """Jz basis |j,j-a>, j=n/2; [Jx,Jy]=iJz."""
    d = n + 1
    jp = np.diag(np.sqrt(np.arange(1, d) * np.arange(n, 0, -1)), 1)
    return (jp + jp.T) / 2, (jp - jp.T) / (2j), np.diag(n / 2 - np.arange(d))


def channel_blocks(n, t, rhos):
    """Exact -ad_Jx^2-ad_Jy^2 evolution by conserved coherence order.

    This is the original finite-spin generator, not an oscillator evolution.
    """
    d = n + 1
    j = n / 2
    outputs = [np.zeros((d, d), dtype=complex) for _ in rhos]
    for delta in range(-n, n + 1):
        a = np.arange(max(0, delta), min(d, d + delta))
        b = a - delta
        diagonal = -2 * j * (j + 1) + (j - a) ** 2 + (j - b) ** 2
        aa, bb = a[:-1], b[:-1]
        off = np.sqrt((n - aa) * (aa + 1) * (n - bb) * (bb + 1))
        values, vectors = eigh_tridiagonal(diagonal, off)
        assert values[-1] < 2e-10, "Diffusion generator acquired a positive eigenvalue"
        inputs = np.stack([rho[a, b] for rho in rhos], axis=1)
        evolved = vectors @ (np.exp(t * values)[:, None] * (vectors.T @ inputs))
        for output, column in zip(outputs, evolved.T):
            output[a, b] = column
    return outputs


def squeezed_code(n):
    """Normalized finite-ladder projections of S(r)|0>, S(r)|1>."""
    d = n + 1
    r = np.log(n) / 6
    inputs = np.zeros((d, 2))
    for a in range(d):
        k = a // 2
        if a % 2 == 0:
            logarithm = (0.5 * gammaln(2 * k + 1) - k * np.log(2)
                         - gammaln(k + 1) + k * np.log(np.tanh(r))
                         - 0.5 * np.log(np.cosh(r)))
            inputs[a, 0] = np.exp(logarithm)
        else:
            logarithm = (0.5 * gammaln(2 * k + 2) - k * np.log(2)
                         - gammaln(k + 1) + k * np.log(np.tanh(r))
                         - 1.5 * np.log(np.cosh(r)))
            inputs[a, 1] = np.exp(logarithm)
    retained = np.sum(inputs ** 2, axis=0)
    inputs /= np.sqrt(retained)
    assert np.linalg.norm(inputs.T @ inputs - np.eye(2)) < 1e-12
    return inputs, retained


def witness_case(n, s):
    """Noisy y,z axes with a z-pole code, evaluated after an exact rotation."""
    local, retained = squeezed_code(n)
    _, jy, jz = spin_operators(n)
    eigenvalues, vectors = eigh(jy)
    rotation = (vectors * np.exp(-1j * np.pi * eigenvalues / 2)) @ vectors.conj().T
    code = rotation @ local
    rhos = [np.outer(code[:, 0], code[:, 0].conj()),
            np.outer(code[:, 1], code[:, 1].conj()),
            np.outer(code[:, 0], code[:, 1].conj())]
    t = s * n ** (-2 / 3)
    outputs = channel_blocks(n, t, rhos)

    def element(rho, a, b):
        return np.vdot(code[:, a], rho @ code[:, b])

    d01 = element(outputs[0], 1, 1).real
    d10 = element(outputs[1], 0, 0).real
    coherence = element(outputs[2], 0, 1)
    block = np.array([[d01, coherence.conjugate()], [coherence, d10]]) / 2
    expectation = (d01 + d10 - 2 * abs(coherence)) / 4
    fidelity = (element(outputs[0], 0, 0).real
                + element(outputs[1], 1, 1).real + 2 * coherence.real) / 4
    marginal = local @ local.T / 2

    def variance(operator):
        mean = np.trace(marginal @ operator).real
        return np.trace(marginal @ operator @ operator).real - mean ** 2

    variance_sum = variance(jy) + variance(jz)
    fidelity_tangent = 1 - 2 * t * variance_sum
    trace_error = max(abs(np.trace(x) - 1) for x in outputs[:2])
    hermiticity = max(np.linalg.norm(x - x.conj().T) for x in outputs[:2])
    output_min = min(np.linalg.eigvalsh(x)[0] for x in outputs[:2])
    assert trace_error < 2e-10 and hermiticity < 2e-10
    assert output_min > -2e-10
    assert abs(d01 - d10) < 2e-10
    assert fidelity + 2e-10 >= fidelity_tangent
    assert abs(np.linalg.eigvalsh(block)[0] - expectation) < 2e-10
    if s <= 1:
        assert expectation < -0.035, "Registered finite-spin witness lost its NPT margin"
    excitation = np.sum(np.arange(n + 1)[:, None] * abs(local) ** 2, axis=0)
    return {
        "n": n, "scaled_time_s": s, "time_t": t,
        "pt_block_min": float(np.linalg.eigvalsh(block)[0]),
        "witness_expectation": float(expectation),
        "distance_lower_from_witness": float(max(0, -expectation)),
        "entanglement_fidelity": float(fidelity),
        "fidelity_tangent_lower": float(fidelity_tangent),
        "distance_lower_from_tangent": float(max(0, fidelity_tangent - 0.5)),
        "variance_sum": float(variance_sum),
        "variance_sum_over_n_two_thirds": float(variance_sum / n ** (2 / 3)),
        "predicted_variance_limit": 13 / 16,
        "mean_excitation": [float(x) for x in excitation],
        "retained_probability_before_normalization": [float(x) for x in retained],
        "tail_at_excitation_n_over_2": [float(x) for x in np.sum(abs(local[n // 2:]) ** 2, axis=0)],
        "trace_error": float(trace_error), "hermiticity_error": float(hermiticity),
        "population_output_min_eigenvalue": float(output_min),
    }


def independent_generator_controls():
    """Compare block evolution with an independent full Kronecker generator."""
    rows = []
    for n in (1, 2, 3, 4, 7):
        d = n + 1
        jx, jy, _ = spin_operators(n)
        generator = np.zeros((d * d, d * d), dtype=complex)
        for operator in (jx, jy):
            commutator = np.kron(np.eye(d), operator) - np.kron(operator.T, np.eye(d))
            generator -= commutator @ commutator
        random = np.random.default_rng(193 + n)
        vector = random.normal(size=d) + 1j * random.normal(size=d)
        vector /= np.linalg.norm(vector)
        rho = np.outer(vector, vector.conj())
        for t in (0, 0.03, 0.7):
            direct = (expm(t * generator) @ rho.reshape(-1, order="F")).reshape((d, d), order="F")
            blocks = channel_blocks(n, t, [rho])[0]
            error = np.linalg.norm(direct - blocks)
            trace_error = abs(np.trace(blocks) - 1)
            minimum = np.linalg.eigvalsh(blocks)[0]
            assert error < 1e-12 and trace_error < 1e-12 and minimum > -1e-12
            rows.append({"n": n, "t": t, "full_generator_error": float(error),
                         "trace_error": float(trace_error), "output_min_eigenvalue": float(minimum)})
    for n in (16, 32):
        initial = witness_case(n, 0)
        assert abs(initial["pt_block_min"] + 0.5) < 1e-12
        assert abs(initial["entanglement_fidelity"] - 1) < 1e-12
    return rows


def growing_excitation_checks():
    """Exact Jy and Jy^2 versus their limiting vectors on a squeezed vacuum."""
    rows = []
    for n in (64, 128, 256, 512, 1024, 2048, 4096):
        dim = n + 5
        r = np.log(n) / 6
        ch, sh = np.cosh(r), np.sinh(r)
        k = np.arange((dim + 1) // 2)
        even = np.exp(0.5 * gammaln(2 * k + 1) - k * np.log(2) - gammaln(k + 1)
                      + k * np.log(np.tanh(r)) - 0.5 * np.log(ch))
        v0 = np.zeros(dim)
        v0[2 * k] = even
        a = diags(np.sqrt(np.arange(1, dim)), 1, shape=(dim, dim), format="csr")
        v1 = (ch * a.T - sh * a) @ v0
        v2 = (ch * a.T - sh * a) @ v1 / np.sqrt(2)
        kk = np.arange(1, n + 1)
        jp = diags(np.r_[np.sqrt(kk * (n - kk + 1)), np.zeros(dim - n - 1)],
                   1, shape=(dim, dim), format="csr")
        jy = (jp - jp.T) / (2j)
        scaled = jy * n ** (-1 / 3)
        first_error = np.linalg.norm(scaled @ v0 - 1j * v1 / 2)
        second_error = np.linalg.norm(scaled @ (scaled @ v0) - (v0 - np.sqrt(2) * v2) / 4)
        mean_number = np.sum(np.arange(dim) * v0 ** 2)
        scaled_first = first_error * n ** (2 / 3)
        scaled_second = second_error * n ** (2 / 3)
        # Registered finite-case envelopes, not universal error constants.
        assert abs(np.linalg.norm(v0) - 1) < 1e-11
        assert scaled_first < 0.18 and scaled_second < 0.35
        assert mean_number < 0.3 * n ** (1 / 3)
        rows.append({"n": n, "error_A": float(first_error), "error_A_squared": float(second_error),
                     "n_two_thirds_times_error_A": float(scaled_first),
                     "n_two_thirds_times_error_A_squared": float(scaled_second),
                     "mean_excitation": float(mean_number),
                     "tail_above_spin_ladder": float(np.sum(v0[n + 1:] ** 2))})
    return rows


def run_checks(full=False):
    sizes = (16, 32, 64, 128, 256, 512) if full else (16, 32, 64, 128)
    controls = independent_generator_controls()
    witnesses = [witness_case(n, s) for n in sizes for s in (0.1, 0.5, 1.0, 2.0)]
    vectors = growing_excitation_checks()
    return {
        "model": "j=n/2; generator -ad_Jy^2-ad_Jz^2; t=s*n^(-2/3)",
        "code": "Normalized finite-ladder S(log(n)/6)|0>, S(log(n)/6)|1>; qubit reference",
        "scope": "Exact finite-spin witness and local generator/vector checks; no global EB upper or optimized diamond norm",
        "all_assertions_passed": True, "full_witness_grid": bool(full),
        "independent_generator_controls": controls,
        "max_full_generator_error": max(x["full_generator_error"] for x in controls),
        "finite_spin_witnesses": witnesses, "growing_excitation_generator_checks": vectors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "results" / "rank_two.json")
    parser.add_argument("--full", action="store_true", help="Also evaluate finite witnesses at n=256,512")
    args = parser.parse_args()
    report = run_checks(full=args.full)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(f"Rank-two checks passed; report: {args.output}")


if __name__ == "__main__":
    main()
