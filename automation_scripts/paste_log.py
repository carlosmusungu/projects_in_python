import pyautogui
import keyboard
import time
import csv
from datetime import datetime

# Coordinates (Change these as needed)
CLICK1_X, CLICK1_Y = 478, 470  # First click location
CLICK2_X, CLICK2_Y = 252, 462  # Second click location

# Open the CSV file to log the actions and their timestamps
with open("actions_log.csv", "a", newline='') as csvfile:
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
        pyautogui.click(CLICK1_X, CLICK1_Y)
        pyautogui.hotkey('ctrl', 'v')
        log_action("Action One Executed")  # Log the action
        pyautogui.click(5528, 648)

    def action_two():
        """Clicks at the second location, then performs a sequence of actions."""
        pyautogui.click(CLICK2_X, CLICK2_Y)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.hotkey('right')
        time.sleep(0.3)
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
        pyautogui.click(5528, 648)

    # Listen for key commands
    keyboard.add_hotkey('[', action_one)
    keyboard.add_hotkey(']', action_two)

    print("Script running... Press [ for Action One and ] for Action Two. Press ESC to exit.")
    keyboard.wait('esc')  # Keep the script running until 'esc' is pressed
