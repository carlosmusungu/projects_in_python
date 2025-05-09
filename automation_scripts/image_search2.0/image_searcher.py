import cv2
import pyautogui
import numpy as np
import os
import winsound
import time
#import paste_log4 as pl


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
        print(f"Item found at coordinates: {max_loc}")
        return max_loc, template.shape[::-1]  # Return the top-left corner coordinates of the match
    else:
        print("Item not found on screen.")
        return None  # No match found

# Function to perform a second action (custom function you can define)
def action_two():
    print("Running action_two function...")
    # Add your custom code here for the action you want to perform
    time.sleep(1)  # Simulate some action time (e.g., wait for animation or response)
    print("action_two completed!")

# Main function to execute the sequence of image matches
def execute_workflow():
        
    # Step 1: Find first image and click
    coordinates, item_size = find_item_on_screen('C:\\Users\\Work\\Desktop\\down_arrow.png') or (None, None)
    if coordinates:
        pyautogui.click(click_on_center(coordinates,item_size)) # Click on the found coordinates
        print(f"Clicked on the coordinates: {coordinates}")
        time.sleep(2)
    else:
        play_beep()
    

    # Step 2: After first image is clicked, find second image and move to it
    coordinates, item_size = find_item_on_screen('C:\\Users\\Work\\Desktop\\copy_image.png') or (None, None)
    if coordinates:
        pyautogui.moveTo(click_on_center(coordinates,item_size))  # Move to the found coordinates
        time.sleep(2)
        print(f"Moved to the coordinates: {coordinates}")
    else:
        play_beep()
        play_beep()
        play_beep()
        return(print("Image two not found"))
        # If not found, continue to the next image match

    # Step 3: After second image is found, click and run 'action_two'
    coordinates, item_size = find_item_on_screen('C:\\Users\\Work\\Desktop\\copy_image_sentence.png') or (None, None)
    if coordinates:
        pyautogui.click(click_on_center(coordinates, item_size))  # Click on the found coordinates
        print(f"Clicked on the coordinates: {coordinates}")
        #pl.action_two()  # Run the action_two function
        #break  # End the loop after executing action_two
    else:
        play_beep()
        play_beep()
        play_beep()
        return(print("Image Three not found"))
        #break  # If not found, continue to the next image match

    # Step 4: If none of the images were found, beep and end the loop



#execute_workflow()
