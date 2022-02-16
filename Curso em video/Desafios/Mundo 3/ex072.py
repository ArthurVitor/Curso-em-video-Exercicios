nus = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

esl = -1
while True:
    if esl < 0 or esl > 20:
        esl = int(input('Digite um numero valido: '))
    else:
        print(f'Você digitou o numero {nus[esl]}')
        break
print('Fim')