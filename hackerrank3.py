def aVeryBigSum(ar):
    tam = len(ar)
    bigSoma = 0
    bigSoma = int(bigSoma)
    for i in range(tam):
        bigSoma=bigSoma+ar[i]
    return bigSoma

vetorExemplo = [1000000001,1000000002,1000000003,1000000004,1000000005]
print(aVeryBigSum(vetorExemplo))