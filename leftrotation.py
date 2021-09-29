
def rotLeft(a, d):
    tam = len(a)
    for i in range(d):
        a.append(a[i])
        a.pop(0)
    return a

d = 4
a = [1,2,3,4,5]
print("a orifinal",a)
print("Rortaciones: ",rotLeft(a,d))