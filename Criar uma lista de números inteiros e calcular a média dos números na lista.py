lista = []

while True:
    v = int(input('Digite o valor ou 0 para salvar e fechar: '))
    lista.append(v)
    if v == 0:
        break
    

print('Numeros da lista', lista)
total = len(lista)
soma = sum(lista)
media = soma/total

print('Quantidade de numeros da lista', total)
print('Soma de muneros da lista', soma)
print('Média dos números da lista', media)