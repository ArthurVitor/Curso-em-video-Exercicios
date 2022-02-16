frase = str(input('Digite uma frase para verificar se é um palindromo: ')).lower()
if frase[::-1] == frase:
    print('É um palindromo')
else:
    print('Não é um palindromo')