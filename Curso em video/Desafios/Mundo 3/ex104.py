def leiaint():
    while True:
        num = input('Digite um numero inteiro: ').set
        if num not in '1234567890':
            num = input('Digite um numero inteiro valido: ')
        else:
            break


if __name__ == '__main__':
    leiaint()