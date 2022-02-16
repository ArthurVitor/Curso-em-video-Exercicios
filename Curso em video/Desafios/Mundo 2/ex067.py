while True:
    print('_______________________________________________')
    num = int(input('Quer ver a tabuada de qual valor?: '))
    print('_______________________________________________')
    if num < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{num} * {c} = {num*c}')