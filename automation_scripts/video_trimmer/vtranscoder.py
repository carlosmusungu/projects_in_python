import os
import subprocess
from pathlib import Path
import argparse

def transcode_video(input_path, output_path, crf=0, preset="slow"):
    # Transcode to constant frame rate, visually lossless or lossless
    cmd = [
        "ffmpeg",
        "-i", str(input_path),
        "-vsync", "cfr",  # force constant frame rate
        "-c:v", "libx264",
        "-crf", str(crf),         # 0 = lossless, 18 = visually lossless
        "-preset", preset,        # slower = better compression
        "-c:a", "copy",           # copy audio without re-encoding
        str(output_path)
    ]

    print(f"🔄 Transcoding: {input_path.name}")
    subprocess.run(cmd, check=True)
    print(f"✅ Saved: {output_path.name}")

def main():
    parser = argparse.ArgumentParser(description="Transcode all videos in a folder to constant frame rate (CFR) without losing quality.")
    parser.add_argument('--input_folder', required=True, help='Path to input videos')
    parser.add_argument('--output_folder', required=True, help='Path to save transcoded videos')
    parser.add_argument('--crf', type=int, default=0, help='CRF value (0 = lossless, 18 = visually lossless)')
    parser.add_argument('--preset', default="slow", help='x264 preset (ultrafast, superfast, fast, medium, slow, slower, veryslow)')
    args = parser.parse_args()

    input_dir = Path(args.input_folder)
    output_dir = Path(args.output_folder)
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in input_dir.glob("*.*"):
        if file.suffix.lower() not in [".mp4", ".mov", ".mkv", ".avi"]:
            continue

        output_file = output_dir / f"{file.stem}_transcoded.mp4"
        transcode_video(file, output_file, crf=args.crf, preset=args.preset)

if __name__ == "__main__":
    main()
