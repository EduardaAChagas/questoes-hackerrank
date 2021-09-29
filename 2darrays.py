
def somando(arr, row, col):
    sum = 0
    sum = sum+arr[row-1][col-1]
    sum = sum+arr[row-1][col]
    sum = sum+arr[row-1][col+1]
    sum = sum+arr[row][col]
    sum = sum+arr[+1][col-1]
    sum = sum+arr[row+1][col]
    sum = sum+arr[row+1][col+1]
    return sum

def hourglassSum(arr):
    max = -63
    for i in range (1,5):
        for j in range(1,5):
            somatual = somando(arr,i,j)
            if somatual>=max:
                max = somatual
    return max


