notas = []
while True:
    n = int(input('Digite um valor para a lista ou 0 para salvar e sair: '))
    notas.append(n)
    if n == 0:
        break
print(notas)
v=int(input('digite o valor da lista para remover: '))
notas.remove(v)
print(notas)