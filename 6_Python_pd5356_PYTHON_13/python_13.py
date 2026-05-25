import os
from datetime import datetime
import biologia

folder_name = "bio_data"
file_path = os.path.join(folder_name, "nucleotides.txt")
dna_sample = "AGCTTAGCTAAGGCT"

os.makedirs(folder_name, exist_ok=True)

note = biologia.cell_note()
base_count = biologia.count_bases(dna_sample)
created_at = datetime.now()

print(note)

with open(file_path, "w") as file:
    file.write(note + "\n")
    file.write("DNA sequence: " + dna_sample + "\n")
    file.write("Base count: " + str(base_count) + "\n")
    file.write("Created at: " + str(created_at) + "\n")

print("Saved:", file_path)