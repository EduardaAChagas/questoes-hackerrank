num = [1,3,1,4,5,6,3,2]
contar = num.count(1)
#retorna quantas vezes um numero aparece



def countDuplicate(numbers):
    cont = 0
    print(numbers)
    for i in range(len(numbers)):
        if numbers.count(i)>=2:
            cont=cont+1
    return cont
print(countDuplicate(num))