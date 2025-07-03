import pyautogui
import random
import datetime
import time
import csv
import os

# === Configuration ===
TARGET_IMAGES = ['dashboard.png', 'home_logo.png', 'message_icon.png', 'refresh_button.png', 'view_progress.png']
CONFIDENCE = 0.8
CLICK_INTERVAL = (30, 136)
LOG_FILE = 'click_log.csv'

def is_time_allowed():
    """Logic check for allowed time"""
    now = datetime.datetime.now()
    hour = now.hour
    return hour >= 22 or hour < 6  # Between 10PM and 6AM

def find_target_locations(image_path):
    """Find all locations on screen matching the image"""
    try:
        matches = list(pyautogui.locateAllOnScreen(image_path, confidence=CONFIDENCE))
        return matches
    except Exception as e:
        print(f"Error finding image '{image_path}' on screen:", e)
        return []

def log_click_action(image_name, position):
    """Log the click action with timestamp and image name to a CSV file"""
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'Image Name', 'X', 'Y'])  # Write header
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        x, y = position
        writer.writerow([timestamp, image_name, x, y])

def click_random_target(matches, image_name):
    """Click a random match from found locations"""
    if not matches:
        print(f"No matches found for '{image_name}'.")
        return
    match = random.choice(matches)
    x, y = pyautogui.center(match)
    pyautogui.moveTo(x, y, duration=random.uniform(1, 3))
    pyautogui.click()
    print(f"Clicked on '{image_name}' at: ({x}, {y})")
    log_click_action(image_name, (x, y))

def main():
    while True:
        if is_time_allowed():
            print("Time is allowed. Searching for targets...")
            images = TARGET_IMAGES[:]
            random.shuffle(images)
            for image in images:
                matches = find_target_locations(image)
                if matches:
                    click_random_target(matches, image)
                    break  # Click only one image per interval
        else:
            print("Time not allowed. Skipping click.")

        time.sleep(random.uniform(*CLICK_INTERVAL))

if __name__ == "__main__":
    main()
