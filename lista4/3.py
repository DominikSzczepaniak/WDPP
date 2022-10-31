from random import randint, choice

def randperm(n):
    wynik = []
    for i in range(n):
        wynik.append(i)
    for i in range(n):
        pozycja = randint(i, n-1) #bierzemy dowolna liczbe do zamiany miejscami z obecna pozycja i pozycja wylosowana
        pamiec = wynik[i]
        wynik[i] = wynik[pozycja] 
        wynik[pozycja] = pamiec
    return wynik
print(randperm(9))
print(randperm(9))
print(randperm(9))
print(randperm(10**6))
