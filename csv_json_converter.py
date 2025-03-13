import os
import csv
import json
from pathlib import Path

def csv_to_json(csv_file_path, json_file_path):
    """
    Converts a CSV file to a JSON file.
    Args:
    - csv_file_path: Path to the CSV file
    - json_file_path: Path to save the resulting JSON file
    """
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = list(csv_reader)  # Read the CSV file into a list of dictionaries
        
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4)  # Write to the JSON file with indentation for readability

def convert_all_csv_to_json(input_folder, output_folder):
    """
    Converts all CSV files in the specified folder to JSON files.
    Args:
    - input_folder: Path to the folder containing CSV files
    - output_folder: Path to the folder where JSON files will be saved
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the directory
    files = os.listdir(input_folder)
    
    # Loop through the files in the directory
    for file in files:
        file_path = os.path.join(input_folder, file)
        
        # Check if the file is a CSV file
        if file.lower().endswith('.csv'):
            json_file_name = file.replace('.csv', '.json')
            json_file_path = os.path.join(output_folder, json_file_name)
            
            # Convert CSV to JSON
            print(f"Converting {file} to {json_file_name}")
            csv_to_json(file_path, json_file_path)
        else:
            print(f"Skipping non-CSV file: {file}")

# Example usage
if __name__ == '__main__':
    # Define the input folder path (converter folder)
    input_folder = r'C:\Users\Work\Desktop\converter'
    output_folder = r'C:\Users\Work\Desktop\converter/json'
    
    # Define the output folder path (json folder)
    output_folder = os.path.join(os.path.dirname(output_folder), 'json')
    
    # Check if the input folder exists
    if os.path.exists(input_folder) and os.path.isdir(input_folder):
        convert_all_csv_to_json(input_folder, output_folder)
    else:
        print(f"Input folder '{input_folder}' does not exist or is not a directory.")
