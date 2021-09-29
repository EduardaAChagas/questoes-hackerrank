# #sales by match

# #input: numero de meias, e array com as cores
# #output: numero de pares
# # print("Ar[i]",ar[i],"i:", i)
# # print("Ar[j]",ar[j],"j:",j)
# meias = 7
# gaveta= [1,2,1,2,1,3,2]
# meia = 9
# gavetar = [10,20,20,10,10,30,50,10,20]
# n = 15
# ar = [6,5,2,3,5,2,2,1,1,5,1,3,3,3,5]

# def sockMerchant(n, ar):
#     qte_pares = 0
#     tem_par = 0
#     for i in range(n):
#         tem_par = 0
#         for j in range(n):
#             if tem_par==0:
#                 if i!=j:
#                     if ar[i]==ar[j]:
#                         tem_par = tem_par + 1
#                         qte_pares=qte_pares+1
#                         break
#     return qte_pares


# print("Quantidade de pares: ",sockMerchant(meias, gaveta))

tamanho = 7
cores = [1,2,1,2,1,3,2]

def sockMerchant(n,vetor):
    pares = 0
    keys = dict.fromkeys(vetor)
    for i in keys:
        for j in range(1,(vetor.count(i))):
            if j%2 == 0:
                pares +=1
    return pares

