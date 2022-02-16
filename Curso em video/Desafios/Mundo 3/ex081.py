lista = []
cont = 0

while True:
    cont += 1
    lista.append(int(input('Digite o primeiro numero: ')))
    esl = str(input('Deseja continuar? ')).strip().upper()[0]
    if esl == 'N':
        break
print(f'O total de numeros digitados foi de {cont} \n'
      f'Os numeros digitados em forma decrescente ficam {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O numero 5 está na lista na posição {lista.index(5)}')
else:
    print('O numero 5 não está na lista')