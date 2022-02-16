import random
cont = 0


#Computador pensa no numero
cmp = random.randint(1, 10)
print(cmp)

#Jogador tenta advinhar o numero até acertar
jgd = int(input('Tente advinhar o numero! '))
while jgd != cmp:
    cont += 1
    jgd = int(input('Tente novamente: '))
print(f'Você precisou de {cont} tentativas para acertar o numero!')