import pyautogui
import keyboard



def copy():
    pyautogui.hotkey('ctrl', 'c')
    print("Copied")

def action_two():
    pyautogui.hotkey('ctrl', 'v')
    print("pasted")

keyboard.add_hotkey('\', copy)
keyboard.add_hotkey('z', paste)

print("Script running... Press esc to exit.")
keyboard.wait('esc')


