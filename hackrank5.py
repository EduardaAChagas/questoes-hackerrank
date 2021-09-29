def sockMerchant(n,vetor):
	pares = 0
	qtde = dict.fromkeys(vetor)
	for i in range(keys):
		for j in range(1,(vetor.count(i))):
			if j%2==0:
				pares += 1
	return pares
