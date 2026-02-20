#!/usr/bin/env bash
set -euo pipefail

echo "------------------------------------------"
echo "Regen Atom 2.1 generated artifacts"
echo "------------------------------------------"
echo

echo "Regenerating claims/index/tree/paper outline..."
python scripts/build_node_claims.py
python scripts/build_node_index.py
python scripts/build_paper_outline.py

echo
echo "DONE: regenerated artifacts."
echo
echo "Next (manual):"
echo "  git add -A"
echo "  git commit -m \"Regenerate artifacts\""
echo "  git push"
echo
