import pyperclip
import pandas as pd
import os
import keyboard
import winsound
import csv
from datetime import datetime
import pyautogui
import image_searcher as im_s
import time
import sys

# Countdown displayer

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\rSleeping... {remaining} seconds remaining")
        sys.stdout.flush()
        time.sleep(1)
    print("\rDone sleeping!                  ")





csv_path = "new_excel.csv"
log_path = "new_workflow_log.csv"

# Ensure log file exists
def log_event(event_msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", newline='') as logfile:
        writer = csv.writer(logfile)
        if os.path.getsize(log_path) == 0:
            writer.writerow(["Event", "Timestamp"])
        writer.writerow([event_msg, timestamp])
    #print(f"{event_msg} at {timestamp}")


def capture_tm():
     # Step 1: Get timestamp lines
    #time.sleep(1)
    global timestamp_lines
    timestamp_lines = []
    timestamp_lines = pyperclip.paste().strip().splitlines()
    # Add padding lines
    try:
        if not any(timestamp_lines) or timestamp_lines[0].startswith("http"):
            raise ValueError("Error with timestamp content")
        else:
            timestamp_lines += ["", ""]
            return 1
    except ValueError:
        print('value error')
        return 0
    except Exception:
        print('error')
        return 0
    
        
    
    #print(timestamp_lines[-3])
    #winsound.Beep(659, 600)
    

def link():
    """Clicks at the first location and copies."""
    pyautogui.click(670,92)
    #time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    pyautogui.click(436, 132)
    

def c_tab():
    pyautogui.hotkey('ctrl', 'w')


def content():
    x = im_s.execute_workflow()
    
    if x == 1:
        capture_tm()
    else:
        print("error copying")
        return 3
    #capture_tm() if x == 1 else print("error copying")
    return 1

def caputure_l():
    link()
    log_event("Link captured")

    global ylink
    ylink = pyperclip.paste().strip()
    try:
        if not ylink.startswith("http"):
            raise ValueError("Invalid YouTube link in clipboard.")
    
    except ValueError as e:
        print(f"Error: {e}")
        return 0
    print(ylink)
    winsound.Beep(440, 600)
    return 1
    


def save():
    try:
        #play_beep()
        print("🔹 Copying lines from clipboard...")
        #log_event("updating gen_csv_file")
      
        # Step 4: Assemble data
        column_a = timestamp_lines
        column_b = [ylink if i < len(column_a) - 2 else "" for i in range(len(column_a))]

        df_new = pd.DataFrame({
            "Timestamp Line": column_a,
            "YouTube Link": column_b
        })

        # Step 5: Append to CSV or create new
        if os.path.exists(csv_path):
            df_existing = pd.read_csv(csv_path)
            df_final = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_final = df_new

        df_final.to_csv(csv_path, index=False)
        winsound.Beep(880, 600)
        log_event("Data appended to CSV")
        print(df_final.iloc[-3])
        c_tab()

    except Exception as e:
        print(f"❌ Error: {e}")
        winsound.Beep(5000, 300)
        log_event(f"Error occurred: {e}")


def both():
    caputure_l()
    content()
    c = content()
    if c==3:
        print("error copying content: the program has halted")
        return 3
    y = capture_tm()
    save() if y == 1 else (print("error saving"), winsound.Beep(8000, 400))


# Instructions:
#print("press [ to copy the content, \n press ] to copy the link; \n press = to save, \n press ` to exit the application")

# Entry point
#keyboard.add_hotkey('.', both)
#keyboard.add_hotkey('z', c_tab)
#keyboard.add_hotkey('[', content)
#keyboard.add_hotkey(']', caputure_l)
#keyboard.add_hotkey('=', save)
#keyboard.wait('`')
