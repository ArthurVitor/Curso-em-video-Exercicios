lista = []

for c in range(1, 6):
    kg = int(input('Digite seu peso: '))
    lista.append(kg)
print(f'O maior peso da sequencia foi {max(lista)} e o menor foi de {min(lista)}')