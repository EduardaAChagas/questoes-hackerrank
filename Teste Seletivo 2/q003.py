def removeNodes(listHead,x):
    while (listHead is not None) and (listHead.data > x):
        listHead = listHead.next
    
    corrente = listHead

    while (corrente is not None) and (corrente.next is not None):
        if(corrente.next.data > x):
            corrente.next = corrente.next.next
        else:
            corrente = corrente.next

    
    return listHead 

cabeca = [5, 10, 11, 12, 4]
x = 5
print(cabeca)
removeNodes(cabeca, x)
print(cabeca)