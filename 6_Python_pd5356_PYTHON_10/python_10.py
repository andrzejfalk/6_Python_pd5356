# PYTHON_10

def charakterystyka_bialka(sekwencja, masa, pI):
    return f"Białko ma sekwencję {sekwencja}, masę {masa} kDa i punkt izoelektryczny {pI}."


def sumuj_cechy_bialek(**kwargs):
    suma_mas = 0
    suma_pI = 0
    liczba_bialek = 0

    for nazwa, cechy in kwargs.items():
        suma_mas += cechy["masa"]
        suma_pI += cechy["pI"]
        liczba_bialek += 1

    srednie_pI = suma_pI / liczba_bialek
    return suma_mas, srednie_pI


opis = charakterystyka_bialka(sekwencja="MKTLLIL", masa=58.4, pI=6.8)
print(opis)

suma_mas, srednie_pI = sumuj_cechy_bialek(
    bialko1={"masa": 58.4, "pI": 6.8},
    bialko2={"masa": 42.1, "pI": 7.2},
    bialko3={"masa": 35.6, "pI": 5.9}
)

print("Suma mas białek:", suma_mas)
print("Średni punkt izoelektryczny:", srednie_pI)