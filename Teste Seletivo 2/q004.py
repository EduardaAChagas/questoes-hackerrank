
def checar(list):
    print('list: ',list)
    tam = len(list)
    pilha = []
    for i in range(tam):
        if list[i]=='{' or list[i]=='[' or list[i]=='(':
            pilha.append(list[i])
    
        else:
            fechamento = ''
            aux = pilha.pop()
            if aux=='(':
                fechamento = ')'
            elif aux=='[':
                fechamento = ']'
            elif aux=='{':
                fechamento = '}'
            if list[i]!=fechamento:
                return 'NO'
    if len(pilha)==0:
        return 0
    return 1

def braces(values):
    string1 = values[0]
    string2 = values[1]
    list1 = list(string1)
    list2 = list(string2)
    print(checar(list1))
    print(checar(list2))
    if checar(list1):
        return 'YES'
    if not checar(list1):
        return 'NO'
    if checar(list2):
        return 'YES'

teste = ['{[])','{[()]}']
braces(teste)
