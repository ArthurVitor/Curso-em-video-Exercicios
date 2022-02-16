s = 0

for c in range(1, 7):
    num = int(input('Digite o primeiro valor: '))
    if num % 2 == 0:
        s += num
print(f'A soma total dos numeros pares foi de {s}')