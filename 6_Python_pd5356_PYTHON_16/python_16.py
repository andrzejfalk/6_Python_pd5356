import numpy as np
import matplotlib.pyplot as plt

# Dane
geny = ['GenA', 'GenB', 'GenC']
proby = ['Proba1', 'Proba2', 'Proba3']

ekspresja = np.array([
    [5.1, 2.3, 7.8],  # GenA
    [3.2, 4.5, 6.1],  # GenB
    [4.8, 5.5, 3.9]   # GenC
])

# 1. Wykres liniowy
plt.figure(figsize=(8, 5))

for i in range(len(geny)):
    plt.plot(proby, ekspresja[i], marker='o', label=geny[i])

plt.title('Zmiany ekspresji genów w próbkach')
plt.xlabel('Próbki')
plt.ylabel('Poziom ekspresji')
plt.legend()
plt.grid(True)

plt.savefig('ekspresja_genow.png')
plt.show()


# 2. Wykres słupkowy
x = np.arange(len(proby))
szerokosc = 0.25

plt.figure(figsize=(8, 5))

plt.bar(x - szerokosc, ekspresja[0], width=szerokosc, label='GenA')
plt.bar(x, ekspresja[1], width=szerokosc, label='GenB')
plt.bar(x + szerokosc, ekspresja[2], width=szerokosc, label='GenC')

plt.title('Porównanie ekspresji genów w próbkach')
plt.xlabel('Próbki')
plt.ylabel('Poziom ekspresji')
plt.xticks(x, proby)
plt.legend()
plt.grid(axis='y')

plt.show()


# 3. Wykres rozrzutu GenA vs GenB
plt.figure(figsize=(6, 5))

plt.scatter(ekspresja[0], ekspresja[1])

for i in range(len(proby)):
    plt.text(ekspresja[0][i], ekspresja[1][i], proby[i])

plt.title('Porównanie ekspresji GenA i GenB')
plt.xlabel('Ekspresja GenA')
plt.ylabel('Ekspresja GenB')
plt.grid(True)

plt.show()