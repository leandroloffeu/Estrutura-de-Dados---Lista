lista = []

while True:
    pessoas = str(input('Digite um nome ou x para sair: '))
    if pessoas == 'x':
        break
    lista.append(pessoas)

print(lista)
print('Primeiro nome da lista:', lista[0])
print('Último nome da lista:', lista[-1])    