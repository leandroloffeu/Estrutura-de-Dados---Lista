lista = []
while True:
    nome = str(input('digite um nome ou x para sair: '))
    if nome == 'x':
        break
    else:
        lista.append(nome)
lista.sort()
print(lista)