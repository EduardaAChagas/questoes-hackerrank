# #transforma inteiro pra binario
# testi = 27
# temp = format(testi, "b")
# print(temp)
# numberEx = int ( str(1010) , 2)
# print(numberEx)
# #transforma binario pra inteiro
# def binary2int(binary): 
#     int_val, i, n = 0, 0, 0
#     while(binary != 0): 
#         a = binary % 10
#         int_val = int_val + a * pow(2, i) 
#         binary = binary//10
#         i += 1
#     print(int_val) 
# #teste = 0b27
# def binaryToDecimal(binary):
    
#     binary1 = binary
#     decimal, i, n = 0, 0, 0
#     while(binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary//10
#         i += 1
#     print(decimal)
# #print(int(teste, 2))
# #binary2int(teste)
# teste27 = 11011
# binaryToDecimal(teste27)

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
    
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

teste = 50
print("RETORNO: ",changeAds(teste))
tesb = '110010'
tesb = int(tesb)
#print(binaryToDecimal(tesb))