import cv2
import pyautogui
import numpy as np
import os
import winsound
import time
import keyboard
import mouse
import pyperclip
import csv
#import paste_log4 as pl




with open("gen_links", mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Function to play a beep sound if an image is not found
    def play_beep():
        winsound.Beep(1000, 500)  # Frequency, Duration (in milliseconds)

    def click_on_center(coordinates, item_size):
        # Calculate the center of the found item
        x, y = coordinates
        width, height = item_size
        center_x = x + width // 2
        center_y = y + height // 2
        return(center_x, center_y)  # Click at the center
        print(f"Clicked at the center: ({center_x}, {center_y})")

    # Function to find the image on the screen and return coordinates
    def find_item_on_screen(image_path, threshold=0.8):
        if not os.path.exists(image_path):
            print(f"Error: The file {image_path} does not exist!")
            return None

        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a numpy array (needed for OpenCV)
        screenshot_np = np.array(screenshot)

        # Convert the image to grayscale (OpenCV works better with grayscale images)
        screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

        # Load the template image you want to find
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Perform template matching
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

        # Get the best match location (top-left corner)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:  # If the match is above the threshold, consider it a valid match
            #print(f"Item found at coordinates: {max_loc}")
            return max_loc, template.shape[::-1]  # Return the top-left corner coordinates of the match
        else:
            print("Item not found on screen.")
            return None  # No match found
        

    def log_action(action):
            """copies the clipboard content to a csv file"""
            clipboard_content = pyperclip.paste()
            writer.writerow([clipboard_content, time.asctime()])
            print({clipboard_content})  # Print to console as well

    # Main function to execute the image match
    
    def execute_workflow():
        
        time.sleep(0.5)
        # Step 1: Find first image and click
        coordinates, item_size = find_item_on_screen('copy_image_sentence.png') or (None, None)
        if coordinates:
            pyautogui.click(click_on_center(coordinates,item_size)) # Click on the found coordinates
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'w')
            print(time.asctime())
            log_action("copied")
            pyautogui.moveTo(164, 886)

            #time.sleep(0.5)
        else:
            play_beep()
    def close_page():
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.moveTo(164,886)
    
    def copy_link():
        pyautogui.moveTo(598,382)
        mouse.click(button='right')
    
    mouse.on_button(execute_workflow, buttons=mouse.RIGHT, types=mouse.DOWN)
    keyboard.add_hotkey('x', close_page)
    keyboard.add_hotkey('z', copy_link)
    keyboard.wait('esc')