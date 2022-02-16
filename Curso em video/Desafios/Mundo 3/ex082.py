lista = []
impar = []
par = []

while True:
    lista.append(int(input('Digite o numero: ')))
    esl = str(input('Deseja continuar? ')).strip().upper()[0]
    if esl == 'N':
        break

for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Todos os numeros digitados {sorted(lista)} \n'
      f'Todos os numeros impares {sorted(impar)} \n'
      f'Todos os numeros pares {sorted(par)}')