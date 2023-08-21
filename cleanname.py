import os
import re

def remove_non_english_characters(name: str) -> str:
    pattern = re.compile('[^ -~]+')
    return pattern.sub('', name)

def rename_files_in_directory(directory: str):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Skip directories
        if os.path.isdir(file_path):
            continue
        new_filename = remove_non_english_characters(filename)
        new_file_path = os.path.join(directory, new_filename)
        os.rename(file_path, new_file_path)

directory = input("give path: ")
rename_files_in_directory(directory)
