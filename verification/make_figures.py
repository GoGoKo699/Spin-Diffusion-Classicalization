"""Generate the two scientific figures from recorded numerical reports."""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def configure():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.titlesize": 12, "axes.labelsize": 10,
        "legend.fontsize": 9, "axes.spines.top": False,
        "axes.spines.right": False, "svg.hashsalt": "spin-diffusion",
        "svg.fonttype": "none", "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })


def save(fig, destination, png_dir):
    fig.savefig(destination, metadata={"Date": None}, bbox_inches="tight")
    if png_dir is not None:
        png_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(png_dir / (destination.stem + ".png"), dpi=180,
                    bbox_inches="tight")
    plt.close(fig)


def operational_figure(core):
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.35), layout="constrained")
    ax = axes[0]
    rows = core["kernel_checks"]
    n = np.array([r["n"] for r in rows])
    tv = np.array([r["tv"] for r in rows])
    grid = np.geomspace(1, 1000, 300)
    ax.loglog(grid, np.minimum(1, core["K0"] / grid), "--", color="#a55d16",
              lw=1.8, label=r"Proved bound $\min(1,K_0/n)$")
    ax.loglog(n, tv, "o-", color="#007b7f", lw=1.8, ms=5,
              label="Computed kernel total variation")
    ax.set(xlabel=r"Spin size $n=2j$", ylabel="Total variation",
           title="A  Uniform upper comparison")
    ax.grid(alpha=.18, which="both")
    ax.legend(loc="upper right", frameon=False)

    ax = axes[1]
    nu = np.linspace(0, 1.25, 350)
    bound = np.maximum(0, (1-nu) / (2*(1+nu)**2))
    ax.plot(nu, bound, color="#25334a", lw=2.1, label="Proved large-spin witness limit")
    palette = [(10, "#e49a30", "s"), (50, "#6d65a5", "^"),
               (1000, "#008d84", "o")]
    for n_value, color, marker in palette:
        selected = sorted((r for r in core["bell_sector_checks"] if r["n"] == n_value),
                          key=lambda r: r["nu"])
        ax.scatter([r["nu"] for r in selected],
                   [max(0, -r["lambda_minus"]) for r in selected],
                   color=color, marker=marker, s=42 if n_value != 1000 else 24,
                   label=fr"Finite spin: $n={n_value}$", zorder=3)
    ax.axvline(1, color="#8b919a", ls=":", lw=1.3)
    ax.set(xlabel=r"Scaled diffusion time $\nu=nt$",
           ylabel="Witness lower bound on distance to EB",
           xlim=(0, 1.26), ylim=(-.015, .52),
           title="B  Matching subthreshold converse")
    ax.grid(alpha=.18)
    ax.legend(loc="upper right", frameon=False)
    return fig


def residual_figure(residual):
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.35), layout="constrained")
    for label, color, marker in [("1", "#007b7f", "o"), ("1.5", "#965ca0", "s")]:
        rows = sorted((r for r in residual["high_precision_scalar_checks"]
                       if r["nu"] == label and Decimal(r["singlet_eigenvalue"]) < 0),
                      key=lambda r: r["n"])
        n = np.array([r["n"] for r in rows])
        with localcontext() as ctx:
            ctx.prec = 60
            logarithms = [float((-Decimal(r["singlet_eigenvalue"])).log10()) for r in rows]
            ratios = [float(-Decimal(r["scaled_finite_sum"]) /
                            Decimal(r["tail_limit_beta"]) *
                            Decimal(r["n"])**2 / Decimal(r["n"]+1)**2) for r in rows]
        nu = float(label)
        beta = math.exp(-2*nu) / math.cosh(nu)
        grid = np.linspace(n.min(), 401, 350)
        asymptotic_log = math.log10(beta) - nu*grid/math.log(10) - np.log10(grid)
        axes[0].plot(grid, asymptotic_log, "--", color=color, lw=1.4)
        axes[0].plot(n, logarithms, linestyle="none", marker=marker, ms=6,
                     color=color, label=fr"Exact finite sum, $\nu={label}$")
        axes[1].plot(n, ratios, marker=marker, ms=5, lw=1.4,
                     color=color, label=fr"$\nu={label}$")
    axes[0].plot([], [], "--", color="#7c828a", label="Leading asymptotic")
    axes[0].set(xlabel=r"Odd spin size $n=2j$",
                ylabel=r"$\log_{10}(-\lambda_{0,n})$",
                title="A  Negative, but exponentially small")
    axes[0].legend(frameon=False, loc="lower left")
    axes[1].axhline(1, color="#7c828a", ls="--", lw=1.3, label="Asymptotic limit")
    axes[1].set(xlabel=r"Odd spin size $n=2j$", ylabel="Exact eigenvalue / leading asymptotic",
                title="B  Convergence of the signed formula", ylim=(0, 1.07))
    axes[1].legend(frameon=False, loc="lower right")
    for ax in axes:
        ax.set_xlim(0, 415)
        ax.grid(alpha=.18)
    return fig


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-dir", type=Path, default=root / "verification" / "results")
    parser.add_argument("--output-dir", type=Path, default=root / "figures")
    parser.add_argument("--png-dir", type=Path, help="Optional raster previews for inspection")
    args = parser.parse_args()
    configure()
    core = json.loads((args.results_dir / "core.json").read_text())
    residual = json.loads((args.results_dir / "residual_npt.json").read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for filename, figure in [
        ("operational_threshold.svg", operational_figure(core)),
        ("residual_entanglement.svg", residual_figure(residual)),
    ]:
        destination = args.output_dir / filename
        save(figure, destination, args.png_dir)
        print(destination)


if __name__ == "__main__":
    main()
