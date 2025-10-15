import os
import subprocess
from pathlib import Path
import argparse

def get_video_dimensions(video_path):
    """Return width and height of a video using ffprobe."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height",
            "-of", "csv=s=x:p=0", str(video_path)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    try:
        width, height = map(int, result.stdout.strip().split('x'))
        return width, height
    except:
        print(f"❌ Failed to get dimensions for {video_path}")
        return None, None

def crop_center_third(input_path, output_path):
    width, height = get_video_dimensions(input_path)
    if not width or not height:
        return

    crop_width = width // 3
    crop_height = height
    crop_x = (width - crop_width) // 2
    crop_y = 0

    crop_filter = f"crop={crop_width}:{crop_height}:{crop_x}:{crop_y}"

    subprocess.run([
        "ffmpeg",
        "-i", str(input_path),
        "-vf", crop_filter,
        "-c:a", "copy",  # copy audio
        str(output_path)
    ])

    print(f"✅ Cropped: {input_path.name} -> {output_path.name}")

def main():
    parser = argparse.ArgumentParser(description="Crop center third (horizontal) of all videos in a folder.")
    parser.add_argument('--input_folder', required=True, help='Path to input folder')
    parser.add_argument('--output_folder', required=True, help='Path to save cropped videos')
    args = parser.parse_args()

    input_folder = Path(args.input_folder)
    output_folder = Path(args.output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    for video_file in input_folder.glob("*.*"):
        if video_file.suffix.lower() not in ['.mp4', '.mov', '.mkv', '.avi']:
            continue

        output_file = output_folder / f"{video_file.stem}_cropped{video_file.suffix}"
        crop_center_third(video_file, output_file)

if __name__ == "__main__":
    main()
