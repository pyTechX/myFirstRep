import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import random


def calka(x, y):
    suma = 0
    for i in range(0, len(x) - 1):
        suma = suma + ((y[i + 1] + y[i]) / 2) * (x[i + 1] - x[i])
    return suma


t = np.arange(0, 10, 1.0)
s = np.arange(0, 10, 1.0)

for i in range(0, len(s)):
    s[i] = sp.rand()

line = plt.plot(t, s, lw=2)
C = calka(t, s)
plt.ylim(0, 1)
plt.title("Całka = " + str(C))
plt.show()


def calka_na_podstawie_stalej(x, y):
    suma = 0
    for i in range(0, len(x) - 1):
        punkt_z_przedzialu = random.uniform(y[i + 1], y[i])
        suma = suma + ((x[i + 1] - x[i]) * punkt_z_przedzialu)
    return suma


line2 = plt.plot(t, s, lw=2)
C2 = calka_na_podstawie_stalej(t, s)
plt.ylim(0, 1)
plt.title("Calka w oparciu o stałą = " + str(C2))
plt.show()


def calka_wielomianu_pierwszego_stopnia(x, y):
    # całka liczona jako pole pod powierzchnią funkcji liniowej
    # uzyskanej za pomocą regresji liniowej metodą najmniejszych kwadratów
    suma = 0
    srednia_x = np.average(x)
    srednia_y = np.average(y)
    iloczyn_odchylen = 0
    odchylenie_x_2 = 0
    for i in range(0, len(x) - 1):
        iloczyn_odchylen = iloczyn_odchylen + ((x[i] - srednia_x) * (y[i] - srednia_y))
        odchylenie_x_2 = odchylenie_x_2 + ((x[i] - srednia_x) ** 2)
    a = iloczyn_odchylen / odchylenie_x_2
    b = srednia_y - (a * srednia_x)
    # y = ax + b
    pole = ((0.5 * a) * ((x[len(x) - 1] ** 2) - (x[0] ** 2))) + (b*(x[len(x)-1] - x[0]))
    return pole


line3 = plt.plot(t, s, lw=2)
C3 = calka_wielomianu_pierwszego_stopnia(t, s)
plt.ylim(0, 1)
plt.title("Całka jako pole pod wykresem regresji liniowej = " + str(C3))
plt.show()

print('Różnica związana z niedokładniością liczenia całki metodą przybliżoną wyniosła {0:.8f}'.format(C - C2))
print('Różnica związana z niedokładniością liczenia całki za pomocą regresji liniowej {0:.8f}'.format(C - C3))