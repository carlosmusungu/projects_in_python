
## TRANSCRIBING SCRIPT USING BROWSER'S AI EXTENSION

import webbrowser
import time
from concurrent.futures import ThreadPoolExecutor


def open_link(link):
    try:
        if link:
            print(f"Opening: {link}")
            webbrowser.open(link)
    except Exception as e:
        print(f"Error opening {link}: {e}")

        

def prep_links(source_file, dest_file, num_lines):
    # Step 1: Open the source file and read all lines
    with open(source_file, 'r') as src:
        lines = src.readlines()

    # Step 2: Select the first `num_lines` lines to move
    working_lines = lines[:num_lines]
    remaining_lines = lines[num_lines:]

    with ThreadPoolExecutor() as executor:
        executor.map(open_link, [link.strip() for link in working_lines])
        print(f"opened links {working_lines}")

    # Step 3: Write the selected lines to the destination file
    with open(dest_file, 'a') as dest:  # 'a' to append to the file if it exists
        dest.writelines(working_lines)
        print("updated links worked on")

    # Step 4: Overwrite the source file with the remaining lines
    with open(source_file, 'w') as src:
        src.writelines(remaining_lines)
        print(f"deleted the first {num_lines} in {source_file}")

    #print(f"Moved {num_lines} lines from {source_file} to {dest_file}")

# Usage
source_file = 'source.txt'
dest_file = 'links_transcribed.txt'
num_lines = 10  # Number of lines to move

prep_links(source_file, dest_file, num_lines)



