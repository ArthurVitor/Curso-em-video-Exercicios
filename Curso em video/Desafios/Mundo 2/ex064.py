cont = 0
s = 0
num = 0


while num != 999:
        cont += 1
        num = int(input('Digite o numero: '))
        if num != 999:
            s += num
        else:
            print(f'Soma total foi de {s} e tiveram {cont} numeros no total')
            quit()