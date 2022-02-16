fid18 = 0
idd18 = 0
hm = 0


while True:
    esl = str(input('Deseja adicionar mais uma pessoa? ')).strip().upper()[0]
    if esl == 'S':
        idd = int(input('Qual a idade da pessoa? '))
        sx = str(input('Qual seu sexo? '))
        if idd < 18 and sx == 'F':
                fid18 += 1

        elif idd >= 20:
            idd18 += 1

        elif sx == 'M':
            hm += 1
    else:
        break

print(f'Existem {fid18} mulheres menores de 18 anos \n'
      f'Existem {idd18} pessoas maiores de 18 anos \n'
      f'Existem {hm} homems cadastrados')