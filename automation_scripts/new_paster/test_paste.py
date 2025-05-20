import pyperclip
import pandas as pd
import os

# Path to your CSV file
csv_path = "C:\\Users\\Work\\Desktop\\test_Data\\test_data.csv"

# Step 1: Get timestamp lines from clipboard
timestamp_lines = pyperclip.paste().strip().splitlines()

# Step 2: Add two extra lines
timestamp_lines += ["", ""]

# Step 3: Prompt user to copy YouTube link
input("Now copy the YouTube link to clipboard and press Enter...")

# Step 4: Get the YouTube link
link = pyperclip.paste().strip()

# Step 5: Create columns
column_a = timestamp_lines
column_b = [link if i < len(column_a) - 2 else "" for i in range(len(column_a))]

# Step 6: Create DataFrame
df = pd.DataFrame({
    "Timestamp Line": column_a,
    "YouTube Link": column_b
})

# Step 7: Append to or create the CSV
if os.path.exists(csv_path):
    existing_df = pd.read_csv(csv_path)
    df = pd.concat([existing_df, df], ignore_index=True)

df.to_csv(csv_path, index=False)
print(f"✅ Data saved to {csv_path}")
