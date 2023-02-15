lista = []

while True:
    v = int(input('Digite valor para a lista ou 0 para salvar e sair: '))
    if v == 0:
        break
    lista.append(v)

soma = sum (lista)

print(('A soma dos valores da lista é:'), soma)
