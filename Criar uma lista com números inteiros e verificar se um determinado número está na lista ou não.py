lista=[]

while True:
    n = int (input('digite um valor ou 0 para slavar e sair da lista: '))
    lista.append(n)
    if 0 == n:
        break

print(lista)

while True:
    v = int (input('Digite o valor para verificar: '))
    if v in lista:
      print("Está na lista!")
    else:
      print('Não está na lista')