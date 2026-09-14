#!/usr/bin/env python3
"""Reduce a `claude plugin eval` run to precision/recall numbers.

The eval harness reports per-grader verdicts but does not aggregate them. This
reads a run's JSON and reports, per case and per arm:

  recall                 must-find-* graders passed / total
  false-positive rate    must-not-flag-* graders failed / total
  calibration            calibration-* graders passed / total
  lift                   with-arm score - without-arm score

Grader intent comes from the filename prefix, so the prefix is a contract,
enforced by scripts/check-consistency.sh:

  must-find-<x>.md       a seeded defect the review must report
  must-not-flag-<x>.md   a concern the review must NOT report
  calibration-<x>.md     severity / evidence calibration

Usage:
  python3 scripts/eval-summary.py [run.json | results-dir]

With no argument, the newest evals/results/*/aggregate-result.json is used.
"""
from __future__ import annotations

import glob
import json
import os
import sys

FIND, NOTFLAG, CALIB = "must-find-", "must-not-flag-", "calibration-"
ARMS = ("with", "without")
FEW_CASES = 5


def classify(name: str) -> str:
    for prefix, kind in ((FIND, "find"), (NOTFLAG, "notflag"), (CALIB, "calib")):
        if name.startswith(prefix):
            return kind
    return "unknown"


def latest_run() -> str:
    hits = sorted(glob.glob("evals/results/*/aggregate-result.json"))
    if not hits:
        raise SystemExit("no evals/results/*/aggregate-result.json found — pass a path")
    return hits[-1]


def collect(case: dict, arm: str) -> dict:
    """grader name -> one bool per run; with-only and unscored graders omitted."""
    per: dict = {}
    for run in case.get("arms", {}).get(arm) or []:
        for g in run.get("graders") or []:
            if g.get("withOnly") or g.get("scored") is False:
                continue
            per.setdefault(g.get("name", "?"), []).append(bool(g.get("passed")))
    return per


def rate(per: dict, kind: str, invert: bool = False):
    """Mean pass rate across graders of one kind. None when there are none."""
    vals = [sum(p) / len(p) for name, p in per.items() if classify(name) == kind]
    if not vals:
        return None, 0
    total = sum((1.0 - v) if invert else v for v in vals) / len(vals)
    return total, len(vals)


def arm_score(case: dict, arm: str):
    scores = [r.get("score") for r in case.get("arms", {}).get(arm) or []
              if r.get("score") is not None]
    return sum(scores) / len(scores) if scores else None


def pct(v) -> str:
    return "   n/a" if v is None else f"{v * 100:5.1f}%"


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else latest_run()
    if os.path.isdir(path):
        path = os.path.join(path, "aggregate-result.json")
    with open(path) as fh:
        doc = json.load(fh)

    print(f"run:      {path}")
    print(f"cost:     ${doc.get('costUsd', 0):.3f}   partial: {doc.get('partial')}   "
          f"duration: {doc.get('durationSeconds')}s   schema: {doc.get('schemaVersion')}")
    print()

    unknown: set = set()
    mixed: list = []
    lifts: list = []

    header = (f"{'case':<28} {'arm':<8} {'score':>6} {'recall':>7} "
              f"{'fp-rate':>8} {'calib':>7}")
    print(header)
    print("-" * len(header))

    for case in doc.get("cases", []):
        name = case.get("name") or case.get("id") or "?"
        for arm in ARMS:
            per = collect(case, arm)
            for gname, passes in per.items():
                kind = classify(gname)
                if kind == "unknown":
                    unknown.add(gname)
                elif 0.0 < sum(passes) / len(passes) < 1.0:
                    mixed.append(f"{name}/{arm}/{gname}")
            rec, _ = rate(per, "find")
            fpr, _ = rate(per, "notflag", invert=True)
            cal, _ = rate(per, "calib")
            score = arm_score(case, arm)
            print(f"{name[:28]:<28} {arm:<8} "
                  f"{'   n/a' if score is None else f'{score:.2f}':>6} "
                  f"{pct(rec):>7} {pct(fpr):>8} {pct(cal):>7}")
        with_score, without_score = arm_score(case, "with"), arm_score(case, "without")
        if with_score is not None and without_score is not None:
            lifts.append(with_score - without_score)
            print(f"{'':<28} {'lift':<8} {with_score - without_score:+.2f}")
        print()

    if lifts:
        print(f"mean lift over {len(lifts)} case(s): {sum(lifts) / len(lifts):+.3f}")
        if len(lifts) < FEW_CASES:
            print(f"  caution: fewer than {FEW_CASES} cases — a smoke result, not a benchmark")
    print("note: fp-rate is the share of must-not-flag graders that FAILED in that arm")
    if unknown:
        print(f"WARNING: graders outside the naming contract, excluded from P/R: {sorted(unknown)}")
    if mixed:
        print("WARNING: judge verdicts disagreed across runs, so these rates are unstable:")
        for item in mixed:
            print(f"  {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
