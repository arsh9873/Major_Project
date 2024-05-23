import os

# Directory containing the text files
folder_path = "./"

# Get a list of all text files in the folder
text_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

# Rename the text files
for i, file_name in enumerate(text_files, start=1):
    old_path = os.path.join(folder_path, file_name)
    new_name = f"ben{i}.txt"
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed: {old_path} to {new_path}")

