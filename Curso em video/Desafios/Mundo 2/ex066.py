s = cont = 0
while True:
    num = int(input('Digite um numero \n'
                    'Condição de parada [999]: '))
    if num == 999:
        print(f'Soma total foi de {s} e foram digitados {cont} numeros')
        break
    else:
        cont += 1
        s += num