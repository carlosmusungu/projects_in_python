import pyperclip
import pandas as pd
import os
import keyboard  # To listen for hotkeys

# CSV path
csv_path = "gen_content_cont.csv"

def process_clipboard():
    try:
        # Step 1: Get timestamp lines
        timestamp_lines = pyperclip.paste().strip().splitlines()
        timestamp_lines += ["", ""]

        # Step 2: Prompt to copy link
        print("✅ Timestamps copied. Now copy the YouTube link and press Ctrl+Shift+L...")

        # Wait for link trigger
        keyboard.wait("p")

        # Step 3: Get link
        link = pyperclip.paste().strip()

        # Step 4: Assemble data
        column_a = timestamp_lines
        column_b = [link if i < len(column_a) - 2 else "" for i in range(len(column_a))]

        df = pd.DataFrame({
            "Timestamp Line": column_a,
            "YouTube Link": column_b
        })

        # Step 5: Append or create
        if os.path.exists(csv_path):
            existing_df = pd.read_csv(csv_path)
            df = pd.concat([existing_df, df], ignore_index=True)

        df.to_csv(csv_path, index=False)
        print(f"✅ Data saved to {csv_path}\n")
    except Exception as e:
        print(f"❌ Error: {e}")

# Register the hotkey
print("🔁 Script running... Press Ctrl+Shift+Y to start timestamp capture.")
keyboard.add_hotkey("t", process_clipboard)

# Keep the script alive
keyboard.wait('esc')
