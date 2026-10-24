"""Run the three bounded scientific checks and record versions and outputs."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import platform
import tempfile
import time

from check_core import run_checks as check_core
from check_anisotropic import run_checks as check_anisotropic
from check_residual_npt import run_checks as check_residual_npt


def write_manifest(destination, manifest):
    """Replace the manifest atomically so readers never see partial JSON."""
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                     dir=destination.parent,
                                     prefix=".manifest-", suffix=".tmp",
                                     delete=False) as temporary:
        temporary_path = Path(temporary.name)
        try:
            temporary.write(json.dumps(manifest, indent=2, allow_nan=False) + "\n")
        except BaseException:
            temporary_path.unlink(missing_ok=True)
            raise
    try:
        temporary_path.replace(destination)
    finally:
        temporary_path.unlink(missing_ok=True)


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
        "status": "running",
        "all_assertions_passed": False,
        "checks": [],
    }
    manifest_path = args.output_dir / "manifest.json"
    write_manifest(manifest_path, manifest)
    for name, function in (("core", check_core),
                           ("anisotropic", check_anisotropic),
                           ("residual_npt", check_residual_npt)):
        print(f"Running {name} checks...", flush=True)
        before = time.monotonic()
        manifest["active_check"] = name
        write_manifest(manifest_path, manifest)
        try:
            report = function()
            destination = args.output_dir / f"{name}.json"
            destination.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
        except Exception as error:
            manifest["status"] = "failed"
            manifest["failed_check"] = name
            manifest["error"] = {"type": type(error).__name__, "message": str(error)}
            manifest["elapsed_seconds"] = round(time.monotonic() - started, 3)
            write_manifest(manifest_path, manifest)
            raise
        elapsed = round(time.monotonic() - before, 3)
        manifest["checks"].append({"name": name, "all_assertions_passed": True,
                                   "elapsed_seconds": elapsed,
                                   "report": destination.name})
        manifest.pop("active_check", None)
        manifest["elapsed_seconds"] = round(time.monotonic() - started, 3)
        write_manifest(manifest_path, manifest)
        print(f"  Passed; report: {destination.name}", flush=True)
    manifest["status"] = "passed"
    manifest["all_assertions_passed"] = True
    manifest["elapsed_seconds"] = round(time.monotonic() - started, 3)
    write_manifest(manifest_path, manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
