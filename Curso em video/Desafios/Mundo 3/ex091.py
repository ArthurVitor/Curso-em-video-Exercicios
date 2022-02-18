import random, operator


jg = {'jogador1': random.randint(1, 6),
      'jogador2': random.randint(1, 6),
      'jogador3': random.randint(1, 6),
      'jogador4': random.randint(1, 6)}

rank = {}

print(f'Valores sorteados: ')
for k, v in jg.items():
    print(f'{k} tirou {v}')

rank = sorted(jg.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')