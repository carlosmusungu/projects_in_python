import os
import subprocess
from pathlib import Path
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed

def transcode_video(input_path, output_path, crf=0, preset="slow"):
    cmd = [
        "ffmpeg",
        "-i", str(input_path),
        "-fps_mode", "cfr",  # force constant frame rate
        "-c:v", "libx264",
        "-crf", str(crf),
        "-preset", preset,
        "-c:a", "copy",
        str(output_path)
    ]
    print(f"🔄 Transcoding: {input_path.name}")
    subprocess.run(cmd, check=True)
    print(f"✅ Saved: {output_path.name}")

def main():
    parser = argparse.ArgumentParser(description="Transcode all videos in a folder to CFR.")
    parser.add_argument('--input_folder', required=True, help='Path to input videos')
    parser.add_argument('--output_folder', required=True, help='Path to save transcoded videos')
    parser.add_argument('--crf', type=int, default=0, help='CRF value (0 = lossless, 18 = visually lossless)')
    parser.add_argument('--preset', default="slow", help='x264 preset (ultrafast to veryslow)')
    parser.add_argument('--workers', type=int, default=os.cpu_count() - 2, help='Number of parallel processes to run')
    args = parser.parse_args()

    input_dir = Path(args.input_folder)
    output_dir = Path(args.output_folder)
    output_dir.mkdir(parents=True, exist_ok=True)

    tasks = []
    for file in input_dir.glob("*.*"):
        if file.suffix.lower() not in [".mp4", ".mov", ".mkv", ".avi"]:
            continue
        output_file = output_dir / f"{file.stem}_transcoded.mp4"
        tasks.append((file, output_file))

    # Use a process pool for parallel transcoding
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = [
            executor.submit(transcode_video, input_path, output_path, args.crf, args.preset)
            for input_path, output_path in tasks
        ]
        for future in as_completed(futures):
            try:
                future.result()
            except subprocess.CalledProcessError as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
