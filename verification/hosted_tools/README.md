# Hosted mathematical comparison

These two unchanged verification helpers are copied from Guinevere commit `1bf4ed4c9fec085f1f23437981637d8a66abbd86`, `plugins/merlin-arthur-research/skills/merlin-arthur-research/scripts/`. They compare the exact source expressions with MathML on commit-pinned GitHub pages at widths 1440 and 760. The report does not replace scientific review or visual inspection of screenshots.

Install Playwright 1.56.1 and mathjax-full 3.2.1 outside the source checkout, then run `capture_hosted_math.cjs --root REPOSITORY_ROOT --repository OWNER/NAME --revision FULL_COMMIT_SHA --output NEW_EMPTY_DIRECTORY`. The default scope is every Markdown page tracked at the pinned commit. Outputs are reproducible diagnostics; screenshots require separate inspection.
