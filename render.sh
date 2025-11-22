#!/usr/bin/env bash
set -euo pipefail

# Render the example Manim scene at low quality (fast preview)
manim -pql manim_scenes/my_first_scene.py MyScene
