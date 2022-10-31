def usun_duplikaty(L):
	L = sorted(L)
	bez_duplikatow = []
	bez_duplikatow.append(L[0])
	for i in range(1, len(L)):
		if(bez_duplikatow[len(bez_duplikatow)-1] != L[i]):
			bez_duplikatow.append(L[i])
	return bez_duplikatow



tab = list(map(int, input().split()))
print(usun_duplikaty(tab))

