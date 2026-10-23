"""Run the three bounded scientific checks and record versions and outputs."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import platform
import time

from check_core import run_checks as check_core
from check_anisotropic import run_checks as check_anisotropic
from check_residual_npt import run_checks as check_residual_npt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).parent / "local_results")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    manifest = {
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "packages": {name: importlib.metadata.version(name)
                     for name in ("numpy", "scipy", "matplotlib")},
        "scope": "Finite numerical consistency checks; analytical proofs are in science/.",
        "checks": [],
    }
    for name, function in (("core", check_core),
                           ("anisotropic", check_anisotropic),
                           ("residual_npt", check_residual_npt)):
        print(f"Running {name} checks...", flush=True)
        before = time.monotonic()
        report = function()
        destination = args.output_dir / f"{name}.json"
        destination.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
        elapsed = round(time.monotonic() - before, 3)
        manifest["checks"].append({"name": name, "all_assertions_passed": True,
                                   "elapsed_seconds": elapsed,
                                   "report": destination.name})
        print(f"  Passed; report: {destination.name}", flush=True)
    manifest["all_assertions_passed"] = True
    manifest["elapsed_seconds"] = round(time.monotonic() - started, 3)
    (args.output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
