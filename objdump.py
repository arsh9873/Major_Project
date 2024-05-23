import os
import subprocess

# Directory containing the .exe files
folder_path = "./"

# Function to execute objdump -d command, remove top 7 lines, and save output to a text file
def execute_objdump(file_path, output_file):
    command = ["objdump", "-d", file_path]
    # Run the objdump command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Split the output into lines and remove the top 7 lines
    lines = result.stdout.split('\n')[7:]
    # Write the modified output to the text file
    with open(output_file, "w") as f:
        f.write('\n'.join(lines))
        print(output_file)

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".exe"):
        file_path = os.path.join(folder_path, filename)
        output_file = f"virus_{len(os.listdir(folder_path)) + 1}.txt"  # Naming the output file
        execute_objdump(file_path, output_file)

