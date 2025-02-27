# Import necessary modules
from pathlib import Path  # Used for handling file paths
import os  # Used for interacting with the operating system

# Ask the user to provide the folder path
folder_path = input("Please provide the path of the folder to rename files in: ").strip()
folder_path = Path(folder_path)  # Convert the input to a Path object

# Check if the provided path exists and is a folder
if folder_path.exists() and not folder_path.is_file():
    # Check if the folder is empty
    if not os.listdir(folder_path):
        print("The given folder is empty. Please check the folder and try again.")
    else:
        # Ask for the file type and ensure it starts with a dot
        while True:
            file_type = input("Please provide the type of files to rename (e.g., .txt, .jpeg): ").strip().lower()
            if not file_type.startswith("."):  # Ensure the file type starts with a dot
                print("Invalid file type! The file type should start with a dot (e.g., .txt). Please try again.")
            else:
                break  # Exit the loop if the file type is valid

        # Get a list of files matching the given file type
        matching_files = [f for f in os.listdir(folder_path) if f.lower().endswith(file_type)]

        # Check if there are any matching files
        if matching_files:
            base_name = input("Please enter a base name for the new files: ").strip()

            # Rename files with a number appended to the base name
            for t, file_name in enumerate(matching_files, start=1):
                new_name = f"{base_name}_{t}{file_type}"  # Create the new file name
                os.rename(folder_path / file_name, folder_path / new_name)  # Rename the file

            print("Renaming is complete.")
        else:
            print(f"No '{file_type}' files found in {folder_path}. Please check and try again.")

# Handle cases where the provided path does not exist or is not a folder
elif not folder_path.exists():
    print("The given path does not exist.")
elif folder_path.is_file():
    print("The given path is a file. Please provide a folder path.")
