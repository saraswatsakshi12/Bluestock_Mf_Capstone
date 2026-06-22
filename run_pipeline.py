"""
run_pipeline.py
----------------
Bluestock Fintech — Mutual Fund Analytics Capstone
Master pipeline orchestrator. Runs the full ETL → Analytics chain
in order and prints a stage-by-stage status summary.

Looks inside scripts/ for each stage. If your scripts use slightly
different filenames (e.g. etl.py instead of data_ingestion.py),
list the alternatives in PIPELINE_STAGES below — the first match
found is used.

Usage:
    python run_pipeline.py
"""

import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "scripts"

# Each stage lists possible filenames — first one found in scripts/ is run.
PIPELINE_STAGES = [
    ("Data Ingestion",        ["data_ingestion.py", "etl.py", "etl_pipeline.py"]),
    ("Live NAV Fetch",        ["live_nav_fetch.py"]),
    ("Data Cleaning",         ["data_cleaning.py", "clean_data.py"]),
    ("Database Load",        ["load_to_sqlite.py", "load_db.py"]),
    ("EDA",                   ["eda.py"]),
    ("Performance Metrics",   ["compute_metrics.py", "performance.py"]),
    ("Risk Analytics",        ["risk_metrics.py"]),
    ("Fund Recommender Test", ["recommender.py"]),
]


def find_script(candidates: list[str]) -> Path | None:
    """Return the first existing script path from a list of candidate filenames."""
    for name in candidates:
        path = SCRIPTS_DIR / name
        if path.exists():
            return path
    return None


def run_stage(label: str, candidates: list[str]) -> bool:
    """Run a single pipeline stage as a subprocess. Returns True on success."""
    print(f"\n{'=' * 65}")
    print(f"  STAGE: {label}")
    print(f"{'=' * 65}")

    script_path = find_script(candidates)
    if script_path is None:
        print(f"  ⚠  SKIPPED — none of {candidates} found in scripts/")
        return False

    start = time.time()
    result = subprocess.run([sys.executable, str(script_path)], cwd=BASE_DIR)
    elapsed = time.time() - start

    if result.returncode == 0:
        print(f"  ✓ {label} ({script_path.name}) completed in {elapsed:.1f}s")
        return True
    else:
        print(f"  ✗ {label} ({script_path.name}) FAILED (exit code {result.returncode})")
        return False


def main():
    print("=" * 65)
    print("  BLUESTOCK FINTECH — MF ANALYTICS PIPELINE")
    print("=" * 65)

    results = {}
    for label, candidates in PIPELINE_STAGES:
        results[label] = run_stage(label, candidates)

    print(f"\n{'=' * 65}")
    print("  PIPELINE SUMMARY")
    print(f"{'=' * 65}")
    for label, success in results.items():
        status = "✓ PASS" if success else "✗ SKIPPED/FAILED"
        print(f"  {label:<28} {status}")

    total = len(results)
    passed = sum(results.values())
    print(f"\n  {passed}/{total} stages completed successfully.")
    print("=" * 65)


if __name__ == "__main__":
    main()
