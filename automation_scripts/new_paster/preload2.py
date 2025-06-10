import pyautogui
import keyboard
import time
import cv2
import image_searcher as im_s

def action_one(repetitions=1):
    """Clicks at the first location and pastes, repeated a specified number of times."""
    for _ in range(repetitions):
        # The action steps
        time.sleep(2)
        #pyautogui.hotkey('ctrl', 'r')
        #time.sleep(5)
        pyautogui.hotkey('alt', 'j')
        time.sleep(2)
        #pyautogui.click(397, 500)
        #pyautogui.hotkey('enter') ##### DO MATCHING HERE
        coordinates, item_size = im_s.find_item_on_screen("C:\\Users\\Work\\Pictures\\Screenshots\\timestamped.png") or (None, None)
        if coordinates: 
            pyautogui.click(im_s.click_on_center(coordinates, item_size))
        else:
            print("timestamped summary option not found, trying again")
            return 
        time.sleep(3)
        
        #coordinates, item_size = im_s.find_item_on_screen("C:\Users\Work\Pictures\Screenshots\timestamped.png") or (None, None)

        attempts = 0
        while attempts < 5:
            coordinates, item_size = coordinates, item_size = im_s.find_item_on_screen("C:\\Users\\Work\\Pictures\\Screenshots\\understanding.png") or (None, None)
            if coordinates:
                print("Ai ready proceeeding to next tab")
                break

            attempts +=1
            time.sleep(1)
            print(f"item not found retrying doing attempt {attempts}") 

        ############################# DO A SECOND MATCH HERE
        #pyautogui.hotkey('space')
        time.sleep(2)
        #pyautogui.click(3644, -89)
        #time.sleep(5)
        pyautogui.hotkey('ctrl', 'tab')
        print(f"Action One Executed ({_+1}/{repetitions})")




def find_uq():
    coordinates, item_size = im_s.find_item_on_screen("C:\\Users\\Work\\Pictures\\Screenshots\\understanding.png") or (None, None)
    return coordinates, item_size

    
        
def invoke_action_one():
    """Prompts the user for the number of repetitions and invokes action_one."""
    try:
        repetitions = int(input("Enter the number of repetitions: "))
        if repetitions <= 0:
            print("Please enter a positive number.")
        else:
            time.sleep(2)
            #pyautogui.hotkey('ctrl', '2')
            action_one(repetitions)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

keyboard.add_hotkey('1', invoke_action_one)

print("Script running... Press '1' to execute actions. Press ESC to exit.")
keyboard.wait('esc')  # Keep the script running until 'esc' is pressed
