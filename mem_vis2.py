import os

def get_folder_size(path):
    """Calculate total size of files in the given folder and its subfolders."""
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total += os.path.getsize(fp)
    return total

def convert_size(size_bytes):
    """Convert bytes to KB, MB, GB, etc."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024

def list_large_folders(root_path, min_size_mb=500):
    """Print the size of folders larger than min_size_mb."""
    min_size_bytes = min_size_mb * 1024 * 1024
    for dirpath, _, _ in os.walk(root_path):
        size = get_folder_size(dirpath)
        if size >= min_size_bytes:
            print(f"{convert_size(size)}\t{dirpath}")

if __name__ == "__main__":
    root = input("Enter folder path: ").strip()
    if os.path.isdir(root):
        list_large_folders(root, min_size_mb=500)
    else:
        print("Invalid folder path.")
