def binaryToDecimal(binary):
    
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def achaTamanho(x):
    a = str(x)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
        else:
            return len(a)
    return len(a)

def fourthBit(number):
    cont = 0
    numBin = format(number,"b")
    string = str(numBin)
    print(numBin)
    aux = list(string)
    print(aux)
    tam = len(aux)
    for i in range(tam):
        aux[i] = int(aux[i])
    print('aux',aux)
    idx = len(aux) - 1
    newList = []
    while (idx >= 0):
      newList.append(aux[idx])
      idx = idx - 1
    print('newlist: ',newList)
    return numBin[3]
teste = 23
print(fourthBit(teste))

def changeAds(base10):
    binaro = format(base10,"b") 
    aux = binaro
    cont = 0
    str(aux)
    new_aux = aux
    contaCaracteres = binaro.count('1')
    contaCaracteres = contaCaracteres + binaro.count('0')
    print('aux: antes do for',aux)
    for i in range(len(aux)):
        if aux[i]==1:
            new_aux = aux.replace(aux[i],0)
        elif aux[i]==0:
            new_aux = aux.replace(aux[i],1)
    new_aux = int(new_aux)
    print("new aux: ",new_aux)
    return binaryToDecimal(new_aux)