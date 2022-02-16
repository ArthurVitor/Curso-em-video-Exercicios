numlist = []
maior = 0
menor = 0
for c in range(0, 5):
    numlist.append((int(input('Digite o numero: '))))
    if c == 0:
        maior = menor = numlist[c]
    else:
        if numlist[c] > maior:
            maior = numlist[c]
        if numlist[c] > menor:
            menor = numlist[c]

print(f'Valores da lista {numlist}')
print(f'O maior valor da lista foi {maior} nas posições ', end='')
for i, v in enumerate(numlist):
    if v == maior:
        print(f'{i} ->', end='')
print()
print(f'O menor valor da lista foi {menor} nas posições ', end='')
for i, v in enumerate(numlist):
    if v == menor:
        print(f'{i} ->', end='')
