
## TRANSCRIBING SCRIPT USING BROWSER'S AI EXTENSION

import webbrowser
import pyautogui
import keyboard
import time
from concurrent.futures import ThreadPoolExecutor
import image_searcher as im_s
import preload2 as preloader
import p_paster as paster

#sleep time displayer
import sys

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\rSleeping... {remaining} seconds remaining")
        sys.stdout.flush()
        time.sleep(1)
    print("\rDone sleeping!                  ")



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
        print("completed")

    # Step 3: Write the selected lines to the destination file
    with open(dest_file, 'a') as dest:  # 'a' to append to the file if it exists
        dest.writelines(working_lines)
        print("updated links worked on")

    # Step 4: Overwrite the source file with the remaining lines
    with open(source_file, 'w') as src:
        src.writelines(remaining_lines)
        print(f"deleted the first {num_lines} in {source_file} new length is {len(remaining_lines)}")

    #print(f"Moved {num_lines} lines from {source_file} to {dest_file}")

# Usage
source_file = 'Joe_Regan.txt'
dest_file = 'Joe_links_transcribed.txt'
num_lines = 10  # Number of lines to move

def work_flow():
    #time.sleep(4)
    countdown(4)
    coordinates, item_size = im_s.find_item_on_screen("C:\\Users\\Work\\Pictures\\Screenshots\\fresh_slate.png")

    if coordinates:
        prep_links(source_file, dest_file, num_lines)
        countdown(30)
        #time.sleep(30)
        pyautogui.hotkey('ctrl','2')

        preloader.action_one(num_lines)

        pyautogui.hotkey('ctrl','2')

        #time.sleep(30)
        countdown(30)


        number = 0
        while number < num_lines:
            #paster.both()
            x = paster.both()

            if x==3:
                print("program has stopped")
                return 0

            #time.sleep(3)
            countdown(3)
            number +=1
            print("done") if number == num_lines else print(f"pasting {number+1}/{num_lines}")

        return 1
    else:
        print("Could not copy links")
        return 0 
        
    


def paste_only():
    print("Initiating process b")
    #time.sleep(2)
    countdown(3)
    number = 0
    videos = int(input("please enter the number of videos:"))

    while number < videos:
        #paster.both()
        x = paster.both()

        if x==3:
            print("program has stopped")
            break

        number +=1
        #time.sleep(3)
        countdown(3)
        print(f"{number}/{videos} completed successfuly")
    
    print("Process Completed")
    

def large_scale_paster():

    x = 1
    vids = int(input("Enter the batch number in multiples of 10"))
    while x <= vids:
        print(f"large_Scale {x}")
        y = work_flow()

        if y == 1:
            print(f"Proceeding to the next batch of {num_lines} batch number {x+1}/{vids}")
            countdown(5)
            x+=1
        else:
            print("Batches stopped")
            return
        
    return print("Completed: \n Ready for the next Batch")    
    
            






keyboard.add_hotkey('l', large_scale_paster)
keyboard.add_hotkey('b', paste_only)
keyboard.add_hotkey('d', work_flow)
keyboard.wait('q')




#prep_links(source_file, dest_file, num_lines)



