def sito_erasthothenesa(n):
	p = [1]*(n+1)
	p[0] = p[1] = 0
	#liczby_pierwsze = []
	for i in range(2, n+1):
		if(p[i] == False):
			continue
		#liczby_pierwsze.append(i)
		for j in range(i+i, n+1, i):
			p[j] = 0
	return p

def is_palindrom(n):
	n = str(n)
	for i in range(len(n)//2):
		if(n[i] != n[len(n)-1-i]):
			return False
	return True

def palindromiczne_liczby_pierwsze(n, p):
	if(p[n] == 1 and is_palindrom(n)):
		return True
	return False

def palindrom(a, b):
	p = sito_erasthothenesa(b)
	lista = []
	for i in range(a, b+1):
		if(palindromiczne_liczby_pierwsze(i, p) == True):
			lista.append(i)
	return lista

print(palindrom(10, 200))	
