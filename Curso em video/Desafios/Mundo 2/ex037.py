num = int(input('Digite um numero inteiro! '))
esl = int(input('Para qual valor você deseja converter? \n'
                '1 para Binario \n'
                '2 para Octal \n'
                '3 para hexadecimal \n'))
if esl == 1:
    print(f'O numero {num} em binario fica {bin(num)}')
elif esl == 2:
    print(f'O numero {num} em octal fica {oct(num)}')
else:
    print(f'O numero {num} em hexadecimal fica {hex(num)}')