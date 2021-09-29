import random
ar = [4,9,2,1,7,8]


def bubbleSort(n,lista):

    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i]>lista[i+1]:
                #troca de elementos nas poisções i e i+1
                lista[i], lista[i+1] = lista[i+1],a[i]


any_numbers = random.sample(range(1,100),10)
# print("Desordenado",any_numbers)
# bubbleSort(any_numbers)
# print("Ordenado:",any_numbers)

def countSwaps(a):
    swap = 0
    firstElement = None
    lastElement = None
    n=len(a)
    for j in range(n-1):
        for i in range(n-1):
            if a[i]>a[i+1]:
                swap = swap+1
                a[i], a[i+1] = a[i+1],a[i]
    firstElement = a[0]
    lastElement = a[n-1]
    print("Array is sorted in",swap,"swaps.")
    print("First Element:",firstElement)
    print("Last Element:",lastElement)
    return swap
ar = [1,2,3]
ra = [3,2,1]
print("Desordenado",ra)
countSwaps(ra)
print("Ordenado:",ra)