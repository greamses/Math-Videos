#!/usr/bin/env bash
set -euo pipefail

# Render the factoring explainer scene at low-quality (fast preview)
manim -pql manim_scenes/factoring_quadratic.py FactoringQuadratic
