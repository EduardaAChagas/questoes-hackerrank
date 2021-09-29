import numpy
#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# def diagonalDifference(arr):
#     tam = len(arr)
#     diagonal1a = 0
#     for i in range(tam):
#        diagonal1 = diagonal1+arr[i][i]
#     return diagonal1
# matriz = []
# matriz[0][0] = [3]
# matriz[1][0] = [11]
# matriz[1][1] = [2]
# matriz[1][2] = [4]
# matriz[2][0] = [4]
# matriz[2][1] = [5]
# matriz[2][2] = [6]
# matriz[3][0] = [10]
# matriz[3][1] = [8]
# matriz[3][2] = [-12]


def diagp(arr):
    somadiagp = 0
    somadiags = 0
    somatotal = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                somadiagp = somadiagp + arr[i][j]
            if i == (len(arr) -1 -j):
                somadiags = somadiags + arr[i][j]
    somatotal = somadiagp-somadiags
    return abs(somatotal)
arr = [[11,2,4],[4,5,6],[10,8,-12]]
print(diagp(arr))

# arr = [[11,2,4],[4,5,6],[10,8,-12]]
# somadiagp = 0
# somadiags = 0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i==j:
#             somadiagp = somadiagp + arr[i][j]
#         if i == (len(arr) -1 -j):
#             somadiags = somadiags + arr[i][j]

# print("soma da diagonal principal: ", somadiagp)
# print("soma da diagonal secundaria: ", somadiags)