import random

numeros = []
s = 0

def sorteia():
    global numeros
    while len(numeros) < 5:
        num = random.randint(1, 10)
        numeros.append(num)

def  soma():
    global numeros, s
    for c in numeros:
        if c % 2 == 0:
            s += c
    print(s)
if __name__ == '__main__':
    sorteia()
    soma()
