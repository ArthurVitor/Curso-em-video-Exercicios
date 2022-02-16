tmp = []
prc = []
mai = men = 0

while True:
    tmp.append(str(input('Nome: ')))
    tmp.append(float(input('Peso: ')))
    if len(prc) == 0:
        mai = men = tmp[1]
    else:
        if tmp[1] > mai:
            mai = tmp[1]
        if tmp[1] < men:
            men = tmp[1]
    prc.append(tmp[:])
    tmp.clear()
    esl = str(input('Quer continuar? ')).strip().upper()[0]
    if esl in 'N':
        break

print(f'Você cadastrou {len(prc)} pessoas')
print(f'O maior peso foi {mai}kg peso de', end='')
for p in prc:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {men}kg peso de', end='')
for p in prc:
    if p[1] == men:
        print(f'{p[0]}', end='')
