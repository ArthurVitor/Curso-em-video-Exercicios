import random


lista = []
esl = int(input('Quantos jogos quer sortear? '))
cont = 0
if cont <= esl:
    for c in range(0, esl):
        while len(lista) < 6:
            num = random.randint(1, 60)
            if num in lista:
                num = random.randint(1, 60)
            else:
                lista.append(num)
                if len(lista) == 6:
                    print(f'Lista do {c+1}º jogo; numeros sorteados {lista}')
                    lista.clear()
                    cont += 1
                    break
print('Fim')