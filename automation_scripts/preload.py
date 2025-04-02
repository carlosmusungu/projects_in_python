### preload.py

import pyautogui
import keyboard
import time


def action_one():
    """Clicks at the first location and pastes."""
    #pyautogui.click(3351, 626)
    time.sleep(3)
    pyautogui.hotkey('alt', 'j')
    time.sleep(2)
    pyautogui.click(5201, 324)
    time.sleep(0.5)
    pyautogui.click(3551,240)
    time.sleep(2)
    pyautogui.click(3644, -89)
    time.sleep(2)
    pyautogui.hotkey('ctrl','tab')
    print("Action One Executed")

keyboard.add_hotkey('1', action_one)

print("Script running... Press F6 or F7 to execute actions. Press ESC to exit.")
keyboard.wait('esc')  # Keep the script running until 'esc' is pressed