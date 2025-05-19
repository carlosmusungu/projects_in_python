import pyautogui
import keyboard
import time
import csv
from datetime import datetime
import image_searcher as im_s
# Coordinates (Change these as needed)
#CLICK1_X, CLICK1_Y = 478, 470  # First click location
#CLICK2_X, CLICK2_Y = 252, 462  # Second click location

# Open the CSV file to log the actions and their timestamps
with open("actions_log3.csv", "a", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header only if the file is empty
    csvfile.seek(0, 2)  # Move to the end of the file
    if csvfile.tell() == 0:  # If the file is empty
        csv_writer.writerow(["Action", "Time"])  # Header row

    def log_action(action):
        """Logs the action with the timestamp to the CSV file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
        csv_writer.writerow([action, timestamp])
        print(f"{action} at {timestamp}")  # Print to console as well

    def action_one():
        """Clicks at the first location and pastes."""
        pyautogui.click(3191, 468)
        pyautogui.hotkey('ctrl', 'v')
        log_action("Action One Executed")  # Log the action
        #pyautogui.click(3717, -635)

    def action_two():
        """Clicks at the second location, then performs a sequence of actions."""
        pyautogui.click(3023, 468)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.4)
        pyautogui.hotkey('right')
        time.sleep(0.15)
        pyautogui.hotkey('ctrl', 'down')
        time.sleep(0.15)
        pyautogui.hotkey('ctrl', 'left')
        time.sleep(0.15)
        pyautogui.hotkey('ctrl', 'up')
        time.sleep(0.15)
        pyautogui.press('right')
        time.sleep(0.15)
        pyautogui.hotkey('ctrl', 'shift', 'up')
        pyautogui.hotkey('ctrl', 'd')
        pyautogui.hotkey('ctrl', 'down')
        pyautogui.hotkey('ctrl', 'down')
        pyautogui.hotkey('ctrl', 'up')
        log_action("Action Two Executed")  # Log the action
        pyautogui.click(274, 93)

    def link():
        """Clicks at the first location and copies."""
        pyautogui.click(670,92)
        #time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'c')
        action_one()

    def content():
        """Clicks at specific locations and executes content-related actions."""
        #pyautogui.click(1633, 810)
        #pyautogui.click(1526, 490)
        #time.sleep(1)
        #pyautogui.click(4823, 755)
        #time.sleep(2)
        x = im_s.execute_workflow()
        action_two() if x == 1 else None
        #action_two()

    def both():
        """Executes both link and content actions."""
        link()
        time.sleep(2)
        content()

    def undo():
        """ Fixes mistaken content copies"""
        pyautogui.click(4823, 755)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','z')
        pyautogui.click(471,162)

    def complete():
        """ new function to close current page and start the next process automatically"""
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(2)
        both()

    # Listen for key commands
    keyboard.add_hotkey('[', action_one)
    keyboard.add_hotkey(']', action_two)
    keyboard.add_hotkey('v', both)
    keyboard.add_hotkey('r', undo)
    keyboard.add_hotkey('.', complete)
    keyboard.add_hotkey('-', link)
    keyboard.add_hotkey('=', content)

    print("Script running... Press [ for Action One, ] for Action Two, and v for Both Actions. Press ` to exit.")
    keyboard.wait('`')  # Keep the script running until 'esc' is pressed
