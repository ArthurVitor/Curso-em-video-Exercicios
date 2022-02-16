s = 0
n = 0

for c in range(1, 8):
    an = int(input('Digite seu ano de nascimento: '))
    if 2022 - an >= 21:
        s += 1
    else:
        n += 1
print(f'{s} pessoas ja atingiram a maior idade e {n} não atingiram')