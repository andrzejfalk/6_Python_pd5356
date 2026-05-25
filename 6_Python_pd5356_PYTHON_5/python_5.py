# PYTHON_5

sekwencja_dna = "ATGCTAGCTAGC"

print("Sekwencja DNA:", sekwencja_dna)
print("Typ zmiennej sekwencja_dna:", type(sekwencja_dna))

lista_nukleotydow = list(sekwencja_dna)

print("Lista nukleotydów:", lista_nukleotydow)
print("Typ zmiennej lista_nukleotydow:", type(lista_nukleotydow))

print("Pozycje i nukleotydy w sekwencji:")

for indeks in range(len(lista_nukleotydow)):
    print("Pozycja:", indeks, "Nukleotyd:", lista_nukleotydow[indeks])