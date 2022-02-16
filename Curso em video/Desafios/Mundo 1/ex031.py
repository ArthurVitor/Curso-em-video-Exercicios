dist = int(input('Qual a distancia da viagem? '))
if dist > 0 and dist <= 200:
    print(f'O total da viagem ira ser der R$ {dist * 0.50} reais!')
else:
    print(f'O total da viagem ira ser de R$ {dist * 0.45} reais')