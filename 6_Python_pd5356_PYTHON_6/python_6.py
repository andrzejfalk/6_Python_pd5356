# PYTHON_6

sekwencja_first = "ATGCGTA"
sekwencja_second = "CGTACGA"

pelna_sekwencja = sekwencja_first + sekwencja_second

seq_sliced = pelna_sekwencja[2:10]

liczba_A = pelna_sekwencja.count("A")
pozycja_CGT = pelna_sekwencja.find("CGT")
sekwencja_RNA = pelna_sekwencja.replace("T", "U")

print(f"Pełna sekwencja DNA:\n\t{pelna_sekwencja}")
print(f"Fragment sekwencji [2:10]:\n\t{seq_sliced}")
print(f"Liczba nukleotydów A: {liczba_A}")
print(f"Pierwsza pozycja CGT: {pozycja_CGT}")
print(f"Sekwencja po transkrypcji DNA -> RNA:\n\t{sekwencja_RNA}")