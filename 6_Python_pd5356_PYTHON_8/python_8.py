dna_bases = ["A", "T", "G", "C", "A", "T", "G", "G"]
base_names = ("Adenine", "Thymine", "Cytosine", "Guanine")

print(dna_bases[0])
print(dna_bases[-1])

print(base_names[0])
print(base_names[-1])

dna_bases[2] = "C"
print(dna_bases)

dna_bases.append("A")
print(dna_bases)

for base in dna_bases:
    print(base)

for name in base_names:
    print(name)

purines = [base for base in dna_bases if base == "A" or base == "G"]
print(purines)