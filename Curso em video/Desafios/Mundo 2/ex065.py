esl = ' '
nums = []


while esl != 'N':
    nus = int(input('Quantos numeros deseja adicionar? '))
    print('')
    if nus == 0:
        quit()
    else:
        for c in range(0, nus):
            num = int(input('Digite o numero: '))
            nums.append(num)
        print(f'A media dos numeros foi de {(sum(nums)) / len(nums)} ')
        print(f'O maior valor foi {max(nums)} e o menor valor foi {min(nums)}')