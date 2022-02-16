#Recebe o ano de nascimento do atleta
ano = int(input('Digite o seu ano de nascimento! '))

#Calcula a idade do atleta
id = 2022 - ano

#Efetua o teste logico
if id > 0 and id <= 9:
    print('Mirim')
elif id >= 10 and id <= 14:
    print('Infantil')
elif id >= 15 and id <= 19:
    print('Junior')
elif id == 20:
    print('Senior')
elif id > 20:
    print('Master')