lista = [[],[]] #Lista[0] é para valores impares; Lista[1] é para valores pares
for c in range(0, 8):
    num = int(input('Digite o numero: '))
    if num % 2 == 0:
        lista[1].append(num)
    else:
        lista[0].append(num)
print(f'Valores impares em forma crescente {sorted(lista[0])} \n'
      f'Valores pares em forma crescente {sorted(lista[1])}')