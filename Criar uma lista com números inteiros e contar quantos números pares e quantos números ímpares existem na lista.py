par = []
impar = []
while True:
    n1 = int(input('digite um nome ou 0 para salvar e sair: '))
    if n1 == 0:
        break
    elif (n1%2)==0:
         par.append(n1)
    else:
        impar.append(n1) 
print(f'A quantidade de numeros pares digitados foi: {len(par)}')
print(f'A quantidade de numeros impares digitados foi: {len(impar)}')