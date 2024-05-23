import os
import re

# Function to read assembly code from a text file
def read_assembly_code_from_file(file_path):
    with open(file_path, 'r') as file:
        assembly_code = file.read()
    return assembly_code

# Function to tokenize and normalize assembly code
def tokenize_and_normalize(assembly_code):
    tokens = re.findall(r"[\w]+", assembly_code.lower())
    ntokens = [token for token in tokens if len(token) <= 5 and token[0].isalpha() and (len(token) > 2 or token == "or")]
    return ntokens

# Path to the directory containing text files
directory_path = "./"

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)
        
        # Read assembly code from the file
        assembly_code = read_assembly_code_from_file(file_path)
        
        # Tokenize and normalize assembly code
        tokens = tokenize_and_normalize(assembly_code)
        
        # Print tokens to the same file and save it
        with open(file_path, 'w') as file:
            file.write(" ".join(tokens))
            print("saved file"+filename)
