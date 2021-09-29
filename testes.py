d = 3
ar = [1,2,3,4,5]
aux = ar[d:]
print(7/4)
print(7//4)


def activityNotifications(a,d):
    aux = a[:d]
    aux = deque(aux)
    c = 0
    median = statistics.median(aux)
    n = len(a)
    for i in range(d,n-1):
        if a[i]>=2*median:
            c+=1
        aux.popleft()
        aux.append(a[i])
        median = statistics.median(aux)
    return c