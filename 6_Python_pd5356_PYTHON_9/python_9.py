# PYTHON_9

unique_bases = {"A", "T", "C", "G"}
gene_roles = {
    "BRCA1": "DNA repair",
    "TP53": "cell cycle control",
    "EGFR": "growth signaling"
}

unique_bases.add("N")
gene_roles["MYC"] = "transcription regulation"

print("A" in unique_bases)
print("BRCA1" in gene_roles)

unique_bases.discard("N")

print(unique_bases)

for gene, role in gene_roles.items():
    print(gene, role)

if len(unique_bases) > 3:
    print("Set has more than 3 elements")
else:
    print("Set has 3 elements or fewer")

if "TP53" in gene_roles:
    print(gene_roles["TP53"])

rna_bases = {"A", "U", "C", "G"}
all_bases = unique_bases.union(rna_bases)

print(all_bases)