import os
from pathlib import Path

def get_folder_size(path):
    """Return total size (in bytes) of a folder recursively."""
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                total += os.path.getsize(fp)
            except OSError:
                pass
    return total

def format_size(size_bytes):
    """Convert bytes into human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def list_folder_sizes(directory):
    directory = Path(directory)
    folders = [f for f in directory.iterdir() if f.is_dir()]
    
    folder_sizes = []
    for folder in folders:
        size = get_folder_size(folder)
        folder_sizes.append((folder.name, size))
    
    # Sort by size descending
    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    # Print results
    for name, size in folder_sizes:
        print(f"{name:30} {format_size(size)}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="List sizes of folders in a directory (descending).")
    parser.add_argument("directory", help="Directory path to scan")
    args = parser.parse_args()
    list_folder_sizes(args.directory)
