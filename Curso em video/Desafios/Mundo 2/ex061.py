# prim = int(input('Primeiro valor: '))
# raz = int(input('Razão: '))
# dec = prim + (10 - 1) * raz #Calcula o decimo termo
# for c in range(prim, dec + raz, raz):
#     print(c)
cont = 0

prim = int(input('Digite o valor inicial: '))
raz = int(input('Digite a razão: '))

while cont != 10:
    dec = prim * (raz * 10)
    for c in range(prim, dec, raz):
        cont += 1
        ult = c
        print(c)