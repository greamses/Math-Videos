# Manim example scene

This repository contains a minimal Manim scene and helper files to produce a short preview video.

Quick start (Ubuntu):

- Install system dependencies (ffmpeg & cairo):

```bash
sudo apt update
sudo apt install -y ffmpeg libcairo2
```

- Create a virtual environment and install Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Render the scene (low-quality preview):

```bash
manim -pql manim_scenes/my_first_scene.py MyScene
```

- Or use the helper script:

```bash
bash render.sh
```

Output video and media files appear under `media/videos/` by default.
