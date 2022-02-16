#Recebe o valor do produto e forma de pagamento
vlr = float(input('Valor do produto! '))
pgt = int(input('Qual forma de pagamento? \n'
                'Dinheiro = 1 \n'
                'Cartão a vista = 2 \n'
                '2x no cartão = 3 \n'
                '3x no cartão = 4 \n'
                'Escolha: '))

#Calcula o valor final e efetua o teste logico
if pgt == 1:
    print(f'O total será de R${vlr - (vlr * 0.10)} reais pois você ganhou 10% de desconto devido a forma de pagamento')
elif pgt == 2:
    print(f'O total será de R${vlr - (vlr * 0.05)} reais devido ao desconto de 5% ao pagar a vista no cartão')
elif pgt == 3:
    print(f'O total será de R${vlr} reais!')
else:
    print(f'O total será de R${vlr + (vlr * 0.02)} reais')