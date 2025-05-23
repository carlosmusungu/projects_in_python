import pyautogui
import keyboard
import time

def action_one(repetitions=1):
    """Clicks at the first location and pastes, repeated a specified number of times."""
    for _ in range(repetitions):
        # The action steps
        time.sleep(2)
        #pyautogui.hotkey('ctrl', 'r')
        time.sleep(2)
        pyautogui.hotkey('alt', 'j')
        time.sleep(2)
        #pyautogui.click(397, 500)
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        time.sleep(3)
        #pyautogui.hotkey('space')
        #time.sleep(5)
        pyautogui.hotkey('ctrl', 'tab')
        print(f"Action One Executed ({_+1}/{repetitions})")
        
def invoke_action_one():
    """Prompts the user for the number of repetitions and invokes action_one."""
    try:
        repetitions = int(input("Enter the number of repetitions: "))
        if repetitions <= 0:
            print("Please enter a positive number.")
            time.sleep(2)
        else:
            action_one(repetitions)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        

keyboard.add_hotkey('1', invoke_action_one)

print("Script running... Press '1' to execute actions. Press ESC to exit.")
keyboard.wait('esc')  # Keep the script running until 'esc' is pressed
