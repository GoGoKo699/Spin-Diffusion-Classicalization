"""Check authored local links, milestone IDs and optional sister consistency.

This is a document/navigation check. It does not certify scientific claims,
external source contents, hosted mathematical rendering or release readiness.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

REPOSITORY = "Spin-Diffusion-Classicalization"
SISTER = "Nonlinear-Diffusion-Entanglement"
ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def inspect_repository(root, name, counterpart, counterpart_root=None):
    missing, checked, external_sister_files = [], [], []
    for source in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in source.relative_to(root).parts):
            continue
        text = source.read_text()
        # Mathematical/code expressions such as D[L](rho) are not links.
        text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text, flags=re.MULTILINE | re.DOTALL)
        text = re.sub(r"`[^`\n]*`", "", text)
        for raw in LINK.findall(text):
            target = raw.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme:
                if counterpart_root is not None:
                    prefix = f"https://github.com/GoGoKo699/{counterpart}/blob/"
                    if target.startswith(prefix):
                        rest = parsed.path.split("/blob/", 1)[1]
                        _, separator, path = rest.partition("/")
                        if separator:
                            resolved = counterpart_root / unquote(path)
                            external_sister_files.append({"source": str(source.relative_to(root)),
                                                          "target": target, "local_counterpart": path})
                            if not resolved.is_file():
                                missing.append({"source": str(source.relative_to(root)), "target": target})
                continue
            if not parsed.path:
                continue
            destination = (source.parent / unquote(parsed.path)).resolve()
            record = {"source": str(source.relative_to(root)), "target": target}
            checked.append(record)
            if not destination.exists():
                missing.append(record)
    milestones = (root / "learning" / "MILESTONES.md").read_text()
    ids = re.findall(r"^#{2,4}\s+(M\d{2})\b", milestones, flags=re.MULTILINE)
    counts = Counter(ids)
    expected = {f"M{i:02d}" for i in range(1, 31)}
    assert set(counts) == expected and all(n == 1 for n in counts.values()), counts
    readme = (root / "README.md").read_text()
    assert f"https://github.com/GoGoKo699/{counterpart}" in readme, "Missing README sister link"
    assert not missing, json.dumps(missing, indent=2)
    return {"repository": name, "local_link_count": len(checked), "missing_local_links": missing,
            "milestone_ids": ids, "milestone_count": len(ids),
            "readme_sister_link_present": True, "counterpart_file_links_checked": external_sister_files}


def run_checks(sister_root=None):
    sister_root = Path(sister_root).resolve() if sister_root is not None else None
    if sister_root is not None:
        assert sister_root.is_dir(), "The supplied sister checkout is unavailable"
    reports = [inspect_repository(ROOT, REPOSITORY, SISTER, sister_root)]
    if sister_root is not None:
        reports.append(inspect_repository(sister_root, SISTER, REPOSITORY, ROOT))
        # Both educational routes identify the exact selected book edition.
        for root in (ROOT, sister_root):
            anchor_files = list((root / "learning").glob("*.md"))
            assert any("9783110642490" in path.read_text() for path in anchor_files), "Missing common-anchor DOI"
    return {"scope": "File targets, exact M01–M30 IDs and README reciprocity; no scientific or hosted-rendering verdict",
            "all_assertions_passed": True, "reciprocal_checkout_checked": sister_root is not None,
            "reports": reports}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sister-root", type=Path, help="Optional checkout to verify reciprocal links and milestones")
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "results" / "navigation.json")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # The authored documentation links this report. Mark an in-progress report
    # before checking targets, and never retain a stale success after failure.
    args.output.write_text(json.dumps({"status": "running", "all_assertions_passed": False}) + "\n")
    try:
        report = run_checks(args.sister_root)
    except Exception as error:
        args.output.write_text(json.dumps({"status": "failed", "all_assertions_passed": False,
                                           "error": str(error)}, indent=2) + "\n")
        raise
    report["status"] = "passed"
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(f"Navigation checks passed; report: {args.output}")


if __name__ == "__main__":
    main()
