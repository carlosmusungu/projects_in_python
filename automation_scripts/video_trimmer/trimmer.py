import os
import subprocess
from pathlib import Path
import argparse

def get_video_duration(video_path):
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries",
            "format=duration", "-of",
            "default=noprint_wrappers=1:nokey=1", str(video_path)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    return float(result.stdout)

def trim_video(input_path, output_path, trim_start, trim_end):
    duration = get_video_duration(input_path)
    new_duration = duration - trim_start - trim_end

    if new_duration <= 0:
        print(f"⚠️ Skipping {input_path.name}: video too short to trim.")
        return

    subprocess.run([
        "ffmpeg",
        "-ss", str(trim_start),
        "-i", str(input_path),
        "-t", str(new_duration),
        "-c", "copy",
        str(output_path)
    ])

    print(f"✅ Trimmed: {input_path.name} -> {output_path.name}")

def main():
    parser = argparse.ArgumentParser(description="Trim first and last seconds from all .mp4 videos in a folder.")
    parser.add_argument('--input_folder', required=True, help='Path to folder containing videos')
    parser.add_argument('--output_folder', required=True, help='Path to save trimmed videos')
    parser.add_argument('--trim_start', type=float, required=True, help='Seconds to trim from start')
    parser.add_argument('--trim_end', type=float, required=True, help='Seconds to trim from end')
    args = parser.parse_args()

    input_folder = Path(args.input_folder)
    output_folder = Path(args.output_folder)
    trim_start = args.trim_start
    trim_end = args.trim_end

    if not input_folder.exists():
        print(f"❌ Input folder does not exist: {input_folder}")
        return
    output_folder.mkdir(parents=True, exist_ok=True)

    for video_file in input_folder.glob("*.mp4"):
        output_file = output_folder / f"{video_file.stem}_trimmed.mp4"
        trim_video(video_file, output_file, trim_start, trim_end)

if __name__ == "__main__":
    main()
