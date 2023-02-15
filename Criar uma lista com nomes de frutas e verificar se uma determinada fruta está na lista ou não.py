lista = []

while True:
    v = str(input('digite o nome da fruta ou X para sair: '))
    if v == 'x':
        break
    lista.append(v)
    
print(lista)

c = str(input('digite o nome para conferência: '))
for nome in lista:
    if nome == c:
        print('está na lista!')
    else:
        print('não está na lista')