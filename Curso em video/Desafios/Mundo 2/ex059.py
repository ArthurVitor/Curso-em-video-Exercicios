#Recebe os numeros
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))


#Mostra o menu de opções até o usuario escolher uma das opções
esl = 0
while esl !=  1 or 2 or 3 or 4 or 5:
    print('')
    print('O que você deseja fazer com os valores? \n'
          '[1] Somar \n'
          '[2] Multiplicar \n'
          '[3] Maior \n'
          '[4] Novos valores \n'
          '[5] Fechar')
    esl = int(input('Escolha uma das opções: '))
    print('')

#Efetua o teste logico
    if esl == 1:
        print(f'A soma dos valores foi de {num1 + num2}')
    elif esl == 2:
        print(f'O resultado da multiplicação dos valores foi de {num1 * num2}')
    elif esl == 3:
        print(f'O maior valor foi de {max(num1, num2)}')
    elif esl == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif esl == 5:
        quit()