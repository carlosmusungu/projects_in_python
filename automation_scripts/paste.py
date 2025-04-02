import pyautogui
import keyboard
import time

# Coordinates (Change these as needed)
CLICK1_X, CLICK1_Y = 478, 470  # First click location
CLICK2_X, CLICK2_Y = 252, 462  # Second click location

def action_one():
    """Clicks at the first location and pastes."""
    pyautogui.click(478, 470)
    pyautogui.hotkey('ctrl', 'v')
    print("Action One Executed")
    pyautogui.click(5528, 648)
    

def action_two():
    """Clicks at the second location, then performs a sequence of actions."""
    pyautogui.click(252, 462)
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
    pyautogui.hotkey('ctrl','shift', 'up')
    pyautogui.hotkey('ctrl','d')
    pyautogui.hotkey('ctrl','down')
    pyautogui.hotkey('ctrl','down')
    pyautogui.hotkey('ctrl','up')
    #pyautogui.press('down')
    #pyautogui.press('down')
    #pyautogui.press('down')
    print("Action Two Executed")
    pyautogui.click(5528, 648)

# Listen for key commands
# keyboard.add_hotkey('F6', action_one)
# keyboard.add_hotkey('F7', action_two)

keyboard.add_hotkey('[', action_one)
keyboard.add_hotkey(']', action_two)

print("Script running... Press F6 or F7 to execute actions. Press ESC to exit.")
keyboard.wait('esc')  # Keep the script running until 'esc' is pressed
