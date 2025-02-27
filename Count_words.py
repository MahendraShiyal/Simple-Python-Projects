#Required Library: pathlib (built-in, no installation needed)

from pathlib import Path  # Importing Path to handle file paths

#Ask the user to enter a file name
file_name = input("Enter the text file name (with .txt extension): ").lower().strip()
file_path = Path(file_name)  # Creating a Path object for the given file

#Check if the file exists and has a .txt extension
if file_path.is_file() and file_path.suffix == ".txt":
    with file_path.open("r", encoding="utf-8") as file:  # Open file in read mode with UTF-8 encoding
        data = file.read()  # Read the file content
        word_count = len(data.split())  # Count words by splitting the text

    print(f"Total number of words in '{file_name}': {word_count}")  # Display word count

# Error Handling: File does not exist
elif not file_path.is_file():
    print(f"\n Error: File '{file_name}' not found. Please check the file name and try again.")

# Error Handling: File is not a .txt file
elif file_path.suffix != ".txt":
    print(f"\n Error: '{file_name}' is not a text file. Please provide a .txt file.")
