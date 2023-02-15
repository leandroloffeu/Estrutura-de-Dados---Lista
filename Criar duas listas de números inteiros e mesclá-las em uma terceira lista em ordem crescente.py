lista1 = []
lista2 = []

while True:
    l1 = int(input('digite um numero para a lista1: '))
    lista1.append(l1)
    l2 = int(input('digite um numero oara a lista2: '))
    lista2.append(l2)
    '''l3 = int(input('digite um numero para a lista3: '))
    lista3.append(l3)'''
    v = str(input('deseja encerrar? S(sim) ou n(não): '))
    if v == "s":
        break

lista3 = lista1 + lista2
lista3.sort()
print(lista3)