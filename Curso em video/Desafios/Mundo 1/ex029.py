esl = int(input('Digite a velocidade do carro! '))
if esl > 80:
    print(f'Você está acima da velocidade (80km/h) permitida!\n'
          f'Terá que pagar uma multa de R$ {(esl-80) * 7} reais')
else:
    print('Tudo ok')