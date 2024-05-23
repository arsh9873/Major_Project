import os
import core.gen_gensim_model as gen
import core.instruction2vec as inst2vec
from p1 import fn_model

# Function to generate embeddings for a given text file
def generate_embeddings_for_file(file_path, model, vectorsize):
    with open(file_path, "r") as file:
        asm_code = file.read()
    output_file = os.path.splitext(file_path)[0] + "_emb.txt"
    with open(output_file, "w") as out_file:
        for one_instruction in asm_code.split('\n'):
            vector_of_instruction = inst2vec.instruction2vec(one_instruction.strip(), model, vectorsize)
            out_file.write(f"{vector_of_instruction}\n")
    print(f"Embeddings generated and saved to: {output_file}")

# Load pre-trained model
model = "./m1"

# Directory containing the text files
folder_path = "./pt1/"

# Size of vectors
contextsize = 5

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        generate_embeddings_for_file(file_path, model, contextsize)

