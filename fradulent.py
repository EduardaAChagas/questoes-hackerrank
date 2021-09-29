import statistics
from collections import deque
import math
import bisect


def med(arr,d,m):
    if d%2==0:
        return int(statistics.median(arr)+1)
    else:
        return int(statistics.median(arr))

def fraudulent(a,d):
    aux = a[0:d]
    aux.sort()
    meio = d//2
    cont = 0
    n =  len(a)
    for i in range(d,n):
        if a[i]>=2*med(aux,d,meio):
            print('aux: ',a[i])
            cont = cont+1
        print(aux)
        del aux[bisect.bisect_left(aux,a[i-d])]
        print(aux)
        bisect.insort(aux,a[i])
        print(aux)
    return cont

a = [10,20,30,40,50]
d = 3
def activityNotifications(expenditure, d):
    notification = 0
    d_next = d+1
    for i in range(len(expenditure) - 1):
        exp_mini = expenditure[i:i + d]
        days_value = expenditure[i:i+d_next]
        if len(exp_mini) == d:
            if days_value[len(days_value) - 1] >= 2*(statistics.median(exp_mini)):
                notification+=1
    return notification
    
print('Total de notificações: ', activityNotifications(a,d))