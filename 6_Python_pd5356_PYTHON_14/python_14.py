# PYTHON_14

import numpy as np

macierz_ekspresji = np.array([
    [5.0, 2.5, 7.0],
    [3.2, 4.0, 6.0],
    [8.1, 9.3, 2.5],
    [4.5, 5.7, 6.9]
])

print("Oryginalna macierz ekspresji:")
print(macierz_ekspresji)

zwiekszona_ekspresja = macierz_ekspresji * 1.05

print("\nEkspresja zwiększona o 5%:")
print(zwiekszona_ekspresja)

srednia_dla_genow = np.mean(macierz_ekspresji, axis=1)

print("\nŚrednia ekspresja dla każdego genu:")
print(srednia_dla_genow)

suma_dla_prob = np.sum(macierz_ekspresji, axis=0)

print("\nSuma ekspresji dla każdej próby:")
print(suma_dla_prob)

macierz_z_nan = macierz_ekspresji.copy()
macierz_z_nan[0, 1] = np.nan
macierz_z_nan[2, 2] = np.nan

print("\nMacierz z brakującymi danymi NaN:")
print(macierz_z_nan)

srednia_z_pominieciem_nan = np.nanmean(macierz_z_nan, axis=1)

print("\nŚrednia ekspresja genów z pominięciem NaN:")
print(srednia_z_pominieciem_nan)