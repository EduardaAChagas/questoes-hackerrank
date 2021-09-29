a = [1,2,3]
b = [3,2,1]

c = [17,28,30]
d = [99,16,8]


def compareTriplets(a, b):
    ar =[0,0]
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice=alice+1
        elif a[i]<b[i]:
            bob=bob+1
    ar = [alice,bob]
    return ar

print(compareTriplets(c,d))