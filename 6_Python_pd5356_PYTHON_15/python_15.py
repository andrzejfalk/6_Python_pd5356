import pandas as pd
import numpy as np

# Utworzenie DataFrame
dane = {
    'Gen': ['GenA', 'GenB', 'GenC', 'GenD'],
    'Proba1': [5.1, 2.3, np.nan, 4.4],
    'Proba2': [3.2, 4.5, 3.9, np.nan],
    'Proba3': [6.3, 5.6, np.nan, 6.6]
}

df = pd.DataFrame(dane)

print("Oryginalny DataFrame:")
print(df)

# Sprawdzenie brakujących danych
print("\nBrakujące dane True/False:")
print(df.isna())

print("\nLiczba braków w każdej kolumnie:")
print(df.isna().sum())

# Usunięcie wierszy z brakującymi danymi
df_bez_brakow = df.dropna()

print("\nDataFrame po usunięciu wierszy z brakami:")
print(df_bez_brakow)

# Uzupełnienie braków średnią dla każdej kolumny liczbowej
df_uzupelniony = df.copy()

kolumny_prob = ['Proba1', 'Proba2', 'Proba3']

df_uzupelniony[kolumny_prob] = df_uzupelniony[kolumny_prob].fillna(
    df_uzupelniony[kolumny_prob].mean()
)

print("\nDataFrame po uzupełnieniu braków średnimi kolumn:")
print(df_uzupelniony)

# Dane dotyczące genu GenA
gen_a = df[df['Gen'] == 'GenA']

print("\nDane dotyczące genu GenA:")
print(gen_a)

# Średnia ekspresja dla każdej próbki
srednie_prob = df[kolumny_prob].mean()

print("\nŚrednia ekspresja dla każdej próbki:")
print(srednie_prob)

# Geny, których ekspresja w próbce 1 wynosi więcej niż 4
geny_proba1_gt4 = df[df['Proba1'] > 4]

print("\nGeny z ekspresją w Proba1 > 4:")
print(geny_proba1_gt4)