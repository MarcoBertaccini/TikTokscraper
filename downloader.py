import json
import subprocess
import os

OUTPUT_DIR = "output/videos"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("output/data.json", "r") as f:
    videos = json.load(f)

for i, video in enumerate(videos):
    url = video["url"]
    output_path = f"{OUTPUT_DIR}/video_{i}.mp4"

    if os.path.exists(output_path):
        continue

    print(f"⬇️ Scarico {url}")
    subprocess.run([
        "yt-dlp",
        "-o", output_path,
        url
    ])
