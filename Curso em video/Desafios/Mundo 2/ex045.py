import random

#Maquina escolhe oque jogar!
rnd = random.randint(1, 3)

#Usuario escolhe oque jogar
usr = int(input('Escolha oque jogar! \n'
                'Pedra = 1 \n'
                'Papel = 2 \n'
                'Tesoura = 3 \n'
                'Escolha: '))

#Efetua o teste logico
if rnd == 1:
    if usr == 1:
        print('Empate')
    elif usr == 2:
        print('Ganhou')
    else:
        print('Perdeu')

elif rnd == 2:
    if usr == 1:
        print('Perdeu')
    elif usr == 2:
        print('Empate')
    else:
        print('Ganhou')
else:
    if usr == 1:
        print('Ganhou')
    elif usr == 2:
        print('Perdeu')
    else:
        print('Empate')