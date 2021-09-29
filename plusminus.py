arr = [-4, 3, -9, 0, 4, 1]
aize = 6

def plusMinus(arr):
    size = len(arr)
    positive, zero, negative = 0, 0, 0
    for i in range(len(arr)):
        if arr[i]>0:
            positive = positive+1
        elif arr[i]<0:
            negative = negative+1
        else:
            zero = zero+1
    positive = positive/size
    negative = negative/size
    zero = zero/size
    print('%.6f'%positive)
    print('%.6f'%negative)
    print('%.6f'%zero)

plusMinus(arr)