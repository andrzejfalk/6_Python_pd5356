import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# =========================================
# Funkcja sprawdzająca poprawność sekwencji
# =========================================

def czy_poprawna_sekwencja(sekwencja):

    poprawne = {'A', 'T', 'C', 'G'}

    return all(nukleotyd in poprawne for nukleotyd in sekwencja)


# =========================================
# Funkcja obliczająca GC%
# =========================================

def oblicz_gc(sekwencja):

    if len(sekwencja) == 0:
        return 0

    gc = sekwencja.count('G') + sekwencja.count('C')

    return round((gc / len(sekwencja)) * 100, 2)


# =========================================
# Wczytywanie FASTA
# =========================================

def wczytaj_fasta(nazwa_pliku):

    sekwencje = {}

    try:

        with open(nazwa_pliku, "r") as plik:

            linie = [linia.strip() for linia in plik]

        nazwa = None

        for linia in linie:

            if linia == "":
                continue

            if linia.startswith(">"):
                nazwa = linia[1:]
            else:
                sekwencje[nazwa] = linia.upper()

    except FileNotFoundError:

        print("BŁĄD: Plik nie istnieje")
        return {}

    return sekwencje


# =========================================
# Dodanie sekwencji użytkownika
# =========================================

def dodaj_sekwencje_usera(sekwencje, nazwa_pliku):

    user_seq = input("\nPodaj swoją sekwencję DNA: ").upper()

    nazwa = "UserSequence"

    with open(nazwa_pliku, 'a') as plik:

        plik.write(f"\n>{nazwa}\n")
        plik.write(user_seq + "\n")

    sekwencje[nazwa] = user_seq

    return sekwencje


# =========================================
# Usuwanie błędnych i duplikatów
# =========================================

def filtruj_sekwencje(sekwencje):

    poprawne = {}
    unikalne = set()

    for nazwa, seq in sekwencje.items():

        seq = seq.strip().upper()

        if len(seq) == 0:
            continue

        if len(seq) > 200:
            continue

        if not czy_poprawna_sekwencja(seq):
            continue

        if seq in unikalne:
            continue

        poprawne[nazwa] = seq
        unikalne.add(seq)

    return poprawne


# =========================================
# Tworzenie DataFrame
# =========================================

def utworz_dataframe(sekwencje):

    dane = []

    for nazwa, seq in sekwencje.items():

        rekord = {
            'Nazwa': nazwa,
            'Sekwencja': seq,
            'Dlugosc': len(seq),
            'A': seq.count('A'),
            'T': seq.count('T'),
            'C': seq.count('C'),
            'G': seq.count('G'),
            'GC_%': oblicz_gc(seq)
        }

        dane.append(rekord)

    df = pd.DataFrame(dane)

    return df


# =========================================
# Wizualizacje
# =========================================

def rysuj_wykresy(df):

    # 1. Długości sekwencji
    plt.figure(figsize=(8, 5))

    plt.bar(df['Nazwa'], df['Dlugosc'])

    plt.title("Długość sekwencji DNA")
    plt.xlabel("Sekwencja")
    plt.ylabel("Długość")

    plt.xticks(rotation=45)

    plt.savefig("wykres_dlugosci.png")

    # 2. GC%
    plt.figure(figsize=(8, 5))

    plt.bar(df['Nazwa'], df['GC_%'])

    plt.title("Zawartość GC")
    plt.xlabel("Sekwencja")
    plt.ylabel("GC %")

    plt.xticks(rotation=45)

    plt.savefig("wykres_gc.png")

    # 3. Scatter długość vs GC
    plt.figure(figsize=(6, 5))

    plt.scatter(df['Dlugosc'], df['GC_%'])

    plt.title("Długość vs GC")
    plt.xlabel("Długość")
    plt.ylabel("GC %")

    plt.savefig("wykres_scatter.png")


# =========================================
# MAIN
# =========================================

def main():

    nazwa_pliku = Path(__file__).parent / "sekwencje.txt"
    print(f"Czytam plik: {nazwa_pliku}")

    print("Wczytywanie sekwencji...")

    sekwencje = wczytaj_fasta(nazwa_pliku)

    print(f"Wczytano: {len(sekwencje)} sekwencji")

    sekwencje = dodaj_sekwencje_usera(
        sekwencje,
        nazwa_pliku
    )

    sekwencje = filtruj_sekwencje(sekwencje)

    print(f"\nPo filtracji pozostało: {len(sekwencje)} sekwencji")

    if len(sekwencje) == 0:
        print("Brak poprawnych sekwencji do analizy.")
        print("Sprawdź plik sekwencje.txt albo podaj poprawną sekwencję DNA.")
        return

    df = utworz_dataframe(sekwencje)

    print("\nDataFrame:\n")

    print(df)

    rysuj_wykresy(df)

    print("\nWykresy zostały zapisane do plików PNG")


# =========================================

if __name__ == "__main__":
    main()