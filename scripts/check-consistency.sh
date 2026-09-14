#!/bin/sh
# Consistency checks for this skill repository.
#
# 1. Reference wiring — every references/*.md must be loadable from SKILL.md
#    (a trigger exists) or be declared REDUNDANT below. A reference that
#    SKILL.md never loads is invisible to the agent, so the repository claims
#    review coverage the skill will not apply. This gap appeared in 0.5.0
#    (review-decision-record) and recurred in 0.7.0 (dependency-and-delivery).
#
# 2. Version agreement — the version stated by SKILL.md, .claude-plugin/
#    plugin.json, and the newest changelog entry must match. Drift happened at
#    0.5.0 -> 0.5.1 and again at 0.6.0 -> 0.7.0. The manifest is a second
#    source of truth for the version, so it is checked rather than trusted.
#
# 3. Grader naming — every evals/*/graders/*.md must carry a prefix that
#    scripts/eval-summary.py recognises (must-find-, must-not-flag-,
#    calibration-). An unrecognised name would silently drop out of the
#    precision/recall numbers, the same invisible-content failure as an
#    unwired reference.

set -eu

cd "$(dirname "$0")/.."

# Reference files intentionally NOT loaded during the review workflow.
# Add an entry only after confirming SKILL.md already carries the content.
REDUNDANT=$(cat <<'EOF'
references/review-triage-and-evidence.md
EOF
)

status=0

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  status=1
}

# --- 1. reference wiring ---------------------------------------------------
for file in references/*.md; do
  [ -e "$file" ] || continue
  if grep -qF "$file" SKILL.md; then
    continue
  fi
  if printf '%s\n' "$REDUNDANT" | grep -qxF "$file"; then
    continue
  fi
  fail "unwired reference: $file (add a load trigger in SKILL.md, or declare it REDUNDANT in $0)"
done

# --- 2. version agreement --------------------------------------------------
skill_version=$(sed -n 's/^version:[[:space:]]*//p' SKILL.md | head -1)
plugin_version=$(sed -n 's/.*"version":[[:space:]]*"\([^"]*\)".*/\1/p' .claude-plugin/plugin.json | head -1)
changelog_version=$(sed -n 's/^## \([^ 	]*\).*/\1/p' evolution/CHANGELOG.md | head -1)

if [ -z "$skill_version" ]; then
  fail "no version found in SKILL.md frontmatter"
fi

for source in "SKILL.md" ".claude-plugin/plugin.json" "evolution/CHANGELOG.md"; do
  case "$source" in
    SKILL.md)                    found="$skill_version" ;;
    .claude-plugin/plugin.json)  found="$plugin_version" ;;
    evolution/CHANGELOG.md)      found="$changelog_version" ;;
  esac
  if [ -z "$found" ]; then
    fail "no version found in $source"
  elif [ "$found" != "$skill_version" ]; then
    fail "version mismatch: $source declares $found, SKILL.md declares $skill_version"
  fi
done

# --- 3. grader naming contract ---------------------------------------------
for file in evals/*/graders/*.md; do
  [ -e "$file" ] || continue
  case "$(basename "$file")" in
    must-find-*|must-not-flag-*|calibration-*) ;;
    *) fail "grader name violates the prefix contract: $file (expected must-find-*, must-not-flag-*, or calibration-*)" ;;
  esac
done

if [ "$status" -eq 0 ]; then
  printf 'consistency checks OK (version %s)\n' "$skill_version"
fi

exit "$status"
