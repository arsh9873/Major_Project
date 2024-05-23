import os

# Directory containing the text files
folder_path = "./"

# Output file to save the combined contents
output_file = "combined_text.txt"

# Function to combine text files
def combine_text_files(folder_path, output_file):
    with open(output_file, "w") as out_file:
        # Iterate over files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                # Open each text file and append its contents to the output file
                with open(file_path, "r") as in_file:
                    out_file.write(in_file.read())

# Call the function to combine text files
combine_text_files(folder_path, output_file)

