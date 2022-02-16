import random as rd

cont = 0
jgn = 0
s = 0
cmi = 'Teste'

while True:
    #Usuario escolhe o valor
    jgn = int(input('Digite um valor: '))
    s += jgn

    #Usuario escolher par ou impar
    jge = str(input('Par ou Impar? [P/I]? ')).strip().upper()[0]
    if jge == 'P':
        cmi == 'I'
    else:
        cmi == 'P'

    #Computador escolher um numero
    cmn = rd.randint(1, 10)
    s += cmn

    #Teste logico

    if s % 2 == 0 and jge == 'P':
        print('Você ganhou')
        cont += 1

    elif s % 2 == 0 and jge == 'I':
        break

    elif s % 2 > 0 and jge == 'P':
        break

    elif s % 2 > 0 and jge == 'I':
        cont += 1
        print('Você ganhou')

print(f'Você ganhou {cont} partidas antes de perder')