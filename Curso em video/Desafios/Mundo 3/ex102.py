
def fac(num, s):
    if s == 1:
        f = 1
        for c in range(num, 0, -1):
            f *= c
            print(f'{num} * {c} = {f}')
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f


esl = int(input('Digite o numero: '))
esl1 = int(input('Digite o numero magico: '))
print(f'A forma fatorial de {esl} é de {fac(esl, esl1)}')