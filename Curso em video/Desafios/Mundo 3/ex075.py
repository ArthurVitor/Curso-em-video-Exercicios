num = (int(input('Primeiro numero: ')),
       int(input('Segundo valor: ')),
       int(input('Terceiro valor: ')),
       int(input('Quarto valor: ')))
print(f'Os numeros digitados foram {num}\n'
      f'O valor 9 foi digitado {num.count(9)} vezes')
if 3 not in num:
    print('O numero 3 não foi digitado em nenhuma posição')
else:
    print(f'O numero 3 foi digitado na posição {num.index(3)}')
print('Os valores pares digitados foram: ', end=' ')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')