cont = 1
matriz = [[], [], []]
sp = tot = total = 0
for c in range(0, 9):

    num = int(input('Digite o numero: '))
    if num % 2 == 0:
        sp += num
    if cont > 0 and cont < 4:
        matriz[0].append(num)
        cont += 1
    elif cont > 3 and cont < 7:
        matriz[1].append(num)
        cont += 1
    else:
        matriz[2].append(num)

for c in range(0,3):
    total += matriz[0+c][2]

print(f'A soma de todos os valores pares foi de {sp}')
print(f'A soma dos valores da terceira Coluna foi {total}')
print(f'O maior valor da segunda linha foi {max(matriz[1])}')
