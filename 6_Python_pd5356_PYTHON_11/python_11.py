# PYTHON_11

class Organizm:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def opisz(self):
        return f"Organizm: {self.nazwa}, rodzaj: {self.rodzaj}"

    @staticmethod
    def transkrybuj(sekwencja_dna):
        return sekwencja_dna.replace("T", "U")


class Bakteria(Organizm):
    def __init__(self, nazwa, rodzaj, ksztalt):
        super().__init__(nazwa, rodzaj)
        self.ksztalt = ksztalt

    def opisz(self):
        opis_podstawowy = super().opisz()
        return f"{opis_podstawowy}, kształt: {self.ksztalt}"


bakteria1 = Bakteria("Escherichia coli", "bakteria", "pałeczka")
bakteria2 = Bakteria("Streptococcus pneumoniae", "bakteria", "ziarniak")

print(bakteria1.opisz())
print(bakteria2.opisz())

dna = "ATGCTTACG"
rna = Organizm.transkrybuj(dna)

print("DNA:", dna)
print("RNA:", rna)