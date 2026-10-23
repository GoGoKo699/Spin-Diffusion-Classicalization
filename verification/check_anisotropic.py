"""Sampled finite-spin consistency checks of the anisotropic Bell witness.

Builds the full double-commutator superoperator, rather than implementing
the limiting formula as a dynamical model. The selected finite-size errors
are checked for convergence toward the analytic limit. These sampled checks
are not an asymptotic proof; see science/anisotropic_diffusion.md.

Run from the repository root: python verification/check_anisotropic.py
Optional: --output PATH (default: verification/local_results/anisotropic.json).
Import run_checks() to obtain the report without writing a file.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply


def spin_matrices(n):
    d = n + 1
    # Basis |r> = |j, j-r>, r=0,...,n.
    r = np.arange(1, d)
    jp = sparse.diags(np.sqrt(r * (n-r+1)), 1, shape=(d, d), dtype=complex)
    jm = jp.T.conjugate()
    jx = (jp + jm) / 2
    jy = (jp - jm) / (2j)
    jz = sparse.diags(n/2 - np.arange(d), dtype=complex)
    return [jx.tocsr(), jy.tocsr(), jz.tocsr()]


def exact_block(n, diffusion, tau):
    """Return the PT-block eigenvalue, diagonal symmetry error, and Hermiticity error.

    Both coherence matrix units are propagated independently, so the
    Hermiticity check is not imposed by conjugating one computed entry.
    """
    d = n + 1
    eye = sparse.eye(d, format="csr", dtype=complex)
    ad = [sparse.kron(eye, J, format="csr")
          - sparse.kron(J.T, eye, format="csr") for J in spin_matrices(n)]
    generator = sparse.csr_matrix((d*d, d*d), dtype=complex)
    for a in range(3):
        for b in range(3):
            if diffusion[a, b] != 0:
                generator -= diffusion[a, b] * (ad[a] @ ad[b])
    initial = np.zeros((d*d, 4), dtype=complex)
    initial[0, 0] = 1                  # |0><0|
    initial[1+d, 1] = 1                # |1><1|
    initial[1, 2] = 1                  # |1><0|
    initial[d, 3] = 1                  # |0><1|
    evolved = expm_multiply((tau/n) * generator, initial)
    a0 = evolved[1+d, 0]
    a1 = evolved[0, 1]
    b = evolved[1, 2]
    b_conjugate = evolved[d, 3]
    block = np.array([[a0, b], [b_conjugate, a1]]) / 2
    hermitian_error = float(np.linalg.norm(block - block.conjugate().T))
    value = float(np.linalg.eigvalsh((block+block.conjugate().T)/2)[0])
    return value, float(abs(a0-a1)), hermitian_error


CASES = (
    ("generic_diagonal", np.diag([1., 2., 5.]), 0.5),
    ("sharp_axial_family", np.diag([1., 1., 5.]), 0.8),
    ("longitudinal_cross_terms",
     np.array([[1., .3, .4], [.3, 2., .2], [.4, .2, 5.]]), 0.5),
    ("rank_two_at_late_scaled_time", np.diag([0., 1., 3.]), 2.),
)
SPIN_SIZES = (16, 32, 64)
SYMMETRY_TOLERANCE = 1e-10


def predicted_limit(diffusion, tau):
    """Analytic limit at the pole along the third coordinate axis."""
    tangent = diffusion[:2, :2]
    determinant = float(np.linalg.det(tangent))
    return float(-(1-tau*tau*determinant) / (
        2 * np.linalg.det(np.eye(2) + tau*tangent)**1.5)
    )


def run_checks() -> dict:
    """Run four selected finite-size sequences; return a JSON-ready report.

    Monotone error reduction and the endpoint sign below are assertions
    about these registered samples only, not general finite-n theorems.
    """
    results = []
    for name, diffusion, tau in CASES:
        predicted = predicted_limit(diffusion, tau)
        rows = []
        for n in SPIN_SIZES:
            value, a_error, h_error = exact_block(n, diffusion, tau)
            row = {
                "n": n,
                "lambda_minus": value,
                "difference_from_limit": float(value-predicted),
                "diagonal_symmetry_error": a_error,
                "hermiticity_error": h_error,
            }
            assert np.isfinite([value, a_error, h_error]).all(), (name, row)
            assert a_error < SYMMETRY_TOLERANCE, (name, row)
            assert h_error < SYMMETRY_TOLERANCE, (name, row)
            rows.append(row)

        absolute_errors = [abs(row["difference_from_limit"]) for row in rows]
        assert all(later < earlier for earlier, later in zip(
            absolute_errors, absolute_errors[1:])), (name, rows)
        assert absolute_errors[-1] < 0.5 * absolute_errors[0], (name, rows)
        assert rows[-1]["lambda_minus"] < 0, (name, rows)
        results.append({
            "case": name,
            "D": diffusion.tolist(),
            "tau": tau,
            "predicted_limit": predicted,
            "sampled_convergence_passed": True,
            "rows": rows,
        })

    all_rows = [row for result in results for row in result["rows"]]
    return {
        "passed": True,
        "model": "L_D=-sum_ab D_ab [J_a,[J_b,.]], n=2j, t=tau/n",
        "scope": "Sampled finite-spin consistency checks, not a proof of an asymptotic rate or threshold",
        "proof": "science/anisotropic_diffusion.md",
        "sampled_spin_sizes": list(SPIN_SIZES),
        "sampled_convergence_criterion": "Absolute errors decrease at each listed size; final error is below half the first; final witness is negative",
        "symmetry_tolerance": SYMMETRY_TOLERANCE,
        "max_diagonal_symmetry_error": max(row["diagonal_symmetry_error"] for row in all_rows),
        "max_hermiticity_error": max(row["hermiticity_error"] for row in all_rows),
        "cases": results,
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parent / "local_results" / "anisotropic.json",
        help="JSON report path; parent directories are created if necessary.",
    )
    arguments = parser.parse_args(argv)
    report = run_checks()
    destination = arguments.output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "passed": True,
        "sampled_cases": len(report["cases"]),
        "finite_spin_checks": sum(len(case["rows"]) for case in report["cases"]),
        "max_diagonal_symmetry_error": report["max_diagonal_symmetry_error"],
        "max_hermiticity_error": report["max_hermiticity_error"],
        "report": str(destination),
    }, indent=2))


if __name__ == "__main__":
    main()
