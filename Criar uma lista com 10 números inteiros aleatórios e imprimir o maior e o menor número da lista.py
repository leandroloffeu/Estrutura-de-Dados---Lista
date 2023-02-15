lista = []

while True:
    v = int(input('digite o valor para a lista ou 0 para salvar e sair: '))
    if v == 0:
        break
    lista.append(v)
    
print("Lista de números aleatórios: ", lista)

maior = max(lista)
menor = min(lista)
print("Maior número: ", maior)
print("Menor número: ", menor)