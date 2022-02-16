cont = 1
matriz = [[],[],[]]


for c in range(0, 9):

    num = int(input('Digite o numero: '))
    if cont > 0 and cont < 4:
        matriz[0].append(num)
        cont += 1
    elif cont > 3 and cont < 7:
        matriz[1].append(num)
        cont += 1
    else:
        matriz[2].append(num)

for c in range(0,3):
    print(matriz[c])