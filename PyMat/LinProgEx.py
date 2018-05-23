from scipy.optimize import linprog 
print "Nowe linijki tratatata"
#funkcja od której odjelismy juz wartosc P(o P nie zapominamy bo dodajemy je do warunkow)
f='x[0]*5*30+x[1]*4*50−10*(5*x[0]+10*x[1])'
#uzyskujemy 100x[0]+100x[1]

#c - wartosci przy parametrach x1 i x2
#UWAGA - sa z wartosciami ujemnymi, poniewaz domyslnie linprog szuka minimum wiec zeby
#znalezc maksimum, musimy je odwrocic!
c= [-100, -100]
#odpowiednie pary do warunkow x1 + x2 oraz(WARUNEK Z WARTOSCI P) 5x1 + 10x2 ...
A= [[1,1],[1,2]]
#oraz ich ograniczenia x1 + x2 <= 60 oraz 5x1 + 10x2 <= 400(co zamienia sie na x1 + 2x2 <= 80)
b= [60, 80]
#ogranczenia dla x1 -> musimy byc wiekszy od zera(bo nie mozna miec ujemnej uprawy) oraz z warunku,
#5x1 <= 250(co zamienia sie na x1 <= 50)
x0_bnds = (0, 50)
#ogranczenia dla x2 -> musimy byc wiekszy od zera(bo nie mozna miec ujemnej uprawy) oraz z warunku,
#4x2 <= 120(co zamienia sie na x2 <= 30)
x1_bnds = (0, 30)
#uzywamy funkcji linprog z podanymi parametrami i uzyskujemy wynik
res = linprog(c, A, b, bounds=(x0_bnds, x1_bnds))
print(res,'\n')

print('Najlepsze wartosci do optymalizacji tej funkcji to x1 = ', res.x[0], ', x2 = ',res.x[1])
#tutaj wartosc funkcji musimy odwrocic, ponownie z powodu tego, ze linprog szuka minimum
print('Wtedy, rolnik uzyska maksymalny przychód, równy ',-res.fun)