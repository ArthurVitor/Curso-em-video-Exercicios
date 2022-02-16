import random

nmc = random.randint(0, 5)
esl = int(input('Tente adivinhar o numero que eu pensei! '))
if esl == nmc:
    print('Você acertou!')
else:
    print('Você errou')