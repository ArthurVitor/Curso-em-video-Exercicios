prim = int(input('Primeiro valor: '))
raz = int(input('Razão: '))
dec = prim + (10 - 1) * raz #Calcula o decimo termo
for c in range(prim, dec + raz, raz):
    print(c)